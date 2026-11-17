#!/usr/bin/env python3
"""Read-only exact retention gate for all33 complete course ranges/249 units.

Replays only the exact reviewed reference, credit, structure and layout records.
It requires each whole normalized chapter at its own final chapter label. Thus
every inventoried complete source-unit range contained in that chapter is
retained, not merely its statement label. Mathematical-expression comparison of
the structure stage is kept separate from full-content matching and proof audit.
"""
from pathlib import Path
import collections,hashlib,importlib.util,json,re

D=Path(__file__).resolve().parents[2]
R=D.parent
W=D/'work/maps_audit'


def sha(s):return hashlib.sha256(s.encode()).hexdigest()


def group_end(s,start):
    depth=1;i=start+1
    while depth:
        if i>=len(s):raise ValueError('Unclosed TeX group')
        if s[i]=='\\' and i+1<len(s) and s[i+1] in '{}\\':i+=2;continue
        if s[i]=='{':depth+=1
        elif s[i]=='}':depth-=1
        i+=1
    return i


def math_tokens(s):
    s=s.replace(r'\(\square\)','')
    return re.findall(r'\\begin\{equation\}.*?\\end\{equation\}|'
                      r'\\\[.*?\\\]|\\\(.*?\\\)|\$\$.*?\$\$|(?<!\\)\$[^$\n]+\$',s,re.S)


def clean(s,chapter_labels):
    s=re.sub(r'^%[^\n]*\n','',s,flags=re.M)
    pieces=[];pos=0
    for m in re.finditer(r'\\(Uses|label)\s*\{',s):
        if m.start()<pos:continue
        end=group_end(s,m.end()-1);value=s[m.end():end-1]
        pieces.append(s[pos:m.start()])
        if m[1]=='label' and value in chapter_labels:pieces.append('@@CHAPTER_'+value+'@@')
        pos=end
    pieces.append(s[pos:]);s=''.join(pieces).replace(r'\phantomsection','')
    return ''.join(s.split())


def main():
    manifest_path=W/'III_course_conversion_manifest.json'
    manifest=json.loads(manifest_path.read_text())
    units=json.loads((W/'III_course_retention_units.json').read_text())
    assert len(manifest)==33 and len(units)==249
    structure_path=D/'records/III_course_structure_repairs.json'
    structure_text=structure_path.read_text();structure=json.loads(structure_text)
    by_structure={x['converted']:x for x in structure['chapters']}
    assert len(by_structure)==33
    credit_path=W/'III_course_source_credit_insertions.json'
    credits=json.loads(credit_path.read_text())
    layout_path=D/'records/III_layout_repairs_build10.json'
    layout_text=layout_path.read_text();layouts=json.loads(layout_text)
    wording_path=D/'records/III_external_reference_wording_repairs.json'
    wording_text=wording_path.read_text() if wording_path.exists() else '[]'
    wording_records=json.loads(wording_text)
    transformer_path=D/'code/maps_audit/repair_course_pinned_references.py'
    spec=importlib.util.spec_from_file_location('exact_course_references',transformer_path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    final_path=D/'S6_09_PAPERS_III.tex';final=final_path.read_text()
    available=set(re.findall(r'\\label\{([^}]+)\}',final))
    chapter_labels=set()
    for e in manifest:
        text=(D/e['converted']).read_text()
        key=re.search(r'\\label\{(courseIII:[^}]+:section)\}',text)[1]
        chapter_labels.add(key)
    clean_final=clean(final,chapter_labels)
    aux_inputs=[];aux_data=[]
    for paper in ('I','II'):
        aux=(D/f'S6_09_PAPERS_{paper}.aux').read_text()
        nums=dict(re.findall(r'\\newlabel\{([^}]+)\}\{\{([^}]+)\}',aux))
        kinds=dict(re.findall(r'\\newlabel\{([^}]+)@cref\}\{\{\[([^\]]+)\]',aux))
        aux_data.append((paper,nums,kinds));aux_inputs.append({'paper':paper,'sha256':sha(aux)})
    chapters=[];applied_credits=[];source_by_name={}
    failures_dir=W/'III_course249_source_to_print_differences'
    failures_dir.mkdir(exist_ok=True)
    for e in manifest:
        source_path=R/(e.get('retained') or e['source'])
        lo,hi=e['range'];source_lines=source_path.read_text().splitlines()
        retained_range='\n'.join(source_lines[lo-1:hi])+'\n'
        assert sha(retained_range)==e['source_sha256'],(e['source'],'retained range hash')
        original=(D/e['converted']).read_text()
        assert sha(original)==e['converted_sha256'],(e['converted'],'converted file hash')
        text=module.transform(original,e['converted'])
        for c in credits:
            if Path(c['source_tex']).name!=Path(e['converted']).name:continue
            assert text.count(c['insert_after'])==1
            assert c['idempotence_marker'] not in text
            text=text.replace(c['insert_after'],c['insert_after']+c['insert_text'],1)
            applied_credits.append(c['source_tex'])
        pre_structure=text
        srec=by_structure[e['converted']]
        assert sha(text)==srec['before_sha256'],(e['converted'],'structure input hash')
        applied_structure=[]
        for i,event in enumerate(structure['events']):
            if event['converted']!=e['converted']:continue
            assert text.count(event['before'])==1,(e['converted'],i,'structure literal not unique')
            text=text.replace(event['before'],event['after'],1)
            applied_structure.append(i)
        assert sha(text)==srec['after_sha256'],(e['converted'],'structure output hash')
        old_math=math_tokens(pre_structure.replace(r'dF_y\circ J_y=i,dF_y',r'dF_y\circ J_y=i\,dF_y'))
        new_math=math_tokens(text)
        assert old_math==new_math,(e['converted'],'structure math comparison')
        assert len(new_math)==srec['math_expressions_preserved']
        key=re.search(r'\\label\{(courseIII:[^}]+:section)\}',text)[1]
        # The only relevant shared prose cleanup removes source priority
        # disclaimers, already covered by the recorded global editorial rule.
        text=re.sub(r'(?:No|no) (?:novelty or )?priority claim\s+is made[^.]*\.','',text)
        text=re.sub(r'(?:The )?statement makes no priority claim\.','',text)
        text=re.sub(r';?\s*we claim no priority for integral-conjugacy\s+algorithms\.','.',text)
        text=text.replace('No claim of priority is made.','').replace('This states the search outcome and claims no priority.','This states the search outcome.')
        for paper,nums,kinds in aux_data:
            def external(m):
                out=[]
                for target in m[2].split(','):
                    if target in nums and target not in available:
                        kind='Equation' if m[1]=='eqref' else kinds.get(target,'result').capitalize()
                        out.append('Paper~'+paper+', '+kind+'~'+nums[target])
                    else:out.append('\\'+m[1]+'{'+target+'}')
                return ' and '.join(out)
            text=re.sub(r'\\(ref|eqref|cref|Cref|autoref)\{([^}]+)\}',external,text)
        applied_wording=[]
        for i,event in enumerate(wording_records):
            count=text.count(event['before'])
            if count:
                assert count<=event['occurrences'],(e['converted'],i,'wording occurrence count')
                text=text.replace(event['before'],event['after'])
                applied_wording.append({'record_index':i,'occurrences_in_chapter':count})
        applied_layout=[]
        for i,event in enumerate(layouts):
            if event['before'] in text:
                assert text.count(event['before'])==1,(e['converted'],i,'layout literal not unique')
                text=text.replace(event['before'],event['after'],1);applied_layout.append(i)
        expected=clean(text,chapter_labels);marker='@@CHAPTER_'+key+'@@'
        assert expected.count(marker)==clean_final.count(marker)==1,(e['converted'],'chapter destination')
        start=clean_final.index(marker)-expected.index(marker)
        match=start>=0 and clean_final[start:start+len(expected)]==expected
        labels=set(re.findall(r'\\label\{([^}]+)\}',text))
        final_line=final[:final.index(r'\label{'+key+'}')].count('\n')+1
        record={
            'source':e['source'],'retained_source':e.get('retained'),'retained_range':e['range'],
            'retained_range_sha256':e['source_sha256'],'converted':e['converted'],
            'converted_sha256':e['converted_sha256'],'chapter_label':key,'final_label_line':final_line,
            'full_normalized_chapter_sha256':sha(expected),'complete_chapter_matches_at_own_label':match,
            'match_offset_from_own_chapter_label':0 if match else None,
            'complete_proof_environments':text.count(r'\begin{proof}'),
            'structure_math_expressions_compared':len(old_math),'structure_math_exact_after_recorded_comma_correction':True,
            'exact_structure_event_indices':applied_structure,'exact_layout_event_indices':applied_layout,
            'exact_external_reference_wording_events':applied_wording,
            'existing_labels_retained':srec['labels_preserved'],'new_formal_statement_labels':srec['new_statement_labels'],
            'raw_latex_fence_pairs_removed':srec['raw_latex_fence_pairs_removed'],
            'full_content_scope':'Every proof word, statement, mathematical display, exercise/solution, citation and resolved reference; only whitespace, labels, Uses metadata, comment lines and phantom anchors ignored.',
        }
        if not match:
            stem=Path(e['converted']).stem
            (failures_dir/(stem+'.expected.tex')).write_text(text)
            (failures_dir/(stem+'.normalized_expected.txt')).write_text(expected)
            (failures_dir/(stem+'.normalized_actual.txt')).write_text(clean_final[start:start+len(expected)+2000])
        chapters.append(record);source_by_name[e['source']]=(e,record,labels,source_lines)
    assert len(applied_credits)==len(credits)
    records=[]
    for u in units:
        e,c,labels,source_lines=source_by_name[u['source']]
        a,b=u['source_unit_range'];lo,hi=e['range']
        assert lo<=a<=b<=hi,(u['source_id'],'unit lies outside complete retained source range')
        key=u['reserved_label']
        assert key in labels,(u['source_id'],'unit label absent from expected full chapter')
        count=final.count(r'\label{'+key+'}')
        assert count==1,(u['source_id'],'final unit label count',count)
        records.append({
            'source_id':u['source_id'],'printed_label':key,'source':u['source'],
            'source_unit_range':u['source_unit_range'],'source_proof_range':u['source_proof_range'],
            'source_unit_text_sha256':sha('\n'.join(source_lines[a-1:b])+'\n'),
            'retained_complete_chapter':c['converted'],'complete_chapter_sha256':c['full_normalized_chapter_sha256'],
            'final_label_count':count,'complete_unit_retained':c['complete_chapter_matches_at_own_label'],
            'method':'The entire containing chapter matches at its own final label; this original complete source-unit/proof range is verified to lie inside that retained chapter. This is full-content coverage, not a label-only test.',
            'prior_source_to_conversion_check':'work/maps_audit/III_course_retention_review.json',
            'prior_source_unit_check':'work/maps_audit/III_course_retention_units.json#'+u['source_id'],
        })
    report={
        'reader':'GPT-6 Astra (OpenAI, ChatGPT Pro mode)','effort':'Pro','date_utc':'2026-11-17',
        'scope':'Final full normalized source-to-print retention for all33 complete retained course ranges and all249 inventoried units after exact reference/credit/structure/layout edits; independent mathematical validity remains in the separate full-proof/source audit.',
        'source_manifest_sha256':sha(manifest_path.read_text()),'paper_III_sha256':sha(final),
        'structure_record_sha256':sha(structure_text),'layout_record_sha256':sha(layout_text),
        'external_reference_wording_record_sha256':sha(wording_text),
        'historical_metadata_independent_review':'work/maps_audit/III_final_historical_metadata_review.json',
        'reference_record_sha256':sha(module.LEDGER.read_text()),'source_credit_record_sha256':sha(credit_path.read_text()),
        'aux_inputs':aux_inputs,'chapters':len(chapters),'units':len(records),
        'passed_chapters':sum(c['complete_chapter_matches_at_own_label'] for c in chapters),
        'passed_units':sum(r['complete_unit_retained'] for r in records),
        'failed_chapters':[c['converted'] for c in chapters if not c['complete_chapter_matches_at_own_label']],
        'failed_units':[r['source_id'] for r in records if not r['complete_unit_retained']],
        'complete_proof_environments':sum(c['complete_proof_environments'] for c in chapters),
        'separate_structure_math_comparison':{'expressions':sum(c['structure_math_expressions_compared'] for c in chapters),'passed':True,'sole_math_byte_correction':r'dF_y\circ J_y=i,dF_y -> dF_y\circ J_y=i\,dF_y, independently checked complex-linearity punctuation. Source proof-end squares are delimiters.'},
        'preserved_reference_clarification':'The final reference gate separately records the explicit circle basis(1,a), dual basis(a,1) replacing a dangling exercise pointer; all prior mathematical expressions remain.',
        'source_provenance_limitation':'This final comparison starts from the already checked source-to-conversion chain. It does not claim a new full mathematical proof read or new original-literature opening.',
        'chapter_records':chapters,'records':records,
    }
    out=W/'III_course249_final_source_to_print_check.json'
    if out.exists():
        previous=out.read_text();archive=W/'retention_check_history';archive.mkdir(exist_ok=True)
        old_path=archive/('course249_'+sha(previous)+'.json')
        if not old_path.exists():old_path.write_text(previous)
    out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:report[k] for k in ['chapters','units','passed_chapters','passed_units','complete_proof_environments','failed_chapters']}))


if __name__=='__main__':main()
