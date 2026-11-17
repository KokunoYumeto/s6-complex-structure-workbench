#!/usr/bin/env python3
"""Add every restored PUSH passage and neighbors, then compare with build22."""
from pathlib import Path
import hashlib
import importlib.util
import json
import re
import subprocess

D=Path(__file__).resolve().parents[2]
HASH='3da988a3aeb104e3e2aba87b847ac44fdd56b27027d0fb41606398a76cfb7588'
SOURCE_HASH='234bc439e17c7c00012ab3423e975fc7794dc290b0e90ca0c0bc676bbbe8bd12'
DEST=D/'validation'/('III_'+HASH[:12])
PDF=D/'S6_09_PAPERS_III.pdf'

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def norm(s):return re.sub(r'[^a-z0-9]','',s.casefold())

def main():
    assert sha(PDF)==HASH
    tex=D/'S6_09_PAPERS_III.tex';assert sha(tex)==SOURCE_HASH
    source=tex.read_text()
    base=DEST/'render_manifest.json';m=json.loads(base.read_text())
    assert m['pdf_sha256']==HASH
    records_path=D/'records/III_final_push_prose_restoration.json'
    events=json.loads(records_path.read_text())['events'];assert len(events)==11
    anchors=[
        ['For the marked family'],
        ['the specified descended analytic filling'],
        ['that excluded analytic filling'],
        ['the existence of a particular geometric coboundary requires a separate construction'],
        ['not the invariant','of the original mapping torus'],
        ['model supplies the excluded analytic filling of the original six-sphere'],
        ['specified analytic filling excluded by Paper I','Theorem21.58'],
        ['specified analytic filling excluded by Paper I','Theorem21.58'],
        ['Counterexample: the specified analytic filling premise'],
        ['The descended analytic filling excluded by Paper I','and its proposed resolution'],
        ['The final paragraph below also proves nonextension of the raw invariant-circle coordinate'],
    ]
    texts=(DEST/'extracted_text.txt').read_text().split('\f')
    if not texts[-1].strip():texts.pop()
    assert len(texts)==m['pages']==1004
    page_keys=[norm(t) for t in texts]
    selected={r['page']:dict(r,reasons=list(r['reasons'])) for r in m['rendered']}
    loci=[];extra=[]
    for i,(event,phrases) in enumerate(zip(events,anchors)):
        assert source.count(event['before'])==0,(i,'old source phrase retained')
        assert source.count(event['after'])>=1,(i,'restored source phrase absent')
        pages=[j+1 for j,p in enumerate(page_keys) if all(norm(q) in p for q in phrases)]
        assert pages,(i,event['source_id'],phrases)
        neighbors=sorted({q for p in pages for q in [p-1,p,p+1] if 1<=q<=len(texts)})
        loci.append({'event_index':i,'source_id':event['source_id'],'exact_after':event['after'],
                     'pdf_text_anchors':phrases,'actual_text_matching_pages':pages,
                     'selected_matching_and_adjacent_pages':neighbors})
        for p in neighbors:
            why=f"Exact restored PUSH passage{event['source_id']} (record{i}); text-matched page or immediate neighbor"
            if p in selected:
                selected[p]['reasons'].append(why);continue
            prefix=DEST/f'page_{p:04d}'
            command=['pdftoppm','-f',str(p),'-l',str(p),'-r','110','-png','-singlefile',str(PDF),str(prefix)]
            run=subprocess.run(command,capture_output=True,text=True)
            assert run.returncode==0,(command,run.stderr)
            selected[p]={'page':p,'file':str(prefix.with_suffix('.png').relative_to(D)),'reasons':[why]}
            extra.append({'page':p,'command':command,'exit_code':run.returncode,'stderr':run.stderr})
    sup=dict(m)
    sup['rendered']=[r for p,r in sorted(selected.items())]
    sup['base_render_manifest']=str(base.relative_to(D));sup['base_render_manifest_sha256']=sha(base)
    sup['supplementary_restored_PUSH_loci']=loci
    sup['supplementary_render_runs']=extra
    sup['restoration_record_sha256']=sha(records_path)
    sup['contacts_note']='Base contacts cover the original renderer selection. The final delta comparison generates four-page contacts for every changed/new page in this expanded selection.'
    path=DEST/'render_manifest_with_push_restorations.json'
    path.write_text(json.dumps(sup,indent=2,ensure_ascii=False)+'\n')
    module_path=D/'code/maps_audit/compare_III_final_render.py'
    spec=importlib.util.spec_from_file_location('exact_visual_delta',module_path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    module.OLD=D/'validation/III_2cfadc0d4d62'
    module.NEW=DEST;module.OUT=DEST/'maps_changed_review'
    module.EXPECTED=HASH
    module.PRIOR_REVIEW=module.OLD/'maps_changed_review/final_visual_review_build22.json'
    module.CURRENT_MANIFEST=path
    module.main()
    print('Restored PUSH passages',len(loci),'extra rendered pages',len(extra),'combined selection',len(selected))

if __name__=='__main__':main()
