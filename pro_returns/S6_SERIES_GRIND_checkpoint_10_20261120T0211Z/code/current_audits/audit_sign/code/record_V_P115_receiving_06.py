from pathlib import Path
import json,csv,hashlib
A=Path(__file__).resolve().parents[1];W=A.parent
report=W/'audit_corrections/V_P115_receiving_proof_06.tex'
text=report.read_text();sha=hashlib.sha256(report.read_bytes()).hexdigest();assert sha=='7878bb63c85af1bb4ab18c9a66d999ee64fb74f7b77d6ec4a440994ac9bbb5be'
old='''The sole nonconstant holomorphic splitting change is the row selecting
$w_0$, and its connection coboundary is the third row of $\\Gamma_W$.
In these two basis vectors that row is $(-48b_1+60b_2)/3125$.
Thus there is one nontrivial flat extension direction modulo splitting
changes and rescaling of the invariant line.  The first vector has
rank-three square-zero cusp residue, so it represents that direction.
The supplied extension is nontrivial, since its dual has no common
invariant vector by P1.1.  It is therefore isomorphic to (1.15.1).
This proves the connection identification without inferring it from
the subsequent numerical matching.'''
new=r'''The holomorphic splitting changes are the constant multiples of the
row $r_0=(0,0,1,0,0)$ selecting $w_0$.  Its connection coboundary
is the third row $r_0\Gamma_W$, whose parameter vector is
$(-48b_1+60b_2)/3125$.  The quotient by this exact gauge direction
is one-dimensional, with coordinate $s=c+4d/5$.  The first
vector has $s=1$ and rank-three square-zero cusp residue.

The supplied extension is nontrivial, since its dual has no common
invariant vector by P1.1; consequently its coordinate $s$ is nonzero.
Set $t=3125d/60$.  Its full row is
$\beta=s b+t r_0\Gamma_W$.  The constant bundle maps
\[
 C=\begin{pmatrix}1&-t r_0\\0&sI_5\end{pmatrix},\qquad
 C^{-1}=\begin{pmatrix}1&(t/s)r_0\\0&s^{-1}I_5\end{pmatrix}
\]
are holomorphic in the stated root frames and fix the invariant
section $e$.  Direct multiplication gives
\[
 C^{-1}\Gamma_6 C+C^{-1}dC
   =\begin{pmatrix}0&\beta\\0&\Gamma_W\end{pmatrix}.
\]
This proves the required equivalence of the complete flat bundles
with their fixed invariant line.  Evaluation at the marked basepoint
gives a common intertwiner for both specified meridians.  Thus its
existence follows from the exact connection maps.  The calculation
of the extension quotient and contraction, and the scalar
simultaneous centralizer of the supplied matrices, is also reproduced
by \texttt{audit\_sign/code/V\_P115\_extension\_independent\_06.py},
with exact output in
\texttt{audit\_sign/V\_P115\_extension\_independent\_06.json}.'''
assert text.count(old)==1
patch=[dict(label='night:P1.15',location='proof step3 full upper-extension equivalence',old_text=old,new_text=new,expected_count=1,reason='State the actual holomorphic gauge and reciprocal map fixing e, correcting nonconstant to constant multiples; makes the common normalized intertwiner existence explicit without numerical residuals.')]
(A/'V_P115_receiving_guard_06.json').write_text(json.dumps(patch,indent=2)+'\n')
md=r'''# P1.15: computed extension quotient and receiving comparison

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
'''
(A/'V_P115_receiving_comparison_06.md').write_text(md)
(A/'V_P115_proposed_assessment_06.json').write_text(json.dumps({'night:P1.15':{
 'confidence_state':'High at full upper-extension, contraction and normalized common-intertwiner scope',
 'confidence_line':'A frozen isolated-statement derivation from the exact root frames gives H1(W*)=0, the complete four-parameter upper row, its square-zero-residue constraints and one-dimensional gauge quotient. Fresh exact rational computation gives class C+4D/5, targetclass1, the explicit holomorphic fixed-line block isomorphism and inverse, contraction625pi*i/128, and scalar-only simultaneous centralizer. All four receiving proof steps were then read; steps3-4 and the normalizedX interface agree exactly. Steps1-2 remain the named supplied quotient/GM inputs in this new route.',
 'independent_routes':['Fresh root-frame divisor bounds and actual global Hom/cohomology classification, frozen before further proof access','New exact rational40-assertion residue, gauge, contraction and simultaneous-centralizer program with no prior checker import','Complete subsequent four-step receiving proof read, with scope of independent derivation limited to upper extension and normalization','Same GPT-6 Astra model family throughout; prior build12 contact-sheet visual exposure explicitly retained'],
 'remaining_risk':'No mathematical gate remains in the checked upper-extension/common-intertwiner argument. The existing quotient Gauss-Manin identification and later numerical period certificates retain their separate evidence. Final new source-layout status belongs to parent/corrections owners.',
 'format_check':'One precise wording repair and an explicit isomorphism/inverse proposed in V_P115_receiving_guard_06.json. No shared body changed and no current PDF layout claim.'}},indent=2)+'\n')
p=A/'CHECK_EVENTS_additions.tsv'
with p.open(newline='') as f:r=csv.DictReader(f,delimiter='\t');fields=r.fieldnames;ev=list(r)
who='GPT-6 Astra (OpenAI), ChatGPT Pro mode, reasoning effort inherited (not separately exposed), S6_SERIES_GRIND/sign_theorem_audit'
news=[('targeted proof check','Frozen statement-input derivation of the complete root-regular upper-extension row space, H1(W*) vanishing, actual global splitting gauge and one-dimensional nonzero extension class. Exact prior build12 V contact-sheet exposure is recorded; no complete-blind claim. The supplied quotient connection/GM identification remains named input.','S6_SERIES_GRIND_sign_VP115_frozen_upper_derivation'),('computation or formal certificate','Fresh SymPy exact rational40-check program imports no earlier checker: solves rR=0, identifies classC+4D/5 and targetclass1, full rank3 square-zero residue, actual kernel(-4096/1171875,64/1875,1), contraction625/192 and factor625pi*i/128, common invariantlineCe0, no dualinvariants and scalar-only centralizer. Explicit fixed-line bundle map and reciprocal give common-monodromy intertwiner existence, independent of numerical residuals.','S6_SERIES_GRIND_sign_VP115_upper_exact_40'),('used and rechecked in this run','After the frozen derivation and computation, read all four P1.15 proof steps and the normalizedX/splitting paragraph. Step3 full extension basis/gauge and step4 contraction agree; explicit fixed-line block isomorphism and inverse supplied. Steps1-2 quotient/GM reduction retain their supplied scope. Proposed correction of nonconstant splitting-change wording to constant multiples. Same model family; no new current PDF layout claim.','S6_SERIES_GRIND_sign_VP115_receiving_comparison')]
ids={x['event_id'] for x in ev}
for typ,outcome,eid in news:
 if eid not in ids:ev.append(dict(statement_id='night:P1.15',date='2026-11-19',who=who,type=typ,outcome=outcome,event_id=eid,phase='qualified isolated-statement derivation and receiving comparison'))
with p.open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(ev)
p=A/'row_assessments.json';d=json.loads(p.read_text());d['night:P3K.36']['remaining_risk']='The fresh sign-branch check establishes the exact0-versus26 arithmetic and full LR covering comparison. Whole geometric counterexample confidence retains the actual supplied IV K74/K105 fan/cap proofs and their historical evidence; neither this branch nor corrections claims a new complete K74/K105 geometric reading in this run.';p.write_text(json.dumps(d,indent=2)+'\n')
p=A/'K111_current_certificate_manifest.json';d=json.loads(p.read_text());d['estimated_zlib6_bytes']=d['total_zlib6_bytes'];p.write_text(json.dumps(d,indent=2)+'\n')
print(json.dumps({'events':len(ev),'receiving_proof_sha256':sha,'guard':'V_P115_receiving_guard_06.json','comparison':'V_P115_receiving_comparison_06.md'},indent=2))
