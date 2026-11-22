"""Prepare exact, primary-source-checked reference transports and program table."""
from pathlib import Path
import datetime,hashlib,json,re
R=Path(__file__).resolve().parents[1]
source=R/'S6_SERIES_PUBLISH_II.tex';before=source.read_text();s=before
sha=lambda b:hashlib.sha256(b.encode() if isinstance(b,str) else b).hexdigest()
assert sha(before)=='a1d4fd6902cf13e774f672d2de4704460737a1f5ad82b036e4612045852eb119'
patches=[]
def patch(old,new,typ,owner,reason):
 global s
 assert s.count(old)==1,(owner,s.count(old),old)
 patches.append(dict(old=old,new=new,type=typ,statement_id=owner,reason=reason))
 s=s.replace(old,new)

old=r'''For every $Y$ and $D$ in Statement \CompendiumRef{II}{cdp:st:C.1.2} and every $L\in\Pic(Y)$,'''
new=r'''Let $Y$ be a smooth connected compact complex threefold with
$b_1(Y)=b_2(Y)=0$, carrying a nonzero effective Cartier divisor $D$.
For every $L\in\Pic(Y)$,'''
patch(old,new,'D06/D25','cdp:st:C.1.3',
'Expand the exact C.1.2 hypotheses in place. The attached compendium C.1.2 refers to C.1.1 for connected compact complex threefold and b1=b2=0, and itself specifies nonzero effective Cartier D with arbitrary positive multiplicities. Smoothness states the manifold scope used by the HRR/duality proof and explicitly required by the opened CDP98 Corollary1.3 (journal p79). No conclusion or divisor multiplicity is changed; no singular-total-space assertion is claimed.')
old=r'''On the dense open subset of each Picard component supplied by
Statement \CompendiumRef{II}{cdp:st:C.1.2}, Statement \ref{cdp:st:C.1.1} becomes'''
new=r'''Fix a component $P$ of $\Pic(Y)$ and a representative $L_P$.
Apply \cite[Corollary~1.3, p.~79]{CDP98} to
$T_Y\otimes L_P$ and $T_Y^*\otimes K_Y\otimes L_P^{-1}$.
Tensoring by $L_P$ identifies $\Pic^0(Y)$ with $P$, and
Serre duality identifies the latter degree-zero vanishing with
the degree-three vanishing for the inverse Picard parameter.
The two dense open sets intersect in a dense open subset of $P$.
On this subset, \cref{cdp:st:C.1.1} gives'''
patch(old,new,'D06/D17','cdp:st:C.1.3',
'Opened the complete compendium C.1.2 proof, CDP98 attached primary source lines269--282, and journal PDF p79 (Corollary1.3 and proof). The map Pic0→P is M↦L_P tensor M. Apply the known H0 theorem with B=T_Y tensor L_P; for H3 use B=T_Y^* tensor K_Y tensor L_P^-1 and M^-1 under Serre duality. Inversion is a biholomorphism of Pic0, so both dense open loci have a dense intersection. These exact maps replace the inaccessible compendium reference without reproving the known endpoint theorem.')
old=r'''The jump locus for the lower
bound on $h^2$ is closed analytic in the explicit family above and
contains a dense subset of the component. It therefore contains the
entire component.'''
new=r'''By \cref{cdp:st:C.1.1}, the component $P$ is a torsor for
$H^1(Y,\OO_Y)$. Exponentiating additive \v Cech representatives
of this vector space and tensoring by $L_P$ gives a holomorphic
family of line bundles on $Y\times P$. Proper cohomology
semicontinuity makes the locus satisfying the lower bound on
$h^2$ closed analytic in $P$. It contains the dense open subset
above and therefore all of $P$.'''
patch(old,new,'D06/D25','cdp:st:C.1.3',
'The omitted compendium proof contained the explicit exponential family; the printed phrase "family above" had no current antecedent. The replacement specifies its actual transition construction and the same proper semicontinuity map. Pic0 is the vector group proved by C.1.1, so the exponential cocycles parameterize P with no quotient ambiguity. The numerical inequality is unchanged.')

e4path=R/'agents/ii_checks_A/S6_SERIES_PUBLISH_II_E4_locator_transport_v2.json'
e4=json.loads(e4path.read_text())
primary=(R/e4['primary_source_path']).resolve()
assert sha(primary.read_bytes())==e4['primary_source_sha256']
assert e4['standing_hypotheses_exact'] in primary.read_text() and e4['statement_exact'] in primary.read_text()
old=r'\CompendiumRef{II}{cdp:st:E4}'
assert s.count(old)==13
new=e4['transport_target_citation']
for k in range(13):
 pos=s.index(old);a=s.rfind('\n',0,pos)+1;z=s.find('\n',pos)
 oldline=s[a:z];newline=oldline.replace(old,new)
 newline=newline.replace('By Statement '+new,'By '+new)
 newline=newline.replace('Statement '+new+' proves','The proof of '+new+' establishes')
 patch(oldline,newline,'D06',f'II:E4-input-occurrence-{k+1:02d}',
 'Exact input transport from compendium II E4 to Viaclovsky Theorem2.2, pp4--5. Root read the complete attached primary theorem and proof, lines379--488. Restriction to coordinate discs preserves properness and connected fibres; the inverse image is connected because a separation would give a disjoint closed separation of the connected disc under the proper map. Open base change identifies the restricted R1 direct image; local freeness glues. The H0 equality concerns the identical full analytic fibre. All other hypotheses and mathematical formulas in this receiving sentence are preserved. Complete owning-proof rereading is tracked separately.')
assert old not in s

opening=re.search(r'\\begin\{thebibliography\}\{[^}]*\}',s)
assert opening
old=opening.group(0)
programs=json.loads((R/'records/S6_SERIES_PUBLISH_II_opened_programs_01/receipt.json').read_text())
scopes={
 'D_exact_checks.py':r'Tangent index; integral monodromy and compact surface calculations (\cref{cdp:st:C.1.1})',
 'A_vertical_pole.py':r'Normalization, inverse Jacobian module and residue poles (\cref{cdp:st:A.2.5})',
 'A_non_lci_cusp.py':r'Curve equations, transverse jets and conormal valuations (\cref{cdp:st:A.2.6})',
 'root_unrestricted_euler.py':r'Exterior-square parity examples and Euler numbers of blowup families (\cref{cdp:st:C.2.UN.1,cdp:st:C.2.UN.2})'}
table=r'''\section*{Programs}
\addcontentsline{toc}{section}{Programs}
The following files contain the indicated computations at commit
\begin{center}\small\ttfamily\SsixRepositoryCommit\end{center}
Each link identifies the complete repository path.

{\footnotesize
\renewcommand{\arraystretch}{.9}
\setlength{\tabcolsep}{4pt}
\begin{longtable}{@{}>{\raggedright\arraybackslash}p{.57\textwidth}>{\raggedright\arraybackslash}p{.39\textwidth}@{}}
\caption{Programs and their mathematical scope.}\label{tab:II:programs}\\
\toprule Computation and statement & Source file \\
\midrule\endfirsthead
\toprule Computation and statement & Source file \\
\midrule\endhead
\bottomrule\endfoot
'''
for item in programs['programs']:
 assert item['pinned_tree_exact_blob_match'] and item['http_status']==200
 url=item['url'].replace(programs['commit'],r'\SsixRepositoryCommit')
 table+=scopes[item['name']]+' & '+r'\href{'+url+r'}{\nolinkurl{'+item['name']+r'}} \\[3pt]'+'\n'
table+=r'''\end{longtable}}

'''
patch(old,table+old,'D09','tab:II:programs',
'Initialize the single end-of-paper program table with four historical sources individually opened at the exact pinned commit. HTTP200 bodies match the recorded Git blob hashes. The first three retain program attributions removed in B-group01; the fourth restores the now-resolved historical attribution removed from UN2. This table adds no mathematical claim or check credit. Further program entries remain an open publication task.')

out=R/'records/S6_SERIES_PUBLISH_II_reference_transports_01';assert not out.exists();out.mkdir()
owner='cdp:st:C.1.3'
def block(t):
 j=t.index('\\label{'+owner+'}');a=t.rfind('\\begin{proposition}',0,j);z=t.index('\\end{proof}',j)+len('\\end{proof}')
 return t[a:z]
(out/'C13_before.tex').write_text(block(before));(out/'C13_after.tex').write_text(block(s))
g=dict(paper='II',source_before_sha256=sha(before),source_after_sha256=sha(s),patches=patches,
 created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),added_labels=['tab:II:programs'],
 primary_source_transport={'path':str(e4path.relative_to(R)),'sha256':sha(e4path.read_bytes())},
 C13_before_sha256=sha(block(before)),C13_after_sha256=sha(block(s)),
 mathematical_events_added=0,visual_reading_credit=0)
(out/'guard.json').write_text(json.dumps(g,indent=2)+'\n')
print(json.dumps(dict(path=str((out/'guard.json').relative_to(R)),sha256=sha((out/'guard.json').read_bytes()),patches=len(patches),source_after_sha256=sha(s)),indent=2))
