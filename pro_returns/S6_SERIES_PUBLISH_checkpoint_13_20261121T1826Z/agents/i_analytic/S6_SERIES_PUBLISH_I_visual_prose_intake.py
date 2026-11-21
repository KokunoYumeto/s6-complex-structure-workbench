from pathlib import Path
import re,json,hashlib
R=Path('/workspace/scratch/653608133b22');s=(R/'work/S6_SERIES_PUBLISH_I.tex').read_text();o=(R/'source/S6_SERIES_GRIND_I.tex').read_text()
keys=['For completeness, every derivative','Then their multiplicity pairs agree','These statements concern the canonical map','No choice of','No statement of convergence','there is no replacement of the translation','For completeness, the relation','Here $A_j$ denotes a scalar','without asserting a uniqueness','For completeness the normalization','no elliptic quotient hidden','this statement requires no K']
def get(t,k):
 hits=list(re.finditer(r'\\begin\{(proposition|theorem|lemma|corollary|remark)\}',t[:k]));a=hits[-1].start();b=t.index('\\end{proof}',k)+len('\\end{proof}');tx=t[a:b];ls=re.findall(r'\\label\{([^}]+)\}',tx);return {'label':ls[0], 'text':tx,'start':a,'end':b}
blocks={};items=[]
for key in keys:
 hits=[m.start() for m in re.finditer(re.escape(key),s)]
 if key=='No choice of':hits=[x for x in hits if 'fibrewise' in s[x:x+90]]
 assert len(hits)==1,(key,hits)
 b=get(s,hits[0]);lab=b['label'];ok=o.index('\\label{'+lab+'}');ob=get(o,ok)
 if lab not in blocks:blocks[lab]={'original':ob['text'],'current':b['text']}
 items.append({'key':key,'label':lab})
O=R/'work/agents/i_analytic';(O/'S6_SERIES_PUBLISH_I_visual_prose_archive.json').write_text(json.dumps({'source_sha256':hashlib.sha256(s.encode()).hexdigest(),'original_sha256':hashlib.sha256(o.encode()).hexdigest(),'blocks':blocks,'items':items},ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'items':items,'block_sizes':{k:{'old':len(v['original']),'current':len(v['current'])} for k,v in blocks.items()}},indent=2))
