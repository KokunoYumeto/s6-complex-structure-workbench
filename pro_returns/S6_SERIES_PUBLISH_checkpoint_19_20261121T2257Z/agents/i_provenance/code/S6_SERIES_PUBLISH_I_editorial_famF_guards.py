import pathlib,json,re,hashlib,datetime,csv
R=pathlib.Path('/workspace/scratch/653608133b22/work/agents/i_provenance')
meta=json.loads((R/'S6_SERIES_PUBLISH_I_editorial_intake.json').read_text()); S=pathlib.Path(meta['snapshot']).read_text(); C=(R/'S6_SERIES_PUBLISH_I_editorial_famF_old.tex').read_text();changes=[]
def add(id,old,new,scope,reason,defects='D01,D02,D04,D05,D08,D09,D13'):
 assert S.count(old)==1,(id,S.count(old));assert old in C,id
 changes.append(dict(id=id,old=old,new=new,expected_count=1,statement_id=scope,reason=reason,defect_types=defects))
# Number all setup definitions without changing their formulas.
a=C.index('We use the clockwise');b=C.index('\\subsection{An exact arithmetic description}')
old=C[a:b];new=old.replace('We use the clockwise root deck generators and the lattice basis specified\non the first page.  In this section a group acts properly discontinuously when, for every','We use the clockwise root deck generators and lattice basis of\nDefinition~\\ref{def:common-conventions}. A group acts properly\ndiscontinuously when, for every').replace('The domain $\\mathcal D$ consists','The period domain $\\mathcal D$ consists').replace('It is the stated\n$\\operatorname{Sp}_4(\\mathbb R)/U(1,1)$','It is\n$\\operatorname{Sp}_4(\\mathbb R)/U(1,1)$')
new='\\begin{definition}[The period domain and proper discontinuity]\\hypertarget{tag-IP01}{}\\label{I:def:period-domain}\n'+new.rstrip()+'\n\\end{definition}\n\n'
add('I-F-number-period-domain',old,new,'I:def:period-domain','Number the existing definitions and replace the unstable first-page pointer by its exact convention label.','D04,D05,D13')
a=C.index('Define the real-analytic function');b=C.index('\\begin{proposition}[counterexample]',a);old=C[a:b];new='\\begin{definition}[The sign domains]\\hypertarget{tag-IP02}{}\\label{I:def:period-sign-domains}\n'+old.replace('Define the real-analytic function','Put').rstrip()+'\n\\end{definition}\n\n'
add('I-F-number-sign-domains',old,new,'I:def:period-sign-domains','Number q_e, O and its sign regions with the existing invariance explanation.','D13')
titles=[('theorem','01R9','fam:src:F.1.1','The integral monodromy group'),('proposition','01RA','fam:src:F.1.2','The center and the Zariski closure'),('theorem','01RC','fam:src:F.2.2','The maximal domain of proper discontinuity'),('proposition','01RD','fam:src:F.2.3','A global chart for positive periods'),('theorem','01RE','fam:src:F.3.1','The embedded period curve'),('proposition','01RF','fam:src:F.3.2','Finite limits and the cusp limit'),('proposition','01RG','fam:src:F.3.3','The determinant of the period derivative')]
for env,tag,label,title in titles:
 old='\\begin{'+env+'}\\hypertarget{tag-'+tag+'}{}\\label{'+label+'}'
 new='\\begin{'+env+'}['+title+']\\hypertarget{tag-'+tag+'}{}\\label{'+label+'}'
 add('I-F-title-'+label.split(':')[-1],old,new,label,'Add a short mathematical title; all identifiers remain.','D13')
add('I-F-title-stabilizer','\\begin{proposition}[counterexample]\\hypertarget{tag-01RB}{}','\\begin{proposition}[An infinite stabilizer]\\hypertarget{tag-01RB}{}','fam:src:F.2.1','Title the constructed infinite stabilizer positively.','D02,D13')
add('I-F-monodromy-prose','With $Q(x)=x_1+x_2+x_1x_2$, the actual monodromy group is','With $Q(x)=x_1+x_2+x_1x_2$, the monodromy group is','fam:src:F.1.1','Remove process emphasis from the exact group formula.','D08')
a=C.index('\\item The matrices in the stated problem');b=C.index('Multiplication gives $A_1^3=A_2^4=I$',a)
add('I-F-canonical-matrices',C[a:b],'\\item Use the matrices $A_1,A_2$ of \\eqref{wb:pshift:eq:finite-data}.\n','fam:src:F.1.1','Use the identical matrices already printed in the common conventions. Every subsequent multiplication and generation step remains.','D05,D12')
add('I-F-presentation-prose','\\item For completeness, the presentation of the Levi group needed here follows\nfrom an elementary action on the real projective line.','\\item The presentation of the Levi group follows from its action on the\nreal projective line.','fam:src:F.1.1','Remove introductory bookkeeping while preserving the entire action/presentation argument.','D08')
add('I-F-kernel-prose','\\item We verify equality with its kernel; containment alone would not determine\nthe group.','\\item We prove $\\Gamma=\\ker\\chi$.','fam:src:F.1.1','State the exact equality proved in this step.','D02')
add('I-F-extension-prose','This proves associativity as well as the claimed abstract\ndescription, without leaving an unspecified extension class.','This proves associativity and identifies the central extension with the\ndisplayed cocycle.','fam:src:F.1.2','State the explicit comparison supplied by the bijection.','D02')
add('I-F-positive-stabilizer','The assertion that $\\Gamma$ acts properly discontinuously on all of\n$\\mathcal D$ is false.  The following point of $\\mathcal D$ has an\nexplicit infinite stabilizer:','The following point of $\\mathcal D$ has an infinite $\\Gamma$-stabilizer:','fam:src:F.2.1','Keep the exact counterexample and its consequence in the proof, without referring to a proposed assertion.','D01,D02')
old='''The compact singleton $\\{J_0\\}$ therefore violates
the stated definition of proper discontinuity.  The fresh exact SymPy calculation in
\\path{code/current_audits/audit_paper_i/code/period_curve_exact.py}
checks these matrices, their eigenvalues, the actual group lift and the
universal identity \\((I+mN)(I+nN)=I+(m+n)N\\).
Its output is
\\path{code/current_audits/audit_paper_i/code/period_curve_exact.output.json}.'''
new='''The identity $N^2=0$ also gives
\\((I+mN)(I+nN)=I+(m+n)N\\). The compact singleton $\\{J_0\\}$ meets every one of its translates by
$R^m$, so the action on $\\mathcal D$ is not properly discontinuous.'''
add('I-F-stabilizer-program-record',old,new,'fam:src:F.2.1','The full exact matrix argument remains; move the independent diagnostic program and output to the program/check mapping.','D08,D09')
add('I-F-maximality-prose','\\item It remains to prove maximality, which requires more than one bad point.','\\item We prove maximality by exhibiting a dense set of points with infinite\nstabilizer in the zero locus of $q_e$.','fam:src:F.2.2','Name the precise argument supplied by the following steps.','D02')
add('I-F-period-chart-pointer','represented by the matrix $\\Pi$ in the stated problem.  In this chart,','represented by the period matrix \\eqref{wb:pshift:eq:periods}, with\n$\\beta_c$ replaced by the coordinate $\\beta$. Put\n$D=\\Im\\beta-6(\\Im\\mu)^2/\\Im\\tau$. In this chart,','fam:src:F.2.3','Give the exact matrix reference and define the determinant scalar used in the displayed formula.','D05,D13')
add('I-F-admissibility-pointer','The admissibility\ninequality in the stated problem is $D_c<0$ everywhere, which proves the last\nassertion by this exact comparison map.','The admissibility\ninequality of Definition~\\ref{I:def:family-parameter} is $D_c<0$\neverywhere, so the displayed comparison map places every admissible\nperiod in $\\mathcal O_+$.','fam:src:F.2.3','Replace a prompt pointer with the exact existing definition and its comparison map.','D05')
add('I-F-elliptic-model-pointer','The elliptic curve\nwhose period is $\\tau$ has the equation stipulated in the stated problem,','The elliptic curve\nwhose period is $\\tau$ has the Engel equation of\nLemma~\\ref{I:weierstrass-comparison},','fam:src:F.3.1','Identify the model through the explicit coordinate comparison already proved.','D05')
old='''Equivalently this is the defining lift of the elliptic modular map used
for $\\tau$ in the period construction.  The discriminant, exact cancellation and derivative of
\\(j/1728\\) are checked by
\\path{code/current_audits/audit_paper_i/code/period_curve_exact.py},
with exact output in
\\path{code/current_audits/audit_paper_i/code/period_curve_exact.output.json}.  In a local base coordinate $t$, the'''
new='''In a local base coordinate $t$, the'''
add('I-F-j-program-record',old,new,'fam:src:F.3.1','Retain the exact displayed discriminant and cancellation argument; archive the independent diagnostic and its output in the check records.','D08,D09')
add('I-F-root-coordinate-pointer','after choosing local coordinates as in the stated problem.','in the root coordinates of Definition~\\ref{def:common-conventions}.','fam:src:F.3.1','Replace a prompt reference by the exact root-coordinate definition.','D05')
add('I-F-Z-definition','The determinant used in the workbench is generically nonzero, with\nthe stated zero at $z_1$:','Let $Z=\\bigl(\\begin{smallmatrix}6\\mu&\\tau\\\\\\beta&\\mu\\end{smallmatrix}\\bigr)$\nbe the left block of \\eqref{wb:pshift:eq:periods}. Its derivative has\ngenerically nonzero determinant, with a zero at $z_1$:','fam:src:F.3.3','Define the exact matrix whose derivative is used and remove a workbench reference.','D04,D05,D13')
add('I-F-immersion-comparison','The immersion established in \\ref{fam:src:F.3.1} holds at every point of $B^\\circ$\nwithout requiring this determinant to be everywhere nonzero.','The period map is an immersion at every point of $B^\\circ$ by\nTheorem~\\ref{fam:src:F.3.1}; its differential and $\\det\\dot Z$ are\nrelated by the polynomial map $\\dot Z\\mapsto\\det\\dot Z$.','fam:src:F.3.3','Replace a defensive clause by the exact map relating the two quantities.','D02')
add('I-F-derivative-conclusion','The maps compared here are explicitly the\ncoordinate derivative and its determinant, and the displayed computation\nstates exactly what each supplies.','Thus the coordinate derivative is nonzero on $B^\\circ$, while its\nassociated matrix has the displayed determinant.','fam:src:F.3.3','Keep the proved relationship in mathematical language.','D08')
N=C
for c in changes:
 assert N.count(c['old'])==1,c['id'];N=N.replace(c['old'],c['new'])
(R/'S6_SERIES_PUBLISH_I_editorial_famF_new.tex').write_text(N)
base={'source':meta['source'],'source_sha256':meta['source_sha256'],'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'changes':changes,'new_tags':['IP01','IP02'],'verification':'All eight original statements and their complete old proofs read; new text constructed by exact guarded substitutions. Original labels and hypertargets preserved. No full mathematical independent verification claimed. Changed proof reread events follow separately.'}
(R/'S6_SERIES_PUBLISH_I_editorial_famF_guards.json').write_text(json.dumps(base,indent=2)+'\n')
programs=[{'program':'code/current_audits/audit_paper_i/code/period_curve_exact.py','output':'code/current_audits/audit_paper_i/code/period_curve_exact.output.json','statement_ids':['fam:src:F.2.1','fam:src:F.3.1'],'role':'Independent exact diagnostic; both mathematical calculations remain explicit in the proof. Retained in check/program mapping, not a new logical input.','pinned_path_status':'Resolve exact manifest path in aggregate program inventory; no current-run availability at old pin asserted here.'}]
(R/'S6_SERIES_PUBLISH_I_editorial_famF_program_mapping.json').write_text(json.dumps(programs,indent=2)+'\n')
print(len(changes),'guards; old/new labels equal:',re.findall(r'\\label\{[^}]+\}',C)==[x for x in re.findall(r'\\label\{[^}]+\}',N) if x not in ['\\label{I:def:period-domain}','\\label{I:def:period-sign-domains}']])
