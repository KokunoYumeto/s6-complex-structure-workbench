from pathlib import Path
import re,json,csv,hashlib,shutil
root=Path('/workspace/scratch/037cd144174c');out=root/'deliverables/work/invariants_arithmetic';out.mkdir(exist_ok=True)
manifest=json.loads((out/'initial_manifest.json').read_text())
for prefix in ['C','B_C6']:
 for p in (root/'sources/returns/S6_05_ARITHMETIC/code').glob(prefix+'*'):
  if p.is_file():shutil.copy2(p,root/'deliverables/code/invariants_arithmetic/arithmetic/code'/p.name)
for p in (root/'sources/returns/S6_05_ARITHMETIC/records').iterdir():
 if p.is_file() and (p.name.startswith('C') or p.name.startswith('B_C6')) and p.suffix in ['.json','.csv','.txt','.log','.tex']:
  shutil.copy2(p,root/'deliverables/code/invariants_arithmetic/arithmetic/records'/p.name)
for p in (root/'sources/returns/S6_05_ARITHMETIC').glob('results_C*.csv'):
 shutil.copy2(p,root/'deliverables/code/invariants_arithmetic/arithmetic'/p.name)
# These declarations only supply source commands; root's unified preamble remains authoritative.
(out/'sections/macros_needed.tex').write_text(r'''\providecommand{\Pone}{\mathbb P^1}
\providecommand{\ddbar}{\partial\bar\partial}
\providecommand{\dd}{\,\mathrm d}
\providecommand{\Imn}{\operatorname{Im}}
\providecommand{\Ren}{\operatorname{Re}}
\providecommand{\Nm}{\operatorname{Nm}}
\providecommand{\Sha}{\operatorname{Sha}}
\providecommand{\divisor}{\operatorname{div}}
''')
fixes=[];sources={};candidates={}
for part in ['A','B','C','D']:
 p=root/f'sources/returns/S6_01_INVARIANTS/fragments/part_{part}.tex';s=p.read_text();sources[str(p.relative_to(root))]=s
 if part=='B':
  start=s.index('For the integral markings we apply');end=s.index('\\end{proof}',start)
  s=s[:start]+r'''For the integral marking fixed in the conventions, use
\[
 P_{\rm mark}=\begin{pmatrix}0&-2&-1&-2\\2&-1&0&-1\\0&2&1&3\\-1&0&0&0\end{pmatrix}.
\]
With the monodromy matrices in the construction, direct multiplication gives
$\det P_{\rm mark}=-1$, $T_0P_{\rm mark}=P_{\rm mark}A_1$ and
$T_1P_{\rm mark}=P_{\rm mark}A_2$. A positive base meridian ends at the
inverse root-deck translate, and its endpoint identification applies the
clockwise root generator; thus its homology action is $A_j$.
Because $A_jv_j=v_j$, the inverse affine generator has translation
$-v_j/m_j$. Its Engel coordinates are therefore
$a_0=-P_{\rm mark}v_1/3$ and $a_1=-P_{\rm mark}v_2/4$.
The chosen reference inverse lift is the transported lift at $c=0$.
Consequently $\lambda_0=1$ and $u=e^{-2\pi i c}=w^2$.

For concordance, the reversed-meridian intertwiner in the invariant run was
\[
 Q=\begin{pmatrix}2&-1&0&-2\\2&-1&0&-1\\0&2&1&3\\1&0&0&0\end{pmatrix}
   =P_{\rm mark}
 \begin{pmatrix}-1&0&0&0\\-6&0&-1&0\\6&-1&0&0\\2&1&1&1\end{pmatrix}.
\]
It satisfies $T_0Q=QA_1^{-1}$ and $T_1Q=QA_2^{-1}$, hence uses a
different meridian convention. The displayed transition matrix is part
of the notation translation; $Q$ is not identified with $P_{\rm mark}$.
The theta-quotient argument above identifies the marked holomorphic
families in the convention fixed here and retains all integral collar
translations.
''' + s[end:]
  s=s.replace('The lattice matrix, meridian orientations, line bundle and parameter\ncomparison stated on the first page identify the two marked smooth\nfamilies. The ambiguity in $u$ is exactly multiplication by the\nnonzero constant specifying Engel\'s reference linearization.', 'The theta quotient identifies the period family with the line-bundle\nquotient in Engel\'s construction. In the marking and reference\nlinearization fixed in the conventions, $u=w^2$. Replacing that\nreference multiplies $u$ by the corresponding nonzero constant.')
  fixes.append({'id':'INV B1.0','change':'Translate the reversed-meridian source dictionary Q to the required P_mark convention, display Q=P_mark S explicitly, and fix the transported reference lambda_0=1. Retain the full theta-quotient proof.','reason':'Source and required family meridian conventions differ; Q and P_mark are not interchangeable.'})
 if part=='C':
  s=s.replace('disputed value','evaluated value')
 if part=='D':
  pos=s.index('\\paragraph{Provenance of the tangent argument.}')
  s=s[:pos]+r'''\paragraph{Source and re-derivation of the tangent theorem.}
The tangent cohomology $(1,1,1,0)$ and the smooth one-dimensional
Kuranishi germ are theorems of Du, Guo, Kusakabe, and Xie,
arXiv:2610.00250v1, Section~6 \citep{DuEtAl2026v1}.
The invariant run re-derived these results after reading that paper.
The present proof prints the root-base calculation, its local
comparisons, and the additional coarse direct images and all Picard
twists. Version~2 \citep{DuEtAl2026v2} does not contain the deformation
section; this does not alter the credit for the version~1 theorems.
'''
  s=s.replace('A/(t-t_*)^2','A/((t-t_*)^2)')
  fixes.append({'id':'INV D1.3; D2.1; D3.1','change':'Credit DGKX v1 theorems as re-derived; remove source wording treating their theorem status as merely asserted/superseded.','reason':'User credit requirement and the v1 theorem statements.'})
 # Keep full proof text; only namespace theorem environments and cross references.
 def claim(m):
  sid,status,title=m.groups();env='question' if status=='Open' else 'proposition'
  return '\\begin{'+env+'}[INV '+sid+'; '+status+': '+title+']\\label{inv:'+sid+'}'
 s=re.sub(r'\\begin\{claim\}\{([^}]+)\}\{([^}]+)\}\{([^\n]+)\}',claim,s)
 # claim endings know all are proposition except the sole open question.
 s=s.replace('\\end{claim}','\\end{proposition}')
 op=s.find('\\begin{question}[INV C3.8;')
 if op>=0:
  en=s.find('\\end{proposition}',op);s=s[:en]+s[en:].replace('\\end{proposition}','\\end{question}',1)
 def nslab(m):
  a=m.group(1);return '\\label{'+(a if a.startswith('inv:') else 'inv:'+a)+'}'
 s=re.sub(r'\\label\{([^}]+)\}',nslab,s)
 def nsref(m):
  cmd,arg=m.groups();args=[]
  for a in arg.split(','):
   if a.startswith('st:'):a='inv:'+a[3:]
   elif not a.startswith('inv:'):a='inv:'+a
   args.append(a)
  return '\\'+cmd+'{'+','.join(args)+'}'
 s=re.sub(r'\\(ref|eqref|cref|Cref|pageref)\{([^}]+)\}',nsref,s)
 name=f'inv_part_{part}.tex';candidates[name]=s
 (out/'sections'/name).write_text('% Complete proof candidate. Individual check status is in result_audit.json.\n'+s)
# All Part-C sections, including every intermediate identity and open-route analysis.
ari_files=['C_special','C_heights','C_rank','C_gz_factors','C_torsion_heights','C_analytic','C_integral','C_measure','C_critical','C_periods','C_cm_transcendence','C_padic','C_diagonal_obstruction','C_cm_enlargement','C_complexified','C_division_values']
for f in ari_files:
 p=root/f'sources/returns/S6_05_ARITHMETIC/sections/{f}.tex';s=p.read_text();sources[str(p.relative_to(root))]=s
 s=s.replace('\\input{sections/C_height_tables.tex}',(root/'sources/returns/S6_05_ARITHMETIC/sections/C_height_tables.tex').read_text())
 if f=='C_special':
  s=s.replace('hitting $y=T$ would give a pole.', 'hitting $y=T$ would give another half-period zero. Either event\nwould force $g_3=0$.')
  fixes.append({'id':'ARI C.1.2','change':'Replace the y=T pole assertion by a half-period zero and g3=0 contradiction.','reason':'At tau=1/2+iT, mu=1/2-iT is congruent to 1/2 modulo the lattice, not to zero.'})
 if f=='C_critical':
  # beta is only the scalar cusp constant in this section; w only Cayley coordinate.
  s=re.sub(r'\\beta\b',r'\\beta_{\\rm cusp}',s)
  s=re.sub(r'(?<![A-Za-z\\])w(?![A-Za-z])',r'\\chi',s)
  fixes.append({'id':'ARI C.8.12-C.8.15','change':'Rename the Cayley coordinate w to chi and the scalar cusp beta to beta_cusp.','reason':'Avoid conflict with the global parameter w=exp(-pi i c) and the period beta.'})
 def statement(m):
  title=m.group(1);sid=title.split(';')[0].strip();return '\\begin{proposition}[ARI '+title+']\\label{ari:'+sid+'}'
 s=re.sub(r'\\begin\{statement\}\[([^\]]+)\]',statement,s).replace('\\end{statement}','\\end{proposition}')
 s=re.sub(r'\\label\{([^}]+)\}',lambda m:'\\label{'+(m[1] if m[1].startswith('ari:') else 'ari:'+m[1])+'}',s)
 s=re.sub(r'\\(ref|eqref|cref|Cref|pageref)\{([^}]+)\}',lambda m:'\\'+m[1]+'{'+','.join(a if a.startswith('ari:') else 'ari:'+a for a in m[2].split(','))+'}',s)
 name='ari_'+f[2:]+'.tex';candidates[name]=s
 (out/'sections'/name).write_text('% Complete proof candidate. Individual check status is in result_audit.json.\n'+s)
# Exact statement/proof locators for every final source row.
rows=[]
for r in manifest:
 ns='inv' if r['source_run']=='S6_01_INVARIANTS' else 'ari';sid=r['id']
 found=[]
 for path,s in sources.items():
  pat=r'\\begin\{claim\}\{'+re.escape(sid)+r'\}' if ns=='inv' else r'\\begin\{statement\}\['+re.escape(sid)+r';'
  m=re.search(pat,s)
  if not m:continue
  env='claim' if ns=='inv' else 'statement';ee=s.index('\\end{'+env+'}',m.end())+len('\\end{'+env+'}')
  pe=ee;pm=re.match(r'\s*\\begin\{proof\}(?:\[[^\]]*\])?',s[ee:])
  if pm:pe=s.index('\\end{proof}',ee+pm.end())+len('\\end{proof}')
  sourceblock=s[m.start():pe];ep=out/'extracted'/f'{ns.upper()}_{sid.replace(".","_")}.tex';ep.write_text(sourceblock+'\n')
  found.append((path,s.count('\n',0,m.start())+1,s.count('\n',0,ee)+1,s.count('\n',0,pe)+1,str(ep.relative_to(root/'deliverables')),s[m.start():ee]))
 if len(found)!=1:raise Exception((sid,len(found)))
 path,ls,le,lp,ep,statement=found[0]
 row=dict(r);row.update(source_id=sid,paper='I',printed_label=f'{ns}:{sid}',source_file=path,statement_start_line=ls,statement_end_line=le,proof_end_line=lp,source_statement=statement,source_proof_file=ep,source_sha256=hashlib.sha256((root/path).read_bytes()).hexdigest(),candidate_file=f'work/invariants_arithmetic/sections/'+(f'inv_part_{sid[0]}.tex' if ns=='inv' else next(k for k,v in candidates.items() if f'\\label{{ari:{sid}}}' in v)),recorded_checks=[],own_check={'checker':'GPT-6 Astra (OpenAI, ChatGPT Pro mode)','effort':'Pro','date':'2026-11-17','state':'pending audit record integration'},credit_checks=[],taken_over_by='',change_notes=[x for x in fixes if sid in x['id']])
 rows.append(row)
(out/'result_audit.json').write_text(json.dumps(rows,indent=2)+'\n')
with (out/'result_audit.csv').open('w') as h:
 w=csv.DictWriter(h,fieldnames=list(rows[0]));w.writeheader()
 for r in rows:w.writerow({k:json.dumps(v,ensure_ascii=False) if isinstance(v,(dict,list)) else v for k,v in r.items()})
(out/'corrections.json').write_text(json.dumps(fixes,indent=2)+'\n')
(out/'section_order.json').write_text(json.dumps([f'inv_part_{p}.tex' for p in 'ABCD']+['ari_'+f[2:]+'.tex' for f in ari_files],indent=2)+'\n')
print('Saved',len(rows),'complete source proof blocks and',len(candidates),'full namespaced section candidates;',len(fixes),'normalization/correction records.')
