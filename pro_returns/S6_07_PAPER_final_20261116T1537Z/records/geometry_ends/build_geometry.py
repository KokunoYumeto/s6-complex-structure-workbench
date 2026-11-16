from pathlib import Path
import re, json, difflib, hashlib

ROOT=Path('/workspace/scratch/33c5206c0778')
OUT=ROOT/'deliverables/records/geometry_ends'
SRC=ROOT/'inputs/sources'
RUNS={'FAM':'S6_02_FAMILY','PUSH':'S6_02_PUSH','MAPS':'S6_04_MAPS_MANIFOLDS','ARI':'S6_05_ARITHMETIC'}
FILES={
 'ab':('FAM','sections/AB.tex'), 'cd':('FAM','sections/CD.tex'), 'f':('FAM','sections/F.tex'),
 'ari':('ARI','sections/C_special.tex'), 'real':('MAPS','sections/real_forms.tex'),
 'maps':('MAPS','sections/maps_B.tex'), 'pab':('PUSH','sections/AB_push.tex'),
 'pd':('PUSH','sections/D_push.tex'),
 'nonfill':('PUSH','sections/B_global_noncompletion.tex'),
 'mono1':('PUSH','sections/C_monodromy_value.tex'),
 'mono2':('PUSH','sections/C_independent_monodromy_value.tex'),
 'global':('PUSH','sections/E_global_completion.tex'),
 'disc':('PUSH','sections/E_disc_propagation.tex'),
 'bases':('PUSH','sections/E_arbitrary_deformation_bases.tex'),
 'continuous':('PUSH','sections/E_continuous_deformations.tex'),
 'specialization':('PUSH','sections/E_smooth_specialization.tex'),
 'zero':('PUSH','sections/E_zero_period_obstruction.tex'),
 'general':('PUSH','sections/E_push.tex'),
 'alg':('PUSH','sections/ab_push_normalization_algorithm.tex'),
 'pushconv':('PUSH','sections/conventions_push.tex'),
 'mapsconv':('MAPS','sections/conventions.tex'),
 'cpush':('PUSH','sections/C_push.tex'),
}
texts={k:(SRC/'returns'/RUNS[r]/f).read_text() for k,(r,f) in FILES.items() if (SRC/'returns'/RUNS[r]/f).exists()}
records=[]; comparisons=[]; proof_comparisons=[]; sections=[]; appendix=[]

prior_paths={
 'AC26':ROOT/'inputs/context/original/AC26_transcription.tex',
 'E26':ROOT/'inputs/context/papers/arXiv_2609.38442_Engel_src/S6.tex',
 'DGKX_v1':ROOT/'inputs/context/papers/arXiv_2610.00250v1_Du_Guo_Kusakabe_Xie.tex',
}
prior={k:p.read_text() for k,p in prior_paths.items()}
search_terms={
 'aut':[r'full.automorph',r'Aut',r'identity component',r'automorphism group'],
 'real':[r'antiholomorphic',r'anti.holomorphic',r'real structure',r'real form',r'fixed set',r'Hopf action'],
 'mono':[r'Klingler',r'Heisenberg',r'index.?12',r'properly discontinu',r'period domain',r'Zariski closure'],
 'quotient':[r'elliptic quotient',r'first projection',r'6016',r'8192',r'32/5',r'torsion locus',r'countable and dense'],
 'ns':[r'N.ron.Severi',r'\\NS',r'Pfaffian',r'6\\mu\^2',r'countab',r'Lemma 9.2',r'-3n\^2',r'12n\\mu',r'-6\\tau-12\\mu',r'Z_E',r'algebraic dimension one'],
 'curves':[r'compact irreducible',r'every.*curve',r'curve.*(fibre|fiber|vertical)',r'surface.*(fibre|fiber|vertical)',r'normalization.*dP',r'bielliptic'],
 'outer':[r'216',r'natural boundary',r'meromorphic continuation',r'anticanonical divisor',r'Albanese'],
 'pinching':[r'Conjecture',r'flat, proper filling',r'virtual',r'semistable',r'normalization',r'plumbing'],
 'nonfill':[r'proper.*filling',r'proper.*completion',r'finite.*base.change',r'log.torsor',r'Conjecture'],
 'smoothmono':[r'Theta',r'\\Theta',r'mapping torus',r'smooth monodromy',r'Pontryagin',r'spin.c',r'28'],
 'components':[r'open and closed',r'connected components',r'integrable',r'continuous family',r'coprime',r'Kuranishi'],
}
credit_searches=[]
for group,terms in search_terms.items():
 for name,txt in prior.items():
  findings=[]
  for term in terms:
   matches=list(re.finditer(term,txt,re.I))
   findings.append({'term':term,'count':len(matches),'locations':[{'line':txt.count('\n',0,m.start())+1,'context':txt[max(0,m.start()-100):min(len(txt),m.end()+160)].replace('\n',' ')} for m in matches[:8]]})
  credit_searches.append({'group':group,'source':name,'file':str(prior_paths[name].relative_to(ROOT/'inputs/context')),'searches':findings})

locators={
 'aut':{
  'AC26':'found: §9.7, Proposition 9.23 and Corollary 9.24, transcription lines 4340–4390, give Aut^0=C*, its translation periods and fixed curve; they do not supply the full-component conclusion.',
  'E26':'not found: searched full automorphism, Aut, identity component, automorphism group; inspected §8 Remarks 8.1–8.4, which discuss the family and degeneration but do not state the full group.',
  'DGKX_v1':'found: theorem labelled p2:thm:full-automorphisms, source line 11086, with proof, states Aut(X)=Aut_{P^1}(X)=C*.'},
 'real':{
  'AC26':'not found for real structures or real fixed loci: searched antiholomorphic, anti.holomorphic, real structure, real form, fixed set, Hopf action; §9.7 Propositions 9.23–9.24 supply the holomorphic C* action and its fixed curve only.',
  'E26':'not found: searched antiholomorphic, anti.holomorphic, real structure, real form, fixed set, Hopf action; inspected §8 without finding a real-structure classification.',
  'DGKX_v1':'not found: searched antiholomorphic, anti.holomorphic, real structure, real form, fixed set, Hopf action; the theorem p2:thm:full-automorphisms concerns holomorphic automorphisms only.'},
 'mono':{
  'AC26':'not found for exact index, maximal domain or answer: searched Klingler, Heisenberg, index12, properly discontinu, period domain, Zariski closure; the construction provides the integral monodromy and period input, not these arithmetic/properness conclusions.',
  'E26':'found as input/question: §5 gives integral monodromy; Remark 8.4 (source lines 1720–1737) identifies the indefinite (1,6) period domain and asks Klingler’s proper-action question. No index-12 character or maximal proper open set is stated there.',
  'DGKX_v1':'not found for these conclusions: searched Klingler, Heisenberg, index12, properly discontinu, period domain, Zariski closure; its occurrences of proper discontinuity concern the existing period construction.'},
 'quotient':{
  'AC26':'not found for the explicit first-projection/torsion/counting/counterexample conclusions: searched elliptic quotient, first projection, 6016, 8192, 32/5, torsion locus, countable and dense; §9.1 gives generic Néron–Severi and algebraic-dimension input.',
  'E26':'found input only: §2 Lemma 2.1 and its proof compute the height 1/6 of P and the relevant fibre contributions; searched elliptic quotient, first projection, 6016, 8192, 32/5, torsion locus, countable and dense without finding the printed conclusions.',
  'DGKX_v1':'not found: searched elliptic quotient, first projection, 6016, 8192, 32/5, torsion locus, countable and dense; inspected the family/classification discussion.'},
 'ns':{
  'AC26':'found in substantial part: §9.1 Lemma 9.2 is exactly the displayed Néron–Severi equation; Lemma 9.3 proves the five-function independence; Lemma 9.4 treats indefiniteness of eta; Proposition 9.5 and Corollary 9.8 give the countable-exceptional/generic NS=Z eta and algebraic-dimension-zero conclusions (transcription lines 3274–3551). The explicit c_n and algebraic-dimension-one construction are not found in searches for their coefficients.',
  'E26':'not found for the Néron–Severi equation/classification: searched N.ron.Severi, NS, Pfaffian, 6mu^2, countab; §8 Remark 8.4 supplies only the indefinite alternating-form framework.',
  'DGKX_v1':'not found for the equation and exact fibre loci: searched N.ron.Severi, NS, Pfaffian, 6mu^2, countab; no counterpart of the six-coefficient criterion was located.'},
 'curves':{
  'AC26':'found input and part of the special-fibre description: §4.6 Proposition 4.6 (source PDF p.29; transcription lines 1452–1470) gives the finite dP6 normalization, opposite boundary identifications, three double curves and two triple points; §9.1 gives generic no-curve fibres. No every-compact-curve-is-vertical or every-compact-surface-is-a-fibre theorem was found by searches compact irreducible, every curve, curve.*fibre/fiber/vertical, surface.*fibre/fiber/vertical.',
  'E26':'not found for the exhaustive curve/surface assertions: searched compact irreducible, every.*curve, curve.*fibre/fiber/vertical, surface.*fibre/fiber/vertical, bielliptic; §8 supplies degeneration context only.',
  'DGKX_v1':'not found for these exhaustive assertions: searched compact irreducible, every.*curve, curve.*fibre/fiber/vertical, surface.*fibre/fiber/vertical, bielliptic; the separate compact-curve occurrences concern Oka questions, not this classification.'},
 'outer':{
  'AC26':'found input only: the canonical divisor and distinguished reduced multiple fibre are part of the construction, while searches 216, natural boundary, meromorphic continuation, Albanese do not give the boundary obstruction.',
  'E26':'not found for the boundary obstruction: searched 216, natural boundary, meromorphic continuation, anticanonical divisor, Albanese; §8 Remark 8.1 states a different moduli interpretation, corrected elsewhere in the paper.',
  'DGKX_v1':'found input only: Theorem 7.1 and its companion recover the intrinsic pencil and distinguished fibre; searched 216, natural boundary, meromorphic continuation, Albanese without finding the outer-boundary obstruction.'},
 'pinching':{
  'AC26':'not found for the virtual-Euler obstruction or corrected fillings: searched virtual, flat proper filling, semistable, plumbing; §4.6 Proposition 4.6 supplies the original cusp fibre with Euler number two.',
  'E26':'found target/input: §2 Lemma 2.1 and Corollary 2.2 give the line bundle and smoothing section; §8 Conjecture 8.2 (source lines 1673–1676) is the exact conjecture refuted. No virtual-Euler calculation or corrected fillings are stated there.',
  'DGKX_v1':'not found: searched virtual, flat proper filling, semistable, plumbing, Conjecture 8.2; no counterpart of the obstruction or corrected fillings was located.'},
 'nonfill':{
  'AC26':'not found: searched proper.*filling, proper.*completion, finite.*base.change, log.torsor; the supplied construction is of individual compact fibres, not this global noncompletion statement.',
  'E26':'found related conjecture only: §8 Conjecture 8.2 proposes an untwisted filling with a specified central fibre. It is not the same family or the universal no-filling statement; searched proper.*filling/completion, finite.*base.change, log.torsor.',
  'DGKX_v1':'not found: searched proper.*filling, proper.*completion, finite.*base.change, log.torsor; no global analytic noncompletion statement was located.'},
 'smoothmono':{
  'AC26':'not found: searched Theta, mapping torus, smooth monodromy, Pontryagin, spin.c, 28; §9.7 supplies the circle action used as geometric input, not the loop class in Theta7.',
  'E26':'not found: searched Theta, mapping torus, smooth monodromy, Pontryagin, spin.c, 28; §8 Remark 8.4 concerns lattice monodromy, not smooth mapping classes.',
  'DGKX_v1':'not found: searched Theta, mapping torus, smooth monodromy, Pontryagin, spin.c, 28; no evaluation of this smooth monodromy was located.'},
 'components':{
  'AC26':'not found for the component/deformation-separation conclusions: searched open and closed, connected components, integrable, continuous family, coprime, Kuranishi; Theorem 1.1 supplies the constructed family only.',
  'E26':'not found: searched open and closed, connected components, integrable, continuous family, coprime, Kuranishi; no such separation theorem was located.',
  'DGKX_v1':'found local input only: Theorem 1.3 and its detailed deformation section supply the Kuranishi line/miniversality for the retained family. Searched open and closed, connected components, integrable, continuous family, coprime; the global fixed-pair separation assertions were not found.'},
}

def unit(key,id):
 s=texts[key]
 pat=r'\\begin\{(theorem|proposition|lemma|corollary|remark|statement)\}\['+re.escape(id)+r'(?=[;\s(])([^\]]*)\]'
 m=re.search(pat,s)
 if m:
  end=s.index('\\end{'+m[1]+'}',m.end())
  body=s[m.end():end].strip()
  tail=s[end+len('\\end{'+m[1]+'}'):]
  pm=re.match(r'\s*\\begin\{proof\}(?:\[[^\]]*\])?([\s\S]*?)\\end\{proof\}',tail)
  return {'env':m[1],'body':body,'proof':pm[1].strip() if pm else '', 'line':s.count('\n',0,m.start())+1,'heading':id+m[2]}
 pat=r'\\paragraph\{(Theorem|Proposition|Lemma|Corollary) '+re.escape(id)+r'[^\n]*\}\s*'
 m=re.search(pat,s)
 if not m: raise ValueError((key,id,'not found'))
 end=s.index('\\begin{proof}',m.end())
 pend=s.index('\\end{proof}',end)
 return {'env':m[1].lower(),'body':s[m.end():end].strip(),'proof':s[end+len('\\begin{proof}'):pend].strip(),'line':s.count('\n',0,m.start())+1,'heading':m[0].strip()}

FAM_IDS=['B.4.1','B.4.2']+['F.1.1','F.1.2','F.2.1','F.2.2','F.2.3','F.3.1','F.3.2','F.3.3']+[f'D.1.{i}' for i in range(1,8)]+[f'D.2.{i}' for i in range(1,4)]+['A.1.1','A.1.2','A.2.1','A.3.1','A.5.1','B.2.1','C.2.3','C.1.1']
PUSH_IDS=['D.1.1','D.1.2','D.1.3','A.1.1','A.1.2','A.2.1','A.2.2','A.2.3','A.2.4','A.3.1','A.3.2','B.4.33','C.3.24','C.3.27','E.2.21','E.2.22','E.2.23','E.2.24']

def normalize(s,run,key,proof=False):
 # Unify only names, displayed labels, locators and source-internal cross references.
 s=re.sub(r'\\label\{(?:st:|push:)[^}]+\}\s*','',s, count=1) if not proof else s
 s=s.replace('\\cite{DuGuoKusakabeXie2026v1}',r'\cite[theorem \texttt{p2:thm:full-automorphisms}]{DGKX26v1}')
 s=s.replace('DGKX26v1','DGKXv1').replace(r'\PP',r'\Pp').replace(r'\RP',r'\mathbb{RP}')
 s=s.replace(r'u\wedge w',r'u_{\Lambda}\wedge w_{\Lambda}')
 s=s.replace('Theorem~1.4 of\n'+r'\cite[theorem \texttt{p2:thm:full-automorphisms}]{DGKXv1}',r'\cite[theorem \texttt{p2:thm:full-automorphisms}]{DGKXv1}')
 for old,new in {'push:A31':'push:A.3.1','push:A32':'push:A.3.2'}.items(): s=s.replace('{'+old+'}','{'+new+'}')
 if run=='FAM':
  s=re.sub(r'\{st:([^}]+)\}',r'{fam:\1}',s)
  s=re.sub(r'\{(eq:[^}]+)\}',r'{fam:\1}',s)
  for id in sorted(FAM_IDS,key=len,reverse=True):
   s=re.sub(r'(?<![:{\w])'+re.escape(id)+r'(?![\w}])',lambda m:r'\ref{fam:'+id+'}',s)
 if run=='PUSH':
  for id in sorted(PUSH_IDS,key=len,reverse=True):
   s=re.sub(r'(?<![:{\w])'+re.escape(id)+r'(?![\w}])',lambda m:r'\ref{push:'+id+'}',s)
 if key=='f':
  # e in F is the primitive lattice vector, whereas e in FAM AB is its fibre period.
  s=s.replace(r'e^{\pi i/3}','EXPONENTIALONE').replace(r'e^{2\pi is}','EXPONENTIALTWO')
  s=re.sub(r'(?<![A-Za-z\\])d(?![A-Za-z])',lambda m:r'd_{\rm aux}',s)
  s=re.sub(r'(?<![A-Za-z\\])e(?![A-Za-z])','d',s)
  s=s.replace(r'\mathbb Ze',r'\mathbb Zd').replace(r'\mathbb Re',r'\mathbb Rd').replace(r'\mathbb Ce',r'\mathbb Cd').replace('Je','Jd')
  s=s.replace('EXPONENTIALONE',r'e^{\pi i/3}').replace('EXPONENTIALTWO',r'e^{2\pi is}')
  s=s.replace('C(q)','C(t_c)').replace(r'$q=e^{2\pi is}$',r'$t_c=e^{2\pi is}$').replace('O(q)','O(t_c)')
  s=s.replace('the matrices in the question','the matrices in the fixed conventions').replace('The matrices in the question','The matrices in the fixed conventions')
 if key in ['pab','alg']:
  s=re.sub(r'(?<![A-Za-z\\])J(?![A-Za-z])',lambda m:r'J_{\rm lin}',s)
  s=s.replace(r'\mathbb L','COTANGENTCOMPLEX')
  s=re.sub(r'(?<![A-Za-z\\])L(?![A-Za-z])','M_S',s)
  s=s.replace('COTANGENTCOMPLEX',r'\mathbb L')
  s=s.replace('h_q','h_{t_c}')
  s=re.sub(r'(?<![A-Za-z\\])q(?![A-Za-z])','t_c',s)
 if key=='real':
  s=s.replace(r'\rho',r'\rho_{\rm circ}')
  s=s.replace('A.3.2',r'\ref{maps:A.3.2}').replace('\\tag{A.3.1}',r'\label{maps:eq:A.3.1}').replace('\\tag{A.3.3}',r'\label{maps:eq:A.3.3}')
  s=s.replace('\\tag{\\ref{maps:A.3.2}}',r'\label{maps:eq:A.3.2}')
 if key=='pd':
  s=s.replace('Grauert (1960, \\S7, Satz~1)',r'\cite[\S7, Satz~1]{Grauert1960D}')
  s=s.replace("Grauert's direct-image theorem\n(1960, \\S6, Hauptsatz~I)",r"Grauert's direct-image theorem \cite[\S6, Hauptsatz~I]{Grauert1960D}")
  s=s.replace("Grauert's 1963 erratum.",r"Grauert's 1963 erratum \cite[item~2, p.~36]{Grauert1963ErratumD}.")
  s=s.replace("Ehresmann's theorem identifies",r"Ehresmann's theorem \cite[\S1, Proposition, pp.~154--155]{Ehresmann52} identifies")
  s=s.replace('Buchdahl (1999,\nTheorem~11)',r'\cite[Theorem~11]{Buchdahl1999}')
  s=s.replace('R7',r'FAM A.4.1').replace('R3',r'FAM C.1.1').replace('R1',r'FAM A.1.1')
  s=s.replace('in the earlier return, A.1.1',r'in FAM A.1.1 (Statement~\ref{fam:A.1.1})')
  s=s.replace('in the earlier return,\nC.3.4',r'in FAM C.3.4')
 if key=='ari':
  s=s.replace('S6\\_02 B.4.2',r'FAM B.4.2 (Statement~\ref{fam:B.4.2})')
  s=s.replace('so R5 gives',r'so Statement~\ref{fam:A.5.1} gives')
 if key=='cd':
  s=s.replace('in AC26, Lemma 9.4',r'in \cite[Lemma~9.4]{AC26}')
  s=s.replace('computed in C.4.1',r'computed in FAM C.4.1; see also \cite[\S4.6, Proposition~4.6]{AC26}')
 s=s.replace(r'Theorem 5.8 and\nRemark 5.9 of \cite{FG10}',r'\cite[Theorem~5.8 and Remark~5.9]{FG10}')
 s=s.replace('Theorem 5.8 and\nRemark 5.9 of '+r'\cite{FG10}',r'\cite[Theorem~5.8 and Remark~5.9]{FG10}')
 if key=='pab':
  s=s.replace(r'of the attached \cite{E26}',r'of \cite[Conjecture~8.2]{E26}')
  s=s.replace('A.4.3 below','PUSH A.4.3 in the repository')
  s=s.replace('The cones $P_{k,l}$ in Lead 2',r'The cones $P_{k,l}$ in Definition~\ref{push:A.1.fan}')
  s=s.replace('gives Part A, and $n=2,12$ give the two cases of B.2.','gives PUSH Part A, and $n=2,12$ give the two cases of PUSH B.2.')
 return s

def step_proof(s):
 if len(s)<1500:return '\\begin{proof}\n'+s+'\n\\end{proof}\n'
 # Break only at source paragraph boundaries outside displayed mathematics/environments.
 chunks=re.split(r'(\n\s*\n)',s)
 out=[];envdepth=0;display=0;n=0
 for chunk in chunks:
  if not chunk.strip():out.append(chunk);continue
  if envdepth==0 and display==0 and not chunk.lstrip().startswith(('\\[','\\begin','\\end')):
   n+=1;out.append(r'\par\noindent\textit{Step '+str(n)+r'.} ')
  out.append(chunk)
  envdepth+=len(re.findall(r'\\begin\{',chunk))-len(re.findall(r'\\end\{',chunk))
  display+=chunk.count('\\[')-chunk.count('\\]')
 return '\\begin{proof}\n'+''.join(out)+'\n\\end{proof}\n'

def row(key,id,body,status,uses,summary,kind='Theorem',group=None,raw=None,line=None,wording=None,credit=None,label=None,proofloc=None):
 run,file=FILES[key];prefix=run.lower();label=label or prefix+':'+id
 sec=7 if key in ['ab','ari','real'] else (8 if key=='f' else (9 if key=='cd' else (10 if key in ['pd','pab','alg'] else 11)))
 if raw is None:
  u=unit(key,id);raw=u['body'];line=u['line']
 group=group or 'mono'
 comp=list(difflib.unified_diff(raw.splitlines(),body.splitlines(),fromfile='source '+id,tofile='paper '+label,lineterm=''))
 comparisons.append({'paper_label':label,'source_file':'returns/'+RUNS[run]+'/'+file,'source_line':line,'source_sha256':hashlib.sha256(raw.encode()).hexdigest(),'printed_sha256':hashlib.sha256(body.encode()).hexdigest(),'diff':comp})
 rr={'paper_label':label,'statement_as_printed':body,'status':status,'source_run':run,'source_id':id,'source_file':'returns/'+RUNS[run]+'/'+file,
 'wording_vs_source':wording or ('same content: only run-prefixed labels, mathematical notation, source locators, status heading and typographical layout are normalized; exact textual diff is in statement_comparisons.json.' if comp else 'same content: statement body unchanged.'),
 'found_in_AC26':locators[group]['AC26'],'found_in_E26':locators[group]['E26'],'found_in_DGKX_v1':locators[group]['DGKX_v1'],
 'credited_to':credit or 'Source run, with construction/period data credited to AC26 and E26; no novelty claimed for separately credited input.',
 'checks':'Exact source-to-print text diff recorded; three prior sources searched with specific terms in credit_searches.json and matched locations inspected. Current assembly asserts S checks only, not a new independent proof verification. Historical proof checks are those of the supplied status files.',
 'source_statement':raw,'summary':summary,'one_line':summary,'kind':kind,'uses':uses,'proof_location':proofloc or ('§'+str(sec)+'; proof in repository: '+run+' '+id if status=='A' else ('Appendix B, re-derivation of FAM B.4.1' if status=='K' else '§'+str(sec))),'source_line':line,'section':sec}
 records.append(rr);return label

def emit(key,id,status,uses,summary,group,kind='Theorem',mechanism=None,credit=None,body_override=None,wording=None,proof_override=None,split_announcement=None):
 uses=uses.replace('–','--').replace('—','---')
 u=unit(key,id);run=FILES[key][0];label=run.lower()+':'+id
 body=normalize(u['body'],run,key) if body_override is None else body_override
 env='announcement' if status=='A' else ('cited' if status=='K' else ('theorem' if u['env'] in ['statement','remark'] else u['env']))
 row(key,id,body,status,uses,summary,kind,group,wording=wording,credit=credit)
 out='\\begin{'+env+'}['+run+' '+id+'; '+status+']\\label{'+label+'}\n'+body+'\n\\end{'+env+'}\n'
 out+=r'\noindent\emph{Uses:} '+uses+'.\\par\n'
 if status=='A':
  out+='\n'+(mechanism or 'The mechanism is the construction specified in the source statement.')+'\n\n'
  out+=r'\noindent\emph{Proof:} proof in the repository, '+run+' '+id+r' (\url{https://github.com/KokunoYumeto/s6-complex-structure-workbench}).'+'\n'
 elif status=='K':
  out+=r'\noindent The re-derivation is in Appendix~B.\par'+'\n'
  printed_proof=step_proof(normalize(u['proof'],run,key,True))
  appendix.append('\\subsection{Re-derivation of FAM B.4.1}\n'+printed_proof)
  proof_comparisons.append({'paper_label':label,'source_file':'returns/'+RUNS[run]+'/'+FILES[key][1],'source_proof':u['proof'],'proof_as_printed':printed_proof,'diff':list(difflib.unified_diff(u['proof'].splitlines(),printed_proof.splitlines(),fromfile='source proof',tofile='printed re-derivation',lineterm=''))})
 else:
  printed_proof=step_proof(normalize(u['proof'],run,key,True) if proof_override is None else proof_override)
  out+='\n'+printed_proof
  proof_comparisons.append({'paper_label':label,'source_file':'returns/'+RUNS[run]+'/'+FILES[key][1],'source_proof':u['proof'],'proof_as_printed':printed_proof,'diff':list(difflib.unified_diff(u['proof'].splitlines(),printed_proof.splitlines(),fromfile='source proof',tofile='printed proof',lineterm=''))})
 return out+'\n'

def definition(key,id,raw,printed,uses,summary,group='mono',status='text',kind='Definition',credit=None,line=1):
 uses=uses.replace('–','--').replace('—','---')
 if key=='real':printed=printed.replace(r'\rho',r'\rho_{\rm circ}')
 run=FILES[key][0];label=run.lower()+':'+id
 if line==1:
  start=texts[key].find(raw.split('\n',1)[0])
  if start>=0:line=texts[key].count('\n',0,start)+1
 row(key,id,printed,status,uses,summary,kind,group,raw=raw,line=line,credit=credit)
 return '\\begin{definition}['+run+' '+id+']\\label{'+label+'}\n'+printed+'\n\\end{definition}\n'+r'\noindent\emph{Uses:} '+uses+'.\\par\n\n'

sections.append(r'''\section{Automorphisms and real structures}
\label{sec:real}
The full holomorphic automorphism group is the theorem of
\cite[theorem \texttt{p2:thm:full-automorphisms}]{DGKXv1}; its identity
component and translation action are due to \cite[\S9.7, Proposition~9.23
and Corollary~9.24]{AC26}. Our lattice calculation is a re-derivation.
''')
sections.append(emit('ab','B.4.1','K','FAM A.1.1, A.1.2, A.2.1, A.3.1 and the cusp valuation comparison in FAM B.2','The full automorphism group is C*.','aut','New proof',credit='DGKXv1, theorem p2:thm:full-automorphisms, for all components; AC26 §9.7 Propositions 9.23–9.24 for Aut^0 and the action.'))
sections.append(emit('ab','B.4.2','T','FAM A.3.1, A.5.1, B.2.1 and B.4.1; the cusp-normalized period laws','Conjugation sends c to 1−conjugate(c), and the real members have split extended automorphism group.','real'))
sections.append(emit('ari','C.2.2','T','FAM B.4.1, B.4.2 and A.5.1; ARI C.2.1','Real structures occur exactly at nonzero real Albanese nome q2.','real'))
sections.append('\\subsection{Announced real fixed loci}\n')
realtxt=texts['real']
raw=realtxt[realtxt.index('In this subsection'):realtxt.index('\\paragraph{Proposition A.3.1')].strip()
printed=raw.replace('In this subsection $d=\\widehat\\delta$ and $g=\\widehat\\gamma$.',r'Here $d=\widehat\delta$, and $\rho(b)$ is translation by $be$ for $b\in\mathbb R/\mathbb Z$.')
sections.append(definition('real','A.3.setup',raw,printed,'FAM B.4.1 and the cusp fan','Cusp double curves and the real circle action.','real',credit='MAPS notation for the cusp curves; the circle action and fixed curve are AC26 §9.7.'))
sections.append(emit('real','A.3.1','A','FAM B.4.1 and B.4.2; the semifree circle action','There are two holomorphic-conjugacy classes of antiholomorphic involutions.','real',mechanism=r'The mechanism combines the sign of the coefficient of an involution in the split group $\mathbb C^*\rtimes\mathbb Z/2$ with the fixed-set calculation for the circle action. The statement concerns the smooth fixed manifolds and the two conjugacy classes; the embedded knot type is not determined.'))
raw=realtxt[realtxt.index('We now fix a representative'):realtxt.index('\\paragraph{Theorem A.3.2')].strip()
printed=raw.replace('We now fix a representative of each sign class, instead of leaving the\nsymbol $\\sigma$ unspecified. Put','For the explicit representatives, put')
printed=printed.replace(r'S(t(z))d',r'S(t(z))e')
printed=printed.replace(r'\Pi_c(z)g',r'\Pi_c(z)\widehat\gamma')
printed=printed.replace(r'\tag{A.3.1}',r'\tag{MAPS A.3.1}').replace(r'\tag{A.3.2}',r'\tag{MAPS A.3.2}')
printed+='\n'+r'Here the fibre vector $e=\Pi_c d=(0,1)^{\mathsf t}$ makes explicit the fibre-coordinate interpretation of $d$ in the source translation formula.'
sections.append(definition('real','A.3.representatives',raw,printed,'FAM B.4.2 and the specified root branches','Explicit roots, branches and translating vectors for the two real representatives.','real'))
sections.append(emit('real','A.3.2','A','MAPS A.3.1 and its explicit representative data; FAM B.4.2','Exact real fixed sets on the ordinary, multiple and cusp fibres.','real',mechanism='The mechanism is the exact affine fixed-point congruence on the three real base arcs, followed by the finite-root quotient calculation at $0$ and $1$ and the sign calculation for the toric units at the cusp. These are calculations for the stated representatives, including their half-circle translates.'))
sections.append(emit('real','A.3.3','A','MAPS A.3.1 and A.3.2','Every nonempty real fixed manifold is S3, with the specified circle action.','real',mechanism='For negative imaginary $w$, the mechanism uses the surface orbit space of the semifree action. For positive imaginary $w$, it uses the two solid-torus caps and the determinant-one comparison of their primitive meridians. No ambient-isotopy classification or Haefliger knot invariant of the embedded three-spheres is asserted.'))

sections.append(r'''\section{The monodromy group and Klingler's question}
\label{sec:monodromy}
The indefinite alternating form and the question about proper discontinuity
are those of \cite[Remark~8.4]{E26}. We retain the actual integral
monodromy of the constructed family.
''')
raw=texts['f'].split('\\subsection{F.1.')[0].split('\n\n',1)[1].strip()
printed=normalize(raw,'FAM','f').replace('on the first page','in our conventions')
sections.append(definition('f','F.setup',raw,printed,'The retained integral marking and monodromy matrices','The indefinite period domain and the convention for proper discontinuity.','mono',credit='E26 Remark 8.4 for the (1,6) form and period-domain question; FAM for the fixed notation.'))
sections.append('\\subsection{An exact arithmetic description}\n')
fuses={
'F.1.1':'The matrices $A_1,A_2$ and the integral symplectic form',
'F.1.2':'FAM F.1.1 and its exact Heisenberg kernel',
'F.2.1':'FAM F.1.1 and the explicit matrices $J_0,R$',
'F.2.2':'FAM F.1.1, F.1.2 and F.2.1; the homogeneous-space stabilizer calculation',
'F.2.3':'The global Siegel chart and the signature condition',
'F.3.1':'FAM F.2.2 and F.2.3; the finite-root and cusp period expansions',
'F.3.2':'The finite special values and the cusp-normalized period matrix',
'F.3.3':'The derivative transformation laws and the finite special values',
}
fsumm={'F.1.1':'The monodromy group is an explicit index-12 character kernel.','F.1.2':'The centre, extension cocycle and Zariski closures are explicit.','F.2.1':'The action is not properly discontinuous on the entire domain.','F.2.2':'The complement of q_d=0 is the largest invariant proper-discontinuity domain.','F.2.3':'All admissible period images lie in a global chart of the positive region.','F.3.1':'The period curve is an injective immersion and has a proper embedded extension.','F.3.2':'The finite limits lie in the domain, while the cusp limit lies outside it.','F.3.3':'The determinant of the derivative is generically nonzero and vanishes at z1.'}
for id in ['F.1.1','F.1.2','F.2.1','F.2.2','F.2.3','F.3.1','F.3.2','F.3.3']:
 if id=='F.2.1':
  sections.append('\\subsection{Properness and the maximal open set}\n')
  raw=texts['f'].split('\\subsection{F.2.')[1].split('\n\n',1)[1].split('\\begin{proposition}')[0].strip()
  sections.append(definition('f','F.2.setup',raw,normalize(raw,'FAM','f'),'FAM F.setup','The invariant function q_d and its two nonzero sign regions.','mono'))
 if id=='F.3.1':sections.append('\\subsection{The curve in the proper quotient}\n')
 sections.append(emit('f',id,'T',fuses[id],fsumm[id],'mono',kind='Counterexample' if id=='F.2.1' else 'Theorem'))

sections.append(r'''\section{Special fibres, curves and surfaces}
\label{sec:fibres}
The N\'eron--Severi equation below is already
\cite[\S9.1, Lemma~9.2]{AC26}; the accompanying independence and
indefiniteness calculations occur in its Lemmas~9.3--9.4. Its
Proposition~9.5 and Corollary~9.8 give the very-general conclusion
$\operatorname{NS}=\mathbb Z\eta$ and algebraic dimension zero.
Those parts are credited to that source, with a derivation retained here
under the binding T status. The explicit quotient loci, examples and
exhaustive descriptions below have their distinct source statements.
\subsection{Elliptic quotients and the torsion locus}
''')
duses={
'D.1.1':'The fixed period matrix and the exact division-polynomial computation',
'D.1.2':'FAM D.1.1; E26 Lemma 2.1 and its height calculation',
'D.1.3':'FAM D.1.1 and the source bound FAM C.2.1',
'D.1.4':'The period matrix; the Hermitian-form convention in FAM D.1.6; AC26 Lemmas 9.2 and 9.4',
'D.1.5':'FAM D.1.4; the five-function independence of AC26 Lemma 9.3',
'D.1.6':'FAM D.1.4; the Appell--Humbert and Riemann criteria',
'D.1.7':'FAM D.1.6 and the cusp expansions',
'D.2.1':r'$X_c\simeq S^6$; the K\"ahler geometry of the reduced fibres',
'D.2.2':'FAM D.1.1 and D.2.1; the finite normalization and boundary identifications of AC26 Proposition 4.6',
'D.2.3':'FAM D.1.6 and D.2.1; the Appell--Humbert theorem and its theta equation',
}
dsumm={'D.1.1':'The first projection descends exactly at the six-division points.','D.1.2':'The torsion locus is countable and dense, with exact intersection degree.','D.1.3':'An unrestricted elliptic-quotient wording is refuted at t=32/5.','D.1.4':'The six-coefficient Néron–Severi equation and the indefinite generator.','D.1.5':'Generic rank one and explicit abelian fibres arbitrarily far into the c half-plane.','D.1.6':'Exact elliptic-quotient, projective and algebraic-dimension loci.','D.1.7':'Actual algebraic-dimension-one fibres, including nontorsion P.','D.2.1':'Every compact curve is vertical and every compact surface is a reduced fibre.','D.2.2':'Rational and elliptic curves and the singular-fibre descriptions.','D.2.3':'All compact curves are classified by the algebraic dimension of their fibre.'}
for id in ['D.1.1','D.1.2','D.1.3','D.1.4','D.1.5','D.1.6','D.1.7','D.2.1','D.2.2','D.2.3']:
 if id=='D.1.3':sections.append(r'\noindent The following counterexample addresses only the unrestricted wording in FAM Lead~6. The first-projection assertion of Statement~\ref{fam:D.1.1} stands.\par'+'\n')
 if id=='D.1.4':
  p=unit('cd','D.1.6')['proof'];a=p.index('The real vector-space');b=p.index('Direct substitution gives')
  raw=p[a:b].strip()
  printed=normalize(raw,'FAM','cd')
  printed+=r' We use $T=\operatorname{Im}\tau$, $U=\operatorname{Im}\mu$ and $D=\operatorname{Im}\beta-6U^2/T$ in the matrix calculation below.'
  sections.append(definition('cd','D.1.Hermitian',raw,printed,'FAM D.1.6, Hermitian-form convention','The transferred alternating form and its explicit Hermitian convention.','ns'))
 if id=='D.2.1':sections.append('\\subsection{Compact curves and surfaces}\n'+r'The cusp normalization and its boundary identifications used here are due to \cite[\S4.6, Proposition~4.6]{AC26}.'+'\n')
 group='quotient' if id in ['D.1.1','D.1.2','D.1.3'] else ('curves' if id.startswith('D.2.') else 'ns')
 knowncredit=None
 if id in ['D.1.4','D.1.5']:
  knowncredit='AC26 §9.1 Lemmas 9.2–9.4, Proposition 9.5 and Corollary 9.8 for the equation, independence, indefinite class and generic conclusion; explicit c_n family is FAM D.1.5.'
 if id=='D.2.2':knowncredit='AC26 §4.6 Proposition 4.6 for the cusp normalization/pairings and the construction of the multiple fibres; the exhaustive curve application and t± restriction are FAM D.2.2.'
 sections.append(emit('cd',id,'T',duses[id],dsumm[id],group,kind='Counterexample' if id=='D.1.3' else ('New proof' if id in ['D.1.4'] else 'Theorem'),credit=knowncredit))

sections.append(r'''\section{The outer boundary and the untwisted filling conjecture}
\label{sec:ends}
\subsection{The intrinsic obstruction at the outer circle}
Throughout this subsection the twists are the standard ones.
Since $q_2=iw/216$, its boundary circle is $|q_2|=1$.
''')
raw=texts['pd'].split('\\subsection{D.1.')[0].split('\n\n',1)[1].strip()
printed=raw[:raw.index('The distinction')].strip()
sections.append(definition('pd','D.1.setup',raw,printed,'The exact radius 216','The boundary parameter and its height.','outer'))
for id,uses,summary in [
 ('D.1.1','FAM C.1.1 and A.4.1; ARI C.2.1; modular invariance of j','The Albanese j-invariant has a natural boundary at |w|=216.'),
 ('D.1.2','Grauert direct-image and proper-mapping theorems with the 1963 correction; Ehresmann; Buchdahl Theorem 11','An intrinsic reduced anticanonical surface family exists off a countable exceptional set.'),
 ('D.1.3','FAM A.1.1; PUSH D.1.1 and D.1.2','No flat proper analytic extension crosses any point of the outer circle, even fibrewise.')]:
 sections.append(emit('pd',id,'T',uses,summary,'outer'))

sections.append('\\subsection{The specified pinching and its virtual Euler number}\n')
raw=texts['pab'].split('\\begin{proposition}[A.1.1')[0].split('\n\n',1)[1].strip()
printed=normalize(raw,'PUSH','pab')
printed=printed.replace("Engel's Lemma 2.1",r'\cite[Lemma~2.1]{E26}').replace('his\nCorollary 2.2',r'\cite[Corollary~2.2]{E26}')
printed=printed.replace('The source being checked is the attached version of\n\\cite{E26}, not a later inference from its conjecture.','')
sections.append(definition('pab','A.1.setup',raw,printed,'E26 Lemma 2.1 and Corollary 2.2','The ruled normalization, specified pinching Q and linearization line.','pinching',credit='E26 §2 Lemma 2.1, Corollary 2.2 and §8 Conjecture 8.2; PUSH fixes the exact pinching convention.'))
quote_match=re.search(r'\\begin\{conjecture\}\s*(There is a flat, proper filling[\s\S]*?)\\end\{conjecture\}',prior['E26'])
raw=quote_match[1].strip()
quote=raw.replace(r'\cX',r'\mathcal X').replace(r'\bP',r'\mathbb P').replace(r'\cO',r'\mathcal O')
# The quotation retains the source symbol M; the adjoining dictionary identifies it.
sections.append('\\begin{refuted}[E26 Conjecture 8.2; false as worded]\\label{e26:Conjecture8.2}\n'+quote+'\n\\end{refuted}\n'+r"\noindent\emph{Uses:} the untwisted family and the specified pinching of \cite[Conjecture~8.2]{E26}. In this quotation $M$ is Engel's bundle $M_S$.\par"+'\n')
records.append({'paper_label':'e26:Conjecture8.2','statement_as_printed':quote,'status':'false as worded','source_run':'E26','source_id':'Conjecture 8.2','source_file':'papers/arXiv_2609.38442_Engel_src/S6.tex','wording_vs_source':'same content: prose quoted verbatim; only cX,bP,cO macros expanded for the common preamble. Source M is retained inside the quotation and identified with M_S outside it.','found_in_AC26':'not found: searched flat proper filling, virtual, pinching; the conjecture is E26’s.','found_in_E26':'found: §8 Conjecture 8.2, source lines 1673–1676, opened and quoted.','found_in_DGKX_v1':'not found: searched Conjecture 8.2, flat proper filling, virtual, pinching.','credited_to':'Engel, E26 Conjecture 8.2.','checks':'S: exact supplied source opened; source-to-quotation comparison changes macro spelling only. Refutation count is PUSH A.3.2, not attributed to this citation.','source_statement':raw,'summary':'The specified nonnormal pinching is conjectured to fill the untwisted family.','one_line':'The specified nonnormal pinching is conjectured to fill the untwisted family.','kind':'Counterexample target','uses':'E26 §8 specified untwisted family','proof_location':'Refuted by PUSH A.3.2 in text','source_line':prior['E26'].count('\n',0,quote_match.start())+1})
comparisons.append({'paper_label':'e26:Conjecture8.2','source_file':'papers/arXiv_2609.38442_Engel_src/S6.tex','diff':list(difflib.unified_diff(raw.splitlines(),quote.splitlines(),fromfile='E26 source',tofile='paper quotation',lineterm=''))})
sections.append(emit('pab','A.3.1','T',r'The local-complete-intersection deformation calculation; Levy Lemmas 3.1--3.2; \L{}ojasiewicz \S3 Theorems 1--2','The intrinsic virtual Euler number equals that of every smooth proper-flat smoothing.','pinching'))
u=unit('pab','A.3.2')
full=normalize(u['body'],'PUSH','pab')
partition=full.index('The proper nodal')
tpart=full[:partition].strip()
apart=full[partition:].strip()
sections.append(emit('pab','A.3.2','T','PUSH A.3.1; the specified pinching; the Euler number two of the chosen untwisted family','The specified pinching has virtual Euler number zero and cannot fill Engel’s family.','pinching','Counterexample',body_override=tpart,wording='changed: the source statement is partitioned by the binding statuses. Its Euler-number obstruction and refutation of E26 Conjecture 8.2 are printed here as T; its final replacement sentence is printed separately as A with source ID A.3.2. No mathematical sentence is removed or changed in scope; common notation and locators are normalized.'))
row('pab','A.3.2',apart,'A','PUSH A.1.2 and A.2.2','The nodal and two semistable constructions are precise replacements with different central fibres.','Counterexample replacement','pinching',raw=u['body'],line=u['line'],label='push:A.3.2.replacement',wording='changed: exact final mathematical sentence of source A.3.2 is partitioned from its T obstruction and printed with A status, as required for corrected fillings. Only run-prefixed cross references change.',proofloc='Repository: PUSH A.1.2 and A.2.2')
sections.append('\\begin{announcement}[PUSH A.3.2, final sentence; A]\\label{push:A.3.2.replacement}\n'+apart+'\n\\end{announcement}\n'+r'\noindent\emph{Uses:} PUSH A.1.2 and A.2.2.\par'+'\n'+r'The mechanism changes the central fibre through the nodal construction or one of the two toroidal resolutions described below.'+'\n\n'+r'\noindent\emph{Proof:} proof in the repository, PUSH A.1.2 and A.2.2 (\url{https://github.com/KokunoYumeto/s6-complex-structure-workbench}).'+'\n')
sections.append(r'''\paragraph{Counterexample checklist.}
The target is the exact pinching $Q$ in the quotation. Its normalization
and gluing are fixed in Definition~\ref{push:A.1.setup}; its reduced local
complete-intersection structure is the local equation $xy=0$ used in
the proof. Statement~\ref{push:A.3.1} applies to every proper flat smooth
smoothing of that $Q$, without a projectivity or K\"ahler assumption.
Statement~\ref{push:A.3.2} gives the conflicting counts $0$ and $2$.
The announced replacements change the central fibre, and the nodal
replacement also changes the nonzero fibres by the specified contraction.
''')
sections.append('\\subsection{Announced corrected fillings}\n')
raw=unit('pab','A.1.1')['proof'].split('When $h_q=0$')[0].strip()
printed=normalize(raw,'PUSH','pab')
sections.append(definition('pab','A.1.fan',raw,printed,'The cusp cocharacter lattice','The cones of the two-parameter cusp fan.','pinching'))
amechanisms={
 'A.1.1':r'The mechanism is the rectangle tiling in the cocharacter lattice and the dual-monoid equation $xy=ut_c$.',
 'A.1.2':r'The mechanism glues a compact annular core to the global node bundle $a\otimes b=u\phi_x$, using the two specified collars. At the nodal elliptic fibre, the chart $xy=uzv$ produces the stated ordinary double point and its prescribed contraction.',
 'A.2.1':r'The mechanism enumerates the unimodular triangulations of the six-ray prism and imposes the period identifications. Joint flatness excludes a ray over the origin of the two-dimensional base; without that restriction, the stated period-invariant point stars give arbitrarily many refinements.',
 'A.2.2':r'The mechanism applies either of the two period-invariant subdivisions to the proper nodal construction and leaves the other charts unchanged. The central heights determine the reduced normal crossings, and the conductor normal-bundle calculation gives the trivial product.',
 'A.2.3':r'The mechanism is the new complete toric component in a maximal-cone star. Its second Betti number obstructs the proposed bimeromorphic map to the ruled threefold; the finite star-chart description is retained in its place.',
 'A.2.4':r'The mechanism enumerates a finite height-bounded collection of primitive rays, tests unimodularity and rational face intersections, and imposes the two period identifications. Increasing the bound exhausts the finite invariant subdivisions, while the star fans record the central normalizations and their multiplicities.',
 'A.2.5':r'The mechanism compares finite marked cone complexes through ordinary star blow-ups and their inverse moves. The local monomial Jacobian quotient records the deformation sheaf with its stated nonreduced scope.',
}
asumm={
'A.1.1':'The unsubdivided cusp chart is xy=uzv, with cusp coordinate t_c=zv.',
'A.1.2':'A proper nodal filling contracts the specified (-1,-1) curve on each nonzero fibre.',
'A.2.1':'Exactly two subdivisions satisfy the joint-flatness and reducedness restrictions.',
'A.2.2':'The two natural semistable fillings have the stated normalized central fibres.',
'A.2.3':'The unrestricted blow-up shape is false; star charts supply its replacement.',
'A.2.4':'Finite fan data enumerate all invariant smooth refinements in the stated scope.',
'A.2.5':'A terminating blow-up/blow-down algorithm describes normalization comparisons.',
}
for id in ['A.1.1','A.1.2','A.2.1','A.2.2','A.2.3','A.2.4','A.2.5']:
 if id=='A.2.1':
  raw=unit('pab','A.2.1')['proof'].split('A triangular prism')[0].strip()
  sections.append(definition('pab','A.2.rays',raw,normalize(raw,'PUSH','pab'),'PUSH A.1.1','The six cusp rays and retained bottom diagonal.','pinching'))
 if id=='A.2.4':
  p=unit('pab',id)['proof'];end=p.index('One closed fundamental cone')
  raw=p[:end].strip()
  aa=p.index('In a unimodular chart');bb=p.index('The total space is smooth.',aa)
  raw+='\n\n'+p[aa:bb].strip()
  sections.append(definition('pab','A.2.periods',raw,normalize(raw,'PUSH','pab'),'PUSH A.2.4, finite fan coordinates','The period shears after the base change u=r^n.','pinching'))
 key='alg' if id=='A.2.5' else 'pab'
 uses={'A.1.1':'PUSH A.1.fan','A.1.2':'PUSH A.1.1; E26 Lemma 2.1 and Corollary 2.2','A.2.1':'PUSH A.1.1 and the retained bottom triangulation','A.2.2':'PUSH A.1.2 and A.2.1','A.2.3':'PUSH A.2.4 and A.2.5','A.2.4':'PUSH A.1.1 and the explicit base-changed period shears','A.2.5':'PUSH A.2.4 and its marked star charts'}[id]
 sections.append(emit(key,id,'A',uses,asumm[id],'pinching',kind='Counterexample' if id in ['A.2.3','A.2.5'] else 'Theorem',mechanism=amechanisms[id]))

sections.append(r'''\section{Announcements at the puncture and in the space of structures}
\label{sec:announcements}
\subsection{The fixed-family noncompletion statement}
''')
conv=texts['pushconv']
raw=conv[conv.index('The first two have orders'):conv.index('We use the period matrix')].strip()
raw+='\n'+conv[conv.index("The untwisted family is"):conv.index('Engel\'s indices')].strip()
printed=raw.replace('The first two have orders $3,4$; the last is unipotent. We put','The retained sphere family has multiplicities $(3,4)$ and the fixed data')
printed=printed.replace('and\n$p=',r'and $p=')
sections.append(definition('pushconv','B.4.33.scope',raw,printed,'The first-run retained data','The fixed sphere family and its distinction from Engel’s untwisted family.','nonfill'))
sections.append(emit('nonfill','B.4.33','A','PUSH B.4.31 and B.4.32; the actual fixed punctured sphere family','The retained family has no proper Hausdorff analytic filling after a finite parameter cover.','nonfill',mechanism='The mechanism passes from a proposed filling to a marked proper map and controls the radial-loop class through differences of extending sections. The resulting specific logarithmic torsor contradicts the nonzero degree; an arbitrary affine origin is not asserted to extend.'))
sections.append(r'''The assertion has the fixed-family scope just stated. Whether the same
noncompletion holds for every admissible twist remains a question.
The proposed reading of a monodromy integer as $J=P\mathbin{.}O$ is a
reader's remark recorded in the intake; it is unverified and is not a
theorem or a premise of this paper.
\subsection{Smooth monodromy: two runs and two methods}
''')
raw=conv[conv.index('The six-sphere has its complex orientation'):conv.index('A smoothing and a resolution')].strip()
sections.append(definition('pushconv','C.orientation',raw,raw,'The complex orientation and the positive parameter circle','Mapping-torus, sphere-gluing and Theta7 orientation conventions.','smoothmono'))
raw=unit('cpush','C.4.1')['body']
printed=r'The twist comparison used in PUSH C.3.24 has fixed multiplicities $(3,4)$ and the admissible sphere data $|p|=1$ of FAM B.2.1. Its monodromy convention is the positive $w$-circle with the complex orientation on every fibre.'
sections.append(definition('cpush','C.4.1.scope',raw,printed,'FAM B.2.1; PUSH C.4.1','The exact twist-comparison scope used in PUSH C.3.24.','smoothmono'))
sections.append(emit('mono1','C.3.24','A','PUSH C.3.18, C.3.21–C.3.23 and C.4.1','The actual positive-loop mapping class is zero in Theta7, by the orbit-knot method.','smoothmono',mechanism=r'The mechanism is an integer calculation before reduction modulo $28$: the source gives $p_{\rm rel}=-24$, $s_\delta=-2$ and $J_\psi=\epsilon_{\rm cap}(-24-12(-2))/24=0$. Additivity compares the six-loop representative to six times the one-loop integer.'))
sections.append(emit('mono2','C.3.27','A','PUSH C.3.25 and C.3.26; the shared characteristic calculations C.3.18–C.3.22','A spin-c coboundary and direct index additivity give a second zero determination.','smoothmono',mechanism=r'The mechanism uses the explicit eight-dimensional spin$^c$ coboundary and the integer index $\lambda=(p_\psi-4k_\psi)/24$, with $p_\psi=-24\epsilon_{\rm cap}$ and $k_\psi=-6\epsilon_{\rm cap}$. The boundary-invariant and one-loop arguments differ from the orbit-knot method; the actual annular representative and characteristic inputs are shared.'))
sections.append(emit('maps','B.6.21','A','MAPS B.6.15–B.6.20 and the specified mapping-torus comparison','The MAPS calculation gives the original (3,4) positive-loop class zero.','smoothmono',mechanism=r'The mechanism uses the free-circle replacement with its actual peripheral identifications, the values $k=-1$ and $\ell=-4$, and the parametrized spin-surgery trace. Its normalized correction is zero, so the specified Eells--Kuiper invariant selects the original residue $0$.'))
general=unit('general','E.1.1')['body']
raw=general[general.index('With the counterclockwise deck generators'):general.index('The brackets in')].strip()
printed=r'''For the higher-family announcements, $m=3k$, $n=4l$,
$\gcd(m,n)=1$, and $k,l>0$. A fixed sphere twist datum in the K1 scope
of MAPS means fixed integers $\rho_0,N_0,\rho_1,N_1$ with
\[
 w_1=N_0\varepsilon-\rho_0\widehat\delta,\qquad
 w_2=N_1\varepsilon'-(\rho_1+N_1)\widehat\delta,\qquad l_0=0,
\]
and $nN_0+mN_1=\pm1$, in the admissible period domain. The vectors are
the first-run clockwise-root vectors; the original K1 data use the
transported counterclockwise-root marking. The parameter period is
$2kl\mathbb Z$.'''
sections.append(definition('general','E.1.1.scope',raw,printed,'PUSH E.1.1–E.1.3; FAM B.3.1','The fixed coprime sphere-pair and twist scope of the higher-family announcements.','components',credit='PUSH E.1.1 dictionary and FAM B.3.1; the definition records the exact K1 sphere-data scope.'))
sections.append(emit('maps','B.6.24','A','The fixed K1 twist datum; MAPS B.6.19 and B.6.22–B.6.23','All stated coprime sphere-pair monodromy classes vanish in Theta7.','smoothmono',mechanism=r'The mechanism is the higher-family free-circle quotient calculation $k_{\rm cup}=-kl$, $\ell=-4kl$, followed by the signed spin-surgery trace and the mapping-torus comparison. This is the source statement for every fixed K1 datum in the stated scope.'))
sections.append(r'''The last announcement has a broader scope than MAPS B.6.21, whose
last sentence is retained. The supplied open-problem list also calls
``the monodromy of the other families'' open. Those wordings are not
silently identified: MAPS B.6.24 announces zero for the explicitly
specified coprime sphere pairs and fixed K1 data, while an open question
beyond that scope is not answered here.
\subsection{Families and components of the space of structures}
''')
raw=unit('specialization','E.2.5')['body'].split('There is a unique')[0].strip()
raw+='\n'+unit('zero','E.2.7')['body'][unit('zero','E.2.7')['body'].index('Normalize the punctured'):unit('zero','E.2.7')['body'].index('The resulting holomorphic')].strip()
printed=r'''The smooth-completion hypotheses used below are those of PUSH E.2.5:
$\pi:\mathcal X\to\Delta$ is a proper holomorphic submersion,
all fibres are diffeomorphic to $S^6$, and every noncentral fibre belongs
to one fixed coprime multiplicity family $(3k,4l)$ of PUSH E.2.1.
The integers in that statement are $A=12kl$ and $D=kl-3k-4l\ne0$.
For fixed discrete logarithmic data, the isomorphism parameter of
PUSH E.2.7 is denoted here by
\[
 w_{k,l}=\exp\!\left(-\frac{\pi i c}{kl}\right).
\]
The symbol $z$ in those source statements denotes this parameter,
not the uniformizing coordinate of the first-run conventions.'''
sections.append(definition('specialization','E.2.5.scope',raw,printed,'PUSH E.2.5 and E.2.7','The precise smooth-specialization hypotheses and fixed-pair parameter.','components'))
for key,id,uses,summary,mech in [
 ('global','E.2.21','PUSH E.2.5, E.2.7 and E.2.10–E.2.20','A smooth completion is an actual member at an interior fixed-pair parameter.','The mechanism extends the intrinsic pencil and its nonzero interior period, identifies the ordinary marked Jacobian, and glues the finite-root and cusp comparisons using the connected translation group.'),
 ('disc','E.2.22','PUSH E.2.1 and E.2.21','A fixed constructed pair propagates from a nonempty open subset of a disc.','The mechanism propagates the geometric data outside successive discrete analytic exceptional sets and then fills those sets in reverse order by the smooth-completion comparison.'),
 ('bases','E.2.23','PUSH E.2.21 and E.2.22; local miniversality','Proper smooth deformation chains preserve the ordered coprime multiplicity pair.','The mechanism combines propagation on Riemann surfaces with the local analytic-base argument. It uses the constructed fixed-pair locus and does not assume that a punctured analytic disc can be selected inside an arbitrary open set.'),
 ('continuous','E.2.24','PUSH E.2.23 and local completeness of the deformation charts','Each fixed-pair locus is open and closed in the space of integrable structures.',r'The mechanism transfers the analytic-family separation to the local deformation charts in the smooth topology of \cite[\S2.1 and \S3.2, Theorem~3.4 and Remark~3.6]{Meersseman2019E}, and then to the indicated quotient spaces. It supplies no count of marked connected components within a single pair.')]:
  body=normalize(unit(key,id)['body'],'PUSH',key)
  if id=='E.2.21':
   body=body.replace('E.2.5',r'Definition~\ref{push:E.2.5.scope}').replace('$z(0)$','$w_{k,l}(0)$').replace('E.2.7','PUSH E.2.7')
  if id=='E.2.23':body=body.replace(', and E.2.4 is resolved by this theorem','')
  sections.append(emit(key,id,'A',uses,summary,'components',body_override=body,mechanism=mech,wording='same mathematical content: source internal references are made explicit, the parameter z is written w_{k,l}, and the editorial claim that an old question is resolved is omitted where present. All hypotheses and conclusions are retained.'))

def save():
 OUT.mkdir(parents=True,exist_ok=True)
 (OUT/'sections.tex').write_text('% Source-faithful fragments for §§7–11. Generated by build_geometry.py.\n'+''.join(sections))
 (OUT/'appendix_b_aut.tex').write_text('% Re-derivation of the credited full automorphism theorem.\n'+''.join(appendix))
 (OUT/'records.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
 (OUT/'statement_comparisons.json').write_text(json.dumps(comparisons,ensure_ascii=False,indent=2)+'\n')
 (OUT/'proof_comparisons.json').write_text(json.dumps(proof_comparisons,ensure_ascii=False,indent=2)+'\n')
 (OUT/'credit_searches.json').write_text(json.dumps(credit_searches,ensure_ascii=False,indent=2)+'\n')

if __name__=='__main__':
 # Explicitly identify contextual extracts rather than inventing source statement numbers.
 ctx={
 'maps:A.3.setup':'A.3 (opening conventions)',
 'maps:A.3.representatives':'A.3, equations (A.3.1)–(A.3.2)',
 'fam:F.setup':'F (opening conventions)',
 'fam:F.2.setup':'F.2 (definition preceding F.2.1)',
 'fam:D.1.Hermitian':'D.1.6 (proof, Hermitian-form convention)',
 'push:D.1.setup':'D (opening definitions)',
 'push:A.1.setup':'A.1 (opening definitions)',
 'push:A.1.fan':'A.1.1 (proof, cone definition)',
 'push:A.2.rays':'A.2.1 (proof, six rays and bottom diagonal)',
 'push:A.2.periods':'A.2.4 (proof, base-changed period shears)',
 'push:B.4.33.scope':'Conventions; B.4.33 (scope)',
 'push:C.orientation':'Conventions (mapping-torus orientation)',
 'push:C.4.1.scope':'C.4.1 (scope)',
 'push:E.1.1.scope':'E.1.1 (sphere data); FAM B.3.1 (parameter lattice)',
 'push:E.2.5.scope':'E.2.5 (hypotheses); E.2.7 (parameter)',
 }
 ctx_edits={
 'maps:A.3.setup':'changed: the opening cusp-curve definitions are made a numbered definition; the unused local g alias is removed, and rho_circ(b) is explicitly the translation action of FAM B.4.1. The source circle rho is renamed rho_circ to reserve rho=exp(pi*i/3) for the period constant. The three named double curves and the distinction between D1 and D2 are unchanged.',
 'maps:A.3.representatives':'changed: the prose introducing the fixed representatives is shortened; source g is written hat-gamma, and d in the fibre translation is written e=Pi_c hat-delta, with the type identification stated explicitly. Root/logarithm branches, representatives c, alpha, S(t) and every constant are unchanged. Original equation tags acquire a MAPS prefix.',
 'fam:F.setup':'changed: the source opening conventions become a definition; first page is replaced by our conventions; source lattice e becomes d, E=e tensor gamma becomes E=d tensor gamma, and dual covectors u,w are written u_Lambda,w_Lambda. The domain, signature, action and proper-discontinuity definition are unchanged.',
 'fam:F.2.setup':'same content: the source definition is set as a formal definition, with q_e renamed q_d and every lattice e (including Je) renamed d. Both sign regions and the invariance statement are retained.',
 'push:D.1.setup':'changed: H_*, c_* and a are extracted as a definition. The source’s subsequent discussion of total quotients and Hausdorff reflections belongs to omitted PUSH D.2 and is not printed here; none of the boundary hypotheses or constants changes.',
 'push:A.1.setup':'changed: opening definitions become formal context; L becomes M_S and the linearization line J becomes J_lin; source prose locator is replaced by exact E26 Lemma2.1/Corollary2.2 citations. The editorial sentence about the attached version is removed. All bundles, intersection calculations, gluing and section data are retained.',
 'push:A.1.fan':'same content: the cone-defining first proof paragraph is extracted into a definition; q and h_q become t_c and h_(t_c). No inequality or height condition changes.',
 'push:A.2.rays':'same content: the six-ray definition and bottom diagonal are extracted from the A.2.1 proof; only surrounding typography changes.',
 'push:A.2.periods':'changed: two exact defining excerpts from the A.2.4 proof (period shears and local monomial equations A.24d) are placed together as context for the announcement. The cusp symbol q is written t_c; no numerical data or equations change.',
 'push:B.4.33.scope':'changed: two passages of the supplied conventions are extracted to fix the actual sphere-family data and distinguish the untwisted quotient. The opening sentence explicitly recalls multiplicities (3,4); no claim about a larger twist class is introduced.',
 'push:C.orientation':'same content: exact supplied convention paragraph made a formal definition.',
 'push:C.4.1.scope':'changed: only the domain of the source C.4.1 comparison is restated as a definition. Source R5 is identified with FAM B.2.1; the theorem’s equality-of-monodromy conclusion is not restated as a new proved claim here.',
 'push:E.1.1.scope':'changed: the fixed first-run translation vectors and sphere condition are extracted from PUSH E.1.1, with its opposite generator convention stated. Positivity of multiplicities and the period lattice from FAM B.3.1 are explicit; no new parameter/twist scope is added.',
 }
 for r in records:
  lab=r['paper_label']
  if lab in ctx:r['source_id']=ctx[lab]
  if lab in ctx_edits:r['wording_vs_source']=ctx_edits[lab]
  if lab in ['fam:D.1.2','fam:D.1.6','fam:D.2.3']:
   r['wording_vs_source']+=' The source heading Known, with derivation is replaced by the binding T heading; the proof remains in the text as explicitly required for §9.'
  if lab=='fam:D.1.6':
   r['found_in_AC26']='found input only: §9.1 Lemma9.2 gives the exact equation used here, with Lemmas9.3–9.4 and Proposition9.5 for generic properties. The displayed exact elliptic/projective loci and full a=0/1/2 test were not found; searched Z_E, Pfaffian, elliptic quotient, algebraic dimension one.'
   r['credited_to']='Classical Appell–Humbert and Riemann criteria (Schnell19 Theorems4.1/4.4), specialized to the AC26 Lemma9.2 equation by FAM D.1.6; source itself labels this Known, with derivation.'
  if lab=='fam:D.1.7':
   r['found_in_AC26']='found input only: §9.1 Lemma9.2 gives the NS equation. No c=-6tau-12mu-beta_part rank-two construction was found; searched its coefficients, Z_E, Pfaffian and algebraic dimension one.'
  if lab=='fam:D.2.3':r['credited_to']='Classical compact-torus divisor theory, with Appell–Humbert and theta equation as in Schnell19 Theorem4.1/equation4.3; FAM applies it to the exact fibre loci and finite covers. Source labels the derivation Known.'
  if lab=='push:E.2.5.scope':
   r['additional_sources']=[{'source_file':'returns/S6_02_PUSH/sections/E_zero_period_obstruction.tex','source_id':'E.2.7 (parameter definition)'}]
   r['wording_vs_source']='changed: the hypotheses of E.2.5 and the parameter definition of E.2.7 are extracted as a standalone definition; no conclusions of those auxiliary propositions are asserted. z is renamed w_{k,l}. Exact extracts are recorded in source_statement and the additional source is listed.'
  if lab=='push:E.1.1.scope':r['additional_sources']=[{'source_file':'returns/S6_02_FAMILY/sections/AB.tex','source_id':'B.3.1 (fixed-data parameter lattice)'}]
  if lab=='maps:A.3.setup':r['additional_sources']=[{'source_file':'returns/S6_02_FAMILY/sections/AB.tex','source_id':'B.4.1 (translation action)'}]
  if lab=='fam:D.1.Hermitian':r['wording_vs_source']='changed: the source D.1.6 Hermitian definitions are moved before D.1.4, with source equation reference retained. The shorthand T=Im(tau), U=Im(mu), D=Im(beta)-6U^2/T is made explicit; the source uses U without a local definition, recorded in discrepancies.md. No formula is altered.'
 save()
 print(f'{len(records)} statement records; {len("".join(sections))} section characters; {len("".join(appendix))} appendix characters')
