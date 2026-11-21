#!/usr/bin/env python3
"""Bind defect loci while preserving the exact historical before-PDF scope.

Inherited old-side records are reused only after their old-text, statement-id
and old-location hashes match the authenticated checkpoint. Continuation edits
use the declared candidate explicitly. Current locations use SyncTeX or an
explicitly named retained context; a context is never described as an exact
phrase locus. Default operation writes a preview only.
"""
from pathlib import Path
import argparse
import bisect
import collections
import csv
import datetime as dt
import hashlib
import importlib.util
import json
import re
import shutil

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT.parent/'S6_SERIES_PUBLISH_work'
CP10 = BASE/'S6_SERIES_PUBLISH_checkpoint_10'
csv.field_size_limit(100_000_000)
ENV = re.compile(r'\\begin\{(maintheorem|theorem|proposition|lemma|corollary|definition|remark|cited)\}')


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def htext(s):
    return hashlib.sha256(s.encode()).hexdigest()


def load(p):
    return json.loads(p.read_text())


def contexts(text, snippet):
    """Find containing historical statements or section labels, not text pages."""
    if not snippet:
        return []
    result, pos = [], 0
    envs = list(ENV.finditer(text))
    headings = list(re.finditer(r'\\(?:sub)*section\*?\{([^}]+)\}',text))
    while True:
        at = text.find(snippet,pos)
        if at < 0:
            return result
        pos = at+max(1,len(snippet))
        es = [x for x in envs if x.start() <= at]
        hs = [x for x in headings if x.start() <= at]
        e = es[-1] if es else None
        heading = hs[-1] if hs else None
        if e and (not heading or e.start() > heading.start()):
            end = text.find('\\end{'+e[1]+'}',e.end())
            header = text[e.start():end]
            labels = re.findall(r'\\label\{([^}]+)\}',header)
            result.extend(dict(label=x,basis='containing historical statement label',source_position=at) for x in labels)
        elif heading:
            next_env = next((x.start() for x in envs if x.start()>heading.start()),len(text))
            next_heading = next((x.start() for x in headings if x.start()>heading.start()),len(text))
            header = text[heading.start():min(next_env,next_heading)]
            labels = re.findall(r'\\label\{([^}]+)\}',header)
            result.extend(dict(label=x,basis='historical section label',source_position=at) for x in labels)
            result.append(dict(title=heading[1],basis='historical section title',source_position=at))


def frozen_text(doc, text):
    # Keep doc.source equal to the path recorded in this PDF's SyncTeX input.
    doc.text = text
    doc.docstart = text.index(r'\begin{document}')
    doc.line_starts = [0]+[m.end() for m in re.finditer('\n',text)]
    doc.sections = list(re.finditer(r'\\(?:sub)*section\*?\{([^}]+)\}',text))
    doc.labels = {m[1]:m.start() for m in re.finditer(r'\\label\{([^}]+)\}',text)}


def scoped_description(module, item, side, row):
    if item['method'] == 'intermediate revision source-only':
        return 'intermediate revision wording; no exact original-PDF phrase locus established'
    result = module.description(item, side, row)
    if side == 'new' and not row['new_text'] and item.get('pages'):
        result = 'deleted text; retained context at p. '+module.page_ranges(item['pages'])+' ('+item['method']+')'
    return result


def extra_current_context(module, doc, row, old_item, original_source, cp13_source, all_rows):
    sid = row['statement_id']
    if 'preamble' in sid.lower():
        return dict(method='nonprinting preamble source',pages=[],location='preamble source; no printed page',exact=True)
    bib = re.search(r'\\bibitem(?:\[[^\]]*\])?\{([^}]+)\}', row['old_text'])
    if not row['new_text'] and bib and not re.search(r'\\bibitem(?:\[[^\]]*\])?\{'+re.escape(bib[1])+r'\}',doc.text):
        return dict(method='removed uncited bibliography entry',pages=[],location='Bibliography entry '+bib[1]+' is removed; exact text remains in the shared bibliography records',exact=False)
    anchors = re.findall(r'outline-[IV]+-[A-Z]',sid+' '+row['old_text'][:200])
    for anchor in anchors:
        token='\\hypertarget{'+anchor+'}{}'
        if token in doc.text:
            at=doc.text.index(token)
            return dict(method='retained outline anchor locus',lines=[doc.line(at)],location=anchor,exact=False)
    if sid=='further results':
        m=re.search(r'\\(?:subsection|paragraph)\*?\{Further results\}',doc.text)
        if m:return dict(method='retained section heading locus',lines=[doc.line(m.start())],location='Further results',exact=False)
    labels=[]
    for label in doc.aux:
        if label and (sid.startswith(label+';') or sid==label):
            labels.append(dict(label=label,basis='explicit statement-id prefix'))
    labels += contexts(original_source,row['old_text'])
    labels += contexts(original_source,row['old_text'].rstrip())
    labels += contexts(original_source,row['new_text'])
    labels += contexts(cp13_source,row['new_text'])
    labels += contexts(cp13_source,row['old_text'])
    if not row['new_text'] and re.match(r'\\(?:sub)*section\*?\{',row['old_text']):
        at=original_source.find(row['old_text'].rstrip())
        if at>=0:
            following=ENV.search(original_source,at+len(row['old_text'].rstrip()))
            if following:
                end=original_source.find('\\end{'+following[1]+'}',following.end())
                labels += [dict(label=x,basis='retained statement immediately following the deleted historical heading')
                           for x in re.findall(r'\\label\{([^}]+)\}',original_source[following.start():end])]
    exact_guard_sources={
        'I-00438':('agents/i_analytic/S6_SERIES_PUBLISH_I_editorial_batch_h_guards.json','IA-H-22'),
        'I-00572':('agents/i_topology/editorial/S6_SERIES_PUBLISH_I_boundary_batch4_guarded.json','I-topology4-04')}
    if row['change_id'] in exact_guard_sources:
        name,key=exact_guard_sources[row['change_id']]
        guard_path=ROOT/name
        found=[]
        def walk(value):
            if isinstance(value,dict):
                if value.get('id')==key:found.append(value)
                for item in value.values():walk(item)
            elif isinstance(value,list):
                for item in value:walk(item)
        walk(load(guard_path));assert len(found)==1
        guard=found[0]
        assert guard['old']==row['old_text'] and guard['new']==row['new_text']
        labels += [dict(label=x,basis='exact archived guard '+name+'#'+key,
                        evidence_sha256=sha(guard_path)) for x in guard['statement_ids']]
    if row['change_id']=='I-00893':
        preview=ROOT/'agents/i_analytic/S6_SERIES_PUBLISH_I_editorial_batch_h_preview.tex'
        assert preview.read_text().count(row['old_text'])==1
        for item in contexts(preview.read_text(),row['old_text']):
            labels.append(dict(item,basis='exact archived preview '+str(preview.relative_to(ROOT)),evidence_sha256=sha(preview)))
    for key in ['destinations','related_baseline_loci']:
        labels += [dict(label=x.get('label'),title=x.get('title'),basis='authenticated historical '+key)
                   for x in old_item.get(key,[])]
    accepted=[]
    for c in labels:
        label=c.get('label')
        if label in doc.aux:
            q=doc.aux[label]
            accepted.append(dict(label=label,page=int(q['page']),number=q['number'],basis=c['basis'],
                                 **({'evidence_sha256':c['evidence_sha256']} if 'evidence_sha256' in c else {})))
    if accepted:
        unique={x['label']:x for x in accepted}
        return dict(method='retained historical context locus',pages=sorted({x['page'] for x in unique.values()}),
                    location='; '.join(f"{x['label']}, number {x['number']}" for x in unique.values()),
                    context_bindings=list(unique.values()),exact=False,
                    scope='A retained statement/section context, not the location of superseded wording.')
    for c in labels:
        title=c.get('title')
        matches=[m for m in doc.sections if m[1]==title]
        if title and len(matches)==1:
            return dict(method='retained historical section title locus',lines=[doc.line(matches[0].start())],
                        location=title,exact=False,scope='Section-start context only; no exact phrase locus.')
    # A sufficiently long replacement can be traced into a later exact edit.
    replacement=row['new_text']
    if len(replacement)>60:
        later=[x for x in all_rows if x['change_id']>row['change_id'] and replacement in x['old_text']]
        if len(later)==1:
            target=module.plan(doc,later[0],'new')
            if target['method']!='source-only change':
                return dict(target,method='later exact edit context: '+target['method'],exact=False,
                            via_change_id=later[0]['change_id'],scope='The entire historical replacement occurs in this later edit; its surviving context is located.')
    return None


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--current-build',type=Path,required=True)
    p.add_argument('--apply',action='store_true')
    p.add_argument('--plan-only',action='store_true')
    p.add_argument('--source-snapshot',type=Path)
    p.add_argument('--defects-snapshot',type=Path)
    p.add_argument('--cli-synctex',action='store_true',help='Parse SyncTeX anew for every query using the historical CLI loop')
    a=p.parse_args()
    stamp=dt.datetime.now(dt.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
    run=ROOT/'agents/continuation_infra'/('defect_mapping_'+stamp)
    (run/'records').mkdir(parents=True)
    program=ROOT/'code/S6_SERIES_PUBLISH_map_defect_pages.py'
    spec=importlib.util.spec_from_file_location('historical_defect_mapper',program)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    module.ROOT=run  # isolate all newly generated SyncTeX caches
    batch_program=ROOT/'code/S6_SERIES_PUBLISH_synctex_batch.py'
    batch_spec=importlib.util.spec_from_file_location('continuation_synctex_batch',batch_program)
    batch=importlib.util.module_from_spec(batch_spec);batch_spec.loader.exec_module(batch)
    canonical_source=ROOT/'S6_SERIES_PUBLISH_I.tex'
    source=a.source_snapshot or canonical_source
    source_sha=sha(source)
    source_text=source.read_text()
    canonical_defects=ROOT/'S6_SERIES_PUBLISH_defects_I.tsv'
    defects=a.defects_snapshot or canonical_defects
    defects_sha=sha(defects)
    rows=list(csv.DictReader(defects.open(),delimiter='\t'))
    assert len({x['change_id'] for x in rows})==len(rows)
    inherited_path=CP10/'agents/i_marking/S6_SERIES_PUBLISH_I_baseline_page_mapping.json'
    inherited=load(inherited_path)
    baseline=BASE/'S6_SERIES_GRIND_I.tex'
    assert sha(baseline)==inherited['baseline_source_sha256']
    by_old={x['change_id']:x for x in inherited['details']}
    cp13=CP10/'S6_SERIES_PUBLISH_I.tex'
    restore_comparison=load(ROOT/'agents/continuation_infra/S6_SERIES_PUBLISH_I_candidate13_restore_comparison.json')
    assert restore_comparison['different_pages']==[] and len(restore_comparison['identical_entire_png_pages'])==346
    old_docs={}
    before_source_paths={}
    for row in rows:
        if row['change_id'] in by_old:continue
        match=re.search(r'candidate\s*(\d+)',row['old_location'],re.I)
        assert match,('Continuation before-candidate is not identified',row['change_id'])
        candidate=int(match[1])
        if candidate in old_docs:continue
        if candidate==13:
            old_docs[candidate]=module.Document(cp13,ROOT/'build/I_candidate13_restored')
            before_source_paths[candidate]=cp13
        else:
            before=ROOT/f'agents/continuation_infra/S6_SERIES_PUBLISH_I_candidate{candidate}_source_for_mapping.tex'
            before_build=ROOT/f'build/I_candidate{candidate}'
            assert sha(before)==load(before_build/'build_summary.json')['source_sha256']
            old_docs[candidate]=module.Document(canonical_source,before_build)
            frozen_text(old_docs[candidate],before.read_text())
            before_source_paths[candidate]=before
    current=module.Document(canonical_source,a.current_build)
    frozen_text(current,source_text)
    build=load(current.build/'build_summary.json')
    assert build['source_sha256']==source_sha and build['pdf_sha256']==sha(current.pdf)
    original_source=baseline.read_text();cp13_source=cp13.read_text()
    plans=[]
    for row in rows:
        historic=by_old.get(row['change_id'])
        if historic:
            assert historic['old_text_sha256']==htext(row['old_text']),row['change_id']
            assert historic['statement_id']==row['statement_id'],row['change_id']
            assert historic['original_old_location']==row['old_location'],row['change_id']
            old=dict(historic['old'],reused_from_unchanged_baseline_receipt=True,
                     before_pdf_scope='original419-page Paper I',before_pdf_sha256=inherited['baseline_pdf_sha256'],
                     before_source_sha256=inherited['baseline_source_sha256'])
            old_doc=None
        else:
            candidate=int(re.search(r'candidate\s*(\d+)',row['old_location'],re.I)[1])
            old_doc=old_docs[candidate]
            assert row['old_text'] and old_doc.text.count(row['old_text'])>=1, ('Before text absent from declared candidate',row['change_id'])
            old=module.plan(old_doc,row,'old')
            old['before_pdf_scope']=f'candidate{candidate}'
            old['before_source_sha256']=sha(before_source_paths[candidate])
            old['before_pdf_sha256']=(restore_comparison['old_pdf_sha256'] if candidate==13
                                      else load(old_doc.build/'build_summary.json')['pdf_sha256'])
            old['reconstructed_before_pdf_sha256']=sha(old_doc.pdf)
        new=module.plan(current,row,'new')
        if new.get('occurrences',0)>1:
            occurrence_count=new['occurrences']
            context=module.fallback(current,row)
            if context['method']=='source-only change':
                context=extra_current_context(module,current,row,old,original_source,cp13_source,rows)
            if context and context['method']!='source-only change':
                new=dict(context,replacement_occurrences_in_current_source=occurrence_count,
                         scope='The replacement string has multiple current occurrences; this field locates the explicitly retained context and does not identify a unique edited occurrence.')
            else:
                new=dict(new,method='all matching current replacement occurrences and SyncTeX',exact=False,
                         scope='All current occurrences of the repeated replacement string are located; no unique edited-occurrence claim.')
        if new['method']=='source-only change':
            replacement=extra_current_context(module,current,row,old,original_source,cp13_source,rows)
            if replacement:new=replacement
        plans.append((row,old_doc,old,new))
    if a.plan_only:
        pending=[dict(change_id=row['change_id'],statement_id=row['statement_id'],
                      old_text=row['old_text'],new_text=row['new_text'],old=old,new=new)
                 for row,_,old,new in plans if new['method']=='source-only change']
        path=run/'S6_SERIES_PUBLISH_I_unresolved_context_plan.json'
        path.write_text(json.dumps(pending,indent=2)+'\n')
        print(json.dumps(dict(path=str(path),rows=len(rows),unresolved=[x['change_id'] for x in pending],
                              scope='Plan only; SyncTeX loci have not been materialized in this run.')))
        return
    reused_caches=[]
    for doc in [*old_docs.values(),current]:
        # Exact PDF-hash keyed caches from this continuation are reusable across
        # preview reruns; this avoids repeating thousands of identical queries.
        for prior_cache in sorted((ROOT/'agents/continuation_infra').glob('defect_mapping_*/records/'+doc.cache_path.name)):
            if prior_cache==doc.cache_path:continue
            cached={int(k):v for k,v in load(prior_cache).items()}
            for key,value in cached.items():
                assert key not in doc.cache or doc.cache[key]==value,'Conflicting exact-PDF SyncTeX cache'
                doc.cache[key]=value
            reused_caches.append(dict(path=str(prior_cache.relative_to(ROOT)),sha256=sha(prior_cache),queries=len(cached)))
        requests=[]
        for _,old_doc,old,new in plans:
            if doc is old_doc:requests+=old.get('lines',[])
            if doc is current:requests+=new.get('lines',[])
        if a.cli_synctex:
            doc.prepare(requests)
        else:
            batch.prepare(doc,requests)
    details=[]
    for row,old_doc,old,new in plans:
        old=module.materialize(old_doc,old)
        new=module.materialize(current,new)
        old_description=scoped_description(module,old,'old',row)
        new_description=scoped_description(module,new,'new',row)
        row['old_page']=old['before_pdf_scope']+': '+old_description
        row['new_page']='current candidate: '+new_description
        row['mapped_old_location']=old['location']
        row['mapped_new_location']=new['location']
        row['page_mapping_method']=old['method']+' -> '+new['method']
        row['review_status']='applied; exact scoped before/current page mapping; current final gate pending'
        details.append(dict(change_id=row['change_id'],statement_id=row['statement_id'],
                            old_text_sha256=htext(row['old_text']),new_text_sha256=htext(row['new_text']),old=old,new=new))
    canonical_stable=(sha(canonical_source)==source_sha and sha(canonical_defects)==defects_sha)
    if a.apply:
        assert canonical_stable,'Canonical source or defect rows changed while mapping.'
    mapped=run/'S6_SERIES_PUBLISH_defects_I_mapped.tsv'
    with mapped.open('w') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t');w.writeheader();w.writerows(rows)
    unresolved=[x for x in details if x['new']['method']=='source-only change']
    receipt=dict(recorded_utc=dt.datetime.now(dt.timezone.utc).isoformat(),paper='I',rows=len(rows),
                 applied=a.apply,mathematical_events_added=0,page_reading_events_added=0,
                 current_source_sha256=source_sha,current_pdf_sha256=sha(current.pdf),
                 canonical_source_and_defects_match_snapshot=canonical_stable,
                 source_input=str(source),defect_input=str(defects),
                 defect_input_sha256=defects_sha,mapped_defects_sha256=sha(mapped),
                 historical_mapper_sha256=sha(program),inherited_old_receipt=str(inherited_path),
                 synctex_query_engine=('CLI per-query parser' if a.cli_synctex else 'shared libsynctex parser; same installed library as CLI'),
                 synctex_batch_program_sha256=sha(batch_program),
                 inherited_old_receipt_sha256=sha(inherited_path),
                 inherited_old_rows_reused=sum(x['old'].get('reused_from_unchanged_baseline_receipt',False) for x in details),
                 old_scope_counts=dict(collections.Counter(x['old']['before_pdf_scope'] for x in details)),
                 current_mapping_methods=dict(collections.Counter(x['new']['method'] for x in details)),
                 reused_exact_pdf_synctex_caches=reused_caches,
                 unresolved_current_context_ids=[x['change_id'] for x in unresolved],details=details,
                 scope='Location metadata only. Before-PDF scopes are preserved per row; old intermediate wording receives no invented original-page locus. Current retained contexts are explicitly distinguished from exact phrase ranges.')
    receipt_path=run/'S6_SERIES_PUBLISH_I_defect_page_mapping.json'
    receipt_path.write_text(json.dumps(receipt,indent=2)+'\n')
    (run/'S6_SERIES_PUBLISH_I_unresolved_current_contexts.json').write_text(json.dumps(unresolved,indent=2)+'\n')
    if a.apply:
        assert not unresolved,'Resolve all source-only current contexts before application.'
        shutil.copyfile(mapped,canonical_defects)
        shutil.copyfile(receipt_path,ROOT/'records/S6_SERIES_PUBLISH_I_defect_page_mapping.json')
    print(json.dumps({k:v for k,v in receipt.items() if k!='details'},indent=2))
    print('MAPPED_TSV',mapped)


if __name__=='__main__':
    main()
