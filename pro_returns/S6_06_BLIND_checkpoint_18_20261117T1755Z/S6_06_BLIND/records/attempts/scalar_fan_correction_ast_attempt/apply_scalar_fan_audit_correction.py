"""Preserve and explicitly reopen compound claims depending on the false product."""
from datetime import datetime,timezone
from pathlib import Path
import ast,csv,hashlib,json,re,shutil

root=Path(__file__).resolve().parents[1]
dest=root/'records/attempts/scalar_fan_premise_correction'
dest.mkdir(parents=True,exist_ok=False)
scope={
 'P3K.17':('notes/part3_fourfold.tex',
  'The OS49 extra fixed-normal boundary must retain its own outer collar arrows. The whole-I1 obstruction does not compute that separate correction. The claimed complete two-fan equality is reopened pending that explicit outer-marking audit.'),
 'P3K.25':('notes/part3_whole_i1_shear.tex',
  'The outer C1 normal comparison has determinant winding -2M at one branch and zero at the other. The earlier inner common-gauge calculation does not establish the asserted vanishing of the extra fixed-normal boundary. The all-shear equality below is withdrawn. The direct initial/reflected C2 comparison is repaired separately in P3K.62.'),
 'P3K.29':('notes/part3_common_exterior_meridians.tex',
  'The simultaneous periodic marked delta-equivariant product invoked in Section 3 is obstructed for nonzero scalar winding M: its exact determinant equations give -M=0. The scalar rank-one variation and zero nonfixed derivative conclusions are withdrawn. The integral cells, meridian and dual-basis maps, variation symmetry, and exact frame-change formula remain separate valid calculations.'),
 'P3K.31':('notes/part3_common_exterior_frame_recurrence.tex',
  'The scalar initial variation and derivative vector used for the universal fan recurrence depend on the obstructed product in P3K.29. The universal scalar-fan polynomial and its ranges below are withdrawn. The explicitly computed single-star product-frame arrow, boundary flop and complex normal reset remain available in their stated local markings.'),
 'P3K.33':('notes/part3_original_cox_descent.tex',
  'The explicit parameter/root/cap descent and individual reference fixed-star comparison are retained. The all-fan application of P3K.31 and its numerical range are withdrawn; a simultaneous equivariant product of the full marked plumbing cannot be supplied merely by the fixed-star product.'),
 'P3K.34':('notes/part3_os49_full_framing.tex',
  'The component-supported source, line and individual reference characteristic calculation are retained. Section 6 imports the unverified full-plumbing product and P3K.29/P3K.31 recurrence. Its universal fan expression and range are withdrawn. The separate OS49 outer markings require their own audit.'),
 'P3K.35':('notes/part3_weighted_shorter_loop.tex',
  'The actual finite-root, line, period, cyclic norm and shorter-parameter morphisms are retained, together with their independent reference fixed-star calculation. The all-fan application of P3K.31 is withdrawn. No simultaneous equivariant full-plumbing product is inferred from the individual closed star.'),
 'P3K.36':('notes/part3_liu_rollenske_parameter.tex',
  'The intrinsic one-u endpoint obstruction and the actual corrected degree-two family are retained. The displayed universal fan formula depends on P3K.31 and is withdrawn. The independently constructed reference fixed-star result is not replaced by that formula.'),
 'P3K.37':('notes/part3_os49_shorter_loop.tex',
  'The actual shorter scalar descent, cap/cusp endpoint maps and their reference calculation are retained. The universal fan expression and associated range inherit the P3K.31/P3K.34 product issue and are withdrawn.'),
 'P3K.41':('notes/part3_fixed_source_cap_loops.tex',
  'The actual marked cap-data comparison, necessary scalar winding, fixed-scalar triviality and reduction to an integer iterate of the constructed shorter return are retained. Its displayed numerical universal fan expression imports P3K.31 through P3K.35 and is withdrawn.'),
 'P3K.43':('notes/part3_moving_order_one_sites.tex',
  'The moving-site family morphism, fixed-scalar triviality and actual reduction to a shorter scalar return are retained. The numerical universal fan polynomial inherited from P3K.35/P3K.41 is withdrawn.'),
 'P3K.44':('notes/part3_os49_cap_loops.tex',
  'The actual component-line cap comparison, scalar winding and reduction to an iterate of the constructed OS49 return are retained. The numerical universal fan expression inherited from P3K.37 is withdrawn.'),
 'P3F.52':('notes/part3_vertical_line_exhaustion.tex',
  'The actual invariant-divisor, source-line, root-evaluation and collar morphisms are retained. The claimed preservation of the particular numerical all-fan formula imports P3K.31, whose scalar initial data are withdrawn. A family isomorphism preserves actual returns but does not prove that unsupported formula.'),
 'P3F.53':('notes/part3_canonical_scalar_catalogue.tex',
  'The source-pair and root tables, cap topology, exact endpoint constructions and independent reference page/line values are retained. The all-fan polynomial fields and ranges import P3K.31 and are withdrawn pending a corrected actual scalar product computation.')
}
saved={}
for name in sorted({v[0] for v in scope.values()}|{'S6_06_BLIND_paper.pdf','S6_06_BLIND_paper.log','S6_06_BLIND_report.md','S6_06_BLIND_results.csv','code/update_report.py'}):
    p=root/name
    out=dest/name
    out.parent.mkdir(parents=True,exist_ok=True)
    shutil.copy2(p,out)
    saved[name]=hashlib.sha256(p.read_bytes()).hexdigest()
for sid,(name,reason) in scope.items():
    p=root/name;text=p.read_text()
    marker='\\begin{statement}{'+sid+'}{Proved}'
    assert text.count(marker)==1,(sid,name)
    notice=('\n\\par\\noindent\\textbf{Audit correction, 17 November 2026.} '
      +reason+' The formulas and earlier argument below are retained as the audited prior claim, not as current proved conclusions. See P3K.61--62 and the correction ledger.\n\\medskip\n')
    replacement='\\begin{statement}{'+sid+'}{Unresolved; scalar-fan audit correction}'+notice
    text=text.replace(marker,replacement,1)
    after=text.index(replacement)+len(replacement)
    pos=text.index('\\begin{proof}',after)
    text=text[:pos]+text[pos:].replace('\\begin{proof}',
      '\\begin{proof}[Preserved earlier argument; scope corrected above]',1)
    p.write_text(text)

p=root/'code/update_report.py';text=p.read_text();tree=ast.parse(text)
items=next(n.value for n in tree.body if isinstance(n,ast.Assign)
           and any(isinstance(t,ast.Name) and t.id=='ITEMS' for t in n.targets))
entry=next(v for k,v in zip(items.keys,items.values()) if k.value=='3.4')
old_ids=ast.get_source_segment(text,entry.elts[0])
old_state=ast.get_source_segment(text,entry.elts[1])
new_ids='P3F.1–P3F.56, P3K.5–P3K.38, P3K.40–P3K.62; reopened compound assertions identified below'
new_state='INCOMPLETE, with a newly located proof error. The exact fixed-source construction, source/root/cap topology, initial page and line calculations, actual shorter-parameter morphisms, minimal scalar covers, and marked cap-data comparisons remain in their stated independently proved scopes. The reference OS45 family has class25 and its positive covers realize every class in Theta7; the stated universal vanishing is therefore refuted independently of the withdrawn fan recurrence. The fixed-source catalogue retains sixteen profiles, twenty-six source pairs, thirty-one root branches with thirty nonempty branches, and its exact reference values. However P3K.61 proves that the simultaneous marked delta-equivariant three-curve product used in P3K.29 cannot exist for nonzero scalar winding M. The actual outer C1 determinant winds-2M at one branch and0 at the other. P3K.25, P3K.29 and P3K.31 therefore require correction, and the all-fan portions of P3F.52–53 and P3K.33–37,41,43–44 are explicitly reopened. The analogous OS49 outer-marking assertion in P3K.17 is under its own audit. Every earlier proof and audit is preserved, and the affected compound statement labels are Unresolved. P3K.62 supplies the literal scalar C1/C2 native maps, their actual relative squares and the narrow C2 characteristic comparison; it repairs the initial/reflected scalar equality used in P3K.57–58 without the withdrawn universal assertion. The selected-cusp source-loop results P3F.55–56 and P3K.40,42,45–60 use their separately constructed products and the retained local topology/frame arrows. They include the initial class1, fixed-edge class23, ordinary variation and derivative, unselected collision class0, the full vertical-edge source return1-3n(n-1), and the two exact infinite families in P3K.59. For P_j=[[1,-j],[0,1]], j>=0, the class is1-3j(j+1), with its full matrix and derivative; for R_j=[[j+1,-j],[-1,1]], the class is-5-24j(j+1), with least period7 and range{3,15,19,23}. P3K.57 gives the actual source-infinity classes0 and1 on the initial/reflected fans, with the corrected N-5/N-6 analytic bounds and safe geometric orders8 and6. P3K.58 gives the full global groupoid and paired source-zero sums. P3K.60 gives the actual single native pair(1-a,a) and difference Z_JT-Z_T=a. The remaining ordered pair is(-a+k*A_scalar+14e,k*A_scalar+14e), e in{0,1}, with A_scalar=0 or1-3p; no e is selected. The smallest good case is(27,0) or(13,14), and reduced p=k=1 gives(24,26) or(10,12). The source-zero global central attachment, full sheared fixed-star characteristics, corrected scalar-fan returns, remaining source-moduli loops, added ordinary OS49 clutches and unmarked endpoint sectors remain under proof.'
text=text.replace(old_ids,repr(new_ids),1).replace(old_state,repr(new_state),1)
text=text.replace('The original reference-fan class is zero with every orientation convention fixed; P3K.33 supplies its explicit all-fan extension.',
 'The original reference-fan class is zero with every orientation convention fixed. The all-fan extension previously asserted in P3K.33 is reopened by the scalar-product audit P3K.61; the reference-fan proof is retained.')
tree=ast.parse(text)
long_value=next(x for n in tree.body if isinstance(n,ast.AugAssign)
 and isinstance(n.target,ast.Name) and n.target.id=='lines' and isinstance(n.value,ast.List)
 for x in n.value.elts if isinstance(x,ast.Constant) and isinstance(x.value,str)
 and x.value.startswith('The exact outstanding instances'))
old=ast.get_source_segment(text,long_value)
provenance=('The exact outstanding instances, attempted constructions and failures remain in the part notes, working proofs and code outputs. This checkpoint includes an explicit post-checkpoint14 scalar-fan correction. '
 +new_state+
 ' The correction ledger is records/scalar_fan_correction_scope.json, with complete prior files under records/attempts/scalar_fan_premise_correction/. The local common-exterior integral topology and single-star frame arrows remain separately audited and are the only portions of K29/K31 used by the new source-loop proofs. The exploratory second mutation seed is also preserved; the active certificate starts only from the proved initial seed and checks210 bases and128 fans. '
 'The unrestricted non-normal-crossing extensions of the supplied Part4 assertions, unidentified extra numerical rows, and any broader claims outside the explicit theorem scopes remain undecided. Part4.2 is proved in its requested irreducible or normal-crossing scope. Parts1,2 and the original blind Part5 retain their recorded proofs and immutable blind hashes. No uncomputed class, missing global filling, or unsupported integer lift is assigned.')
text=text.replace(old,repr(provenance),1)
ast.parse(text);p.write_text(text)
record={'utc':datetime.now(timezone.utc).isoformat(),'status':'CORRECTION_APPLIED',
 'reason':'The exact scalar determinant obstruction invalidates the full-plumbing product premise, and the actual outer C1 line is missing from the earlier zero-boundary calculation.',
 'scope':{sid:{'file':name,'status':'Open','correction':reason} for sid,(name,reason) in scope.items()},
 'retained_local_results':['K29 integral cells, bases and symmetry','K29 exact frame-change identity','K31 local product-frame, native boundary and complex reset maps'],
 'narrow_repair':'K62 actual C2 comparison replaces K25 only for the initial/reflected scalar equality.',
 'prior_master_build':50,'preserved_files':saved,
 'independent_audits':['records/root_audit_scalar_consistency.json','notes/part3_scalar_outer_clutch_audit.md','notes/part3_scalar_consistency_dependencies.md']}
(root/'records/scalar_fan_correction_scope.json').write_text(json.dumps(record,indent=2)+'\n')
print('Preserved build50 and earlier arguments; reopened',len(scope),'compound statements with precise correction notices.')
