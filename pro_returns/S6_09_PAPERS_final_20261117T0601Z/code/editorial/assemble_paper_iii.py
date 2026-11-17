"""Assemble all Paper III proofs after the independently recorded II gate.

This complete-source assembly is an editorial operation. Final source
retention, mathematical dependency, bibliography and layout gates are separate.
"""
from pathlib import Path
import re,json,csv,hashlib,importlib.util
from paper_ii_transform import expand,namespace,normalize_equations,raw_refs,common_cleanup,protect
from statement_dependencies import add_uses
from paper_iii_source_aliases import maps as maps_source_aliases, push as push_source_aliases

ROOT=Path(__file__).resolve().parents[3];D=ROOT/'deliverables';S=ROOT/'sources';E=D/'editorial';W=D/'work'
assert json.loads((D/'records/II_final_validation.json').read_text())['gate_passed'] if 'gate_passed' in json.loads((D/'records/II_final_validation.json').read_text()) else (D/'records/II_final_validation.json').exists()
rows=list(csv.DictReader((D/'S6_09_PAPERS_inventory.csv').open()))
mapsrows=[r for r in rows if r['source_run']=='S6_04_MAPS_MANIFOLDS']
allmapids=[r['source_id'] for r in mapsrows]
knownids={r['source_id'] for r in mapsrows if r['paper']=='III' and ('Cited' in r['kind'] or 'Known' in r['kind'])}
manifest=[];placements={};known=[];pushknown=[];openparts=[];body=[]

def brace(s,pos):
 assert s[pos]=='{';level=1;i=pos+1
 while level:
  if s[i]=='{' and (i==0 or s[i-1]!='\\'):level+=1
  if s[i]=='}' and (i==0 or s[i-1]!='\\'):level-=1
  i+=1
 return s[pos+1:i-1],i

def owned_namespace(s,owner):
 def one(m):
  vals=[]
  for x in m[2].split(','):
   vals.append(x if x.startswith(('maps:','mapsIII:','mapsD:','courseIII:','mapsaudit:','fam:','push:','inv:','cdp:','mapsI:','wb:')) else owner+':'+x)
  return '\\'+m[1]+'{'+','.join(vals)+'}'
 return re.sub(r'\\(label|ref|eqref|cref|Cref|autoref)\{([^}]+)\}',one,s)

def paragraph_results(s):
 marks=[]
 for m in re.finditer(r'\\paragraph\{',s):
  head,end=brace(s,m.end()-1)
  q=re.match(r'(Theorem|Proposition|Lemma|Corollary|Conclusion|Remaining task|Remark|Computation)\s+([A-F]\.\d+\.\d+)\s*(.*)',head,re.S)
  if q:marks.append((m.start(),end,q[1],q[2],q[3]))
 if not marks:return s
 pieces=[s[:marks[0][0]]]
 for i,(start,end,kind,sid,title) in enumerate(marks):
  stop=marks[i+1][0] if i+1<len(marks) else len(s)
  raw=s[end:stop];tail=''
  # A heading introducing the following result stays at its original place.
  m=re.search(r'((?:\s*\\(?:sub)*section\*?\{[^\n]+\}\s*)+)$',raw)
  if m:tail=m[1];raw=raw[:m.start()]
  label='maps:src:'+sid;placements[('S6_04_MAPS_MANIFOLDS',sid)]=label
  env={'Theorem':'theorem','Proposition':'proposition','Lemma':'lemma','Corollary':'corollary','Conclusion':'proposition','Remaining task':'problem','Remark':'remark','Computation':'computed'}[kind]
  ttl=title.strip(' .()')
  ttl=re.sub(r'^(?:Proved|Known, with derivation|Known formula|Refuted)(?:\s*[:;]\s*)?', '',ttl).strip()
  if sid in knownids:ttl='Credited re-derivation'+(': '+ttl if ttl else '')
  if 'Refuted' in title:ttl='Counterexample'+(': '+ttl if ttl else '')
  ttl=ttl.replace('the proposed connected sum in Lead 5','the proposed connected sum for cyclic covers').replace('the normalization in Lead 6','the proposed normalization')
  heading='\\begin{'+env+'}'+('['+ttl+']' if ttl else '')+'\\label{'+label+'}\n'
  p=raw.find('\\begin{proof}')
  if p>=0:block=heading+raw[:p]+'\\end{'+env+'}\n'+raw[p:]
  else:block=heading+raw+'\n\\end{'+env+'}\n'
  manifest.append({'source_id':sid,'source_original_heading':kind+' '+sid+' '+title,'expanded_original_sha256':hashlib.sha256(raw.encode()).hexdigest(),'complete_expanded_source':raw,'destination_label':label,'routing':'known appendix' if sid in knownids else 'open final part' if sid=='D.2.4' else 'body'})
  if sid in knownids:known.append(block);pieces.append('The complete credited statement and re-derivation are in \\cref{'+label+'}.\n'+tail)
  elif sid=='D.2.4':openparts.append(block);pieces.append('The exact remaining classification questions and all established subcases are in \\cref{'+label+'}.\n'+tail)
  else:pieces.append(block+tail)
 return ''.join(pieces)

def maps_adapt(s):
 s=maps_source_aliases(s)
 s=owned_namespace(s,'maps')
 s,_=normalize_equations(s,'maps')
 s=raw_refs(s,allmapids,'maps:src:')
 s=common_cleanup(s)
 s=re.sub(r'\\(sub)*section\{[A-F]\.\d*\.?\s*',lambda m:'\\'+(m[1] or '')+'section{',s)
 s=s.replace('We claim no priority for that general algorithm.','The general algorithm is credited to its published source.')
 return s

# The unrestricted extension counterexample belongs with the sphere maps;
# the canonical circle quotient and its complete proof are already in I.
ma=(S/'returns/S6_04_MAPS_MANIFOLDS/sections/maps_A.tex').read_text()
ma=ma[ma.index('\\paragraph{Proposition A.2.2'):]
body.append('\\section{Sphere maps, framings and homotopy classes}\\label{sec:III:maps}\n'+maps_adapt(paragraph_results(ma)))
for filename in ['maps_B','kummer','manifolds','fourfolds']:
 s=expand((S/'returns/S6_04_MAPS_MANIFOLDS/sections'/(filename+'.tex')).read_text(),'S6_04_MAPS_MANIFOLDS')
 if filename=='manifolds':
  p=E.parent/'code/editorial/paper_iii_D_corrections.py'
  if p.exists():
   spec=importlib.util.spec_from_file_location('paper_iii_D_corrections',p);mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);s=mod.transform(s)
 if filename=='fourfolds':
  # Additional full proof of the classical rank-five spin bridge.
  marker='\\paragraph{Theorem F.2.10'
  pos=s.index(marker)
  s=s[:pos]+(W/'root/F_spin_bridge_repair.tex').read_text()+'\n'+s[pos:]
  marker='\\paragraph{Theorem F.2.6'
  pos=s.index(marker)
  s=s[:pos]+(W/'maps_audit/fourfold_torsion_transgression.tex').read_text()+'\n'+s[pos:]
  for marker,insert in [
   ('The free action makes the Borel construction equivalent to','maps_F_cyclic_bar_inclusion.tex'),
   ('We specify finite integer chains, rather than only the','maps_F_log_cylinder_scope.tex')]:
   assert s.count(marker)==1,(insert,s.count(marker))
   extra=(W/'invariants_arithmetic'/insert).read_text()
   extra=re.sub(r'\\paragraph\{([^\n]+)\}',lambda m:'\\par\\medskip\\noindent\\textbf{'+m[1]+'}\\quad ',extra)
   s=s.replace(marker,extra+'\n'+marker)
  marker='\\paragraph{Theorem F.2.35'
  assert s.count(marker)==1
  credit=(W/'invariants_arithmetic/maps_F_source_credit.tex').read_text().replace('theorem emph{','theorem \\emph{')
  s=s.replace(marker,credit+'\n'+marker)
  s=s.replace('Euler characteristic discussion in Section~2','Euler characteristic discussion in Section~3, Theorem~3.6, pp.~435--436')
  s=s.replace('\\cite{rootIWX20}',r'\cite[Corollary~1.3 and Table~1, pp.~112--113]{IsaksenWangXu2023}')
 s=paragraph_results(s)
 body.append(maps_adapt(s))

# The separate complete smooth-monodromy arguments, with their actual cap
# and linking calculations, retain the source definitions and all inputs.
push=expand((S/'returns/S6_02_PUSH/sections/C_push.tex').read_text(),'S6_02_PUSH')
push=push_source_aliases(push)
pm=list(re.finditer(r'\\begin\{(?:theorem|proposition|lemma|corollary|remark|problem)\}\[(C\.\d+\.\d+)\b[^\]]*\]',push))
pk={r['source_id'] for r in rows if r['source_run']=='S6_02_PUSH' and r['paper']=='III' and ('Cited' in r['kind'] or 'Known' in r['kind'])}
chunks=[push[:pm[0].start()]]
sharedroutes=[]
for i,m in enumerate(pm):
 end=pm[i+1].start() if i+1<len(pm) else len(push)
 block=push[m.start():end];tail=''
 h=re.search(r'((?:\s*\\(?:sub)*section\*?\{[^\n]+\}\s*)+)$',block)
 if h:tail=h[1];block=block[:h.start()]
 sid=m[1]
 if sid=='C.3.5':
  chunks.append('The complete coherent closing translation and its full chartwise proof are in \\cref{push:src:C.3.5}.\n'+tail)
  sharedroutes.append({'source_run':'S6_02_PUSH','source_id':sid,'paper':'I','printed_label':'push:src:C.3.5','removed_duplicate_sha256':hashlib.sha256(block.encode()).hexdigest(),'reason':'Same complete C_closing_cocycle.tex proof already printed in Paper I; no distinct argument removed.'})
 elif sid in pk:
  pushknown.append(block);chunks.append('The credited statement and complete re-derivation are in \\cref{push:src:'+sid+'}.\n'+tail)
 else:chunks.append(block+tail)
push=''.join(chunks)
push=owned_namespace(push,'push')
def pushhead(m):
 env,title=m[1],m[2];q=re.match(r'([A-F]\.\d+\.\d+)\s*(.*)',title,re.S)
 if not q:return m[0]
 sid=q[1];label='push:src:'+sid;placements[('S6_02_PUSH',sid)]=label
 title=q[2].strip(' ();:');title=re.sub(r'^(?:Proved|Known, with derivation)\)?:?\s*','',title)
 return '\\begin{'+env+'}'+('['+title+']' if title else '')+'\\label{'+label+'}'
push=re.sub(r'\\begin\{(theorem|proposition|lemma|corollary|remark|problem)\}\[([^\]]+)\]',pushhead,push)
pushids=[r['source_id'] for r in rows if r['source_run']=='S6_02_PUSH']
push=raw_refs(push,pushids,'push:src:');push,_=normalize_equations(push,'pushIII')
body.append(common_cleanup(push))
pushknown=[common_cleanup(normalize_equations(raw_refs(re.sub(r'\\begin\{(theorem|proposition|lemma|corollary|remark|problem)\}\[([^\]]+)\]',pushhead,owned_namespace(x,'push')),pushids,'push:src:'),'pushIII')[0]) for x in pushknown]

trans=json.loads((W/'root/family_transferred_to_III.json').read_text())
fam=trans[0]['statement']+'\n'+trans[0]['proof']
fam=namespace(fam,'fam').replace('\\label{fam:st:E.2.2}','\\label{fam:src:E.2.2}')
fam=fam.replace('E.2.2; Proved','The actual positive-loop clutching map')
fam=fam.replace("Cerf's\nCorollary~2 in dimension six \\cite[p.~76]{Cerf71}",r"Cerf's sphere-gluing comparison in dimension six \cite[Theorem~0 and Corollaries~1--2, p.~8]{Cerf1970}")
fam=fam.replace(r'\cite[Section 7, pp.~100--103]{EK62}',r'\cite[Section~6, equation~(11), pp.~101--103]{EellsKuiper1962}')
fam,_=normalize_equations(fam,'famIII')
placements[('S6_02_FAMILY','E.2.2')]='fam:src:E.2.2'
body.append('\\section{The parameter-loop reduction in the family marking}\n'+fam)
# Retain the full historical unresolved target with its now-proved resolution,
# without displaying its obsolete assertion as a currently open problem.
hist=trans[1]['statement'];hist=namespace(hist,'fam')
hist=hist.replace('\\begin{problem}[E.2.3; Open, with local fillings and an invariant reduction]','\\begin{remark}[Resolution of the original compact-filling and mapping-class questions]')
hist=hist.replace('\\end{problem}','\\end{remark}').replace('\\label{fam:st:E.2.3}','\\label{fam:src:E.2.3}')
hist=hist.replace('We have not assembled a flat proper filling of the compact $S^6$\nfamily over $w=0$.', 'The original question asked for a flat proper filling of the compact $S^6$ family over $w=0$. The specific equivariant compactification is excluded by Paper~I, \\ref{push:src:B.4.33}.')
hist=hist.replace('The smallest missing finite-place instance is','The finite-place test in that question was').replace('the unresolved periodic gluing is','the prescribed periodic gluing was')
hist=hist.replace('No Pontryagin-number or\nsignature calculation for a coboundary of this particular\n$\\Sigma_\\Phi$ has been completed.', 'The complete characteristic and boundary calculations in \\cref{push:src:C.3.24,push:src:C.3.27} give zero for this particular $\\Sigma_\\Phi$.')
hist=hist.replace('The smallest undecided numeric\ninstance is','The numeric instance to be evaluated was').replace('The identity\non cohomology proved above supplies no value for that residue.', 'The identity on cohomology alone does not evaluate that residue; the complete cap calculations do.')
hist=raw_refs(hist,['E.2.1','E.1.5'],'fam:src:').replace('(E10)',r'\eqref{famIII:eq:E10}')
placements[('S6_02_FAMILY','E.2.3')]='fam:src:E.2.3';body.append(hist)

# Every working-edition carrier construction is retained with its complete
# point-set and metric arguments, before its separately checked repairs.
body.append('\\section{Local covers, global quotients and cusp carriers}\\label{sec:III:carriers}\n')
for name in ['cusp_toric_cover_completion','cusp_globalization_replacement','cusp_cone_sphere_routes','cusp_sphere_route_strengthening','cusp_s12_carrier_homotopy']:
 s=(S/'workbench'/(name+'.tex')).read_text();s=namespace(s,'wb')
 for r in rows:
  if r['paper']=='III' and r['source_run']=='working_edition' and name+'.tex' in r['source_file']:
   label='wb:'+r['source_id']
   if '\\label{'+label+'}' in s:placements[(r['source_run'],r['source_id'])]=label
   elif r['source_id'].endswith(':L567'):
    pos=s.rfind('\\begin{corollary}');assert pos>=0
    s=s[:pos]+s[pos:].replace('\\begin{corollary}','\\begin{corollary}\\label{'+label+'}',1);placements[(r['source_run'],r['source_id'])]=label
 body.append(common_cleanup(s))
late=E/'III_late_carriers.tex'
if late.exists():body.append(late.read_text())
for name in ['globalization_deck_group_correction','carrier_three_complex_wedge','kummer_compact_chart_repair','finite_degree_three_correction','carrier_nullhomotopy_by_extension']:
 body.append(common_cleanup((W/'maps_audit'/(name+'.tex')).read_text()))
placements[('working_edition_reader_extension','G2-8')]='mapsaudit:almost-complex-homotopy'

body.append('\\appendix\n\\renewcommand{\\thesection}{\\AlphAlph{\\value{section}}}\n\\renewcommand{\\theHsection}{appendix.\\arabic{section}}\n\\section{Known source results and complete re-derivations}\\label{app:III:known}\n')
body.append(r'\paragraph{Almost-complex homotopy.} The fixed-orientation homotopy conclusion is stated in \cite[Section~1.4, p.~7]{AC26}. The following complete section-bundle argument is a credited expanded derivation.'+'\n')
body.append(common_cleanup((W/'maps_audit/almost_complex_homotopy.tex').read_text()))
body.extend(maps_adapt(x) for x in known)
body.extend(pushknown)
modular=W/'invariants_arithmetic/maps_modular_collision_realizations.tex'
if modular.exists():
 mtext=modular.read_text()
 mtext=re.sub(r'\\paragraph\{([^\n]+)\}',lambda m:'\\par\\medskip\\noindent\\textbf{'+m[1]+'}\\quad ',mtext)
 body.append(common_cleanup(mtext))

course=json.loads((W/'maps_audit/III_course_conversion_manifest.json').read_text())
course_reference_path=D/'code/maps_audit/repair_course_pinned_references.py'
course_reference_spec=importlib.util.spec_from_file_location('course_reference_repairs',course_reference_path)
course_reference_module=importlib.util.module_from_spec(course_reference_spec)
course_reference_spec.loader.exec_module(course_reference_module)
course_credit_path=W/'maps_audit/III_course_source_credit_insertions.json'
course_credits=json.loads(course_credit_path.read_text()) if course_credit_path.exists() else []
applied_course_credits=[]
from normalize_course_structure import transform as normalize_course_structure, write_record as write_course_structure_record
for r in course:
 course_text=(D/r['converted']).read_text()
 course_text=course_reference_module.transform(course_text,r['converted'])
 for credit in course_credits:
  if Path(credit['source_tex']).name!=Path(r['converted']).name:continue
  assert course_text.count(credit['insert_after'])==1,(credit['source_tex'],'credit anchor')
  assert credit['idempotence_marker'] not in course_text,(credit['source_tex'],'duplicate credit')
  course_text=course_text.replace(credit['insert_after'],credit['insert_after']+credit['insert_text'])
  applied_course_credits.append(credit['source_tex'])
 course_text=normalize_course_structure(course_text,r)
 body.append(course_text)
 if Path(r['source']).name=='framed-manifolds-and-the-pontryagin-thom-map.md':
  repair=(W/'maps_audit/pt_relative_bordism_repair.tex').read_text()
  repair=re.sub(r'\\paragraph\{([^\n]+)\}',lambda m:'\\par\\medskip\\noindent\\textbf{'+m[1]+'}\\quad ',repair)
  body.append(repair)
 if Path(r['source']).name=='coefficient-rings-and-the-original-degree-six-class.md':body.append((W/'maps_audit/coefficient_h28_complete_certificate.tex').read_text())
assert len(applied_course_credits)==len(course_credits),(len(applied_course_credits),len(course_credits))
write_course_structure_record()
cp=json.loads((W/'maps_audit/III_course_placements.json').read_text())
for r in rows:
 if r['paper']=='III' and r['source_id'] in cp:placements[(r['source_run'],r['source_id'])]=cp[r['source_id']]
for r in rows:
 if r['paper']=='III' and r['source_run']=='WRITING_REPAIR':
  lab=re.search(r'\\label\{([^}]+)\}',r['statement_as_printed'])
  if lab:placements[(r['source_run'],r['source_id'])]=lab[1]
for name in ['III_result_index','III_programs','III_provenance']:
 p=E/(name+'.tex')
 if p.exists():body.append(p.read_text())
body.append('\\clearpage\\part{Questions not established by the present arguments}\\label{part:III:open}\n')
body.extend(maps_adapt(x) for x in openparts)

text='\n'.join(body)
embedded_bibliographies=re.findall(r'\\begin\{thebibliography\}.*?\\end\{thebibliography\}',text,re.S)
if embedded_bibliographies:
 (W/'root/III_consolidated_embedded_bibliographies.json').write_text(json.dumps({'reason':'All entries are in the verified common APA bibliography; local numerical bibitems would duplicate destinations and force natbib numeric mode. No mathematical proof text removed.','removed_local_bibliographies':embedded_bibliographies},indent=2)+'\n')
 text=re.sub(r'\\begin\{thebibliography\}.*?\\end\{thebibliography\}','',text,flags=re.S)
from paper_iii_carrier_corrections import transform as carrier_corrections
text=carrier_corrections(text)
credit_insertions=W/'invariants_arithmetic/push_C_credit_insertions.json'
if credit_insertions.exists():
 for item in json.loads(credit_insertions.read_text()):
  if item['source_id'] not in {'C.3.1','C.3.8'}:continue
  lab=item['printed_label'];pos=text.index('\\label{'+lab+'}')
  end=re.search(r'\\end\{(?:theorem|proposition|lemma|corollary)\}',text[pos:])
  assert end,(lab,'statement end missing')
  insertion=item['tex'].replace('original first version','original version~1')
  at=pos+end.end();text=text[:at]+'\n'+insertion+'\n'+text[at:]
text=re.sub(r'\\(ref|eqref|cref|Cref|autoref)\{([^}]+)\}',lambda m:'\\'+m[1]+'{'+re.sub(r'%[^\n]*\n\s*','',m[2])+'}',text)
text=text.replace('{wb:prop:geometric-pi1}','{mapsI:top:prop:geometric-pi1}')
text=text.replace('{wb:h24:ret:main}','{maps:src:B.3.1}')
# Late credit insertions use the same actually opened v1 as the common
# bibliography; the source shorthand key has no independent verification.
text=text.replace('{DGKXv1}','{DuEtAl2026v1}')
# Source-inherited comma superscripts were typography artifacts in the
# spin-c formula; its proof uses the ordinary second and fourth powers.
for old,new in [(r'\bar p^{,2}',r'\bar p^{\,2}'),(r'\bar c^{,2}',r'\bar c^{\,2}'),(r'\bar c^{,4}',r'\bar c^{\,4}')]:
 assert text.count(old)==1,(old,text.count(old))
 text=text.replace(old,new)
text=text.replace('convention of C.3.19:',r'convention of \cref{push:src:C.3.19}:')
text=text.replace('seven-manifold of C.3.20:',r'seven-manifold of \cref{push:src:C.3.20}:')
push_standalone=W/'cdp_audit/push_C_retention/editorial_findings.json'
standalone_changes=[]
for fix in json.loads(push_standalone.read_text())['replacements'][5:]:
 # The first five typography/reference repairs were applied immediately
 # above.  Apply the eleven remaining exact repairs independently of the
 # audit's mutable status field: its later 'Observed applied' status must
 # not silently remove a repair from a fresh assembly.
 assert text.count(fix['before'])==1,(fix['source_id'],fix['before'],text.count(fix['before']))
 after=fix['after'].replace(r'Paper~I, Theorem~21.58',r'\cref{push:src:B.4.33}')
 text=text.replace(fix['before'],after)
 standalone_changes.append({**fix,'after':after,'status':'Applied after independent full contextual review; mathematical argument retained'})
(D/'records/III_push_standalone_edits.json').write_text(json.dumps(standalone_changes,ensure_ascii=False,indent=2)+'\n')
from final_standalone_fixes import transform as final_standalone_fixes
text=final_standalone_fixes(text,'III')
# The unique closing-cocycle proof and all of its equations are in Paper I.
for old in re.findall(r'\\label\{([^}]+)\}',(S/'returns/S6_02_PUSH/sections/C_closing_cocycle.tex').read_text()):
 text=text.replace('{push:'+old+'}','{mapsI:closing:'+old+'}')
text=re.sub(r'\\cite(?:p|t)?(?:\[[^\]]*\])?\{rootIWX20\}',lambda m:r'\cite[Corollary~1.3 and Table~1, pp.~112--113]{IsaksenWangXu2023}',text)
text=text.replace('differentials vanish by their different weights.',r'differentials vanish by their different weights \cite[Proposition~8.3.5, pp.~42--43]{mapsDeligne1974HodgeIII}.')
text=re.sub(r'(?:No|no) (?:novelty or )?priority claim\s+is made[^.]*\.','',text)
text=re.sub(r'(?:The )?statement makes no priority claim\.','',text)
text=re.sub(r';?\s*we claim no priority for integral-conjugacy\s+algorithms\.','.',text)
text=text.replace('No claim of priority is made.','').replace('This states the search outcome and claims no priority.','This states the search outcome.')
# One source statement is shared across papers. Resolve source aliases to the
# unique printed statement before replacing cross-paper refs by real numbers.
for r in mapsrows:
 if r['paper']!='III' and r['printed_label']:
  text=text.replace('{maps:src:'+r['source_id']+'}','{'+r['printed_label']+'}')
available=set(re.findall(r'\\label\{([^}]+)\}',text))
for r in rows:
 if r['paper']=='III' and r['source_run']=='working_edition' and r['printed_label'] in available:
  placements[(r['source_run'],r['source_id'])]=r['printed_label']
for paper in ['I','II']:
 aux=(D/('S6_09_PAPERS_'+paper+'.aux')).read_text()
 nums=dict(re.findall(r'\\newlabel\{([^}]+)\}\{\{([^}]+)\}',aux))
 kinds=dict(re.findall(r'\\newlabel\{([^}]+)@cref\}\{\{\[([^\]]+)\]',aux))
 def external(m):
  keys=m[2].split(',');out=[]
  for key in keys:
   if key in nums and key not in available:
    kind='Equation' if m[1]=='eqref' else kinds.get(key,'result').capitalize()
    out.append('Paper~'+paper+', '+kind+'~'+nums[key])
   else:out.append('\\'+m[1]+'{'+key+'}')
  return ' and '.join(out)
 text=re.sub(r'\\(ref|eqref|cref|Cref|autoref)\{([^}]+)\}',external,text)
from normalize_external_reference_words import transform as normalize_external_reference_words
text=normalize_external_reference_words(text,'III')
from paper_iii_layout import transform as layout_corrections
text=layout_corrections(text)
text=add_uses(text,'III')
pre=(E/'shared_preamble.tex').read_text().replace('S6_09_PAPERS_I','S6_09_PAPERS_III').replace('Paper I}','Paper III}')
pre=re.sub(r'pdftitle=\{[^}]*\}', 'pdftitle={Maps from the complex six-spheres and the manifolds of the torus-fibration construction}', pre)
pre=re.sub(r'% statement_plain:.*','% statement_plain: Sphere-map homotopy classes, trivial smooth parameter monodromy, explicit manifold invariants, compact fourfolds and complete marked classification algorithms.',pre)
pre=re.sub(r'% main_statements:.*','% main_statements: maps:src:B.1.2, maps:src:B.2.1, push:src:C.3.27, maps:src:E.2.4, maps:src:F.2.39, maps:src:F.4.1',pre)
pre=re.sub(r'% open_points:.*','% open_points: precisely scoped remaining noncanonical and torsion-marked six-manifold filling questions',pre)
pre=pre.replace(r'\fancyhead[L]{\small The $(3,4,\infty)$ family}',r'\fancyhead[L]{\small Sphere maps and manifold constructions}')
pre+=r'\newcommand{\HP}{\mathbb{HP}}'+'\n'
pre+=r'\renewcommand{\Uses}[1]{\par\smallskip\begingroup\raggedright\noindent\textit{Uses:} #1.\par\endgroup\smallskip}'+'\n'
extra=E/'III_extra_preamble.tex'
if extra.exists():pre+=extra.read_text()+'\n'
front=(E/'III_front.tex').read_text();back=(E/'III_back.tex').read_text()
bib=E/'III_bibliography.tex'
if bib.exists():back=re.sub(r'\\bibliographystyle\{[^}]+\}\s*\\bibliography\{[^}]+\}',lambda m:bib.read_text(),back)
final=pre+'\n\\begin{document}\n'+front+'\n'+text+'\n'+back+'\n\\end{document}\n'
(D/'S6_09_PAPERS_III.tex').write_text(final)
jsonrows=[{'source_run':a,'source_id':b,'printed_label':lab} for (a,b),lab in placements.items()]
(W/'root/III_source_placements.json').write_text(json.dumps(jsonrows,indent=2)+'\n')
(W/'root/III_shared_statement_routes.json').write_text(json.dumps(sharedroutes,indent=2)+'\n')
(W/'root/III_assembly_manifest.json').write_text(json.dumps({'source_result_blocks':manifest,'course_ranges':course,'source_placements':len(jsonrows),'known_source_ids':sorted(knownids),'stage':'complete-source candidate; separate validation pending'},indent=2)+'\n')
print('III complete-source candidate:',len(final),'characters;',len(manifest),'MAPS blocks;',len(jsonrows),'source placements')
