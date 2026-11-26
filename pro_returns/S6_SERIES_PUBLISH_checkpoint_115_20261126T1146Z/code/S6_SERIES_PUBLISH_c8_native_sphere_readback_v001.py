"""Apply bounded native-sphere refinements and the full moved comparison."""
import csv
import hashlib
from pathlib import Path
import S6_SERIES_PUBLISH_c8_integrate_units as units
import S6_SERIES_PUBLISH_c8_integrate_presentation as presentation
root=Path(__file__).resolve().parent.parent
lane=root/'agents/continuation8_iii_weighted_units'
path=root/'agents/continuation8_iii_integration/units/root/full_sphere_nullity.tex'
old_all=path.read_text();text=old_all
assert hashlib.sha256(path.read_bytes()).hexdigest()=='54ec0404b8e9ad92060d01beff9aa89466720f28baaafbf3e715aac3bdb2d517'
table=lane/'S6_SERIES_PUBLISH_NATIVE_SPHERE_publication_defects.tsv'
with table.open(newline='') as f:
    r=csv.DictReader(f,delimiter='\t');fields=r.fieldnames;rows=list(r)
assert len(rows)==50
number=15
def edit(old,new,kinds,why,owner='wb:cusp-s12-one-copy-invariant'):
    global text,number
    assert text.count(old)==1,(old[:100],text.count(old))
    line=text.count('\n',0,text.index(old))+1
    text=text.replace(old,new,1);number+=1
    for kind in kinds:
        rows.append(dict(zip(fields,[f'III-C8-NATIVE-SPHERE-PUB-{number:03}-{kind}',kind,owner,f'full_sphere_nullity.tex sequential line {line}','pending page concordance','root/full_sphere_nullity.tex','pending final build',old,new,why,'whole533-line candidate read; bounded follow-up readback pending; global gates open'])))

edit(r'''Use the exact cube representative $g_C=\phi gd$ of
Definition~\ref{wb:def:native-sphere-carriers}. In the following
suspension formulas, $g$ denotes $g_C$; their inverse geometric
transport is $g=\phi^{-1}g_Cd^{-1}$ as specified there.
''',r'''Use the exact cube representative $g_C=\phi gd$ of
Definition~\ref{wb:def:native-sphere-carriers}, with inverse
geometric transport $g=\phi^{-1}g_Cd^{-1}$.
''',['D20','D23'], 'Keep the geometric map g and its cube representative g_C explicit instead of reusing g inside the point-set suspension formulas.')
edit(r'[E^6g]=2a\nu_9',r'[E^6g_C]=2a\nu_9',['D20'],
     'Equation038Z is the same exact class in the declared cube coordinates; its permanent label and target remain.')
edit(r''' E_L=\mu_{6,3}(\mathrm{id}_{C_6}\wedge g)\mu_{6,6}^{-1},
 \qquad
 E_R=\mu_{3,6}(g\wedge\mathrm{id}_{C_6})\mu_{6,6}^{-1}.
''',r''' E_L=\mu_{6,3}(\mathrm{id}_{C_6}\wedge g_C)\mu_{6,6}^{-1},
 \qquad
 E_R=\mu_{3,6}(g_C\wedge\mathrm{id}_{C_6})\mu_{6,6}^{-1}.
''',['D20'], 'Use the actual typed map C6 to C3 in both ordered suspension representatives, with unchanged twists and signs.')
edit('Their class is $E^6g$, and','Their class is $E^6[g_C]$, and',['D20'],
     'Name the exact transported homotopy class of the framed product.')
start=text.index('We specify the target coordinate change used in the construction.')
end=text.index('Choose a framed tubular embedding',start)
block=text[start:end]
renamed=block.replace('h_i','b_i').replace('h_1','b_1').replace('h_2','b_2').replace('h_3','b_3')
edit(block,renamed,['D20','D23'],
     'Rename only the three scalar interval-to-line maps b_i, with the identity notation transport b_i=h_i and inverse h_i=b_i. This keeps the sphere homeomorphisms h_d from Q253 unshadowed; every scalar formula, derivative, inverse root and target derivative remains identical.')
edit(r'''groups are zero.  Both $H_0$ maps are the identity.
''',r'''groups are zero. Both $H_0$ maps are the identity.
Since $F_i=b f_i d^{-1}$, functoriality gives
$(F_i)_*=b_*(f_i)_*(d_*)^{-1}$ in every degree, proving the
same statements for the two smooth maps on $X$.
''',['D20','D22'], 'Give the actual homology transport through the same two homeomorphisms for the newly formalized F_i statement.')
edit(r'''Thus $Q:C_{12}\to\mathcal A\wedge\mathcal A$ and
$P:\mathcal A\wedge\mathcal A\to C_6$, with literal equality
$PQ=\widehat q_3^{\wedge2}$ under these identifications: both send
$[x_1,x_2]$ to $[pq_2(x_1),pq_2(x_2)]$ and send the fat wedge to the
basepoint.  Postcomposition therefore gives the homomorphism
''',r'''For $u_1,u_2\in C_6$, the composite sends
\[
 \mu_{6,6}[u_1,u_2]\longmapsto
 \mu_{3,3}[\phi p q_2d(u_1),\phi p q_2d(u_2)]
 =\mu_{3,3}[g_C(u_1),g_C(u_2)].
\]
Each side sends the fat wedge to the basepoint, proving the literal
identity $PQ=\mu_{3,3}(g_C\wedge g_C)\mu_{6,6}^{-1}$.
Postcomposition therefore gives the homomorphism
''',['D20','D22'], 'Spell out both source and target cube coordinate transports in the actual P Q identity, including its basepoint locus.',
     'wb:cusp-s12-nullity-scope')
edit(r'''To construct the four-sphere homotopy retract, give $K=(S^1)^3$ its product cell
structure and, for each nonempty $I\subset\{0,1,2\}$, let
$k_I:K\to\bigwedge_{i\in I}S^1=C_{|I|}$ be the ordered coordinate
projection followed by the product-to-smash quotient.  Order these
subsets as
''',r'''To construct the four-sphere homotopy retract, give $K=(S^1)^3$
its product cell structure. The based circle homeomorphism
$\vartheta:C_1\to S^1$ is $[a]\mapsto e^{2\pi ia}$; its inverse
chooses $0<a<1$ off $1$ and sends $1$ to the cube basepoint.
For each nonempty $I\subset\{0,1,2\}$, define
$k_I:K\to C_{|I|}$ by the ordered coordinate projection, the
product-to-smash quotient, the smash of the maps $\vartheta^{-1}$,
and $\mu_{1,\ldots,1}$. Its nonbasepoint cell coordinates are
exactly the selected ordered circle coordinates. Order the subsets as
''',['D20','D22'], 'Make the circle/cube identification and its inverse explicit before the seven-piece homology equivalence, preserving all cells and their degrees.',
     'wb:cusp-s12-nullity-scope')
edit(r'''and put $V=\bigvee_{I\ne\varnothing}\Sigma_{\mathrm{red}}C_{|I|}$.
''',r'''and put $V=\bigvee_{I\ne\varnothing}\Sigma_{\mathrm{red}}C_{|I|}$.
The summand $\Sigma_{\mathrm{red}}C_{|I|}$ is $C_{|I|+1}$ by
putting its suspension coordinate first; the inverse splits that
coordinate from the remaining block.
''',['D20','D22'], 'Specify the actual sphere coordinate map/inverse for each wedge summand, including the C4 retract.',
     'wb:cusp-s12-nullity-scope')

remark=r'''\begin{remark}[The two cusp postcompositions]\hypertarget{tag-Q257}{}\label{wb:remark:two-cusp-postcompositions}
{\normalfont\scriptsize tag Q257}\par
Use the same $q_2:X\to\mathcal A$ and ordered coordinates of
Definition~\ref{wb:def:native-sphere-carriers}. For
$K=S^1\times\overline T^2$, put
\[
 K^{(2)}=(\{1\}\times\overline T^2)
 \cup(S^1\times\{u_1=0\})\cup(S^1\times\{u_2=0\}),
 \qquad c_3:K\to K/K^{(2)}.
\]
The two actual based maps from $\mathcal A$ are
\[
 p_3[r,z,a]=[r,c_3(z,a)]\in\Sigma_{\mathrm{red},\epsilon}(K/K^{(2)})\cong S^4,
 \qquad
 \widehat p_2[r,z,a]=[r,c(a)]\in B\cong S^3.
\]
Both send $v_0,v_1$ to their target basepoints. The quotient relations
give the continuous maps and the exact composites
$H=p_3q_2$ and $g=\widehat p_2q_2$, on the punctured cusp and on
both collapsed ends.

At the common small-radius value with
$u^0=(-1/4,1/4)$ and $\varphi_0=\pi$, the coordinates of
\cref{wb:h24:ret:chart-lemma,wb:cusp-null:thm} give
\[
 N=\{(\rho_0e^{i(\varphi-a-b)},\rho_1e^{ia},\rho_2e^{ib})\},
 \qquad
 M=\{(\rho_0e^{i(\pi-a-b)},\rho_1e^{ia},\rho_2e^{ib})\}\subset N,
\]
where all phase variables are modulo $2\pi$ and
$(\rho_0,\rho_1,\rho_2)=(r_0^{1/2},r_0^{1/4},r_0^{1/4})$.
The inclusion in parameter coordinates is $(a,b)\mapsto(\pi,a,b)$;
projection to $(a,b)$ is its inverse on the image. In the open
target cells, the map from the retained coordinates to the
angle-forgotten coordinates is
$(r,\varphi,u_1,u_2)\mapsto(r,u_1,u_2)$.
The full differential calculations in the cited proofs give the
actual ordered normal four-frame of $M$ and three-frame of $N$.
The former induces the Lie stable tangent frame
$(-\partial_a,\partial_b)$ with Arf invariant one, with the
orientation comparison of \cref{wb:h24:ret:orientation-lemma}.
The latter is the derivative frame $\mathfrak n$ of
\eqref{wb:cusp-null:eq:actual-frame}, extended over the explicit
framed cap by \eqref{wb:cusp-null:eq:extended-frame}.

Consequently the two postcomposition homomorphisms, with the fixed
source $d$, have the proved values
\[
 (p_3)_*[q_2d]=[Hd]=\eta_4\eta_5\ne0\in\pi_6(S^4),\qquad
 (\widehat p_2)_*[q_2d]=[gd]=0\in\pi_6(S^3).
\]
The first equality is \cref{maps:src:B.3.1}, and the second is
\cref{wb:cusp-null:thm} with the target coordinates above.
In particular $[q_2d]\ne0$, since its image under $(p_3)_*$ is
nonzero. These two values are computed from the specified normal
frames and the same native quotient. The point-set quotient and
intrinsic metric applications use these same initial maps, as
proved in \cref{wb:cusp-s12-nullity-scope}.
\end{remark}
'''
tail='specified initial quotient maps of based null-homotopies.\n\\end{proof}\n'+text.split('specified initial quotient maps of based null-homotopies.\n\\end{proof}\n',1)[1]
assert tail.endswith('\n')
edit(tail,'specified initial quotient maps of based null-homotopies.\n\\end{proof}\n\n'+remark,
     ['D02','D11','D13','D14','D20','D22','D26'],
     'Own the full mathematical content moved from the old retained-angle comparison paragraph as numbered Q257 after both full framing proofs. Give both actual postcomposition maps, common source, parameterized fibre inclusion/inverse, local target projection, exact normal-frame classes and the detected nonzero q2 class. The remaining initial-map/metric clause is justified by complete038W. Root alone removes the old retained paragraph.',
     'wb:remark:two-cusp-postcompositions')
edit('\\end{proof}\n\n\n\n\n\n\n\\begin{proposition}[The postcomposition kernel and metric slices]',
     '\\end{proof}\n\n\\begin{proposition}[The postcomposition kernel and metric slices]', ['D23'],
     'Remove only the inherited blank-line gap between the two complete formal units.',
     'wb:cusp-s12-nullity-scope')
units.check_permanent_identifiers(old_all,text,['wb:remark:two-cusp-postcompositions'],['tag-Q257'])
_,changes,issues,aliases=presentation.remove_manual_equation_tags(text)
assert not changes and not issues and not aliases
assert not presentation.unresolved_literal_equation_references(text)
path.write_text(text,encoding='utf-8',newline='\n')
with table.open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
print('EXACT_EDITS_TOTAL',number,'DEFECT_ROWS',len(rows),'NEW_ID','Q257')
print('FINAL_CANDIDATE',len(text.splitlines()),hashlib.sha256(text.encode()).hexdigest())
print('ALL_OLD_IDENTITIES_PRESERVED; NO_SHARED_WRITES; NO_INDEPENDENT_CREDIT')
print(remark)
