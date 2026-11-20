"""Keep unverified candidates in check provenance and cite actual opened loci."""
from pathlib import Path
import json,re,csv
R=Path(__file__).resolve().parents[1];p=R/'parts/I.body.linked.tex';s=p.read_text();changes=[]
def span(a,b,new,reason):
 global s
 i=s.index(a);j=s.index(b,i);old=s[i:j];changes.append(dict(old=old,new=new,reason=reason));s=s[:i]+new+s[j:]
span('This is an author-verified\nreproduction of Tate\'s result,','For our explicit bounded remainder and local normalization,',r'''This is Tate's height-variation identity as reproduced in the
remark following Theorem~4.1 of \citet[pp.~183--184]{callSilverman1993}.
The author's presentation \citet[slide~22]{silverman2006heights}
states the specialization limit, and slide~21 gives the uniform
canonical-versus-Weil-height bound in terms of the base height.
''','The mathematical dependence is on these opened author reproductions and the already cited DeMarco theorems; the inaccessible original editions remain documented in checks.')
span("Rubin's original ordinary main-conjecture\npaper is",'\n\nIn particular these ordinary-prime statements',r'''The asserted application retains the exact hypotheses of
\citet[Theorem~A]{CrCastella2025}.''','Remove an unopened historical bibliography mention without changing the stated Castella application or its exclusions.')
span(r'\paragraph{A theta criterion requiring its original normalization.}','A subsequent source check resolves the normalization of the',r'''\paragraph{The exact dependence of the theta expression on its lifts.}
Put
$g(u,v)=\log(\sigma(u+v)/(\sigma(u)\sigma(v)))$ on a branch where
all three sigma values are nonzero. Replacing $v$ by $v+\omega$,
$\omega\in\Lambda$, changes $g(u,v)-s_2uv$, modulo $2\pi i\Z$, by
\[
 (\eta(\omega)-s_2\omega)u=\frac{\pi\bar\omega u}{A}.
\]
The map $v\mapsto\exp_Ev$ sends these two lifts to the same
elliptic point. Thus $N\exp_Ev=f(\exp_Eu)$ for a
Rosati-antisymmetric $f$ retains its value under this lift change,
while the displayed theta expression acquires the stated term.
A use of the pointwise criterion in
\citet[final slide, comment~(c)]{bertrand2017} must therefore retain
its compatible lift convention. The Gaussian-norm question here
remains the precise question stated above.

''','Preserve the explicit lattice-lift calculation; move the withdrawn inference and unavailable Corollary3 access record to checks.')
span(r'\paragraph{A current source whose theorem text remains unchecked.}',r'\subsection{The precise nonarchimedean comparison}','', 'Move the Pham access/search history, which supplied no theorem premise, to the external check record.')
p.write_text(s);(R/'analysis/reference_scope_prose_changes.json').write_text(json.dumps(changes,indent=2))
D=json.loads((R/'analysis/source_bibliography_entries.json').read_text())
for e in D['Simonic2016Hartogs']:
 if 'Opened and matched' not in e['text']:
  e['text']+=r'''\newblock Opened and matched: arXiv:1608.00950v1, Theorem~1, p.~1, on 19 November 2026. The hypotheses are a bounded domain in $\mathbb C^n$, $n\ge2$, a compact subset, and connected complement; the conclusion is unique holomorphic extension. Verification concerns this exact local Hartogs use.'''
(R/'analysis/source_bibliography_entries.json').write_text(json.dumps(D,indent=2))
q=R/'analysis/reference_verification_overrides.json';q.write_text(json.dumps({
 'Simonic2016Hartogs':{'verified':True,'url':'https://arxiv.org/pdf/1608.00950','locator':'Theorem1 p1; v1 printed on page1','reference':'turn492317952view0','date':'2026-11-19','scope':'Exact bounded Hartogs extension theorem; no full-proof rereading claimed'},
 'BeukersHeckman1989':{'verified':True,'url':'https://math.uchicago.edu/~drinfeld/Hypergeometric_motives/Beukers-Heckman.pdf','locator':'Theorem3.5 pp331–332; Corollary3.6 p332','reference':'turn672654284view1','date':'2026-11-19','scope':'Companion monodromy presentation for disjoint roots and ring of definition; actual rational intertwiner remains proved in receiving paper'},
 **{k:{'verified':False,'scope':'Theorem text not opened; no receiving mathematical dependence authorized; access/search record preserved externally.'} for k in ['CrRubin1991','bertrand1984','pham2025sigma','silverman1983specialization','tate1983variation']}
},indent=2))
print(json.dumps({'prose_spans_moved':len(changes),'remaining_unverified_citations':[k for k in ['CrRubin1991','bertrand1984','pham2025sigma','silverman1983specialization','tate1983variation'] if k in s]}))
