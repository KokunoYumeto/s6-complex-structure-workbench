#!/usr/bin/env python3
import re,json
from S6_SERIES_PUBLISH_editing import Editor,ROOT
e=Editor('V')
old=r'''We construct compact complex fourfolds from the torus-fibred complex
six-spheres of the $(3,4,\infty)$ family.  The main construction is a
family of complex three-tori over $\mathbb P^1$ with monodromy in
$GL_6(\mathbb Z)$: two multiple fibres, of multiplicities five and four,
and one Kuhn cusp.  Its periods come from the exterior square of the
genus-two pencil $y^2=x^5+\lambda^3x+\lambda^4$.  Every member is a
compact complex fourfold diffeomorphic, with its complex orientation, to
$3\mathbb{HP}^2\#(-\mathbb{HP}^2)$.  The family is parametrized exactly'''
new=r'''We construct compact complex fourfolds diffeomorphic, with their complex
orientation, to $3\mathbb{HP}^2\#(-\mathbb{HP}^2)$.
They form a family of complex three-tori over $\mathbb P^1$ with
monodromy in $GL_6(\mathbb Z)$: two multiple fibres, of multiplicities
five and four, and one Kuhn cusp. Its periods come from the exterior
square of the genus-two pencil $y^2=x^5+\lambda^3x+\lambda^4$.
The family is parametrized exactly'''
e.replace(old,new,'D15','State the headline compact complex realization in the first abstract sentence.','sec:results')
# The auxiliary fivefold part needs readable mathematical sections too.
for label,title,newlabel in [
('def:V:ordinary-closed-spin','The fibre complement and its homotopy coinvariants','pub:V:sec-complement'),
('maps:src:E.2.13','The circle fibration and its torus twist','pub:V:sec-torus-twist'),
('maps:src:E.2.16','The homotopy module and the quadratic cusp attachment','pub:V:sec-homotopy-module'),
('maps:src:E.2.19','Smooth plumbings and framed handles','pub:V:sec-handles')]:
 pos=e.text.index('\\label{'+label+'}');start=e.text.rfind('\\begin{',0,pos);head=e.text[start:pos]
 e.replace(head,'\\section{'+title+'}\\label{'+newlabel+'}\n\n'+head,'D14','Divide the long shifted-product part at a change of mathematical subject.',label)
e.replace('\\section{Shifted fibre products of two six-spheres}', '\\section{The shifted product and its bordism}', 'D14','Name the first shifted-product section by its content.','sec:shifted')
# Deduplicate main statement expansion lists after alias consolidation.
for c in 'ABCDEF':
 pat=re.compile(r'(\\hyperlink\{outline-V-'+c+r'\}\{Outline of the proof\}); proofs: [^\n]+')
 m=pat.search(e.text)
 if m:e.replace(m[0],m[1]+'.','D10','Keep one main-theorem navigation link; the outline supplies its exact proof references.','series:V:'+c)
# A repeated trailing See line contributes no further reference.
a=e.text.index('\\subsection{The proofs in outline}');b=e.text.index('\\subsection{Known and new}',a)
chunk=e.text[a:b]
for m in list(re.finditer(r'\\item\\hypertarget\{step-V-([^}]+)\}\{\}.*?(?=\n\\item|\n\\end\{enumerate\})',chunk,re.S)):
 old=m[0];tail=re.search(r'\nSee (.*?)\.\s*$',old,re.S)
 if not tail:continue
 tailrefs={v for g in re.findall(r'\\(?:cref|Cref|ref)\{([^}]+)\}',tail[1]) for v in g.split(',')}
 priorrefs={v for g in re.findall(r'\\(?:cref|Cref|ref)\{([^}]+)\}',old[:tail.start()]) for v in g.split(',')}
 if tailrefs and tailrefs<=priorrefs:e.replace(old,old[:tail.start()]+'\n','D10','Remove an exactly repeated outline-reference line.','step-V-'+m[1])
# Include the smooth classification conclusion proved for the retained inputs.
old='orders, twists or lattice indices (\\cref{maps:src:F.2.39}).'
new='orders, twists or lattice indices (\\cref{maps:src:F.2.39}).\nEvery resulting three-connected manifold is orientation-preservingly\ndiffeomorphic to $3\\mathbb{HP}^2\\#(-\\mathbb{HP}^2)$, by\n\\cref{maps:src:F.2.30}.'
e.replace(old,new,'D15','Include the body’s common oriented diffeomorphism conclusion in the full main classification statement.','series:V:F')
e.replace('almost complex compatibility: \\cite[Corollary~1.4, p.~4]{ffMandal}', 'connected-sum criterion and tangent classes: \\cite[Corollary~1.4, p.~4, Lemma~2.1, p.~5, and Theorem~2.4, p.~7]{ffMandal}', 'D18','Specify the roles of the opened Mandal results; the constructed almost complex extension is proved in the body.','pub:V:known-new')
# Compact only the vertical spacing of the contents, preserving type size.
e.replace('\\usepackage{tabularx}','\\usepackage{tabularx,etoolbox}\n\\makeatletter\n\\patchcmd{\\l@section}{\\addvspace{1.0em \\@plus\\p@}}{\\addvspace{.35em \\@plus\\p@}}{}{}\n\\patchcmd{\\l@part}{\\addvspace{2.25em \\@plus\\p@}}{\\addvspace{1em \\@plus\\p@}}{}{}\n\\makeatother','D23','Prevent a nearly empty continuation contents page by reducing inter-entry whitespace, preserving readable type size.')
e.save()
# Record this actual preliminary rendered read separately from the final certification.
record={'stage':'V_stage4','pdf_sha256':'0d29230eefd8f019839a820bf3a40fa901011bd829a2711e617c2148e395dd3d','pages_read':[1,2,3,4,5,9], 'scope':'Root visually read these complete rendered pages at1.5x; not a final-PDF certification.', 'findings':{'1':'Readable; headline moved to first sentence.','2':'Contents readable but overflowed by three entries onto page3; spacing fixed and shifted part subdivided.','3':'Nearly empty contents continuation; spacing fix pending rebuild.','4':'Headline and parameter readable; proof expansion/navigation lists too repetitive.','5':'Hodge table legible; duplicate alias references in the integral-theorem expansion removed.','9':'Proof outlines legible; repeated trailing See references removed.'}}
(ROOT/'records/S6_SERIES_PUBLISH_V_preflight_read.json').write_text(json.dumps(record,indent=2)+'\n')
