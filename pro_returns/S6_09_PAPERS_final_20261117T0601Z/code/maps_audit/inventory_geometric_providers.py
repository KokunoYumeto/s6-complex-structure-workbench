"""Inventory retained course proof units without changing the root inventory.

Section-numbered constructions are identified as such: the source does not give
them an invented theorem number.  Every unit retains its full text and explicit
range, and the containing complete chapter remains available for all setup.
"""
from pathlib import Path
import csv, hashlib, json, re

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / 'deliverables/work/maps_audit'
EVENTS = json.loads((OUT / 'course_geometric_provider_full_checks.json').read_text())
META = dict(reader='GPT-6 Astra (OpenAI, ChatGPT Pro mode)', effort='Pro', date='2026-11-17')
CODES = {
 'the-original-six-dimensional-framing-invariant.md':'FRAMED6',
 'whitney-moves-in-the-receiving-dimensions.md':'WHITNEY-RECEIVING',
 'higher-index-framed-slides-and-chain-maps.md':'HIGHER-SLIDES',
 'realizing-framed-handles-and-middle-cancellation.md':'MIDDLE-CANCEL',
 'morse-cancellation-with-controlled-support.md':'MORSE-CANCEL',
 'spin-six-and-the-framing-comparison.md':'SPIN6',
 'the-original-integral-stable-group-and-its-completion-maps.md':'INTEGRAL-STABLE',
 'framed-manifolds-and-the-pontryagin-thom-map.md':'PONTRYAGIN-THOM',
 'relative-morse-functions-and-original-handles.md':'RELATIVE-MORSE',
 'rearranging-the-original-framed-handles.md':'HANDLE-ARRANGEMENT',
 'removing-the-original-zero-and-top-handles.md':'ZERO-TOP',
 'morse-trajectories-and-critical-value-lowering.md':'TRAJECTORY-LOWERING',
 'belt-sphere-complements-and-the-whitney-disk.md':'BELT-COMPLEMENT',
 'whitney-move-with-controlled-support.md':'WHITNEY-SUPPORT',
 'integral-handle-chains-and-signed-incidences.md':'HANDLE-CHAINS',
 'creating-an-original-cancelling-handle-pair.md':'PAIR-CREATION',
 'framed-handle-slides-and-index-one-removal.md':'LOW-INDEX-SLIDES',
 'the-original-adams-tower-and-arithmetic-completion.md':'ADAMS-ARITHMETIC',
 'the-adams-tower-and-exact-inverse-limits.md':'ADAMS-TOWER',
 'the-actual-mod-two-cooperation-comparison-through-degree-eight.md':'ACTUAL-DEGREE8',
 'the-original-projective-coordinate-and-actual-cooperations.md':'PROJECTIVE-COOP',
 'the-exact-characteristic-two-coordinate-calculation.md':'FORMAL-CHAR2',
 'the-actual-mod-two-adams-resolution-and-cooperation-maps.md':'ACTUAL-RESOLUTION',
 'the-degree-six-milnor-cobar-calculation.md':'MILNOR-COBAR',
 'the-original-odd-prime-cooperations-and-degree-six-adams-calculation.md':'ODD-COOP',
 'coefficient-rings-and-the-original-degree-six-class.md':'COEFFICIENT-RINGS',
}
I_ALIASES = [
 dict(source_id='CG-S6-CHAIN-LEMMA-1.1',printed_label='mapsI:chain:lemma:1.1',result='Singular homotopy invariance; reuse the complete Paper I proof'),
 dict(source_id='CG-S6-CHAIN-LEMMA-2.1',printed_label='mapsI:chain:lemma:2.1',result='Small chains and barycentric subdivision; reuse the complete Paper I proof'),
 dict(source_id='CG-S6-CHAIN-COROLLARY-2.2',printed_label='mapsI:chain:corollary:2.2',result='Singular excision; reuse the complete Paper I proof'),
 dict(source_id='CG-S6-CHAIN-LEMMA-4.1',printed_label='mapsI:chain:lemma:4.1',result='Singular product chain comparison; reuse the complete Paper I proof'),
 dict(source_id='CG-S6-CW-THEOREM-4.1',printed_label='mapsI:cw:hurewicz-theorem-result',result='First Hurewicz map for the actual CW model; reuse the complete Paper I proof'),
 dict(source_id='CG-S6-PF-THEOREM-5.1',printed_label='mapsI:pf:theorem:5.1',result='Simply connected integral homology equivalence; reuse the complete Paper I proof'),
]

rows=[]; chapter_manifest=[]
for e in EVENTS:
    p=ROOT/e['source']; ls=p.read_text().splitlines(); code=CODES[p.name]
    heads=[]
    for i,line in enumerate(ls):
        m=re.match(r'^(#{2,3})\s+(.+)$',line)
        if m: heads.append((i+1,len(m.group(1)),m.group(2)))
    mains=[x for x in heads if x[1]==2]
    units=[]
    for k,(start,level,title) in enumerate(mains):
        end=(mains[k+1][0]-1) if k+1<len(mains) else len(ls)
        if re.search(r'(sources|reading and proof state|reading scope|human sources|source use|source and verification scope)',title,re.I): continue
        number=re.match(r'(\d+)\.',title)
        if not number: continue
        sec=number.group(1)
        if code=='PROJECTIVE-COOP' and sec=='7':
            # This paragraph only points forward to previously inventoried
            # results; retain it in the complete chapter, not as a new proof.
            continue
        if code=='ACTUAL-RESOLUTION' and sec=='9':
            continue
        if code=='ODD-COOP' and sec=='8':
            continue
        if code=='MILNOR-COBAR' and sec in {'2','3','4','5'}:
            # These are the complete proof of the explicit Theorem 1.1;
            # retaining them inside its full range avoids printing them twice.
            continue
        children=[h for h in heads if start<h[0]<=end and h[1]==3]
        is_exercise=bool(re.search(r'(exercises|worked calculations|complete calculations|complete receiving calculations)',title,re.I))
        # Each worked example has an independent complete calculation.  A parent
        # heading with no separate assertion is not made into an extra result.
        if code=='MILNOR-COBAR' and sec=='1':
            last=next(h[0]-1 for h in mains if h[2].startswith('6.'))
            sub=[h for h in heads if start<h[0]<=last]
            units.append((start,last,'1.1','Theorem 1.1 (all-length degree-six Milnor cobar calculation)','Theorem',sub))
        elif code=='MILNOR-COBAR' and sec=='6':
            units.append((start,end,'6.1','Theorem 6.1 (all-length odd-prime algebraic vanishing)','Theorem',children))
        elif is_exercise and children:
            if code=='FORMAL-CHAR2' and sec=='4':
                units.append((start,children[0][0]-1,sec,title,'Proved construction',[]))
            for j,(s,_,t) in enumerate(children):
                z=children[j+1][0]-1 if j+1<len(children) else end
                mm=re.search(r'(?:Exercise\s+)?(\d+\.\d+)',t)
                num=mm.group(1) if mm else f'{sec}.{j+1}'
                units.append((s,z,num,t,'Worked example' if sec!='6' or code!='HANDLE-CHAINS' else 'Proved construction',[]))
        elif code=='MORSE-CANCEL' and sec=='2':
            # Source Theorem 2.1 has its proof in the following three sections.
            last=next(h[0]-1 for h in mains if h[2].startswith('6.'))
            units.append((start,last,'2.1','Theorem 2.1 (supported cancellation)','Theorem',children))
        elif code=='MORSE-CANCEL' and sec in {'3','4','5'}:
            continue
        else:
            units.append((start,end,sec,title,'Proved construction',children))
    chapterrows=[]
    for start,end,number,title,kind,subheads in units:
        source_id=f'CG-S6-{code}-{number}'
        block='\n'.join(ls[start-1:end])+'\n'
        anchor=re.search(r'\{#([^}]+)\}',ls[start-1])
        # An exact heading is a statement locator, not a paraphrase falsely
        # attributed to a source theorem.  The complete source text is retained.
        producer_date=e['producer_date']
        addition_notice=''
        if code=='ADAMS-TOWER' and int(number.split('.')[0])>=8:
            producer_date='11 October 2026'
            addition_notice=ls[4]
        row=dict(source_run='WORKING_EDITION_COURSE_PROVIDER',source_id=source_id,
          source_file=str(p.relative_to(ROOT)),source_sha256=e['source_sha256'],
          start_line=start,end_line=end,proof_range=[start,end],
          full_setup_range=[1,start-1],source_number=number,
          source_result_form=('explicit source theorem' if kind=='Theorem' else 'numbered source section containing the proved construction and its complete argument'),
          source_heading=ls[start-1],title=re.sub(r'\s*\{#[^}]+\}','',title),
          source_anchor=anchor.group(1) if anchor else '',kind=kind,paper='III',
          intended_section='Classical prerequisites appendix, in the dependency order of the retained course',
          printed_label='',reserved_label=f'courseIII:{code.lower()}:{number}',
          statement_as_printed=ls[start-1],complete_source_text=block,
          complete_source_text_sha256=hashlib.sha256(block.encode()).hexdigest(),
          retained_complete_proof=f'deliverables/work/maps_audit/checked_course_providers/{p.name}',
          contained_numbered_subresults=[dict(line=s,heading=t) for s,_,t in subheads],
          raw_producer_header=e['raw_producer_header'],producer=e['producer'],
          producer_metadata_evidence=e.get('producer_metadata_evidence',[]),
          producer_effort=e['producer_effort'],producer_date=producer_date,
          original_chapter_header_date=e['producer_date'],raw_addition_notice=addition_notice,
          recorded_checks='Raw source author self-check declaration; this is not an independent reviewer claim.',
          current_check_event=e['event_id'],full_proof_read=True,
          check_outcome='Full receiving proof read and rederived; imported dependency closure is separately scoped, not presumed.',
          dependency_check_notes=e.get('remaining_imported_dependencies',[]),
          numerical_program_rerun=e.get('numerical_program_rerun','not yet rerun by this event'),
          duplicate_of_existing_inventory=False,taken_over_by='',
          available_PaperI_classical_aliases=I_ALIASES,
          found_in_AC26='Provider-specific baseline comparison pending; no novelty claim.',
          found_in_E26='Provider-specific baseline comparison pending; no novelty claim.',
          found_in_DGKX_v1='Provider-specific baseline comparison pending; no novelty claim.',
          found_elsewhere='Classical topology/geometric-topology result rederived in this course; precise operative primary-source checks recorded separately and incomplete where explicitly stated.',
          credited_to='Classical sources cited in the complete chapter; receiving proof by '+e['producer']+', effort '+e['producer_effort']+', '+producer_date+'.',
          wording_vs_source='Exact source proof unit retained. No paper has yet been assembled from this inventory.',
          notes='Do not print an identical prerequisite statement already in Paper I; use the listed aliases. Distinct coordinate proofs and worked calculations are retained in the complete chapter.',
          **META)
        rows.append(row);chapterrows.append(source_id)
    chapter_manifest.append(dict(source=e['source'],sha256=e['source_sha256'],
      whole_proof_range=[1,len(ls)],retained_complete_proof=f'deliverables/work/maps_audit/checked_course_providers/{p.name}',
      raw_producer_header=e['raw_producer_header'],producer=e['producer'],producer_effort=e['producer_effort'],producer_date=e['producer_date'],
      current_check_event=e['event_id'],full_receiving_proof_read=True,result_ids=chapterrows,
      imported_dependency_status=e.get('remaining_imported_dependencies',[]),**META))

(OUT/'course_geometric_provider_inventory.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
fields=['source_run','source_id','source_file','paper','reserved_label','kind','title','start_line','end_line','full_proof_read','current_check_event','producer','producer_effort','producer_date','raw_producer_header','source_sha256','duplicate_of_existing_inventory','taken_over_by','check_outcome','retained_complete_proof']
with (OUT/'course_geometric_provider_inventory.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore');w.writeheader();w.writerows(rows)
(OUT/'course_geometric_provider_full_proof_ranges.json').write_text(json.dumps(chapter_manifest,ensure_ascii=False,indent=2)+'\n')
(OUT/'course_geometric_PaperI_aliases.json').write_text(json.dumps(I_ALIASES,ensure_ascii=False,indent=2)+'\n')
# Keep all deeper linked source chapters visible, without turning link discovery
# into a proof-read or citation-check claim.
graph=json.loads((OUT/'course_source_dependency_graph.json').read_text())
(OUT/'course_deeper_dependency_inventory.json').write_text(json.dumps(dict(
  method='All local Markdown links from the course source are retained. A missing current geometric event does not overwrite earlier scoped receiving checks; inspect the named ledgers. Forward/navigation links are not automatically operative dependencies.',
  sources=graph,**META),ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(complete_checked_provider_chapters=len(chapter_manifest),numbered_proof_units=len(rows),deeper_source_files=len(graph),paper_assembly_performed=False)))
