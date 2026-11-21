"""Guarded CM applications and height presentation, following batches A/B."""
from pathlib import Path
from decimal import Decimal,localcontext
import re,json,hashlib,datetime
B=Path(__file__).parent
base=B/'S6_SERIES_PUBLISH_I_editorial_batch_b_preview.tex'
original=base.read_text();s=original;guards=[];removed=[]
def patch(old,new,reason,ids=()):
 global s
 assert s.count(old)==1,(reason,s.count(old),old[:100])
 guards.append(dict(id=f'IA-C-{len(guards)+1:02}',old=old,new=new,
   expected_count=1,reason=reason,statement_ids=list(ids)))
 s=s.replace(old,new,1)
def preserve(name,old,reason):
 removed.append(dict(name=name,reason=reason,original=old,sha256=hashlib.sha256(old.encode()).hexdigest()))
def full_block(label,proof=True):
 i=s.index(r'\label{'+label+'}')
 a,env=max((s.rfind(r'\begin{'+e+'}',0,i),e)for e in ['proposition','theorem','lemma','cited','remark','corollary'])
 z=s.index(r'\end{'+env+'}',i)+len(r'\end{'+env+'}')
 if proof:
  p=s.find(r'\begin{proof}',z);n=re.search(r'\\begin\{(?:proposition|theorem|lemma|cited|remark|corollary)\}',s[z:])
  if p>=0 and(not n or p<z+n.start()):z=s.index(r'\end{proof}',p)+len(r'\end{proof}')
 return s[a:z]

# Restore the exact known-input application from the attached compendium.
old=r'''The expanded source derivation is retained in the proof compendium, Paper~I, label \nolinkurl{ari:C.5.1}.




This applies \citet[Theorem~4.15]{BourdonClarkStankewicz2017} and \citet[Theorem~20.12 and Corollary~20.13]{Sutherland2023CM}; the exact finite enumeration is retained. A complete re-derivation is given in \CompendiumRef{I}{app:rederive:ari-C.5.1}.'''
new=r'''\begin{proof}
Theorem~4.15(a) of
\cite[arXiv v3, p.~23]{BourdonClarkStankewicz2017} applies to an
elliptic curve with CM by any imaginary quadratic order over
$F=\mathbb Q(j(E))$. Its torsion group is one of
$0,\mathbb Z/2,\mathbb Z/3,\mathbb Z/4,\mathbb Z/6,(\mathbb Z/2)^2$.
Here $F=\mathbb Q(t)$ because $j=1728t$, and the actual equation
and section of \cref{I:def:theta-height} are defined over $F$.
On the smooth base, $\psi_2(P)$ and $\psi_3(P)$ are nonzero.
Thus only orders four and six remain.

The order-four value has $j=55296/5$. The order-six values have
irreducible monic polynomial
\[
 X^2-\frac{10395648}{11}X+\frac{24461180928}{11}.
\]
None is an algebraic integer. The integrality of singular moduli
for every imaginary quadratic order
\cite[Theorem~20.12 and Corollary~20.13, Lecture~20, p.~6]{Sutherland2023CM}
therefore excludes CM in all these cases.

At zero, the changes $t=s^3$, $x=s^4X$, $y=s^6Y$ give
\[
 Y^2=X^3-\tfrac34s(s^3-1)X+\tfrac14(s^3-1)^2,\qquad
 P_s=(0,(s^3-1)/2).
\]
The central equation is $Y^2=X^3+1/4$, and the limiting point
$(0,-1/2)$ has order three by its horizontal tangent.
At one, $t=1+s^4$, $x=s^2X$, $y=s^3Y$ give
\[
 Y^2=X^3-\tfrac34(1+s^4)^3X+
            \tfrac14(1+s^4)^4s^2,\qquad
 P_s=(0,(1+s^4)^2s/2).
\]
The central equation is $Y^2=X^3-3X/4$, and $(0,0)$ has
exact order two. Both central discriminants are nonzero.
Their CM orders are $\mathbb Z[\rho]$ and $\mathbb Z[i]$,
and their norm values are those of \cref{ari:C.1.2}.
\end{proof}'''
patch(old,new,'Restore the finite CM-torsion application with verified primary locators and exact boundary model maps.',('ari:C.5.1',))

# The arithmetic model and height conventions were defined once by parent.
old=r'''We use the equation
\[
 E_t:Y^2=X^3-\frac34t^3(t-1)X+\frac14t^4(t-1)^2,
 \qquad P_t=(0,t^2(t-1)/2).
\]
Its discriminant is $27t^8(t-1)^3$. Our canonical height is
$\widehat h_O(P)=\frac12\lim_{n\to\infty}n^{-2}h(x(nP))$.
In particular the bilinear Mordell--Weil self-pairing used in the
supplied surface calculation is $2\widehat h_O$.
For a finite place $v$ above the rational prime $p$, we normalize
$|p|_v=p^{-1}$ and set $n_v=[K_v:\Q_p]$. At an archimedean
place $n_v$ is one or two, according as the place is real or complex.'''
new=r'''We use the arithmetic equation, invariant differential, place weights,
and height normalization of \cref{I:def:theta-height}.'''
patch(old,new,'Use the established common conventions once.')
patch(r'''calculation in Statement \ref{ari:C.7.1}.''',
      r'''normalization in \cref{ari:C.4.1}.''',
      'Remove forward dependence of the global-height calculation.',('ari:C.6.1',))
patch(r'''\citet[Section 2.1]{demarco2017}; their duplication law includes''',
      r'''\citet[Section~2.1, arXiv v2, pp.~5--6]{demarco2017}; their duplication law includes''',
      'Use the actually read local-height locator.',('ari:C.6.1',))
old=r'''Under a coordinate scaling the changes in the sigma or formal
parameter term and in $\frac1{12}\log|\Delta|_v$ cancel.'''
new=r'''For the homothety
$(x,y,\Delta,\psi_n)\mapsto
(c^{-2}x,c^{-3}y,c^{-12}\Delta,c^{1-n^2}\psi_n)$,
the change in the two logarithmic terms of
\eqref{ari:eq:ch-local-mult} is
$-(1-n^2)\log|c|_v-(n^2-1)\log|c|_v=0$.
The pole normalization is transported by the same formal-parameter map.'''
patch(old,new,'Replace an implicit normalization assertion by its exact morphism and cancellation.',('ari:C.6.1',))

old=r'''The sign of $P$, which is immaterial to all these heights,
is chosen by the recorded change of variables.'''
new=r'''For row $i$, put $t_i=j_i/1728$ and
\[
 u_i=-\frac{3t_i(2y_{P,i}+a_{3,i})}{4a_{4,i}}.
\]
The exact pointed isomorphism to the arithmetic equation is
\[
 X=u_i^2x,\qquad Y=u_i^3(y+a_{3,i}/2).
\]
It sends the displayed point to $P_{t_i}$ and pulls back
$dX/(2Y)$ to $u_i^{-1}dx/(2y+a_{3,i})$.'''
patch(old,new,'Give the exact rational model/differential map for all eleven rows; independently recomputed after reading.',('ari:C.6.3',))
old=r'''We substitute the eleven exact values $t=j/1728$, and perform
the integral minimal-model transformations and Tate reduction
algorithm. The transformations and resulting invariants are
printed in \path{code/C_cm_models.out}; the exact valuation
computations are in \path{code/C_cm_local_heights.out}.
For each bad prime the program computes $mP$ by the rational
group law, tests the two partial derivatives of the minimal
cubic, and evaluates $\psi_m$ by its exact recursion. Formula'''
new=r'''Substitution verifies the displayed pointed isomorphisms and
$\Delta(E_t)=u_i^{12}\Delta(E_i)$.
Tate's reduction algorithm on each integral equation gives the
minimality, fibre types and component groups in the table.
For each bad prime, rational tangent addition computes $mP$,
the two partial derivatives of the minimal cubic test membership
in its nonsingular locus, and the division recurrence computes $\psi_m$.
Formula'''
patch(old,new,'Describe exact inputs, algorithms and outputs without file references.',('ari:C.6.3',))
old=r'''\item The independent analytic check uses the exact quadratic CM
period ratio, solves $\wp(\mu)=0$ by its convergent Fourier
series, and evaluates the theta product at 270-digit working
precision. The value of $j$ agrees with its prescribed integer
to absolute error less than $10^{-245}$. For every row the
direct value of $\log N$ agrees with
$\log A_t-\widehat h_O(P_t)$ to more than 245 decimal places.
These numerical comparisons test the exact normalization;
the algebraic local-height entries were already proved by
integer and rational arithmetic. The full precision values
are in \path{records/C_cm_theta_pslq.json}.'''
preserve('C6_3_numerical_crosscheck',old,'Independent analytic agreement retained in records.')
patch(old,'','Keep the exact local-height proof once; archive independent numerical corroboration.',('ari:C.6.3',))

# Compact the display without changing its certified meaning.
a=s.index(r'\noindent The next table prints 52 significant digits.')
z=s.index(r'\begin{proposition}[the maximum as a height inequality]',a)
oldtable=s[a:z]
preserve('C6_3_full_precision_table',oldtable,'Full precision output table; compact display keeps useful numerical scale.')
heights=re.findall(r'\\widehat h_O=([-0-9.]+)',oldtable)
norms=re.findall(r'\\log N=([-0-9.]+)',oldtable)
assert len(heights)==len(norms)==11
with localcontext()as ctx:
 ctx.prec=80
 data=[(str(Decimal(h).quantize(Decimal('.00000001'))),str(Decimal(n).quantize(Decimal('.00000001'))))for h,n in zip(heights,norms)]
newtable=r'''\begin{remark}[Numerical sizes of the CM heights]
\hypertarget{tag-IA02}{}\label{I:CM-height-sizes}
The following approximations have absolute error less than $10^{-8}$,
by the enclosures in \cref{ari:C.6.5}.
\[
\begin{array}{r|rr}
i&\widehat h_O(P_i)&\log N(P_i)\\\hline
'''+''.join(f'{i}&{h}&{n}'+r'\\'+'\n'for i,(h,n)in enumerate(data,1))+r'''\end{array}
\]
\end{remark}

'''
patch(oldtable,newtable,'Replace repeated 52-digit output with a compact certified display; retain every original digit in records.',('ari:C.6.3','ari:C.6.5'))

# The height-variation application is complete before its repeated source audit.
oldstart=r'''\item We spell out the comparison with the opened primary author sources.'''
a=s.index(oldstart);z=s.index(r'\end{enumerate}',a)
old=s[a:z]
preserve('C6_4_parallel_height_variation_sources',old,'Parallel source-hypothesis audit; operative DeMarco--Mavraki application retained.')
new=r'''\item The same generic coefficient appears in
\cite[Theorem~4.1 and the following remark, pp.~183--184]{callSilverman1993}:
for $T=\mathbb P^1$ and $[2]^*(O)\sim4(O)$, the specialization
ratio tends to $1/12$. The bounded remainder used here is the
adelic-height conclusion applied in the preceding step.
'''
patch(old,new,'Consolidate repeated variation-theorem application while preserving the precise comparison.',('ari:C.6.4',))

old=r'''For every one of the eleven rational CM parameters in \ref{ari:C.6.3},
the files \path{records/C_cm_height_arb.json} and
\path{code/C_cm_height_arb.out} give certified enclosures of
$\log N(P)$ and $\widehat h_O(P)$ of radius less than
$10^{-236}$. These enclosures use no floating-point height
value as a proof step.'''
new=r'''For each of the eleven rational CM parameters in \cref{ari:C.6.3},
the Fourier and product algorithms below give rational interval
enclosures of $\log N(P)$ and $\widehat h_O(P)$ of radius less
than $10^{-236}$.'''
patch(old,new,'State the mathematical enclosure result and its method.',('ari:C.6.5',))
patch(r'''Exact class
polynomials were also computed independently in
\path{code/C_cm_class_polynomials.gp} and its output.''','',
'Remove duplicate computational corroboration; class-number enumeration and integrality are retained.',('ari:C.6.5',))
patch(r'''Each previously computed decimal supplies only a rational
candidate centre $y_0$.''',r'''A numerical zero approximation selects a rational centre $y_0$.''',
'State the role of approximation without file history.',('ari:C.6.5',))
patch(r'''The code records all twenty-two strict signs.''',
r'''These strict endpoint signs are evaluated with outward error bounds.''',
'Describe the mathematical certificate rather than a check count.',('ari:C.6.5',))
patch(r'''All calculations use Arb enclosures at $1152$ bits; the
radius comparisons and endpoint signs are exact interval
comparisons.''',
r'''The finite sums, elementary functions and tails are evaluated by
outward interval arithmetic. The radius and sign comparisons are strict.''',
'Remove library/precision options while retaining enclosure semantics.',('ari:C.6.5',))
patch(r'''Thus $E_4^3/\Delta_0$ is rigorously enclosed. The complete
certificate is \path{code/C_cm_height_arb.py}, with its
output and rational bracket centres retained.''',
r'''Thus $E_4^3/\Delta_0$ is enclosed by the stated finite sums and tails.''',
'Keep the complete mathematical singular-modulus enclosure.',('ari:C.6.5',))

# Restore the operative Miller application and its exact coarse-height algorithm.
old=r'''The expanded source derivation is retained in the proof compendium, Paper~I, label \nolinkurl{ari:C.6.R4}.




The three exact cases specialize \citet[Definition~1.1, Theorem~1.2 and Table~9]{miller2011}. The complete application is retained in the proof compendium, Paper~I, label \nolinkurl{app:rederive:ari-C.6.R4}.'''
new=r'''\begin{proof}
Miller's theorem
\cite[Definition~1.1 and Theorem~1.2, arXiv v3, p.~2;
Table~9, p.~23]{miller2011}
applies to analytic rank at most one and conductor less than $5000$,
outside the listed exceptional curve--prime pairs.
The present conductors are $3136,3136,361$; none occurs in
that exception table, and their analytic ranks are one by
\cref{ari:C.6.R2}. The theorem applies to every curve in each
isogeny class.

For these three rows,
$2\prod_pc_p/\#E(\mathbb Q)_{\rm tors}^2=4$, and
\cref{ari:C.6.R1} proves primitivity. Therefore
$L'(E_i,1)/(4\Omega_i\widehat h_O(P_i))$ is the positive integer
$\#\operatorname{Sha}(E_i/\mathbb Q)$.
To isolate it, complete the square and write the duplication map
as relatively prime integral quartics $[F(X,Z):G(X,Z)]$.
The extended Euclidean algorithm gives integer homogeneous cubics
$A_0,B_0,A_1,B_1$ and $D\ne0$ with
\[
 A_0F+B_0G=DZ^7,\qquad A_1F+B_1G=DX^7.
\]
Let $C$ dominate the coefficient one-norms of $F,G$ and both
pairs $(A_j,B_j)$. For coprime $a,b$, the two identities bound
the common divisor of $F(a,b),G(a,b)$ by $|D|$ and give
\[
 |h(x(2Q))-4h(x(Q))|\le\log C.
\]
Telescoping yields
\[
 \left|\widehat h_O(P)-
       \frac{h(x(2^6P))}{2\cdot4^6}\right|
       \le\frac{\log C}{6\cdot4^6}.
\]
The exact constants for rows $3,5,7$ are
$26610617537591808$, $188716953600$, and $285931133$.
Six rational doublings and outward logarithm enclosures, together
with the derivative tails of \cref{ari:C.6.R2}, give respective
quotient intervals $1\pm0.003$, $1\pm0.003$, and $1\pm0.009$.
Each contains only the integer one.
Finally $A_t=1$ in row seven by \cref{ari:C.6.3}, giving the
displayed formula for $N(P)$.
\end{proof}'''
patch(old,new,'Restore the exact known-theorem application, height algorithm and integer separation; verified primary locators.',('ari:C.6.R4',))

# Title cleanup contains no mathematical claim or new proof.
for old,new in [
('Supplement: ranks, saturation, and central derivatives','Ranks, saturation, and central derivatives'),
('Supplement: exact leading factors from a genus-character denominator bound','Exact leading factors from a genus-character denominator bound'),
('Supplement: the three specified smooth torsion fibres','The three smooth torsion fibres'),
(r'ARI \ref{ari:C.6.R1}; Proved by descent and full saturation','Mordell--Weil ranks and primitive sections'),
(r'ARI \ref{ari:C.6.R2}; Proved: central derivatives with explicit tails','Central derivatives with explicit tails'),
(r'ARI \ref{ari:C.6.R3}; Proved: the consequences of Gross--Zagier and Kolyvagin','Rational leading factors and finite Tate--Shafarevich groups'),
(r'ARI \ref{ari:C.6.R4}; Known input: three exact leading factors','Three exact leading factors'),
(r'ARI \ref{ari:C.6.R5}; Proved: all remaining rational leading factors','The remaining rational leading factors'),
('T1; Proved, with exact local and descent computations','The rational order-four fibre'),
('T2; Proved, with exact number-field local arithmetic','The conjugate order-six fibres'),
('Refuted sign and normalization, with the corrected current identity proved','The positive Betti measure and its current'),
('the correctly normalized equidistribution','Torsion equidistribution')]:
 patch(old,new,'Use a mathematical title without status or historical labels.')

out=dict(source_path=str(base),source_sha256=hashlib.sha256(original.encode()).hexdigest(),
 generated_at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
 requires_batch='S6_SERIES_PUBLISH_I_editorial_batch_b_guards.json',guards=guards)
(B/'S6_SERIES_PUBLISH_I_editorial_batch_c_guards.json').write_text(json.dumps(out,indent=2)+'\n')
(B/'S6_SERIES_PUBLISH_I_editorial_batch_c_removed.json').write_text(json.dumps(removed,indent=2)+'\n')
(B/'S6_SERIES_PUBLISH_I_editorial_batch_c_preview.tex').write_text(s)
print(json.dumps({'guards':len(guards),'removed_blocks':len(removed),'preview_sha256':hashlib.sha256(s.encode()).hexdigest()},indent=2))
