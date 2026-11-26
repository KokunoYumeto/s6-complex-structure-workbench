"""One exact lattice proof for both strong and column-only hypotheses."""
from S6_SERIES_PUBLISH_c3_edit import *

lemma=r'''\begin{lemma}[Rank-one tensors in a conormal lattice]\hypertarget{tag-P259}{}\label{lem:II:rank-one-conormal-lattice}
\StatementRecord{lem:II:rank-one-conormal-lattice}{proved}{P259}{}
Let $\mathcal O=\mathbb C\{t\}$, let $K=\mathcal Oe_1\oplus\mathcal Oe_2$,
and let $E=t^a\mathcal Oe_1\oplus t^b\mathcal Oe_2$ with $0\le a\le b$.
For a primitive vector $\ell=u e_1+v e_2$, put $L=\mathcal O\ell$,
\[
 \alpha=\operatorname{length}(L/(L\cap E)),\qquad
 \beta=\operatorname{length}((K/L)/\operatorname{im}E).
\]
Then $\alpha+\beta=a+b$ and $\beta\ge a$.
For a rank-one symmetric tensor $T=\varepsilon t^d\ell^2$, with
$\varepsilon$ a unit, membership in $\operatorname{Sym}^2E$ gives
$d/2+\beta\ge a+b$. The inclusion in $E$ of every column of $T$
gives $d/2+\beta\ge a+b/2$. The column condition is independent
of the chosen basis of $K$.
\end{lemma}
\begin{proof}
The inclusion and projection maps give the exact sequence
\[
 0\longrightarrow L/(L\cap E)\longrightarrow K/E
 \longrightarrow (K/L)/\operatorname{im}E\longrightarrow0,
\]
so $\alpha+\beta=a+b$. Since $E\subset t^aK$, its image in
the free rank-one quotient $K/L$ is contained in $t^a(K/L)$,
giving $\beta\ge a$. Directly, with the order of a zero coordinate
read as infinity,
\[
 \alpha=\max\{a-\operatorname{ord}u,b-\operatorname{ord}v\},\qquad
 \beta=\min\{a+\operatorname{ord}v,b+\operatorname{ord}u\}.
\]
Membership of $T$ in $\operatorname{Sym}^2E$ gives $d\ge2\alpha$
by its two diagonal coefficients; the mixed coefficient satisfies
the intermediate inequality. This proves the first bound.
For the second, one coordinate of $\ell$ is a unit, so its
corresponding column puts $t^d\ell$ in $E$. Thus $d\ge\alpha$,
and $d/2+\beta\ge(a+b+\beta)/2\ge a+b/2$.
Under a basis change the columns are invertible linear combinations
of the same homomorphism $K^*\to K$; their membership in $E$ is
the intrinsic inclusion of its image in $E$.
\end{proof}

'''
anchor=r'\begin{proposition}[Two identifications in the tacnodal ruled case]'
apply_edit(anchor,lemma+anchor,'II-C3-CONORMAL-LATTICE-OWNER',['D12'],
 'lem:II:rank-one-conormal-lattice; night:P4.42; night:P4R.16; night:P4R.17','Before the first full lattice application',
 'Give the strong symmetric-square and weaker column-only estimates one full proof through the identical inclusion/projection exact sequence and primitive line. The weaker hypothesis needed in R17 is preserved.')
s=SOURCE.read_text();a=s.index('On a branch\n'+r'put $E_0=');b=s.index('On normalized branch $i$',a)
old=s[a:b]
new=r'''On each normalized branch apply
\cref{lem:II:rank-one-conormal-lattice} with $E=E_0$, the same
saturated Hessian line $L$, exponent $d$ and quotient colength
$\beta=b_{\rm proj}$. Its symmetric-square bound is
$d/2+b_{\rm proj}\ge a+b$ for the elementary-divisor orders $(a,b)$.
'''
apply_edit(old,new,'II-C3-TWO-IDENTIFICATION-LATTICE-MAP',['D12'],'night:P4.42','Second proof item',
 'Use the same normalized conormal lattice, primitive Hessian line and quotient projection at the shared owner. The subsequent residue/different calculation is unchanged.')
s=SOURCE.read_text();i=s.index(r'\label{night:P4R.16}');a=s.rfind(r'\begin{proposition}',0,i);b=s.index(r'\end{proof}',i)+len(r'\end{proof}');old=s[a:b];new=old
new=new.replace(r'''In the remaining positive ruled case with uniform transverse
type $A_3$, the three-branch point of the critical curve cannot''',r'''In the setting of \cref{lem:II:positive-ruled-conductor-graph},
with generic transverse type $A_3$ along every conductor component,
the three-branch point of the critical curve cannot''',1)
a=new.index(r'\item We first determine the symbolic square');b=new.index('Furthermore',a)
new=new[:a]+r'''\item Apply the symbolic-square identity in the proof of
\cref{night:P4.38} to the identical ambient coordinates, with
$h=y^2-x^4$ and $k=4$. That identity concerns only this reduced
curve ideal and its generic primes. It gives
\[
 P^{(2)}=(z,h)^2\cap(x,y)^2=P^2+(zh).
\]
The equality on the right uses $P=(xz,yz,h)$: the three
quadratic $z^2$ generators are in $P^2$, and the remaining
two generators are $zh,h^2$.
'''+new[b:]
a=new.index(r'\item For completeness,');b=new.index('The local defect',a)
new=new[:a]+r'''\item The preceding calculation proves $f\in P^2$.
On each branch apply the symmetric-square clause of
\cref{lem:II:rank-one-conormal-lattice} with $E=E_i\subset K_i$,
its primitive Hessian direction, $d=d_i$ and $\beta=b_i$.
The three exact elementary-divisor pairs just computed give
the respective bounds $3,3,2$ for $d_i/2+b_i$.
'''+new[b:]
new=new.replace('Here $q\\ge0$ is the further descent colength, retained\nrather than discarded from the definition.','Here $q\\ge0$ is the normalization descent colength.')
new=new.replace('(4.42a)',r'\eqref{eq:II:refined-4-42a}').replace('harmless common convention','common convention')
apply_edit(old,new,'II-C3-TACNODE-LINE-COMPLETE-UNIT',['D02','D04','D08','D12','D25'],
 'night:P4R.16','Complete tacnode-plus-line proof',
 'State the same positive ruled domain through its exact earlier owner. Transfer only the duplicated symbolic intersection and rank-one lattice proof, with the identity curve coordinates and the three displayed elementary-divisor pairs. Preserve the residue-field symbolic defect, rank-one Hessian argument forcing kappa=0, all generator matrices and lower bound eleven against the same total nine.')
add_event('lem:II:rank-one-conormal-lattice; night:P4.42; night:P4R.16',
 'II-C3-ROOT-LATTICE-OWNER-APPLICATIONS','used and rechecked in this run',
 'Root read the complete old strong estimate in P4.42 and R16 and the weaker estimate in R17. P259 proves both through 0->L/(L intersect E)->K/E->(K/L)/image(E)->0. The strong tensor membership gives d>=2alpha; the column-only condition gives d>=alpha with beta>=a. The P4.42 and R16 applications identify the same normalized lattice, saturated Hessian line and projected colength. Every original numerical inequality and proof step is retained at its single owner. The complete R16 unit was read; R17 receiving transfer follows separately. No independent or final-page credit.',
 'S6_SERIES_PUBLISH_II.tex: conormal lattice and exact applications',source=__file__)
for number in range(1,26):
 kind=f'D{number:02}'
 if kind in ['D10','D16']:continue
 status='open' if kind in ['D14','D18','D23'] else 'done'
 set_unit_status('night:P4R.16',kind,status,'Complete old/receiving unit read; final placement, bibliography and rendered typography remain open.' if status=='open' else 'Complete current unit read; all identified instances recorded and no local residue.','CHECK_EVENTS.tsv: II-C3-ROOT-LATTICE-OWNER-APPLICATIONS')
print('P259 and complete R16 receiving proof admitted.')
