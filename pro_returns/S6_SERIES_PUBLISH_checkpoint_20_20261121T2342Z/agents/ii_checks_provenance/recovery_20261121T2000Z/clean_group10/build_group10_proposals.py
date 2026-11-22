from pathlib import Path
import hashlib, json, re
from datetime import datetime, timezone

ROOT=Path('/workspace/scratch/08a92fb2355d/S6_SERIES_PUBLISH')
D=Path(__file__).parent
BASE=D.parent
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def bind(p): return {'path':str(p.relative_to(ROOT)), 'sha256':sha(p)}
def dump(p,obj): p.write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n')
now=lambda:datetime.now(timezone.utc).isoformat()
source=ROOT/'S6_SERIES_PUBLISH_II.tex'
canonical=source.read_text()
release={r['tag']:r for r in json.loads((D/'S6_SERIES_PUBLISH_II_clean_group10_releases.json').read_text())}
targets=[]
class Edit:
 def __init__(self,t):
  self.tag=t; self.p=D/f'S6_SERIES_PUBLISH_II_{t}_original.tex';self.orig=self.p.read_text();self.text=self.orig;self.guards=[]
  assert canonical.count(self.orig)==1,(t,'original absent/multiple in current source')
 def r(self,old,new,typ,why,n=1):
  assert self.text.count(old)==n,(self.tag,old,self.text.count(old),n)
  self.guards.append({'change_id':f'II-REC-C10-{self.tag}-{len(self.guards)+1:02d}','defect_type':typ,'old':old,'new':new,'expected_occurrences_in_owning_block':n,'reason':why})
  self.text=self.text.replace(old,new)
 def standard(self,title):
  m=re.search(r'\\begin\{(?:lemma|proposition|theorem|corollary)\}\[([^\n]+)\]',self.text)
  if m.group(1)!=title:self.r(m.group(1),title,'D23','Capitalize the mathematical title.')
  self.r('\n\n\\ ','\n\n','D23','Remove the stray control-space at the statement opening.',1)
 def enum(self):
  self.r(r'\begin{enumerate}[label={$\langle1\rangle$\arabic*.},leftmargin=*]',r'\begin{enumerate}[label=\arabic*.,leftmargin=*]','D04,D23','Use ordinary proof-step numbering in place of an iteration label.')
 def single(self):
  self.r('\\begin{enumerate}[label={$\\langle1\\rangle$\\arabic*.},leftmargin=*]\n\\item \n\\noindent\\textbf{Step 1.} ','','D04,D23','Remove the single-item iteration wrapper and duplicate step heading.')
  self.r('\n\\end{enumerate}','','D04,D23','Remove the matching single-item wrapper terminator.')
 def save(self):
  p=D/f'S6_SERIES_PUBLISH_II_{self.tag}_proposed.tex';p.write_text(self.text)
  lab=lambda s:re.findall(r'\\(?:label|hypertarget)\{[^}]+\}',s)
  assert lab(self.orig)==lab(self.text),(self.tag,'label/tag change')
  assert self.orig.count(r'\begin{proof}')==self.text.count(r'\begin{proof}')==1
  fr=json.loads((BASE/'clean_derivations'/f'S6_SERIES_PUBLISH_II_{self.tag}_freeze_pointer.json').read_text())
  rr=release[self.tag]['release']
  # The pointer schema is deliberately retained verbatim, with the exact underlying receipt separately resolved below.
  fpath=ROOT/(fr.get('receipt') or fr.get('freeze_receipt') or fr.get('path'))
  fj=json.loads(fpath.read_text())
  targets.append({'tag':self.tag,'statement_owner':re.search(r'\\label\{([^}]+)\}',self.orig).group(1),'checker':'i_provenance_recovery',
   'freeze_pointer':bind(BASE/'clean_derivations'/f'S6_SERIES_PUBLISH_II_{self.tag}_freeze_pointer.json'),
   'freeze_receipt':bind(fpath),'release_receipt':bind(ROOT/rr['receipt']),
   'release_envelope':bind(ROOT/rr['full_block']),
   'original_full_block':bind(self.p),'proposed_full_block':bind(p),'guards':self.guards,
   'actual_complete_original_proof_read':True,'actual_complete_proposed_proof_read':False,
   'source_application_pending':True,'events_added':0,
   'guard_validation':{'exact_application':True,'all_statement_labels_tags_preserved':True,'proof_count_preserved':True}})

e=Edit('03IC');e.standard('The pair-of-pants defect class');e.enum()
e.r(r'\CompendiumRef{I}{mapsI:top:prop:geometric-pi1}',r'\CompendiumRef{I}{inv:src:B.3.1}', 'D06','Bind the zero-section lifts to the current full based-loop construction; use its zero-section relation, without importing its separate covering conclusion.')
e.r('whose affine regluing class is $\u03bc=0$','whose affine regluing class is $\u03bc=0$','D13','Unreachable Unicode guard') if False else None
e.r('whose affine regluing class is $\\mu=0$ (equivalently\n$\\ell_0=\\gamma(\\mu)=0$);','whose affine regluing class is $\\mu=0$, hence\n$\\ell_0=\\gamma(\\mu)=0$;','D13,D25','State the actual implication through the homomorphism gamma, without asserting its unproved converse.')
e.r('whose class records\n$c_1(L|_{J_P})-[\\Omega_E]$.','whose class records\n$c_1(L|_{J_P})-[\\Omega_E]$.  Here $A_g$ is the linear part of the\nleft deck action $(b,x)\\mapsto(gb,A_gx)$, and\n$T_g=(A_g^{-1})^{\\mathsf t}$ is its action on coefficient covectors.\nA clockwise loop lifts from $b$ to $gb$; the endpoint return map $g^{-1}$\nacts on homology by $A_g^{-1}$ and on cohomology by $A_g^{\\mathsf t}=T_g^{-1}$.\nThe crossed-homomorphism convention above uses the left deck action $T_g$.','D13,D25','Specify the deck-module action and the exact inverse endpoint-return map; this corrects the ambiguous use of monodromy without changing the crossed law.')
e.r('fixed by every monodromy\n$T_g$','fixed by every deck coefficient action\n$T_g$','D13','Use the stated left deck-module convention.')
e.r(r'\cite[Chapter~III, \S1, Exercise~2, p.~60; Chapter~IV, \S2, pp.~88--89]{Brown1982}',r'\cite[Example~3.5, p.~4]{SchnellLecture3}','D06,D18','Use the actually read primary crossed/principal-homomorphism calculation, with its explicit cochain differential.',2)
e.r('For completeness, the slant convention in \\eqref{wbII:eq:W:5.17j\'} is part of this\nidentification, not an additional geometric assertion.  Give','For the slant convention in \\eqref{wbII:eq:W:5.17j\'}, give','D02,D08','Introduce the exact orientation computation directly.')
e.r(r'\langle\beta_s,\nu\rangle,ds',r'\langle\beta_s,\nu\rangle\,ds','D23','Correct the differential-spacing punctuation.')
e.r("This proves \\eqref{wbII:eq:W:5.17j'}.\n",'','D08','Remove the closing announcement after the complete slant calculation.')
e.r(r'\CompendiumRef{I}{wb:prop:monodromy-certificate}',r'\CompendiumRef{I}{def:common-conventions}','D06','Point to the current displayed integral matrices.')
e.r('=0,\n\\]\nwhich proves the final assertion.','=0.\n\\]', 'D08','Remove the empty final-assertion recap after the vanishing formula.')
e.save()

e=Edit('03IE');e.standard('The finite-cover norm identity');e.enum()
e.r(r'\cref{wbII:lem:picard-crossed-defect}; \CompendiumRef{I}{wb:prop:candidate-finite-fillings}.',r'\cref{wbII:lem:picard-crossed-defect} and the normalized root covers in \CompendiumRef{I}{fam:src:A.1.2}.','D06','Bind the finite root cover to its current owning proposition.')
e.r('This is the cohomological pullback of the annular defect to the\n$s_j$-cover; the norm, rather than unqualified multiplication by $m_j$, is\nessential before passage to global coinvariants.','This is the cohomological pullback of the annular defect to the\n$s_j$-cover, expressed by the norm $N_{T_j}$.','D02','State the precise pullback map positively.')
e.r('The second equality is the actual radial/stalk identification in\n\\CompendiumRef{I}{wb:lem:finite-filling-stalk-map};','The second equality follows from the normalized root cover in\n\\CompendiumRef{I}{fam:src:A.1.2} and the radial restriction above;','D06,D08','Retain the explicit radial identification and its current root-cover source.')
e.r('On $\\Delta_j^*$, the source identity','On $\\Delta_j^*$, the connector in\n\\CompendiumRef{I}{pub:I:eq:PD8} satisfies the identity','D06,D08','Bind the actual logarithmic connector formula instead of referring to a source identity.')
e.r('On a branch of the logarithm the actual real\ntranslation vector is','On a branch of the logarithm the real\ntranslation vector is','D08','Remove the process qualifier while retaining the exact real-complex comparison.')
e.r('Complex multiplication by $\\alpha$ is\nnot multiplication by a real scalar in this marking.','The two real components in \\eqref{wbII:eq:W:5.17m} map under $\\Pi(s)$ to\n$\\alpha(s)\\Pi(s)v_j$.','D02','State the explicit morphism between the real marking and complex translation, retaining both components.') if False else None
e.r('Complex multiplication by \\(\\alpha\\) is\nnot multiplication by a real scalar in this marking.','The real and imaginary parts in \\eqref{wbII:eq:W:5.17m} therefore give\nthe translation in the real marking.','D02','Retain the preceding explicit Pi map and both real components while removing a repeated negative formulation.')
e.r('  This proves \\eqref{wbII:eq:W:5.17k}, with the\noriginal clockwise convention and no change to either translation\nvector.','', 'D08','Remove the closing verification announcement; all norm equations and clockwise lift calculations remain.')
e.save()

e=Edit('03ID');e.standard('The cusp boundary defect and Chern-class specialization');e.enum()
e.r('This is the zero-section\nsweep: there is no hidden vertical drift in $\\widetilde a_0$, by the\nexplicit overlap calculation in \\CompendiumRef{I}{mapsI:top:prop:geometric-pi1}.','The zero-section\nlift $\\widetilde a_0$ has constant fibre coordinate by the overlap\ncalculation in \\CompendiumRef{I}{inv:src:B.3.1}.','D02,D06','State the actual zero-section coordinate and current based-loop input.')
e.r('with\nthe unimodular cusp chart','with\nthe unimodular cusp chart of \\CompendiumRef{I}{mapsI:src:A.1.2}','D06','Bind the explicit coordinates and delta action to the current chart proof.')
e.r('The literal solid torus','The solid torus','D08','Remove a process qualifier from the explicit solid torus.')
e.r('  No reduced\nMayer--Vietoris block or Leray comparison is used here.','', 'D02,D08','Remove a method-scope announcement after the orientation comparison.')
e.r(r'\CompendiumRef{I}{wb:thm:coinvariants}',r'\cite[Proposition~7.26, pp.~61--62]{AC2026}','D06,D18','Use the exact primary integral coinvariant calculation transported by the identical marked construction.')
e.r('  This proves \\eqref{wbII:eq:W:5.17n}.','', 'D08','Remove the final equation recap after its complete vanishing argument.')
e.r('recalled in the proof of\n\\CompendiumRef{I}{mapsI:top:thm:p0-integral-specialization}','in \\cite[Theorem~B.1, pp.~101--105, especially (N1)--(N2), p.~101]{AC2026}','D06,D18','Bind the nearby-cycle unit and natural specialization to the primary theorem actually read in full.')
e.r('  This proves the claimed\nnaturality without using any global Leray differential.','', 'D02,D08','Remove a closing method-scope recap after the exact naturality map.')
e.save()

e=Edit('03IL');e.standard('Direct boundary-Picard vanishing');e.enum()
e.r('This proof is independent of the global Leray transgressions\n$d_2^{0,q}$ and of the packaged conclusion $H^2(X;\\mathbb Z)=0$; it uses\nonly the actual finite-filling lattices, their logarithmic overlap maps, the\nbased boundary relation, the local cusp solid torus, and the local integral\nspecialization theorem.\n','', 'D02,D08','Remove the proof-method inventory after the complete mathematical statement.')
e.r(r'\CompendiumRef{I}{wb:thm:coinvariants}',r'\cite[Proposition~7.26, pp.~61--62]{AC2026}','D06,D18','Bind the common invariant lattice to the exact primary computation.')
e.r('actual specialization lattice','specialization lattice','D08','Remove the process adjective.')
e.r(r'of \CompendiumRef{I}{wb:prop:finite-indices}; \CompendiumRef{I}{wb:lem:finite-filling-stalk-map}.',r'of \cite[Lemma~A.4, pp.~99--100]{AC2026}, through the normalized cover of \CompendiumRef{I}{fam:src:A.1.2}.','D06,D18','Retain the stronger integral parity input and bind the exact finite covering map.')
e.r('Now combine the balance relation','Combine the balance relation','D08','State the algebraic operation directly.')
e.r(r'\CompendiumRef{I}{mapsI:top:thm:p0-integral-specialization}',r'\cite[Theorem~B.1, pp.~101--105]{AC2026}','D06,D18','Use the primary integral specialization theorem, including injectivity, rather than a nonexistent current owner label.')
e.save()

e=Edit('03IM');e.standard('Leray-edge vanishing of normalized cusp restrictions');e.enum()
e.r('This proof does not invoke the packaged conclusion\n$H^2(X;\\mathbb Z)=0$.\n','', 'D02,D08','Remove a method-scope announcement after the mathematical conclusion.')
e.r('First record explicitly the compatibility used here.  For every $b\\in B$,','For every $b\\in B$,','D08','Remove the opening announcement while retaining the complete square.')
e.r(r'\cite[Theorem~2.3.26]{Dimca2004}',r'\cite[Tag~09V6]{StacksProject}','D06,D18','Use the actually read topological proper-base-change lemma for the underlying proper map.',2)
e.r('and analytic proper base\nchange','and topological proper base\nchange','D13,D18','Name the exact primary theorem being applied to the underlying proper map.')
e.r('For the constructed\ncandidate, \\CompendiumRef{I}{mapsI:top:prop:leray-e2}; \\CompendiumRef{I}{mapsI:top:lem:higher-transgressions} give','For the standard family, \\cite[Propositions~7.26--7.27, pp.~61--63]{AC2026}\ngive $E_2^{0,2}=\\mathbb Z(2q)$ and\n$E_2^{2,1}=\\mathbb Z\\,\\omega_{\\rm AC}[\\delta]$, with\n$d_2^{0,2}(2q)=\\varepsilon p\\,\\omega_{\\rm AC}[\\delta]$,\nwhere $\\varepsilon\\in\\{1,-1\\}$ is the common differential sign and\n$p=12\\ell_0-4\\ell_1-3\\ell_2=-1$.\nDefine the generator $\\omega:=\\varepsilon p\\,\\omega_{\\rm AC}$; equivalently,\n$\\omega[\\delta]$ is the actual element $d_2^{0,2}(2q)$.  It is primitive\nbecause $\\varepsilon p\\in\\{1,-1\\}$.  With this generator,','D06,D13,D18','Bind the exact primary E2/differential and define the previously unspecified generator by the actual primitive image; do not assert an uncomputed numerical sign.')
e.save()

e=Edit('03DR');e.standard('Application to the standard threefold');e.single()
e.r(r'\CompendiumRef{I}{wb:thm:candidate-global-geometry}',r'\CompendiumRef{I}{fam:src:A.3.1}','D06','Bind the standard proper holomorphic construction to the current family proposition.')
e.r('The cusp construction gives the compact full Cartier fibre, its\n$\\mathrm{dP}_6$ normalization, and the local trivialization of $\\omega_X$.','The cusp charts in \\CompendiumRef{I}{push:src:E.3.1} give the compact\nfull Cartier fibre and its $\\mathrm{dP}_6$ normalization.  The isomorphism\n$\\omega_X\\simeq\\mathcal O_X(-2S_2)$ in\n\\CompendiumRef{I}{fam:src:A.1.1} trivializes $\\omega_X$ near $W$, since\n$W$ and $S_2$ lie over distinct base points.','D06,D13','Bind the exact full fibre, normalization and local canonical trivialization used in the previously checked DS chain.')
e.r('  This is exactly\nthe chain proved in','  This chain is proved in','D08','Remove a verification qualifier while retaining its precise dependency.')
e.r('}, now with the all-Pic\nrestriction supplied directly by','}, with the all-Pic\nrestriction supplied by','D08','State the dependency without a process transition.')
e.r('The\nglobal Leray-edge proof in \\cref{wbII:prop:leray-edge-restriction} is an\nindependent certificate of the same restriction statement.','The restriction also follows from\n\\cref{wbII:prop:leray-edge-restriction}.','D08','Retain the alternate mathematical implication and its reference without a verification-certificate claim.')
e.save()

e=Edit('03IW');e.standard('Analytic vanishing of the global restriction');e.single()
e.r('is the zero homomorphism.  This proof uses only holomorphic\n\\(\\mathcal O^*\\)-factors, the two finite logarithmic fillings, the cusp\nargument principle, and the \\(\\Psi\\)-equivariant toric support function.\nIt uses neither a global integral Leray transgression nor local integral\nnearby-cycle specialization.','is the zero homomorphism.','D02,D08','Remove the method inventory after the complete restriction-map conclusion.')
e.r(r'\CompendiumRef{I}{wb:thm:coinvariants}',r'\cite[Proposition~7.26, pp.~61--62]{AC2026}','D06,D18','Bind the invariant fibre lattice to the exact primary result.')
e.r('The exact contractions, now used without an integral specialization\nlattice, are','The contractions are','D02,D08','Introduce the unchanged exact contraction formulas directly.')
e.r('This holds for every \\(L\\), proving \\(r=0\\).\n','', 'D08','Remove the closing recap after the quantified line-bundle conclusion.')
e.save()

e=Edit('03IN');e.standard('An explicit nonzero local cusp restriction');e.enum()
e.r('\\item \n\\noindent\\textbf{Step 1. Local finiteness and Cartier status.}','\\item \\emph{Local finiteness and Cartier status.}','D04,D23','Make each proof step a single ordinary enumerated item.')
for n,title in [(2,'The signed divisor pullback identity.'),(3,'The complete \\(\\Psi\\)-cocycle.'),(4,'Analytic descent.'),(5,'The normalized central restriction.'),(6,'The generic-fibre factor and its exact Chern class.')]:
 e.r(f'\\noindent\\textbf{{Step {n}. {title}}}',f'\\item \\emph{{{title}}}','D04,D23','Replace the manually numbered heading by an ordinary proof item.')
e.r(r'\CompendiumRef{I}{wb:thm:candidate-cusp-geometry}',r'\CompendiumRef{I}{mapsI:src:A.1.2}','D06','Bind unimodular cusp charts to the current owning proposition.',1) if False else None
# The two uses require different precise current scopes.
e.r('Every triangle of the fan is unimodular, as proved in\n\\CompendiumRef{I}{wb:thm:candidate-cusp-geometry}.','Every triangle of the fan is unimodular, as in\n\\CompendiumRef{I}{mapsI:src:A.1.2}.','D06','Bind the exact unimodular chart and height-one fan.')
e.r('This proves a complete equivariance datum, not merely invariance of the\ndivisor class.\n','', 'D02,D08','Remove the recap after the complete displayed theta cocycle.')
e.r('By \\CompendiumRef{I}{wb:thm:candidate-cusp-geometry}, the action on \\(Y_\\epsilon\\) is','The cusp action of \\CompendiumRef{I}{pub:I:eq:PD11}, proved in\n\\CompendiumRef{I}{fam:src:A.3.1}, is','D06','Bind the full C(t)-dependent action and its proved freeness/proper discontinuity.')
e.r('Hence \\eqref{wbII:eq:W:5.17ax} is exactly \\(-2q\\), as asserted.','Hence \\eqref{wbII:eq:W:5.17ax} is \\(-2q\\).','D08','Remove the assertion recap while retaining the exact Chern-class identification.')
e.save()

e=Edit('03IH');e.standard('Analytic Appell--Humbert boundary cocycle');e.enum()
e.r(r'\CompendiumRef{I}{mapsI:top:prop:geometric-pi1}',r'\CompendiumRef{I}{inv:src:B.3.1}','D06','Bind the zero-section whiskers and actual based relation to their current construction.')
e.r('\\cite[Chapter~1, \\S2, pp.~5--8, especially\nTheorem~2.1, p.~7]{BirkenhakeLange1999}; ','','D06,D18','Remove an unopened precise book locator; the immediately following actually read Schnell factor calculation supplies the same stated input.')
e.r('calculation \\cite[Chapter~1, \\S2, pp.~5--8, especially\nTheorem~2.1, p.~7]{BirkenhakeLange1999}%\n\\cite','calculation\n\\cite','D06,D18','Use the actually read primary factor calculation without an unverified redundant book-page claim.')
e.r('\\tag{W.94}\\hypertarget{tag-03EY}{}\\label{wbII:eq:W:5.17-A2}\n\\]\n','\\tag{W.94}\\hypertarget{tag-03EY}{}\\label{wbII:eq:W:5.17-A2}\n\\]\nHere $A_g$ is the linear part of the left deck action and $T_g=A_g^{-\\mathsf t}$\nis its coefficient action.  A clockwise loop ends at the deck translate $g$;\nits endpoint return $g^{-1}$ acts on homology by $A_g^{-1}$ and on\ncohomology by $A_g^{\\mathsf t}=T_g^{-1}$.  The cocycle below uses $T_g$.\n','D13,D25','Specify the exact left deck-module action and the inverse endpoint-return map without changing any cocycle formula.')
e.r('These identities are obtained from holomorphic transition factors and the\nargument principle.\n','', 'D08','Remove the method announcement after the complete identities.')
e.r('For the order-\\(m_j\\) filling, distinguish every covering level.  Put','For the order-\\(m_j\\) filling, put','D08','Introduce the specified covers directly.')
e.r('and (2.8f):','and \\CompendiumRef{I}{pub:I:eq:PD7}:','D06','Replace the literal historical equation number with the current finite-root action.')
e.r('constructed in (2.9d) satisfies, on this quotient level,','constructed in \\CompendiumRef{I}{pub:I:eq:PD8} satisfies','D06,D08','Bind the exact logarithmic connector and retain its conjugacy equation.')
e.r('hence the exactly typed\nline-bundle square gives','hence the\nline-bundle square gives','D08','Remove a process adjective from the explicitly displayed square.')
e.r('For the factor extension return to the filled vector cover.  Let','On the filled vector cover, let','D08','State the domain directly.')
e.r('This specifies every group and comparison\nmap used in the norm computation.\n','', 'D08','Remove the closing roadmap after all comparison maps are displayed.')
e.r('Choose \\(x_j\\in J_j^{\\prime *}\\) such that\n\\(p_{j,\\mathrm{lin}}(h_j(x_j))=\\gamma_j^J(0)\\), put\n\\(x_{j,\\mathrm{lin}}=h_j(x_j)\\), and let','Choose a root point $s_j$ over the initial base point and a logarithm\nbranch $\\alpha=\\log s_j/(2\\pi i)$.  For the vector-cover connector\n$H_j(s,\\zeta)=(s,\\zeta+\\alpha(s)\\Pi(s)v_j)$, set\n\\[\n \\widetilde x_j=(s_j,-\\alpha(s_j)\\Pi(s_j)v_j),\\qquad\n x_j=r_j^*(\\widetilde x_j),\\qquad x_{j,\\mathrm{lin}}=h_j(x_j).\n\\]\nThus $H_j(\\widetilde x_j)=(s_j,0)$ and\n$p_{j,\\mathrm{lin}}(x_{j,\\mathrm{lin}})=\\gamma_j^J(0)$.  Let','D13,D25','Select the precise zero-section vector lift required by the claimed point-valued endpoint; an arbitrary lattice-shifted lift changes the endpoint deck element by conjugacy.')
e.r("Choose \\(\\widetilde x_j\\in\\widetilde J_j^*\\) with\n\\(r_j^*(\\widetilde x_j)=x_j\\), and let\n\\(\\widetilde\\gamma_{j,\\mathrm{vec}}\\) be the \\(r_j^*\\)-lift of\n\\(\\widetilde\\gamma_{j,\\log}\\) beginning at \\(\\widetilde x_j\\).  On\nadjacent sheets choose compatible logarithm branches \\(\\ell,\\ell'\\) with\n\\[\n \\ell'(w)=\\ell(g_j^{-1}w)-\\frac{2\\pi i}{m_j}.\n\\]\nThe calculation in (2.9e) gives the point-valued endpoint formula",'Let $\\widetilde\\gamma_{j,\\mathrm{vec}}$ be the $r_j^*$-lift of\n$\\widetilde\\gamma_{j,\\log}$ beginning at the selected $\\widetilde x_j$.\nFor the clockwise lift, $\\alpha_1=\\alpha_0-1/m_j$.  Writing\n$\\zeta_0=-\\alpha_0\\Pi(s_j)v_j$, period equivariance and $A_jv_j=v_j$ give\n\\[\n \\zeta_1=-(\\alpha_0-1/m_j)\\Pi(g_js_j)v_j\n =R_{g_j}(s_j)\\zeta_0+\\Pi(g_js_j)v_j/m_j.\n\\]\nBy \\CompendiumRef{I}{pub:I:eq:PD7}, this gives','D06,D13,D25','Prove the selected lift endpoint directly from the current connector, period equivariance, and clockwise branch change.')
e.r('excluding both \\(Q_{j,\\log}^{-1}(\\widetilde x_j)\\) and every\n\\(\\tau_\\lambda Q_{j,\\log}(\\widetilde x_j)\\) with \\(\\lambda\\ne0\\).\n','for this selected vector lift.\n','D13,D25','Restrict the exact endpoint formula to the selected lift; arbitrary lifts are explicitly conjugate in the separate comparison record.')
e.r('The factor of \\(L\\) along the fixed lift of \\(\\omega_j\\) identifies the','Lift $\\omega_j$ along the zero section on the linear cover and use\n$H_j^{-1}$ at its local endpoint; this gives the selected\n$\\widetilde x_j$ above.  The factor of $L$ along this fixed lift identifies the','D13,D25','Bind the whisker comparison to the selected vector lift, preserving the actual based boundary element.')
e.r('It remains to obtain \\eqref{wbII:eq:W:5.17-A6} analytically.  Since','Since','D08','Remove the roadmap before the actual cusp commutator computation.')
e.r('Use the actual unimodular cusp chart','Use the unimodular cusp chart of \\CompendiumRef{I}{mapsI:src:A.1.2}','D06,D08','Bind the exact cusp chart and remove the process adjective.')
e.r('In the basis\n\\((a_u,m_{x_2})\\), the base and fibre loops are','In the basis\n$ (a_u,m_{x_2}) $, the counterclockwise base loop $b_+$ and the fibre loop are','D13,D25','Separate the positive theta parametrization from the fixed clockwise based meridian.')
e.r(' b=a_u,\n \\qquad\n f=m_{x_2}-a_u,\n \\qquad\n b\\wedge f=a_u\\wedge m_{x_2}.',' b_+=a_u,\n \\qquad\n f=m_{x_2}-a_u,\n \\qquad\n b_+\\wedge f=a_u\\wedge m_{x_2}.','D13,D25','Keep the exact change-of-basis formula for the positively oriented theta loop.')
e.r('The change-of-basis determinant is \\(+1\\), so this preserves the\nbase-first orientation in \\eqref{wbII:eq:W:5.17-A17}.  Now \\(m_{x_2}\\) does bound the','The determinant of this change of basis is $+1$.  The clockwise loop in\n\\eqref{wbII:eq:W:5.17-A17} is $b=-b_+$, so\n$b\\wedge f=-a_u\\wedge m_{x_2}$.  The winding computed below is zero\nin either orientation.  The loop $m_{x_2}$ bounds the','D13,D25','Give the exact orientation reversal and retain the zero-winding conclusion without an unnamed sign convention.')
e.r('For completeness, the exponential sequence is','The exponential sequence is','D08','Remove an editorial completeness qualifier.')
e.r('  This is a calculation in\n\\(\\mathcal O^*\\), not an evaluation of a Chern class on a bounding chain.','', 'D02,D08','Remove the method-scope comparison after the full holomorphic-frame calculation.')
e.r('  This proves \\eqref{wbII:eq:W:5.17-A6}.','', 'D08','Remove the final equation recap after its full vanishing argument.')
e.save()

e=Edit('03I6');e.standard('The toric support function detects central restriction');e.enum()
e.r('Propositions~4.1.1--4.1.2, p.~171; Theorems~4.2.8,\np.~181 and~4.2.12, p.~184','2010 text, Propositions~4.1.1--4.1.2, p.~171; Theorems~4.2.8,\np.~181 and~4.2.12, p.~184','D06,D18','State the exact 2010 edition whose indexed primary statements and proofs have the displayed locators.',2)
e.r('Example~1.2.21, p.~31','2010 text, Example~1.2.21, p.~31','D06,D18','Pin the smooth-cone chart example to the verified 2010 text.',2)
e.r('genuine\n\\(\\Psi\\)-equivariant','\\(\\Psi\\)-equivariant','D08','Remove the process qualifier; the descent map is explicitly stated.')
e.r('The genuine descent structure','The descent structure','D08','Remove the process qualifier from the stated descent structure.')
e.r('No cocycle assertion for these individual isomorphisms is needed: we use\nthem only to separate the horizontal winding of the genuine descent factor\nof \\(\\mathcal M\\).','These individual isomorphisms separate the horizontal winding of the\ndescent factor of $\\mathcal M$ in the tensor-product map below.','D02,D08','State precisely the use of the individual character maps without asserting an unproved cocycle for them.')
e.r('compare the author preprint','compare','D18','Use the explicitly pinned bibliographic edition instead of describing a supplied source.')
e.r('We also need to compare these frames on the generic torus.  The direction\nof the toric affine-open inclusions is essential here.  If','For the comparison of these frames on the generic torus, let','D08','Introduce the exact comparison construction directly.')
e.r('adjacent vertices, choose a triangle','adjacent vertices and choose a triangle','D23','Complete the revised grammatical construction.')
e.r('The space \\(S_\\sigma\\) is nevertheless the required comparison chart.  It\nis the closed graph','The space $S_\\sigma$ is the closed graph','D08','Introduce the exact Stein chart without a process transition.')
e.r('On their actual common\ndomain','On their common\ndomain','D08','Remove a process adjective while retaining the exact open intersection.')
e.r('now gives','gives','D08','State the connected-fan multiplication directly.')
e.r('be the genuine descent isomorphism','be the descent isomorphism','D08','Remove the process adjective from the specified morphism.')
e.r('by the typed identity','by the identity','D08','Remove a process adjective from the fully typed displayed map.')
e.r('  This is \\eqref{wbII:eq:W:5.17-A22}.','', 'D08','Remove the final equation recap after the exact Picard conclusion.')
e.save()

bibs=[]
for key in ['SchnellLecture3','Cartan1957','StacksProject']:
 m=re.search(r'\\bibitem(?:\[[^\]]*\])?\{'+key+r'\}',canonical);assert m
 end=re.search(r'\\bibitem|\\end\{thebibliography\}',canonical[m.end():]);old=canonical[m.start():m.end()+end.start()]
 new=old.replace('\\newblock \\emph{Verified}.\n','')
 if key=='Cartan1957':new=new.replace('\\newblock URL','\\newblock \\doi{10.24033/bsmf.1481}.\n\n\\newblock URL',1)
 assert old!=new
 a=D/f'S6_SERIES_PUBLISH_II_bib_{key}_original.tex';b=D/f'S6_SERIES_PUBLISH_II_bib_{key}_proposed.tex';a.write_text(old);b.write_text(new)
 bibs.append({'key':key,'change_id':f'II-REC-C10-BIB-{key}','defect_type':'D18,D08','old':old,'new':new,'expected_occurrences':1,'reason':'Remove verification status from the published bibliography; Cartan additionally receives its primary Numdam DOI.','original':bind(a),'proposed':bind(b),'actual_full_pair_read':False})

out={'schema_version':1,'paper':'II','checker':'i_provenance_recovery','created_utc':now(),'source_at_preparation':bind(source),'targets':targets,'bibliography_guards':bibs,'canonical_mutations':0,'events_added':0,'status':'Exact proposals prepared; complete proposed-proof rereading and final source/primary/evidence binding pending.'}
dump(D/'S6_SERIES_PUBLISH_II_clean_group10_preparation.json',out)
print(json.dumps({'targets':len(targets),'guards':sum(len(t['guards']) for t in targets),'bibliography':len(bibs),'preparation':bind(D/'S6_SERIES_PUBLISH_II_clean_group10_preparation.json')}))
