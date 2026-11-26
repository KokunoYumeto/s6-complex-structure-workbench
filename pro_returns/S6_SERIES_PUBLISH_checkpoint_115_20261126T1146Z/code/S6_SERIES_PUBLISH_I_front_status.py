from pathlib import Path
import json,datetime,hashlib
from S6_SERIES_PUBLISH_editing import Editor
r=Path(__file__).resolve().parents[1];ed=Editor('I')
mechanisms={
 'A':r'Theta transformation laws fix the additive constant, division identities control the norm, and the local-height product formula fixes its arithmetic normalization.',
 'B':r'Integral centralizers, finite norm maps and cusp winding determine the parameter equivalence, while the marked reflection and cap-meridian maps determine the real forms.',
 'C':r'The integral congruence kernel determines the parabolic quotient, and the wedge equation with its Hermitian form determines the fibre strata.',
 'D':r'Root characters and logarithmic residues compute the connecting scalar and direct images, exterior quotients by $dt$ give the ordinary modules, and theta factors with cusp Cartier frames give the coefficient cocycles.',
 'E':r'Weighted section counts and local Koszul modules compute every Picard twist, while the nonzero Kodaira--Spencer class gives the coordinate on the Kuranishi line.',
 'F':r'The intrinsic canonical system recovers the marked base, finite-orbit vanishing kills horizontal meridians, and their constant ratio across the connected compact corner contradicts the nonzero cusp coefficient.',
 'G':r'The intrinsic Albanese invariant detects the outer boundary, and the exact dual-period equations with their quadratic cancellation determine nonseparation and every marked closed-group limit.'}
statuses={
 'A':r'New period evaluations, norm values and level classification, using the elliptic section of \cite[Remark~3.12, p.~19]{AC2026}.',
 'B':r'New classification for the displayed discrete data and real forms; the standard $2\mathbb Z$ equivalence is known \cite[Theorem~1.4, p.~3]{DuEtAl2026v1}.',
 'C':r'New integral monodromy and maximal proper domain, answering \cite[Remark~8.4, pp.~23--24]{Engel2026}.',
 'D':r'New evaluated cohomology and coefficient atlas; the ordinary-module calculation corrects \cite[Remark~9.21, p.~81]{AC2026}.',
 'E':r'New all-twist and higher-multiplicity formulas; the standard untwisted deformation results are known \cite[Theorem~6.12, pp.~81--82; Proposition~6.16, p.~85]{DuEtAl2026v1}.',
 'F':r'New filling obstruction and untwisted plumbing; the Euler calculation corrects the proposed central model in \cite[Conjecture~8.2, p.~22]{Engel2026}.',
 'G':r'New boundary obstruction and marked limit formulas, using the annihilator duality of \cite[Theorem~3.1, p.~2017]{Cornulier2011}.'}
for letter in 'ABCDEFG':
 p=ed.text.index(r'\label{series:I:'+letter+'}')
 a=ed.text.index(r'\end{maintheorem}',p)+len(r'\end{maintheorem}')
 b=ed.text.index(r'\hypertarget{main-I-'+chr(ord(letter)+1)+'}{}',a) if letter!='G' else ed.text.index(r'\subsection{The proofs in outline}',a)
 old=ed.text[a:b]
 new='\n\n'+r'\textit{Mechanism.} '+mechanisms[letter]+'\n'+r'\textit{Literature status.} '+statuses[letter]+'\n'+r'\hyperlink{outline-I-'+letter+'}{Proof in outline}.'+'\n\n'
 ed.replace(old,new,'D07','Give one mathematical mechanism sentence and one scoped literature-status line; the detailed source map remains in the known/new table and proof outline.','series:I:'+letter)
rows={
 'A':r'New explicit evaluations and sharp norm bounds from the known section \cite[Remark~3.12, p.~19]{AC2026}; the quotient and height inputs are \cite[Definition~2.3, p.~5; proof of Lemma~2.1, pp.~3--4]{Engel2026}, transported by \cref{I:weierstrass-comparison}.',
 'B':r'New discrete-data and real-form extensions of the standard equivalence \cite[Theorem~1.4, p.~3]{DuEtAl2026v1}; the higher construction is \cite[Theorem~1.1, p.~1; Section~2.1, pp.~4--6]{ViaclovskyLog2026}, with $(k,l)=(1,1)$ giving the standard data.',
 'C':r'New exact group, quotient and proper-domain answer to \cite[Remark~8.4, pp.~23--24]{Engel2026}; the fibre tests use the integral wedge equation of \cite[Lemma~9.2, p.~65]{AC2026} with the period row $\beta=\beta_c$.',
 'D':r'New value of the Hodge integer, full cohomology and coefficient representatives extending \cite[Theorem~9.1(vi), p.~65; Proposition~9.20, p.~80]{AC2026}; the degree-one cusp module corrects its Remark~9.21, p.~81, and specifies the degree dependence of Remark~1.3, p.~5.',
 'E':r'New Picard-twist and coprime-root calculations extending the known standard tangent, Kuranishi and automorphism results \cite[Theorems~1.3--1.4, p.~3; Theorem~6.12, pp.~81--82; Proposition~6.16, p.~85; Theorem~7.14, p.~95]{DuEtAl2026v1}, under the parameter map of \cref{night:P5.7}.',
 'F':r'New marked nonfilling obstruction and explicit untwisted filling in the degeneration setting of \cite[Remark~8.1, p.~22]{Engel2026}; virtual Euler number zero excludes the particular central model in its Conjecture~8.2, p.~22.',
 'G':r'New intrinsic boundary and marked additive-limit calculations; the map $w\mapsto iw/216$ supplies the modular boundary, and \cite[Theorem~3.1, p.~2017]{Cornulier2011} supplies closed-group duality under the real annihilator map.'}
a=ed.text.index(r'\subsection{Known and new}');b=ed.text.index(r'\subsection{Methodology}',a)
old=ed.text[a:b]
new=r'''\subsection{Known and new}\label{pub:I:known-new}
\begingroup\small
\begin{longtable}{@{}p{.08\textwidth}p{.87\textwidth}@{}}
\toprule Theorem & Status and credited inputs\\\midrule\endhead
'''
new+='\n'.join(letter+' & '+rows[letter]+r'\\' for letter in 'ABCDEFG')
new+='\n'+r'\bottomrule\end{longtable}\endgroup'+'\n\n'
ed.replace(old,new,'D07','Give one source-specific row per main theorem; remove duplicated status paragraphs and preserve exact source-to-application maps.','pub:I:known-new')
ed.save()
sources=[r/'agents/i_analytic/S6_SERIES_PUBLISH_I_global_ABC_comparison.md',r/'agents/i_provenance/S6_SERIES_PUBLISH_I_DG_literature_status.json',r/'agents/i_provenance/S6_SERIES_PUBLISH_I_DG_literature_search_scope.json']
(r/'records/S6_SERIES_PUBLISH_I_front_status_receipt.json').write_text(json.dumps({'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source_sha256':hashlib.sha256(ed.text.encode()).hexdigest(),'mechanisms':mechanisms,'statuses':statuses,'known_new_rows':rows,'source_receipts':[{'path':str(p.relative_to(r)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in sources],'scope':'Scoped literature/application descriptions based on the opened primary locators and bounded searches. No exhaustive priority or absence claim. Mathematical statements and proof outlines are unchanged; the full credited appendix remains. Final provenance cross-check against deposits remains required.'},indent=2)+'\n')
