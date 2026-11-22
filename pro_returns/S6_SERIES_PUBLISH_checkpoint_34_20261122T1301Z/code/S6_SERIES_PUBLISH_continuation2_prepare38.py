from pathlib import Path
import csv,datetime as dt,hashlib,json
R=Path(__file__).resolve().parents[1]
def bind(p):return {'path':p,'sha256':hashlib.sha256((R/p).read_bytes()).hexdigest()}
def read(p):return json.loads((R/p).read_text())
proposal='agents/continuation2_C/S6_SERIES_PUBLISH_II_C2_group02_proposals.json';p=read(proposal)
index='agents/continuation2_C/S6_SERIES_PUBLISH_II_C2_group02_final_index.json';idx=read(index)
assert idx['historical_program_method_comparison_complete']
assert p['full_proposed_reading_pending'] is False
review='records/S6_SERIES_PUBLISH_II_root_continuation2_batch38_review.json';assert not (R/review).exists()
(R/review).write_text(json.dumps(dict(created_utc=dt.datetime.now(dt.timezone.utc).isoformat(),
 checker='GPT-6 Astra (OpenAI), ChatGPT Pro mode, root, second continuation',
 actual_reading='Complete original/proposed five-item 033G and seven-item 033H proofs, both frozen derivations, full comparison and the historical/new HRR method comparison read. The original 033H block was reread separately after an initial output limit cut its middle.',
 mathematical_review=[
 '033G: the support cohomology Thom map corresponds under duality to the fundamental/linking-class map in Alexander duality, giving b1 of the complement equal to the total component count. The graph-base Leray edge sequence retains precisely the invariant subspace. Its rank at most one and the lower component bound force equality and trivial monodromy. Each horizontal Cartier section is a non-zero-divisor on every local branch. Pullback along resolution-normalization-inclusion preserves its nonempty effective zero divisor but has zero c1; its positive Kahler integral is the contradiction. The same composite applies component by component to a connected reducible fibre. The negative-slope canonical identity kills all plurigenera, and exact surface classification gives b1=1.',
 '033H: Krull intersection, normalization continuation and finite-dimensional stabilization prove eventual negative-twist section vanishing on a reduced irreducible support; the ideal-power filtration proves it on every entire thickened fibre. All associated-prime claims use the Cartier Cohen-Macaulay fibre. Flatness over the smooth curve and Gorenstein adjunction give the precise duality map. Nested closed bad sets and compactness give a uniform twist; top base change and positive base twist give H2=H3=0. The exponential-sequence isomorphism makes the affine Picard path an explicit holomorphic family. Local finite free complexes make each jumping locus analytic, so one point avoids all three endpoint-proper loci. Topologically trivial twists preserve HRR, while the independently expanded tangent index is c3/2=1, yielding the contradiction.',
 'Computation separation: the historical routine inserts the Chern-class ch/td polynomials and a scalar twist. The new routine constructs the Todd product and Chern character from three independent roots. Substitution l=0,c1=x+y+z,c2=xy+xz+yz,c3=xyz identifies their integrands exactly. The tangent coefficient is c1^3/2-19c1c2/24+c3/2. Shared exact-algebra software does not create an extra independent group; only the distinct root construction is credited.'
 ],statement_changed=False,page_reading_credit=0,evidence=[bind(proposal),bind(index),p['comparison'],bind('agents/continuation2_C/S6_SERIES_PUBLISH_II_C2_033H_HRR_method_comparison.md')]),indent=2)+'\n')
with (R.parent/'S6_SERIES_GRIND_tags.tsv').open() as f:pages={x['tag']:x['page'] for x in csv.DictReader(f,delimiter='\t')}
targets=[]
for t in p['blocks']:
 tag=t['tag'];prefix='agents/continuation2_C/S6_SERIES_PUBLISH_II_C2_'+tag
 targets.append(dict(owner=t['statement_owner'],tag=tag,old_page=pages[tag],original=t['original_full_block'],proposed=t['proposed_full_block'],
  freeze=bind(prefix+'_freeze.json'),release=bind(prefix+'_release.json'),events=bind('agents/continuation2_C/S6_SERIES_PUBLISH_II_C2_group02_event_proposals.json'),
  who='GPT-6 Astra (OpenAI), ChatGPT Pro mode, continuation2_C',
  guards=[dict(old=g['old'],new=g['new'],type=g['defect_type'],reason=g['reason'],occurrences=g['expected_occurrences_in_owning_block']) for g in t['guards']],
  scope='Complete frozen derivation and full comparative proof reading, preserving the entire-fibre and exact monodromy-invariant hypotheses.',
  event_note='Admitted after full root comparison and the recorded bounded historical/new HRR method comparison. Computation is postrelease and shares the target evidence group; no additional independent route or rendered-page credit.'))
source=(R/'S6_SERIES_PUBLISH_II.tex').read_text();st=source.index('\\caption{Programs and their mathematical scope.}');end=source.index('\\end{longtable}',st);last=source[:end].splitlines(True)[-1]
name='S6_SERIES_PUBLISH_II_C2_033H_HRR_postrelease.py'
row=r'Chern-root expansion of the tangent Riemann--Roch coefficient (\cref{push:src:E.2.9}) & \href{https://raw.githubusercontent.com/KokunoYumeto/s6-complex-structure-workbench/\SsixRepositoryCommit/code/'+name+r'}{\nolinkurl{'+name+r'}} \\[3pt]'+'\n'
cfg=dict(batch=38,root_review_complete=True,source_before_sha256=bind('S6_SERIES_PUBLISH_II.tex')['sha256'],ledger_before_sha256=bind('CHECK_EVENTS.tsv')['sha256'],
 review_evidence=[bind(review),bind(proposal),bind(index)],targets=targets,
 code_copies=[{'from':bind('agents/continuation2_C/'+name),'to':'code/'+name},{'from':bind('agents/continuation2_C/S6_SERIES_PUBLISH_II_C2_033H_HRR_postrelease.json'),'to':'code/S6_SERIES_PUBLISH_II_C2_033H_HRR_postrelease.json'}],
 additional_source_edits=[dict(old=last,new=last+row,type='D09',reason='Record the exact Chern-root computation once in the Programs table through the common repository macro.')],
 mathematical_repairs=[],scope='The rank-one fibre-component/monodromy argument and the horizontal-divisor exclusion with irreducible fibre supports are admitted. Both use the actual possibly nonreduced fibres, exact Cartier-section and duality maps, and the stated analytic base-change theorems. The latter has a fresh Chern-root index computation compared with the historical Chern-class routine through the exact elementary-symmetric substitution. All statement hypotheses, conclusions, formulas, labels and tags are retained; exact source locators and ordinary proof numbering replace the editorial residues.')
out='records/S6_SERIES_PUBLISH_II_continuation2_batch38_config.json';assert not (R/out).exists();(R/out).write_text(json.dumps(cfg,indent=2)+'\n');print(json.dumps(bind(out),indent=2))
