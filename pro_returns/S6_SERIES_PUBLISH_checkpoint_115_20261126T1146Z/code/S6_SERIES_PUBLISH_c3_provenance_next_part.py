#!/usr/bin/env python3
"""Prepare the next bounded Paper II fragment without shared-source writes.

The --reviewed option is reserved for the completed exposed old/receiving
reading. It is not a claim of an independent derivation.
"""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import csv
import hashlib
import json
import re

ROOT=Path(__file__).resolve().parents[1]
TMP=ROOT.parents[1]/'tmp'
OUT=ROOT/'agents/continuation3_provenance/next_part'
OUT.mkdir(parents=True,exist_ok=True)
original={
 'push':(TMP/'c3_provenance_push_stability_old.tex').read_text(),
 'combs':(TMP/'c3_provenance_combs_old.tex').read_text(),
 'uniform':(TMP/'c3_provenance_uniform_nontorsion_old.tex').read_text(),
}
owner_re=re.compile(r'\\begin\{(proposition|lemma|theorem|corollary|definition|remark|example|cited)\}')

def digest(text):return hashlib.sha256(text.encode()).hexdigest()
def write_tsv(path,rows,fields=None):
    with path.open('w',newline='') as f:
        w=csv.DictWriter(f,fields or list(rows[0]),delimiter='\t',lineterminator='\n')
        w.writeheader();w.writerows(rows)

def block(text,start):
    m=owner_re.match(text,start);assert m
    env=m.group(1);end=text.index(r'\end{'+env+'}',start)+len(r'\end{'+env+'}')
    p=text.find(r'\begin{proof}',end);n=owner_re.search(text,end)
    if p>=0 and (not n or p<n.start()):end=text.index(r'\end{proof}',p)+len(r'\end{proof}')
    return text[start:end]

old_blocks={};units={};source_unit={}
for unit,text in original.items():
    for match in owner_re.finditer(text):
        b=block(text,match.start())
        label=re.search(r'\\label\{([^}]+)\}',b).group(1)
        assert label not in units,label
        units[label]=b;old_blocks[label]=b;source_unit[label]=unit
assert len(units)==29,len(units)
rows=[]

def record(owner,old,new,types,reason,location='statement and proof'):
    rows.append(dict(change_id=f'II-C3-NEXT-{len(rows)+1:03d}',type=types,statement_id=owner,
        old_location=location,old_page='cp35; final page concordance pending',
        new_location=location,new_page='integrated build pending',old_text=old,new_text=new,
        reason=reason,review_status='Complete receiving comparison pending --reviewed.'))

def edit(owner,old,new,types,reason,all_matches=False):
    text=units[owner];count=text.count(old)
    assert count==1 or (all_matches and count>0),(owner,count,old[:100])
    for i in range(count if all_matches else 1):
        record(owner,old,new,types,reason,f'statement and proof; occurrence {i+1}' if count>1 else 'statement and proof')
    units[owner]=text.replace(old,new) if all_matches else text.replace(old,new,1)

def between(owner,start,end):
    t=units[owner];a=t.index(start);b=t.index(end,a)
    return t[a:b]

def statement_only(text):
    m=owner_re.match(text);e=r'\end{'+m.group(1)+'}'
    return text[:text.index(e)+len(e)]

protected=['push:src:E.5.2','push:src:E.5.3','push:src:E.2.4']

# A proved earlier owner supplies the exact non-holomorphic-reduction theorem.
owner='push:src:E.2.5'
old=between(owner,r'\item We apply \citet',r'\item In particular')
new=r'''\item Apply \cref{cdp:st:E2} to $X_0$. Its hypotheses hold because
$b_2(X_0)=0$ and $\langle c_3(X_0),[X_0]\rangle=2$.
Thus every meromorphic function on $X_0$ extends to a holomorphic
map to $\mathbb P^1$.

'''
edit(owner,old,new,'D12;D17','Use the earlier cited-result owner with the identity map on X0 and the exact b2 and c3 hypotheses; retain the relative-root, pencil, factorization and fixed-divisor proof.')
edit(owner,r'\citet[Theorem~2.1]{CDP2020}; \citet[Theorem~3.1 and Corollary~3.2]{LRS2019}',
     r'\SeriesRef{cdp:st:E2}','D04;D12','Metadata names the earlier exact premise used by this proof.')

# Correct exact primary locators, including each metadata occurrence.
replacements=[
 ('push:src:E.2.6',r'\citet[Proposition~3.1.2]{AbashevaDeev2024AB}',r'\citet[proof of Proposition~3.1.2, arXiv v1, p.~13]{AbashevaDeev2024AB}'),
 ('push:src:E.2.8',r'\citet[Lemma~3.3 and Corollary~3.4]{Fujino2021E}',r'\citet[Lemma~3.3 and Corollary~3.4, author version~0.08, p.~6]{Fujino2021E}'),
 ('push:src:E.2.8',r'\citet[Lemma~4.2]{CDP2020}',r'\citet[Lemma~4.2, p.~684]{CDP2020}'),
 ('push:src:E.2.9',r'\cite[Chapter~III, Theorem~4.12(ii)]{BS76push}',r'\cite[Chapter~III, Theorem~4.12(ii), pp.~134--135]{BS76push}'),
 ('push:src:E.2.9',r'\cite[Chapter~III, Theorem~4.1]{BS76push}',r'\cite[Chapter~III, Theorem~4.1, p.~124]{BS76push}'),
 ('push:src:E.2.14',r'\cite[Proposition~2.8 and Remark~8.3]{Engel2026}',r'\cite[Proposition~2.8, pp.~6--7, and Remark~8.3, pp.~22--23, arXiv v1]{Engel2026}'),
 ('push:src:E.2.22',r'\cite[Chapter~II, Theorem~8.8]{Demailly2012E}',r'\cite[Chapter~II, Theorem~8.8, pp.~118--121]{Demailly2012E}'),
 ('push:src:E.2.22',r'\cite[Chapter~VI, Theorem~1.1 and Table~10]{BHPV2004E}',r'\cite[Chapter~VI, Theorem~1.1 and Table~10, pp.~243--244]{BHPV2004E}'),
 ('push:src:E.2.22',r'\cite[Chapter~II, Definition~7.9 and Theorem~7.12]{Demailly2012E}',r'\cite[Chapter~II, Definition~7.9 and Theorem~7.12, pp.~114--115]{Demailly2012E}'),
 ('push:src:E.5.2',r'\citet[Proposition~4.2]{Viaclovsky2026Two}',r'\citet[Proposition~4.2, pp.~11--12]{Viaclovsky2026Two}'),
]
for owner,old,new in replacements:
    edit(owner,old,new,'D18','Opened the complete cited statement at the specified version and locus; the source supplies precisely the premise used here.',all_matches=True)
for owner in ['push:src:E.2.18','push:src:E.2.19','inv:E2.2']:
    edit(owner,r'\cite[\S7, Satz~5, pp.~63--64]{Grauert1960D}',
         r'\cite[\S7, Satz~5, p.~64; hypotheses and proof, pp.~62--64]{Grauert1960D}',
         'D18','Read §7 hypotheses and complete Satz 5 proof: proper map, flat coherent sheaf, reduced base and constant fibre cohomology give local freeness and the stated restriction isomorphism.')

# The invariant-cycle argument is specific and is retained in full.
edit('push:src:E.2.6',r'\SeriesRef{push:src:E.2.5}, \SeriesRef{push:src:E.2.22}, \SeriesRef{push:src:E.2.24};',
     r'\SeriesRef{push:src:E.2.5};','D14','Remove later-result metadata from an earlier proof whose actual premises are E2.5 and the explicitly cited classification input.')
edit('push:src:E.2.6','The classification of compact complex surfaces, or its\nspecial case for the differentiable four-torus, then makes\nthe central surface a complex two-torus as well.',
     'The root identity restricts to $K_F^A\\simeq\\mathcal O_F$, since\n$E_0=0$ and $\\mathcal L_0=g_0^*\\mathcal O(1)$. Hence $\\kappa(F)=0$.\nTogether with $b_1(F)=4$, the classification in\n'+r'\cite[Chapter~VI, Theorem~1.1 and Table~10, pp.~243--244]{BHPV2004E}'+ '\nidentifies $F$ as a complex two-torus.',
     'D18;D22','Give the exact canonical-root restriction and b1 value selecting the torus row of the opened classification table.')
edit('push:src:E.2.10',r'\SeriesRef{push:src:E.2.4}, ','','D14','Remove the forward chain-corollary metadata; its proof uses only the displayed earlier specialization results.')

owner='push:src:E.2.9'
old=between(owner,r'\item We first record the elementary vanishing',r'\item Let $B$ be any')
new=r'''\item Apply \cref{cdp:st:E17} on the reduced irreducible fibre $S$,
with effective Cartier divisor $H|_S$ and a locally free sheaf $V$.
The divisor meets its sole irreducible component, so
\[
 H^0(S,V(-nH))=0\qquad(n\gg0).
\]
For a full fibre $mS$, the ideal filtration has quotients
\[
 V|_S\otimes\mathcal O_S(-jS),\qquad 0\le j<m.
\]
Apply the same result to these finitely many bundles and use the
filtration exact sequences. This gives the vanishing on $mS$.
Multiplication by the canonical section of $H$ is injective on
$mS$: this Cartier hypersurface is Cohen--Macaulay, its only
associated component is $S$, and $H$ contains no local branch of $S$.

'''
edit(owner,old,new,'D12;D17','Replace the repeated divisor-vanishing proof by E17 with the exact divisor/bundle substitutions; retain the full mS filtration and associated-component injection needed for the later descending sets.')
edit(owner,r'; see also \SeriesRef{push:src:E.3.1}.','.',
     'D14;D18','The immediately preceding exact Ramis–Ruget citation supplies singular compact duality; remove the later analytic-duality owner from this proof.')
edit(owner,'The proper analytic coherence, semicontinuity and base-change\ntheorems are stated in '+r'\SeriesRef{push:src:E.3.1}.'+'\n','',
     'D12;D14','The exact primary base-change citation already stands at the application; remove the duplicate forward sentence.')
edit(owner,'linear combination.  Equivalently, use the integrable\nDolbeault operators obtained by a holomorphic linear\ncombination of fixed closed $(0,1)$-form representatives.',
     'linear combination.','D12','The explicit exponential Čech cocycle already constructs the holomorphic Picard family; remove the second construction.')
edit(owner,'holomorphic Cech\ncocycles','holomorphic '+r'\v{C}ech'+'\ncocycles','D23','Use the established accented Čech spelling.')

# Cusp topology is known; preserve the new transport and all explicit maps.
owner='push:src:E.2.20'
old=between(owner,'For the known Mumford cusp we\n','Take the universal covering\n')
new=r'''For the prescribed Mumford cusp,
\cite[Theorem~4.5, pp.~26--28; Proposition~4.7 and Corollary~4.8,
pp.~30--31]{AC26} give its simply connected toric cover and the free
period quotient, with deck group
\[
 \overline\Lambda=\Lambda/\Lambda_{\rm tor}\simeq\mathbb Z^2.
\]
On a regular fibre the covering is
$\mathbb C^2/\Lambda_{\rm tor}\to\mathbb C^2/\Lambda$.
Its fundamental-group homomorphism is the quotient
$\Lambda\to\overline\Lambda$; the $q$-meridian contracts along
$(x,y,z)=(q,1,1)$. The $q$-preserving diffeomorphisms above
transport this marking, the fibre-inclusion homomorphism and the
meridian contraction to $\mathcal N$.

'''
edit(owner,old,new,'D17;D12','The opened AC theorem and propositions prove the prescribed cover and inclusion map. Keep the exact lattice quotient, regular-fibre map, meridian section and new q-preserving transport; remove the duplicate van Kampen proof.')

# The two-period matrix statement and classification statement are protected.
owner='push:src:E.5.1'
old=units[owner]
new=r'''\begin{cited}[Singular fibres of the two-parameter threefold]\hypertarget{tag-033N}{}\label{push:src:E.5.1}
\StatementRecord{push:src:E.5.1}{proved}{033N}{\SeriesRef{push:src:E.5.2}; \cite[Lemma~2.1, pp.~3--4; Proposition~3.1, pp.~6--7; Theorem~1.1, p.~2]{Viaclovsky2026Two}}
In \cite[Lemma~2.1, pp.~3--4]{Viaclovsky2026Two}, the elliptic surface
$y^2=x^3+tx+1$ has fibre $III^*$ at infinity. The associated
threefold has two rank-one fibres at $p_1,p_2$, a rank-two
hexagonal fibre at $p_3$, and the multiple bielliptic fibre
$4B_*$ at infinity
\cite[Proposition~3.1, pp.~6--7; Theorem~1.1, p.~2]{Viaclovsky2026Two}.
The labels are those of \cref{push:src:E.5.2}; the ranks of
$T_1-I,T_2-I,T_3-I$ in that marking are $1,1,2$.
\end{cited}'''
edit(owner,old,new,'D17;D12;D18','Replace the known fibre configuration and its repeated Weierstrass calculation by the opened exact source results; the identity marking and the retained E5.2 matrices identify the three reduced-fibre labels.')

owner='push:src:E.5.3'
old=between(owner,r'\item The intrinsic fibration is the anticanonical pencil.',r'A biholomorphism therefore induces')
new=r'''\item On each parameter neighbourhood $U$ constructed above, the
family of \cite[Proposition~6.4, pp.~19--20]{Viaclovsky2026Two}
uses the same smooth-core charts, free degree-four root quotient,
and rank-one and hexagonal fillings as the construction in
\cite[Proposition~6.1, pp.~17--18]{Viaclovsky2026Two}.
Pull back those charts and their line-bundle transition maps along
the local parameter isomorphism
$(\mu,c)\mapsto(\mu,e^{-2\pi i c})$ on $U$, with the transported
marking and the fixed vector $\ell$. Its canonical isomorphism
therefore gives $K_X\simeq f^*\mathcal O_{\mathbb P^1}(-1)$
for the present member. Since $f_*\mathcal O_X=\mathcal O_{\mathbb P^1}$,
projection identifies
$H^0(X,-K_X)=f^*H^0(\mathbb P^1,\mathcal O(1))$.
Thus its base-point-free anticanonical pencil is $f$.
'''
edit(owner,old,new,'D17;D12','Use the opened canonical-bundle proposition through the explicit parameter pullback and identical filling charts; retain the projection-formula identification of the intrinsic pencil and every classification step.')
edit(owner,'common nonzero bound $|\\lambda|<\\eta$.  Pulling back by\n$\\lambda=e^{-2\\pi i c}$ gives the indicated half-plane.\nThe integral markings and the four-torsion section $\\ell/4$\ncontinue uniquely on this simply connected parameter domain.',
     r'''common nonzero bound $|\lambda|<\eta$. This bound corresponds to
the indicated half-plane under $\lambda=e^{-2\pi i c}$.
At any point of that half-plane, choose a parameter neighbourhood
$U$ on which $(\mu,c)\mapsto(\mu,e^{-2\pi i c})$ is biholomorphic
onto a source bidisc. Its inverse is
$(\mu,\lambda)\mapsto(\mu,-\log\lambda/(2\pi i))$, with the
branch taking the prescribed value of $c$. Transport the integral
marking to this bidisc and use the fixed vector $\ell$ in its
degree-four filling. The integral markings and the four-torsion
section $\ell/4$ continue uniquely on the simply connected
half-plane parameter domain.''',
     'D18;D22','The opened Proposition 6.4 constructs marked source bidiscs. Write the local parameter isomorphism and its logarithmic inverse, then continue the marking and ℓ over the half-plane; this preserves the exact global parameter scope and all protected statement bytes.')

# Remove defensive clauses after preserving their precise mathematical content.
edits=[
 ('push:src:E.2.7','We first control the moving three critical values without\nassuming that they remain distinct at zero.  Since','The three critical-value sections may coincide at zero. Since','D02','State the allowed collision positively before the critical-locus argument.'),
 ('push:src:E.2.12','In particular, no additional critical value occurs only\non the central target curve.\n\n','','D11','The preceding equality already specifies the exact central critical-value set.'),
 ('push:src:E.2.13','Equivalently this follows from normality of\n$Y$ and the finite birational form of its\nStein factorization.\n','','D12','The preceding finite birational map to the normal bidisc already proves connectedness.'),
 ('push:src:E.2.21','holomorphic dependence on $s$.  Equivalently one\nmay use a finite chart cover and its deck translates;\nthe same averaging solves the equivariant comparison.\nThe reduced finite fibres are the resulting free\nquotients; they have not been assumed to be tori.',
  'holomorphic dependence on $s$. The reduced finite fibres are the\nresulting free quotients.','D02;D12','The explicit averaging constructs the comparison; retain the finite-quotient identification once.'),
 ('push:src:E.2.21','centres; it does not evaluate a logarithm at a\nsingular fibre.  The finite and cusp chart',
  'centres. The finite and cusp chart','D02','The fixed-collar domain is already explicit and supplies the logarithm domain.'),
 ('push:src:E.2.21','actual marked period action there.  Thus\nthere is no additional central integral\ntranslation or fan datum.',
  'marked period action there.','D02;D11','The locally constant lattice comparison already identifies every allowed central class.'),
 ('push:src:E.2.22','root and normal-crossing charts used below; only\npointwise isomorphisms are not being substituted\nfor these relative comparisons.',
  'root and normal-crossing charts used below.','D02','The preceding local miniversality premise explicitly supplies family comparisons.'),
 ('push:src:E.2.22','are reduced.  This proof did not assume\nthat normalization commutes with base\nchange before obtaining the charts.',
  'are reduced.','D02','The retained finite immersion and diagonal test constructs the relative charts directly.'),
 ('push:src:E.2.22','This comparison does not assume\nthat the two actual columns were\nindependent at every $t$; equality\nof the kernels proves it afterwards.\n','',
  'D02;D11','The following rank argument explicitly proves invertibility of W from equality of kernels.'),
 ('push:src:E.2.22','The proof works along any path from\n$U$ and locally in the current\nparameter; it does not need an\nalready known punctured neighbourhood\nat the point being classified.',
  'This construction works along any path from $U$ and locally in the\nparameter.','D02;D08','Keep the pathwise scope in direct mathematical language.'),
 ('push:src:E.2.24','This statement does not identify the number of marked\nconnected components belonging to a single pair.\n','',
  'D11','The proved open-and-closed separation has its scope in the statement; remove the neighbouring unproved question.'),
 ('push:src:E.2.24','the quotient topology.  No assertion that the\nsaturated set itself is connected is needed.',
  'the quotient topology.','D02;D11','The proof establishes exactly the asserted open-and-closed property.'),
 ('inv:E2.5','actual conic data; no particular coordinate witness is asserted to\nbe an admissible conic.',
  'conic data.','D02','The later dense-open/intersection argument supplies admissible smoothings; the coordinate witness is used only to establish nonemptiness of the stated algebraic open set.'),
]
for owner,old,new,types,reason in edits:edit(owner,old,new,types,reason)

# Exact cross-paper owners from the attached pre-split E.1.2/E.1.3 proofs.
owner='push:src:E.2.21'
for old,new in [
 ('group already determined in E.1.',r'group of \SeriesRef{push:src:E.1.3}.'),
 ('the integral coboundary allowed in E.1.',r'the integral coboundary in \SeriesRef{push:src:E.1.2}.'),
 ('averaging in E.1 removes it',r'averaging in \SeriesRef{push:src:E.1.2} removes it'),
 ('the integral changes of origins in E.1.',r'the integral changes of origins in \SeriesRef{push:src:E.1.2}.'),
 ('extension sheaf $\\mathcal V$ of E.1.',r'extension sheaf $\mathcal V$ of \SeriesRef{push:src:E.1.2}.'),
 ('E.1 therefore applies to this actual\ncover and gives',r'\SeriesRef{push:src:E.1.2} therefore applies to this cover and gives'),
 ('splitting in E.1 kill the additive cocycle.',r'splitting in \SeriesRef{push:src:E.1.2} kill the additive cocycle.'),
 ('scalar translation group of E.1.  This\nproves both the central and family assertions.',r'scalar translation group of \SeriesRef{push:src:E.1.3}.'),
]:edit(owner,old,new,'D04;D06;D18','Read the complete attached pre-split E1.2/E1.3 statements and proofs: E1.2 supplies the explicit norm/coboundary, toric and extension-sheaf maps; E1.3 supplies their holomorphic parameter dependence and connected ambiguity. No Paper I manuscript was reopened.')
edit('push:src:E.2.22','E.1 and '+r'\ref{push:src:E.2.21}',
     r'\SeriesRef{push:src:E.1.2} and \ref{push:src:E.2.21}',
     'D04;D06','Resolve the exact global additive-comparison owner through the attached pre-split proof.')

# Replace an alternative contradiction by the first complete fixed-point argument.
owner='push:src:E.2.14'
old='by its entire complex flow.  Equivalently,\nthe resulting nowhere-zero real vector\nfield would give $\\chi(X_0)=0$,\nwhereas $X_0$ is diffeomorphic to $S^6$.'
edit(owner,old,'by its entire complex flow.','D12','The retained compact-group linearization and fixed-point contradiction already complete the exclusion; remove the second Euler-characteristic contradiction. Preserve the following extension to an ordinary constant-image torus with a second period.')

# A single numbered step structure for the two long comparison proofs.
for owner in ['push:src:E.2.21','push:src:E.2.22']:
    for m in list(re.finditer(r'\\noindent\\textbf\{Step ([0-9]+)\. ([^}]+)\}',units[owner])):
        edit(owner,m.group(),r'\item \emph{'+m.group(2)+'}',
             'D14;D23','Use one enumerate hierarchy: the preliminary comparison is its first item and each following geometric step is a separate item.')

# Direct mathematical phrasing, one logged occurrence at a time.
for owner in list(units):
    if owner in protected:
        begin=len(statement_only(units[owner]))
    else:begin=0
    while True:
        m=re.search(r'\bactual[ \t]*',units[owner][begin:])
        if not m:break
        start=begin+m.start();end=begin+m.end()
        old=units[owner][start:end]
        a=units[owner].rfind('\n',0,start)+1;b=units[owner].find('\n',end)
        if b<0:b=len(units[owner])
        oldline=units[owner][a:b];newline=oldline[:start-a]+oldline[end-a:]
        record(owner,oldline,newline,'D08','The adjacent formulas and named family already identify the mathematical object; remove the workflow intensifier.')
        units[owner]=units[owner][:start]+units[owner][end:]

# Remaining exact source locators and scope clauses.
edit('push:src:E.2.20','The and prescribed period kernels agree for $s\\ne0$;',
     'The period kernel of the family and the prescribed kernel agree for $s\\ne0$;',
     'D08;D23','Name both period kernels explicitly after removing the workflow adjective; the holomorphic kernel comparison is unchanged.')
edit('push:src:E.2.20','the just-verified regular-fibre\ninclusion map.',
     'the identified regular-fibre\ninclusion map.','D08','Refer directly to the explicit lattice quotient and fibre-inclusion map.')
for old,new in [('In an flat cohomology','In a flat cohomology'),
                ('smooth curve is an section.','smooth curve is a section.'),
                ('For completeness, these two vanishings determine the bundle by','These two vanishings determine the bundle by')]:
    edit('inv:E2.5',old,new,'D08;D23','Restore the grammatical article after removing the workflow adjective, or state the retained exact bundle calculation directly.')
edit('push:src:E.5.3',"The torsor's Cech class",r"The torsor's \v{C}ech class",
     'D23','Use the established accented Čech spelling.')
for owner,old,new in [
 ('push:src:E.5.3','The verified canonical formula','The canonical formula'),
 ('push:src:E.2.17','The original parameter\n$s$ is retained by this averaging.','This averaging fixes the parameter $s$.'),
 ('push:src:E.2.19','This can be checked at every stratum.  For','At each stratum the displayed coordinate vector fields give the map. For'),
 ('push:src:E.2.20','lift supplied by '+r'\ref{push:src:E.2.7}',r'lift of \ref{push:src:E.2.7}'),
 ('push:src:E.2.20','with both parameters retained.','fixing both parameters.'),
 ('inv:E2.5','derivatives with their frame derivatives retained.','derivatives, including the derivatives of the frames.'),
]:edit(owner,old,new,'D08','Name the mathematical formula or parameter-preserving map directly; all displayed coordinates and derivative terms remain unchanged.')
edit('push:src:E.2.12','This also explains why no zero of the leading\ncoefficient may be overlooked: such a zero would put\nthe point on the labelled graph closure.\n','',
     'D02;D11','The stated divisor identity and the choice of the bidisc already prove that u is a unit.')
edit('push:src:E.2.12',r'\item For completeness $t_*=\infty$ is impossible.',
     r'\item The value $t_*=\infty$ is impossible.','D08','State the monodromy exclusion directly.')
edit('push:src:E.2.16','Finally, the valid irreducible-fibre',
     'Finally, the irreducible-fibre','D08','The exact citation and the already proved irreducibility establish the premise; remove the editorial adjective.')
edit('push:src:E.2.22','group with a complex vector space.  This construction\nneeds no hypothesis on the fibres outside $U$.',
     'group with a complex vector space.','D02','The root construction uses only the globally stated proper submersion and sphere topology.')
edit('push:src:E.2.22','No finite\nsubring or seminormality assumption\nis being used.  Independence of the',
     'Independence of the','D02','The embedded reduced-hypersurface product equation was proved immediately before this sentence.')
edit('push:src:E.2.22','This is the descent proof of '+r'\ref{push:src:E.2.19}'+ ';\nit requires a nonempty known open set,\nnot specifically a punctured disc.',
     'This applies the descent proof of '+r'\ref{push:src:E.2.19}'+ '\nto identities holding over the nonempty open set $U$.',
     'D02','State the positive hypothesis of the identity-theorem transfer and retain the exact owner.')
edit('push:src:E.2.22','known.  No analytic curve selection\nfor an arbitrary open locus has\nbeen assumed.',
     'a member of the fixed constructed family.','D02;D08','The retained finite sequence of discrete exceptional layers and reverse filling directly gives the conclusion.')
old=between('push:src:E.2.22','These surfaces are complex tori.  To spell\n',r'\item \emph{The finite root charts.}')
new=r'''The root identity restricts to $K_F^{\otimes A}\simeq\mathcal O_F$,
so $\kappa(F)=0$. The vanishing of its canonical Chern class
excludes a $(-1)$-curve, and hence $F$ is minimal.
In \cite[Chapter~VI, Theorem~1.1 and Table~10, pp.~243--244]{BHPV2004E},
the minimal surface of Kodaira dimension zero with $b_1(F)=4$
is a complex two-torus.

'''
edit('push:src:E.2.22',old,new,'D12;D18;D22','The displayed global root identity, restricted to the smooth fibre, proves canonical torsion directly. Together with minimality and b1=4 this selects the torus row of the opened classification table, without repeating a Kähler-classification argument.')
edit('push:src:E.2.24','theorem at an arbitrary $J_0\\in\\mathcal I(S^6)$,\nincluding an initially unconstructed structure.',
     'theorem at an arbitrary $J_0\\in\\mathcal I(S^6)$.',
     'D11','The arbitrary-J0 quantifier already specifies the full ambient space needed for the open-and-closed argument.')
for owner in ['push:src:E.2.22']:
    edit(owner,'etale',r"\'etale",'D23','Restore the accent in étale.',all_matches=True)
edit('push:src:E.2.23',r'\citet[Chapter~II, Theorem~4.19, pp.~95--96]{Demailly2012E}',
     r'\citet[Chapter~II, Theorem~4.19 and proof, pp.~95--97]{Demailly2012E}',
     'D18','Read the full finite-projection statement and proof, including connectedness and the isolated central fibre on p.97.')
edit('push:src:E.2.12','that point and need not be an abelian surface.  The cusp',
     'that point. The cusp','D02;D11','The statement already identifies the torus with its precise source fibre; remove the extra scope disclaimer.')
edit('push:src:E.2.8','Without the hypothesis $b_1(F)=1$, every irreducible component\nof a \\emph{reducible} fibre of any such connected map from a\ncomplex $S^6$ also has normalization outside $\\mathcal C$.',
     'For every surjective holomorphic map from a complex $S^6$ to\n$\\mathbb P^1$ with connected fibres, each irreducible component\nof a reducible fibre has normalization outside $\\mathcal C$.',
     'D02','State the general reducible-fibre conclusion with its precise positive hypotheses, separately from the rank-one conclusion.')
edit('push:src:E.2.13','This is an assertion about the normalized cover;\nthe unnormalized fibre product generally has\nintersecting branches.\n','',
     'D02;D11','The preceding factorization and mutually inverse graph/projection maps already specify the normalized cover and its sheets.')
edit('push:src:E.2.22','The proof first propagates the geometric data\noutside finitely many successive discrete analytic\nexceptional sets.  It then fills these sets in reverse\norder by '+r'\ref{push:src:E.2.21}'+'.  Later exceptional sets are only\nclaimed to be discrete on the domain then under\nconsideration; they may accumulate at points removed\nat an earlier stage.',
     'At each step the exceptional set is a closed discrete analytic\nsubset of the current parameter domain. Such a set may accumulate\nonly at points removed from that domain. We apply\n'+r'\cref{push:src:E.2.21}'+ ' to these domains in reverse order.',
     'D08;D11','Retain the precise relative closedness needed for reverse filling, expressed as a property of the successive parameter domains.')
for old,new in [
 (r'\cite[Proposition~5.3]{Viaclovsky2026Combs}',r'\cite[Proposition~5.3, pp.~17--18]{Viaclovsky2026Combs}'),
 (r'Lemma~5.1 of \cite{Viaclovsky2026Combs}',r'\cite[Lemma~5.1, pp.~15--16]{Viaclovsky2026Combs}'),
 (r'\cite[Proposition~5.3 and \S9.2]{Viaclovsky2026Combs}',r'\cite[Proposition~5.3, pp.~17--18, and \S9.2, p.~30]{Viaclovsky2026Combs}'),
]:edit('inv:E2.5',old,new,'D18','Read the complete embedded-conic deformation, fixed-marking smoothing and normal-modification loci; retain all maps that identify these hypotheses with the present comb.')
edit('inv:E2.4',r'\citet[Corollary~1.3, preprint p.~2]{HKP2000}',
     r'\citet[Corollary~1.3, arXiv v1, p.~2]{HKP2000}',
     'D18','Use the opened arXiv version and exact location of the published universal vector-field assertion.',all_matches=True)
edit('inv:E2.4',r'\citet[Remarks 1.2 and 9.26]{AC26}',
     r'\citet[Remark~1.2, p.~2, and Remark~9.26, p.~83]{AC26}',
     'D18','Read both complete remarks in the opened author PDF; retain the explicit field injection proving why the combs contradict the cited assertion.',all_matches=True)

# Define the cup kernel before both its Hodge calculation and its twelve-tooth use.
owner='inv:E2.2'
old_kernel=between(owner,r'\item Define',r'The preceding map')
kernel_def=r'''\begin{definition}[Cup-product kernel of a positive comb]\hypertarget{tag-P278}{}\label{def:II:comb-cup-kernel}
\StatementRecord{def:II:comb-cup-kernel}{proved}{P278}{\SeriesRef{cdp:st:E15}; \cite[Proposition~6.1, p.~19]{Viaclovsky2026Combs}}
Let $X_m$ be a smooth $m$-tooth member with $m\ge12$, fixed limiting
period planes and standard logarithmic data, as in \cref{cdp:st:E15}.
Write $\bar f_m:X_m\to\mathcal B=\mathbb P(3,4)$ for its root lift,
$\rho:\mathcal B\to B$ for the coarse map, $F$ for the Hodge
bundle of \cref{cdp:st:E15}, $E_m=F^*$ for its vertical bundle,
and $G_m=R^1\bar f_{m*}\mathcal O_{X_m}$.
Exterior product with the logarithmic Kodaira--Spencer tensor defines
\[
 K_m=\ker\left\{\rho_*(E_m^*\otimes G_m)
  \xrightarrow{\ \kappa_1\ }
       \rho_*(\mathcal O(5)\otimes\det G_m)\right\}.
 \tag{E.6}\hypertarget{tag-01TV}{}\label{invII:eq:E.6}
\]
This is a rank-three vector bundle on $B$.
\end{definition}
\begin{proof}
At the cusp, \cite[Proposition~6.1, p.~19]{Viaclovsky2026Combs}
gives periods $(\log q)I/(2\pi i)+H_m(q)$ with $H_m$ holomorphic.
Their logarithmic derivative is $I/(2\pi i)+qH'_m(q)$ and is
invertible at zero. Thus $\kappa_1$ has generic rank one.
Its kernel is a torsion-free subsheaf of a rank-four bundle on the
smooth curve $B$, hence is locally free of rank three.
\end{proof}'''
units['def:II:comb-cup-kernel']=kernel_def;source_unit['def:II:comb-cup-kernel']='combs'
edit(owner,old_kernel,r'''\item ''','D13;D14','Move the kernel and its rank proof into a numbered definition before its statement and all consumers. The kernel map, root curve, bundles and equation target are unchanged.')
edit(owner,'The preceding map\n','The map preceding $\\kappa_1$ in the cotangent direct-image sequence\n',
     'D13;D23','Name the precise boundary map after extracting the kernel definition; its displayed domain, codomain and transpose tensor are unchanged.')
record('def:II:comb-cup-kernel',old_kernel,kernel_def,'D13;D14','The earlier E15 bundles are identified by E_m=F* and G_m=R¹fbar_*O; the same cup map and rank argument now define K_m before it is used.','before inv:E2.2')
old=between(owner,'The local periods at the cusp are\n','The connecting map\n')
new=r'''By \cref{def:II:comb-cup-kernel}, the logarithmic
Kodaira--Spencer tensor is invertible at the cusp.
'''
edit(owner,old,new,'D12','Its complete period-derivative calculation now belongs to the immediately preceding kernel definition.')
edit(owner,'There is a rank-three vector bundle $K_m$ on $B$ for which',
     r'For the rank-three bundle $K_m$ of \cref{def:II:comb-cup-kernel},',
     'D13;D14','Resolve the newly placed numbered definition with exactly the same root bundles and cup map.')
edit(owner,'The splitting in the last line need not be canonical.',
     '',
     'D02;D11','The displayed sheaf isomorphism states exactly the proved conclusion. Its proof explicitly computes Ext¹=0; remove the qualification about a preferred splitting.')

# Normalize the Picard parameter for the precise original (3,4) family.
owner='wb:thm:uniform-nontorsion-audit'
old_parameter=between(owner,r'\item The pullback',r'\item Fix a smooth fibre')
parameter_def=r'''\begin{definition}[Normalized Picard parameter]\hypertarget{tag-P279}{}\label{def:II:normalized-picard-parameter}
\StatementRecord{def:II:normalized-picard-parameter}{proved}{P279}{\SeriesRef{inv:A1.0}, \SeriesRef{inv:C3.1}}
Let $f:X\to B=\mathbb P^1$ be a member of the standard $(3,4)$
family in \SeriesRef{inv:A1.0}, with full special fibres
$3S_1,4S_2,W$ and its fixed period marking.
Use $M_u=\exp(ug)$ for the Picard isomorphism of
\SeriesRef{inv:C3.1}. Let $u_0$ be the unique parameter for
$M_{u_0}=f^*\mathcal O_B(1)$ and set
\[
 \phi(z)=u_0z/12,\qquad \phi^{-1}(u)=12u/u_0,
 \qquad L_z=M_{\phi(z)}.
\]
Thus
\[
 L_{12}=f^*\mathcal O_B(1).
 \tag{WBAPII.9.19}\hypertarget{tag-01TJ}{}\label{inv:wb:eq:9.19}
\]
For a full fibre $X_b$, write
$\iota_b(z)=(u_0z/12)g|_{X_b}$; its exponential is $L_z|_{X_b}$.
\end{definition}
\begin{proof}
Connected fibres and projection give
$h^0(X,f^*\mathcal O_B(1))=h^0(B,\mathcal O_B(1))=2$, whereas
$h^0(X,\mathcal O_X)=1$. Thus $f^*\mathcal O_B(1)$ is nontrivial,
so $u_0\ne0$ and the displayed scalar maps are inverse isomorphisms.
Under the coherent Leray and base-change maps of \SeriesRef{inv:A1.0},
the generator $g$ restricts to the nonzero invariant class
$\gamma^{0,1}$ on every full fibre. Multiplication by $u_0/12$
preserves that image line and makes every $\iota_b$ injective.
\end{proof}'''
units['def:II:normalized-picard-parameter']=parameter_def;source_unit['def:II:normalized-picard-parameter']='uniform'
edit(owner,old_parameter,'','D13;D14;D18','Move the normalization into a preceding numbered definition and identify the exact coherent-Leray/base-change premise A1.0. The inverse scalar map and L12 equality are retained.')
record('def:II:normalized-picard-parameter',old_parameter,parameter_def,'D13;D14;D18','The attached pre-split conventions and A1.0/C3.1 show the theorem is for the standard (3,4) family. A1.0 supplies nonzero full-fibre restriction; C3.1 supplies Pic=C. No Paper I manuscript was reopened.','before uniform non-torsion theorem')
edit(owner,r'There is a line bundle \(L\in\operatorname{Pic}(X)\) such that',
     r'For the fibration of \cref{def:II:normalized-picard-parameter}, there is a line bundle \(L\in\operatorname{Pic}(X)\) such that',
     'D20;D22','Make the ambient standard family and the chosen Picard-coordinate map explicit; the original proof and attached conventions use precisely this family.')
edit(owner,r'More precisely, identify \(\operatorname{Pic}(X)\) with \(\mathbb C\),'+ '\n'+r'\(z\mapsto L_z\).  Every \(z\) outside the union of \(\mathbb R\) with a',
     r'In the normalization of \cref{def:II:normalized-picard-parameter}, every \(z\) outside the union of \(\mathbb R\) with a',
     'D13;D20','Use the single numbered normalization, whose real exceptional line depends on the specified scalar map.')
edit(owner,r'\SeriesRef{inv:C3.1}, the image of \(\iota_q\) is the line',
     r'\SeriesRef{inv:A1.0}, the image of \(\iota_q\) is the line',
     'D18','A1.0, through coherent Leray and the invariant γ summand, supplies the smooth-fibre image; C3.1 supplies only the Picard exponential identification.')
edit(owner,r'\SeriesRef{inv:C3.1}, restriction',
     r'\SeriesRef{inv:A1.0} and \cref{def:II:normalized-picard-parameter}, restriction',
     'D18','Use the exact full-fibre base-change premise for nonzero restriction on 3S1, 4S2 and W, with the normalized scalar map.')
tail=original['uniform'][original['uniform'].index('% Complete working-edition supplement.'):]
record('sec:II:uniform-nontorsion',tail,'','D01;D07','Delete source-history and worker comments; the methodology section owns provenance.','source tail after uniform non-torsion proof')

# The legacy corollary states both holomorphic and continuous-family scopes.
# Keep it as their combined consequence after both complete owners, so that
# its tag does not lose any clause for an external reader.
owner='push:src:E.2.4'
old=units[owner][units[owner].index(r'\begin{proof}'):]
new=r'''\begin{proof}
For a connected analytic base $B$, pull back the family along
$B_{\mathrm{red}}\hookrightarrow B$. This preserves its complex
fibres and underlying parameter space, and preserves properness and
smoothness by base change. Apply \cref{push:src:E.2.23} to this
family. Its finite-chain conclusion and connected period-family
converse give the asserted equivalence.

By \cref{push:src:E.2.24}, the fixed-pair locus is open and closed
in the $C^\infty$ space of integrable complex structures. Its inverse
image under a continuous family on a connected parameter space is
empty or the whole parameter space, proving the final clause.
\end{proof}'''
edit(owner,old,new,'D12;D14','Retain every original corollary clause and its own tag. After the two complete owners, use the exact reduction pullback and inverse-image maps to combine their holomorphic/finite-chain and continuous-family conclusions.')

# Automatic equation numbers, retaining every existing equation label and tag.
equation_map={}
manual=re.compile(r'\\\[((?:(?!\\\]).)*?)\\tag\{([^}]+)\}((?:(?!\\\]).)*?)\\\]',re.S)
for owner in list(units):
    while True:
        m=manual.search(units[owner])
        if not m:break
        old=m.group();a,num,b=m.groups()
        labels=re.findall(r'\\label\{([^}]+)\}',a+b)
        label=labels[0] if labels else 'eq:II:next-'+re.sub(r'[^A-Za-z0-9]+','-',num).strip('-')
        equation_map[num]=label
        suffix='' if labels else r'\label{'+label+'}'
        new='\\begin{equation}'+a+b+suffix+'\\end{equation}'
        edit(owner,old,new,'D19','Use the current section equation counter while preserving the mathematical display, existing tag and label; add a stable label where the old inline number had none.')
for owner in list(units):
    for num,label in equation_map.items():
        token='('+num+')'
        if token in units[owner]:
            edit(owner,token,r'\eqref{'+label+'}','D04;D19','Resolve the equation through its preserved or newly assigned label after automatic section numbering.',all_matches=True)

# Stable section structure. No constant-monodromy or sign prerequisite moves.
section_specs=[
 ('S6_SERIES_PUBLISH_next_canonical_proposed.tex','Canonical pencils in smooth specializations','034G','sec:II:push-stability',
  [f'push:src:E.2.{n}' for n in range(5,11)]),
 ('S6_SERIES_PUBLISH_next_critical_proposed.tex','Extension of critical fibres','P273','sec:II:critical-fibre-extension',
  [f'push:src:E.2.{n}' for n in range(11,17)]),
 ('S6_SERIES_PUBLISH_next_nc_cusp_proposed.tex','Normal-crossing cusps','P274','sec:II:normal-crossing-cusps',
  [f'push:src:E.2.{n}' for n in range(17,19)]),
 ('S6_SERIES_PUBLISH_next_analytic_cusp_proposed.tex','Torus actions and analytic cusps','P275','sec:II:analytic-cusp-identification',
  [f'push:src:E.2.{n}' for n in range(19,21)]),
 ('S6_SERIES_PUBLISH_next_chains_proposed.tex','Connected deformation chains','P276','sec:II:connected-deformation-chains',
  [f'push:src:E.2.{n}' for n in range(21,25)]+['push:src:E.2.4']),
 ('S6_SERIES_PUBLISH_next_two_periods_proposed.tex','Two independent periods','P277','sec:II:two-independent-periods',
  ['push:src:E.5.2','push:src:E.5.1','def:II:two-parameter-period-data','push:src:E.5.3']),
 ('S6_SERIES_PUBLISH_next_combs_proposed.tex','Hodge growth and cup-product kernels of combs','034D','sec:II:combs',
  ['def:II:comb-cup-kernel','inv:E2.2','inv:E2.4','inv:E2.5']),
 ('S6_SERIES_PUBLISH_next_uniform_proposed.tex','Uniform non-torsion on every full fibre','034H','sec:II:uniform-nontorsion',
  ['def:II:normalized-picard-parameter','wb:thm:uniform-nontorsion-audit']),
]
pieces=[];placements=[]
for filename,title,tag,label,owners in section_specs:
    heading=r'\section{'+title+r'}\hypertarget{tag-'+tag+r'}{}\label{'+label+'}'
    text=heading+'\n\n'+'\n\n'.join(units[o] for o in owners)+'\n'
    (OUT/filename).write_text(text,newline='\n');pieces.append(text)
    placements.append(dict(section=label,title=title,tag=tag,owners=owners,file=filename))
combined='\n'.join(pieces)
record('sec:II:push-stability',original['push'].split('\n',1)[0],
       '\n'.join(r'\section{'+t+r'}\hypertarget{tag-'+tag+r'}{}\label{'+l+'}' for _,t,tag,l,_ in section_specs[:6]),
       'D14','Order the relative-pencil, critical-value, root, cusp and global-comparison premises before deformation chains. Place E5.2 before the configuration that uses its monodromy ranks. Preserve all full new proofs and both protected statements.','section order')
record('sec:II:combs',original['combs'].split('\n',1)[0],pieces[6].split('\n',1)[0],
       'D14','Place the numbered kernel definition, Hodge calculation, vector-field consequence and twelve-tooth kernel calculation in their dependency order.','section title and internal order')
(OUT/'S6_SERIES_PUBLISH_next_part_proposed.tex').write_text(combined,newline='\n')

guards=[]
for owner in protected:
    old=statement_only(old_blocks[owner]);new=statement_only(units[owner])
    assert old==new,owner
    guards.append(dict(statement_id=owner,old_sha256=digest(old),new_sha256=digest(new),bytes=len(old.encode()),outcome='Statement bytes unchanged, including title, tag, label and metadata.'))
old_labels=set(re.findall(r'\\label\{([^}]+)\}','\n'.join(original.values())))
old_tags=set(re.findall(r'\\hypertarget\{(tag-[^}]+)\}','\n'.join(original.values())))
assert old_labels<=set(re.findall(r'\\label\{([^}]+)\}',combined)),old_labels-set(re.findall(r'\\label\{([^}]+)\}',combined))
assert old_tags<=set(re.findall(r'\\hypertarget\{(tag-[^}]+)\}',combined)),old_tags-set(re.findall(r'\\hypertarget\{(tag-[^}]+)\}',combined))
assert r'\tag{' not in combined
for target in ['night:P4R.13','night:P4.40']:
    assert all(target not in s for s in original.values()) and target not in combined
write_tsv(OUT/'S6_SERIES_PUBLISH_next_statement_guards.tsv',guards)

ap=argparse.ArgumentParser();ap.add_argument('--reviewed',action='store_true');args=ap.parse_args()
if args.reviewed:
    for row in rows:row['review_status']='Complete old/receiving statement-and-proof comparison read; used and rechecked in this run.'
write_tsv(OUT/'S6_SERIES_PUBLISH_next_defects.tsv',rows)
status=dict(scope='Connected chains, two periods, combs and uniform non-torsion; stops before Analytic duality.',
    source_snapshots={k:str(TMP/('c3_provenance_'+{'push':'push_stability','combs':'combs','uniform':'uniform_nontorsion'}[k]+'_old.tex')) for k in original},
    structure=placements,old_complete_reading=True,receiving_complete_reading=args.reviewed,
    source_admission=False,shared_writes=False,pdf_pages='Parent integrated build and complete page reading pending.',
    protected_statements=guards,refined_P4R13_P440_uses='No direct use in either original or receiving bounded fragments.',
    unused_reserved_tags=['P280'],defect_classes={f'D{i:02d}':('receiving comparison complete; final integration gate pending' if args.reviewed else 'receiving comparison pending') for i in range(1,26)})
(OUT/'S6_SERIES_PUBLISH_next_status.json').write_text(json.dumps(status,indent=2,ensure_ascii=False)+'\n',newline='\n')
print(f'Prepared {len(rows)} exact instance/movement rows and {len(units)} receiving owners; reviewed={args.reviewed}; shared source unchanged.')
