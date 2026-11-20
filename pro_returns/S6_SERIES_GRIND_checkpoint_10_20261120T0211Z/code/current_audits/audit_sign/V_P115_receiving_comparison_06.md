# P1.15: computed extension quotient and receiving comparison

The isolated statement derivation was frozen in `V_P115_statement_derivation_06.md` (SHA256 `04a8d3a6a6477288ceb11822e8d1efcf07b2cd8e2b7573fe354c1ca879de81fb`) before any further proof access. The exact prior exposure remains the build12 V contact-sheet layout inspection, including pages109,118,122,124,125. This is not labelled completely blind. The quotient connection and its integral-local-system identification are named supplied inputs; the new derivation concerns the entire upper extension, contraction and common-intertwiner interface.

## Exact result and actual isomorphism

The root-frame inequalities give the four-dimensional row space with parameters `(A,B,C,D)`. The quotient residue R has square zero and rank2. The full square-zero condition is exactly

\[
 A=-\frac{25}{6}C+\frac53D,\qquad
 B=-\frac{125}{48}C-\frac{25}{3}D.
\]

The actual gauge row is `r0 Gamma_W`, `r0=(0,0,1,0,0)`, with parameter vector `(300,-375,-48,60)/3125`. Hence the quotient class is `s=C+4D/5`. The displayed target has class1. Every admissible row has the exact decomposition

\[
 \beta=s b+t r_0\Gamma_W,\qquad t=3125D/60.
\]

For the supplied nonsplit extension s is nonzero. The fixed-line bundle map and its inverse are

\[
 C_{s,t}=\begin{pmatrix}1&-t r_0\\0&sI_5\end{pmatrix},\qquad
 C_{s,t}^{-1}=\begin{pmatrix}1&(t/s)r_0\\0&s^{-1}I_5\end{pmatrix}.
\]

The row-frame transformation gives

\[
 C_{s,t}^{-1}\Gamma_bC_{s,t}+C_{s,t}^{-1}dC_{s,t}
 =\begin{pmatrix}0&\beta\\0&\Gamma_W\end{pmatrix}.
\]

The matrices are holomorphic bundle maps on the root curve: the off-diagonal row is precisely its unique global Hom section, the quotient scalar is nonzero, and the invariant section e is fixed. Their basepoint values supply the actual common monodromy isomorphism, with the original based positive meridians. This establishes existence independently of any numerical residual containment.

## Contraction and normalized uniqueness

The normalized kernel vector is

\[
 v=(-4096/1171875,64/1875,1,0,0)^t.
\]

It satisfies `R v=0`, and the target residue row evaluates to `625/192`. The algebraic contraction evaluates to `4/3`, so the ratio is `625/256`. Multiplication by the stipulated `2 pi i` yields exactly `(625 pi i/128) alpha_alg`. Every allowed splitting change vanishes on this kernel because its residue correction is `-tau R`. The global contraction space on P is one-dimensional: its three dual summands have coarse degrees `-1,-1,0`. Thus this one-line evaluation fixes the whole contraction map.

The supplied integral matrices have common invariant space `C e0` and zero common invariant covector space. Their 72-equation simultaneous-centralizer system in36 unknowns has rank35 and basis `I6`; adding `Z e0=0` gives rank36. Any two common intertwiners fixing e0 therefore agree. The target full residue has rank3 and square zero; an exact gauge extension has rank2. These computations also verify the nonsplit character without a numerical matching argument.

## Actual receiving read

After the freeze and successful exact computation I read all four complete receiving proof steps in `audit_corrections/V_P115_receiving_proof_06.tex` (SHA256 `7878bb63c85af1bb4ab18c9a66d999ee64fb74f7b77d6ec4a440994ac9bbb5be`) and the immediately following normalized-X and splitting-translation paragraph in `parts/V.body.linked.tex`.

Step3's two residue-basis vectors, its exact gauge relation and its nontrivial-extension argument agree with the independent derivation. Step4's kernel, residue contraction and scalar agree exactly. The root-frame powers in the statement give the same entrywise bounds used in that step. The normalized-X existence assertion is supplied by the explicit fixed-line equivalence above, and its uniqueness is supplied by the scalar centralizer. Steps1–2 identify the quotient connection and de Rham/root bundles; those are the pre-existing inputs of this fresh derivation, not claimed as newly independently rederived here. No fault was found in the upper-extension argument.

The phrase “sole nonconstant holomorphic splitting change” should read “holomorphic splitting changes are constant multiples of the row selecting w0.” `V_P115_receiving_guard_06.json` gives that repair together with the explicit fixed-line matrix and inverse. The separate later numerical period bounds are outside this check.

## Certificate and attribution

`code/V_P115_extension_independent_06.py` and `V_P115_extension_independent_06.json` record40 passing exact rational assertions, including all matrix inputs, upper parameter solution, root coefficients, full residue, kernel, class functional and centralizer basis. The program imports no prior checker or residue output. Current derivation, producing checks, receiving comparisons and parent work are all within the same GPT-6 Astra model family. The new conclusion is an exact fresh method and scoped proof comparison, not a new-model-family verification or a claim of zero prior image exposure.
