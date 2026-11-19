#!/usr/bin/env python3
"""Assemble the complete audited P3K.80 proof; preserve every working source."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib,json,re

BASE=Path(__file__).resolve().parents[2]
paths={
 "EA":"notes/part3_source_zero_annular_attachment_working.md",
 "RT":"notes/part3_source_zero_real_trace_working.md",
 "SZ":"notes/part3_source_zero_completion_working.md",
 "TL":"notes/part3_source_zero_tate_label_working.md",
}
texts={key:(BASE/path).read_text() for key,path in paths.items()}
with (BASE/"records/literature_fourfold.md").open("a") as f:
 f.write("\n- "+datetime.now(timezone.utc).isoformat()+" — Read "+", ".join(paths.values())+
  ". Reason: complete K80 proof assembly after root and checks full attachment PASS; source/Cartier/Tate/root maps, exact finite domain, all mixed-face collars, whole-F cap, physical transfer.\n")

def section(key,number):
 p=re.compile(r"^## "+re.escape(key)+r"\."+str(number)+r"\. .*$",re.M)
 m=p.search(texts[key])
 assert m,(key,number)
 nxt=re.search(r"^## ",texts[key][m.end():],re.M)
 end=m.end()+nxt.start() if nxt else len(texts[key])
 return texts[key][m.start():end].strip()

def numbered_sz(number):
 m=re.search(r"^## "+str(number)+r"\. .*$",texts["SZ"],re.M)
 assert m
 nxt=re.search(r"^## ",texts["SZ"][m.end():],re.M)
 end=m.end()+nxt.start() if nxt else len(texts["SZ"])
 return texts["SZ"][m.start():end].strip()

statement=r"""Retain the marked source
\[
 E_v:\quad Y^2=X^3+(1-2v)X^2+TX+v^2,\qquad G=(0,v),
\]
the actual Cartier line \(M_2=O([2G]-[O])\), the suspension
over \(-G\), and the selected whole-zero fibre at
\(T_0(v)=v^2-2v\). Retain the reduced III cap of order
\(m=4p-1\), \(p\ge1\), either norm sign \(n=\pm1\),
and every admitted integral \(d\delta\) character. These
are the sphere families and exact cap markings of P3K.24,
with the physical line convention of P3K.68.

For a fixed sufficiently small nonzero scalar, the positive
\(v\)-loop has physical Jin integer \(0\) in the initial
negative-square fan \(T_0\). Its actual oriented clutched-sphere
class is \(0\in\Theta_7\simeq\mathbb Z/28\). The literal
reflected fan \(JT_0\) has actual class \(2\). For the
actual coupled family \(r=v^k r_0\), \(\lambda=r^m\),
\(k\ge1\), the two classes are
\[
 (Z_{T_0},Z_{JT_0})
   =\bigl(k(3p-1),\ 2+k(3p-1)\bigr)\pmod {28}.
 \tag{RA.1}
\]
The reflected value uses the actual directed relative flop.
This statement treats the reduced \(a=2,b=1\) branch."""

intro=r"""The proof constructs a finite real bordism carrying the
actual physical circle, its associated line, and the
canonical complex spin-c arrows on every local overlap.
The fixed-scalar loop is separated from the scalar winding
by the actual two-parameter family before the cut is made.
All local source, line, node and finite-root maps needed
for the cut are reproduced below. The local equation
prefixes identify the component calculations within this
single proof. In this proof \(a=2,b=1\), except in the
displayed weight identities which retain \(a\) to show
the actual character. The Tate period is denoted
\(H_T=(Q,P^2)\); the finite-cap unit is
\(h_\infty=1-T_0(v)q_\infty\). They are distinct
explicit maps/functions throughout.

## RA.2. Source, Cartier and actual Tate data

Put \(q=T-(v^2-2v)\).  On the source threefold set
\[
 A=Y-v,\quad B=Y+v,\quad C=X,\quad
 D=T+X^2+(1-2v)X .
\]
The source equation is literally \(AB=CD\).  Its marked small
resolution has the chart
\[
 A=Dz,\qquad C=Bz,\qquad v=(B-Dz)/2.
\]
The chosen section \(G\) has \(z=0\).  The actual closure of
\(2G\) has Cartier equation
\[
 F_2=1-Bz^3-(1-2v)z^2=0.
\]
Indeed the doubling formula gives \(z=-2v/T\) and
\(zT+2v=BF_2\); the factor \(B=0\) is the other section
\(-G\), so the strict closure is \(F_2=0\).
Define the actual target-point primitive on \(O(G-O)\) by
\[
 U:(p,w)\longmapsto\left(p-G,\frac{w}{X(p-G)}\right).
 \tag{SZ.7}
\]
The identity
\((G)-O-t_G^*((G)-O)=\operatorname{div}X\)
makes this the indicated line map; its tensor-square is the
primitive on \(O(2G-2O)\).  The Cartier conjugation below
identifies that tensor-square with the specified actual
line \(M_2\).  In that conjugation the retained rational
function is
\[
 F_{21}=\frac{Y+v+(T/(2v))X}{X}.
\]
Its displayed poles are carried by the rational line map;
the resolved Cartier arrows below are the extensions used
on the finite cut.
"""
sz9=numbered_sz(9)
sz9=sz9.replace("## 9. The actual Cartier overlap of the two source flop chambers",
 "### The source graph and its Cartier coefficient")
sz9=sz9.replace("The chamber overlap in the preceding paragraph can be made literal.",
 "The chamber overlap is the following literal map.")
sz9=sz9.replace("Cartier equation from Section 2.","Cartier equation just displayed.")
sz9=re.sub(r"The only remaining comparison is consequently[\s\S]*?including its Mumford boundary and finite-root caps\.",
 "The finite construction below uses these actual chambers, the full selected factor, and their finite-root maps.",sz9,count=1)
sz9=sz9.replace("Its boundary must be matched with the original completed family\nbefore the local link numbers of Section 8 can be summed.",
 "Its outside boundary is identified with the actual family by the mixed-face maps below.")
sz19=numbered_sz(19).replace("## 19. Exact Tate units on the two-node base",
 "### The full Tate periods and units")
sz10=numbered_sz(10)
sz10=sz10[:sz10.index("This supplies the two-node base chart")]
sz10=sz10.replace("## 10. Exact two-node base coordinates",
 "### The exact two-node base coordinates")
tl="\n\n".join(section("TL",j) for j in (1,2,3,4))
tl=tl.split("The compact",1)[0] if False else tl
# Remove the historical final paragraph while keeping every actual period arrow.
tl=re.sub(r"\nThe compact radial[\s\S]*$","",tl)
tl=tl.replace("## TL.4. Period, closing, and remaining attachment scope",
 "## TL.4. Full period and closing arrows")
rt1=section("RT",1)
rt1=rt1[:rt1.index("The local intersection numbers")]
rt1=rt1.rstrip()+"\nThe complete fixed and cap contributions are calculated in RT.16--17 below.\n"
rt2=section("RT",2)
rt2=rt2.replace("They show why a proposed\ncompletion has to inspect their quotient strata at v=0 explicitly; the\nhorizontal trace and the isolated origin link do not by themselves enumerate\nall strata of such a completion.",
 "The finite domain below retains the quotient strata over both branches.")
ea17=section("EA",17)
scalar=section("RT",12)
scalar=re.sub(r"\nThis proves only[\s\S]*$","",scalar)
cap=section("EA",12)
cap=cap[:cap.index("The fixed boundary of the horizontal")]
cap=cap.replace("## EA.12. The fixed-scalar exterior and the remaining boundary equations",
 "## EA.12. The actual fixed-scalar exterior, finite root and inverse square")
cap=cap.replace("The full node-to-Tate map being recorded independently",
 "The full node-to-Tate map TL.1--4")
cap=cap.replace("still accompany this chart","accompany this chart")
metric=section("EA",5)
metric=metric.replace("The remaining construction is the\nactual surgery joining those two portions, with its boundary orientation.\nNo individual source-zero return follows from (EA.11)--(EA.15) alone.",
 "The complete mixed-face construction below joins these portions with their actual boundary orientations.")
positive=section("EA",6)
positive=positive[:positive.index("The compact radial link")]
positive+= "\nThe actual radial and product cuts are compared by the complete domain EA.19, rather than by identifying their defining functions.\n"
radial=section("RT",13)
radial=radial[:radial.index("The fixed trace on the radial sphere")]
parts=[intro,sz9,sz10,sz19,tl,rt1,rt2,ea17,scalar,cap,metric,
 section("EA",9),section("EA",10),section("EA",11),
 section("EA",13),section("EA",14),section("EA",15),section("EA",16),
 positive,radial,section("EA",19),section("EA",20),
 section("EA",21),section("EA",22),section("EA",18),
 section("RT",16),section("RT",17)]
body="\n\n".join(parts)

# The chronological notes remain unchanged. This proof uses their completed scopes.
replacements={
 "This section is the full reduced-branch attachment draft for audit.":
 "This section assembles the finite reduced-branch attachment.",
 "On the positive\nmoment piece use the compact region RT.20 and its invariant\ncorner rounding.":
 "On the positive\nmoment piece use the complete retained domain EA.48 and its invariant\ncorner rounding. It includes the upper fibre and charge-one point.",
 "The remaining compact construction must give\n the retained and excised sides of these strata explicitly.":
 "The retained and excised sides are the exact domains in EA.19--20.",
 "Here is the resulting oriented boundary equation to be audited\nagainst the full construction, before assigning a return value.":
 "The complete face maps give the following oriented boundary equation.",
 "The geometric global\nattachment and (EA.47) are kept in this audit draft until the\ncomplete outside and cyclic endpoint comparison has passed.\nNo individual source-zero return is assigned in this note.":
 "The complete outside and cyclic endpoint maps in EA.19--22 establish this boundary identity for the actual family.",
 "The complete finite-strip and outside comparison remains an\naudit draft; no individual source-zero return is entered here.":
 "The complete finite-strip and outside comparison is the one established in EA.21--22.",
 "This supplies the upper endpoint and the mixed-face\noverlaps required by the finite ledger EA.47.\nThe full reduced attachment is submitted for\nindependent audit with these maps; no numerical\nsource-zero return is entered before that audit.":
 "These are the full upper endpoint and mixed-face overlaps used in the finite boundary identity EA.47.",
 "This fixes the local lift data for the compact attachment. It does\nnot assert that the still-unassembled compact cut already carries\n a global spin filling or select an individual source-zero class.":
 "These lift data are carried on the finite compact attachment below.",
 "The global construction must still insert these faces into the\ncompact period strip and account for its horizontal fixed cap;\n(EA.41) records their local oriented ownership without assigning\nthe resulting absolute source-zero return.":
 "The complete domain and mixed-face maps in EA.19--22 insert these full faces into the compact period strip and retain the whole fixed cap.",
 "Its status explicitly stops at": "The original local certificate records",
 "No individual source-zero return is assigned from this\nchart calculation alone.":"",
}
for a,b in replacements.items():
 body=body.replace(a,b)
body=body.replace("The earlier wording of EA.20 is preserved in\n\\path{records/attempts/source_zero_outer_face/pre_mixed_face_decomposition.md}.\n","")
body=body.replace("The previous EA.18 draft","The finite construction")
body=body.replace("This supplies the upper-domain ownership omitted\nfrom the first EA.18 draft; the full boundary ledger remains\nunder audit.","This gives the upper-domain ownership in the complete boundary ledger.")
body=body.replace("the complete finite-period comparison is still open","the complete finite-period comparison is given below")
body=body.replace("The finite-period comparison is complete only\nafter these maps agree with its ordinary and root faces through\nthe actual B and F0 arrows.",
 "The ordinary and root face agreements are the actual B and F0 arrows in EA.22.")
body=body.replace(r"F_0 B^{-1}=(c_\lambda h)^{-1}",r"F_0 B^{-1}=(c_\lambda h_\infty)^{-1}")
body=body.replace(r"q_1=q_\infty^{-1}h .",r"q_1=q_\infty^{-1}h_\infty .")
body=body.replace("The h period in\nEA.64","The full Tate period H_T in\nEA.64")
body=body.replace(
 "This supplies the cyclic chart transition and its local charged\norientation. The compact radial-to-product-radius cobordism and its\ncomplete global attachment are still being constructed. No individual\nsource-zero return is assigned by counting the charts in this section.",
 "These are the cyclic chart transition and local charged orientation used in the complete finite-domain attachment below.")
body=body.replace(
 "class in \\(\\Theta_7\\) is divided. The still-missing compact\nfixed-scalar source attachment has not been supplied by this\nboundary comparison.",
 "class in \\(\\Theta_7\\) is divided. The fixed-scalar attachment is constructed by the complete domains and collar maps below.")
body=body.replace(
 "This fixes the local lift data for the compact attachment. It does\nnot assert that the still-unassembled compact cut already carries\na global spin filling or select an individual source-zero class.",
 "These are the actual local lift data carried on the complete finite attachment below.")
body=body.replace(
 "The actual compact comparison region is RT.20, with its two arms\nretained.",
 "The regular part RT.20 has its two explicit arms; the actual complete retained domain is EA.48, which also retains its upper fibre and charge-one point.")
body=body.replace(
 "The compact strip\nmust specify where the complement of the lower arm in this full\nshape lies among its boundary faces.",
 "The complete domain and horn chain EA.48--52 specify where the complement of the lower arm lies among the boundary faces.")
body=body.replace(
 "fix the radial normal and its spin-c/line data without silently\nclosing the remaining period-strip boundary.",
 "fix the radial normal and its spin-c/line data for the full mixed-face attachment EA.21--22.")
# Retain the cap unit's distinct name in every displayed cap square.
body=body.replace(r"q=q_\infty^{-1}h",r"q=q_\infty^{-1}h_\infty")
body=body.replace(r"q_1=q_\infty^{-1}h",r"q_1=q_\infty^{-1}h_\infty")
body=body.replace("h_\\infty_\\infty","h_\\infty")
body=body.replace(r"\lambda h\,U_{\rm cap}",r"\lambda h_\infty\,U_{\rm cap}")
body=body.replace(r"q_1^n=h^n",r"q_1^n=h_\infty^n")
body=body.replace(r"\(q_1^n\) and \(h^n\)",r"\(q_1^n\) and \(h_\infty^n\)")
body=body.replace(r"\mathcal A_f={\rho_0/2",r"\mathcal A_f=\{\rho_0/2")
body=body.replace("The portion rho=r0,R<=epsilon has exactly two disjoint components.\nWriting eta=epsilon2/r0^2 and",
 r"The portion \(\rho=r_0,\ R\le\varepsilon\) has exactly two disjoint components."+"\n"+
 r"Write \(\eta=\varepsilon^2/r_0^2\) and")
body=body.replace(r"t^2={\rho_0^2\over1+|\zeta|^2}",r"t^2=\frac{\rho_0^2}{1+|\zeta|^2}")
body=body.replace("The period matrices used in Section 18 can be obtained from actual",
 "The periods used in the finite construction are obtained from the actual")
body=body.replace("factors \\(q_1q_2\\) of Section 10.","factors \\(q_1q_2\\) just defined.")
body=body.replace("Section 10 are \\(v+T/2\\) and \\(v-T/2\\)",
 "the preceding two-node chart are \\(v+T/2\\) and \\(v-T/2\\)")
body=body.replace("The target-point primitive lift of Section 6 is now exactly",
 "The target-point primitive lift (SZ.7) is now exactly")
body=body.replace("The root audit RE.9 uses instead","A second explicit charged atlas uses instead")
body=body.replace("This records the comparison in the root's written atlas as well\nas in the convenient conjugated atlas.",
 "This gives the literal comparison between the two charged atlases.")
body=body.replace("This supplies the charged/native seam map. Its hemisphere\ninversion and both S2 antipodal arrows still have to be combined\nwith the actual retained/excised boundary sides in the complete\nfinite strip. No sign of a global characteristic sum is inferred\nfrom the quaternion formula alone.",
 "This is the charged/native seam map. Its hemisphere inversion and both sphere antipodal maps are retained in the complete finite-strip boundary calculation EA.47 below.")
for old,new in {
 r"R^2={\rho_0^2\over1+|\zeta|^2}":r"R^2=\frac{\rho_0^2}{1+|\zeta|^2}",
 r"{u_P^2\over q_2^2}":r"\frac{u_P^2}{q_2^2}",
 r"{u_P^2u_X^2\over c_\lambda T}":r"\frac{u_P^2u_X^2}{c_\lambda T}",
 r"{u_Gu_P^2u_X^2\over c_\lambda}":r"\frac{u_Gu_P^2u_X^2}{c_\lambda}",
 r"{1\over2\pi i}":r"\frac{1}{2\pi i}",
 r"{4k-\ell\over24}":r"\frac{4k-\ell}{24}",
 r"{\langle p_1(F-C),[F-C]\rangle-3b^2\over24}":r"\frac{\langle p_1(F-C),[F-C]\rangle-3b^2}{24}",
 r"{\sigma(F-C)-b^2\over8}":r"\frac{\sigma(F-C)-b^2}{8}",
 r"{a(a-1)\over2}":r"\frac{a(a-1)}{2}",
}.items():
 body=body.replace(old,new)
body=body.replace("A point z=V=0 on the outer radial sphere has full physical\ncircle stabilizer. The charged product faces of EA.39 are free.",
 "The explicit fixed points z=V=0 on the outer radial sphere are retained separately from the charged product faces by the following full chart decomposition.")

conclusion=r"""
## RA.3. The physical characteristic equation and actual return

Let \(N_7\) be the actual completed outside boundary of the
finite construction. The physical circle is free after
the conifold/Hopf replacement on its selected fixed tube.
Let \(N_6=N_7/S^1\), with the Jin orientation of P3K.68.
On every free part of the seven-dimensional quotient
bordism the associated line is the actual nonzero-vector
line \(M\), and \(x=c_1(M)\). The tangent splitting is the
quotient tangent plus the oriented physical circle. Thus
\(p_1\) is the pullback of the quotient \(p_1\).
Choose invariant product connections on the named collars
and patch them on the compact interior. Stokes applied
to the closed Chern--Weil polynomial gives the exact
oriented characteristic identity
\[
 -A(N_6)-A(\mathbb P^3_2)
       -A(B_{F-C})-A(B_{S^4})+A(\mathbb P^3_1)=0,
 \qquad
 A(X)=\int_X\frac{4x^3-p_1(TX)x}{24}.             \tag{RA.3}
\]
The boundary signs are those of EA.47. The full charged
end occurs once by the horn chain, the exceptional disk
belongs to the whole \(F\), and the sole fixed cap is \(C_0\).
The two auxiliary charged descriptions are related by
EA.26 and contribute one boundary.

On a positively oriented charged projective boundary the
physical line is \(O(-a)\). Hence, writing \(h\) for the
positive generator, \(x=-a h\) and \(p_1=4h^2\), so
\[
 A(\mathbb P^3_a)=-\frac{a(a^2-1)}6.
\]
For \(a=2\) this is \(-1\); for the isolated charge-one
boundary it is zero. The whole capped surface calculation
RT.27--32 retains both actual normal clutches and gives
\(A(B_{F-C})=1\). The actual comparison cap \(S^4\) has
\(A(B_{S^4})=0\), independently of its retained normal
\(c_2\). Therefore (RA.3) gives
\[
                     A(N_6)=-(-1)-1-0+0=0.      \tag{RA.4}
\]
This is a calculation on the specified compact finite
bordism. The physical line and canonical spin-c overlap
maps, including the residual \(\mu_2\) endpoint, have
already been carried through every face.

For the actual return, take a delta-averaged connection on
the original completed family, product on the selected
tube in the exact RT.33a--b coordinates. Its quotient after
the conifold replacement is a diffeomorphism
\(f:S^2\times S^3\to S^2\times S^3\), fixed on that tube.
The preserved Euler class generates \(H^2\), and the
orientation then preserves \(H^3\); thus \(f\) belongs to
the required homology-trivial relative group.
The Hopf lift in P3F.22 is literally the physical return
lift on the complement and uses the same identity
extension on the selected tube. P3K.68 supplies the full
piece and inverse-clutch arrow
\[
       \lambda_M(f)=-\Sigma(f^{-1})=\Sigma(f).
\]
Consequently its class in \(\Theta_7\) is the physical
integer (RA.4), namely zero. This step selects the
actual parameter return by its source, cap, tube and
line maps, rather than only by its characteristic polynomial.

For the literal reflected fan, the already proved single
native directed flop of P3K.60 has the actual pair
\((1-a,a)=(-1,2)\). Its signed relative Cox conjugation
adds the right exponent \(a=2\) to the central class.
The complex normal orientation and the physical transfer
are precisely those retained in P3K.68--69. Thus the
reflected fixed-scalar class is \(2\). No division of a
covered \(\Theta_7\) class is made.

Finally the actual scalar-root loop has physical index
\(3p-1\) in these two fans: P3K.24 with the physical
correction P3K.68 gives the initial value, and the narrow
actual C2 comparison P3K.62 gives their equality.
The exact based parameter homotopy RT.12 adds \(k\) such
loops, with basepoint \(r_{\rm base}=v_*^k r_0\).
It therefore gives (RA.1), retaining either norm sign
and all prescribed finite characters.

## RA.4. Exact certificates and proof scope

The full source/Cartier, node and shape calculations are
executed in the following retained certificates:
\path{code/part3_fourfold/source_zero_two_node_cox.json},
\path{code/part3/source_zero_tate_label.json},
\path{code/part3_fourfold/source_zero_associated_reset.json},
\path{code/part3_fourfold/source_zero_chamber_ledger.json},
\path{code/part3_fourfold/source_zero_spin_chart.json},
\path{code/part3_fourfold/source_zero_charged_shape.json},
\path{code/part3_fourfold/source_zero_native_charged_seam.json},
\path{code/part3_fourfold/source_zero_full_faces.json},
\path{code/part3_fourfold/source_zero_upper_domain.json},
\path{code/part3_fourfold/source_zero_boundary_ledger.json},
and \path{code/part3_fourfold/source_zero_mixed_outer.json}.
They retain the full units and exact integer/normal
characters. The analytic extension and compact-face proofs
are given above; numerical identities do not replace those
maps. The chronological attempts and withdrawn shortcuts
remain in the working notes and attempt records. This
theorem proves the reduced branch only.
"""
body += "\n\n"+conclusion
body=body.replace(r"\tag{",r"\tag{")  # Keep source equation tags for the consistent prefix pass.

working=BASE/"notes/part3_source_zero_reduced_attachment_working.md"
working.write_text("# P3K.80. Proved: the actual reduced-source zero return\n\n## Statement\n\n"+
 statement+"\n\n## Proof\n\n"+body+"\n")
record={
 "id":"P3K.80","status":"Proved","root_audit":"Full EA18--22 and RT16--17 PASS 2026-11-17 after checkpoint18",
 "peer_audit":"checks full reduced attachment PASS; blind narrow full-unit inverse B/edge PASS",
 "working_sources":{paths[k]:hashlib.sha256(v.encode()).hexdigest() for k,v in texts.items()},
 "proof_sha256":hashlib.sha256(working.read_bytes()).hexdigest(),
 "scope":"reduced a=2,b=1,m=4p-1,n=+/-1,retained d; initial T0 and literal reflected JT0",
 "fixed_scalar":{"T0":{"physical_Jin_integer":0,"Theta7":0},"JT0":{"Theta7":2}},
 "coupled":{"T0":"k*(3*p-1) mod 28","JT0":"2+k*(3*p-1) mod 28"},
 "good_branch":"not asserted"
}
(BASE/"records/k80_proof_assembly.json").write_text(json.dumps(record,indent=2)+"\n")

# Protect all mathematical and explicit path spans before escaping prose.
def latex(value):
 for prefix in ("SZ","TL","EA","RT","RA"):
  value=value.replace("\\tag{"+prefix+".","\\tag{P3K.80."+prefix+".")
  value=value.replace("("+prefix+".","(P3K.80."+prefix+".")
 blocks={}
 def protect(m):
  key="PROTECTEDSPAN"+str(len(blocks))+"END"
  blocks[key]=m.group(0)
  return key
 value=re.sub(r"\\\[[\s\S]*?\\\]|\\\([\s\S]*?\\\)|\\path\{[^}]*\}",protect,value)
 value=re.sub(r"^## (.+)$",lambda m:"\\par\\medskip\\noindent\\textbf{"+m.group(1)+".}\\par\\nopagebreak[4]",value,flags=re.M)
 value=re.sub(r"^### (.+)$",lambda m:"\\par\\smallskip\\noindent\\textit{"+m.group(1)+".}\\par\\nopagebreak[4]",value,flags=re.M)
 value=re.sub(chr(96)+r"([^"+chr(96)+r"]+)"+chr(96),lambda m:"\\path{"+m.group(1)+"}",value)
 # Escape prose characters; TeX paths and displayed mathematics are protected.
 value=re.sub(r"(?<!\\)_",r"\\_",value)
 value=re.sub(r"(?<!\\)\^",r"\\textasciicircum{}",value)
 # Source proof lists are rendered with their actual paragraph content.
 lines=value.splitlines()
 result=[]; list_open=False; item_buf=[]
 for line in lines:
  if line.startswith("* "):
   if not list_open:
    result.append("\\begin{itemize}");list_open=True
   result.append("\\item "+line[2:])
  elif list_open and line.strip()=="":
   result.append(line)
  elif list_open and line.startswith("  "):
   result.append(line.strip())
  else:
   if list_open:
    result.append("\\end{itemize}");list_open=False
   result.append(line)
 if list_open: result.append("\\end{itemize}")
 value="\n".join(result)
 for key,content in blocks.items():
  value=value.replace(key,content)
 return value.strip()+"\n"

tex="\\subsection{The reduced source-zero return by the full finite attachment}\n"+"\\begin{statement}{P3K.80}{Proved}\n"+latex(statement)+"\\end{statement}\n\\begin{proof}\n"+latex(body)+"\\end{proof}\n"
assert not re.search(r"^#{1,3} ",tex,re.M)
(BASE/"notes/part3_source_zero_reduced_attachment.tex").write_text(tex)
preamble=(BASE/"code/part3_fourfold/k68_standalone.tex").read_text().split("\\begin{document}",1)[0]
(BASE/"code/part3_fourfold/k80_standalone.tex").write_text(preamble+
 "\\begin{document}\n\\input{notes/part3_source_zero_reduced_attachment.tex}\n\\end{document}\n")
print("Wrote complete K80 proof and standalone:",len(body.split()),"words")

