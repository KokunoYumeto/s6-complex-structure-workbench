"""Generate per-tag check files, uses/reverse uses, and honest row states."""
from pathlib import Path
from collections import Counter,defaultdict
import csv,json,re
ROOT=Path(__file__).resolve().parents[1]
PAPERS=['I','II','III','IV','V']
csv.field_size_limit(10**9)

def main():
    labeltags=json.loads((ROOT/'analysis/label_tags.json').read_text())
    registry=json.loads((ROOT/'analysis/permanent_tag_registry.json').read_text())
    maps=json.loads((ROOT/'analysis/main_theorems.json').read_text()) if (ROOT/'analysis/main_theorems.json').exists() else {}
    dependencies=json.loads((ROOT/'analysis/dependencies.json').read_text()) if (ROOT/'analysis/dependencies.json').exists() else {}
    backlinks=json.loads((ROOT/'analysis/outline_backlinks.json').read_text()) if (ROOT/'analysis/outline_backlinks.json').exists() else {}
    with (ROOT/'CHECK_EVENTS.tsv').open() as f:events=list(csv.DictReader(f,delimiter='\t'))
    with (ROOT/'S6_SERIES_GRIND_inventory.csv').open() as f:rows=list(csv.DictReader(f))
    columns=list(rows[0])
    for key in ['source_main_or_supporting','series_main_theorems','format_check','layout_check','independent_routes','remaining_risk','assessment_source']:
        if key not in columns:columns.append(key)
        for row in rows:row.setdefault(key,'')
    assessments={}
    assessment_sources={}
    for path in sorted(ROOT.glob('audit_*/**/row_assessments.json')):
        data=json.loads(path.read_text())
        if isinstance(data,dict) and 'assessments' in data:data=data['assessments']
        if isinstance(data,list):data={r['label']:r for r in data}
        for label,assessment in data.items():
            if not isinstance(assessment,dict):continue
            if label in assessments and assessments[label]!=assessment:
                raise ValueError(f'Conflicting row assessments for {label}: {assessment_sources[label]} / {path}')
            assessments[label]=assessment
            assessment_sources[label]=str(path.relative_to(ROOT))
    main_info={};body_to_main=defaultdict(set)
    for paper,data in maps.items():
        for m in data['main_theorems']:
            main_info[m['label']]=dict(m,paper=paper)
            for lab in m['body_labels']+[lab for st in m['steps'] for lab in st['body_targets']]:body_to_main[lab].add(paper+'.'+m['letter'])
            if not any(r['label']==m['label'] for r in rows):
                r={k:'' for k in columns}
                r.update(paper=paper,label=m['label'],source_run='S6_SERIES_GRIND',source_id=paper+'.'+m['letter'],
                    kind='Main theorem',status='proved',main_or_supporting='main',uses='; '.join(m['body_labels']),
                    credited_to='Exact source relationship is stated in the main theorem and §1.4.',
                    notes='Consolidated statement of the identified body conclusions; exact outline and expansion targets in analysis/main_theorems.json.',
                    source_inventory_row='series-main:'+paper+'.'+m['letter'],source_paper=paper,
                    placement_state='main theorem',writing_state='full statement and linked outline assembled',
                    confidence_state='global statement-to-proof assessment in progress',completion_state='pending',
                    check_record=json.dumps(m,ensure_ascii=False))
                rows.append(r)
    tag_events=defaultdict(list);unassigned=[]
    for e in events:
        info=labeltags.get(e['statement_id'])
        if info:tag_events[info['tag']].append(e)
        else:unassigned.append(e)
    tag_rows=defaultdict(list)
    printed={}
    for paper in PAPERS:
        path=ROOT/f'S6_SERIES_GRIND_{paper}.tex'
        if path.exists():
            for label in re.findall(r'\\StatementRecord\{([^}]+)\}',path.read_text()):printed[label]=paper
    current={}
    for paper in PAPERS:
        path=ROOT/f'analysis/current_labels_{paper}.json'
        current[paper]=json.loads(path.read_text()) if path.exists() else {}
    for row in rows:
        lab=row['label'];info=labeltags.get(lab)
        if info:
            row['tag']=info['tag'];row['paper']=info['paper'];tag_rows[info['tag']].append(row)
            row['series_main_theorems']='; '.join(sorted(body_to_main.get(lab,set())))
            if not row['source_main_or_supporting']:row['source_main_or_supporting']=row['main_or_supporting']
            row['main_or_supporting']='main' if lab in main_info else 'supporting'
            evid=tag_events.get(info['tag'],[])
            historical=[e for e in evid if e.get('phase')!='S6_SERIES_GRIND']
            fresh=[e for e in evid if e.get('phase')=='S6_SERIES_GRIND']
            row['check_summary']=f'{len(historical)} retained and {len(fresh)} current typed events; '+', '.join(f'{k}: {n}' for k,n in sorted(Counter(e['type'] for e in evid).items()))
            if lab in printed:
                row['placement_state']='printed in '+printed[lab]
                row['writing_state']='tagged statement and retained proof assembled'
                row['format_check']='automated assembly complete; semantic/outline review in progress'
                row['layout_check']='pending final rendered-PDF inspection'
                row['completion_state']='pending final statement, confidence and layout review'
            if lab in main_info:
                row['confidence_line']='The outline points to the listed full body statements. Their exact checks are inherited by reference; the consolidated scope and remaining risks require the explicit global assessment.'
            elif fresh:
                row['confidence_line']='Current scoped checks are recorded alongside retained evidence; their exact outcomes and unreviewed dependencies control the remaining confidence assessment.'
            elif evid:
                row['confidence_line']='Retained check evidence is preserved with its original method and scope. The receiving-format review contributes no independent proof check.'
            assessment=assessments.get(lab)
            if assessment:
                for field in ['confidence_state','confidence_line','independent_routes','remaining_risk','format_check','layout_check','completion_state']:
                    if field in assessment and assessment[field] is not None:
                        value=assessment[field]
                        row[field]='; '.join(str(v) for v in value) if isinstance(value,list) else str(value)
                row['assessment_source']=assessment_sources[lab]
    # Exact reverse uses of the declared label lists.
    usedby=defaultdict(list)
    for source,targets in dependencies.items():
        for target in targets:
            if source not in usedby[target]:usedby[target].append(source)
    def link(lab):
        info=labeltags.get(lab)
        if not info:return '`'+lab+'`'
        return '['+lab+'](S6_SERIES_GRIND_checks_'+info['paper']+'.md#tag-'+info['tag']+')'
    grouped=defaultdict(dict)
    for tag,rs in tag_rows.items():
        info=labeltags[rs[0]['label']]
        grouped[info['paper']][tag]=(info['canonical_label'],rs)
    for lab,info in labeltags.items():
        if info['kind'] in ['statement','main theorem'] and info['tag'] not in grouped[info['paper']]:
            grouped[info['paper']][info['tag']]=(info['canonical_label'],[])
    per_paper={}
    for paper in PAPERS:
        out=[f'# S6_SERIES_GRIND — Paper {paper} check file\n',
             'Every entry preserves the actual method, date, model and scope of the recorded event. Imported evidence retains its original attribution. Source movement, numbering, compilation and metadata reconciliation supply no new mathematical verification.\n',
             'Current review state: **in progress**. An inherited mathematical status does not imply completion of the present editorial and confidence assessment.\n']
        for tag,(label,rs) in sorted(grouped[paper].items()):
            meta=current.get(paper,{}).get(label,{})
            number=meta.get('number','number pending');page=meta.get('page','page pending')
            out += [f'<a id="tag-{tag}"></a>\n',f'## {tag} — {paper}.{number}\n',f'Label: `{label}`. Page: {page}.\n']
            statuses=sorted({r['status'] for r in rs})
            out.append('Recorded mathematical status: '+('; '.join(statuses) if statuses else 'as stated in the retained body')+'.\n')
            if rs:
                out.append('Inventory source rows: '+', '.join('`'+r['source_inventory_row']+'`' for r in rs)+'.\n')
                reasons=list(dict.fromkeys(r['in_compendium_only_because'] for r in rs if r['in_compendium_only_because']))
                for reason in reasons:out.append('Disposition: '+reason+'\n')
            if label in main_info:
                m=main_info[label]
                out.append('### How we know the consolidated statement\n')
                out.append('Full expansion targets: '+', '.join(link(lab) for lab in m['body_labels'])+'.\n')
                assessment=assessments.get(label,{})
                out.append(assessment.get('confidence_line','Independent routes are recorded at those targets. Each outline step names its exact expansion. Aggregation of the targets does not itself establish the exact consolidated scope.')+'\n')
                risk=assessment.get('remaining_risk','Completion of the explicit statement-to-outline-to-body comparison, the stated source-opening and computational obligations, and final rendered-layout verification.')
                if isinstance(risk,list):risk='; '.join(risk)
                out.append('Remaining risk: '+risk+'\n')
            evid=tag_events.get(tag,[])
            out.append('### Recorded routes and present scope\n')
            for row in rs:
                if row.get('assessment_source'):
                    out.append('Assessment: '+row['confidence_state']+'. '+row['confidence_line']+'\n')
                    out.append('Independent routes: '+(row.get('independent_routes') or 'see the individually scoped events below')+'.\n')
                    out.append('Remaining risk: '+(row.get('remaining_risk') or 'no further risk statement supplied in this scoped assessment')+'\n')
                    out.append('Assessment source: `'+row['assessment_source']+'`. Completion: '+row['completion_state']+'.\n')
            if evid:
                counts=Counter(e['type'] for e in evid)
                out.append('; '.join(f'{n} {kind}' for kind,n in sorted(counts.items()))+'.\n')
                who=list(dict.fromkeys(e['who'] for e in evid))
                out.append('Recorded checkers: '+'; '.join(who)+'.\n')
            else:out.append('No separate event is assigned to this exact tag. Any receiving proof or shared-source relation is named explicitly above and in the inventory.\n')
            out.append(f'<a id="uses-{tag}"></a>\n### Uses and used by\n')
            aliases=[lab for lab,info in labeltags.items() if info['tag']==tag]
            uses=list(dict.fromkeys(lab for alias in aliases for lab in dependencies.get(alias,[])))
            reverse=list(dict.fromkeys(lab for alias in aliases for lab in usedby.get(alias,[])))
            out.append('Uses: '+(', '.join(link(lab) for lab in uses) or 'the definitions and explicit constructions in the proof; external citations remain at their point of use')+'.\n')
            out.append('Used by: '+(', '.join(link(lab) for lab in reverse) or 'no declared label dependency in the current uses lists')+'.\n')
            steps=[step for alias in aliases for step in backlinks.get(alias,[])]
            for p,letter,n,anchor in steps:
                out.append(f'Proves step {n} of Theorem {p}.{letter}: [outline](S6_SERIES_GRIND_{p}.pdf#nameddest={anchor}).\n')
            out.append('### Check events\n')
            for n,event in enumerate(evid,1):
                out += [f'#### {n}. {event["date"]} — {event["type"]}\n',
                        'Who: '+event['who']+'.\n',
                        'Event: `'+event['event_id']+'`; evidence group: `'+event.get('evidence_group','')+'`.\n',
                        'Source: `'+event.get('source_file','')+'`, row '+event.get('source_row','')+'.\n',
                        event['outcome']+'\n']
        path=ROOT/f'S6_SERIES_GRIND_checks_{paper}.md';path.write_text('\n'.join(out))
        per_paper[paper]={'entries':len(grouped[paper]),'bytes':path.stat().st_size}
    with (ROOT/'S6_SERIES_GRIND_inventory.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=columns);w.writeheader();w.writerows(rows)
    # Every label sharing a source anchor maps to the same immutable tag.
    bycanon={info['canonical_label']:info for info in labeltags.values()}
    taglist=[]
    for lab,tag in sorted(registry.items(),key=lambda kv:kv[1]):
        info=bycanon.get(lab,{})
        paper=info.get('paper','');meta=current.get(paper,{}).get(lab,{})
        rs=tag_rows.get(tag,[])
        taglist.append({'tag':tag,'paper':paper,'number':meta.get('number',''),'page':meta.get('page',''),'label':lab,
                        'status':' | '.join(sorted({r['status'] for r in rs})),'kind':info.get('kind','reserved')})
    with (ROOT/'S6_SERIES_GRIND_tags.tsv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=['tag','paper','number','page','label','status','kind'],delimiter='\t');w.writeheader();w.writerows(taglist)
    (ROOT/'analysis/unassigned_events.json').write_text(json.dumps(unassigned,indent=2))
    summary={'inventory_rows':len(rows),'consolidated_main_rows':len(main_info),'check_files':per_paper,'unassigned_events':len(unassigned),'scoped_assessments':len(assessments),'assessment_labels_missing_from_inventory':sorted(set(assessments)-{r['label'] for r in rows})}
    (ROOT/'code/outputs/check_file_generation.json').write_text(json.dumps(summary,indent=2));print(json.dumps(summary))

if __name__=='__main__':main()
