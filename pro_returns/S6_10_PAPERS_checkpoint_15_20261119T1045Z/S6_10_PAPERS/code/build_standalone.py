"""Build self-contained TeX with exact receiving/compendium references and bibliography.

This is editorial assembly. It confers no mathematical proof check.
"""
from pathlib import Path
import argparse,concurrent.futures,csv,hashlib,json,os,re,subprocess
from fix_verified_legacy_locators import fix_legacy_locators
P=Path(__file__).resolve().parents[1];ROOT=P.parents[1]
PREVIEWS={'I':'build/I_preview','II':'build/sign_II','III':'build/III_preview','IV':'analysis/IV/preview','V':'analysis/V/preview','VI':'build/sign_VI'}
TITLES={'II':'Torus-fibred threefolds: cotangent torsion, tangent cohomology and fibre signs',
 'IV':'Smooth monodromy, circle quotients and integral return classes',
 'V':'Complex fourfolds from a marked rank-six torus family',
 'VI':'Analytic degenerations and the sign theorem for singular torus fibres'}
env=os.environ.copy();env.update(json.loads((P/'build/tex_runtime/environment.json').read_text()))

def argument(s,at):
 assert s[at]=='{';depth=1;i=at+1
 while depth:
  if s[i]=='{' and s[i-1]!='\\':depth+=1
  if s[i]=='}' and s[i-1]!='\\':depth-=1
  i+=1
 return s[at+1:i-1],i

def aux_records(path):
 text=path.read_text(errors='replace');out={}
 for m in re.finditer(r'\\newlabel\{([^}]+)\}\{',text):
  val,_=argument(text,m.end()-1)
  if val.startswith('{'):
   first,_=argument(val,0)
   if m[1].endswith('@cref'):
    q=re.match(r'\[([^]]+)\]',first)
    if q:out.setdefault(m[1][:-5],{})['type']=q[1]
   else:out.setdefault(m[1],{})['number']=first
 return out

def math_unicode(s):
 table={'≥':r'\ensuremath{\geq}','≤':r'\ensuremath{\leq}','≠':r'\ensuremath{\neq}',
 '⊂':r'\ensuremath{\subset}','⊆':r'\ensuremath{\subseteq}','⊗':r'\ensuremath{\otimes}',
 '⊕':r'\ensuremath{\oplus}','→':r'\ensuremath{\to}','↔':r'\ensuremath{\leftrightarrow}',
 '↦':r'\ensuremath{\mapsto}','⇒':r'\ensuremath{\Rightarrow}','⇔':r'\ensuremath{\Leftrightarrow}',
 '∈':r'\ensuremath{\in}','∉':r'\ensuremath{\notin}','∞':r'\ensuremath{\infty}',
 '∂':r'\ensuremath{\partial}','∧':r'\ensuremath{\wedge}','∩':r'\ensuremath{\cap}',
 '∪':r'\ensuremath{\cup}','×':r'\ensuremath{\times}','−':r'\ensuremath{-}',
 '≅':r'\ensuremath{\cong}','ℤ':r'\ensuremath{\mathbb Z}','ℚ':r'\ensuremath{\mathbb Q}',
 'ℝ':r'\ensuremath{\mathbb R}','ℂ':r'\ensuremath{\mathbb C}','′':r'\ensuremath{\prime}',
 'χ':r'\ensuremath{\chi}','√':r'\ensuremath{\surd}',
 'Π':r'\ensuremath{\Pi}','Σ':r'\ensuremath{\Sigma}','Θ':r'\ensuremath{\Theta}',
 'Δ':r'\ensuremath{\Delta}','Ω':r'\ensuremath{\Omega}'}
 for ch,name in zip('αβγδεζηθικλμνξοπρστυφω', ['alpha','beta','gamma','delta','epsilon','zeta','eta','theta','iota','kappa','lambda','mu','nu','xi','mathrm{o}','pi','rho','sigma','tau','upsilon','phi','omega']):
  table[ch]='\\ensuremath{\\'+name+'}'
 for ch,v in zip('⁰¹²³⁴⁵⁶⁷⁸⁹','0123456789'):table[ch]=r'\textsuperscript{'+v+'}'
 for ch,v in zip('₀₁₂₃₄₅₆₇₈₉','0123456789'):table[ch]=r'\textsubscript{'+v+'}'
 return ''.join(table.get(ch,ch) for ch in s)

RAW={paper:(P/path/'preview.tex').read_text() for paper,path in PREVIEWS.items()}
LABELS={p:set(re.findall(r'\\label\{([^}]+)\}',s)) for p,s in RAW.items()}
AUX={p:aux_records(P/path/'preview.aux') for p,path in PREVIEWS.items()}
OWNERS={}
for p,labels in LABELS.items():
 for label in labels:OWNERS.setdefault(label,[]).append(p)
COMP={}
for p in ['I','II','III']:
 for label in set(re.findall(r'\\label\{([^}]+)\}',(ROOT/f'sources/s6_09/S6_09_PAPERS_{p}.tex').read_text())):
  COMP.setdefault(label,[]).append(p)

MACROS=r'''
\newcommand{\ExternalPaperRef}[3]{\ifmmode\text{\upshape #1#2 (Paper~#3)}\else #1#2 (Paper~#3)\fi}
\newcommand{\CompendiumRef}[2]{\ifmmode\text{\upshape S6\_09, Paper~#1, label~\nolinkurl{#2}}\else S6\_09, Paper~#1, label~\nolinkurl{#2}\fi}
'''

def rewrite_refs(paper,body):
 changes=[]
 # The source CSV mistook the map F_0 for a statement P3F.0. The actual
 # cited construction is K49, RCZ.5--7, as checked in the IV source audit.
 body=body.replace(r'\cref{night:P3F.0}',r'the complete annular map $F_0$ in \cref{night:P3K.49}, RCZ.5--7')
 def one(kind,label):
  if label in LABELS[paper]:return '\\'+kind+'{'+label+'}'
  if label in OWNERS:
   owners=OWNERS[label]
   if len(owners)!=1:raise ValueError('Ambiguous receiving label '+label+':'+str(owners))
   owner=owners[0];data=AUX[owner].get(label,{})
   if 'number' not in data:raise ValueError('Missing compiled label number '+label)
   number=data['number'];prefix=''
   if kind.lower()=='cref':prefix=data.get('type','statement').replace('openq','open question').replace('auditrecord','verification record')+'~'
   if kind=='Cref':prefix=prefix[:1].upper()+prefix[1:]
   if kind=='eqref':number='('+number+')'
   changes.append({'label':label,'destination':'Paper '+owner,'number':number,'source_command':kind})
   return r'\ExternalPaperRef{'+prefix+'}{'+number+'}{'+owner+'}'
  if label in COMP:
   owners=COMP[label]
   if len(owners)!=1:raise ValueError('Ambiguous compendium label '+label+':'+str(owners))
   changes.append({'label':label,'destination':'S6_09 Paper '+owners[0],'source_command':kind})
   return r'\CompendiumRef{'+owners[0]+'}{'+label+'}'
  raise ValueError('Unresolved label '+label+' in '+paper)
 def transform(s):
  s=re.sub(r'\\(crefrange|Crefrange)\{([^}]+)\}\{([^}]+)\}',lambda m: m[0] if m[2] in LABELS[paper] and m[3] in LABELS[paper] else one('Cref' if m[1][0]=='C' else 'cref',m[2])+'--'+one('cref',m[3]),s)
  s=re.sub(r'\\(ref|eqref|cref|Cref|autoref)\*?\{([^}]+)\}',lambda m:', '.join(one(m[1],label.strip()) for label in m[2].split(',')),s)
  s=re.sub(r'(?:Appendix|appendix|Theorem|theorem|Lemma|lemma|Proposition|proposition|Corollary|corollary|Section|section|equation|Equation)~(?=\\CompendiumRef)', '',s)
  return s
 # Literal source listings remain byte-for-byte unchanged.
 pattern=r'(\\begin\{(?:verbatim|Verbatim|lstlisting)\}[\s\S]*?\\end\{(?:verbatim|Verbatim|lstlisting)\})'
 chunks=re.split(pattern,body)
 return ''.join(s if n%2 else transform(s) for n,s in enumerate(chunks)),changes

def bibliography(folder,text):
 keys=set()
 for m in re.finditer(r'\\(?:no)?cite\w*\*?\s*(?:\[[^\]]*\]\s*)*\{([^}]+)\}',text):keys.update(k.strip() for k in m[1].split(','))
 bib=(P/'S6_10_PAPERS_references.bib').read_text();available=set(re.findall(r'^@\w+\{([^,]+),',bib,re.M))
 missing=sorted(keys-available)
 if missing:raise ValueError('Missing bibliography entries: '+','.join(missing))
 (folder/'references.bib').write_text(math_unicode(bib))
 (folder/'bibliography.aux').write_text('\\relax\n\\citation{'+','.join(sorted(keys))+'}\n\\bibstyle{plainnat}\n\\bibdata{references}\n')
 run=subprocess.run(['bibtex','bibliography'],cwd=folder,env=env,capture_output=True,text=True)
 (folder/'bibtex.stdout.txt').write_text(run.stdout+run.stderr)
 if run.returncode:raise RuntimeError('BibTeX failed; see '+str(folder/'bibtex.stdout.txt'))
 # Long locator lists retain their punctuation and gain legal line breaks.
 return (folder/'bibliography.bbl').read_text().replace(';',r';\allowbreak{}'),sorted(keys)

def run(paper):
 folder=P/'build/standalone'/paper;folder.mkdir(parents=True,exist_ok=True)
 src=RAW[paper];head,body=src.split(r'\begin{document}',1);body=body.rsplit(r'\end{document}',1)[0]
 editorial=[]
 old_rung=r'\newcommand{\RungOne}{\par\noindent\textbf{Proof at the first rung.}\par\smallskip}'
 new_rung=r'\newcommand{\RungOne}{\par\Needspace{6\baselineskip}\noindent\textbf{Proof at the first rung.}\par\nobreak\smallskip}'
 if old_rung in head:
  head=head.replace(old_rung,new_rung)
  editorial.append('Keep every rung-one lead-in with the opening lines of its numbered argument; observed orphan in the II opening preview.')
 if paper in TITLES:
  if r'\title{' in body:
   body=re.sub(r'\\title\{[^\n]*\}',lambda _:r'\title{'+TITLES[paper]+'}',body,count=1)
  else:
   body='\n\\title{'+TITLES[paper]+'}\n\\author{AI-produced mathematical text}\n\\date{19 November 2026}\n\\maketitle\n'+body
   editorial.append('Add the printed title, AI authorship and date block also preserved in the current frontmatter fragment.')
 if paper=='III' and r'\RungOne' in body:
  pos=body.index(r'\RungOne')
  if r'\Needspace{5\baselineskip}' not in body[max(0,pos-50):pos]:
   body=body[:pos]+r'\Needspace{5\baselineskip}'+'\n'+body[pos:]
   editorial.append('Keep the first rung-one lead-in with the beginning of its numbered proof.')
 body=body.replace(r'\author{}',r'\author{AI-produced mathematical text}')
 declarations=(P/'papers/common_declarations.tex').read_text()
 marker=r'\end{abstract}' if r'\end{abstract}' in body else r'\maketitle'
 if marker not in body:raise ValueError('No declaration insertion point '+paper)
 body=body.replace(marker,marker+'\n'+declarations,1)
 body,legacy_changes=fix_legacy_locators(body,'canonical '+paper)
 body,changes=rewrite_refs(paper,body)
 changes=legacy_changes+changes
 bbl,keys=bibliography(folder,body)
 assembled=head+MACROS+'\n\\begin{document}\n'+body+'\n\\clearpage\n'+bbl+'\n\\end{document}\n'
 dest=folder/f'S6_10_PAPERS_{paper}.tex';dest.write_text(assembled)
 for passno in (1,2,3):
  with (folder/f'lualatex_pass{passno}.txt').open('w') as f:
   r=subprocess.run(['lualatex','-interaction=nonstopmode','-halt-on-error',dest.name],cwd=folder,env=env,stdout=f,stderr=subprocess.STDOUT)
  if r.returncode:raise RuntimeError('LuaLaTeX failed; see '+str(folder/f'lualatex_pass{passno}.txt'))
  if passno>=2 and 'Label(s) may have changed' not in dest.with_suffix('.log').read_text(errors='replace'):
   break
 pdf=dest.with_suffix('.pdf');log=dest.with_suffix('.log').read_text(errors='replace')
 # The compiled canonical TeX contains its bibliography, with no sidecar input.
 (P/dest.name).write_bytes(dest.read_bytes());(P/pdf.name).write_bytes(pdf.read_bytes())
 record={'paper':paper,'source_sha256':hashlib.sha256(src.encode()).hexdigest(),'tex_sha256':hashlib.sha256(dest.read_bytes()).hexdigest(),'pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),'citations':keys,'cross_reference_changes':changes,'editorial_corrections':editorial,'missing_characters':len(re.findall('Missing character:',log)),'font_warnings':len(re.findall(r'(?:LaTeX Font Warning|fontspec Warning)',log)),'overfull_above2pt':[float(x) for x in re.findall(r'Overfull \\[hv]box \(([0-9.]+)pt',log) if float(x)>2],'undefined_reference_messages':len(re.findall(r'LaTeX Warning: Reference',log)),'undefined_citation_messages':len(re.findall(r'Package natbib Warning: Citation',log)),'scope':'Editorial assembly and typesetting only; no proof credit.'}
 (folder/'assembly_record.json').write_text(json.dumps(record,indent=2));print(paper,'compiled',len(changes),'external references',len(keys),'citations','missing',record['missing_characters'],'overflow',len(record['overfull_above2pt']),flush=True)
 return record

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('papers',nargs='*',default=list(PREVIEWS));ap.add_argument('--jobs',type=int,default=2);args=ap.parse_args()
 with concurrent.futures.ThreadPoolExecutor(max_workers=args.jobs) as ex:
  failures=[]
  futures={ex.submit(run,p):p for p in args.papers}
  for f in concurrent.futures.as_completed(futures):
   try:f.result()
   except Exception as e:
    failures.append(futures[f]);print(futures[f],'FAILED',repr(e),flush=True)
  if failures:raise SystemExit('Failed standalone builds: '+','.join(failures))
