"""Resolve original numeric cross-paper references through rebuilt source AUX.

Resolution uses the exact numbered destination, retaining every source alias.
The output records every replaced occurrence and fails on ambiguity.
"""
from pathlib import Path
import json,re
from collections import defaultdict,Counter
from tex_tools import PAPERS,macros,replace_spans
ROOT=Path(__file__).resolve().parents[1]
ANALYSIS=ROOT/'analysis'
SOURCE=ROOT.parent/'S6_SERIES_GRIND_source/S6_GRIND_1_papers_cp15'

def main():
    aux={p:json.loads((ANALYSIS/f'baseline_labels_{p}.json').read_text()) for p in PAPERS}
    structure=json.loads((ANALYSIS/'source_statement_structure.json').read_text())
    owners=json.loads((ANALYSIS/'label_owners.json').read_text())
    preferred={p:set(r['label'] for r in structure[p]) for p in PAPERS}
    allrecords=json.loads((ANALYSIS/'source_statement_records.json').read_text())
    for r in allrecords:preferred[r['source_paper']].add(r['label'])
    keymap={};errors=[];occurrences=[]
    kindnames={'cited':'cited','cited result':'cited','refuted':'refuted','correction':'refuted','open question':'openq','computation':'computed','verification record':'auditrecord','verification':'test'}
    for p in PAPERS:
        source=(SOURCE/f'S6_10_PAPERS_{p}.tex').read_text()
        for a,b,args in macros(source,'ExternalPaperRef',3):
            rawkind,num,target=args
            kind=rawkind.replace('~','').strip().lower()
            kind=kindnames.get(kind,kind)
            candidates=[(lab,v) for lab,v in aux[target].items() if not lab.endswith('@cref') and v['number']==num and
                        (not kind or v['destination'].startswith(kind+'.'))]
            if not candidates and kind in ('equation',''):
                normalized=lambda value:re.sub(r'[{}()]','',value)
                candidates=[(lab,v) for lab,v in aux[target].items() if not lab.endswith('@cref') and normalized(v['number'])==normalized(num) and v['destination'].startswith(('equation.','AMS.'))]
            destinations={v['destination'] for lab,v in candidates}
            if len(destinations)!=1:
                errors.append({'from':p,'kind':rawkind,'number':num,'to':target,'candidates':candidates,'context':source[max(a-120,0):b+120]})
                continue
            candidates.sort(key=lambda item:(item[0] not in preferred[target],item[0] not in owners,len(item[0]),item[0]))
            label=candidates[0][0]
            if target=='VI' and label in {'sec:II:08','sec:II:12'}:label=label.replace('sec:II:','sec:II:all:')
            keymap[tuple(args)]=label
            occurrences.append({'from_source_paper':p,'source_offset':a,'kind':rawkind,'old_number':num,'source_target_paper':target,'target_label':label,'new_target_paper':owners.get(label),'aliases':[x[0] for x in candidates]})
    (ANALYSIS/'numeric_reference_resolution.json').write_text(json.dumps({'occurrences':occurrences,'errors':errors},indent=2,ensure_ascii=False))
    if errors:
        print(json.dumps({'resolved':len(occurrences),'errors':len(errors),'details':errors[:12]},ensure_ascii=False))
        return
    for path in (ROOT/'parts').glob('*.tex'):
        if path.name.endswith('.linked.tex'):continue
        text=path.read_text();spans=[]
        for a,b,args in macros(text,'ExternalPaperRef',3):
            label=keymap.get(tuple(args))
            if label is None:raise ValueError((path,args))
            spans.append((a,b,'\\SeriesRef{'+label+'}'))
        linked=replace_spans(text,spans)
        # Every relocated local citation also resolves through the label owner.
        current=path.name.split('.')[0]
        if current=='VI':current='II'
        spans=[]
        pattern=re.compile(r'\\(?P<kind>(?:c|C)?ref|eqref|autoref|pageref)\{(?P<labels>[^}]+)\}')
        for m in pattern.finditer(linked):
            labels=[s.strip() for s in m.group('labels').split(',')]
            if any(lab in owners and owners[lab]!=current for lab in labels):
                items=[]
                for lab in labels:
                    if lab in owners and owners[lab]!=current:items.append('\\SeriesRef{'+lab+'}')
                    else:items.append('\\'+m.group('kind')+'{'+lab+'}')
                spans.append((m.start(),m.end(),', '.join(items)))
        linked=replace_spans(linked,spans)
        path.with_name(path.stem+'.linked.tex').write_text(linked)
    print(json.dumps({'resolved_occurrences':len(occurrences),'unique_numeric_targets':len(keymap),'errors':0,'new_paper_pairs':dict(Counter(r['from_source_paper']+'->'+str(r['new_target_paper']) for r in occurrences))}))

if __name__=='__main__':main()
