"""Source-to-print text/equation comparison, not a mathematical proof checker.

The complete original blocks and the actual printed blocks are retained. Only
explicit editorial transformations are used to construct an expected text;
all residual differences are saved for an independent receiving read.
"""
from pathlib import Path
import re, json, csv, hashlib, difflib, sys

D = Path(__file__).resolve().parents[2]
ROOT = D.parent
W = D / 'work/cdp_audit/push_C_retention'
W.mkdir(parents=True, exist_ok=True)
sys.path.insert(0, str(D/'code/editorial'))
from paper_ii_transform import raw_refs, normalize_equations, common_cleanup
from paper_iii_source_aliases import push as source_aliases

def sha(s): return hashlib.sha256(s.encode()).hexdigest()
def expand(path):
    text = []; provenance = []
    for line_number, line in enumerate(path.read_text().splitlines(keepends=True), 1):
        m = re.fullmatch(r'\s*\\input\{([^}]+)\}\s*', line)
        if m:
            child = ROOT/'sources/returns/S6_02_PUSH'/m[1]
            if not child.suffix: child = child.with_suffix('.tex')
            a, b = expand(child); text.extend(a); provenance.extend(b)
        else:
            text.append(line)
            provenance.append({'source_file': str(path.relative_to(ROOT)), 'line': line_number})
    return text, provenance

source_lines, provenance = expand(ROOT/'sources/returns/S6_02_PUSH/sections/C_push.tex')
source = ''.join(source_lines)
(W/'C_push_complete_expansion.tex').write_text(source)
(W/'C_push_expansion_provenance.json').write_text(json.dumps(provenance, indent=2)+'\n')
inventory = list(csv.DictReader((D/'S6_09_PAPERS_inventory.csv').open()))
push_ids = [r['source_id'] for r in inventory if r['source_run']=='S6_02_PUSH']
rows = {r['source_id']: r for r in inventory if r['source_run']=='S6_02_PUSH' and r['source_id'].startswith('C.')}
printed = {paper:(D/f'S6_09_PAPERS_{paper}.tex').read_text() for paper in ['I','II','III']}
aux = {}
for paper in ['I','II','III']:
    s=(D/f'S6_09_PAPERS_{paper}.aux').read_text()
    aux[paper] = {
        'numbers':dict(re.findall(r'\\newlabel\{([^}]+)\}\{\{([^}]+)\}',s)),
        'kinds':dict(re.findall(r'\\newlabel\{([^}]+)@cref\}\{\{\[([^\]]+)\]',s))}

def owned_namespace(s):
    def one(m):
        keys = [x if x.startswith(('maps:','mapsIII:','mapsD:','courseIII:','mapsaudit:','fam:','push:','inv:','cdp:','mapsI:','wb:')) else 'push:'+x for x in m[2].split(',')]
        return '\\'+m[1]+'{'+','.join(keys)+'}'
    return re.sub(r'\\(label|ref|eqref|cref|Cref|autoref)\{([^}]+)\}',one,s)

def expected(s):
    s = owned_namespace(source_aliases(s))
    def heading(m):
        env, title = m[1],m[2]
        q = re.match(r'(C\.\d+\.\d+)\s*(.*)',title,re.S)
        if not q:return m[0]
        title = q[2].strip(' ();:')
        title = re.sub(r'^(?:Proved|Known, with derivation)\)?:?\s*','',title)
        return '\\begin{'+env+'}'+('['+title+']' if title else '')+'\\label{push:src:'+q[1]+'}'
    s = re.sub(r'\\begin\{(theorem|proposition|lemma|corollary|remark|problem)\}\[([^\]]+)\]',heading,s)
    s = raw_refs(s,push_ids,'push:src:')
    s,_ = normalize_equations(s,'pushIII')
    s = common_cleanup(s)
    for label in re.findall(r'\\label\{([^}]+)\}', (ROOT/'sources/returns/S6_02_PUSH/sections/C_closing_cocycle.tex').read_text()):
        s=s.replace('{push:'+label+'}', '{mapsI:closing:'+label+'}')
    available=set(re.findall(r'\\label\{([^}]+)\}',printed['III']))
    for paper in ['I','II']:
        def external(m):
            out=[]
            for key in m[2].split(','):
                if key in aux[paper]['numbers'] and key not in available:
                    kind='Equation' if m[1]=='eqref' else aux[paper]['kinds'].get(key,'result').capitalize()
                    out.append('Paper~'+paper+', '+kind+'~'+aux[paper]['numbers'][key])
                else:out.append('\\'+m[1]+'{'+key+'}')
            return ' and '.join(out)
        s=re.sub(r'\\(ref|eqref|cref|Cref|autoref)\{([^}]+)\}',external,s)
    return s

def remove_balanced_command(s,command):
    pattern = re.compile(r'\\'+re.escape(command)+r'\{')
    while (m:=pattern.search(s)):
        level=1;i=m.end()
        while level:
            if s[i]=='{' and s[i-1]!='\\':level+=1
            elif s[i]=='}' and s[i-1]!='\\':level-=1
            i+=1
        s=s[:m.start()]+s[i:]
    return s

def canonical(s):
    # These removals are presentation/dependency annotations, never proof text.
    s=re.sub(r'(?<!\\)%[^\n]*','',s)
    s=remove_balanced_command(s,'Uses')
    s=re.sub(r'\\label\{[^}]+\}','',s)
    s=re.sub(r'\\(?:sub)*section\*?\{[^\n]+\}\s*','',s)
    s=re.sub(r'\\(?:Verified|AuthorSelfCheck|NeedsCheck|Refuted)\b','',s)
    return re.sub(r'\s+',' ',s).strip()

marks=list(re.finditer(r'\\begin\{(?:theorem|proposition|lemma|corollary|remark|problem)\}\[(C\.\d+\.\d+)\b[^\]]*\]',source))
actual_marks=list(re.finditer(r'\\begin\{(?:theorem|proposition|lemma|corollary|remark|problem)\}(?:\[[^\]]*\])?\\label\{push:src:(C\.\d+\.\d+)\}',printed['III']))
actual_by_id={m[1]:(i,m) for i,m in enumerate(actual_marks)}
records=[]
for i,m in enumerate(marks):
    sid=m[1];stop=marks[i+1].start() if i+1<len(marks) else len(source)
    raw=source[m.start():stop]
    expected_text=expected(raw)
    first=source.count('\n',0,m.start());last=source.count('\n',0,stop)
    pp=provenance[first:last]
    ranges=[]
    for loc in pp:
        if ranges and ranges[-1]['source_file']==loc['source_file'] and ranges[-1]['end_line']+1==loc['line']:
            ranges[-1]['end_line']=loc['line']
        else:ranges.append({'source_file':loc['source_file'],'start_line':loc['line'],'end_line':loc['line']})
    if sid=='C.3.5':
        txt=printed['I'];a=txt.index('\\begin{proposition}[The coherent closing translation]');b=txt.index('\\end{proposition}',a)+len('\\end{proposition}')
        c=txt.index('\\subsection{Re-derivation of Proposition~\\ref{push:src:C.3.5}}');c=txt.index('\\begin{proof}',c);d=txt.index('\\end{proof}',c)+len('\\end{proof}')
        actual=txt[a:b]+'\n'+txt[c:d]
        destination_ranges=[{'paper':'I','start_line':txt.count('\n',0,a)+1,'end_line':txt.count('\n',0,b)+1},{'paper':'I','start_line':txt.count('\n',0,c)+1,'end_line':txt.count('\n',0,d)+1}]
        # This special split is deliberately left as a residual comparison:
        # the independently reviewed I edits have exact numbered references.
    else:
        j,n=actual_by_id[sid];a=n.start();b=actual_marks[j+1].start() if j+1<len(actual_marks) else len(printed['III'])
        # The final body/appendix block ends before a different subject begins.
        if sid in ['C.5.1','C.3.3']:
            nxt=re.search(r'\\section\{',printed['III'][a:]);assert nxt
            b=a+nxt.start()
        actual=printed['III'][a:b]
        destination_ranges=[{'paper':'III','start_line':printed['III'].count('\n',0,a)+1,'end_line':printed['III'].count('\n',0,b)+1}]
    stem=sid.replace('.','_')
    for kind,value in [('original',raw),('expected',expected_text),('printed',actual)]:
        (W/f'{stem}.{kind}.tex').write_text(value)
    e,p=canonical(expected_text),canonical(actual)
    et,pt=e.split(),p.split()
    matcher=difflib.SequenceMatcher(None,et,pt,autojunk=False)
    diffs=[{'operation':tag,'expected_tokens':[a,b],'printed_tokens':[c,d], 'expected':' '.join(et[a:b]),'printed':' '.join(pt[c:d])} for tag,a,b,c,d in matcher.get_opcodes() if tag!='equal']
    r={'source_id':sid,'paper':rows[sid]['paper'],'printed_label':rows[sid]['printed_label'],
       'source_ranges':ranges,'destination_ranges':destination_ranges,
       'source_sha256':sha(raw),'printed_sha256':sha(actual),
       'raw_source_lines':len(raw.splitlines()),'raw_printed_lines':len(actual.splitlines()),
       'source_proof_environments':raw.count('\\begin{proof}'),'printed_proof_environments':actual.count('\\begin{proof}'),
       'expected_token_count':len(et),'printed_token_count':len(pt),'residual_changes':diffs,
       'artifact_prefix':str((W/stem).relative_to(D)),'review_status':'Residual changes awaiting receiving read.'}
    records.append(r)

(W/'text_comparison.json').write_text(json.dumps({'reader':'GPT-6 Astra (OpenAI, ChatGPT Pro mode)','effort':'Pro','date':'2026-11-17',
    'scope':'Complete source-to-print textual comparison and residual edits; not a new independent mathematical proof audit.',
    'paper_hashes':{p:sha(s)for p,s in printed.items()},'rows':records},ensure_ascii=False,indent=2)+'\n')
for r in records:
    print(r['source_id'],r['raw_source_lines'],r['raw_printed_lines'],len(r['residual_changes']),r['source_proof_environments'],r['printed_proof_environments'])
