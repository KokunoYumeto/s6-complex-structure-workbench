from pathlib import Path
import datetime, json, shutil, re
root=Path(__file__).resolve().parents[2]
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
archive=root/'records/k42_pre_antilinear_arrow'
extra=['notes/part3_source_cusp_trace.tex','code/part3/export_source_cusp_trace.py','code/part3/source_cusp_trace.py','code/part3/source_cusp_trace.json','code/part3/source_cusp_trace.out']
for rel in extra:
 p=root/rel;d=archive/rel;d.parent.mkdir(parents=True,exist_ok=True)
 if p.exists() and not d.exists():shutil.copy2(p,d)

p=root/'notes/part3_source_cusp_characteristic_pair_working.md'
s=(archive/'notes/part3_source_cusp_characteristic_pair_working.md').read_text()
s=s.replace('The resulting characteristic numbers in Jin\'s convention are',
'''Corrected by the fully audited physical-line and cap morphisms of
P3K.68. Write U for the outward-meridian-one Thom line and M for the
actual nonzero-vector physical line. They are dual. The physical
characteristic numbers in Jin's convention are''')
s=s.replace('(k,\\ell)=(6,0).', '(k_M,\\ell_M)=(-6,0),\\qquad(k_U,\\ell_U)=(6,0).',1)
s=s.replace('\\((m,n)=(0,-6)\\), with central coordinate one. The first fixed-edge\nflop remains the value \\(-5=23\\) already proved in P3K.40.',
'''\\((m,n,s)=(0,-6,-1)\\). The former source-class assertion used the
Thom index as the physical index; its exact correction is retained below.
No value for a different fan is assigned here.''')
s=s.replace('Let \\(x\\) be the meridian class with integral one on this sphere.',
'''Let \\(x=x_U\\) be the meridian class with integral one on this sphere.
It is the Thom-line convention; the physical nonzero-vector line is its
dual, as proved explicitly in SP.2 and SP.5 below.''')
a=s.index('The actual Cox quaternion is')
b=s.index('The inner projection-normal frame',a)
replacement=r'''The actual positive-weight spinor coefficients are
\((\overline{c_0},c_1)\), while the right-complex Cox coefficients are
\((c_0,\overline{c_1})\). Put \(Y=y/|y|\). The full coefficient map
from (SP.8) is therefore
\[
 (\overline{c_0},c_1)=\operatorname{diag}(\overline Y,Y)(a,b),
 \qquad (c_0,\overline{c_1})
      =\operatorname{diag}(Y,\overline Y)(\overline a,\overline b).
\]
Multiplication by the normalized quaternion \(1+jZ\) gives the actual
anti-linear arrow
\[
 (a,b)\longmapsto g(x,y)\overline{(a,b)},\qquad
 g(x,y)=\frac1{\sqrt{|x|^2+|y|^2}}
 \begin{pmatrix}y&-\overline x\\x&\overline y\end{pmatrix}.
                                                        \tag{SP.9}
\]
It intertwines the positive scalar action on the spinor with the
physical negative right scalar on the Cox quaternion. The previous
linear summand swap omitted this conjugation.

For \(J=\left(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\right)\)
and every SU(2) transition, \(\overline g=JgJ^{-1}\). Thus the
global anti-linear map \(Q=J^{-1}C\),
\[
 Q(a,b)=(\overline b,-\overline a),\qquad
 Q(e^{i\theta}v)=e^{-i\theta}Q(v),                       \tag{SP.10}
\]
commutes with all clutches. It has real four-dimensional determinant
one, while its adjoint is the antipodal map of the real normal
three-plane, of determinant minus one. It extends over both cap
normal discs by minus the identity. The Hermitian dual associated-line
map is retained on both cap collars; every extending scalar gauge is
inverted pointwise. The conjugated complex clutch has the same second
Chern number, since conjugation by J is an actual constant bundle map.

The physical meridian sign follows in the literal F9 chart
\((x,v,z)\), with \(y=vz\), weights \((0,-1,+1)\), and
\(b=(|z|^2-|v|^2)/2\). Its positive spinor is
\((\overline v,z)\). At \(v=1,z=0\), the projective coordinate
\(z/\overline v\) has the complex orientation of \(y\), while
the outward raw normal sphere at \(b<0\) has its negative. The
physical circle-first normal orientation is the negative raw
orientation. Thus the physical spinor projective sphere has that
physical normal orientation. Its physical nonzero-vector line is
tautological, with Chern number minus one. The meridian-one Thom
line U is its Hermitian dual; on the source page it is M inverse.
This is a coefficient and circle map, not merely a degree comparison.

'''
s=s[:a]+replacement+s[b:]
s=s.replace('The bundle \\(E\\) extends across the inner ball and is a trivial',
'''Use the conjugate spinor on the inner ball, with its conjugate Cartier
frame, and the actual right-complex Cox frame on the outer cap.
The coefficient map between these is exactly the complex-linear matrix
g in (SP.9), after retaining the global anti-linear map (SP.10).
Its Chern number equals that of E by the explicit J conjugacy.
The resulting bundle extends across the inner ball and is a trivial''')
s=s.replace('On the inner boundary its coordinate matrix is (SP.9).',
'''On the inner boundary its complex-linear coordinate matrix after
that conjugation is exactly g in (SP.9).''')
a=s.index('## SP.5.')
b=s.index('## Audit and computation status',a)
s=s[:a]+r'''## SP.5. Both line conventions and the actual physical return

The base orientation is the complex orientation on W. In the actual
F9 normal coordinates the ambient orbit orientation is
\(-\Omega_{\rm source}\wedge d\gamma\), and the physical normal
orientation is \(-d\gamma\wedge\Omega_L\). The anti-linear map
(SP.10) supplies the actual normal reflection between the coefficient
frames. Its extensions over the inner D4 and outer D3 times S1 caps
carry the dual circle character and every retained boundary gauge.
In particular the meridian-one line U extends through both product
surgery collars with exactly the line used in (SP.5) and (SP.20).

The outward boundary of the seven-dimensional quotient bordism is
\(-P_f\sqcup-N_e\sqcup-B\): the first sign is the five-dimensional
orbit followed by the outward parameter radial coordinate, and each
inner sign is the outward boundary of a removed normal disc. Thus
Stokes for U gives
\[
 (k_U,\ell_U)(P_f)=-(5,-4)-(1,4).
\]
The physical family is Jin's mapping torus for the inverse return;
reversing that parameter gives
\[
                (k_U,\ell_U)_{\rm Jin}=(6,0).
                                                        \tag{SP.21}
\]
The raw local complex-plus-height six-dimensional orientation and the
physical orbit orientation are opposite. The outward-meridian-one
Thom line changes sign with that normal orientation; hence the raw
Seifert values (SP.6) enter the U calculation with the signs displayed.
The physical nonzero-vector line M instead satisfies M=U inverse,
so in the same oriented Jin manifold
\[
           (k_M,\ell_M)=-(k_U,\ell_U)=(-6,0),
           \qquad A_M=-1.                              \tag{SP.22}
\]

For completeness the Hopf transfer uses this physical line. The
actual complex exterior is D3_y times S3_q, and the sphere is
minus the boundary of D3_y times D4_q. Physical M is positive on
the oppositely oriented Hopf base; reverse the y factor at the same
time, so the quotient orientation is unchanged. The F22 positive
Hopf factor is then u=+q and y'=-y. If L=D4_y times S3_q and
R=S3_y times D4_q, its first and second pieces are -R and -L.
The first-to-second clutch r maps to F(r); rewriting with L first
sets x=F(r), so the second point is F inverse of x. Consequently
lambda_M(F) is minus Sigma_(F inverse). The removed ball is
D4_u times D3_y', whose boundary is the original complex sphere;
the F8 cut-and-reglue maps coincide on its actual free face and are
the identity on its fixed-tube face. This proves that lambda_M is
the physical clutched sphere. For U the pieces are +R,+L and the
same clutch gives lambda_U(F)=Sigma_(F inverse), its orientation
reverse. All circle gauges are carried by the Hermitian dual map.
These exact arrows are written in mathematical notation in P3K.68.

Therefore the physical source class is -1 modulo 28. The exact
relative-coordinate identities in the physical convention are
\(m=k_M-6A_M\), \(n=6A_M\), giving
\[
                    (m,n,s)=(0,-6,-1).                  \tag{SP.23}
\]
The native central generator still has sign plus one: exchanging
the two Hopf pieces inverts the clutch, and the outer orientation
reversal cancels that inverse on a disc-supported central class.
No value on another fan is assigned here.

''' + s[b:]
s+='\n\nPhysical-line correction, '+now+': original SP.9/10 proof and certificate preserved at records/k42_pre_antilinear_arrow/. The complete cap and inverse-clutch correction is P3K.68.\n'
p.write_text(s)

p=root/'code/part3/export_source_cusp_characteristic_pair.py'
t=p.read_text()
t=t.replace('and positive-meridian conventions its characteristic pair and','and physical nonzero-vector-line conventions its characteristic pair and')
t=t.replace('(k,\\ell)=(6,0),','(k_M,\\ell_M)=(-6,0),\\qquad(k_U,\\ell_U)=(6,0),')
t=t.replace('(m_{\\rm rel},n_{\\rm rel},s)=(0,-6,1).','(m_{\\rm rel},n_{\\rm rel},s)=(0,-6,-1).')
t=t.replace('Their oriented sum gives the displayed return pair.','Their oriented sum gives the meridian-one U pair; the actual physical line M is its Hermitian dual and gives the displayed negative pair.')
t=t.replace('This statement concerns the specified initial fan; P3K.40 gives\nthe first fixed-edge flop class \\(-5=23\\) separately.','This statement concerns only the specified initial fan. The complete physical line and Hopf-transfer correction is P3K.68.')
p.write_text(t)

p=root/'notes/part3_source_cusp_trace_working.md'
t=(archive/'notes/part3_source_cusp_trace_working.md').read_text()
t=t.replace('Its Hopf sphere bundle carries the meridian line with determinant\nclass \\(b=0\\).',
'''Its Hopf sphere bundle carries the meridian-one Thom line U with
determinant class b=0. The physical nonzero-vector line M is its dual:
in the literal normal chart (v,z), the positive spinor is (bar v,z),
whose physical circle is the unit circle of the tautological line.
The actual outward normal meridian has its projective complex orientation,
so that physical line has degree -1. The Hermitian dual map supplies
the degree-one Thom line and inverts its circle character. P3K.68
gives this complete coordinate and orientation computation.''')
t=t.replace('This is the actual outer circle line.', 'This identifies the actual outer physical circle line and its meridian-one dual; their characters are retained separately.')
t=t.replace('On the outer complement the actual\nEuler line has this value,','On the outer complement the actual\nmeridian-one dual U has this value,')
t=t.replace('It retains the physical circle action.','It retains the stated dual circle character.',1)
t=t.replace('The actual Euler line extends over both collars.', 'The meridian-one dual U extends over both collars; the physical M extends by the inverse character.')
t=t.replace('A_{\\rm Jin}(f)=A(N_e).', 'A_{U,\\rm Jin}(f)=A_U(N_e).')
t=t.replace('A(N_e)=\\frac{e(\\nu V)^2-\\sigma(V)}8', 'A_U(N_e)=\\frac{e(\\nu V)^2-\\sigma(V)}8')
a=t.index('There is no unrecorded mirror sign in this comparison.')
b=t.index('The second equality is the oriented Hopf transfer',a)
t=t[:a]+r'''The displayed local Seifert computation uses the meridian-one U
line. Its raw complex-plus-height orientation and the physical orbit
orientation are opposite; the outward-meridian-one line reverses at
the same time, so its U index is the displayed H(e)=1. The actual
nonzero-vector physical line M is U inverse. Therefore its odd
characteristic index in the same oriented Jin manifold is the negative.
The exact spinor arrow is anti-linear, not the previously written
linear swap: Cartier coefficients (a,b) map to g(x,y) overline(a,b)
in the right-complex Cox spinor. The globally defined quaternionic
anti-linear map commutes with all SU2 clutches and extends over both
cap products; its normal antipodal map and the dual circle character
are retained. P3K.68 gives every unit and both cap extensions.

The physical Hopf transfer has positive-line base -S2_z and y'=-y,
so its first and second pieces are -R,-L in the K23 plumbing order.
Its first-to-second clutch r maps to F(r); rewriting with L first
gives minus Sigma_(F inverse). The removed ball has the original
complex six-sphere as its outward boundary, and its free-face map is
the actual physical return, with the identity on the fixed tube.
Thus this is the actual clutched sphere. The meridian-one U transfer
instead has pieces +R,+L and is its orientation reverse. There is
no extra inverse after this explicit piece exchange.

Consequently the direct local calculation H(e)=1 gives
\[
 A_{U,\rm Jin}(f)=1,\qquad A_{M,\rm Jin}(f)=-1,
 \qquad[\Phi]=-1\in\Theta_7\cong\mathbb Z/28.          \tag{SC.19}
\]
''' +t[b:]
t=t.replace('The second equality is the oriented Hopf transfer of P3F.22.', 'The last equality is the physical-line oriented Hopf transfer of P3F.22, with the exact dual and piece maps of P3K.68.')
t=t.replace('\\Sigma_1','\\Sigma_{-1}').replace('invariant \\(1/28\\)','invariant \\(-1/28\\)').replace('1=[\\Phi]=2[\\Phi_a]','-1=[\\Phi]=2[\\Phi_a]')
t+='\n\nPhysical-line correction, '+now+': original source/line proof preserved verbatim; P3K.68 replaces only the anti-linear coefficient and physical-transfer convention. The local link and all source/cap geometry remain.\n'
p.write_text(t)
p=root/'code/part3/export_source_cusp_trace.py'
t=p.read_text().replace('A_{\\rm Jin}(f)=1,\\qquad [\\Phi]=1','A_{M,\\rm Jin}(f)=-1,\\qquad [\\Phi]=-1')
t=t.replace('\\Sigma_1','\\Sigma_{-1}').replace('invariant \\(1/28\\)','invariant \\(-1/28\\)').replace('one cannot be twice','minus one cannot be twice')
t=t.replace('and Hopf transfer of P3F.22.', 'and physical-line Hopf transfer of P3F.22 as explicitly identified in P3K.68.')
p.write_text(t)
with (root/'records/literature_fourfold.md').open('a') as f:
 f.write(f'\n- {now} — Opened preserved K42/F56 source and current exporters to apply the root-authorized exact K68 physical-line correction. Material: full source/cap proofs retained; anti-linear spinor arrow, dual character, both cap conventions, and inverse-clutch map replaced explicitly. Originals preserved with hashes.\n')
print(json.dumps({'utc':now,'status':'Patched complete K42/F56 source and exporters','no_master_edit':True},indent=2))
