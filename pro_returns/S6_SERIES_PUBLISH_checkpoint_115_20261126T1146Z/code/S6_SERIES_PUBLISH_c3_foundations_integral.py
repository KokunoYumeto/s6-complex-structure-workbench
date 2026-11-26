from pathlib import Path
import csv, datetime, re

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'agents/continuation3_foundations'
OUT.mkdir(parents=True,exist_ok=True)
s=(ROOT/'S6_SERIES_PUBLISH_II.tex').read_text()
a=s.index('\\section{Integral specialization, coherent restrictions and component counts}')
b=s.index('\\section{Complete smooth-fibre classification and actual Hopf occurrence}',a)
original=s[a:b]
x=original
fields=['change_id','type','statement_id','old_location','old_page','new_location','new_page','old_text','new_text','reason','review_status']
rows=[]
now=datetime.datetime.now(datetime.timezone.utc).isoformat()

def edit(old,new,types,owner,location,reason):
    global x
    assert x.count(old)==1,(owner,location,x.count(old))
    x=x.replace(old,new)
    for kind in types.split(','):
        rows.append(dict(change_id=f'II-C3-INTEGRAL-{len(rows)+1:03}',type=kind,statement_id=owner,
          old_location=location,old_page='cp35; final page concordance pending',new_location=location,new_page='integrated build pending',
          old_text=old,new_text=new,reason=reason,
          review_status='Complete original and receiving proof compared; source loci read at the stated scope.'))

edit('Let $f:Y\\to C$ be a proper holomorphic surjection from a connected\ncompact complex threefold to a compact Riemann surface, with',
 'Let $f:Y\\to C$ be a proper holomorphic surjection from a connected\nsmooth compact complex threefold to a compact Riemann surface, with',
 'D22','cdp:st:D.1.2','Components of exceptional fibres: ambient domain',
 'Clarify the inherited bare word threefold by stating smoothness explicitly. CDP98 §1.0 defines its ambient X as a compact complex manifold; its §5/Lemma5.2 and AC26 §10.5 use that manifold. The previous independent 01G0 derivation step6 explicitly uses a compact smooth manifold, and Hatcher Theorem3.44 requires an oriented manifold. All actual II consumers are smooth by their stated hypotheses, the Wang construction, or this inherited domain. The proof and conclusions are checked on that exact scope. This is a domain clarification, not a refutation or an extension to singular ambients.')
edit('Let $f:Y\\to\\PP^1$ be a holomorphic algebraic reduction of a compact\ncomplex threefold with $b_1(Y)=b_2(Y)=0$ and $a(Y)=1$.',
 'Let $f:Y\\to\\PP^1$ be a holomorphic algebraic reduction of a smooth compact\ncomplex threefold with $b_1(Y)=b_2(Y)=0$ and $a(Y)=1$.',
 'D22','cdp:st:D.1.10','Invariant restriction classes: ambient domain',
 'Make explicit the same inherited smooth-manifold domain as D.1.2 and CDP98 §1.0/§5. The divisor line bundles, component formula, Picard exponential identification and local-freeness input were checked at this scope. Every actual consumer has smooth ambient Y. No claim concerning singular ambients is made or refuted.')

# The rational count is already proved in the opened primary source. Retain
# the labelled abelianization map and prove the integral extension here.
m=re.search(r'\\begin\{proposition\}.*?\\label\{cdp:st:D\.1\.2\}.*?\\end\{proof\}',x,re.S)
before=m.group()
oldproof=before[before.index('\\begin{proof}'):]
newproof=r'''\begin{proof}
Put $U=Y\setminus D$ and $C^\circ=C\setminus\Delta$.
The rational component formula and the isomorphism
\begin{equation}
H_1(U;\Z)\simeq
\Z^{2g+s-1}\oplus H_1(F;\Z)_{\pi_1(C^\circ)}
\hypertarget{tag-019T}{}\label{cdp:eq:D1}
\end{equation}
are proved in \cite[Section~10.5, pp.~90--91, including
Lemma~10.7]{AC26}. The splitting in \eqref{cdp:eq:D1} comes from
lifting free generators of $\pi_1(C^\circ)$. The dual of its
coinvariant summand is the invariant space in the definition of $t'$:
a functional descends precisely when it vanishes on every
$\rho(g)v-v$.

For the integral assertion, the universal coefficient theorem first
makes $H_1(Y;\Z)$ finite from $H^1(Y;\Z)=0$, and then gives
$H_1(Y;\Z)=0$ from
$\operatorname{Ext}^1(H_1(Y;\Z),\Z)\subset H^2(Y;\Z)=0$.
It also makes $H_2(Y;\Z)$ finite. The compact-support sequence is
\[
H^4(Y;\Z)\longrightarrow H^4(D;\Z)
\longrightarrow H_c^5(U;\Z)
\longrightarrow H^5(Y;\Z)\longrightarrow H^5(D;\Z)=0.
\]
The complex orientation identifies $H^4(D;\Z)$ with $\Z^r$:
the singular and pairwise intersection loci have real dimension at
most two, so top cohomology has one generator for each oriented
irreducible component. Poincar\'e duality identifies $H^4(Y;\Z)$
with the finite group $H_2(Y;\Z)$, $H_c^5(U;\Z)$ with
$H_1(U;\Z)$, and $H^5(Y;\Z)$ with $H_1(Y;\Z)=0$.
The map from the finite group to $\Z^r$ is zero. Hence the
connecting map identifies $H_1(U;\Z)$ with $\Z^r$, and
\eqref{cdp:eq:D1} makes the coinvariant summand free abelian.
Finally, the Leray edge injection
$H^1(C;\Q)\hookrightarrow H^1(Y;\Q)=0$ gives $g=0$.
Substitution in the rational formula gives $r=s-1+t'$.
\end{proof}'''
edit(oldproof,newproof,'D17','cdp:st:D.1.2','Components of exceptional fibres: proof',
 'AC26 original manuscript Section 10.5, printed pp.90–91, proves the rational component formula and split coinvariant homology map at the same manifold/curve scope. Replace that already published rational proof by its exact citation, retaining equation D1 and the complete integral refinement. Cap product with the complex orientation identifies the compact-support sequence used in both versions; the finite-to-free map is zero, and its connecting map is the same H_1(U) identification. No rational or integral conclusion is discarded.')
edit("Under CDP20's integral assumptions",'Under the additional integral hypotheses','D18','cdp:st:D.1.2','Components of exceptional fibres: integral clause',
 'State the two displayed integral hypotheses directly. Their formulas and the credited component formula are unchanged.')

orphan=r'''The bielliptic-product rank defect is already described in \citet[Section~10.5, p.~91]{AC26}. The full integral torsion calculation, the coherent direct images and the separate rational-elliptic product below retain their additional precise content.'''
edit(orphan,'','D01,D08,D12,D13','cdp:st:D.1.5','After the two-projective-fibrations proof',
 'The proof already credits the bielliptic example to the same precise source, then proves the integral torsion, coherent direct images and rational elliptic product. Remove the repeated credit and production-facing description; the complete example and proof remain.')
edit('The component formula of \\cref{cdp:st:D.1.2} now gives four,\nin agreement with the four irreducible reduced fibres.',
 'The component formula of \\cref{cdp:st:D.1.2} gives $r=4$.',
 'D08,D21','cdp:st:D.1.6','Components in Wang\'s fibration: end of proof',
 'The same component count is asserted directly. The four fibre descriptions and their irreducibility remain in the statement and its cited filling construction.')
edit('The coherent direct images are given in \\cref{cdp:st:D.1.13}.','',
 'D12,D14','cdp:st:D.1.6','Components in Wang\'s fibration: last statement sentence',
 'The coherent direct images have their unique full statement and proof in D.1.13. Remove the forward-looking outline sentence; no direct-image formula was asserted here.')
edit("The final spanning step of CDP's rank argument reaches the whole\ntarget exactly when this span is $H^1(F,\\OO_F)$. This characterization concerns the subspace generated by the\nindicated invariant lattice in the restriction image.",
 r'''The final spanning step in \cite[Theorem~3.1, proof, p.~85]{CDP98}
reaches the whole target exactly when the indicated invariant lattice
spans $H^1(F,\OO_F)$ over $\C$.''',
 'D11,D18','cdp:st:D.1.10','Invariant restriction classes: source and scope',
 'The exact complex-span equivalence is unchanged. The citation identifies the published rank argument; AC26 Section10.5 explicitly maps its published Theorem3.1 to Theorem5.1 of the opened arXiv source. Remove the repeated scope sentence.')
edit(r'''Here is the rank computation with its maps specified. The map is
$\Z^r\to\Pic^0(Y)$, $(n_i)\mapsto\OO_Y(N\sum n_iD_i)$.''',
 r'''Consider the homomorphism
$\Z^r\to\Pic^0(Y)$, $(n_i)\mapsto\OO_Y(N\sum n_iD_i)$.''',
 'D08','cdp:st:D.1.10','Invariant restriction classes: divisor homomorphism',
 'The same explicit divisor-to-line-bundle homomorphism, kernel and rank computation remain; remove the process introduction.')
edit(r'''Coherent Leray identifies restriction
$H^1(Y,\OO_Y)\to H^1(U,\OO_U)$ with restriction of global
sections of $E$;''',
 r'''Put $E=R^1f_*\OO_Y$. Coherent Leray identifies restriction
$H^1(Y,\OO_Y)\to H^1(U,\OO_U)$ with restriction of global
sections of $E$;''',
 'D22','cdp:st:D.1.10','Invariant restriction classes: coherent bundle',
 'Define the bundle E at its use. It is exactly the R^1f_*O_Y bundle of D.1.4 and the cited local-freeness theorem; the maps and inference are unchanged.')

old_density=r'''The quantifier in \ref{cdp:st:D.1.11} is explicit. In the globally generated
two-torus case, the torsion parameters at even one fixed smooth fibre are
dense: the rational period lattice is dense in
$H^1(F,\OO_F)$, and restriction onto that space is surjective.
Thus the good set in that case cannot contain a nonempty open
subset of the Picard parameter space. A dense $G_\delta$ set of
full measure is the appropriate conclusion of the incidence
argument, rather than a Zariski-open conclusion.'''
remark=r'''\begin{remark}[Dense torsion restrictions]
\hypertarget{tag-P211}{}\label{rem:II:dense-torsion-restrictions}
\StatementRecord{rem:II:dense-torsion-restrictions}{proved}{P211}{}
In the globally generated two-torus case of \cref{cdp:st:D.1.11},
the line bundles in $\Pic^0(Y)$ which are torsion on any fixed
smooth fibre form a dense subset. Indeed, \cref{cdp:st:D.1.4,cdp:st:D.1.12}
identify restriction with a surjective complex-linear map onto
$H^1(F,\OO_F)$. The coefficient map identifies $H^1(F;\R)$
with the underlying real vector space of $H^1(F,\OO_F)$, so the
image of $H^1(F;\Q)$ is dense there. Its inverse image under
restriction is dense because a surjective linear map between
finite-dimensional vector spaces is open. The exponential sequence
identifies that inverse image precisely with the torsion restrictions.
Consequently the line bundles which are non-torsion on every fibre
contain no nonempty open subset of $\Pic^0(Y)$ in this case.
\end{remark}'''
edit(old_density,remark,'D02,D11,D13','rem:II:dense-torsion-restrictions','After the generic-line-bundles proof',
 'Move the existing mathematical density conclusion to one numbered remark. Its exact morphism is the coherent restriction/evaluation map of D.1.4, with base change from D.1.12; the real coefficient isomorphism for a torus sends H^1(F;Q) to a dense subgroup, and the exponential sequence identifies torsion. Openness of the surjective linear map justifies the inverse-image density already asserted by the original paragraph. Remove the draft-facing quantifier and Zariski-open commentary.')
edit(r'\citet[Proposition~5.6]{CDP2020}',r'\citet[Proposition~5.6, p.~689]{CDP2020}',
 'D18','cdp:st:D.1.11','Generic line bundles: published comparison',
 'The publisher PDF was opened at the statement and proof of Proposition5.6 on printed p.689. Add its exact page; mathematical claim unchanged.')
edit('This proves these two cases of CDP20\nProposition 5.1 by an index and cup-product argument.',
 r'''These are the torus and primary Kodaira cases of
\cite[Proposition~5.1, pp.~687--688]{CDP2020}.''',
 'D18','cdp:st:D.1.12','Cup products: published comparison',
 'Replace the bare publication shorthand by its exact existing bibliography key and locator; the assertion and method are unchanged.')
edit(r'''\cite[Theorem~2.2, pp.~4--5]{Viaclovsky2026Combs} gives $h^0=1$. These arguments retain the
scheme-theoretic fibres throughout.''',
 r'''\cite[Theorem~2.2, pp.~4--5]{Viaclovsky2026Combs} gives $h^0=1$
on every full fibre.''',
 'D08,D11','cdp:st:D.1.12','Cup products: end of proof',
 'Retain the full scheme-theoretic fibre scope at the exact conclusion, removing its separate production-style recap.')
edit(r'''In particular, the nonnegative splitting
degrees claimed by CDP20 Proposition 5.5 are equivalent to its
claimed general-fibre surjectivity when $E$ has rank two and is
locally free.''',
 r'''For a locally free sheaf $E$ of rank two, the nonnegative splitting
degrees in \cite[Proposition~5.5, p.~688]{CDP2020} are therefore
equivalent to surjectivity of the general-fibre restriction map.''',
 'D18','cdp:st:D.1.4','Restriction maps: published comparison',
 'The two rank-two conditions and their equivalence are identical; identify the published statement with a precise citation.')
edit(r'''The proof of \cite[Theorem~2.2, pp.~4--5]{Viaclovsky2026Combs} establishes local freeness by resolving the fibre support,
normalizing a cyclic base change with reduced central fibre, and
taking the invariant direct image.''',
 r'''Local freeness is \cite[Theorem~2.2, pp.~4--5]{Viaclovsky2026Combs}.''',
 'D12,D17','cdp:st:D.1.4','Restriction maps: local freeness citation',
 'The exact theorem was opened at its general analytic manifold scope. Its proof summary is unnecessary because the stated local-freeness conclusion is the only input here; no new proof step is removed.')

# Place the explicit maps before their uses and group the two sorts of examples.
pattern=r'\\begin\{(?:proposition|remark)\}.*?\\end\{(?:proof|remark)\}'
blocks={}
for m in re.finditer(pattern,x,re.S):
    owner=re.search(r'\\label\{([^}]+)\}',m.group()).group(1)
    assert owner not in blocks
    blocks[owner]=m.group().strip()
assert len(blocks)==13,blocks.keys()
section=x[:x.index('\\begin{proposition}')].strip()
residual=re.sub(pattern,'',x,flags=re.S).replace(section,'').strip()
assert not residual,residual
groups=[
 ('Component counts and projective examples','sec:II:component-counts',['cdp:st:D.1.2','cdp:st:D.1.5','cdp:st:D.1.6']),
 ('Cohomology and line-bundle restrictions','sec:II:coherent-restrictions',['cdp:st:D.1.7','cdp:st:D.1.8','cdp:st:D.1.4','cdp:st:D.1.12','cdp:st:D.1.9','cdp:st:D.1.10','cdp:st:D.1.11','rem:II:dense-torsion-restrictions']),
 ('Coherent splitting in explicit torus families','sec:II:coherent-splitting',['cdp:st:D.1.13','cdp:st:D.1.15'])]
new=section+'\n\n'+ '\n\n'.join('\\subsection{'+title+'}\\label{'+label+'}\n\n'+'\n\n'.join(blocks[o] for o in owners) for title,label,owners in groups)+'\n\n'
rows.append(dict(change_id=f'II-C3-INTEGRAL-{len(rows)+1:03}',type='D14',statement_id='sec:II:02',
 old_location='Integral specialization section: original statement order',old_page='cp35',new_location='Three descriptive subsections in the same section',new_page='integrated build pending',
 old_text='D.1.2, D.1.5, D.1.6, D.1.7, D.1.8, D.1.9, D.1.10, D.1.11, D.1.12, D.1.4, D.1.13, D.1.15',
 new_text='; '.join(title+': '+', '.join(owners) for title,_,owners in groups),
 reason='The coherent Leray and evaluation maps D.1.4 now precede their uses. D.1.12 supplies full-fibre base change before the new numbered density remark. The integral count, its examples, restriction theory and explicit splitting models form three bounded subsections. Every original statement and proof owner is retained exactly once.',
 review_status='Complete blocks read and ordered by these explicit dependencies; surrounding source not changed.'))

for pat in [r'\\label\{([^}]+)\}',r'\\hypertarget\{([^}]+)\}\{\}']:
    oldkeys=re.findall(pat,original);newkeys=re.findall(pat,new)
    for key in oldkeys: assert newkeys.count(key)==oldkeys.count(key),key
assert new.count('\\hypertarget{tag-P211}{}')==1
(OUT/'S6_SERIES_PUBLISH_II_integral_specialization.tex').write_text(new,newline='\n')

eventfields=next(csv.reader((ROOT/'CHECK_EVENTS.tsv').open(),delimiter='\t'))
events=[]
changed_owners=['cdp:st:D.1.2','cdp:st:D.1.5','cdp:st:D.1.6','cdp:st:D.1.10','cdp:st:D.1.11','cdp:st:D.1.12','cdp:st:D.1.4','rem:II:dense-torsion-restrictions']
for owner in changed_owners:
    details=' '.join(r['reason'] for r in rows if owner in r['statement_id'])
    row={k:'' for k in eventfields};row.update(statement_id=owner,date=now[:10],
      who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; inherited effort not separately exposed; continuation3 foundations',
      type='used and rechecked in this run',outcome='Complete original and receiving proof read and compared. '+details+' This is an exposed editorial reading, not an independent re-proof or final PDF reading.',
      event_id=f'publish:c3:integral:{owner}',phase='publication text and proof comparison',
      source_file='agents/continuation3_foundations/S6_SERIES_PUBLISH_integral_CHECK_EVENTS.tsv',source_event_type='used and rechecked in this run',
      evidence_group=f'publish:c3:integral:{owner}',date_utc=now,where='Integral specialization: complete owner proof and explicitly mapped consolidation')
    events.append(row)

status=[]
for title,label,owners in groups:
    for kind in [f'D{i:02}' for i in range(1,26)]+['structure']:
        pending={}
        pending['structure']='Internal dependency order is complete; root decides final whole-paper placement.'
        status.append(dict(unit=label,row=kind,status='open' if kind in pending else 'done',basis=pending.get(kind,'Complete unit read against all 25 types; each changed instance is logged and no residual instance found.'),fragment='agents/continuation3_foundations/S6_SERIES_PUBLISH_II_integral_specialization.tex'))

def table(name,headers,data):
    with (OUT/name).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=headers,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(data)
table('S6_SERIES_PUBLISH_integral_defects.tsv',fields,rows)
table('S6_SERIES_PUBLISH_integral_CHECK_EVENTS.tsv',eventfields,events)
table('S6_SERIES_PUBLISH_integral_unit_progress.tsv',['unit','row','status','basis','fragment'],status)
result=f'{len(rows)} defect rows; {len(events)} exposed readings; 3 units; P211 newly numbered. Every old label and target retained. Shared files unchanged.\n'
(ROOT/'code/S6_SERIES_PUBLISH_c3_foundations_integral.out').write_text(result,newline='\n')
print(result,end='')
