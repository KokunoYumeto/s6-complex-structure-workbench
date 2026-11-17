"""Convert every selected complete course proof to standalone manuscript TeX.

This is an editorial conversion. The independently recorded mathematical
checks are separate; this script never upgrades an audit verdict.
"""
from pathlib import Path
import re,json,hashlib,subprocess,collections,csv

ROOT=Path(__file__).resolve().parents[3];D=ROOT/'deliverables';W=D/'work/maps_audit';E=D/'editorial'
OUT=E/'III_course';OUT.mkdir(exist_ok=True)
handoff=json.loads((W/'course_provider_assembly_handoff.json').read_text())
geo=json.loads((W/'course_geometric_provider_inventory.json').read_text())
dual=json.loads((W/'course_duality_euler_provider_inventory.json').read_text())
characteristic=json.loads((W/'course_characteristic_provider_inventory.json').read_text())
inventory=list(csv.DictReader((D/'S6_09_PAPERS_inventory.csv').open()))
metadata_math_tails={r['source']:r for r in json.loads((W/'III_course_metadata_math_restore.json').read_text())}
configs=[]
for basename,start,end,title in [
 ('thom-euler-for-lesson11.md',175,322,'Thom, Euler and orientation comparisons'),
 ('projective-splitting-for-lesson11.md',5,111,'Integral projective splitting'),
 ('integral-chern-classes-for-lesson11.md',5,100,'Integral Chern classes')]:
 configs.append(dict(source='sources/codex_workspace/courses/CG-S6/src/'+basename,start=start,end=end,title=title,category='characteristic'))
configs.append(dict(source=dual[0]['source_file'],retained=dual[0]['retained_complete_proof'],start=1,end=250,title='Singular duality, the diagonal and the Euler class',category='duality'))
for c in handoff['chapters']:
 configs.append(dict(source=c['source'],retained=c['retained_complete_proof'],start=1,end=c['whole_proof_range'][1],category='geometric'))
configs.extend([
 dict(source='sources/codex_workspace/courses/CG-S6/src/sphere-twists-and-the-original-smooth-six-sphere-comparison.md',start=1,end=818,category='working'),
 dict(source='sources/codex_workspace/courses/CG-S6/src/integral-homology-and-sphere-recognition.md',start=954,end=1185,title='The original sphere comparison and its complete exercises',category='working'),
 dict(source='sources/codex_workspace/courses/CG-S6/src/almost-complex-structures-and-integrability.md',start=1,end=1241,category='working')])

def slug(s):return re.sub(r'[^a-zA-Z0-9:.-]+','-',s).strip('-')
def cname(c):return Path(c['source']).name
def ns(c):return 'courseIII:'+slug(Path(c['source']).stem)
def read(c):
 p=ROOT/c.get('retained',c['source']);ls=p.read_text().splitlines()
 # Retained provider files begin at source line one in all supplied handoffs.
 return '\n'.join(ls[c['start']-1:c['end']])+'\n'

links={};placements={};removed=[];unmapped=[];manifest=[];alignment_repairs=[]
for c in configs:
 c['raw']=read(c);c['ns']=ns(c);n=cname(c)
 links[n]=c['ns']+':section'
 if n.endswith('.source.txt'):links[n.replace('.source.txt','.md')]=c['ns']+':section'
 for a in re.findall(r'\{#([^}]+)\}|<a\s+(?:id|name)="([^"]+)"\s*>',c['raw']):
  anchor=next(x for x in a if x);links[n+'#'+anchor]=c['ns']+':'+slug(anchor)
 for m in re.finditer(r'^#{2,4}\s+([0-9]+(?:\.[0-9]+)*)\.?(?:\s|$)',c['raw'],re.M):
  links[n+'#section-'+m[1]]=c['ns']+':section-'+m[1]

# Already printed complete classical proofs stay in Paper I.
I_AUX=(D/'S6_09_PAPERS_I.aux').read_text()
I_LABELS=set(re.findall(r'\\newlabel\{([^}@]+)\}',I_AUX))
for name,prefix in [('thom-euler-for-lesson11.md','mapsI:chain'),('cw-models-and-the-first-hurewicz-map.md','mapsI:cw'),('path-fibres-and-integral-homotopy-equivalences.md','mapsI:pf')]:
 if name not in links:links[name]=prefix+':section'
 for label in I_LABELS:
  if label.startswith(prefix+':'):links[name+'#'+label[len(prefix)+1:]]=label
links.update({
 'cw-models-and-the-first-hurewicz-map.md#hurewicz-theorem':'mapsI:cw:hurewicz-theorem-result',
 'integral-homology-and-sphere-recognition.md#sphere-homotopy':'mapsI:course:homotopy-section',
 'integral-homology-and-sphere-recognition.md#sphere-recognition':links['integral-homology-and-sphere-recognition.md'],
 'DG-CHAR-06.html':links['thom-euler-for-lesson11.md'],
 'DG-CHAR-02.html':links['projective-splitting-for-lesson11.md'],
 'DG-CHAR-09.html':links['integral-chern-classes-for-lesson11.md'],
 'tangent-index-with-torsion-line-bundles.md#tangent-characteristic-comparison':links['manifold-duality-the-diagonal-and-wu-classes.source.txt'],
})

for c in configs:
 raw=c['raw'];s=raw;n=cname(c);prefix=c['ns'];items=[]
 if c['category']=='geometric':items=[r for r in geo if r['source_file']==c['source'] and not r['duplicate_of_existing_inventory']]
 if c['category']=='duality':items=dual
 if c['category']=='characteristic':items=[r for r in characteristic if r['source_file']==c['source'] and not r['duplicate_of_existing_inventory']]
 for r in items:
  if not r.get('source_number'):r['source_number']=re.search(r'(\d+(?:\.\d+)*)$',r['source_id'])[1]
  r.setdefault('reserved_label',prefix+':'+slug(r['source_id']))
 # Preserve exact model/effort/date in a dedicated provenance record, rather
 # than source-era self-review prose interspersed with a current proof.
 ls=s.splitlines();kept=[]
 for i,line in enumerate(ls):
  if i<7 and any(t in line for t in ['GPT-6','Written by','Receiving proof for','Proof companion for']):
   restoration=metadata_math_tails.get(c['source'])
   tail=''
   if restoration and restoration['source_line']==i+c['start']:
    assert hashlib.sha256(line.encode()).hexdigest()==restoration['raw_line_sha256'], ('Producer/setup line changed; re-audit required',c['source'])
    tail=restoration['keep_in_mathematical_text']
    kept.append(tail)
   removed.append({'source':c['source'],'source_line':i+c['start'],'text':line,'mathematical_tail_retained':tail,'reason':'raw producer line retained in provenance; only actual producer metadata removed, every identified mathematical setup/dependency tail retained in place'})
  else:kept.append(line)
 s='\n'.join(kept)+'\n'
 if c['category']=='duality':
  s=s.replace('The [squares chapter](DG-CHAR-05.html) proves the cochain operations, Cartan and the Thom definition of Stiefel–Whitney classes. ', '')
 # Strip only terminal source/check inventories, preserving them separately.
 sourceheads=list(re.finditer(r'^##\s+(?:\d+\.\s+)?(?:Sources|Source and|Included prerequisites|Checks and|Verification and)[^\n]*',s,re.M))
 for m in reversed(sourceheads):
  nxt=re.search(r'^##\s',s[m.end():],re.M)
  end=m.end()+nxt.start() if nxt else len(s)
  removed.append({'source':c['source'],'text':s[m.start():end],'reason':'source and self-check inventory moved to provenance records; following mathematical sections and exercises retained'})
  s=s[:m.start()]+s[end:]
 title=c.get('title')
 m=re.search(r'^#\s+(.+?)(?:\s+\{#[^}]+\})?$',s,re.M)
 if m:
  title=title or m[1];s=s[:m.start()]+s[m.end():]
 title=title or Path(n).stem.replace('-',' ').capitalize()
 c['title']=title
 # Remove redundant SVG illustrations only; the adjacent equations and all
 # captions are retained. No proof is encoded exclusively in those pictures.
 def pic(m):
  removed.append({'source':c['source'],'text':m[0],'reason':'external illustration not embedded; description, anchor and adjacent mathematical proof retained; asset availability and proof sufficiency audited separately'})
  anchor='\\label{'+prefix+':'+slug(m[2])+'}\n' if m[2] else ''
  return anchor+'Illustration description: '+m[1]
 s=re.sub(r'^!\[([^\n]*)\]\([^\n]*\)(?:\s*\{#([^}]+)\})?[ \t]*$',pic,s,flags=re.M)
 def htmlpic(m):
  original=m[0]
  def attr(name):
   a=re.search(r'\b'+name+r'="([^"]*)"',original)
   return a[1] if a else ''
  alt=attr('alt');aid=attr('id')
  removed.append({'source':c['source'],'text':original,'retained_description':alt,'reason':'external HTML illustration not embedded; complete alt description, image anchor and adjacent figcaption retained; asset availability and proof sufficiency audited separately'})
  return ('\\label{'+prefix+':'+slug(aid)+'}\n' if aid else '')+'Illustration description: '+alt+'\n'
 s=re.sub(r'<img\b[^>]*>',htmlpic,s)
 # Pandoc may silently discard raw image elements. Remove only the figure
 # wrappers after explicitly retaining their descriptions and full captions.
 s=re.sub(r'</?(?:figure|figcaption)\b[^>]*>','\n',s)
 def anchor(m):return '\\label{'+prefix+':'+slug(m[1])+'}'
 s=re.sub(r'<a\s+(?:id|name)="([^"]+)"\s*>\s*</a>',anchor,s)
 def heading(m):
  level,body=m[1],m[2];a=re.search(r'\s*\{#([^}]+)\}\s*$',body)
  extra=''
  if a:extra='\\label{'+prefix+':'+slug(a[1])+'}';body=body[:a.start()]
  q=re.match(r'(?:(?:Exercise|Worked example)\s+)?(\d+(?:\.\d+)*)\.?(?:\s+|$)',body);number=q[1] if q else ''
  if number:
   numberkey=('exercise-' if re.match(r'(?:Exercise|Worked example)\s',body) else 'section-')+number
   extra+='\\label{'+prefix+':'+numberkey+'}'
  for r in items:
   matched=m[0].strip()==r['source_heading'].strip() if r.get('source_heading') else r.get('source_number')==number
   if matched:
    label=r['reserved_label'];extra+='\\label{'+label+'}';placements[r['source_id']]=label
  if c['category']=='working':
   for r in inventory:
    if r['source_run']=='course_CG-S6' and r['source_file']==c['source']:
     sid=r['source_id']
     if a and sid==a[1]:placements[sid]=prefix+':'+slug(a[1])
  cleanbody=re.sub(r'^\d+(?:\.\d+)*\.?\s+','',body)
  cmd='subsection' if len(level)==2 else 'subsubsection' if len(level)==3 else 'paragraph'
  return '\\'+cmd+'{'+cleanbody+'}\n'+extra
 s=re.sub(r'^(#{2,4})\s+(.+)$',heading,s,flags=re.M)
 # Characteristic/duality units carry original numbered theorem headings.
 for r in items:
  if r['source_id'] in placements:continue
  number=r.get('source_number') or re.search(r'(\d+\.\d+)$',r['source_id'])[1]
  kind=r.get('kind','Lemma').split()[-1].capitalize()
  label=r.get('reserved_label',prefix+':'+slug(r['source_id']))
  pat=r'(\*\*(?:Theorem|Lemma|Proposition|Corollary)\s+'+re.escape(number)+r'\b[^\n]*?\*\*)'
  if re.search(pat,s):s=re.sub(pat,lambda m:'\\label{'+label+'}\n'+m[0],s,count=1);placements[r['source_id']]=label
  else:unmapped.append({'source':c['source'],'provider':r['source_id'],'problem':'numbered unit heading not found'})
 # Every equation obtains a unique chapter-owned label and a global number.
 tags=set(re.findall(r'\\tag\{([^}]+)\}',s))
 s=re.sub(r'\\tag\{([^}]+)\}',lambda m:'\\label{'+prefix+':eq:'+slug(m[1])+'}',s)
 for tag in sorted(tags,key=len,reverse=True):s=s.replace('('+tag+')','\\eqref{'+prefix+':eq:'+slug(tag)+'}')
 def repair_split(m):
  block=m[0]
  if any(len(re.findall(r'(?<!\\)&',row))>1 for row in block.split(r'\\')):
   replacement=block.replace('\\begin{split}','\\begin{aligned}').replace('\\end{split}','\\end{aligned}')
   alignment_repairs.append({'source':c['source'],'original':block,'replacement':replacement,'reason':'The source split environment has more than one alignment tab in a row; aligned permits the retained equation and condition columns. Every mathematical token is unchanged.'})
   return replacement
  return block
 s=re.sub(r'\\begin\{split\}.*?\\end\{split\}',repair_split,s,flags=re.S)
 s=re.sub(r'\\\[(.*?)\\\]',lambda m:'\\begin{equation}\n'+m[1].strip()+'\n\\end{equation}' if '\\label{' in m[1] else m[0],s,flags=re.S)
 def link(m):
  text,url=m[1],m[2]
  if re.match(r'https?://',url):return m[0]
  key=(n+url) if url.startswith('#') else url
  key=key.removeprefix('./').removeprefix('../src/')
  if key.startswith('../checks/'):
   filename=Path(key).name
   candidates=sorted((D/'code').rglob(filename),key=lambda x:len(str(x)))
   if candidates:return text+' ('+'\\path{'+str(candidates[0].relative_to(D))+'})'
   return text+' ('+'\\path{'+filename+'}; illustrative source asset)'
  if key in links:return '\\cref{'+links[key]+'}'
  target='courseIII:unresolved:'+slug(key)
  unmapped.append({'source':c['source'],'link':url,'text':text,'label':target})
  return '\\cref{'+target+'}'
 mathparts=[]
 def protect_math(m):mathparts.append(m[0]);return 'ZZMATHPROTECTED'+str(len(mathparts)-1)+'ZZ'
 s=re.sub(r'\\begin\{equation\}.*?\\end\{equation\}|\\\[.*?\\\]|\\\(.*?\\\)|\$\$.*?\$\$|(?<!\\)\$[^$\n]+\$',protect_math,s,flags=re.S)
 s=re.sub(r'(?<!!)\[([^\]]+)\]\(([^)]+)\)',link,s)
 s=re.sub(r'ZZMATHPROTECTED(\d+)ZZ',lambda m:mathparts[int(m[1])],s)
 # Preserve all prose and mathematics in formal statement/proof pairs.
 patt=r'\*\*(Theorem|Lemma|Corollary|Proposition)\s+([0-9.]+)([^\n]*?)\*\*(.*?)\*\*Proof\.?\*\*(.*?)(?:∎|\\\(\\square\\\))'
 def formal(m):
  kind,num,title,st,pr=m.groups();env=kind.lower();title=title.strip(' .()—–:')
  return '\\begin{'+env+'}'+('['+title+']' if title else '')+'\n'+st.strip()+'\n\\end{'+env+'}\n\\begin{proof}\n'+pr.strip()+'\n\\end{proof}'
 s=re.sub(patt,formal,s,flags=re.S)
 # Local source section references become numbered manuscript references.
 for number in set(re.findall(r'\\label\{'+re.escape(prefix)+r':section-([^}]+)\}',s)):
  s=re.sub(r'(?i)\bsection\s+'+re.escape(number)+r'(?![\d.])',lambda m:'\\cref{'+prefix+':section-'+number+'}',s)
 pre='\\section{'+title+'}\\label{'+prefix+':section}\n'
 pre+='The following complete arguments are retained as re-derivations of their classical prerequisites. Source-specific calculations and their hypotheses are stated explicitly.\n\n'
 # Pandoc's raw-TeX recognizer can misread a source control-space at a
 # physical newline inside a display. Raw blocks preserve every math byte.
 s=re.sub(r'\\begin\{equation\}.*?\\end\{equation\}|\\\[.*?\\\]',lambda m:'\n\n```{=latex}\n'+m[0]+'\n```\n\n',s,flags=re.S)
 md=OUT/(slug(Path(n).stem)+'.md');tex=md.with_suffix('.tex');md.write_text(pre+s)
 cmd=['pandoc','-f','markdown+tex_math_single_backslash+raw_tex','-t','latex','--wrap=preserve',str(md),'-o',str(tex)]
 r=subprocess.run(cmd,capture_output=True,text=True);assert r.returncode==0,(n,r.stderr)
 out=tex.read_text().replace('\\tightlist','')
 # A bracketed cobar word at the beginning of the next array row is not
 # an optional vertical-spacing argument to the preceding row terminator.
 out=re.sub(r'(\\\\\s*\n)([ \t]*)(?=\[)',r'\1\2{}',out)
 out=out.replace('No independent review or novelty claim.','')
 out=re.sub(r'No (?:result[- ]?)?priority[^.]*\.','',out,flags=re.I)
 tex.write_text(out)
 manifest.append({'source':c['source'],'retained':c.get('retained'),'range':[c['start'],c['end']],
  'source_sha256':hashlib.sha256(raw.encode()).hexdigest(),'converted':str(tex.relative_to(D)),
  'converted_sha256':hashlib.sha256(out.encode()).hexdigest(),'category':c['category'],'title':title,
  'mathematical_scope':'Complete selected source range; only recorded provenance/illustration moves; no proof checking claimed by conversion.'})

# Existing registered lesson sections map exactly to their chapter headings.
ac=next(c for c in configs if cname(c)=='almost-complex-structures-and-integrability.md')
for i,suffix in enumerate(['TYPES','OCTONIONS','NIJENHUIS','ASSOCIATOR','TRANSPORT','COORDINATES','GAUGE','ANALYTIC','INTEGRABILITY','SPHERES','EXERCISES'],1):placements['CG-S6-11-'+suffix]=ac['ns']+':section-'+str(i)
sc=next(c for c in configs if cname(c)=='integral-homology-and-sphere-recognition.md')
placements['CG-S6-07-SMOOTH']=sc['ns']+':section'
(W/'III_course_conversion_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
(W/'III_course_placements.json').write_text(json.dumps(placements,indent=2)+'\n')
(W/'III_course_link_map.json').write_text(json.dumps(links,indent=2)+'\n')
(W/'III_course_conversion_moves.json').write_text(json.dumps(removed,indent=2)+'\n')
(W/'III_course_unresolved_links.json').write_text(json.dumps(unmapped,indent=2)+'\n')
(W/'III_course_alignment_repairs.json').write_text(json.dumps(alignment_repairs,indent=2)+'\n')
print('Converted',len(manifest),'complete chapter ranges;',len(placements),'inventory placements;',len(unmapped),'references require resolution')
