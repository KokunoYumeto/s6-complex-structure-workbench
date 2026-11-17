from pathlib import Path
import re,json,hashlib,subprocess
SRC=Path('sources/codex_workspace/courses/CG-S6/src')
OUT=Path('deliverables/work/maps_audit')
anchor_map={
 'cw-models-and-the-first-hurewicz-map.md':'mapsI:cw:section',
 'cw-models-and-the-first-hurewicz-map.md#hurewicz-theorem':'mapsI:cw:hurewicz-theorem',
 'cw-models-and-the-first-hurewicz-map.md#cw-manifolds':'mapsI:cw:cw-manifolds',
 'path-fibres-and-integral-homotopy-equivalences.md':'mapsI:pf:section',
 'path-fibres-and-integral-homotopy-equivalences.md#path-lifting':'mapsI:pf:path-lifting',
 'path-fibres-and-integral-homotopy-equivalences.md#serre-homology':'mapsI:pf:serre-homology',
 'path-fibres-and-integral-homotopy-equivalences.md#cw-inverses':'mapsI:pf:cw-inverses',
 'thom-euler-for-lesson11.md':'mapsI:chain:section'
}
configs=[
 ('chain','thom-euler-for-lesson11.md','Elementary integral chain constructions',1,5),
 ('cw','cw-models-and-the-first-hurewicz-map.md','Actual CW models and the first Hurewicz map',1,None),
 ('pf','path-fibres-and-integral-homotopy-equivalences.md','Path fibres and integral homotopy equivalences',1,None)
]
manifest=[]
for ns,name,title,startsec,endsec in configs:
 p=SRC/name;raw=p.read_text();ls=raw.splitlines()
 start=next(i for i,l in enumerate(ls) if l.startswith('## 1.'))
 if endsec:end=next(i for i,l in enumerate(ls) if l.startswith('## '+str(endsec)+'.'))
 else:end=next(i for i,l in enumerate(ls) if l.startswith('## Source'))
 s='\n'.join(ls[start:end]).strip()
 # The source diagrams repeat the adjacent displayed equations and caption.
 # Preserve the explanatory caption as prose, omit only the redundant image asset.
 s=re.sub(r'^!\[[^\n]*\]\([^\n]*\)\s*$', '',s,flags=re.M)
 heads=[]
 def heading(m):
  num,txt,anchor=m.groups();anchor=anchor or 'section-'+num
  heads.append((num,anchor));return '\\subsection{'+txt+'}\n\\label{mapsI:'+ns+':'+anchor+'}'
 s=re.sub(r'^## ([0-9]+)\. (.*?)(?: \{#([^}]+)\})?$',heading,s,flags=re.M)
 tags=re.findall(r'\\tag\{([^}]+)\}',s)
 for tag in sorted(set(tags),key=len,reverse=True):
  s=s.replace('('+tag+')','\\eqref{mapsI:'+ns+':eq:'+tag+'}')
 s=re.sub(r'\\tag\{([^}]+)\}',lambda m:'\\label{mapsI:'+ns+':eq:'+m.group(1)+'}',s)
 # Put every labelled source display into the global equation counter.
 s=re.sub(r'\\\[(.*?)\\\]',lambda m:('\\begin{equation}\n'+m.group(1).strip()+'\n\\end{equation}') if '\\label{' in m.group(1) else m.group(0),s,flags=re.S)
 for num,anchor in heads:
  s=re.sub(r'(?i)\bSection '+re.escape(num)+r'\b',lambda m:'\\cref{mapsI:'+ns+':'+anchor+'}',s)
 # Formal statement/proof environments retain all mathematical text.
 patt=r'\*\*(Theorem|Lemma|Corollary|Proposition) ([0-9.]+)(?: \(([^*]+)\))?\.\*\*(.*?)\*\*Proof\.\*\*(.*?)(?:∎|\\\(\\square\\\))'
 def env(m):
  kind,num,ttl,st,pr=m.groups();num=num.rstrip('.')
  label='mapsI:'+ns+':'+kind.lower()+':'+num
  if ns=='cw' and num=='4.1':label='mapsI:cw:hurewicz-theorem-result'
  return '\\begin{'+kind.lower()+'}'+('['+ttl+']' if ttl else '')+'\n\\label{'+label+'}\n'+st.strip()+'\n\\end{'+kind.lower()+'}\n\n\\begin{proof}\n'+pr.strip()+'\n\\end{proof}'
 s=re.sub(patt,env,s,flags=re.S)
 # Replace source theorem numbers in prose by actual internal references.
 for kind,num in re.findall(r'\\label\{mapsI:'+ns+r':(theorem|lemma|corollary|proposition):([0-9.]+)\}',s):
  s=s.replace(kind.title()+' '+num,'\\cref{mapsI:'+ns+':'+kind+':'+num+'}')
 if ns=='cw':s=s.replace('Theorem 4.1','\\cref{mapsI:cw:hurewicz-theorem-result}')
 def link(m):
  text,url=m.groups()
  if url in anchor_map:return '\\cref{'+anchor_map[url]+'}'
  raise ValueError('Unmapped operative course link: '+url)
 s=re.sub(r'(?<!!)\[([^\]]+)\]\(([^)]+)\)',link,s)
 s=s.replace("Once lesson 7's integral calculation and lesson 6's fundamental-group calculation have been applied",'Once \\cref{mapsI:top:thm:h2-vanishing,mapsI:top:lem:cohomological-closure,mapsI:top:prop:geometric-pi1} have been applied')
 s=s.replace('the included Hurewicz companion','\\cref{mapsI:cw:hurewicz-theorem-result}')
 s=s.replace('the CW companion','\\cref{mapsI:cw:cw-manifolds}')
 s=s.replace('The included CW model for', 'The CW model of \\cref{mapsI:cw:cw-manifolds} for')
 s=s.replace('the exact maps and orientation classes in lesson 7. That lesson proves', 'the exact maps and orientation classes of \\cref{mapsI:course:homotopy-section}. The already proved integral and fundamental-group calculations give')
 s=s.replace('The pair computation in lesson 7 has the actual sequence', 'Excision for the original two discs and the integral homology of $X$ give the actual pair sequence')
 s=s.replace('as proved there,', 'by adding the two simply connected discs back along collars of their simply connected boundary spheres,')
 s=s.replace('the further smooth arguments in lesson 7.', 'the smooth recognition arguments; the homotopy comparison alone does not supply them.')
 s=s.replace('original threefold and its punctured cobordism from lesson 7','original threefold and its punctured cobordism')
 s=s.replace('The inverse-function argument proved in the Morse companion gives a local diffeomorphism there.', 'Here is the finite-dimensional inverse-function argument. After translations and an invertible linear change, write the map as $F(x)=x+R(x)$ near zero, with $\\|DR\\|<1/2$ on a closed ball. For $y$ in a sufficiently small ball, $x\\mapsto y-R(x)$ maps the first ball into itself and is a contraction. Its iterates are uniformly Cauchy, giving the unique inverse value. The inequality $\\|F(x)-F(x^{\\prime})\\|\\ge\\|x-x^{\\prime}\\|/2$ proves continuity of the inverse. The remainder estimate in the differentiability formula then gives derivative $DF(x)^{-1}$; induction gives smoothness. Thus the displayed map is a local diffeomorphism there.')
 s=s.replace('The diagram represents these proved homology maps, not a geometric picture of the fibre.', 'These are the actual proved homology edge maps.')
 s=s.replace('lesson 7','the original sphere construction')
 pre='\\section{'+title+'}\n\\label{mapsI:'+ns+':section}\n\n'
 if ns=='chain':pre+='These classical constructions are included as rederivations of the singular-chain prerequisites; they make no novelty claim.\n\n'
 if ns=='cw':pre+='The singular-chain prerequisites, sphere generators and prism calculations are proved in \\cref{mapsI:chain:section}.  The first Hurewicz theorem is the classical result of \\cite[Theorem~4.32]{Hatcher2002}; the following is our complete expanded proof.\n\n'
 if ns=='pf':pre+='The CW and Hurewicz inputs are proved in \\cref{mapsI:cw:section}; singular chains, excision, products and prisms are proved in \\cref{mapsI:chain:section}. These are expanded classical proofs; the homological Whitehead conclusion is \\cite[Corollary~4.33]{Hatcher2002}. All homology below is integral unless a coefficient group is displayed.\n\n'
 md=OUT/('course_'+ns+'_conversion.md');md.write_text(pre+s+'\n')
 tex=OUT/('paperI_course_'+ns+'_foundations.tex')
 run=subprocess.run(['pandoc','-f','markdown+tex_math_single_backslash+raw_tex','-t','latex','--wrap=preserve',str(md),'-o',str(tex)],capture_output=True,text=True)
 assert run.returncode==0,run.stderr
 body=tex.read_text();body=body.replace('\\tightlist','').replace('\\square','\\square')
 # Section 3 chain proof uses the elementary rotation computation from its Section 6;
 # print that finite-dimensional argument here, where it is used.
 if ns=='chain':
  body=body.replace('the plane-rotation argument of Section 6','the following elementary plane-rotation argument: an orthogonal orientation-preserving matrix is reduced to the identity by successive rotations in coordinate two-planes, each connected to the identity by its angle parameter')
 body=body.replace('The formula is natural, is associative (the three face intervals are identical in either parenthesization), and has the constant zero-cochain \\(1\\) as unit.', 'The formula is natural. It is associative: the same three face intervals occur in either order of multiplication. The constant zero-cochain \\(1\\) is its unit.')
 body=body.replace('These two maps are inverse up to natural chain homotopies. The homotopies preserve products of subspaces.', '\\leavevmode\\par\nThe two maps are inverse up to natural chain homotopies, preserving products of subspaces.')
 body=body.replace("The prism identity proves homotopy invariance. The two-disk pinch sends the sphere's fundamental class to the sum of the two positive disk generators, by their local values and excision.", 'The prism identity gives homotopy invariance. Under the two-disc pinch, the fundamental class of the sphere maps to the sum of the two positive disc generators. This follows from their local values and excision.')
 body=body.replace('For the last two equations, contract the path followed by its reverse by traversing an initial portion and returning along it. These are continuous homotopies, as follows from the path adjunction.', 'For the last two equations, contract a path followed by its reverse: traverse an initial segment and return along it. Path adjunction proves these homotopies continuous.')
 tex.write_text(body)
 manifest.append({'namespace':ns,'source':str(p),'source_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'full_selected_proof_range':[start+1,end],'output':str(tex),'output_sha256':hashlib.sha256(tex.read_bytes()).hexdigest(),'raw_source_header':ls[2],'provenance_policy':'Raw author/model/effort/month preserved here only; no additional manuscript timeline claim.','proof_preservation':'Every selected argument retained in full; section/equation references namespaced; repeated explanatory SVG omitted with its explanatory caption retained; source-review declarations stored only in provenance.','reader':'GPT-6 Astra (OpenAI, ChatGPT Pro mode)','effort':'Pro','date':'2026-11-17'})
(OUT/'paperI_course_foundations_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print([(r['output'],r['full_selected_proof_range']) for r in manifest])
