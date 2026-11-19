"""Preserve cited inputs and write the checked BC/Green specializations."""
from pathlib import Path
import csv,json
P=Path(__file__).resolve().parents[2]
S=(P.parents[1]/'sources/s6_09/S6_09_PAPERS_I.tex').read_text()
J=json.loads((P/'analysis/inventory_source_index.json').read_text())
def statement(key):
 d=J[key];return S[d['start']:d['statement_end']]
def save(label,s,uses,proof=''):
 text=s+'\n\\Uses{'+uses+'}\n'
 if proof:text+='\\begin{proof}\n'+proof+'\n\\end{proof}\n'
 (P/'papers/I/revisions'/(label.replace(':','_')+'.tex')).write_text(text)
s=statement('S6_01_INVARIANTS:A1.0')
s=s.replace('The direct images',r'This is the structure-sheaf calculation of Claude and Alp\"oge: '+r'\cite[Lemma~9.12, pp.~72--74; Proposition~9.13, pp.~74--76, and the base-change clarification on p.~92]{AC2026}. The direct images',1)
save('inv:A1.0',s,r'\cite[Lemma~9.12, pp.~72--74; Proposition~9.13, pp.~74--76; p.~92]{AC2026}')
s=statement('S6_01_INVARIANTS:C3.1')
s=s.replace('Let $G$',r'The Picard-group identification and fibrewise injectivity below are due to Claude and Alp\"oge \cite[Theorem~10.5(b), proof Steps~1 and~4, p.~88]{AC2026}. We compute the real Chern map and a specified Green-operator representative in that coordinate. Let $G$',1)
proof=r'''
By \ref{inv:C1.1}, the Dolbeault image of $\mathsf A$ is
$d_1g\ne0$. The class $\mathsf B=\overline{\mathsf A}$ is nonzero,
whereas its Dolbeault image is zero. Thus these two classes are
independent; the dimension calculation of \ref{inv:C2.1} makes
them a basis. In this basis conjugation sends $(a,b)$ to
$(\bar b,\bar a)$, so its fixed real subspace consists precisely
of $(z,\bar z)$.

The exponential sequence and $H^1(X;\Z)=H^2(X;\Z)=0$ give the
cited identification $\Pic(X)=H^1(X,\OO_X)=\C g$.
On a smooth trivial line with unit frame $s$, put
$\bar\partial_zs=-2\pi izG\otimes s$. Integrability follows from
$\bar\partial G=0$. On a cover with $G=\bar\partial\phi_i$,
the holomorphic frames $e_i=e^{2\pi iz\phi_i}s$ satisfy
$e_j=e^{2\pi iz(\phi_j-\phi_i)}e_i$; hence this is exactly the
line represented by the exponential of the Cech class $zg$.
Its unitary Chern connection and curvature are
\[
 \nabla_z=d-2\pi i(zG+\bar z\bar G),\qquad
 F_z=-2\pi i(z\partial G+\bar z\bar\partial\bar G).
\]
Multiplication by $i/(2\pi)$ proves \eqref{inv:eq:C-Pic-map}.
The two independent basis vectors prove injectivity, additivity
as real Lie groups and the assertion about the image.

The closed real form $\theta$ is exact since $H^2(X;\R)=0$.
It has zero harmonic projection. De Rham Hodge decomposition,
with $d\mathcal G_d=\mathcal G_dd$, therefore gives
$dd^*\mathcal G_d\theta=\theta$. The Green operator and $d^*$
preserve reality, so $\alpha$ is real and $d\alpha=\theta$.
The $(0,2)$ component yields $\bar\partial G_0=0$.
To prove nonvanishing, an equation $G_0=\bar\partial u$ would give
\[
 \theta=\partial\bar\partial(u-\bar u)
       =2i\partial\bar\partial\operatorname{Im}u.
\]
Semipositivity of $\theta$ would make $\operatorname{Im}u$
plurisubharmonic. The maximum principle on compact connected $X$
would make it constant, contradicting the nonzero pullback of
$\omega_{FS}$ on the regular locus of $f$.

Since $\alpha=G_0+\bar G_0$, the Chern formula already proved
sends $\exp([G_0])$ to $[\theta]_{BC}$, which is also
$c_{1,BC}(f^*\OO(1))$. Its injectivity proves the stated
line-bundle equality, with exactly the declared $2\pi i$
exponential and curvature conventions.

For the last assertion, the exact sequence of a full scheme
fibre is
\[
 0\longrightarrow f^*\OO(-1)\longrightarrow\OO_X
   \longrightarrow\OO_{X_b}\longrightarrow0.
\]
The cited direct images in \ref{inv:A1.0} give
$f_*f^*\OO(-1)=\OO(-1)$ and
$R^1f_*f^*\OO(-1)=\OO(-1)\oplus\OO(-2)$.
Both terms bounding $H^1(X,f^*\OO(-1))$ in the degree-one Leray
edge sequence vanish, so this group vanishes. Restriction on
$H^1(\OO)$ is injective. On a smooth fibre, the same edge map is
the evaluation of $H^0(B,G)=\C\gamma^{0,1}$ in $G_b$.
This identifies its image as claimed and reproduces exactly
the application of \cite[Theorem~10.5(b), Step~4, p.~88]{AC2026}.
'''
save('inv:C3.1',s,r'\cref{inv:C1.1,inv:C2.1,inv:A1.0}; \cite[Theorem~10.5(b), proof Steps~1 and~4, p.~88]{AC2026}',proof)
s=statement('S6_01_INVARIANTS:C3.8')
s=s.replace('This concerns\ncohomology classes and does not assert literal equality of arbitrary\nsmooth representatives with an invariant fibre form.',r'The map is induced by pullback of $\partial\bar\partial$-closed forms followed by the quotient by $\partial$- and $\bar\partial$-exact forms on $F_b$. Thus it specifies the class of each restricted representative through that exact quotient map.')
s=s.replace('This is the\nunfulfilled literal-coefficient requirement, not an undecided Hodge\nnumber, product, or existence of the Leray class.','The coefficient functions on that specified common atlas remain open.')
proof=r'''
We verify the settled operator assertions in this open question.
The Green formula and $\exp([G_0])=f^*\OO(1)$ were proved in
\ref{inv:C3.1}; the primitive marking in \ref{inv:C3.2} then gives
$[G_0]/12=g_\gamma$.

Restriction of a Dolbeault-harmonic representative is a closed
Dolbeault form on the regular fibre. By \ref{inv:A3.2}, its class
is $c\eta$. Integration against the closed $(1,1)$ form $\eta$
annihilates Dolbeault-exact changes by Stokes' theorem. Since
$\int_F\eta^2=-12$, the displayed functional gives $\ell(e)=c$.
The image is $\C\eta$, hence $\ell$ is nonzero on the
 two-dimensional harmonic space and its squared norm
$|\ell(e_1)|^2+|\ell(e_2)|^2$ is positive.

For another orthonormal basis $e'_j=\sum_k U_{jk}e_k$ with
$U$ unitary, put $l_k=\ell(e_k)$. Then $l'=Ul$ and
\[
 \sum_j\overline{l'_j}e'_j
 =\sum_{j,k,r}\overline{U_{jk}}\bar l_k U_{jr}e_r
 =\sum_k\bar l_ke_k,
 \qquad \sum_j|l'_j|^2=\sum_k|l_k|^2.
\]
Thus $Q$ is independent of the orthonormal basis. It is a linear
combination of harmonic forms and $\ell(Q)=1$, so its fibre class
is precisely $\eta$. These computations establish the operator
representatives and their restrictions. They leave the stated
evaluation of their coefficient functions on a common global
atlas unevaluated.
'''
save('inv:C3.8',s,r'\cref{inv:A3.2,inv:C3.1,inv:C3.2,inv:C3.7}',proof)
p=P/'records/root_events.tsv';rows=list(csv.DictReader(p.open(),delimiter='\t'));fields=list(rows[0])
checker='GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro, S6_10_PAPERS'
E=[('inv:A1.0','exact primary-source check','Read AC26 original PDF pp72–76 and p92: matched the entire structure-sheaf statement to Lemma9.12 and Proposition9.13, including cyclic exponents, gamma subbundle, cusp cup pairing and full scheme-fibre base-change maps. Its expanded re-derivation remains a compendium proof of a known input.'),('inv:C3.1','targeted proof check','Re-derived the explicit Cech exponential-to-unitary-connection morphism, curvature sign and real BC image; checked the Green identity, nonvanishing via compact plurisubharmonic maximum principle and exact f*O(1) identification. Read AC26 Th10.5(b) Steps1/4 p88 for the separately credited Picard/fibre restriction input and included its short exact-sequence application.'),('inv:C3.8','targeted open-boundary check','Re-derived the harmonic Riesz representative, positivity of its denominator, exact restriction coefficient and invariance under a unitary change of basis; added a receiving proof for these settled assertions. The literal common-atlas coefficient evaluation remains open; no elliptic inverse was numerically evaluated.')]
for label,kind,out in E:
 if not any(r['statement_id']==label and r['outcome']==out for r in rows):rows.append(dict(zip(fields,[label,'2026-11-18',checker,kind,out])))
with p.open('w') as f:w=csv.DictWriter(f,fields,delimiter='\t');w.writeheader();w.writerows(rows)
f=P/'analysis/I_sources/current_source_matches.json';d=json.loads(f.read_text());r=d.get('AC2026',{})
r.update({'exact_locator':'Original attached108-page PDF: Lemma9.12 pp72–74; Proposition9.13 pp74–76; base-change clarification p92; Theorem10.5(b), proof Steps1 and4 p88.','scope':'Complete inv:A1.0 known structure-sheaf input, Picard identification and injectivity on every full scheme fibre for inv:C3.1. Current reading does not credit the specialized BC/Green operator formulas to AC26.','source_path':'sources/original/AC26_original_manuscript.pdf','sha256':'283bba102dd1d5dc346af81b28145bdaaea6654398d5032e76e97bafb9a858f2'})
d['AC2026']=r;f.write_text(json.dumps(d,indent=2,ensure_ascii=False))
print('Wrote three checked input/specialization revisions; events',len(rows))
