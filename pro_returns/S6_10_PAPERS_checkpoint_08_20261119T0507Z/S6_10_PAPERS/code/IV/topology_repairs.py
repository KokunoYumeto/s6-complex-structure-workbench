"""Local changes after the current integral topology proof reviews.

Executed in revise_body.py's namespace (s, change, add_uses, W, P, changes).
"""
def complete_f20(t):
    old='At the remaining \\(I_1\\) the scalar zero gives the unimodular two-period toric model, with its standard hexagonal component and integral specialization.'
    new=r'''At the remaining \(I_1\) the scalar zero gives the unimodular two-period toric model. The complete normalization matrices, saturated invariant bases and the actual period-equivariant cross line in \cref{iv:rank_two_specialization} prove its integral specialization in every degree, retaining all four unit multipliers.'''
    assert old in t
    t=t.replace(old,new,1)
    old="These are the displayed local charts in the supplied source's Lemma \\texttt{fill:tate} and Propositions \\texttt{fill:rankone}, \\texttt{fill:a2}; the exponent and primitive collapse calculations above verify their use here."
    new=r'''These are the displayed local charts in \cite[Lemma 2.6 and Propositions 2.7--2.8, pp.~4--6]{Wang2026}; the exponent and primitive collapse calculations above, and the complete integral proof just given, verify their use here.'''
    assert old in t
    return t.replace(old,new,1)
change('night:P3F.20',complete_f20,
       'Supply the full integral rank-two specialization morphism and matrices, and resolve the original-only source labels to the opened numbered statements.')

def complete_f21(t):
    old=r'''The rank-two local fan is the unimodular one in E26, Lemma 7.4; its normalization-and-double-curve cellular calculation applies verbatim because both period vectors form an integral basis. Its hypotheses are exactly the checked valuation vectors \((1,0),(0,1)\), the same triangulation and unit changes of coordinates. Its top specialization has degree one off the double curves.'''
    new=r'''For the rank-two local fan, \cref{iv:rank_two_specialization} gives the actual map of the unit-bearing family to its zero-unit model, both integral normalization matrices, every saturated invariant generator and a descended Cartier line realizing the cross generator. The unit-square fan and the checked valuation vectors \((1,0),(0,1)\) are exactly those in that proof. Its specialization is therefore an integral isomorphism in every degree, with no index inferred from a rational dimension count.'''
    assert old in t;t=t.replace(old,new,1)
    old=r'''The group \(\Theta _6\) is zero (Kervaire--Milnor, the table on printed p.505), so it is diffeomorphic to the standard \(S^6\).'''
    new=r'''The table of \(\Theta_n/bP_{n+1}\) on printed p.~512 of \cite{KervaireMilnor1963} gives \(\Theta_6/bP_7=0\); Theorem 5.1 on that same page gives \(bP_7=0\). Hence \(\Theta_6=0\), and this homotopy sphere is diffeomorphic to the standard \(S^6\).'''
    assert old in t;t=t.replace(old,new,1)
    old='It is trivial there because its Chern class has degree zero on every component.'
    new=r'''The chosen Hermitian norm gives its explicit trivialization: the class of a nonzero vector \(v\) modulo the unit circle maps to \((\pi(v),\|v\|)\), with inverse the circle orbit of any vector of that positive norm. This is a smooth map through every source node because the line itself is invertible there.'''
    assert old in t;t=t.replace(old,new,1)
    old=r'''\path{code/part3/os47_topology.py} has executed successfully. Its JSON file contains the modular coset table, the complete integral Jacobi tuple, the symbolic uniqueness equation for the geometric section lift, the fundamental-group relation matrices, every exterior-power local image basis, every entry of the parabolic differentials, the finite specialization indices and all four integral clutch contractions. The printed output records \(d_2=(1,1,1,1)\), sphere homology and the page expression four. No prior-run code or proof is imported.'''
    new=r'''The received \path{os47_topology.py} was read in full and rerun on 18 November 2026 at 04:29 UTC; its unchanged source hash and current execution are recorded in \path{code/IV/replay_os47_other/current_execution.json}. Its output contains the modular coset table, integral Jacobi tuple, geometric-section uniqueness equation, fundamental-group relation matrices, full exterior and parabolic matrices, specialization indices and four clutch contractions. The received output field \path{page_index_expression=-4} is the meridian-line index \(A_U\). The positive page expression and physical index are \(4\), by the actual extending duality above. The separate current rational-function calculation in \path{code/IV/os47_sevenfold_section.py} verifies the full coordinate of \(7G\) and its ordinary pole. These executions supplement the complete geometric proof and do not replace its cap, line or orientation maps.'''
    assert old in t;t=t.replace(old,new,1)
    return t
change('night:P3F.21',complete_f21,
       'Complete the integral cusp input, correct the exact Theta6 locator and quotient table, give the actual positive-norm trivialization, and separate current execution from historical output with its retained U-line sign.')

for label,uses in {
 'night:P3F.18':r'\cite[Lemma 2.1, pp.~3--4; Lemma 3.2, p.~7; equations (3.11)--(3.14), p.~8]{Viaclovsky2026Two}; \cite[Proposition 2.1, pp.~3--4; Proposition 2.12, pp.~7--8; Definition 3.7, p.~10]{LiuRollenske2026}',
 'night:P3F.19':r'\cite[Lemma 7.1 and Theorem 7.2, pp.~40--41, attached repaired edition]{Yang2026}',
 'night:P3F.20':r'\cref{iv:rank_two_specialization}; \cite[Theorem 1.1, p.~2; Propositions 2.7--2.8, pp.~4--6; Sections 4--6, pp.~9--15]{Wang2026}',
 'night:P3F.21':r'\cref{iv:rank_two_specialization,night:P3K.68}; \cite[Proposition 3.4, p.~204]{Miranda1990}; \cite[Theorem 8.6, table (8.16), Proposition 8.12, pp.~228--231]{Shioda1990}; \cite[table of $\Theta_n/bP_{n+1}$ and Theorem 5.1, p.~512]{KervaireMilnor1963}',
 'night:P3F.23':r'\cref{night:P3K.68}',
}.items():
    change(label,lambda t,u=uses:add_uses(t,u),'Add the exact current primary-source locators and completed integral or typed-line dependency.')

archive=W/'analysis/IV/full_rederivations'
archive.mkdir(exist_ok=True)
def keep_application(t,label,statement,proof):
    (archive/(label.replace('night:','')+'.tex')).write_text(
        '% Full current rederivation retained as research source; the receiving paper cites the known portion.\n'
        +r'\begin{theorem}'+t+'\n')
    # The statement record is before the statement.  Its fourth braced argument
    # ends at the beginning of the received statement, located by its exact text.
    marker={'night:P3F.19':'Yang Type B and Type C have explicit',
            'night:P3F.20':"Wang's supplied threefold is simply"}[label]
    a=t.index(marker)
    return t[:a]+statement+'\n'+r'\end{theorem}'+'\n'+proof

f19statement=r'''For the Type B and Type C attachments of \cite[Theorem 7.2,
pp.~40--41, attached repaired edition]{Yang2026}, the actual boundary
presentation has the surjective quotient maps to \(\mathbb Z/2\)
and \(\mathbb Z/3\) constructed below, for every admitted twist.
These maps obstruct a homeomorphism of either family member with
\(S^6\).  The complete source presentation and the canonical exact
groups are Yang's cited theorem.'''
f19proof=r'''\begin{proof}
\begin{enumerate}[label=\arabic*.]
\item Use the full finite and cusp attaching presentation in the cited
Theorem 7.2.  Its finite multiplicities are \((m_1,m_2)=(4,6)\)
and \((3,6)\), respectively.  Put \(g=\gcd(m_1,m_2)\).
\item Kill every fibre loop, send the two finite meridians to
\(1,-1\in\mathbb Z/g\), and send the cusp meridian to zero.
Every semidirect relation holds.  A finite power relation has fibre
translation on its other side, so it maps to zero because \(g\mid m_i\).
The cusp relation also has only its meridian and fibre translations,
and the sphere relation maps to \(1-1+0=0\).  Thus this is an actual
map of the complete boundary presentation, and it is onto because
the first meridian maps to one.
\item A homeomorphism induces an isomorphism on fundamental groups.
The displayed nontrivial quotients therefore exclude a homeomorphism
to the simply connected \(S^6\).  For the canonical twists the
exact groups \(\mathbb Z/2\) and \(\mathbb Z/3\) are already
the conclusion of Yang's theorem; no second proof of them is needed.
\end{enumerate}
\end{proof}'''
change('night:P3F.19',lambda t:keep_application(t,'night:P3F.19',f19statement,f19proof),
       'Condition 2: cite Yang’s known complete presentation and canonical groups; retain only the full short quotient morphism used for the sphere obstruction. Archive the complete current rederivation separately.')

f20statement=r'''For Wang's threefold, the primitive \(I_2\) filling has the
literal coordinate and specialization maps below, and its physical
line circle has isotropy \(\mathbb Z/2\) on the pinching locus.
The global conclusions \(\pi_1=0\) and
\(H_2=H_3=\mathbb Z/2\) are
\cite[Theorem 1.1, p.~2; proof in Sections 4--6, pp.~9--15]{Wang2026}.
The comparison retains the specified primitive filling and the
component-supported OS49 application stated in the proof.'''
f20proof=r'''\begin{proof}
\begin{enumerate}[label=\arabic*.]
\item Wang's cited construction uses source configuration
\(IV^*,I_2,I_1,I_1\), line \(M=\mathcal O(P-O)\), translation
by \(-6P\), and one order-three logarithmic cap.  Its topology is
the cited theorem.  Its nonzero \(H_2\) obstructs a homeomorphism
to \(S^6\) by the induced map on integral homology.
\item Retain the actual local periods
\[
h(z,v)=(q^2c_1z,qc_2v),\qquad
g(z,v)=(c_3z,\lambda c_4v),
\]
where the \(c_i\) are holomorphic units and the second generator
is the original lift multiplied by \(h^3\).  The invertible
monomial map
\[
 (z,v)\longmapsto(x,y)=(v,v^2/z),\qquad
 (x,y)\longmapsto(z,v)=(x^2/y,x)
\]
sends the exponent \((2,1)\) to \((1,0)\).  The zero-exponent
period multiplies \(y\) by \(\lambda^2c_4^2/c_3\), retaining
its strict contraction.  The ray fan therefore gives the actual
one-component primitive rank-one collapse.  Its surviving one-cell
and its two-cell both have coefficient one.  The other rank-one
filling has the same primitive collapse; the unit-bearing rank-two
filling has the full specialization morphism of
\cref{iv:rank_two_specialization}.  This supplies the explicit
local comparison required here, including the integral indices.
\item On the angular two-torus, the physical line circle is
\(\theta\mapsto(0,\theta)\), and the pinched circle is
\(a\mapsto(2a,a)\), both modulo \(\mathbb Z^2\).
Their intersection is obtained from \(2a\in\mathbb Z\):
\(a=0,1/2\) modulo one.  The physical line circle therefore has
exact stabilizer \(\{0,1/2\}\cong\mathbb Z/2\) on that
pinching locus.  This follows from the actual primitive collapse,
so the order-two isotropy is retained in further orbit comparisons.
\item For the component-supported OS49 source with \(Q=3P\),
the regular-binding degree-three page has three \(II\) and three
\(I_2\) fibres.  Thus \(\chi(\mathcal O)=1\), \(\sigma=-8\),
\(h(P)=1/2\), and the reducible-fibre correction is \(3/2\).
The height formula gives \(P\cdot O=0\).  Its actual
component-permuting translation and positive-fan page are carried
through \cref{night:P3F.31,night:P3F.32}, giving index zero.
The complete native closing and ruling map in \cref{night:P3K.65}
gives negative-fan class \(-3\) for \(\lambda=r^3\) and
\(-1\) for the constructed shorter loop \(\lambda=w\).
These are the specified maps and page data; the source-configuration
enumeration in \cref{night:P3F.1} supplies no numerical bounds
for an additional bounded slice of all compact fillings.
\end{enumerate}
\end{proof}'''
change('night:P3F.20',lambda t:keep_application(t,'night:P3F.20',f20statement,f20proof),
       'Condition 2: cite Wang’s known global topology; retain complete proofs of the literal primitive coordinate/collapse comparison, line-circle isotropy and the needed OS49 local application. Archive the full current topology rederivation.')

marker=r'\begin{theorem}\label{night:P3F.20}'
assert s.count(marker)==1
assert s.count(r'\label{iv:rank_two_specialization}')==1
changes.append({'label':'iv:rank_two_specialization','reason':'Add the complete integral normalization, actual family flow and Cartier-line specialization proof; current proof and independent exact algebra checks are separately recorded.'})
