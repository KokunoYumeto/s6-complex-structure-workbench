from pathlib import Path
import json,hashlib,datetime,re
R=Path('/workspace/scratch/653608133b22');O=R/'work/agents/i_analytic';s=(R/'work/S6_SERIES_PUBLISH_I.tex').read_text()
p=O/'S6_SERIES_PUBLISH_I_final_candidate11_reading_analytic_guards.json';d=json.loads(p.read_text());d['guards']=d['guards'][:4]
def add(page,typ,old,new,why):
 assert s.count(old)==1,(page,old,s.count(old));d['guards'].append({'id':f"I-VIS-A{len(d['guards'])+1:02d}",'page':page,'defect_type':typ,'old':old,'new':new,'expected_count':1,'reason':why})
add(131,'D02/D12',' These statements concern the canonical map, not\nmerely equal dimensions.','','The preceding exact base-change sequence and explicit isomorphism statement already give the canonical comparison. Keep both; remove this repeated contrast.')
add(132,'D02',r'''It is therefore an analytic continuation through
that point, contrary to Proposition~\ref{push:src:D.1.1}. No choice of the
fibrewise biholomorphisms was used. Thus the weaker hypothesis already
leads to the contradiction.''',r'''The pointwise agreement gives an analytic continuation through
that point, contrary to Proposition~\ref{push:src:D.1.1}.''','The statement and proof retain the fibrewise-isomorphism hypothesis and its exact intrinsic invariant; express the completed comparison positively without repeating the conclusion.')
add(137,'D02',r'''No statement of convergence of compact complex
threefolds follows from a real-group limit. In particular \ref{push:src:D.1.3}
already excludes a holomorphic proper extension.''',r'''Theorem~\ref{push:src:D.1.3} excludes a flat proper holomorphic
extension across the parameter boundary.''','Retain the precise cited nonextension result, with its explicit flatness scope, in place of the general negative comparison.')
add(144,'D02/D18',r'''$\operatorname{Hom}(T^*L,L)=\pi^*\OO_B(1)$ \cite[Lemma 2.1]{Engel2026}.
Its identification applies here with exactly $T=t_{6P}$ and $L=\OO(P-O)$;
there is no replacement of the translation by its inverse in this
normal-bundle calculation.''',r'''$\operatorname{Hom}(T^*L,L)=\pi^*\OO_B(1)$
\cite[Lemma~2.1, pp.~3--4]{Engel2026}.
Its identification applies here with $T=t_{6P}$ and $L=\OO(P-O)$.''','Preserve the exact direction T=t6P, bundle L, pullback Hom identity and following degree calculation; remove only the inverse-translation disclaimer. Primary pp3–4 actually read.')
add(147,'D02/D18',r'''\item For completeness, the relation to the infinite fan quotient is
also explicit. In a Tate covering of a neighbourhood of the $I_1$
fibre use the torus coordinates $(Z,W)$ of Engel's Proposition 2.7.''',r'''\item In a Tate covering of a neighbourhood of the $I_1$
fibre use the torus coordinates $(Z,W)$ of
\citet[Proposition~2.7, p.~6]{Engel2026}.''','The complete covering, two period maps, unit corrections and small-resolution comparison remain. Remove the defensive preface and supply the actually-read primary page.')
add(149,'D02',r'''Here $A_j$ denotes a scalar only within this proof; it is not a
monodromy matrix.''',r'''Here $A_j$ denotes the displayed scalar constant within this proof.''','Keep the local scalar convention and every period/root formula, using a positive definition.')
add(152,'D02/D11','This specifies the birational map without asserting a uniqueness\ntheorem for arbitrary non-toroidal fillings.','This specifies the birational map.','The two stated toroidal models, marked isomorphism off the corner and explicit birational modification remain. Remove the unrelated uniqueness disclaimer.')
add(157,'D02',r'''\item For completeness the normalization description is an
explicit chart prescription.''',r'''\item The normalization charts are as follows.''','Retain the complete star-chart, stabilizer, bundle-unit and intersection prescription.')
add(169,'D02/D08','Thus\nthere is no elliptic quotient hidden in those centres.\n','','The preceding trivial-stabilizer proof and following normalization isomorphism supply the exact toric identification. Remove the process epithet/contrast only.')
add(169,'D02',r'''For clarity, this statement requires no K\"ahler
hypothesis. ''','', 'The stated arbitrary smooth complex centers and the full integral Thom/Gysin/Borel–Moore construction remain. Remove the prefatory negative comparison.')
add(148,'D18',r'''The intersection computations in
\cite[Lemma 2.1]{Engel2026} give''',r'''The intersection computations in
\cite[Lemma~2.1, pp.~3--4]{Engel2026} give''','Primary Lemma2.1 statement and height/intersection proof actually viewed on printed pp3–4. Locator addition only.')
d['source_base_sha256']=hashlib.sha256(s.encode()).hexdigest();d['scope']='Actual candidate11 page findings. All wording-affected complete current proofs were read in rendered pages; complete original proof comparison recorded in the companion archive. Citation-only changes have exact primary receipts. No source mutation and no new CHECK_EVENTS for visual/prose QA.'
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
a=json.loads((O/'S6_SERIES_PUBLISH_I_visual_prose_archive.json').read_text());
for lab,b in a['blocks'].items():
 new=b['current'];applied=[]
 for g in d['guards']:
  if g['old'] in new:new=new.replace(g['old'],g['new']);applied.append(g['id'])
 b['replacement']=new;b['guards']=applied;b['original_sha256']=hashlib.sha256(b['original'].encode()).hexdigest();b['current_sha256']=hashlib.sha256(b['current'].encode()).hexdigest();b['replacement_sha256']=hashlib.sha256(new.encode()).hexdigest()
a['method']='Complete current proofs actually read in candidate11 rendered pages. Complete original proofs read in this close-out except inv:C3.8, whose current and original blocks are byte-identical to its previous fully read final-residual comparison; that full reading is reused honestly. Exact proposed phrase replacements then compared in context. Page QA and prose cleanup only; no fresh mathematical event or independent claim.'
a['atlas_reuse_receipt']='S6_SERIES_PUBLISH_I_final_residual_archive.json, inv:C3.8: original block and proposed_after both exactly equal this archive original/current; earlier full exposure/read is in that record.'
a['withdrawn_false_positives']=[{'page':118,'claim':'Mistook italic t for pronoun it','resolution':'Enlarged actual image correctly reads t; no defect/guard/event.'},{'page':155,'claim':'Initially missed n in k+nℓ','resolution':'Enlarged actual image and complete original/current source correctly contain n; no defect/refinement/refutation/event.'}]
(O/'S6_SERIES_PUBLISH_I_visual_prose_archive.json').write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')
preview=s
for g in d['guards']:preview=preview.replace(g['old'],g['new'],1)
for pat in [r'\\label\{([^}]+)\}',r'\\hypertarget\{(tag-[^}]+)\}']:
 from collections import Counter
 assert Counter(re.findall(pat,s))==Counter(re.findall(pat,preview))
(O/'S6_SERIES_PUBLISH_I_visual_prose_preview.tex').write_text(preview)
print({'guards':len(d['guards']),'wording_proof_blocks':len(a['blocks']),'source_sha256':d['source_base_sha256'],'labels_tags':'exactly preserved'})
