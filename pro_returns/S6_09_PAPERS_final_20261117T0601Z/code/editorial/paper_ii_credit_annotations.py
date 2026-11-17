"""Exact positive credit matches from opened original AC26 statements.
No negative literature-absence claim is inferred by this module.
"""
KNOWN={'D.1.1','D.1.3','E19','E2','E3','C.1.2','E4'}
CREDIT={
'E4':r'This is \citet[Theorem~2.2, pp.~4--5]{Viaclovsky2026Combs}, under its standing proper connected map from a complex manifold to a disc. That source attributes an outline to Ofer Gabber, communicated by Brian Conrad, and relates it to Raynaud. We retain the complete re-derivation below with that credit.',
'D.1.12':r'The torus-fibred six-sphere case and the cup-product index method are \citet[Theorem~2.3, pp.~5--6]{Viaclovsky2026Combs}. The statement here has the displayed broader hypotheses: $b_2=0$, an arbitrary base curve, and also primary Kodaira general fibres. The complete proof specifies the additional integral comparison for those hypotheses.',
'E2':r'The vanishing, Euler-index and third-Chern-number conclusions are \citet[Theorem~3.1, p.~9]{LRS2019}; its sphere consequence is Corollary~3.2 there. The extension from $\operatorname{Pic}^0$ to each component follows by tensoring the arbitrary vector bundle with a fixed representative of that component. We retain the complete graph proof below as a credited re-derivation, with the multiplicity filtration made explicit.',
'E3':r'The Moishezon assertion is \citet[Lemma~1.4]{CDP98}. The sphere assertions follow from \citet[Theorem~3.1 and Corollary~3.2, p.~9]{LRS2019}. We retain the complete deduction as a known consequence.',
'C.1.2':r'This conclusion is \citet[Corollary~1.3]{CDP98}, together with Serre duality. Tensoring by a fixed representative gives the assertion on each Picard component. The explicit exponential-family construction below expands the complete re-derivation of that conclusion.',
'D.1.1':r'This semidirect-product abelianization is \citet[Lemma~10.7, p.~90]{AC2026}. We retain the complete re-derivation below, including the dependence of the direct-sum splitting on the chosen splitting of the extension.',
'D.1.3':r'The monodromy invariants, coinvariants and resulting corrected component count are contained in \citet[Lemma~2.7, Section~10.5, p.~91, and Appendix~A]{AC2026}. The exact matrix calculation below is retained as a re-derivation in the common marking.',
'E19':r'The fundamental group and full integral homology tuple for every admissible affine datum are \citet[Theorem~7.17, p.~57; Theorem~7.22, p.~60]{AC2026}. We retain the distinct integral gluing-matrix proof below as a re-derivation. The final algebraic-dimension and deformation conclusions apply Proposition~\ref{cdp:st:E11} and are separate from that topological credit.',
'D.1.2':r'The rational component-count formula is the correction in \citet[Section~10.5, p.~91]{AC2026}. The integral torsion-free conclusion under the displayed integral hypotheses is an additional clause; its full argument is included here.',
'D.1.5':r'The bielliptic-product rank defect is already described in \citet[Section~10.5, p.~91]{AC2026}. The full integral torsion calculation, the coherent direct images and the separate rational-elliptic product below retain their additional precise content.',
'A.4.1':r'The nonvanishing on the compact example and the torsion-free-cotangent vanishing are contained in \citet[Theorem~10.5 and Section~10.4]{AC2026}. The present calculation sharpens the ambient section dimension to exactly one; that sharper equality and its proof are distinguished from the source nonvanishing.'
}
def annotate(s,sid):
 if sid not in CREDIT:return s
 if sid in KNOWN:
  import re
  s=re.sub(r'\\begin\{proposition\}(?:\[([^\]]*)\])?',lambda m:r'\begin{proposition}[Credited re-derivation'+(': '+m[1] if m[1] else '')+']',s,count=1)
 marker=r'\end{proposition}'
 assert marker in s,sid
 return s.replace(marker,marker+'\n\n'+CREDIT[sid]+'\n',1)
