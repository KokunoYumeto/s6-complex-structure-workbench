"""Exact, logged TeX edits; mathematical labels and permanent targets are invariants."""
from pathlib import Path
import csv, hashlib, re, json, datetime, collections
csv.field_size_limit(100_000_000)

ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT.parent/'source'

def labels(text):
    return set(re.findall(r'\\label\{([^}]+)\}',text))

def targets(text):
    return set(re.findall(r'\\hypertarget\{(tag-[^}]+)\}',text))

def block(text, label, proof=True):
    pos=text.index('\\label{'+label+'}')
    heads=list(re.finditer(r'\\begin\{(theorem|proposition|lemma|corollary|definition|remark|maintheorem|cited|computed)\}',text[:pos]))
    m=heads[-1]; start=m.start(); env=m[1]
    end=text.index('\\end{'+env+'}',pos)+len('\\end{'+env+'}')
    if proof:
        after=re.match(r'\s*\\begin\{proof\}',text[end:])
        if after:
            end=text.index('\\end{proof}',end)+len('\\end{proof}')
    return text[start:end]

class Editor:
    def __init__(self,paper):
        self.paper=paper; self.path=ROOT/f'S6_SERIES_PUBLISH_{paper}.tex'
        self.text=self.path.read_text(); self.before=self.text
        self.original=(SOURCE/('S6_series_V_corrected_20261120.tex' if paper=='V' else f'S6_SERIES_GRIND_{paper}.tex')).read_text()
        self.rows=[]
    def record(self,kind,old,new,reason,statement='',old_location='',new_location=''):
        line=self.original[:self.original.find(old)].count('\n')+1 if old and old in self.original else ''
        self.rows.append({'change_id':'','type':kind,'statement_id':statement,
            'old_location':old_location or (f'source line {line}' if line else 'intermediate revision'),
            'old_page':'pending mapping','new_location':new_location or statement,
            'new_page':'pending final build','old_text':old,'new_text':new,'reason':reason,
            'review_status':'applied; final page review pending'})
    def replace(self,old,new,kind,reason,statement='',count=1):
        found=self.text.count(old)
        if found!=count: raise ValueError(f'{statement or kind}: expected {count} exact occurrences, found {found}: {old[:160]!r}')
        self.text=self.text.replace(old,new)
        self.record(kind,old,new,reason,statement)
    def replace_block(self,label,new,kind,reason):
        old=block(self.text,label); self.replace(old,new,kind,reason,label)
    def save(self):
        lost_labels=labels(self.before)-labels(self.text)
        lost_targets=targets(self.before)-targets(self.text)
        if lost_labels or lost_targets:
            raise ValueError(f'Lost labels/targets: {sorted(lost_labels)} / {sorted(lost_targets)}')
        for pattern in (r'\\label\{([^}]+)\}',r'\\hypertarget\{(tag-[^}]+)\}'):
            old_counts=collections.Counter(re.findall(pattern,self.before))
            new_counts=collections.Counter(re.findall(pattern,self.text))
            duplicates={k:n for k,n in new_counts.items() if n>max(1,old_counts[k])}
            if duplicates: raise ValueError(f'New duplicate anchors: {duplicates}')
        path=ROOT/f'S6_SERIES_PUBLISH_defects_{self.paper}.tsv'
        with path.open() as f: rows=list(csv.DictReader(f,delimiter='\t'))
        for row in self.rows:
            row['change_id']=f'{self.paper}-{len(rows)+1:05d}'; rows.append(row)
        self.path.write_text(self.text)
        with path.open('w') as f:
            writer=csv.DictWriter(f,fieldnames=list(rows[0]) if rows else [],delimiter='\t')
            writer.writeheader(); writer.writerows(rows)
        print(json.dumps({'paper':self.paper,'new_edits':len(self.rows),'logged_edits':len(rows),
                          'labels':len(labels(self.text)),'tags':len(targets(self.text)),
                          'sha256':hashlib.sha256(self.text.encode()).hexdigest()}))
