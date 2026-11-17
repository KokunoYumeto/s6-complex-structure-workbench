"""Create the in-paper program/command concordance from actual retained files."""
from pathlib import Path
import re,json,ast,hashlib,shlex
OUT=Path(__file__).resolve().parents[2]
s=(OUT/'S6_09_PAPERS_I.tex').read_text()
# Ignore a previous generated index if this script is repeated.
s=s.split('% BEGIN GENERATED PROGRAM INDEX')[0]
names=sorted(set(x.replace('\\_','_').split('/')[-1] for x in
 re.findall(r'(?:code/)?[A-Za-z0-9_\\.-]+\.(?:py|gp|sage)\b',s)))
names=sorted(set(names)|{'paperI_foundation_arithmetic.py','verify_cw_hurewicz.py','verify_path_fibre.py'})
ari=json.loads((OUT/'work/invariants_arithmetic/arithmetic_program_index.json').read_text())
aruns={}
for r in ari['runs']:aruns.setdefault(Path(r['program']).name,[]).append(r)
purpose={
 'cd_bounds.py':'Outward-rounded global norm bounds, cusp-error estimates and the admissible counterexample bound.',
 'cd_exact.py':'Exact period, torsion, Neron--Severi and special-fibre identities.',
 'cd_special_intervals.py':'Outward-rounded special-period and Albanese-constant intervals.',
 'cd_torsion_independent.py':'Independent division-polynomial, Cartan, height and period-image identities.',
 'e_push_source_audit.py':'Reproducible algebra and scope diagnostics; its metadata assertions are not independent source verification.',
 'f_interval_parallel.py':'Schedules the original interval certifier. Its saved box cover is checked exactly and every norm box is independently recertified in Arb.',
 'f_interval_cert.py':'Original outward interval formula and tails. The saved boxes are independently recertified by e4_arb_certificate.py.',
 'paperI_foundation_arithmetic.py':'Independent exact checks of eight construction, affine-overlap, finite-kernel and normal-character scopes; the complete geometric proofs are printed.',
 'verify_cw_hurewicz.py':'Thirty-four retained algebraic and structural checks for the CW/Hurewicz exposition; these do not replace its full topological proof.',
 'verify_path_fibre.py':'Thirty-eight retained algebraic and structural checks for path-fibration and spectral-sequence formulas; the full proof remains analytic and topological.',
}
def esc(x):
 return ''.join({'&':r'\&','%':r'\%','#':r'\#','_':r'\_','$':r'\$','{':r'\{','}':r'\}','~':r'\textasciitilde{}','^':r'\textasciicircum{}','\\':r'\textbackslash{}'}.get(c,c) for c in str(x))
def path(x):return r'\path{'+str(x).replace(' ',r'}\ \path{')+'}'
records=[]
for name in names:
 files=list((OUT/'code').rglob(name))
 assert files,('Cited program missing',name)
 files.sort(key=lambda p:('portable_gp' in str(p),len(str(p))))
 p=files[0];rel=str(p.relative_to(OUT))
 if name in aruns:
  rr=aruns[name]
  cmds=[dict(command=r['command'],cwd=r['cwd'],output=r.get('stdout_capture',''),role=r['statement_role']) for r in rr]
  role=rr[0]['statement_role']
 else:
  if rel.startswith('code/family/'):
   cwd='code/family';cmd=['python',name]
  elif p.parent.name=='code':
   cwd=str(p.parent.parent.relative_to(OUT));cmd=['python','code/'+name]
  else:
   cwd=str(p.parent.relative_to(OUT));cmd=['python',name]
  if name in ['e4_arb_certificate.py','d_push_global_arb.py']:cmd+=['--workers','4']
  try:doc=ast.get_docstring(ast.parse(p.read_text())) or ''
  except Exception:doc=''
  role=purpose.get(name,doc.split('\n')[0])
  if not role:role='Exact identities and numerical checks displayed at this program\'s point of use.'
  outputs=[str(q.relative_to(OUT)) for q in (OUT/'code').rglob('*') if q.is_file() and
    (q.name.startswith(p.stem+'.rerun.') or q.name==name+'.rerun.txt' or q.name==name+'.txt' or q.name==name+'.output.txt')]
  cmds=[dict(command=cmd,cwd=cwd,output='; '.join(outputs),role=role)]
 records.append(dict(program=rel,name=name,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),role=role,runs=cmds))
# The long MPFR streams are compiled programs rather than .py/.gp references.
for name,rr in aruns.items():
 if name not in names:
  records.append(dict(program=rr[0]['program'],name=name,
   sha256=rr[0].get('program_sha256',''),role=rr[0]['statement_role'],
   runs=[dict(command=r['command'],cwd=r['cwd'],output=r.get('stdout_capture',''),role=r['statement_role']) for r in rr]))
records.sort(key=lambda r:r['program'])
(OUT/'records/I_program_index.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
tex=r'''% BEGIN GENERATED PROGRAM INDEX
\section{Programs, certificates and reproducible commands}
\label{app:I:programs}
All paths are relative to the companion archive's root. For each row, change
to the stated working directory and execute the displayed command. Python
programs use Python~3, SymPy, mpmath and, where imported, python-flint~0.9.0.
The latter's retained dependency directory is
\path{code/invariants_arithmetic/dependencies}; it may be placed on
\texttt{PYTHONPATH}. The PARI/GP calculations use PARI~2.15.2 with its
elliptic-curve data. MPFR programs use directed rounding and explicit tails;
their build commands are displayed below. A numerical diagnostic is labelled
as such and supplies no rigorous inequality. The proofs specify the exact
identity, interval separation or exhaustion established by each certificate.

The rational cover contains 19,701 norm boxes; the independent Arb pass
certifies all of them. The gradient argument's refinement has 19,755 leaves.
The original parallel runner is retained, while its scheduling is not an
additional proof step. The obsolete initial global-meridians assertion is
not used: the corrected program and independent quotient fixed-space check
are the operative certificates. All original failed setup outputs and their
successful dependency-ordered reruns remain in the verification archive.

\begingroup\small
\begin{longtable}{@{}p{48mm}p{56mm}p{44mm}@{}}
\toprule Program and purpose & Working directory; command & Output/role\\\midrule
\endfirsthead
\toprule Program and purpose & Working directory; command & Output/role\\\midrule
\endhead
'''
for r in records:
 for j,cmd in enumerate(r['runs']):
  label=path(r['name'])+r'\par '+esc(r['role']) if j==0 else path(r['name'])+' (additional run)'
  run=path(cmd['cwd'])+r'\par '+path(shlex.join(cmd['command']))
  output=cmd.get('output','')
  last=path(output) if output and '; ' not in output else 'Retained standard output and error log; exact paths and hashes in the command manifest.'
  tex+=label+' & '+run+' & '+last+r'\\'+'\n'
tex+=r'\bottomrule\end{longtable}\endgroup'+'\n'
tex+=r'\subsection{Compiled directed-rounding programs}'+'\n'
for b in ari['build_commands']:
 tex+='In '+path(b['cwd'])+', run '+path(shlex.join(b['command']))+'.\n\n'
tex+='The complete run manifest records every command, input hash, output hash, precision and truncation bound. Commands with differing discriminants or precisions are separate runs in the table.\n% END GENERATED PROGRAM INDEX\n'
(OUT/'editorial/I_programs.tex').write_text(tex)
print('Program records:',len(records),'explicit commands:',sum(len(r['runs']) for r in records))
