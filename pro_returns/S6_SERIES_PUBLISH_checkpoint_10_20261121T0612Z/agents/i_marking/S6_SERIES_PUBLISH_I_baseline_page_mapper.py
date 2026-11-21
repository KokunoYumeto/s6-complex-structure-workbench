#!/usr/bin/env python3
"""Read-only baseline locators from a pinned PDF, its source, and its tag index.

Writes a separate old-side receipt and summary TSV. It never rewrites the defect
TSV, TeX, PDF, or root mapper. Named destinations supply start loci only. Unique
literal prose fragments supply selected-phrase pages, never full proof bounds.
"""
from pathlib import Path
from datetime import datetime, timezone
import argparse,bisect,collections,csv,hashlib,json,re
import fitz
csv.field_size_limit(100_000_000)
ROOT=Path(__file__).resolve().parents[2]
DEFAULT_PDF_SHA='e4a7f4abd0e21a776e8ec0d1ab7e643d2346493465782c91ac5b1832fa69daba'
REPLACEMENTS={'\ufb00':'ff','\ufb01':'fi','\ufb02':'fl','\ufb03':'ffi','\ufb04':'ffl','\u2018':"'",'\u2019':"'",'\u201c':'"','\u201d':'"','\u2013':'--','\u2014':'---','\u00ad':''}

def sha_bytes(b):return hashlib.sha256(b).hexdigest()
def digest(p):return sha_bytes(Path(p).read_bytes())
def canonical_text(s):
    for a,b in REPLACEMENTS.items():s=s.replace(a,b)
    return re.sub(r'\s+',' ',s).strip()
def mask_comments(s):
    chars=list(s);i=0
    while i<len(s):
        if s[i]=='%':
            j=i-1;n=0
            while j>=0 and s[j]=='\\':j-=1;n+=1
            if n%2==0:
                end=s.find('\n',i)
                if end<0:end=len(s)
                for j in range(i,end):chars[j]=' '
                i=end;continue
        i+=1
    return ''.join(chars)
def group(s,i):
    while i<len(s) and s[i].isspace():i+=1
    if i>=len(s) or s[i]!='{':return None,i
    start=i+1;depth=1;i+=1
    while i<len(s) and depth:
        escaped=(i>0 and s[i-1]=='\\')
        if s[i]=='{' and not escaped:depth+=1
        elif s[i]=='}' and not escaped:depth-=1
        i+=1
    return (s[start:i-1],i) if depth==0 else (None,i)
def ranges(values):
    groups=[]
    for n in sorted(set(values)):
        if groups and n==groups[-1][-1]+1:groups[-1].append(n)
        else:groups.append([n])
    return ', '.join(str(x[0]) if len(x)==1 else f'{x[0]}–{x[-1]}' for x in groups)
def row_fingerprint(row):
    return sha_bytes(json.dumps(row,sort_keys=True,ensure_ascii=False,separators=(',',':')).encode())
def identity_candidates(row):
    sid=row.get('statement_id','');out=[sid]+[x.strip() for x in sid.split(',')]
    out += [x.split()[0] for x in sid.split(',') if x.split()]
    for key in ('old_text','new_text'):
        out += re.findall(r'\\(?:StatementRecord|label)\{([^}]+)\}',row.get(key,''))
    out += re.findall(r'\\(?:c|C)?ref\{([^}]+)\}',row.get('new_location',''))
    return list(dict.fromkeys(x for x in out if x))

class Baseline:
    def __init__(self,pdf,source,tags,paper):
        self.pdf=Path(pdf);self.source=Path(source);self.tags=Path(tags)
        self.source_bytes=self.source.read_bytes();self.text=self.source_bytes.decode();self.clean=mask_comments(self.text)
        self.docstart=self.clean.index(r'\begin{document}')
        self.line_starts=[0]+[m.end() for m in re.finditer('\n',self.text)]
        self.doc=fitz.open(self.pdf);self.names=self.doc.resolve_names()
        self.page_text=[];self.footers={};self.word_pages=collections.defaultdict(set)
        for i,page in enumerate(self.doc):
            blocks=page.get_text('blocks');candidates=[b for b in blocks if b[1]>page.rect.height-70 and re.fullmatch(r'\d+',b[4].strip())]
            footer=max(candidates,key=lambda b:b[3])[4].strip() if candidates else None
            self.footers[i+1]=footer
            text=canonical_text(page.get_text())
            self.page_text.append(text)
            for word in set(re.findall(r'\b[A-Za-z][A-Za-z\'-]{2,}\b',text)):
                self.word_pages[word].add(i+1)
        self.phrase_cache={};self.labels={};self.anchors=[];self.tag_audit=[]
        self.source_labels={m[1]:m.start() for m in re.finditer(r'\\label\{([^}]+)\}',self.clean) if m.start()>self.docstart}
        source_tags={m[1]:m for m in re.finditer(r'\\hypertarget\{(tag-[^}]+)\}\{\}',self.clean) if m.start()>self.docstart}
        tagrows=[r for r in csv.DictReader(self.tags.open(),delimiter='\t') if r['paper']==paper]
        for row in tagrows:
            name='tag-'+row['tag'];entry=self.names.get(name);m=source_tags.get(name)
            rec={'label':row['label'],'tag':name,'index_page':row['page'],'source_label_present':row['label'] in self.source_labels,'source_tag_present':bool(m),'destination_present':bool(entry)}
            if entry and m and entry.get('page',-1)>=0:
                pdfpage=entry['page']+1;printed=self.footers[pdfpage]
                rec.update(pdf_page=pdfpage,printed_page=printed,index_agrees=(str(row['page'])==str(printed)))
                anchor={'name':name,'label':row['label'],'number':row['number'],'kind':row['kind'],'position':m.start(),'end_position':m.end(),'source_line':self.line(m.start()),'pdf_page':pdfpage,'printed_page':printed,'basis':'source hypertarget + actual PDF named destination + attached tag-index agreement','destination':entry}
                self.anchors.append(anchor)
                if row['label'] in self.source_labels:self.labels[row['label']]=anchor
            self.tag_audit.append(rec)
        self.section_audit=[]
        toc_by_title=collections.defaultdict(list)
        for level,title,page,info in self.doc.get_toc(simple=False):
            stripped=re.sub(r'^[A-Za-z0-9]+(?:\.[A-Za-z0-9]+)*\s+','',title)
            toc_by_title[canonical_text(stripped)].append((level,title,page,info))
        for m in re.finditer(r'\\((?:sub)*section)\*?\s*\{',self.clean[self.docstart:]):
            pos=self.docstart+m.start();brace=self.docstart+m.end()-1;title,end=group(self.clean,brace)
            if title is None or re.search(r'[\\${}]',title):continue
            matches=toc_by_title.get(canonical_text(title),[])
            if len(matches)!=1:continue
            level,toc_title,page,info=matches[0];name=info.get('nameddest');entry=self.names.get(name)
            if not entry or entry.get('page',-1)<0 or entry['page']+1!=page:continue
            anchor={'name':name,'label':'','number':'','kind':'section','title':title,'position':pos,'end_position':end,'source_line':self.line(pos),'pdf_page':page,'printed_page':self.footers[page],'basis':'exact plain source heading title + unique PDF bookmark + actual named destination','destination':entry}
            self.anchors.append(anchor);self.section_audit.append({'source_title':title,'bookmark_title':toc_title,'name':name,'pdf_page':page})
            cluster=re.match(r'(?:\s|\\label\{[^{}]+\}|\\hypertarget\{tag-[^{}]+\}\{\})*',self.clean[end:]).group(0)
            for label in re.findall(r'\\label\{([^}]+)\}',cluster):self.labels.setdefault(label,dict(anchor,label=label))
        # Aliases are associated only through an adjacent sequence of label/target commands.
        taganchors=sorted([a for a in self.anchors if a['name'].startswith('tag-')],key=lambda x:x['position'])
        positions=[a['position'] for a in taganchors]
        for label,pos in self.source_labels.items():
            if label in self.labels:continue
            i=bisect.bisect_right(positions,pos)-1
            if i<0:continue
            anchor=taganchors[i];between=self.clean[anchor['end_position']:pos]
            if re.fullmatch(r'(?:\s|\\label\{[^{}]+\}|\\hypertarget\{tag-[^{}]+\}\{\})*',between):
                self.labels[label]=dict(anchor,label=label,basis='adjacent original-source alias label + actual PDF named destination')
        for m in re.finditer(r'\\bibitem(?:\[[^\]]*\])?\{([^}]+)\}',self.clean):
            if m.start()<self.docstart:continue
            name='cite.'+m[1];entry=self.names.get(name)
            if not entry or entry.get('page',-1)<0:continue
            page=entry['page']+1;anchor={'name':name,'label':'bibliography:'+m[1],'number':'','kind':'bibliography entry','position':m.start(),'end_position':m.end(),'source_line':self.line(m.start()),'pdf_page':page,'printed_page':self.footers[page],'basis':'original source bibitem + actual PDF citation destination','destination':entry}
            self.anchors.append(anchor);self.labels[anchor['label']]=anchor
        entry=self.names.get('Doc-Start')
        if entry and entry.get('page',-1)>=0:
            page=entry['page']+1;self.anchors.append({'name':'Doc-Start','label':'document-start','number':'','kind':'document start','position':self.docstart,'end_position':self.docstart,'source_line':self.line(self.docstart),'pdf_page':page,'printed_page':self.footers[page],'basis':'begin document + actual Doc-Start destination','destination':entry})
        self.anchors.sort(key=lambda a:a['position']);self.positions=[a['position'] for a in self.anchors]
    def line(self,pos):return bisect.bisect_right(self.line_starts,pos)
    def spans(self,text):
        if not text:return []
        out=[];pos=0
        while True:
            start=self.text.find(text,pos)
            if start<0:return out
            out.append((start,start+len(text)));pos=start+max(1,len(text))
    def phrase_candidates(self,text):
        clean=mask_comments(text);candidates=[]
        for m in re.finditer(r'[A-Za-z][A-Za-z0-9 ,.;:\'"()?!/\-\n\r\t]*',clean):
            raw=m.group(0);words=list(re.finditer(r'\S+',raw))
            if len(words)<7:continue
            windows=[(0,min(len(words),32))]
            if len(words)>32:windows.append((max(0,len(words)-32),len(words)))
            for a,b in windows:
                lo=words[a].start();hi=words[b-1].end();phrase=canonical_text(raw[lo:hi]).strip(' ,.;:')
                if len(phrase)>=45 and len(phrase.split())>=7:candidates.append((m.start()+lo,phrase))
        candidates=list(dict.fromkeys(candidates))
        selected=candidates[:4]+candidates[-4:]+sorted(candidates,key=lambda x:len(x[1]),reverse=True)[:8]
        return sorted(set(selected))
    def locate_phrase(self,phrase):
        if phrase in self.phrase_cache:return self.phrase_cache[phrase]
        words=set(re.findall(r'\b[A-Za-z][A-Za-z\'-]{2,}\b',phrase))
        if not words or any(w not in self.word_pages for w in words):result=[]
        else:
            rare=sorted(words,key=lambda w:len(self.word_pages[w]));pages=set.intersection(*(self.word_pages[w] for w in rare[:5]))
            result=[]
            for page in sorted(pages):
                text=self.page_text[page-1];start=0
                while True:
                    at=text.find(phrase,start)
                    if at<0:break
                    result.append({'pdf_page':page,'printed_page':self.footers[page],'text_offset_after_declared_map':at});start=at+len(phrase)
        self.phrase_cache[phrase]=result
        return result
    def related(self,row,spans):
        out=[]
        for label in identity_candidates(row):
            if label in self.labels:out.append(self.labels[label])
        if not out:
            for a,b in spans:
                if a<self.docstart:continue
                inside=[x for x in self.anchors if a<=x['position']<b]
                if inside:out.extend(inside)
                else:
                    i=bisect.bisect_right(self.positions,a)-1
                    if i>=0:out.append(dict(self.anchors[i],context_only=True))
        unique={a['name']:a for a in out}
        return list(unique.values())
    def map_row(self,row):
        old=row.get('old_text','');spans=self.spans(old);visible=[(a,b) for a,b in spans if a>=self.docstart]
        base={'pages':[],'exact':False,'location':row.get('statement_id',''),'source_match_exact':bool(spans),'source_occurrences':len(spans),'source_line_spans':[[self.line(a),self.line(max(a,b-1))] for a,b in spans],'scope':'location metadata only; no rendered-page reading or mathematical check credit'}
        if 'shared bibliography' in row.get('old_location',''):
            return dict(base,method='shared bibliography metadata',location=row['old_location'])
        if row.get('statement_id')=='preamble' or (spans and not visible) or old.lstrip().startswith(r'\expandafter\def\csname SBack@'):
            return dict(base,method='nonprinting preamble source',location='original preamble/source metadata; no printed phrase page established')
        related=self.related(row,visible)
        fragments=[]
        for offset,phrase in self.phrase_candidates(old):
            matches=self.locate_phrase(phrase)
            if len(matches)==1:
                fragments.append(dict(matches[0],phrase=phrase,old_text_offset=offset))
        pages=sorted({x['pdf_page'] for x in fragments})
        if fragments:
            method='verified unique PDF phrase locus' if visible else 'intermediate or changed wording; verified unchanged PDF phrase locus'
            return dict(base,method=method,pages=pages,printed_pages=[self.footers[p] for p in pages],location='selected literal prose fragment(s) of '+row.get('statement_id',''),phrase_match_exact=True,phrase_scope='The selected phrase(s) occur on these pages. These are not certified complete edit-span or proof bounds.',fragments=fragments,related_baseline_loci=related)
        if row.get('old_location')=='intermediate revision' and not visible:
            return dict(base,method='intermediate revision source-only',location='logged intermediate wording absent from original source; no unique PDF phrase established',related_baseline_loci=related)
        if related:
            pages=sorted({a['pdf_page'] for a in related});context=all(a.get('context_only') for a in related)
            method='preceding authenticated destination context locus' if context else 'authenticated named destination start locus'
            if not visible:method+='; complete logged wording absent from baseline source'
            return dict(base,method=method,pages=pages,printed_pages=[self.footers[p] for p in pages],location='; '.join((a.get('label') or a.get('title') or a['name'])+((' number '+a['number']) if a.get('number') else '') for a in related),destination_scope='Statement, section, bibliography-entry or preceding anchor start locus only; no exact phrase-page claim.',destinations=related)
        return dict(base,method='source-only change',location='no authenticated baseline PDF locus established for '+row.get('statement_id',''))

def load_old_side(receipt_path,pdf,source,rows):
    """Import into a current-SyncTeX mapper; enforce PDF/source AND old-row binding.
    Returns only valid entries keyed by change_id. Missing entries require mapping.
    This avoids constructing an old Document or running old SyncTeX.
    """
    receipt=json.loads(Path(receipt_path).read_text())
    assert receipt['baseline_pdf_sha256']==digest(pdf),'baseline PDF hash mismatch'
    assert receipt['baseline_source_sha256']==digest(source),'baseline source hash mismatch'
    indexed={x['change_id']:x for x in receipt['details']}
    valid={}
    for row in rows:
        item=indexed.get(row['change_id'])
        if item and item['old_text_sha256']==sha_bytes(row.get('old_text','').encode()) and item['statement_id']==row.get('statement_id','') and item['original_old_location']==row.get('old_location',''):
            valid[row['change_id']]=dict(item['old'],reused_from_unchanged_baseline_receipt=True)
    return valid

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--paper',default='I')
    parser.add_argument('--pdf',type=Path,default=ROOT/'build/I_baseline/S6_SERIES_GRIND_I.pdf')
    parser.add_argument('--source',type=Path,default=ROOT.parent/'source/S6_SERIES_GRIND_I.tex')
    parser.add_argument('--tags',type=Path,default=ROOT.parent/'source/S6_SERIES_GRIND_tags.tsv')
    parser.add_argument('--defects',type=Path,default=ROOT/'S6_SERIES_PUBLISH_defects_I.tsv')
    parser.add_argument('--expected-pdf-sha256',default=DEFAULT_PDF_SHA)
    parser.add_argument('--output-prefix',type=Path,default=Path(__file__).with_name('S6_SERIES_PUBLISH_I_baseline_page_mapping'))
    args=parser.parse_args();assert digest(args.pdf)==args.expected_pdf_sha256,'unauthenticated baseline PDF'
    original_defects=args.defects.read_bytes();rows=list(csv.DictReader(original_defects.decode().splitlines(keepends=True),delimiter='\t'))
    assert len({r['change_id'] for r in rows})==len(rows),'duplicate change IDs require explicit handling'
    baseline=Baseline(args.pdf,args.source,args.tags,args.paper)
    details=[]
    for row in rows:
        item=baseline.map_row(row)
        details.append({'change_id':row['change_id'],'statement_id':row.get('statement_id',''),'original_old_location':row.get('old_location',''),'old_text_sha256':sha_bytes(row.get('old_text','').encode()),'new_text_sha256':sha_bytes(row.get('new_text','').encode()),'original_row_sha256':row_fingerprint(row),'old':item})
    methods=collections.Counter(d['old']['method'] for d in details)
    conflicts=[r for r in baseline.tag_audit if r.get('destination_present') and r.get('source_tag_present') and not r.get('index_agrees')]
    source_snapshot_stable=digest(args.source)==sha_bytes(baseline.source_bytes)
    defects_snapshot_stable=args.defects.read_bytes()==original_defects
    receipt={'created_utc':datetime.now(timezone.utc).isoformat(),'paper':args.paper,'baseline_pdf':str(args.pdf),'baseline_pdf_sha256':digest(args.pdf),'baseline_source':str(args.source),'baseline_source_sha256':sha_bytes(baseline.source_bytes),'tag_index':str(args.tags),'tag_index_sha256':digest(args.tags),'defect_input':str(args.defects),'defect_input_sha256':sha_bytes(original_defects),'rows':len(rows),'pdf_pages':len(baseline.doc),'pdf_named_destinations':len(baseline.names),'source_bound_tag_destinations':sum(bool(x.get('destination_present') and x.get('source_tag_present')) for x in baseline.tag_audit),'tag_index_destination_mismatches':conflicts,'printed_footer_audit':{'pages_with_numeric_footer':sum(v is not None for v in baseline.footers.values()),'all_printed_pages_equal_one_based_pdf_pages':all(str(k)==v for k,v in baseline.footers.items())},'source_heading_bookmark_matches':len(baseline.section_audit),'historical_mapping_methods':dict(methods),'text_comparison_map':{'replacements':REPLACEMENTS,'whitespace':'Every maximal Unicode whitespace run maps to one ASCII space; leading/trailing whitespace is removed.','case':'unchanged','mathematical_macros':'not converted','line_end_hyphen_removal':'not performed'},'coverage':{'rows_with_verified_phrase_loci':sum(bool(d['old'].get('fragments')) for d in details),'rows_with_destination_loci':sum(bool(d['old'].get('destinations')) for d in details),'rows_without_page_claim':sum(not d['old']['pages'] for d in details)},'source_snapshot_stable':source_snapshot_stable,'defect_snapshot_stable_during_run':defects_snapshot_stable,'certified':False,'math_check_credit':False,'rendered_page_reading_credit':False,'scope':'Read-only old-side locations. Named destinations are statement/section/entry start or preceding context loci. Unique literal prose matches certify only selected fragment pages. Intermediate wording absent from baseline remains source-only unless a unique unchanged phrase is directly found. No defect source or root mapper is modified.','details':details}
    out=args.output_prefix.with_suffix('.json');out.write_text(json.dumps(receipt,indent=2,ensure_ascii=False,default=str)+'\n')
    audit=args.output_prefix.with_name(args.output_prefix.name+'_destination_audit.json');audit.write_text(json.dumps({'tag_rows':baseline.tag_audit,'heading_matches':baseline.section_audit,'footer_pages':baseline.footers},indent=2,ensure_ascii=False)+'\n')
    table=args.output_prefix.with_suffix('.tsv')
    with table.open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=['change_id','statement_id','baseline_pdf_pages','baseline_printed_pages','method','source_match_exact','selected_phrase_count','location','old_text_sha256'],delimiter='\t',lineterminator='\n');writer.writeheader()
        for d in details:
            item=d['old'];writer.writerow({'change_id':d['change_id'],'statement_id':d['statement_id'],'baseline_pdf_pages':ranges(item['pages']),'baseline_printed_pages':', '.join(item.get('printed_pages',[])),'method':item['method'],'source_match_exact':item['source_match_exact'],'selected_phrase_count':len(item.get('fragments',[])),'location':item['location'],'old_text_sha256':d['old_text_sha256']})
    print(json.dumps({k:v for k,v in receipt.items() if k not in ['details','text_comparison_map']},indent=2))
    print('receipt='+str(out))
    print('receipt_sha256='+digest(out))
    assert source_snapshot_stable,'original source changed while reading; rerun'
    # A concurrent root edit is reported, never reverted or written over.
if __name__=='__main__':main()
