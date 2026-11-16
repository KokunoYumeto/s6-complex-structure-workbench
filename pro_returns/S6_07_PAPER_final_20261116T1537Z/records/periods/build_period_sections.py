from pathlib import Path
import re,json,hashlib,difflib
ROOT=Path('/workspace/scratch/33c5206c0778')
OUT=ROOT/'deliverables/records/periods'
SRC=ROOT/'inputs/sources'
CTX=ROOT/'inputs/context'
paths={
 'fam': 'returns/S6_02_FAMILY/sections/CD.tex',
 'special': 'returns/S6_05_ARITHMETIC/sections/C_special.tex',
 'analytic': 'returns/S6_05_ARITHMETIC/sections/C_analytic.tex',
 'integral': 'returns/S6_05_ARITHMETIC/sections/C_integral.tex',
 'measure': 'returns/S6_05_ARITHMETIC/sections/C_measure.tex',
 'critical': 'returns/S6_05_ARITHMETIC/sections/C_critical.tex',
 'push': 'returns/S6_02_PUSH/sections/E4_push.tex',
}
texts={k:(SRC/p).read_text() for k,p in paths.items()}
records=[]
proofs=[]
changes=[]

def blocks(key):
 text=texts[key]
 pat=re.compile(r'\\begin\{(statement|proposition|theorem|corollary)\}\[(.*?)\](.*?)\\end\{\1\}',re.S)
 result={}
 for m in pat.finditer(text):
  num=re.search(r'[A-Z]\.\d+(?:\.\d+)+',m[2]).group()
  after=text[m.end():]
  pm=re.match(r'\s*\\begin\{proof\}(.*?)\\end\{proof\}',after,re.S)
  result[num]={'body':m[3].strip(),'proof':pm[1].strip() if pm else '', 'env':m[1], 'title':m[2], 'line':text[:m.start()].count('\n')+1}
 return result
B={k:blocks(k) for k in paths}

# Textual notation changes only. Mathematical expressions and all hypotheses are retained.
def adapt(s,key,num=''):
 s=re.sub(r'\\label\{st:[^}]+\}', '',s).strip()
 if key!='fam' and key!='push':
  s=re.sub(r'\\eta(?![A-Za-z_])',r'\\eta_D',s)
  s=re.sub(r'(?<![A-Za-z])N(?![A-Za-z])',lambda m:r'\mathcal N',s)
  s=re.sub(r'(?<![A-Za-z])L(?![A-Za-z])',lambda m:r'\mathcal L',s)
  s=s.replace(r'\Lambda\prime',r'\Lambda_{\mathrm{ell}}\prime')
  s=re.sub(r'\\Lambda(?![A-Za-z])',lambda m:r'\Lambda_{\mathrm{ell}}',s)
  s=s.replace(r'\Delta_\Lambda_{\mathrm{ell}}',r'\Delta_{\Lambda_{\mathrm{ell}}}')
  s=s.replace(r'\Delta_{\Lambda_{\mathrm{ell}}\prime}',r'\Delta_{\Lambda_{\mathrm{ell}}\prime}')
  s=s.replace(r'\Delta(t)',r'\Delta_{\mathrm{div}}(t)')
  s=s.replace(r'\Delta(t_0)',r'\Delta_{\mathrm{div}}(t_0)').replace(r'\Delta(\bar t_0)',r'\Delta_{\mathrm{div}}(\bar t_0)')
  s=s.replace(r'\Delta(T)',r'\Delta_{\mathrm{div}}(T)').replace(r'\Delta(S)',r'\Delta_{\mathrm{div}}(S)')
  s=s.replace(r'\Delta_0',r'\Delta_{\mathrm{mod}}')
  if key in ['special','analytic','integral','measure','critical']:
   s=re.sub(r'(?<![A-Za-z])q(?![A-Za-z_])',lambda m:r'q_\tau',s)
   s=s.replace('nq^',r'nq_\tau^')
  # All P in this run's sections is the point of the rational auxiliary model.
  s=s.replace(r'\mathbb P', 'PROJECTIVEPLACEHOLDER').replace(r'\mathbb{P}', 'PROJECTIVEPLACEHOLDER')
  s=re.sub(r'P(?![A-Za-z])',lambda m:r'P^{\mathrm{div}}',s)
  s=s.replace('PROJECTIVEPLACEHOLDER',r'\mathbb{P}')
  s=s.replace(r'P_{\mathrm{div}}_t',r'P_{\mathrm{div},t}').replace(r'P_{\mathrm{div}}_{t_0}',r'P_{\mathrm{div},t_0}').replace(r'P_{\mathrm{div}}_{\bar t_0}',r'P_{\mathrm{div},\bar t_0}')
  s=s.replace(r'm_P_{\mathrm{div}}',r'm_{P_{\mathrm{div}}}')
  s=s.replace(r'E_t:',r'E^{\mathrm{div}}_t:')
  s=s.replace('DuGuoKusakabeXie2026v1','DGKXv1')
  if key in ['measure','critical']:
   s=re.sub(r'(?<![A-Za-z])W(?![A-Za-z])',lambda m:r'\mathcal W',s)
   s=re.sub(r'(?<![A-Za-z])R(?![A-Za-z])',lambda m:r'\mathcal R_\mu',s)
   s=s.replace('iW',r'i\mathcal W').replace('iR',r'i\mathcal R_\mu')
  if key=='analytic':
   s=re.sub(r'(?<![A-Za-z])u(?![A-Za-z])',lambda m:r'v_t',s)
  if key=='integral':
   s=s.replace(r'dA_u',r'dA_{v_{\wp}}')
   s=re.sub(r'(?<![A-Za-z])u(?![A-Za-z])',lambda m:r'v_{\wp}',s)
  if key=='measure':
   s=re.sub(r'\bw\b','z_B',s)
   s=s.replace(r'\mu_w',r'\mu_{z_B}').replace(r'\tau_w',r'\tau_{z_B}').replace(r'dA_w',r'dA_{z_B}')
  if num=='C.3.2':
   s=s.replace(r'\mu_0',r'\mu_\rho')
 # Every equation label and reference keeps its source namespace.
 prefix='fam' if key=='fam' else ('push' if key=='push' else 'ari')
 s=re.sub(r'(\\(?:label|eqref|ref)\{)(eq:[^}]+)(\})',lambda m:m[1]+prefix+':'+m[2]+m[3],s)
 s=s.replace('C.1.1','ARI C.1.1') if key not in ['fam','push'] else s
 # Detailed source locators remain readable even where no local reprint is needed.
 for old,new in [('R5','FAM A.4.1 and A.5.1'),('R4','FAM C.2.3'),('R3','FAM C.1.1'),('K6','FAM C.2.3'),('K3','ARI C.3.1'),('K2','ARI C.2.1'),('K1','ARI C.1.1')]:
  s=re.sub(r'\b'+old+r'\b',new,s)
 if key=='fam':
  s=s.replace('Statement B.1.3',r'Statement~\ref{fam:B.1.3}').replace(r'(f^2\wp_\tau(v),f^3\wp',r'(f_{\rm sc}^2\wp_\tau(v),f_{\rm sc}^3\wp')
  s=re.sub(r'(?<![A-Za-z])q(?![A-Za-z_])',lambda m:r'q_\tau',s)
  s=s.replace('nq^',r'nq_\tau^')
 s=s.replace(r'_\Lambda_{\mathrm{ell}}',r'_{\Lambda_{\mathrm{ell}}}')
 s=s.replace(r'm_P^{\mathrm{div}}',r'm_{P^{\mathrm{div}}}')
 s=s.replace(r'dd^cL',r'dd^c\mathcal L')
 if key=='fam' and num=='C.1.1':
  s=re.sub(r'(?<![A-Za-z])u(?![A-Za-z])',lambda m:r'v_{\rm cusp}',s)
 if key=='fam' and num=='C.1.2':
  s=s.replace('A further sixty-digit interval computation,','\n\nA further sixty-digit interval computation,')
  s=s.replace('The exact formulas, product-tail bounds, independent algorithms, and\nfull outputs accompany the decimals.', 'The exact formulas, product-tail bounds, independent algorithms, and\nfull outputs are reported by the source run as accompanying the decimals.')
 if key=='analytic' and num in ['C.8.4','C.8.5']:
  s=re.sub(r'A_([123k])',lambda m:r'\mathcal A_'+m[1],s)
 if key=='analytic' and num=='C.8.2':
  s=re.sub(r'(?<![A-Za-z])A_([k012])',lambda m:r'\mathcal S_'+m[1],s)
 if key=='analytic' and num=='C.8.4':
  s=re.sub(r'(?<![A-Za-z])M(?![A-Za-z])',lambda m:r'M_{\rm coeff}',s)
 if (key=='special' and num=='C.3.1') or (key=='analytic' and num=='C.8.2'):
  s=re.sub(r'(?<![A-Za-z])E(?![A-Za-z_])',lambda m:r'\mathcal E_2',s)
 if key=='special' and num=='C.4.3':
  s=re.sub(r'(?<![A-Za-z])W(?![A-Za-z])',lambda m:r'W_{\rm rad}',s)
  s=re.sub(r'(?<![A-Za-z])V(?![A-Za-z])',lambda m:r'V_{\rm rad}',s)
 if key=='special' and num=='C.3.1':
  s=re.sub(r'(?<![A-Za-z])G(?![A-Za-z])',lambda m:r'G_\square',s)
  s=s.replace('iG',r'iG_\square')
  s=s.replace('A_2',r'\alpha_2').replace('A_4',r'\alpha_4')
 # Replace implementation-history sentences only: preserve mathematical proof.
 s=s.replace('This also checks the precise normalization in checkpoint ARI C.1.1;\nits kernel, Laplacian and mean-zero argument are all valid.','The kernel, Laplacian and mean-zero argument fix the normalization.')
 s=s.replace('We use the checked ARI C.1.1 calculation, rather than treat its modulus as an\nopen question:', 'By ARI C.1.1,')
 s=s.replace("We checked checkpoint ARI C.2.1's step giving $q_2=iw/216$: its factor\n$1/2$ is exactly the Albanese projection just computed. Its\nnatural-boundary proof uses modular invariance at rational boundary\npoints and is valid.", "The factor $1/2$ in $q_2=iw/216$ is exactly the Albanese projection just computed. The natural-boundary argument uses modular invariance at rational boundary points.")
 s=s.replace('same rational-cusp argument checked in ARI C.2.1.', 'same rational-cusp argument.')
 s=s.replace('The exact coefficients checked in ARI C.3.1 are','The exact coefficients are')
 s=s.replace('In particular the leading terms of ARI C.3.1 and Lead 9 are correct.','In particular the leading terms of the local expansion in the source prompt are correct.')
 s=s.replace('in K4 follow','in the source checkpoint K4 follow')
 s=s.replace('in Lead 15(b)', 'in the source request labelled Lead 15(b)')
 return s

def step_proof(s,uses):
 # Blank-line paragraph groups are source proof steps. No mathematical text is omitted.
 paras=[p for p in s.split('\n\n') if p.strip()]
 if len(s.splitlines())<=8:return '\\begin{proof}\n'+s+'\n\\end{proof}\n'
 return '\\begin{proof}\n'+'\n\n'.join('\\noindent\\textbf{Step '+str(i+1)+'.} '+p+'\n' for i,p in enumerate(paras))+'\\end{proof}\n'

priorfiles={
 'AC26':CTX/'original/AC26_transcription.tex',
 'E26':CTX/'papers/arXiv_2609.38442_Engel_src/S6.tex',
 'DGKXv1':CTX/'papers/arXiv_2610.00250v1_Du_Guo_Kusakabe_Xie.tex'}
priors={k:p.read_text() for k,p in priorfiles.items()}
searchterms={
 'theta':[r'\\vartheta_1',r'\\vartheta_3','theta quotient','Eichler','log6','216'],
 'decimals':['0.3648518319','1.2710120605','0.2110042581','cd_special_intervals','twenty decimal'],
 'Green':['distribution under isogenies','Green function','theta quotient','kernel product'],
 'nomes':['Albanese','216','27/64','48^3','bare-period'],
 'expansion':['Gamma(1/4)','half-period','fourth order','5000','E_4(i)'],
 'division':['division polynomial','psi_m','torsion locus','6016','4736'],
 'integral':['Mahler','beta integral','centroid','pushforward probability'],
 'maximum':['216','log6','duplication','19701','19911','suprem'],
 'measure':['Betti measure','equidistribution','db\\wedge da','signed Gaussian','first-derivative','star-shaped'],
}
searchlog={}
for topic,terms in searchterms.items():
 searchlog[topic]={}
 for name,text in priors.items():
  lines=text.splitlines(); hits=[]
  for term in terms:
   match=[{'line':i+1,'text':line[:350]} for i,line in enumerate(lines) if term.lower() in line.lower()]
   hits.append({'term':term,'count':len(match),'matches':match})
  searchlog[topic][name]=hits
(OUT/'credit_searches.json').write_text(json.dumps(searchlog,indent=2,ensure_ascii=False))

def credit(topic,num,key):
 terms=', '.join(searchterms[topic])
 ac='not found: searched '+terms+'; inspected AC26 §3, Theorem 3.4 and Remark 3.12 for its period construction.'
 en='not found: searched '+terms+'; inspected E26 §§1.1,2 and Remark 8.1 for the linearization and varying elliptic curves.'
 dg='not found: searched '+terms+'; inspected DGKXv1 §7, Corollary p2:cor:bare-period; no evaluation of M_0 is given.'
 credited='This paper (source run); construction and period laws credited to AC26, elliptic-surface interpretation to AC26 Remark 3.12 and E26.'
 if num=='C.1.1' and key=='fam':
  ac='found in part: AC26 Theorem 3.4(ii) gives the two finite mu values; Remark 3.12 gives the elliptic-logarithm interpretation. Theta formula, cusp logarithm and beta values not found; searched '+terms+'.'
  credited='AC26 Theorem 3.4(ii) for finite mu values and Remark 3.12 for geometric interpretation; this paper for normalized theta expression and beta evaluations; Eichler–Zagier for the zero formula.'
 if num=='C.1.2' and key=='fam':
  ac='found in part: the two finite mu values are exact formulas of AC26 Theorem 3.4(ii); the recorded twenty-decimal theta evaluations and certified special interval are not found. Searched '+terms+'.'
  credited='AC26 Theorem 3.4(ii) for the finite mu values; FAM producing run for the recorded numerical evaluations, tail estimate and special interval.'
 if topic=='nomes':
  en='found in part: E26 Remark 8.1 says the elliptic curves in the bielliptic fibres vary with u. Exact nomes, constants and ratio not found; searched '+terms+'.'
  dg='found in part: DGKXv1 Corollary p2:cor:bare-period, lines 11117–11143, gives the punctured-disc orbit curve with radius exp(-pi M_0); exact nomes/radius not found; searched '+terms+'.'
  credited='This paper for exact nomes, constants and continuation radius; DGKXv1 for the abstract punctured-disc frame; E26 for variation of the elliptic curves.'
 if topic=='maximum':
  dg='found in part: DGKXv1 definition of M_0, lines 722–738, and Corollary p2:cor:bare-period, lines 11117–11143; maximum value, equality locus and radius 216 not found; searched '+terms+'.'
  credited='This paper for the maximum, equality locus and radius; DGKXv1 for the abstract punctured-disc frame.'
 return ac,en,dg,credited

def add(key,num,status='T',topic='theta',uses='definitions only',section='3',mechanism=None,proof=True,env=None):
 b=B[key][num]; source=b['body']; body=adapt(source,key,num)
 prefix='fam' if key=='fam' else ('push' if key=='push' else 'ari'); label=prefix+':'+num
 e=env or ('announcement' if status=='A' else ('computed' if key=='push' or (key=='fam' and num=='C.2.3') else 'proposition'))
 title=re.sub(r'^[A-Z]\.\d+(?:\.\d+)+[; ].*?(?:Proved: |Known, with derivation: )','',b['title'])
 if title==b['title'] or len(title)>100:title=''
 head=prefix.upper()+' '+num+'; '+status+(('; '+title) if title else '')
 head=head.replace('R4 by', 'FAM C.2.3 by')
 rendered='\\begin{'+e+'}['+head+']\\label{'+label+'}\n'+body+'\n\\end{'+e+'}\n\\noindent\\textit{Uses:} '+uses+'.\\par\n'
 if mechanism:
  rendered+=mechanism+'\n\\noindent\\textit{Proof in the repository:} \\href{https://github.com/KokunoYumeto/s6-complex-structure-workbench}{S6 complex-structure workbench}, '+('S6_05_ARITHMETIC' if prefix=='ari' else ('S6_02_FAMILY' if prefix=='fam' else 'S6_02_PUSH')).replace('_',r'\_')+', Statement '+num+'.\n'
 elif proof:
  rendered+=step_proof(adapt(b['proof'],key,num),uses)
 ac,en,dg,credited=credit(topic,num,key)
 records.append({'paper_label':label,'statement_as_printed':body,'status':status,'source_run':{'fam':'FAM','push':'PUSH','ari':'ARI'}[prefix], 'source_id':num,'source_file':paths[key], 'wording_vs_source':'same content: only notation, reference locators and status heading are edited; all hypotheses, parameter ranges, equations and conclusions retained. Exact textual diff in statement_comparisons.json.', 'found_in_AC26':ac,'found_in_E26':en,'found_in_DGKX_v1':dg,'credited_to':credited,'checks':'Statement body compared by exact character diff against extracted source; prior-source searches recorded in credit_searches.json. Historical proof checks only as in status files; no new independent mathematical verification claimed.', 'kind':'Computation' if e=='computed' else 'Theorem','uses':uses,'one_line':b['title'],'proof_location':'§'+section+(' (mechanism only; repository proof)' if status=='A' else ''),'source_statement':source,'source_line':b['line']})
 changes.append({'label':label,'source_sha256':hashlib.sha256(source.encode()).hexdigest(),'printed_sha256':hashlib.sha256(body.encode()).hexdigest(),'diff':'\n'.join(difflib.unified_diff(source.splitlines(),body.splitlines(),fromfile=paths[key],tofile=label,lineterm=''))})
 return rendered

parts=[]
parts.append(r'''\section{Periods in closed form}\label{sec:periods}
\subsection{The normalized theta expression}
We use the odd Jacobi function and the Dedekind function in FAM C.1:
\[
\vartheta_1(v,\tau)=2\sum_{n\ge0}(-1)^n e^{\pi i\tau(n+1/2)^2}\sin((2n+1)\pi v),\qquad
\eta_D(\tau)=e^{\pi i\tau/12}\prod_{n\ge1}(1-e^{2\pi in\tau}).
\]
The cusp branch is reached from $\tau=iT$, $T>1$, on which $\mu=1/2-iy(T)$ and $0<y(T)<T/2$.
Set $a_{\rm cusp}=5+2\sqrt6$. The elliptic-logarithm interpretation is due to \cite[Remark~3.12]{AC26}; the zero formula is due to Eichler and Zagier \cite[unnumbered theorem, p.~399]{EZ82}, also stated in \cite[§2, equation~(6)]{DI10}.
''')
a=add('fam','C.1.1',uses=r'FAM B.1.3; the cusp normalization; the Jacobi transformation laws',topic='theta')
a=a.replace(r'\log a',r'\log a_{\rm cusp}').replace(r'=-a',r'=-a_{\rm cusp}')
# Update printed source record for the intentional cusp-constant rename.
records[-1]['statement_as_printed']=records[-1]['statement_as_printed'].replace(r'\log a',r'\log a_{\rm cusp}').replace(r'=-a',r'=-a_{\rm cusp}')
parts.append(a)
parts.append(add('fam','C.1.2',uses='FAM C.1.1; the theta product and its displayed tail bound',topic='decimals',env='computed'))
parts.append(r'''The computation in FAM C.1.2 is the recorded source computation. Neither \path{cd_numerics.py} nor \path{cd_special_intervals.py}, nor their full outputs, is among the supplied attachments; no current execution is claimed. The latter interval is the input used by FAM A.4.1 for its generic Albanese cross-check. All program and output-file references in the period and maximum proofs below likewise describe the source runs; they do not assert a current execution or the presence of those artifacts in the supplied attachments.
''')
parts.append(r'''\subsection{The elliptic norm and its special values}
The elliptic lattice in this subsection is denoted $\Lambda_{\rm ell}$ to distinguish it from the marked rank-four lattice. Put
\[
\mathcal N(v,\tau)=e^{-\pi(\operatorname{Im}v)^2/\operatorname{Im}\tau}
\left|\frac{\vartheta_1(v,\tau)}{\eta_D(\tau)}\right|,
\qquad U_\tau(v)=\log\mathcal N(v,\tau),
\qquad \mathcal L(t)=U_\tau(\mu).
\]
For $\Lambda_{\rm ell}=\omega(\mathbb Z+\tau\mathbb Z)$ use $U_{\Lambda_{\rm ell}}(z)=U_\tau(z/\omega)$.
The theta formula gives the source identity (FAM C.2.1, equation~\texttt{cd-norm})
\begin{equation}\label{fam:eq:cd-norm}
D_{\rm part}=\frac6\pi\log\frac{\mathcal N(\mu,\tau)}{2\sqrt3}.
\end{equation}
''')
parts.append(add('special','C.1.1',topic='Green',uses='the theta product and Haar probability measure'))
parts.append(add('special','C.1.2',topic='theta',uses=r'ARI C.1.1; FAM C.1.1; the fixed cusp branch'))
parts.append(r'\subsection{The Albanese nomes}'+'\n')
parts.append(add('special','C.2.1',topic='nomes',uses='FAM A.4.1 and A.5.1; ARI C.1.2; the maximum theorem stated in the Result',section='3'))
parts.append(r'''\subsection{Division values}
For division-polynomial calculations we use the rational model of ARI C.4:
\[
E^{\rm div}_t:\quad y_{\rm div}^2=x_{\rm div}^3+A(t)x_{\rm div}+B(t),\quad
A=-\tfrac34t^3(t-1),\quad B=\tfrac14t^4(t-1)^2,
\]
\[
P^{\rm div}=(0,t^2(t-1)/2),\qquad \Delta_{\rm div}(t)=27t^8(t-1)^3.
\]
Its coordinates are distinguished from the cubic coordinates in FAM B.1.1. The notation sheet records the homothety and the sign of its distinguished section; the invariant norm is the same. We use $\lambda_\infty(Q)=-\log\mathcal N(Q)$ as the normalized local-height notation of ARI C.4.1.
''')
parts.append(add('special','C.4.2',topic='division',uses='ARI C.1.1; the displayed rational Weierstrass model and standard division-polynomial normalization'))
parts.append(add('special','C.4.3',topic='division',uses='ARI C.4.2; the nonreal cusp value of the chosen elliptic logarithm'))
parts.append(add('special','C.4.4',topic='division',uses='ARI C.1.2, C.4.2 and C.4.3; the division-polynomial recurrence'))
parts.append(r'\subsection{Integral identities}'+'\n')
parts.append(add('integral','C.8.6',topic='integral',uses='ARI C.1.1; the maximum theorem stated in the Result'))
parts.append(add('integral','C.8.7',topic='integral',uses='ARI C.8.6; the gamma duplication and triplication formulas'))
parts.append(r'\subsection{Announcements on the norm and the Betti measure}'+'\n')
parts.append(add('integral','C.8.8',status='A',topic='measure',uses='the theta series and Poisson summation',mechanism=r'The mechanism is comparison of Fourier coefficients on the real torus. The signed sum of the four half-period translates of the Gaussian has the same coefficients as the squared theta series with its Gaussian normalization.',proof=False))
parts.append(r'''We take $dd^c=(i/\pi)\partial\bar\partial$ and $dA_{z_B}=(i/2)dz_B\wedge d\bar z_B$ (ARI C.8, measure subsection). Here $z_B$ is a local base coordinate; it is unrelated to the global parameter $w$.
''')
parts.append(add('measure','C.8.9',status='A',topic='measure',uses='the normalized theta norm; local root expansions and the cusp branch',mechanism=r'The mechanism is the curvature of the real Gaussian factor and the Jacobian of the two Betti coordinates. The cusp logarithm supplies the point mass, and the two finite root expansions supply the stated integrable densities; we retain the corrected sign and total mass from the source.',proof=False))
parts.append(add('measure','C.8.10',status='A',topic='measure',uses='ARI C.8.9; the height metric and its equidistribution theorem',mechanism=r'The mechanism applies the height metric and the small-height equidistribution theorem of DeMarco and Mavraki \cite[Theorem~1.1 and Corollary~1.2]{DM20}, with the normalization of ARI C.8.9. The passage to full division divisors uses bounded multiplicities at a fixed torsion parameter.',proof=False))
parts.append(add('measure','C.8.11',status='A',topic='measure',uses='the theta heat equation and the Weierstrass differential equation',mechanism=r'The mechanism differentiates the logarithm of the theta quotient and its real Gaussian factor, and then differentiates the zero equation for the chosen elliptic logarithm. The root chart handles a half-period, where the displayed quotients are interpreted by continuation.',proof=False))
parts.append(r'\section{The exact moduli disc}\label{sec:maximum}'+'\n')
parts.append(r'''\subsection{The two interval certificates}
The known abstract orbit-disc description is credited to \cite[Corollary~\texttt{p2:cor:bare-period}]{DGKXv1}; it leaves the maximum unevaluated. The following maximum and its arithmetic certification are FAM C.2.3 and PUSH E.4.
''')
parts.append(add('fam','C.2.3',topic='maximum',uses='FAM C.1.1 and C.2.2; the interval cover described below',section='4',proof=False))
parts.append(add('push','E.4.1',topic='maximum',uses='the supplied rational rectangle endpoints; the theta norm; Arb interval arithmetic',section='4',proof=False))
parts.append(r'''\paragraph{Certificate block.}
The source certificate is the JSON file \path{f_interval_parallel_certificate.json} named in the FAM report. Its verifier is \path{f_interval_verify.py}; the interval calculation is \path{f_interval_cert.py}, scheduled by \path{f_interval_parallel.py}. The certificate has 19,911 leaves: 19,701 norm boxes, 36 boxes in the analytic local square, and 174 boxes strictly inside the unit circle. The root rectangle is $[0,1/2]+i[17/20,2]$, its exact area is $23/40$, and its maximum subdivision depth is 38. There are zero pending boxes. At 30 decimal digits the largest squared-norm upper endpoint is
\[
\frac{9999999982782673130994674616307871}
 {5000000000000000000000000000000000}<2.
\]
The norm boxes use a uniform complex contraction enclosure for a zero of $\wp_\tau$, followed by an outward upper bound for $\mathcal N^2$. Sign and lattice invariance give the same norm at both zeros. The verifier reconstructs the partition and checks the strict bounds and rational exclusions. The local square is covered by FAM C.2.2; the Fourier-product estimate for $T\ge2$ gives $\mathcal N<1.082$. These are the three parts of the certified proof in FAM C.2.3.

PUSH E.4.1 reuses only the rational rectangle endpoints and recomputes roots, preconditioners, radii, contraction estimates, values and tails using Arb through python-flint 0.9.0. The two programs are \path{code/e4_arb_certificate.py} (192 bits) and \path{code/e4_cover_and_local.py} (256 bits). The cover is checked at all 438 distinct vertical edges; each open vertical slab is partitioned once. The independent largest norm bound is
\[
1.999877571767410524070536478244687423578792301873142913
\ \pm9.26\cdot10^{-56},
\]
which is strictly below two. The value belongs to the enclosure of an upper bound, not to an evaluation of the maximum. The midpoint-radius representation is described in \cite[§§2--3]{Johansson2016}; the constructor and outward endpoints are documented in \cite[\texttt{arb}, \texttt{abs\_upper}, \texttt{upper}]{PythonFlint2026}.

The supplied review records a re-execution of all 19,701 FAM boxes with identical upper-bound strings (73 seconds, 12 processes), by Claude Fable 5.2 at effort high, using Python 3.13.9, sympy 1.13.1 and mpmath 1.3.0. The source review records a read of the verifier and interval routines. The PUSH certification is a producing-run computation by GPT-6 Astra, ChatGPT Pro mode; the intake did not rerun that code.

The attached material contains the TeX descriptions and the status records, but contains neither certificate file nor its executable verifier. Consequently their byte sizes, SHA-256 digests and current executions cannot be supplied from these attachments. We have not reconstructed missing certificates or claimed a new execution. This limitation concerns the supplied computational artifacts; the full duplication proof follows in the text. Its presence does not change the designated proof of record.
''')
parts.append(r'''\subsection{Local parameters for the duplication proof}
Put $G_\square=g_2(i)=\Gamma(1/4)^8/(16\pi^2)$ and $D_*=-3\log6/\pi$ (ARI C.3.1).
''')
parts.append(add('special','C.3.1',topic='expansion',uses='the theta heat equation; the half-period Weierstrass equation; the cusp-normalized branch',section='4'))
parts.append(r'''\subsection{The three-step duplication proof}
Throughout this proof $q_\tau=e^{2\pi i\tau}$, $T=\operatorname{Im}\tau$, and
\[
\Delta_{\rm mod}=q_\tau\prod_{n\ge1}(1-q_\tau^n)^{24},\qquad
 t=\frac{E_4^3}{1728\Delta_{\rm mod}},\qquad
 t-1=\frac{E_6^2}{1728\Delta_{\rm mod}}.
\]
This modular discriminant differs from the discriminant of the rational division model.
''')
for n,uses in [
 ('C.8.1','the theta product, Poisson summation and Fourier majorants'),
 ('C.8.2','ARI C.8.1 and C.3.1; the theta heat equation and Cauchy estimates'),
 ('C.8.3','ARI C.8.2; the Ramanujan differential identities and Rouche theorem'),
 ('C.8.4','ARI C.4.2, C.4.4 and C.3.1'),
 ('C.8.5','ARI C.8.1–C.8.4; the norm values of ARI C.1.2')]:
 parts.append(add('analytic',n,topic='maximum',uses=uses,section='4'))
parts.append(r'\subsection{Announcement on rays and level curves}'+'\n')
parts.append(add('critical','C.8.15',status='A',topic='measure',uses='ARI C.8.11–C.8.14 and the two local root expansions',section='4',mechanism=r'The mechanism bounds the two critical factors on a cusp region and on the remaining compact modular region. The root expansions identify their behavior over $t=0,1$; the radial derivative then gives the one-radius parametrization of each lower level.',proof=False))

# Text corrections are recorded as editing of provenance references, never mathematical content.
full='\n'.join(parts)
full=full.replace(r'\citet',r'\cite').replace(r'\citep',r'\cite')
full=full.replace(r'\cite{DGKXv1}',r'\cite[Theorem~1.4 (\texttt{p2:thm:exact-period})]{DGKXv1}')
full=full.replace('Version 2 drops that theorem;',r'Version~2 \cite[Introduction]{DGKXv2} omits that theorem;')
full=full.replace('–','--')
full=full.replace('The executable ', 'The source run records that the executable ')
full=full.replace(r'The script \path', r'The source run records the script \path')
# Unique normalized equation labels and source statement labels are retained.
(OUT/'sections.tex').write_text(full)
# Re-extract the body as printed after every editorial replacement.
changes=[]
for r in records:
 label=r['paper_label']; start=full.index(r'\label{'+label+'}')+len(r'\label{'+label+'}')
 end=re.search(r'\\end\{(?:proposition|computed|announcement)\}',full[start:]).start()+start
 r['statement_as_printed']=full[start:end].strip()
 changes.append({'label':label,'source_sha256':hashlib.sha256(r['source_statement'].encode()).hexdigest(),'printed_sha256':hashlib.sha256(r['statement_as_printed'].encode()).hexdigest(),'diff':'\n'.join(difflib.unified_diff(r['source_statement'].splitlines(),r['statement_as_printed'].splitlines(),fromfile=r['source_file'],tofile=label,lineterm=''))})
(OUT/'records.json').write_text(json.dumps(records,ensure_ascii=False,indent=2))
(OUT/'statement_comparisons.json').write_text(json.dumps(changes,ensure_ascii=False,indent=2))
print(len(records),'statements;',len(full),'characters')
