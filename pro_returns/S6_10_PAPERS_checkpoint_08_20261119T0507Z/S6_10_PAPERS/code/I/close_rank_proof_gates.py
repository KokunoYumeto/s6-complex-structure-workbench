"""Integrate verified arithmetic inputs and the current interval certificates."""
from pathlib import Path
import json, csv, importlib.util, re

P=Path(__file__).resolve().parents[2]
INDEX=json.loads((P/'analysis/inventory_source_index.json').read_text())
S=(P.parents[1]/'sources/s6_09/S6_09_PAPERS_I.tex').read_text()
REV=P/'papers/I/revisions'
spec=importlib.util.spec_from_file_location('iii_numbering',P/'code/III/build_body.py')
helper=importlib.util.module_from_spec(spec);spec.loader.exec_module(helper)

def source(label):
    loc=next(x for x in INDEX.values() if x.get('label')==label)
    block=S[loc['start']:loc['end']]
    for m in list(re.finditer(r'\\begin\{proof\}(?:\[[^\]]*\])?(.*?)\\end\{proof\}',block,re.S))[::-1]:
        block=block[:m.start(1)]+'\n'+helper.numbered(m.group(1))+'\n'+block[m.end(1):]
    return block

s=source('ari:C.6.R2')
needle=r'\item The exact root numbers are $+1$ for $i=1,8$ and $-1$ otherwise.'
assert needle in s
period=r'''\item The real periods are enclosed from the exact minimal invariants,
independently of the saved decimal period values.  For rows $1,2,3,4$
put respectively $T=\sqrt2,\sqrt3,2,\sqrt7$ and $\tau=iT$;
for rows $5,\ldots,11$ put
$T=\sqrt{7}/2,\sqrt{11}/2,\sqrt{19}/2,\sqrt{27}/2,
\sqrt{43}/2,\sqrt{67}/2,\sqrt{163}/2$ and $\tau=1/2+iT$.
Let $r=e^{-2\pi T}$ and $q=e^{2\pi i\tau}$.  The identity
$E_4=1+240\sum_{n\geq1}\sigma_3(n)q^n$ and
$\sigma_3(n)<2n^3$ give, after $M=100$ terms, the tail bound
\[
480r^{A}\left\{
\frac{A^3}{1-r}+\frac{3A^2r}{(1-r)^2}
+\frac{3Ar(1+r)}{(1-r)^3}
+\frac{r(1+4r+r^2)}{(1-r)^4}\right\},\qquad A=101.
\]
This follows by expanding $(A+j)^3$ and summing each geometric
moment.  All eleven parameters satisfy
$1-1008r/(1-32r)>0$; the bound
$\sigma_5(n)<2n^5$ and $n^5\leq32^{n-1}$ therefore proves
$E_6(\tau)>0$.  The exact Weierstrass invariant relations yield
$\kappa=2\pi(E_4/c_4)^{1/4}$.  For $c_6>0$ the real lattice
generator has length $\kappa$.  For $c_6<0$ the lattice is rotated
by $i$: its real generator has length $T\kappa$ in the rectangular
case and $2T\kappa$ in the other case.  Indeed the real vectors in
$i(\Z+iT\Z)$ are $T\Z$, while those in
$i(\Z+(1/2+iT)\Z)$ are $2T\Z$.  Multiplication by the number
$n_{\R}=2$ for $\Delta>0$ and $n_{\R}=1$ for $\Delta<0$
gives the full real period used in the statement.

The current program \path{code/I/certify_all_period_ratios.py}
performs these operations with 768-bit Arb intervals and verifies
every displayed period and derivative ratio.  For the first ten
derivatives it enlarges the explicit tail by one percent and adds
$10^{-100}$ for arithmetic and kernel-series errors.  This last
bound is conservative: fewer than $5\cdot10^5$ coefficients and
740 series terms occur, the intermediate terms are below
$1.4\cdot10^{72}$, and the 1024-bit accumulated rounding and
$10^{-140}$ kernel remainders are below this allowance.
For the last derivative it adds $1.1\cdot10^{-75}$, covering the
proved block Taylor and rounding bounds above.  Division by the
strictly positive period intervals preserves all fifty displayed
digits.  The resulting intervals and exact invariants are in
\path{code/I/records/all_period_ratios_arb.json}.

'''
s=s.replace(needle,period+needle)
s=s.replace(r'For a nonmaximal CM order first pass to an isogenous',
            r'Proposition~5.3 of the same source supplies, for a nonmaximal CM order, an isogenous')
s=s.replace('curve with maximal order; ranks and $L$-functions are unchanged.',
            'curve with maximal order: the quotient is by the Galois-stable subgroup attached to the conductor ideal. The isogeny induces an isomorphism on Mordell--Weil groups tensored with $\\Q$ and on their rational Tate modules, preserving ranks and local $L$-factors.')
(REV/'ari_C.6.R2.tex').write_text(s)

s=source('ari:C.6.R3')
s=s.replace('The two rank-two curves do\nnot satisfy a rank-one formula; there $L\'(E_i,1)=0$ while',
            'For the two rank-two curves, $L\'(E_i,1)=0$ while')
s=s.replace('Changing their period convention\nto the full real period changes that factor only rationally.',
            r'''The differentials in the two conventions are rational multiples:
write $\omega'=a\omega_E$ with $a\in\Q^*$.  A primitive real
period for $\omega'$ is $|a|\Omega_i/n_{\R}$, where
$n_{\R}\in\{1,2\}$ is the number of real components.
Thus the change to the full real period multiplies the rational
factor by $|a|/n_{\R}$.''')
old='''The hypotheses are satisfied separately by the positive derivative
and exact sign in each of the nine rows. The two remaining rows
have analytic rank two, and this implication makes no assertion
of a height formula or of finiteness of their Tate--Shafarevich
groups. In particular it cannot express the second derivative
in terms of the height of $P$ alone: the rank-two regulator involves
a second independent point and their height pairing.'''
new=r'''The hypotheses are satisfied separately by the positive derivative
and exact sign in each of the nine rows.  Explicitly, the auxiliary
imaginary quadratic field $K$ in the proof of Gross--Zagier I.7.3
has split Heegner primes and $L(E_i^D,1)\ne0$; hence
$L'(E_i/K,1)=L'(E_i,1)L(E_i^D,1)\ne0$.  Its Heegner point has
positive height, so Gross's Theorem~1.3 gives finite
$\operatorname{Sha}(E_i/K)$.  The restriction map
\[
\operatorname{Sha}(E_i/\Q)\longrightarrow
\operatorname{Sha}(E_i/K)
\]
has kernel contained in
$H^1(\operatorname{Gal}(K/\Q),E_i(K))$ by restriction--inflation.
This last group is finite: the Mordell--Weil group is finitely
generated, and its degree-one cohomology for this order-two group
is finitely generated and killed by two.  The finite kernel and
finite image prove the claimed finiteness over $\Q$.
For the two other rows the established equations are
$L'(E_i,1)=0$ and $\widehat h_O(P_i)>0$; therefore an equation
$L'(E_i,1)/\Omega_i=q\widehat h_O(P_i)$ with $q>0$ would contradict
these exact values.  Their rank-two regulator, for any free basis
$P,Q$, is the determinant
$\widehat h_O(P)\widehat h_O(Q)-\langle P,Q\rangle^2$.'''
assert old in s;s=s.replace(old,new)
(REV/'ari_C.6.R3.tex').write_text(s)

s=source('ari:C.6.R4')
s=s.replace('Known with derivation: three exact leading factors','Known input: three exact leading factors')
s=s.replace('are exact, not numerical\nrational reconstructions.',
            'are determined exactly by the integer bounds in the cited application.')
s+=r'''\Uses{the exact models and primitivity in \cref{ari:C.6.R1};
the certified derivatives in \cref{ari:C.6.R2};
\citet[Definition~1.1, Theorem~1.2, and Table~9]{miller2011};
the full application retained in the proof compendium, Paper~I,
label \nolinkurl{app:rederive:ari-C.6.R4}}
'''
(REV/'ari_C.6.R4.tex').write_text(s)

f=P/'records/root_events.tsv'
rows=list(csv.DictReader(f.open(),delimiter='\t'));fields=list(rows[0])
events=[
 ('ari:C.6.R2','computation or formal certificate','Read the complete retained C++ summation program and replayed both segmented runs unchanged:384bits/radius128/cutoff170 and512bits/radius96/cutoff190. The latter reproduces915818441 coefficients,69802132 nonzero values,sumabs1904681267996,4745134 blocks and the saved derivative exactly. Explicit tail is3.09321800754876143967e-78. Independently enclosed all eleven real periods and fresh derivative ratios with Arb; all displayed fifty-digit values pass. Opened Rubin Proposition5.3 p15 and Theorem10.1/full Section10 pp47–50; the exact CM isogeny and central-vanishing application are now written out.'),
 ('ari:C.6.R3','complete receiving proof re-derivation','Matched Gross–Zagier I.7.3 pp11–12 and final proof p129 visually, Gross Theorem1.3 pp235–236 visually, and Jetchev–Lauter–Stein Theorem1.1 p2. Re-derived the rational differential/real-component period factor and added the explicit restriction–inflation argument carrying finite Sha from the Heegner field to Q. Exact derivative and algebraic-rank inputs were freshly replayed. The claimed nine positive rational factors and finite Sha conclusions are supported at this complete receiving-proof scope.'),
 ('ari:C.6.R4','exact primary-source and application check','Read Miller Definition1.1/Theorem1.2 p2, Section7 opening p16 and complete exception Table9 p23. Conductors3136,3136,361 lie outside the exceptions; all have proved analytic rank1. Exact local/torsion data give coefficient4. Current Arb height and derivative/period intervals isolate the resulting positive integer Sha order as1 in all three rows. Expanded known application remains in the unchanged proof compendium.'),
 ('ari:C.6.R5','exact primary-source check','Opened Stein Theorem9.18 and its entire proof pp171–173, Corollaries9.19–9.20 pp173–174, matching the coefficient bounds and coset-product argument. Together with the separately recorded YZZ, Cai–Shu–Tian, Darmon, Manin-constant and six directed numerical checks, this closes the named primary-source gates for the six denominator recognitions.'),
 ('ari:C.6.T1','computation or formal certificate','Read and replayed the unmodified local and final torsion programs in PARI2.17.2. Exact rank0,torsion4,conductor40,discriminant80,component orders2/1 and local-height coefficients1/12 match. Exact plus modular symbol is-1/4; the printed period/L-value comparisons reproduce. All starred final-log entries are stack-growth warnings; complete transcript contains no GP error.'),
 ('ari:C.6.T2','computation or formal certificate','Read and replayed the exact local program and the Simon two-isogeny descent driver with only its library read paths changed. bnfcertify=1 and LIMBIGPRIME=0; the complete new transcript has the displayed surviving points and excluded local coverings, quotient orders2 and4, hence rank1. Torsion6,three local types,valuations and weighted height sum match. Also reproduced the optional100-digit number-field L-value display, which retains numerical scope. No independent review of the entire Simon library is claimed.')]
checker='GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro, S6_10_PAPERS'
for label,typ,out in events:
    if not any(r['statement_id']==label and r['outcome']==out for r in rows):
        rows.append(dict(zip(fields,[label,'2026-11-18',checker,typ,out])))
with f.open('w') as h:
    w=csv.DictWriter(h,fields,delimiter='\t');w.writeheader();w.writerows(rows)
print('Integrated three arithmetic revisions and',len(events),'scoped check records.')
