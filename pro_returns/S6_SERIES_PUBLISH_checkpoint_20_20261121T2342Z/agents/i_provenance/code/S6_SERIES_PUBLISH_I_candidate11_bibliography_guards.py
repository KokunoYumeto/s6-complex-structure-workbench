from pathlib import Path
import re,json,hashlib,datetime
R=Path('/workspace/scratch/653608133b22');O=R/'work/agents/i_provenance';P=R/'work/S6_SERIES_PUBLISH_I.tex';s=P.read_text();changes=[]
def span(s,key):
 m=re.search(r'\\bibitem\[[\s\S]*?\]\{'+re.escape(key)+r'\}',s)
 # Keep the nearest bibitem; the broad match above may start at an earlier entry.
 k=s.index('{'+key+'}',s.index('\\begin{thebibliography}'));a=s.rfind('\\bibitem',0,k);b=s.find('\\bibitem',k)
 return s[a:b if b>=0 else s.index('\\end{thebibliography}',k)]
rules={
 'Buchdahl1999':[('On compact kähler surfaces.','On compact Kähler surfaces.')],
 'FG10':[('Riemann--roch','Riemann--Roch'),('gt-v14-n1-p02-s.pdf','gt-v14-n1-p02-p.pdf')],
 'Levy08':[('Riemann--roch','Riemann--Roch')],
 'Xiao91':[('fixed jacobian.','fixed Jacobian.')],
 'AC2026':[('The (3,4,infinity) modular family','The $(3,4,\\infty)$ modular family')],
 'reyssat1982weierstrass':[('fonctions de weierstrass.','fonctions de Weierstrass.')],
 'Grauert60':[('Ein theorem der analytischen garbentheorie und die modulräume\n  komplexer strukturen.','Ein Theorem der analytischen Garbentheorie und die Modulräume\n  komplexer Strukturen.')],
 'Grauert1963ErratumD':[('Berichtigung: Ein theorem der analytischen garbentheorie und die\n  modulräume komplexer strukturen.','Berichtigung: Ein Theorem der analytischen Garbentheorie und die\n  Modulräume komplexer Strukturen.')],
}
for key,rr in rules.items():
 old=span(s,key);new=old
 for a,b in rr:
  assert a in new,(key,a);new=new.replace(a,b)
 changes.append(dict(id='IP-C11-CAP-'+key,old=old,new=new,reason='Preserve primary title capitalization and, for FG10, the primary PDF URL actually retrieved and read by root.'))
old=span(s,'STW2017');new=old.replace('\\newblock Gauduchon metrics with prescribed volume form, 2017.','\\newblock Gauduchon metrics with prescribed volume form.\n\n\\newblock \\emph{Acta Mathematica}, 219(1):181--211, 2017.\n\n\\newblock \\doi{10.4310/ACTA.2017.v219.n1.a6}.\n\n\\newblock Earlier manuscript: arXiv:1503.04491v2, with separate pagination.')
assert new!=old
changes.append(dict(id='IP-C11-CAP-STW2017',old=old,new=new,reason='Official author-submitted arXiv record identifies the published article and DOI. Retain separate v2 pagination for the actually read operative theorem.'))
meta=dict(source=str(P),source_sha256=hashlib.sha256(s.encode()).hexdigest(),created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),source_writes=False,changes=changes,mathematical_check_events=0)
(O/'S6_SERIES_PUBLISH_I_candidate11_bibliography_guards.json').write_text(json.dumps(meta,indent=2,ensure_ascii=False)+'\n')

B=R/'work/S6_SERIES_PUBLISH_references.bib';b=B.read_text();bc=[]
def bspan(key):
 m=re.search(r'@\w+\{'+key+r',',b);assert m;z=re.search(r'\n@',b[m.end():]);return b[m.start():m.end()+z.start() if z else len(b)]
for key in rules:
 old=bspan(key);new=old
 # Protect proper-name capitals against bibliography styles.
 m=re.search(r'  title = \{([^\n]*)\},',new)
 if m:
  title=m.group(1);newtitle=title
  for a,z in [('kähler','{Kähler}'),('Kähler','{Kähler}'),('Riemann--roch','{Riemann--Roch}'),('Riemann--Roch','{Riemann--Roch}'),('weierstrass','{Weierstrass}'),('Weierstrass','{Weierstrass}'),('jacobian','{Jacobian}'),('Jacobian','{Jacobian}')]:
   if a in newtitle and '{'+a+'}' not in newtitle:newtitle=newtitle.replace(a,z)
  # Collapse only immediately duplicated protection introduced by the sequential name variants.
  newtitle=newtitle.replace('{{Kähler}}','{Kähler}').replace('{{Riemann--Roch}}','{Riemann--Roch}').replace('{{Weierstrass}}','{Weierstrass}').replace('{{Jacobian}}','{Jacobian}')
  if key=='AC2026':newtitle=newtitle.replace('(3,4,infinity)',r'$(3,4,\infty)$')
  if key in ['Grauert60','Grauert1963ErratumD']:
   for a,z in [('theorem','Theorem'),('garbentheorie','Garbentheorie'),('modulräume','Modulräume'),('strukturen','Strukturen')]:newtitle=newtitle.replace(a,z)
   if not(newtitle.startswith('{') and newtitle.endswith('}')):newtitle='{'+newtitle+'}'
  new=new.replace(m.group(0),'  title = {'+newtitle+'},',1)
 if key=='FG10':new=new.replace('gt-v14-n1-p02-s.pdf','gt-v14-n1-p02-p.pdf')
 if new!=old:bc.append(dict(id='IP-C11-SCAP-'+key,old=old,new=new,reason='Preserve the same primary title capitalization in BibTeX; historical verification fields unchanged.'))
old=bspan('STW2017');new=old.replace('@misc{STW2017,','@article{STW2017,').replace('  year = {2017},','  year = {2017},\n  journal = {Acta Mathematica},\n  volume = {219},\n  number = {1},\n  pages = {181--211},\n  doi = {10.4310/ACTA.2017.v219.n1.a6},',1)
close=new.rfind('}');head=new[:close].rstrip();head=head if head.endswith(',') else head+',';new=head+'\n  current_run_metadata = {Official arXiv1503.04491 record opened on 21 November 2026 identifies Acta Mathematica219(1)(2017),181--211 and DOI10.4310/ACTA.2017.v219.n1.a6. Operative Theorem1.3 locator remains arXiv v2 p.3; no publication-page equality inferred}\n'+new[close:]
bc.append(dict(id='IP-C11-SCAP-STW2017',old=old,new=new,reason='Published metadata verified against the official arXiv record, preserving the separately paginated v2 source.'))
(O/'S6_SERIES_PUBLISH_I_candidate11_shared_bibliography_tail_guards.json').write_text(json.dumps(dict(source=str(B),source_sha256=hashlib.sha256(b.encode()).hexdigest(),changes=bc,source_writes=False),indent=2,ensure_ascii=False)+'\n')
receipt={'created_utc':meta['created_utc'],'metadata_sources':[{'key':'STW2017','url':'https://arxiv.org/abs/1503.04491','web_ref':'turn186764315view0','verified':'Published journal, volume, issue, pages, year and DOI; v2 date8December2017; metadata-only opening, no extra page or mathematics credit.'},{'key':'nguyen2023','url':'https://sites.google.com/view/khoanguyen-calgary','web_ref':'turn186764315view1','verified':'Author publication list confirms Math.Annalen387(2023),1--15; existing metadata retained.'},{'key':'FG10','receipt':'work/agents/root_primary/S6_SERIES_PUBLISH_I_root_primary_locator_receipt.json','verified':'Root supplied actual published PDF/page opening at -p.pdf; this agent does not claim root page images as its own.'}],'mathematical_check_events':0}
(O/'literature/S6_SERIES_PUBLISH_I_candidate11_bibliography_metadata_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(len(changes),'inline bibliography guards;',len(bc),'shared guards')
