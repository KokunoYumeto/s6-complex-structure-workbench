#!/usr/bin/env python3
"""Generate current check pages, tag locations and inventory overlays from exact inputs.

Reference edges are labelled as such: they do not manufacture a proof check or
an independent evidential route. Historic outcomes and identities stay intact.
"""
from pathlib import Path
import argparse,csv,json,re,hashlib,collections
csv.field_size_limit(100_000_000)
ROOT=Path(__file__).resolve().parents[1]

def rows(p,delimiter='\t'):
    with p.open() as f:return list(csv.DictReader(f,delimiter=delimiter))
def save(p,data,delimiter='\t'):
    fields=list(dict.fromkeys(k for r in data for k in r))
    with p.open('w') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter=delimiter);w.writeheader();w.writerows(data)
def group(s,i):
    while i<len(s) and s[i].isspace():i+=1
    assert s[i]=='{',(i,s[i:i+50])
    start=i+1;level=1;i+=1
    while level:
        if s[i]=='{' and (i==0 or s[i-1]!='\\'):level+=1
        elif s[i]=='}' and (i==0 or s[i-1]!='\\'):level-=1
        i+=1
    return s[start:i-1],i
def auxlabels(p):
    s=p.read_text();out={}
    for m in re.finditer(r'\\newlabel\{',s):
        key,j=group(s,m.end()-1);value,j=group(s,j)
        if key.endswith('@cref'):continue
        fields=[];i=0
        while i<len(value):
            if not value[i:].strip():break
            v,i=group(value,i);fields.append(v)
        out[key]={'number':fields[0] if fields else '', 'page':fields[1] if len(fields)>1 else '',
                  'title':fields[2] if len(fields)>2 else '', 'anchor':fields[3] if len(fields)>3 else ''}
    return out
def remove_macro(s,name,nargs):
    while True:
        m=re.search(r'\\'+name+r'\{',s)
        if not m:return s
        j=m.end()-1
        for _ in range(nargs):_,j=group(s,j)
        s=s[:m.start()]+s[j:]
def refs(s):
    out={x.strip() for g in re.findall(r'\\(?:SeriesRef|Cref|cref|ref|eqref)\*?\{([^}]+)\}',s) for x in g.split(',')}
    for a,b in re.findall(r'\\(?:C|c)refrange\*?\{([^}]+)\}\{([^}]+)\}',s):out.update((a,b))
    return out

p=argparse.ArgumentParser();p.add_argument('paper');p.add_argument('--build',type=Path,required=True);p.add_argument('--certified',action='store_true');a=p.parse_args()
source=ROOT/f'S6_SERIES_PUBLISH_{a.paper}.tex';s=source.read_text();labels=auxlabels(a.build/f'{source.stem}.aux')
pdf=a.build/f'{source.stem}.pdf';pdfsha=hashlib.sha256(pdf.read_bytes()).hexdigest();sourcesha=hashlib.sha256(source.read_bytes()).hexdigest()
build=json.loads((a.build/'build_summary.json').read_text());assert build['source_sha256']==sourcesha
tags=rows(ROOT/'S6_SERIES_PUBLISH_tags.tsv');by_label={r['label']:r for r in tags};events=rows(ROOT/'CHECK_EVENTS.tsv')
by_id=collections.defaultdict(list)
for ev in events:by_id[ev['statement_id']].append(ev)
docstart=s.index('\\begin{document}')
ENV=re.compile(r'\\begin\{(maintheorem|theorem|lemma|proposition|corollary|definition|remark)\}')
statements=[]
for m in ENV.finditer(s,docstart):
    end=s.index('\\end{'+m[1]+'}',m.end())+len('\\end{'+m[1]+'}')
    after=re.match(r'\s*\\begin\{proof\}',s[end:])
    if after:end=s.index('\\end{proof}',end)+len('\\end{proof}')
    region=s[m.start():end];statement_end=region.index('\\end{'+m[1]+'}')
    header=region[:statement_end];primary=re.search(r'\\StatementRecord\{([^}]+)\}',header)
    ls=re.findall(r'\\label\{([^}]+)\}',region)
    if not ls:continue
    sid=primary[1] if primary else ls[0]
    identities=[sid]+[x for x in ls if x!=sid and by_label.get(x,{}).get('kind')=='statement']
    clean=remove_macro(region,'StatementRecord',4)
    match=re.match(r'\\begin\{[^}]+\}(?:\[([^\]]+)\])?',region)
    st={'id':sid,'identities':identities,'labels':ls,'kind':m[1],'title':match[1] or '',
        'tag':re.search(r'\\hypertarget\{tag-([^}]+)\}',header)[1],
        'number':labels.get(sid,{}).get('number',''), 'page':labels.get(sid,{}).get('page',''),
        'line':s.count('\n',0,m.start())+1,'end_line':s.count('\n',0,end)+1,
        'references':sorted(refs(clean)),'start':m.start(),'end':end}
    statements.append(st)
owners={label:st['id'] for st in statements for label in st['labels']}
by_owner={st['id']:st for st in statements}
usedby=collections.defaultdict(set)
for st in statements:
    st['uses']=sorted({owners.get(ref,ref) for ref in st['references']} - {st['id']})
    for ref in st['uses']:usedby[ref].add(st['id'])
outline_by=collections.defaultdict(list)
for m in re.finditer(r'\\hypertarget\{(step-'+re.escape(a.paper)+r'-[^}]+)\}\{\}',s):
    ends=[x for x in (s.find('\\item',m.end()),s.find('\\end{enumerate}',m.end())) if x>=0]
    end=min(ends) if ends else m.end()
    for ref in refs(s[m.end():end]):outline_by[owners.get(ref,ref)].append(m[1])

for tag in tags:
    if tag['paper']!=a.paper:continue
    lab=tag['label']
    if lab in labels:
        tag['number']=labels[lab]['number'];tag['page']=labels[lab]['page']
        tag['current_owner']=owners.get(lab,'');tag['publication_disposition']='current target; original tag identity preserved'
    else:
        tag['publication_disposition']='absent from the supplied corrected source; historical registry identity retained'
        tag['current_owner']=''
save(ROOT/'S6_SERIES_PUBLISH_tags.tsv',tags)

def link(label):
    st=by_owner.get(label);t=by_label.get(label)
    if st:return f"[{a.paper}.{st['number']}](#tag-{st['tag']})"
    if t:return f"[{t['paper']}.{t['number']}](S6_SERIES_PUBLISH_checks_{t['paper']}.md#tag-{t['tag']})"
    return '`'+label+'`'
state='complete for this PDF; later series-wide reference regeneration remains a separate gate' if a.certified else 'current source and reference metadata; final PDF gate pending'
out=[f'# Paper {a.paper}: statement checks and references', '',f'Current review state: **{state}**.', '',
     f'PDF SHA-256: `{pdfsha}`. Source SHA-256: `{sourcesha}`.', '',
     'Every recorded check below keeps its author, effort, method, date and scope. Counts are statement-event associations. A shared evidence group does not become several independent checks. Reference lists are extracted from the current mathematical statements and proofs; a reference edge alone supplies no proof verification. Hidden historical statement-header lists are excluded.', '']
for st in statements:
    for identity in st['identities']:
        t=by_label.get(identity)
        if t:out+=['<a id="tag-'+t['tag']+'"></a>','']
    if st['tag'] not in {by_label.get(i,{}).get('tag') for i in st['identities']}:out+=['<a id="tag-'+st['tag']+'"></a>','']
    out+=[f"## {a.paper}.{st['number']} — {st['title']}",'',f"Kind: {st['kind']}. Page: {st['page']}. Primary identifier: `{st['id']}`.",'',
          'Retained statement identities: '+', '.join('`'+x+'`' for x in st['identities'])+'.','',
          '### Uses and used by','', 'Uses (current explicit references): '+(', '.join(link(x) for x in st['uses']) or 'no other statement referenced')+'.','',
          'Used by (reverse current reference edges): '+(', '.join(link(x) for x in sorted(usedby[st['id']])) or 'no other statement references this result')+'.','',
          'Introductory outline back-links: '+(', '.join('`'+x+'`' for x in sorted(set(outline_by[st['id']]))) or 'none')+'.','',
          '### Check events','']
    selected=[ev for identity in st['identities'] for ev in by_id[identity]]
    counts=collections.Counter(ev['type'] for ev in selected)
    out += ['Recorded association totals: '+('; '.join(f'{n} {k}' for k,n in sorted(counts.items())) or 'no mathematical check event is assigned to this definition or organizational remark')+'.','']
    for j,ev in enumerate(selected,1):
        out += [f"#### {j}. {ev['date']} — {ev['type']}",'',f"Statement scope: `{ev['statement_id']}`. Who: {ev['who']}.",'',
                f"Event: `{ev['event_id']}`. Evidence group: `{ev['evidence_group']}`.",'',ev['outcome'],'',
                f"Source record: `{ev.get('source_file','')}`, row {ev.get('source_row','')}.",'']
current_ids={i for st in statements for i in st['identities']}
historical=[t for t in tags if t['paper']==a.paper and t['kind']=='statement' and t['label'] not in current_ids]
if historical:
    out += ['## Historical statement dispositions','',
            'The following entries were already absent from the supplied corrected Paper V. Their historical identity and events are retained here; they are not counted as printed statements in the current PDF.','']
    for t in historical:
        out += ['<a id="tag-'+t['tag']+'"></a>','',f"### {t['tag']} — `{t['label']}`",'']
        for ev in by_id[t['label']]:out += [f"- {ev['date']}; {ev['type']}; {ev['who']}. {ev['outcome']}",'']
(ROOT/f'S6_SERIES_PUBLISH_checks_{a.paper}.md').write_text('\n'.join(out)+'\n')

inventory=rows(ROOT/'S6_SERIES_PUBLISH_inventory.csv',',');existing={r['label'] for r in inventory}
for st in statements:
    if st['id'] not in existing:
        inventory.append({'paper':a.paper,'label':st['id'],'kind':st['kind'],'status':'definition' if st['kind']=='definition' else 'proved' if st['kind'] not in ('remark',) else 'remark',
                          'tag':st['tag'],'notes':'Numbered during the publication revision; exact content and reasons are in the defect record.'})
for row in inventory:
    if row['paper']!=a.paper:continue
    lab=row['label'];owner=owners.get(lab);row['current_source_sha256']=sourcesha;row['current_pdf_sha256']=pdfsha
    for field in ('writing_state','confidence_state','completion_state','remaining_risk'):
        row.setdefault('received_'+field,row.get(field,''))
    if owner:
        st=by_owner[owner];row.update(current_statement_owner=owner,current_number=st['number'],current_page=st['page'],
            publication_review_status=state,writing_state='publication rewrite and source comparison completed',
            confidence_state='current scoped checks listed individually; no whole-proof independence inferred',
            completion_state='Paper '+a.paper+' gate complete' if a.certified else 'awaiting final rendered-PDF gate',
            uses=';'.join(st['uses']),used_by=';'.join(sorted(usedby[owner])),outline_backlinks=';'.join(sorted(set(outline_by[owner]))))
    else:row.update(current_statement_owner='',publication_review_status='historical disposition; absent from supplied corrected source',
                    completion_state='historical record retained; not a current printed statement')
save(ROOT/'S6_SERIES_PUBLISH_inventory.csv',inventory,',')
receipt={'paper':a.paper,'source_sha256':sourcesha,'pdf_sha256':pdfsha,'printed_environments':len(statements),
         'statement_identifiers':len(current_ids),'certified_flag':a.certified,'historical_absent_statement_ids':[x['label'] for x in historical],
         'scope':'Generated links/metadata only; creates no mathematical check event.'}
(ROOT/'records'/f'S6_SERIES_PUBLISH_{a.paper}_current_metadata.json').write_text(json.dumps(receipt,indent=2)+'\n')
(ROOT/'records'/f'S6_SERIES_PUBLISH_{a.paper}_current_statements.json').write_text(json.dumps(statements,indent=2)+'\n')
print(json.dumps(receipt))
