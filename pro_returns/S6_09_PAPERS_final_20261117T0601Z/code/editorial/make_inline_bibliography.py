"""Run BibTeX and inline its bibliography, with explicit identifiers and status."""
from pathlib import Path
import subprocess,json,re,os,sys
OUT=Path(__file__).resolve().parents[2];ROOT=OUT.parent
sys.path.insert(0,str(ROOT/'deps/python'));import bibtexparser
paper=sys.argv[1] if len(sys.argv)>1 else 'I';stem='S6_09_PAPERS_'+paper
tex=(OUT/(stem+'.tex')).read_text()
keys=sorted(set(k.strip() for m in re.finditer(r'\\(?:cite\w*|nocite)(?:\[[^\]]*\])*\{([^}]+)\}',tex) for k in m[1].split(',')))
job=stem+'_refs'
(OUT/(job+'.aux')).write_text('\\relax\n\\citation{'+','.join(keys)+'}\n\\bibstyle{apalike}\n\\bibdata{S6_09_PAPERS_references}\n')
env={**os.environ,**json.loads((OUT/'code/editorial/tex_runtime_environment.json').read_text())}
env['BSTINPUTS']='/usr/share/texlive/texmf-dist/bibtex/bst/base//:/usr/share/texlive/texmf-dist/bibtex/bst/natbib//:'
env['BIBINPUTS']=str(OUT)+':'
p=subprocess.run(['bibtex',job],cwd=OUT,env=env,capture_output=True,text=True)
(OUT/'editorial'/f'{stem}_bibtex.stdout.txt').write_text(p.stdout+p.stderr)
print(p.stdout[-2500:]);assert p.returncode==0,('BibTeX failed',p.returncode)
entries={e.key:{p.key:p.value for p in e.fields} for e in bibtexparser.parse_file(str(OUT/'S6_09_PAPERS_references.bib')).entries}
provenance=json.loads((OUT/'records/bibliography_provenance.json').read_text())
ver=provenance['verification_records']
s=(OUT/(job+'.bbl')).read_text()
parts=re.split(r'(?=\\bibitem\[)',s);output=[parts[0]];missing=[]
for part in parts[1:]:
 m=re.match(r'\\bibitem\[.*?\]\{([^}]+)\}',part,re.S);assert m,part[:150]
 key=m[1];d=entries[key]
 ending=''
 if '\\end{thebibliography}' in part:
  part,ending=part.split('\\end{thebibliography}',1);ending='\\end{thebibliography}'+ending
 # Replace the long uniform note by the exact present role/status at the end.
 part=re.sub(r'\s*Verified: original source opened.*?precise scope\.\s*','\n',part,flags=re.S)
 part=re.sub(r'\s*Unverified in this writing.*?source-note alone\.\s*','\n',part,flags=re.S)
 identifier=''
 if d.get('doi'):identifier=r'\url{https://doi.org/'+d['doi']+'}'
 elif d.get('url'):identifier=r'\url{'+d['url']+'}'
 elif d.get('eprint'):identifier='arXiv:'+d['eprint']
 else:
  record=ver.get(key,{})
  u=record.get('url',record.get('source_url',''))
  if u:identifier=r'\url{'+u+'}'
  elif d.get('isbn'):identifier='ISBN '+d['isbn']
  else:missing.append(key)
 if key=='CoxLittleSchenck2011':
  identifier += ". Edition consulted: the authors' 2010 prepublication text; the cited page numbers refer to that text"
 if d.get('verification')=='verified':
  role='Verified source for the precisely cited statement or methodological fact: opened and matched by GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), 17 November 2026.'
 else:role='Unverified original: retained only for the explicitly qualified comparison or historical attribution; no proof depends on this entry.'
 output.append(part.rstrip()+'\n\\newblock '+identifier+'. '+role+'\n\n'+ending)
joined=''.join(output)
joined=re.sub(r'\\newblock\s*\\newblock',r'\\newblock',joined)
target=OUT/'editorial'/(paper+'_bibliography.tex');target.write_text(joined)
(OUT/'records'/(paper+'_bibliography_identifiers.json')).write_text(json.dumps({'entries':len(parts)-1,'missing_identifiers':missing},indent=2)+'\n')
print('Inline entries:',len(parts)-1,'missing identifiers:',missing)
