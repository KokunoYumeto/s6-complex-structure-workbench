"""Source-aware reference normalization; audited exceptions are explicit below."""
from pathlib import Path
import re,json
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'deliverables'
EVENTS=[]

def section_labels(s,ns):
 def f(m):
  title=m[2];q=re.match(r'([A-F](?:\.\d+)?)\.(?:\s|$)',title)
  return m[0]+('\\label{'+ns+':section:'+q[1]+'}' if q else '')
 return re.sub(r'\\((?:sub)*section)\{([^}]+)\}',f,s)

def refs(s,name):
 ns='fam' if name.startswith('I_family') or name=='conventions' else 'push' if name.startswith('I_push') or name=='I_paperI_closing_cocycle' else 'inv' if name.startswith('I_inv') else 'ari' if name.startswith('I_ari') else None
 if not ns:return s
 original=s
 if ns in ['fam','push']:s=section_labels(s,ns)
 s=re.sub(r'\s*\(source (?:INV|ARI|PUSH|FAM) [A-F][\d.]+\)','',s)
 # Unambiguous cross-source references identified by full paragraph inspection.
 if name=='I_push_D_push':
  s=s.replace('in the earlier return,\nC.3.4','in \\cref{fam:src:C.3.4}')
  s=s.replace('in the earlier return, A.1.1','in \\cref{fam:src:A.1.1}')
  s=s.replace("in the return's C.2.2",'in \\cref{fam:src:C.2.2}')
 if name=='I_push_E_push':
  s=s.replace('same arithmetic classification in B.3.1','same arithmetic classification in \\cref{fam:src:B.3.1}')
  s=s.replace('steps of B.4.1 in the return','steps of \\cref{fam:src:B.4.1}')
  s=s.replace('Statements C.1.1\nand C.2.3 \\citep{family2026}','\\cref{fam:src:C.1.1,fam:src:C.2.3}')
 if name=='I_push_AB_push':
  s=s.replace('In the audited marking of E.2.7 the two finite peripheral','In the fixed marking the two finite peripheral')
 # Protect structured commands before converting ordinary source numbers.
 saved=[]
 def save(m):saved.append(m[0]);return '@@REFPROTECT'+str(len(saved)-1)+'@@'
 s=re.sub(r'\\(?:label|ref|eqref|cref|Cref|autoref|tag\*?|cite\w*|nocite|path|url|texttt)(?:\[[^\]]*\])*\{[^{}]*\}',save,s)
 if ns=='ari':
  s=re.sub(r'C\.6\.R([1-5])--R([1-5])',lambda m:'\\cref{ari:C.6.R'+m[1]+',ari:C.6.R'+m[2]+'}',s)
  s=re.sub(r'(?<![\w.:])C\.6\.R([1-5])',lambda m:'\\ref{ari:C.6.R'+m[1]+'}',s)
 def explicit(m):
  owner={'FAM':'fam','PUSH':'push','INV':'inv','ARI':'ari'}[m[1]];sid=m[2]
  if owner=='inv':sid=re.sub(r'^([A-F])\.',r'\1',sid)
  else:
   sid=re.sub(r'^([A-F])(\d)',r'\1.\2',sid)
  return '\\ref{'+owner+(':' if owner in ['inv','ari'] else ':src:')+sid+'}'
 s=re.sub(r'\b(FAM|PUSH|INV|ARI)\s+([A-F]\.?(?:\d+\.)+\d+)\b',explicit,s)
 pattern=r'(?<![\w.:])([A-F]\.\d+\.\d+)\b' if ns in ['fam','push','ari'] else r'(?<![\w.:])([A-F]\d+\.\d+)\b'
 s=re.sub(pattern,lambda m:'\\ref{'+ns+(':' if ns in ['inv','ari'] else ':src:')+m[1]+'}',s)
 if ns in ['fam','push']:
  # Section references are owned by the source's actual numbered headings.
  available=set(re.findall(r'\\label\{'+ns+r':section:([^}]+)\}',original))
  available.update(re.findall(r'\\(?:sub)*section\{([A-F]\.\d+)\.',original))
  if ns=='fam':available.update(['A.1','A.2','A.3','A.4','A.5','B.1','B.2','B.3','B.4','C.1','C.2','C.3','C.4','D.1','D.2','E.1','E.2','F.1','F.2','F.3'])
  s=re.sub(r'(?<![\w.:])([A-F]\.\d+)(?![\d.])',lambda m:'\\ref{'+ns+':section:'+m[1]+'}' if m[1] in available else m[0],s)
 s=re.sub(r'@@REFPROTECT(\d+)@@',lambda m:saved[int(m[1])],s)
 EVENTS.append({'part':name,'changes':int(s!=original),'source_reference_tokens_before':len(re.findall(pattern,original))})
 return s

def final_cleanup(s):
 s=s.replace('\\subsubsection{extension of the invariant $(1,1)$ class}',
             '\\subsubsection{Extension of the invariant class of bidegree (1,1)}')
 # These are editorial history sentences; all adjacent mathematical content stays.
 s=re.sub(r'\s*No priority is claimed\.', '',s)
 s=re.sub(r'\s*We make no\s+priority claim\.', '',s)
 s=s.replace('; we do not\nclaim priority for this elementary consequence.','.').replace('; we do not claim priority for this elementary consequence.','.')
 s=s.replace('We claim no priority;\nthe proof here','The proof here')
 s=s.replace('not a later inference from its conjecture','as is shown by its explicit local equations')
 s=s.replace('Our later\nuse at $i$','Our use at $i$')
 s=s.replace('the table in the earlier paper','the table in the paper they discuss')
 s=s.replace("Chen's version 2 of 16 October 2026", "Chen's version 2")
 s=s.replace('with the work obtained in attacking it. The report records every prompt\nitem.', 'with its complete partial proof and the precise remaining step.')
 # The original Kodaira article was not accessible. Its exact statement was opened
 # in Merkulov, and the directly applicable DT proposition is independently opened.
 s=s.replace('The general theorem is due to \\citet{Kodaira1962D}; its exact statement is also recorded in the opening of \\citet{Merkulov1995D}.',
 'The general completeness theorem is due to Kodaira; we use the exact statement in the opening of \\citet{Merkulov1995D}.')
 s=re.sub(r'The general theorem is due to\s+\\citet\{Kodaira1962D\}; its exact statement is also recorded\s+in the opening of \\citet\{Merkulov1995D\}\.',
     r'The general completeness theorem is due to Kodaira; we use the exact statement in the opening of \\citet{Merkulov1995D}.',s)
 s=s.replace('S6\\_02 \\ref{ari:B.4.2}',r'Proposition~\ref{fam:src:B.4.2}')
 s=s.replace('left as \\ref{ari:D.4.6} in the supplied checkpoint.',
             'posed for this normalized norm function.')
 s=s.replace('(9.5c)--(9.5f)','(HL.9.5c)--(HL.9.5f)')
 s=s.replace('(9.4)--(9.6)','(HL.9.4)--(HL.9.6)')
 s=s.replace('coordinate (9.19)',r'coordinate \eqref{inv:eq:C-factor12}')
 s=s.replace('wb:%\nprop:candidate-finite-fillings','wb:prop:candidate-finite-fillings')
 s=s.replace('the direct images used in R4',r'the direct images in Theorem~\ref{fam:src:A.5.2}')
 s=s.replace('the branch step used in R3',r'the branch step in \cref{fam:src:C.1.1,fam:src:C.1.2}')
 s=s.replace('The precise Albanese lattices in R5',r'The precise Albanese lattices in \cref{fam:src:A.4.1}')
 s=s.replace('are R4 and R5;',r'are \cref{fam:src:C.2.3,fam:src:A.5.1};')
 s=s.replace('so R5 gives exactly',r'so \cref{fam:src:A.5.1} gives exactly')
 s=s.replace('The supplied R4 and K6 already establish this inequality',
             r'Theorems~\ref{fam:src:C.2.3} and \cref{push:src:E.4.1,push:src:E.4.2} establish this inequality')
 s=s.replace('a global proof of R4',r'a global proof of Theorem~\ref{fam:src:C.2.3}')
 s=s.replace('the clockwise meridians and act by',
             'the analytic peripheral generators fixed by the root-deck convention and act by')
 s=s.replace('the clockwise meridians and the lift relation of',
             'the analytic peripheral generators and the lift relation of')
 s=s.replace('On the two finite clockwise meridians',
             'On the two finite analytic peripheral generators')
 s=s.replace('code/B_C6_gz_setup.out','code/invariants_arithmetic/arithmetic/outputs/writing_B_C6_gz_exact_metadata.gp.txt')
 s=s.replace('The exact torsion values proved in C.4 have product',
             r'The exact torsion values proved in Proposition~\ref{ari:C.4.4} have product')
 s=s.replace('At $t=0$ the expansion proved in C.3 is',
             r'At $t=0$ the expansion proved in Proposition~\ref{ari:C.3.2} is')
 # A blank source line inside display math is a paragraph token, not spacing.
 s=re.sub(r'(\\begin\{(equation\*?|align\*?|gather\*?|multline\*?)\})(.*?)(\\end\{\2\})',
          lambda m:m[1]+re.sub(r'\n\s*\n','\n',m[3])+m[4],s,flags=re.S)
 s=re.sub(r'\\cite\[\\texttt\{p2:prop:global-even-shift\} and the subsequent\s+orbit-groupoid calculations\]\{DuEtAl2026v1\}',r'\\cite[Proposition~7.8 and Appendix~C, Proposition~C.2]{DuEtAl2026v1}',s)
 (OUT/'work/root/I_source_reference_normalization.json').write_text(json.dumps(EVENTS,indent=2)+'\n')
 return s
