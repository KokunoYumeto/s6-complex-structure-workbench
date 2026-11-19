"""Promote the audited K78 proof and update the precise K75 working gates."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil

root=Path(__file__).resolve().parents[1]
now=datetime.now(timezone.utc).isoformat()
source=root/'notes/part3_os49_order_one_clutches.tex'
sha=hashlib.sha256(source.read_bytes()).hexdigest()
manifest=json.loads((root/'records/k78_export_manifest.json').read_text())
qa=json.loads((root/'records/k78_standalone_visual_qa.json').read_text())
assert sha==manifest['include_sha256']==qa['tex_sha256']
assert qa['status']=='PASS'
audit={
 'utc':now,'status':'PASS','reviewer':'root','statement':'P3K.78',
 'tex_sha256':sha,
 'proof_review':[
  'Complete actual monodromy matrices and extending-period stalks; full order-m root group retained.',
  'Integral 14-by-24 total degree-two relations, primitive kernel preimages, norm, torsion, and full redistribution cochain.',
  'Signed smooth and finite meridians, norm D=n+m sigma, same root quotient and unchanged finite character.',
  'Actual Laurent/Cauchy Lie solution; source, line, cusp-fan, II and finite-root maps and inverses.',
  'Explicit Isom connection, angular scalar correction, radial ODE with its correct transition sign, and holomorphic Cauchy correction.',
  'Literal parameter period monodromy; canonical forward endpoints, typed inverse-endpoint conjugacy and specified transported shorter endpoint.'
 ],
 'certificate':'code/part3/os49_order_one_groupoid.json',
 'certificate_checks':manifest['certificate_checks'],
 'standalone_visual_qa':'records/k78_standalone_visual_qa.json',
 'root_additional_full_page_views':[2,6],
 'scope':'Fixed marked smooth order-one translation clutches on the exact OS49 source; all stated free root data and same fans. No unproved broader endpoint or singular-site assertion.'
}
(root/'records/root_audit_os49_order_one_clutches.json').write_text(json.dumps(audit,indent=2)+'\n')
archive=root/'records/checkpoint18_prior_master60'
archive.mkdir(exist_ok=False)
for name in ('S6_06_BLIND_paper.pdf','S6_06_BLIND_paper.log','notes/part3.tex',
             'notes/part3_remaining_return_obligations.tex','code/update_report.py',
             'code/part3/results_mapping.json'):
    dest=archive/name; dest.parent.mkdir(parents=True,exist_ok=True)
    shutil.copy2(root/name,dest)
p=root/'notes/part3.tex'; text=p.read_text()
assert '\\input{notes/part3_os49_order_one_clutches.tex}' not in text
p.write_text(text+'\n\\input{notes/part3_os49_order_one_clutches.tex}\n')

p=root/'notes/part3_remaining_return_obligations.tex'; text=p.read_text()
old='''Other remaining parts of item 3.4 are the added ordinary-clutch
sectors, the remaining marked source-moduli loops, and unmarked
endpoint sectors. No value is assigned here to those sectors.'''
new=r'''K78 additionally computes all fixed marked smooth order-one
translation clutches of that source. Its full integral cochain
and holomorphic family maps carry them to the exact one-cap norm
\(D=n+m\sum_i\psi(\ell_i)\), retaining the character and the
parameter-closing arrows. The sphere sectors \(D=\pm1\) have the
K77 canonical return and specified transported shorter return.
Remaining parts of item 3.4 include the further ordinary and
singular-site sectors beyond that scope, the remaining marked
source-moduli loops, and unmarked endpoint sectors. No value is
assigned here to those sectors.'''
assert old in text; text=text.replace(old,new)

start=text.index('The remaining local map is the surgery joining this framed')
end=text.index('\nThere is also an exact obstruction',start)
text=text[:start]+r'''The local framed surgery is now constructed in RT.10. In the
reduced case the positive node model is the explicitly identified
total space of \(\mathcal O(-1)\oplus\mathcal O(-2)\) over
\(\mathbb P^2\), with its fixed surface and isolated charge-one
point retained. RT.13 connects its radial boundary to the
product-radius cut by the actual compact region
\(\{\rho\le\rho_0,\ R\ge\varepsilon\}\), with two small-\(R\)
arms having cores \(S^3\) and \(\mathbb{RP}^3\).

The earlier \(j=-1\) designation used the SZ chart index.
TL supplies the full source and Cartier map to the current Tate
fan, retaining
\[
 Z_0W_0=q_1q_2u_Q,\quad P=q_2^{-1}u_P,\quad
 Z=P/S=1/W_0,\quad Z_0=u_Qu_PT_0,\quad W_0=q_2S/u_P.
\]
Its valuation arrow is \((x,y,h)\mapsto(h-x,y,h)\).
The associated positive square maps to the current negative
fan \(\mathcal T_0\), and the opposite resolution to
\(\mathcal T_1\). The actual source period and its full theta
line factor occur before that valuation. The two resolution
charts and their unit inverses extend across both branches.

EA.17 gives the full two-node refinement using the normalized
Morse functions \(\alpha\beta=q_1q_2\) and exact factors
\(F_+F_-=q_1\):
\[
 S_0=F_+,\quad T_0=F_-,\quad
 S_1=-\beta/(2F_-),\quad T_1=-2\alpha/F_+.
\]
The branch-divisor argument makes both quotients holomorphic;
their Jacobian at the origin is \(4\). They give literally
\(q_1=S_0T_0\), \(q_2=S_1T_1\), and
\(\widetilde v=q_1-q_2\). The marked coefficient is multiplied
by \(\kappa^a=((S_1-S_0)/(2s_0))^a\), an extending unit;
the two original Cartier \(r\) maps are retained for \(a=2\).
''' + text[end:]
old='''The labelled
global attachment, including that cap assignment, remains
under construction.'''
new=r'''The lower arm has an actual charged-shape comparison. In its
charge-two cover put \(\sigma^2=\|x\|^2+|y|^2\) and
\(u=|y|^2/\sigma^2\). Near that arm,
\(\rho=\sigma^2\sqrt{1-u}\). Extend this positive factor
to an invariant \(f\) with \(1/\sqrt2\le f\le1\).
The ambient annulus
\[
 \{\rho_0/2\le\sigma^2\le\rho_0/f\}/\mu_2
\]
has positive width and retains the source functions by inclusion.
Its physical line is carried by the explicit Hopf map
\([u,z]\mapsto z u^{\otimes2}\) into \(\mathcal O(-2)\).
Its full quaternion charts have \(w'=w^{-1}\) and
\(u'=(w/|w|)u\), retaining the hemisphere inversion.
EA.15 gives their native ruling-quaternion comparison.
RT.15 carries the actual canonical spin lift \(+\omega_8\).

After the actual node reindex and source reset, the common
coefficient is \(U_j\). The gauge \(U_j=1\), transported to
\(V_{j-1}=1\), gives \(N_t=\|T\|^a\), \(N_s=\|S\|^{-a}\).
The transported coefficient is \(V_{j-1}^{-1}\), retaining
the \(q\) factor in the other node coordinate. Thus the entire
finite faces are
\[
 H_t=(D^4_S(r)\times S^3_T(r))/\mu_a,\qquad
 H_s=(S^3_S(r)\times D^4_T(r))/\mu_a.
\]
On \(R>0\), the actual physical factor \(d=(R/r^2)^a\)
gives \((S,T)\mapsto(d^{-1/a}S,d^{1/a}T)\), preserving
\(q_1,q_2\) and the original base functions.
The forward contracting field \(-\eta\), where
\(\eta=-S\partial_S+T\partial_T\), enters \(H_t\) and
exits \(H_s\). The oriented target-minus-source chain is
the positive product-ball boundary. Both cores are retained;
the normalization is not extended across \(R=0\).

These maps complete the local face and spin comparisons.
The global period-strip equation, its horizontal fixed cap
and the assignment of every retained or excised face remain
under audit. No source-zero integer has been assigned from
these local pairs.'''
assert old in text; text=text.replace(old,new)
old='''added ordinary-clutch sectors remain on the list above.'''
new='''fixed smooth order-one clutch sectors are now completed
by K78, including its signed norm and actual endpoint conjugacy.
The remaining scopes are stated above.'''
assert old in text; text=text.replace(old,new)
p.write_text(text)

p=root/'code/update_report.py'; text=p.read_text()
text=text.replace('P3K.5–P3K.77; exact corrected scopes below',
                  'P3K.5–P3K.78; exact corrected scopes below')
old='K75 records the exact remaining source-zero attachment, added ordinary clutches, remaining marked source-moduli loops and unmarked endpoint sectors. Its local radial surgery does not yet identify the actual product-radius end; the exceptional disk and its fixed-trace class must be assigned once in that attachment.'
new='K78 completes every fixed marked smooth order-one OS49 translation clutch by the full integral root-groupoid H2=Z plus Z/k and actual holomorphic source/line/cap maps. The signed norm is D=n+m*sum(psi(ell_i)); sphere sectors D=+/-1 have the K77 return on every fan and the specified transported shorter endpoint. K75 retains the source-zero global attachment, further ordinary/singular-site scopes, marked source-moduli loops and unmarked endpoints. Source-zero now has the exact two-node/Tate/Cartier map, both full finite faces with their oriented product-ball boundary, a positive-width charged-shape comparison and the actual spin lift. The global fixed-cap and period-strip equation remains under audit; its exceptional class and each end must be counted once.'
assert old in text; text=text.replace(old,new)
p.write_text(text)
p=root/'code/part3/results_mapping.json'; mapping=json.loads(p.read_text())
existing=[x for x in mapping.get('additional_source_loop_results',[]) if x.get('id')=='P3K.78']
if not existing:
    mapping.setdefault('additional_source_loop_results',[]).append({
      'id':'P3K.78','status':'Proved',
      'statement':'All fixed marked smooth order-one OS49 translation clutches: integral H2=Z plus Z/k, signed norm, actual family maps, sphere criterion and K77 return comparison.',
      'proof':'notes/part3_os49_order_one_clutches.tex',
      'certificate':'code/part3/os49_order_one_groupoid.json',
      'audit':'records/root_audit_os49_order_one_clutches.json',
      'scope':'All stated free root data and same fans; canonical r endpoint and specified transported shorter endpoint.'})
p.write_text(json.dumps(mapping,indent=2)+'\n')
(root/'records/k78_promotion.json').write_text(json.dumps({
 'utc':now,'status':'PROMOTED_AFTER_COMPLETE_PROOF_AUDIT','statement':'P3K.78',
 'archive':str(archive.relative_to(root)),'source_sha256':sha,'master_to_build':61,
 'open_register':'Current actual source-zero local maps recorded; global class remains unassigned.'
},indent=2)+'\n')
print('K78 integrated; master60 and prior open-register sources retained.')

