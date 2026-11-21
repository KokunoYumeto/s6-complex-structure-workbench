from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,csv
ROOT=Path(__file__).resolve().parents[4];HERE=Path(__file__).resolve().parent
DER=HERE.parent/'clean_derivations';SOURCE=ROOT/'S6_SERIES_PUBLISH_II.tex'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def ref(p):return {'path':str(p.relative_to(ROOT)),'sha256':sha(p)}
source=SOURCE.read_text();now=datetime.now(timezone.utc).isoformat();targets=[]
scopes={
'02WI':'The fresh derivation and printed proof use the same explicit free proper C-action. The orbit-to-unit-slice diffeomorphism, local Hopf quotient, integral product homology and covering-group obstruction are checked completely. WI and FC were both frozen before either target proof was released.',
'01FC':'The fresh derivation independently constructs the weighted quotient with weights 1 and sqrt(2), proves properness and compactness, constructs the fibre quotient, and proves a(H)=0 using a convergent coefficient solution of the unit cocycle. The printed proof uses a normally convergent orbit sum for the same unit cocycle; expanding that sum coefficientwise gives exactly L_I/(1-q^I). The prerelease secondary example uses m=2, sufficient for the existence statement. The full printed all-m extension and H^2(Y_m,Z)=Z/m are separately checked after release by the exact equivariant slice Y_m=S3 x L(m,1) and the integral cellular program.',
'01G9':'The frozen deduction intersects C.2.G.1 nonnegative Euler values with D.2.5 nonpositivity, uses actual fibration Euler additivity for individual supports, and takes the D.2.7 example through integral-to-rational monodromy. The original statement needs explicit smooth connected total space and a proper holomorphic map onto a smooth compact curve, which are the hypotheses of the invoked theorem. The current adjacent D2.1 scope is bound. The D2.4 statement was safely read after release to repair the literal --4 reference. No singular-total-space reading is certified.'}
for tag in ['02WI','01FC','01G9']:
    fp=json.loads((DER/f'S6_SERIES_PUBLISH_II_{tag}_freeze_pointer.json').read_text());rp=json.loads((DER/f'S6_SERIES_PUBLISH_II_{tag}_release_pointer.json').read_text())
    fpath=ROOT/fp['receipt'];assert sha(fpath)==fp['sha256'];freeze=json.loads(fpath.read_text())
    opath=ROOT/rp['full_block'];original=opath.read_text();assert source.count(original)==1,tag
    proposed=original;guards=[]
    def ch(suffix,typ,old,new,reason):
        global proposed
        assert proposed.count(old)==1,(tag,suffix,proposed.count(old))
        proposed=proposed.replace(old,new,1)
        guards.append({'change_id':'II-REC-C01-'+tag+'-'+suffix,'defect_type':typ,'old':old,'new':new,'expected_occurrences_in_owning_block':1,'reason':reason})
    enum=r'\begin{enumerate}[label={$\langle1\rangle$\arabic*.},leftmargin=*]'
    if tag=='01G9':
        ch('ENUMOPEN','D04,D23',enum+'\n'+r'\item '+'\n','','Remove the one-item iteration wrapper.')
        ch('ENUMCLOSE','D04,D23','\n'+r'\end{enumerate}','','Remove its corresponding terminator.')
    else:ch('ENUM','D04,D23',enum,r'\begin{enumerate}[label=\arabic*.,leftmargin=*]','Use ordinary step numbering without an iteration marker.')
    if tag=='02WI':
        ch('TITLE','D16','[P4.11]','[A primary Hopf bundle on a product of spheres]','Replace the coded heading; retain both permanent labels and the tag.')
        ch('STATEMENT','D01,D06',
          'Thus the torus hypothesis is\nnecessary for the equality classification as stated in the prompt.\nP4.7 proves it unnecessary for the numerical normal-crossings\nsign theorem.',
          r'The covering obstruction gives a counterexample to the smooth-support equality description of \SeriesRef{cdp:st:C.2.G.1} when its torus-fibre hypothesis is omitted. The numerical normal-crossings sign theorem \ref{night:P4.7} applies to this fibration.',
          'Replace the inaccessible prompt reference and bare code by exact theorem references; the complete covering argument establishes the asserted counterexample.')
        ch('CLOSE','D08',
          ' This proves the failure of the stated smooth-support\nclassification using the exact covering morphism.',
          '', 'The explicit finite-index group contradiction already proves the stated covering obstruction.')
    elif tag=='01FC':
        ch('TITLE','D16','Proved actual occurrence of both Hopf types','Bundles with primary and secondary Hopf fibres','Name the two constructions.')
        ch('PROPER','D08',' This proves properness.','','The preceding compact-preimage argument establishes properness.')
        ch('OPEN','D08',r'We verify $a(H)=0$ directly. A meromorphic function on $H$ lifts',r'A meromorphic function on $H$ lifts','Move the algebraic-dimension value to the proved conclusion after the complete germ computation.')
        ch('VALUE','D08',
          'therefore constant, first near the origin and then everywhere by\nanalytic continuation.',
          'therefore constant, first near the origin and then everywhere by\nanalytic continuation. Hence $a(H)=0$.',
          'Retain the exact a(H)=0 value as the mathematical conclusion of the invariant-germ argument.')
        ch('SCOPE','D11',
          'Thus these secondary\nexamples meet exactly the rational hypotheses of C.3; the primary\nexample also has',
          'The primary\nexample has',
          'Retain all displayed rational and integral groups; remove the accompanying scope recap.')
        ch('FINALLY','D08','Finally transfer of Euler characteristic','Transfer of Euler characteristic','Retain the actual finite-cover Euler operation without a process transition.')
    elif tag=='01G9':
        ch('TITLE','D16','Proved existence and exact Euler number','Euler equality under trivial torus monodromy','Name the actual equality class.')
        ch('SCOPE','D22',
          'The class of compact complex threefolds with $b_1=b_2=0$,\na proper connected-fibre map with smooth two-torus general fibre,\nand trivial rational monodromy is nonempty.',
          'The class of smooth compact connected complex threefolds with $b_1=b_2=0$,\na proper surjective holomorphic map with connected fibres onto a smooth compact curve,\nsmooth two-torus general fibre, and trivial rational monodromy is nonempty.',
          'State exactly the smooth total-space and base hypotheses used by C.2.G.1 and the frozen deduction; the adjacent current D2.1 already has smooth scope.')
        ch('STEP','D23',r'\noindent\textbf{Step 1.} ','','Remove the duplicate step marker.')
        ch('INDEPENDENT','D08','and the independent\ntrivial-monodromy upper bound','and the\ntrivial-monodromy upper bound','Keep the two numerical bounds without an unsupported process characterization.')
        ch('LOCAL','D06,D08',
          r'\ref{cdp:st:D.2.3}--4 also'+'\ngive a separate local proof of the equality when all supports\nhave normal crossings.',
          r'The monodromy obstruction of \ref{cdp:st:D.2.3} gives the normal-crossings equality in \ref{cdp:st:D.2.4}.',
          'Resolve the literal --4 to the exact safely read statement and express the mathematical input relation.')
    oc=HERE/f'S6_SERIES_PUBLISH_II_{tag}_original.tex';pc=HERE/f'S6_SERIES_PUBLISH_II_{tag}_proposed.tex';oc.write_text(original);pc.write_text(proposed)
    dp=ROOT/freeze['frozen_derivation_path'];assert sha(dp)==freeze['derivation_sha256']
    targets.append({'tag':tag,'statement_owner':freeze['statement_owner'],'freeze_receipt':ref(fpath),'frozen_derivation':ref(dp),'release_receipt':{'path':rp['receipt'],'sha256':rp['sha256']},'original_full_block':ref(oc),'proposed_full_block':ref(pc),'guards':guards,'actual_complete_original_proof_read':True,'actual_complete_proposed_proof_read':False,'comparison':scopes[tag],'checker':'i_provenance_recovery','proposed_event_counts':{'targeted proof check':1,'used and rechecked in this run':1},'source_application_pending':True,'events_added':0})

ledger=ROOT/'CHECK_EVENTS.tsv';owners=[x['statement_owner'] for x in targets]
with ledger.open() as f:rows=[{'line':i,'row':r} for i,r in enumerate(csv.DictReader(f,delimiter='\t'),2) if r['statement_id'] in owners]
search=HERE/'S6_SERIES_PUBLISH_II_clean_group01_prior_associations.json'
search.write_text(json.dumps({'created_utc':now,'ledger':ref(ledger),'rows':rows,'scope':'Only exact three owner associations, examined after each clean freeze and release; whole shared E_checks.py remains closed.','events_added':0},indent=2)+'\n')
program=HERE/'S6_SERIES_PUBLISH_II_01FC_postrelease_lens_complex.py';output=program.with_suffix('.output.json')
assert json.loads(output.read_text())['all_assertions_passed']
bundle={'schema_version':1,'paper':'II','checker':'i_provenance_recovery','created_utc':now,'canonical_source_at_review':ref(SOURCE),'targets':targets,'prior_associations':ref(search),'postrelease_program':ref(program),'postrelease_output':ref(output),'program_method_scope':'For the ancillary all-m FC integral groups, equivariant slice descent identifies Y_m with S3 x L(m,1); the tensor cellular boundary has entries m and -m and computes the actual quotient Z/m. This is a postrelease supplement to the printed transfer/UCT route, with zero extra independent credit. No prior operative routine is identified by the three printed proofs; any positive prior-program association still requires explicit comparison.','g9_current_smooth_scope':ref(HERE.parent/'S6_SERIES_PUBLISH_II_01G9_D21_current_scope.tex'),'g9_D24_statement_input':ref(DER/'S6_SERIES_PUBLISH_II_G9_D24_safe_input.tex'),'status':'Final complete proposed proof rereading pending.','canonical_mutations':0,'events_added':0}
path=HERE/'S6_SERIES_PUBLISH_II_clean_group01_proposals.json';path.write_text(json.dumps(bundle,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'proposal':ref(path),'guards':sum(len(x['guards']) for x in targets)},indent=2))
