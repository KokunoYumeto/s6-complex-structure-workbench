#!/usr/bin/env python3
"""Complete K99 proof export.  All source files remain byte-for-byte unchanged."""
from pathlib import Path
import hashlib, json, re, subprocess

ROOT = Path(__file__).resolve().parents[2]
EXPECTED = 'd7180ab4503249c18237299d164817abdd70174c58bae394959c95850e99ec33'
SOURCES = [
 ('construction', 'part3_e6_order_three_source_working.md', 'The complete source, Cartier, corner and outer-transfer construction'),
 ('common_fan', 'part3_e6_common_period_fan_root_working.md', 'The actual common periodic fan and all character maps'),
 ('one_corner', 'part3_e6_p_one_cayley_working.md', 'The complete p-one corner and its 558 charts'),
 ('fixed_surfaces', 'part3_e6_order_three_fixed_surfaces_working.md', 'The 117 compact fixed surfaces and their normal clutches'),
 ('lower_surfaces', 'part3_e6_order_three_lower_surfaces_working.md', 'The four lower surfaces, nine blowups and full boundary frames'),
 ('pole_maps', 'part3_e6_two_pole_continuation_working.md', 'The chronological pole charts and complete three-period map'),
 ('surface_check', 'part3_e6_order_three_surface_aux_audit.md', 'An independent evaluation of the compact surface intersections'),
]

STATEMENT = r'''Retain the source and marked point
\[
 S_r:\ y^2=x^3+rx^2+tx+t^2,\qquad G=(0,t),\qquad s=\tfrac14-r,
\]
the point line \(M_6=\mathcal O(6G-O)\), suspension by \(-G\), and the
whole selected zero
\[
 \rho^2=1-3r,\quad \rho\text{ near }\tfrac12,\qquad
 t_+(s)=\frac{1-3\rho^2+2\rho^3}{27},\quad t_+(0)=\frac1{54},\quad
 q=t-t_+(s).
\]
Use the actual Miller section \(B_{\rm sel}=qB_6/t^3\), with the full
Cartier factors defined below. The retained whole-fibre data are
\((a,b;m)=(6,1;2)\), the primitive norm is \(n=1\), and the prescribed
quadratic finite character \((-1)^d\) and complete reference annular map
\(F_0\) are fixed. Use E64's node order \(P_{\rm sel}(0)=e^{-2\pi i/3}\),
its initial fan \(T_0\), and the original physical circle. The fixed-star charts are
\[
 q=Zc_0c_1=Z'c'_0c'_1,\qquad Z'=Z^{-1},\qquad c'_i=Zc_i;
\]
the ordered physical weights of \((c_0,c_1,Z)\) are \((-1,+1,0)\).

Choose the admitted small constants \(\epsilon,r_0\) by the explicit
uniform norm bounds of E82 and E87. On the positive source loop
\(s=\epsilon e^{2\pi i\theta}\), hold the scalar fixed at
\(\lambda=r_0^2\epsilon^4\), with its fixed quadratic root
\(r_{\rm base}=r_0\epsilon^2\). Carry the actual ordinary and finite-cap
closings, their inverses, the selected tube and its physical Hopf line.
For this completed family the physical Jin completion has
\[
 \left(\left\langle x^3,[M_f]\right\rangle,
       \left\langle p_1(TM_f)x,[M_f]\right\rangle\right)=(-27,-12),
 \qquad x=c_1(M),
\]
where \(M\) is the actual nonzero-vector physical line of P3K.68.
The resulting physical index is
\[
 A_M=\frac{4(-27)-(-12)}{24}=-4.
\]
The literal Hopf and inverse-clutch transfer of P3K.68 identifies the
oriented return with \(24\in\Theta_7=\mathbb Z/28\). This statement
records the indicated initial fan, norm, finite character, selected
node order and fixed-scalar loop.'''

OVERVIEW = r'''The proof is given in full below, including its supporting chart and
intersection calculations. The source, line and cap construction is
E61--E109. The common periodic atlas, its p-one corner, the compact
surface normal maps, the lower-surface blowups, and the finite pole
continuations are reproduced as complete companion sections. Their
equation labels are retained, so the displayed dependency arrows can
be followed without changing a frame convention.

The weighted normal-link pushforward and orbifold Stokes map used in
E102 are the maps proved in P3K.57, IE.4--7. The physical-line dual,
the two cap arrows and the first-to-second inverse-clutch convention
are P3K.68, PL.1--6. The initial E6 reference sphere and its primitive
Hopf/Gysin/Mayer--Vietoris comparison are the actual maps of P3K.95,
EC.25a--b; P3K.96--98 retain the indicated root and annular data. These
previously included proofs are used with their original source and
line arrows.

Here is the directed assembly. The three completed end fans have
520, 558 and 524 regular four-dimensional cones, identified on their
common 510-cone boundary by the full period and Cartier maps. Their
compact fixed pieces have physical pair \((-45,120)\). Every lower
surface is the executed ninefold blowup of its minimal I3 source
parent. The complete point-frame map identifies its reference
normals with \(M_6\oplus M_6^{-1}\); the actual boundary gauges add
only fibre classes whose required products vanish by E108. Each
lower double therefore contributes \((18,-27)\). The complete inner
pair is
\[
 (-45,120)+4(18,-27)=(27,12).
\]
E109 gives the actual compact relative filling and its outer boundary
map. The explicit parameter reversal preserves the physical line and
changes this pair to \((-27,-12)\) in the Jin completion. E87's full
two-parameter square and the matched cap maps identify the relative
word \((1,2)-(0,2)\) with the fixed-scalar source word \((1,0)\).
This uses the whole scalar reference once, at the level of the two
integral characteristic numbers.

The construction preserves earlier local calculations and stopped
approaches as stage records. Each local-only scope notice in those
records describes the assertion proved at that stage; E108--E109
supply the final closed-double and outer-transfer assertions. The
opening historical work-list E65 is retained in the archived source
and omitted from this proof export. No native free coordinate or
other-fan value is needed for this theorem.'''

def sha(p):
 return hashlib.sha256(p.read_bytes()).hexdigest()

def export_body(text, key):
 if key == 'construction':
  text = text[text.index('## E61.'):]
  text = re.sub(r'(?ms)^## E65\..*?(?=^## E66\.)', '', text)
  old = r'with the actual physical weights \((-1,+1,0)\).'
  # Preserve the audited source; the order clarification is in this export.
  text = text.replace(old, r'with physical weights \((-1,+1,0)\) in the ordered coordinates \((c_0,c_1,Z)\).')
  anchor = r"Z'=Z^{-1},\qquad c'_i=Zc_i,"
  if anchor in text:
   pos=text.index(anchor)
   close=text.index(r'\]',pos)+2
   text=text[:close]+'\nThe physical weight tuple in this chart is ordered as \\(c_0,c_1,Z\\): it is \\((-1,+1,0)\\).\n'+text[close:]
  text=text.replace(r''' Q_f^+=(Y\times[0,1])/((y,1)\sim(f(y),0))
 \longrightarrow
 M_f=(Y\times[0,1])/((y,0)\sim(f(y),1)),
 \qquad [y,t]\longmapsto[y,1-t].''',r''' \begin{aligned}
 Q_f^+&=(Y\times[0,1])/((y,1)\sim(f(y),0))\longrightarrow M_f,\\
 M_f&=(Y\times[0,1])/((y,0)\sim(f(y),1)),\\
 &[y,t]\longmapsto[y,1-t].
 \end{aligned}''')
 else:
  text = re.sub(r'\A# [^\n]*\n', '', text, count=1)
 # Markdown headings remain text headings and do not reset the paper counters.
 text = re.sub(r'(?m)^#{2,6} (.+)$', lambda m:r'\par\medskip\noindent\textbf{'+m.group(1)+r'}\par\nobreak', text)
 # Real paths are typed as paths, so their underscores and punctuation wrap.
 text=re.sub(r'`((?:code|records|notes)/[^`\n]+)`',lambda m:r'\path{'+m.group(1)+'}',text)
 text = re.sub(r'(?<![\w/`{])((?:code|records|notes)/[A-Za-z0-9_./*+-]+)', lambda m:r'\path{'+m.group(1)+'}', text)
 text=re.sub(r'\\\(([0-9a-f]{64})\\\)',lambda m:r'\path{'+m.group(1)+'}',text)
 result = subprocess.run(['pandoc','-f','markdown+tex_math_single_backslash+raw_tex-superscript-subscript-smart','-t','latex','--wrap=preserve'],input=text,text=True,capture_output=True,check=True)
 tex=result.stdout.replace(r'\tightlist','')
 # A tag labels the complete displayed equation, outside its inner alignment.
 def outer_tag(m):
  inner=m.group(2)
  tags=re.findall(r'\\tag\{[^{}]*\}',inner)
  assert len(tags)<=1, (key, inner)
  inner=re.sub(r'\\tag\{[^{}]*\}','',inner)
  return r'\begin{aligned}'+inner+r'\end{aligned}'+(' '+tags[0] if tags else '')
 tex=re.sub(r'\\begin\{(split|aligned)\}([\s\S]*?)\\end\{\1\}',outer_tag,tex)
 return tex

main = ROOT/'notes/part3_e6_order_three_source_working.md'
assert sha(main)==EXPECTED
audit = json.loads((ROOT/'records/root_audit_e6_order_three_outer_transfer.json').read_text())
assert audit['source_sha256']==EXPECTED and audit['status'].startswith('PASS')
peer = json.loads((ROOT/'records/blind_audit_e6_order_three_outer_transfer.json').read_text())
assert EXPECTED in json.dumps(peer)
outputs=[]
for key, name, title in SOURCES:
 src=ROOT/'notes'/name
 out=ROOT/'notes'/('part3_e6_order_three_return_'+key+'.tex')
 body=export_body(src.read_text(),key)
 out.write_text(r'\par\bigskip\noindent\textbf{K99 supporting proof: '+title+r'}\par\nobreak'+'\n'+body+'\n')
 outputs.append({'source':str(src.relative_to(ROOT)),'source_sha256':sha(src),'include':str(out.relative_to(ROOT)),'include_sha256':sha(out),'title':title})

out=ROOT/'notes/part3_e6_order_three_return.tex'
inputs='\n'.join(r'\input{'+entry['include']+'}' for entry in outputs)
out.write_text(r'\subsection{The E6 order-three source collision on the initial selected fan}'+'\n'+r'\begin{statement}{P3K.99}{Proved}'+'\n'+STATEMENT+'\n'+r'\end{statement}'+'\n'+r'\begin{proof}'+'\n'+OVERVIEW+'\n'+inputs+'\n'+r'\end{proof}'+'\n')
(ROOT/'notes/part3_e6_order_three_return_statement.md').write_text('# P3K.99: the E6 order-three source collision on its initial selected fan\n\n'+STATEMENT+'\n\n## Complete proof assembly\n\n'+OVERVIEW+'\n')
pre=(ROOT/'S6_06_BLIND_paper.tex').read_text().split(r'\begin{document}')[0]
(ROOT/'code/part3/k99_standalone.tex').write_text(pre+'\n'+r'\begin{document}'+'\n'+r'\input{notes/part3_e6_order_three_return.tex}'+'\n'+r'\end{document}'+'\n')

cert_names=[
 'code/part3/e6_collision_boundary_chain.json',
 'code/part3/e6_common_period_fan_peer.json',
 'code/part3/e6_common_corner_lift.json',
 'code/part3/e6_p_one_cayley_peer.json',
 'code/part3/e6_generic_fixed_curve_normals.json',
 'code/part3/e6_order_three_fixed_surfaces.json',
 'code/part3/e6_lower_surface_blowups_peer.json',
 'code/part3/e6_order_three_lower_surfaces.json',
 'code/part3/e6_order_three_relative_double.json',
 'code/part3_root/e6_common_period_fan.json',
 'code/part3_root/e6_order_three_surfaces_aux_peer.json',
 'code/part3_fourfold/e6_p_one_common_cayley.json',
 'code/part3_fourfold/e6_two_pole_continuation.json',
]
certs=[]
for name in cert_names:
 p=ROOT/name
 if not p.exists():
  raise FileNotFoundError(p)
 data=json.loads(p.read_text())
 certs.append({'path':name,'sha256':sha(p),'status':data.get('status'), 'checks':data.get('checks',data.get('checks_passed'))})
manifest={
 'id':'P3K.99','status':'Proved; standalone QA pending','scope':'Initial selected fan; (a,b;m)=(6,1;2), n=1; original finite character and F0; fixed scalar; positive s-loop near rho=+1/2',
 'physical_Jin_pair':[-27,-12],'physical_index':-4,'Theta7_class':24,
 'source_sha256':EXPECTED,'include':str(out.relative_to(ROOT)),'include_sha256':sha(out),
 'supporting_proofs':outputs,'certificates':certs,
 'root_audit':{'path':'records/root_audit_e6_order_three_outer_transfer.json','sha256':sha(ROOT/'records/root_audit_e6_order_three_outer_transfer.json')},
 'peer_audit':{'path':'records/blind_audit_e6_order_three_outer_transfer.json','sha256':sha(ROOT/'records/blind_audit_e6_order_three_outer_transfer.json')},
 'export_only_changes':['Omitted historical opening and E65 work-list; full originals retained.','Clarified signed weight order (c0,c1,Z).','Typeset headings and exact paths.'],
 'existing_manuscript_dependencies':['P3K.57 IE.4--7','P3K.68 PL.1--6','P3K.95 EC.25a--b','P3K.96--98'],
 'master_modified':False,'statement_csv_modified':False,'mapping_modified':False,'qa':'pending'}
(ROOT/'records/k99_export_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps({'include':manifest['include'],'sha256':manifest['include_sha256'],'companions':len(outputs),'source_sha256':EXPECTED,'certificates':len(certs)},indent=2))
