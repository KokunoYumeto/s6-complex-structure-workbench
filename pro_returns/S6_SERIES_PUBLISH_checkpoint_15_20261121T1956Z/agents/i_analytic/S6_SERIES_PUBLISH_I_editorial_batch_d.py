"""Guarded mathematical presentation of local conventions and height algorithms."""
from pathlib import Path
from decimal import Decimal,localcontext
import re,json,hashlib,datetime
B=Path(__file__).parent
base=B/'S6_SERIES_PUBLISH_I_editorial_batch_c_preview.tex'
original=base.read_text();s=original;guards=[];removed=[]
def patch(old,new,reason,ids=()):
 global s
 assert s.count(old)==1,(reason,s.count(old),old[:150])
 guards.append(dict(id=f'IA-D-{len(guards)+1:02}',old=old,new=new,
 expected_count=1,reason=reason,statement_ids=list(ids)))
 s=s.replace(old,new,1)
def archive(name,text,why):
 removed.append(dict(name=name,reason=why,original=text,
 sha256=hashlib.sha256(text.encode()).hexdigest()))

# Place the common local constants and identities before their first use.
a=s.index(r'\subsection{The square and equianharmonic points}')
b=s.index(r'\begin{proposition}[fourth order at the maximum]',a)
old=s[a:b]
setup=old.split('\n',1)[1].strip()
patch(old,r'\subsection{The square and equianharmonic points}'+'\n\n',
      'Move the local setup before the differential identities.')
new=r'''\section{Local expansions of the norm}

\begin{definition}[Local expansion constants and differential conventions]
\hypertarget{tag-IA03}{}\label{I:local-expansion-conventions}
'''+setup+r'''
\end{definition}
'''
patch(r'\section{Local expansions of the norm}',new,
      'Number the common G, D-star, theta and modular-derivative setup before use.',
      ('ari:C.8.11','ari:C.3.1','ari:C.3.2'))

old=r'''We retain the order of the eleven rational CM values in the stated conventions, and
write $E_i$ for the global minimal models recorded in the preceding
tables. The real period in this subsection is
\[
 \Omega_i=\int_{E_i(\R)}|\omega_i|,
\]
including both connected components when $E_i(\R)$ is disconnected.
The canonical height $\widehat h$ is relative to $(O)$; PARI's
\texttt{ellheight} and the regulator convention used in the BSD formula
are relative to $2(O)$, and hence equal $2\widehat h$ in rank one.
This factor of two is essential in every comparison below.'''
new=r'''Write $E_i$ for the eleven minimal models in \cref{ari:C.6.3}.
The full real period and the height relative to $(O)$ are those of
\cref{I:def:theta-height}. Pullback of the normalized Poincar\'e bundle
along the diagonal gives
$[2]^*\mathcal O(O)\otimes\mathcal O(O)^{-2}\simeq\mathcal O(2O)$.
Consequently the diagonal N\'eron--Tate pairing used in the
leading-term formula is $2\widehat h_O$.'''
patch(old,new,'Use the common period convention and exhibit the factor-two bundle morphism.')

a=s.index(r'\item Exact $2$-descent in PARI/GP')
b=s.index(r'\item For clarity,',a)
old=s[a:b];archive('R1_descent_implementation',old,'Implementation and independent-run narration.')
new=r'''\item Exact $2$-descent gives matching lower and upper rank bounds
for all eleven equations. For each of the nine rank-one sections,
height bounds restrict its possible index to a finite interval;
reduction maps at good primes test divisibility by every prime in
that interval and every prime dividing a component-group order.
These saturation tests give index one in all nine cases.

'''
patch(old,new,'State the exact descent and finite saturation algorithm.',('ari:C.6.R1',))
patch(r'''\item For clarity, the rounded-down bounds''',
      r'''\item The integer parts of the bounds''',
      'Give the finite index bounds directly.',('ari:C.6.R1',))
old=r'''These data certify primitivity; merely finding $P$ in the output of
\texttt{ellrank} would not do so. The complete height-bound and
saturation transcripts are retained, including the independent
descent run that was stopped after its ninth completed curve.'''
patch(old,r'''The index bounds and full-rank reduction maps certify primitivity.''',
      'Remove execution history after the operative saturation certificate.',('ari:C.6.R1',))

# Keep a readable table; preserve the original digits in the check record.
a=s.index(r'The following are the values of $L')
b=s.index(r'\end{proposition}',a)
old=s[a:b];archive('R2_full_precision_statement',old,'All original numerical digits retained here.')
rows=re.findall(r'^(\d+)&\$([0-9.]+)(?:\\ldots)?\$',old,re.M)
assert len(rows)==11
with localcontext() as ctx:
 ctx.prec=90
 rows8=[(i,'0' if val=='0' else str(Decimal(val).quantize(Decimal('.00000001')))) for i,val in rows]
new=r'''The first derivative ratios are enclosed by the following values
with absolute error less than $10^{-8}$. The zeros in rows one
and eight are exact.
\[
\begin{array}{r|r}
i&L'(E_i,1)/\Omega_i\\\hline
'''+''.join(i+'&'+v+r'\\'+'\n' for i,v in rows8)+r'''\end{array}
\]
For the same full real periods,
\[
 L''(E_1,1)/\Omega_1=28.71408723\ldots,\qquad
 L''(E_8,1)/\Omega_8=78.03222042\ldots,
\]
again with absolute error less than $10^{-8}$.
The leading Taylor coefficients in these two rows are half
the second derivatives. The proof's error bounds also determine
the finer intervals recorded with the verification data.
'''
patch(old,new,'Compact the numerical display while retaining the original precision in records.',
      ('ari:C.6.R2',))
patch(r'''respectively. For the first ten curves we used
$M=\lceil180/c\rceil$, exact integer coefficients, and 1024-bit
MPFR arithmetic. For the rank-two kernel we used the convergent series''',
r'''respectively. For the first ten curves take
$M=\lceil180/c\rceil$ and compute the coefficients exactly.
For the second-derivative kernel use the convergent series''',
'Give the finite-sum prescription without package options.',('ari:C.6.R2',))
patch(r'''The 1024-bit arithmetic therefore leaves far more than 100 digits
after this cancellation. The largest bound in
\eqref{ari:eq:Cr-tails} was $3.46\cdot10^{-77}$. The source and complete
outputs are \path{code/Crank_coefficients.gp},
\path{code/Crank_derivatives.cpp}, and their corresponding outputs.''',
r'''Evaluating these finite sums with the rounding allowance below
controls this cancellation. The largest infinite-tail bound in
\eqref{ari:eq:Cr-tails} is $3.46\cdot10^{-77}$.''',
'Retain the cancellation and tail bounds, with implementation in the program table.',('ari:C.6.R2',))
patch(r'''\item For $i=11$, a full vector of $819$ million coefficients would be
unnecessarily large. We instead evaluated the CM theta series in
bounded-memory segments. The curve is the quadratic twist, by''',
r'''\item For $i=11$, generate the coefficients by the CM theta series.
The curve is the quadratic twist, by''',
'Describe the coefficient formula directly.',('ari:C.6.R2',))
old=r'''The first 10000 coefficients agree
exactly with PARI for both the untwisted and twisted curve. The same
code at $D=67,d=217$ reproduces the independent PARI derivative.'''
archive('R2_coefficient_crosscheck',old,'Independent coefficient and derivative comparison.')
patch(old,r'''The global identification of this coefficient formula is proved
by the finite modular-form comparison in \cref{ari:C.6.R5}.''',
'Link the proved coefficient identification; archive independent corroboration.',('ari:C.6.R2',))
patch(r'''The values of $E_1$ at consecutive block centres
are continued by the analogous Taylor expansion and refreshed
from a correctly rounded MPFR evaluation every 1024 blocks.''',
r'''The values of $E_1$ at consecutive block centres
are continued by the analogous Taylor expansion; after at most
1024 such continuations, enclose $E_1$ directly again.''',
'State the error-controlled kernel continuation algorithm.',('ari:C.6.R2',))
patch(r'''All moments are integers, not floating-point sums.''',
      r'''All moments are exact integers.''','Concise exact-arithmetic statement.',('ari:C.6.R2',))
a=s.index(r'\item The 384-bit run')
b=s.index(r'\item The real periods are enclosed',a)
old=s[a:b];archive('R2_parallel_runs',old,'Two independent implementations and full decimal output.')
new=r'''\item Taking $R=96$ and cutoff $cM\geq190$ uses
$915818441$ coefficients and gives an infinite tail less than
$3.10\cdot10^{-78}$. In the recurrences,
$|e_k|\leq1$, $|g_k|\leq1$, and $|\phi_k|<20$.
There are fewer than $5\cdot10^6$ blocks and at most 1024
consecutive continuations. Bounding each normalized moment by
$\sum|a_n|(R/n_0)^k$ controls accumulated rounding without
assuming cancellation. The elementary evaluations are carried
out to make that contribution less than $10^{-90}$; adding the
Taylor remainder gives the derivative allowance used below.

'''
patch(old,new,'Retain all error-budget inputs and remove repeated run/output narration.',
      ('ari:C.6.R2',))
patch(r'''\item The real periods are enclosed from the exact minimal invariants,
independently of the saved decimal period values.''',
r'''\item Enclose the real periods from the exact minimal invariants.''',
'Describe the period calculation directly.',('ari:C.6.R2',))
patch(r'''The current program \path{code/I/certify_all_period_ratios.py}
performs these operations with 768-bit Arb intervals and verifies
every displayed period and derivative ratio.  For the first ten
derivatives it enlarges the explicit tail by one percent and adds''',
r'''Evaluate these operations with outward intervals.
For the first ten derivatives enlarge the explicit tail by one
percent and add''',
'Give the interval prescription and retain its error margins.',('ari:C.6.R2',))
patch(r'''and the 1024-bit accumulated rounding and
$10^{-140}$ kernel remainders are below this allowance.''',
r'''and elementary precision chosen to bound accumulated rounding,
together with the $10^{-140}$ kernel remainders, stays below
this allowance.''',
'State the arithmetic requirement as an error bound.',('ari:C.6.R2',))
patch(r'''For the last derivative it adds $1.1\cdot10^{-75}$, covering the
proved block Taylor and rounding bounds above.  Division by the
strictly positive period intervals preserves all fifty displayed
digits.  The resulting intervals and exact invariants are in
\path{code/I/records/all_period_ratios_arb.json}.''',
r'''For the last derivative add $1.1\cdot10^{-75}$, covering the
block Taylor and rounding bounds above. Division by the strictly
positive period intervals gives the stated enclosures.''',
'Finish the mathematical enclosure rather than cite output files.',('ari:C.6.R2',))
patch(r'''Their Theorem I.7.3, in the opened original
preprint \citep{CrGrossZagier1986},''',
r'''Their Theorem~I.7.3 \citep{CrGrossZagier1986}''',
'Remove source-review history from the operative application.',('ari:C.6.R3',))

a=s.index(r'\paragraph{What the numerical BSD comparison')
b=s.index(r'\begin{cited}[Three exact leading factors]',a)
old=s[a:b];archive('BSD_numerical_comparison',old,'Initial numerical prediction superseded by exact factor theorems.')
new=r'''\begin{remark}[The analytic leading quotients]
\hypertarget{tag-IA04}{}\label{I:analytic-leading-quotients}
For the nine rank-one rows, define
\[
 Q_i=\frac{L'(E_i,1)/\Omega_i}
 {2\widehat h_O(P_i)\prod_pc_p/\#E_i(\mathbb Q)_{\rm tors}^{\,2}}.
\]
The exact factors in \cref{ari:C.6.R4,ari:C.6.R5} give $Q_i=1$
for $i=2,3,4,5,6,7,9,10$ and $Q_{11}=9$.
In rows $3,5,7$, \cref{ari:C.6.R4} also computes
$\#\operatorname{Sha}(E_i/\mathbb Q)=1$.
The remaining Tate--Shafarevich orders are discussed in
\cref{ari:C.7.5}.
\end{remark}

'''
patch(old,new,'Replace numerical prediction history with the exact conclusions and explicit open scope.')

a=s.index(r'\paragraph{The scope of Rubin')
b=s.index(r'\subsection{Exact leading factors',a)
old=s[a:b]
new=old.replace(r"\paragraph{The scope of Rubin's theorem.}",
r'''\begin{remark}[Ordinary CM leading-term theorems]
\hypertarget{tag-IA05}{}\label{I:ordinary-CM-scope}''')
new=new.replace('One precise opened formulation of Rubin','One formulation of Rubin')
new=new.replace(r'''Its input is analytic rank one, already verified here.
It is a $p$-adic identity; it does not identify the real exponential
$\exp\widehat h(P)$ as algebraic.''',
r'''The analytic-rank-one input holds by \cref{ari:C.6.R2}.
The formal logarithm, Katz value and period in this formula
are the $p$-adic quantities specified in that theorem.''')
new=new.replace(r'''and we
do not claim that this particular formulation proves its full
leading-term formula. The asserted application retains the exact hypotheses of
\citet[Theorem~A]{CrCastella2025}.''',
r'''so this formulation does not apply directly to that case.''')
new=new.replace(r'''In particular these ordinary-prime statements do not prove that
the $3$-primary part of $\operatorname{Sha}$ has order $9$ for the
last curve: $3$ is inert in $\Q(\sqrt{-163})$ and also excluded
from the stated $p>3$ hypotheses. \ref{ari:C.6.R5} proves the corresponding
analytic quotient to be exactly $9$ by a separate denominator
argument. The identification with the actual Tate--Shafarevich
group remains a separate arithmetic question in that row.''',
r'''For the last curve, $3$ is inert in $\mathbb Q(\sqrt{-163})$
and is excluded by the stated $p>3$ hypotheses.
The exact analytic quotient $Q_{11}=9$ is proved in
\cref{ari:C.6.R5}; the remaining group-order question is
recorded in \cref{ari:C.7.5}.''')
new=new.rstrip()+r'''
\end{remark}

'''
patch(old,new,'Number the exact hypothesis comparison and link the actual unresolved question.')

# The genus-trace argument is retained; only duplicate period calculations
# and implementation narration are consolidated.
patch(r'''We retain the full real period $\Omega_i$ and the absolute canonical
height $\widehat h_O$ of the preceding subsection. The argument below
uses the Gross--Zagier formula to bound a rational denominator; it does
not assume the leading-term Birch--Swinnerton-Dyer formula.''',
r'''Use the full real period and the absolute height of
\cref{I:def:theta-height}. The Gross--Zagier formula gives the
rational denominator bound used below.''',
'Introduce the actual denominator argument directly.')
patch(r'''\item We give the arithmetic denominator bound first and then the interval
certificate that isolates the listed rational numbers.

''','',
'Remove a plan item from the proof.',('ari:C.6.R5',))
patch(r'''For the first five bases this
is independently returned by PARI's unconditional modular-symbol
algorithm.''',
r'''For the first five bases this follows from the exact
modular-symbol algorithm.''',
'State the operative modular-symbol computation.',('ari:C.6.R5',))
a=s.index(r'The first five completed computations are in')
b=s.index(r'\item In every row',a)
old=s[a:b];archive('R5_metadata_implementation',old,'Program locations and implementation comparison.')
new=r'''Exact rational transformations check both $c_4,c_6$ scaling
identities for $b=d,dD$. Tate's algorithm and rational torsion
computations give both conductor identities and torsion orders;
quadratic residue symbols check the splitting conditions.

'''
patch(old,new,'State the exact finite metadata algorithms.',('ari:C.6.R5',))
patch(r'''This factor comes from the Poincar\'e pairing and the base field,
independently of any numerical height routine.''',
r'''This is the factor from the Poincar\'e pairing and the base field.''',
'Keep the exact height morphism without implementation comparison.',('ari:C.6.R5',))
patch(r'''used by the coefficient stream:''',r'''for the coefficients:''',
      'Use mathematical terminology.',('ari:C.6.R5',))
patch(r'''For all four bases, exact PARI elliptic-curve coefficients equal
$b_n$ for $1\leq n\leq10000$.''',
r'''For all four bases, exact point counts at good primes, the bad-prime
Euler factors, and multiplicativity give elliptic-curve coefficients
equal to $b_n$ for $1\leq n\leq10000$.''',
'Specify the exact comparison underlying the Sturm bound.',('ari:C.6.R5',))
patch(r'''The exact
metadata transcript prints the four bounds and their comparisons.''','',
'Remove output narration after the complete coefficient identification.',('ari:C.6.R5',))
patch(r'''The exact coefficients in the smaller cases
come from retained PARI files.''',
r'''Generate the coefficients in the smaller cases by point counts
and the Euler-product recurrence.''',
'State the coefficient algorithm.',('ari:C.6.R5',))
patch(r'''No precision conclusion depends on the nominal
cutoff.''',
r'''The actual integer $M$ enters every tail bound.''',
'State the operative cutoff explicitly.',('ari:C.6.R5',))
patch(r'''\item Here are the finite-sum and rounding certificates implemented in
\path{code/B_C6_central_stream.cpp}. All intervals use 256-bit
MPFR with outward rounding at every operation. In a block centred
at $b$ with radius $R=128$, set''',
r'''\item Evaluate the finite sums with outward interval arithmetic.
In a block centred at $b$ with radius $R=128$, set''',
'Retain the exact block algorithm and interval semantics.',('ari:C.6.R5',))
patch(r'''The program evaluates both with the downward bound
for $c$ and upward bounds for the remaining positive expressions.
It finally adds the block remainders, interval arithmetic errors,
and infinite tail.''',
r'''Evaluate both tails with a lower bound for $c$ and upper bounds
for the remaining positive expressions, then add the block
remainders and elementary-evaluation errors.''',
'State the directed enclosure algorithm.',('ari:C.6.R5',))
patch(r'''All twelve completed interval outputs are
retained, as are the exact coefficient files.''','',
'Remove output inventory from the proof.',('ari:C.6.R5',))
a=s.index(r'\item \textbf{6. Periods, heights, and exact rational separation.}')
b=s.index(r'\item The final computation is',a)
old=s[a:b];archive('R5_duplicate_period_enclosure',old,'Same E4 tail and real-period transport already proved in R2.')
new=r'''\item \textbf{6. Periods, heights, and exact rational separation.}
Apply the real-period algorithm in \cref{ari:C.6.R2} separately
to each target and auxiliary minimal equation, using
$\tau=i\sqrt s$ for $i=2,4$ and
$\tau=(1+i\sqrt s)/2$ for $i=6,9,10,11$, where
$s=3,7,11,43,67,163$ respectively.
These parameters and their class-number-one identification are
proved in \cref{ari:C.6.5}. In both equations the exact
$c_4,c_6$ determine the same homothety rule
$\kappa=2\pi(E_4/c_4)^{1/4}$; the signs of $c_6$ and $\Delta$
select the real generator and number of components.
Thus the $E_4$ tail, positive $E_6$ bound and real-lattice
transport of \cref{ari:C.6.R2} give both full-period intervals.
Use the height intervals of \cref{ari:C.6.5}.

'''
patch(old,new,'Consolidate the identical E4-tail/period proof with an explicit target-and-twist transport.',
      ('ari:C.6.R2','ari:C.6.R5'))
patch(r'''\item The final computation is
\path{code/B_C6_exact_factors.py}. First, the intervals for''',
r'''\item First, the intervals for''',
'State the rational-separation operation.',('ari:C.6.R5',))
patch(r'''The enclosures
below are deliberately enlarged decimal summaries of the recorded
Arb intervals:''',
r'''Outward enlargement of the intervals gives the following rational
error bounds:''',
'Give the finite certificate as rational bounds.',('ari:C.6.R5',))
patch(r'''The JSON certificate records all input
intervals, exact invariants, rational values, and positive separation
margins. Its stdout concludes that all six remaining factors are
exactly certified. This completes the proof.''','',
'Remove file and success-message narration after the proof is complete.',('ari:C.6.R5',))

# Torsion examples: retain exact values and exact coordinate maps.
a=s.index(r'Numerically the two sides of the global height identity equal')
b=s.index(r'\end{proposition}',a)
old=s[a:b];archive('T1_decimal_values',old,'The exact norm and derivative formulas remain in the statement.')
new=r'''The central values satisfy
\[
 \frac{L(E,1)}{\Omega}=\frac18,\qquad
 \frac{L'(E,1)}{\Omega}
   =\frac{\gamma+\log(2\pi/\sqrt{40})}{8},
\]
where $\gamma$ is Euler's constant. In particular the analytic rank is zero.
'''
patch(old,new,'Replace decimal agreement by the exact modular-symbol and functional-equation formulas.',
      ('ari:C.6.T1',))
patch(r'''\item The change of variables from the displayed family is
$x=(24/5)^2X$, $y=(24/5)^3Y$.''',
r'''\item From the displayed minimal coordinates to the family coordinates
of \cref{I:def:theta-height}, the map is
$X=(24/5)^2x$, $Y=(24/5)^3y$.
It sends $(0,1)$ to $P_{32/5}$ and pulls the family differential
back to $(5/24)\,dx/(2y)$.''',
'Specify the direction and differential of the exact coordinate map.',('ari:C.6.T1',))
a=s.index(r'The exact descent output is')
b=s.index(r'\end{enumerate}',a)
old=s[a:b];archive('T1_computation_narration',old,'Exact results retained; output strings and independent comparison archived.')
new=r'''Exact $2$-descent gives rank zero, and the torsion calculation
gives $\mathbb Z/4\mathbb Z$ generated by $P$.
The plus modular symbol from $0$ to $\infty$ is $-1/4$
in the primitive real-period normalization. There are two real
components, so $L(E,1)/\Omega=1/8$ for the full real period.
Differentiating the completed functional equation at its central
point gives the displayed formula for $L'(E,1)/\Omega$.
'''
patch(old,new,'Retain the exact descent, modular-symbol and functional-equation argument.',('ari:C.6.T1',))
old=r'''The common value in the last line is
\[
 0.199824606066530878671828631497094108318475571161451431268214\ldots.
\]
'''
archive('T2_decimal_height',old,'Exact logarithm already displayed.')
patch(old,'','Remove a duplicate decimal evaluation of the exact logarithm.',('ari:C.6.T2',))
patch(r'''The natural Mordell--Weil group here is $E_\pm(K)$; the
notation $E_{t_\pm}(\Q)$ requested in the stated conventions does not
define an elliptic curve over $\Q$, since its $j$-invariant
is irrational. Over $K$, both curves have rank one and torsion
group $\Z/6\Z$.''',
r'''The two $j$-invariants are $1728t_\pm\in K\setminus\mathbb Q$.
An elliptic curve over $\mathbb Q$ has rational $j$, so these
fibres admit no model over $\mathbb Q$.
Over $K$, both curves have rank one and torsion group $\mathbb Z/6\mathbb Z$.''',
'Replace requested-notation history by the exact descent obstruction.',('ari:C.6.T2',))
patch(r'''\item For $t_-$ the change from the original family to this model
has scale $u=48(-64+37s)/11$, with translation parameters zero.''',
r'''\item For $t_-$, put $u=48(-64+37s)/11$.
The map from the displayed minimal model to the family equation is
$X=u^2x$, $Y=u^3y$, with differential
$dX/(2Y)=u^{-1}dx/(2y)$.''',
'Specify the exact number-field model map and its direction.',('ari:C.6.T2',))
a=s.index(r'The field arithmetic was certified by')
b=s.index(r'The torsion calculation',a)
old=s[a:b];archive('T2_descent_execution',old,'Package settings and compatibility history.')
new=r'''The covering equations and local tests use exact arithmetic in
$\mathbb Q(\sqrt3)$; every surviving class is represented by a point,
and every excluded class has a local obstruction at the stated primes.
'''
patch(old,new,'Keep the finite descent certificate and remove execution/compatibility history.',
      ('ari:C.6.T2',))
a=s.index(r'\paragraph{The corresponding number-field')
b=s.index(r'\subsection{Integral and Gaussian',a)
old=s[a:b];archive('T2_number_field_L_numerics',old,'Uncertified decimal derivative comparison retained as check data.')
new=r'''\begin{remark}[The number-field period convention]
\hypertarget{tag-IA06}{}\label{I:number-field-period}
For $K=\mathbb Q(\sqrt3)$, put
\[
 \Omega_{\mathrm{prod}}=
 \prod_{\sigma:K\hookrightarrow\mathbb R}
       \int_{E_\sigma(\mathbb R)}|\omega_\sigma|,
 \qquad
 \Omega_K=\frac{\Omega_{\mathrm{prod}}}{\sqrt{12}}.
\]
The two conjugate equations give the same Hasse--Weil $L$-function
over $K$. Its analytic conductor is $12^2\cdot396=57024$,
its gamma parameters are $(0,0,1,1)$, and its sign is $-1$.
The exact conversion of derivative ratios is
$L'(E/K,1)/\Omega_K=\sqrt{12}\,L'(E/K,1)/\Omega_{\mathrm{prod}}$.
\end{remark}

'''
patch(old,new,'Keep the unique number-field L-data and exact period morphism; archive decimal corroboration.')

old=r'''We take $dd^c=(i/\pi)\partial\bar\partial$, so that
$dd^c\log|w|=\delta_0$. For a local complex coordinate $w$,
$dA_w=(i/2)dw\wedge d\bar w$.'''
new=r'''\begin{definition}[The current convention]
\hypertarget{tag-IA07}{}\label{I:current-convention}
We take $dd^c=(i/\pi)\partial\bar\partial$, so that
$dd^c\log|w|=\delta_0$. For a local complex coordinate $w$,
$dA_w=(i/2)dw\wedge d\bar w$.
\end{definition}'''
patch(old,new,'Number the operative local current convention.')
patch(r'''Thus the proposed form $da\wedge db$ has the wrong sign.''',
r'''Reversing the wedge order gives $da\wedge db=-m_P$.''',
'Replace correction history by the exact sign identity.',('ari:C.8.9',))
patch(r'''Thus the probability limit requires the factor $12$.''',
r'''The factor $12$ normalizes the mass to one.''',
'State the normalization directly.',('ari:C.8.10',))
patch(r'''This division by the degree is essential: a measure
of mass $1/12$ cannot be a weak limit of probability measures.
The source's informal description of the pullback current
is interpreted with this normalization.''',
r'''The total mass is one because
$12\int_{\mathbb P^1}m_P=1$.''',
'Keep the exact mass calculation without a source-review aside.',('ari:C.8.10',))

# The coefficient argument is logically prior to the derivative values.
# Move its full proof once, rather than create an R2/R5 dependency loop.
a=s.index(r'\item \textbf{4. Global identification of the CM coefficient series.}')
b=s.index(r'\item \textbf{5. Directed enclosures of both $L$-sums.}',a)
old=s[a:b]
body=old.replace(r'\item \textbf{4. Global identification of the CM coefficient series.}'+'\n','',1)
body=body.replace(r'\item This finite comparison',r'\par This finite comparison',1)
body=body.replace('For all four bases,','For the four curves in the statement,',1)
replacement=r'''\item \textbf{4. Global identification of the CM coefficient series.}
Apply \cref{I:CM-coefficient-series} with $s=11,43,67,163$,
and then multiply the $n$th coefficient by the exact quadratic
twist character. This identifies both target and auxiliary series.

'''
patch(old,replacement,'Move the complete coefficient-identification proof before its first use.',
      ('ari:C.6.R2','ari:C.6.R5'))
new=r'''\begin{lemma}[The CM coefficient series]
\hypertarget{tag-IA08}{}\label{I:CM-coefficient-series}
For $s=11,43,67,163$, let $E_s$ be the respective rational
elliptic curve $121\mathrm b1$, $1849\mathrm a1$,
$4489\mathrm a1$, or $26569\mathrm a1$.
The coefficients of its normalized newform are
\[
 b_n=\sum_{a^2=n,\ a>0}\left(\frac as\right)a
 +\sum_{\substack{u,v>0,\ u\equiv v\ (2)\\u^2+sv^2=4n}}
       \left(\frac{(s+1)u/2}{s}\right)u.
\]
Quadratic twisting multiplies $b_n$ by the corresponding
quadratic character.
\end{lemma}
\begin{proof}
'''+body+r'''\end{proof}

'''
needle=r'\begin{proposition}[Central derivatives with explicit tails]'
patch(needle,new+needle,'Place the common CM coefficient lemma before the derivative theorem.',
      ('ari:C.6.R2','ari:C.6.R5'))
patch(r'''The global identification of this coefficient formula is proved
by the finite modular-form comparison in \cref{ari:C.6.R5}.''',
r'''The finite modular-form comparison in \cref{I:CM-coefficient-series}
proves the global identification of this coefficient formula.''',
'Use the preceding lemma and remove the potential forward dependency loop.',
('ari:C.6.R2',))

out=dict(source_path=str(base),source_sha256=hashlib.sha256(original.encode()).hexdigest(),
 generated_at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
 requires_batch='S6_SERIES_PUBLISH_I_editorial_batch_c_guards.json',guards=guards)
(B/'S6_SERIES_PUBLISH_I_editorial_batch_d_guards.json').write_text(json.dumps(out,indent=2)+'\n')
(B/'S6_SERIES_PUBLISH_I_editorial_batch_d_removed.json').write_text(json.dumps(removed,indent=2)+'\n')
(B/'S6_SERIES_PUBLISH_I_editorial_batch_d_preview.tex').write_text(s)
print(json.dumps({'guards':len(guards),'removed_blocks':len(removed),
 'preview_sha256':hashlib.sha256(s.encode()).hexdigest()},indent=2))
