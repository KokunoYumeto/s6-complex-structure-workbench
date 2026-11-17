"""Integrate the independently derived ninth-hour statements and audit records."""
from pathlib import Path
from datetime import datetime,timezone
import json
R=Path(__file__).resolve().parents[1]
now=datetime.now(timezone.utc).isoformat()
p=R/'notes/part3.tex';s=p.read_text()
new=[
 'part3_starred_caps','part3_ordinary_additive_caps','part3_ii_caps',
 'part3_additive_affine_exhaustion','part3_primitive_multicap',
 'part3_iv_star_iii_joint','part3_iii_star_ii_joint']
insert=''.join('\\input{notes/'+x+'.tex}\n' for x in new)
if '\\input{notes/part3_starred_caps.tex}' not in s:
    s=s.replace('\\input{notes/part3_fourfold.tex}',insert+'\\input{notes/part3_fourfold.tex}')
for x in ['part3_additive_returns','part3_primitive_cox_framing']:
    line='\\input{notes/'+x+'.tex}\n'
    if line not in s:s+=line
p.write_text(s)

audits={
 'part3_additive_cap_final_audit':{
  'statements':['P3F.41','P3F.42','P3F.43','P3F.44'],
  'independent_auditors':['root','fourfold','checks'],
  'checks':['All eleven actual Weierstrass root substitutions, retained marked sections and component labels.',
   'Exact r3/r4 common toric resolutions, Cartier support functions and exceptional corrections.',
   'All good II/III/IV blowup, quotient, contraction and fibre multiplicity matrices, with source section locations.',
   'Exact resolved line comparison and retained central torsion Picard character; actual commuting line norms.',
   'Full source/boundary cones and retained-kappa integer gluing matrices, including finite torsion targets.',
   'Source conjugation solves (1-D)T=Z in the actual analytic section group, with exact reduced and good-root division.',
   'Extending degree-zero line lift commutes with B; the remaining finite delta character and boundary gauge are retained.'],
  'certificates':['code/part3_root/additive_cap_root_audit.py','code/part3/iii_star_good_complement.py',
   'code/part3/iv_star_complement.py','code/part3/ordinary_additive_boundary.py','code/part3/ii_cap_boundary.py']},
 'part3_additive_returns_final_audit':{
  'statements':['P3K.26'],
  'independent_auditors':['root','fourfold'],
  'checks':['Physical outward gamma and ordinary-to-cap arrow give the exact signed inverse closing and two origins.',
   'Both n=+1 and n=-1 maps identify the actual Seifert gluing with weighted S3; beta=n gamma is the positive physical loop.',
   'The sheet-zero graph identifies the complete resolved root source and its actual line, retaining all deck characters.',
   'Integral monodromy coinvariants vanish by the exact invariant-torsion-section contradiction to MW=Z. Retained source meridians lift as closed loops in a cut page sector.',
   'Relative period two-cocycle and Lie-sheaf comparison fixes the binding; rigidified Hom evaluation precedes its pullback by smooth translations.',
   'Actual page boundary, compression boundary, Hopf normal and Thom orientation give the same signed index for both norm signs.',
   'All sixteen chi, height, line-square and return rows checked exactly; auxiliary cusp base root is not a parameter cover.'],
  'history':'The earlier inference from vanishing-cycle span to full integral monodromy coinvariants was corrected before promotion. The torsion-section proof retains every (T-I) multiplicity.',
  'certificates':['code/part3/additive_returns.py','code/part3_fourfold/signed_cap_page.py']},
 'part3_primitive_multicap_final_audit':{
  'statements':['P3F.45'],
  'independent_auditors':['root','checks'],
  'checks':['Ordinary primitive cap traces and section boundary make the full degree-two ordinary map an integral isomorphism.',
   'Actual inversion makes every ordinary kernel odd and every boundary core even, giving simultaneous zero core columns in free exterior H2.',
   'All smooth exterior powers and exact multiplicative isotropy blocks retain every elliptic and cap path coefficient.',
   'Ordinary degree-three sequence gives the free even kernel modulo the single primitive sum of source-boundary classes. All odd Fgamma images coincide integrally.',
   'Actual multiplicative H1/H3 pairing yields cap row (-n,m,j), and smooth wedge cube yields (-n,m,-lambda_b,lambda_a).',
   'Complete D0--D4 matrices reduce to local (Z/m)^2 blocks and the exact Seifert matrix; every effective smooth/multiplicative sphere order is one.',
   'The actual vanishing-cycle normal subgroup is killed before the residual Seifert presentation; with at most one additive site it is cyclic of the stated determinant.'],
  'certificates':['code/part3_root/primitive_multicap_blocks.py','code/part3_root/primitive_multicap_complete.py']},
 'part3_iv_star_iii_joint_final_audit':{
  'statements':['P3F.46'],
  'independent_auditors':['root','blind_control'],
  'checks':['All four exact E6+A1 source pairs and good/reduced root domains.',
   'Actual starred toric and ordinary good-root line correspondences; central torsion and character norms retained.',
   'Joint punctured-disc family has exact global inverse closing with both local orders and cusp gamma coefficient.',
   'Complete integral source and boundary cone, all raw Smith representatives and actual marked alpha,gamma,N,Fgamma cycles.',
   'Arbitrary-kappa D2 maps are mixed-group isomorphisms for b=6,3,2,1. D1 and D3 have determinant -(m2*n6+m6*n2).',
   'Remaining nodal cycle and its cap-monodromy conjugate form an elliptic basis; full van Kampen gives the cyclic determinant group.',
   'All D=0 groups and all D0--D4 maps retained; standalone six-page visual audit passed.'],
  'certificates':['code/part3/iv_star_iii_joint.py']},
 'part3_primitive_cox_framing_final_audit':{
  'statements':['P3K.27'],
  'independent_auditors':['root','checks'],
  'checks':['The actual cusp origin cancels the bounded representative-cell closing; the annular transition is exactly the marked gamma flow.',
   'The fixed source-preserving positive product Phi makes J_theta=R_theta Phi an exact smooth orbit-family comparison, including the node endpoints.',
   'The actual normal derivative is parameter-independent and triangular with positive gamma scalar; its contraction is intrinsic on the normal exact sequence.',
   'Explicit quaternion normal coordinates agree literally across the two O(-1) plus O(-1) charts, retaining the physical Hopf orientation.',
   'The unitary toric action has literal q_H -> A q_H B form; its remaining constant loop extends over the fixed three-disc.',
   'Full degree-one graph/compression normal clutch factorization gives p1(normal)=0, hence k=-3d, ell=-24 and exact relative tuple (6,3d-6,1-d/2).'],
  'certificates':['code/part3_fourfold/primitive_cox_framing.py','code/part3_fourfold/primitive_normal_clutch.py']}
}
for name,obj in audits.items():
    obj.update(status='PASS',audited_utc=now)
    (R/'records'/(name+'.json')).write_text(json.dumps(obj,indent=2)+'\n')

p=R/'code/update_report.py';s=p.read_text()
s=s.replace('P3F.16–P3F.40, P3K.6–P3K.25','P3F.16–P3F.47, P3K.6–P3K.27')
old='Simultaneous cap tuples, the remaining additive partners and return indices on finite-isotropy fan branches remain under proof.'
newtext=('P3F.41–44 construct and classify the remaining one-cap additive roots and exact affine line lifts. '
 'P3F.45 gives the simultaneous primitive-source degree-two obstruction and complete sphere criterion, with every integral gluing degree. '
 'P3F.46–47 prove all four IVstar/III pairs and both IIIstar/II pairs, including their exact joint determinant, line norms and all integral maps. '
 'P3K.26 supplies the actual signed page, line and return index for sixteen one-cap additive rows, for both norm signs. '
 'P3K.27 identifies the primitive-family rotating and Cox normal framings and computes (k,ell)=(-3d,-24) and relative coordinates(6,3d-6,1-d/2). '
 'Joint additive return pages, the remaining weighted extra-site exclusions, global order-one parameter cochains and finite-isotropy fan return branches remain under proof.')
s=s.replace(old,newtext)
p.write_text(s)

log=R/'S6_06_BLIND_literature_log.md'
with log.open('a') as f:
    f.write('\n| '+now+' | Supplied prompt and E26 S6.tex closing Remark8.5, reread during 08:00–08:06 UTC | Check exact scope before simultaneous-cap promotion | Retained the literal whole-fibre Hom condition, exact finite-kernel cancellation, every elliptic norm coefficient, and the hourly checkpoint rule. No earlier-run proof opened. Timestamp here records this retrospective log entry. |\n')
    f.write('| '+now+' | Current-run additive roots, signed pages, primitive simultaneous caps, E6 joint cone and Cox normal comparison | Independent root and reciprocal agent proof audits | Exact root/line maps, integral torsion matrices, monodromy-coinvariant correction, signed Thom maps, and complete normal frames passed; detailed records are the corresponding final_audit JSON files. |\n')
print(json.dumps({'integrated':new+['part3_additive_returns','part3_primitive_cox_framing'],
                  'audit_records':list(audits),'time':now}))
