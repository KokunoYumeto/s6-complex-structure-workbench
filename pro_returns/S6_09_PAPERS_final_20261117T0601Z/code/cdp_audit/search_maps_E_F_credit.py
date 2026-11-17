"""Actual result-specific bounded comparisons for 22 E and 33 root-owned F rows.

The log preserves commands, hashes and every match. It is a search record,
not an assertion of mathematical priority or exhaustive worldwide absence.
"""
import hashlib,json,re,subprocess
from pathlib import Path
ROOT=Path('/workspace/scratch/037cd144174c')
OUT=ROOT/'deliverables/work/cdp_audit/maps_credit';OUT.mkdir(parents=True,exist_ok=True)
SOURCES={
 'AC26':'sources/external/root/AC26_pdf_text.txt',
 'E26':'sources/papers/arXiv_2609.38442_Engel_src/S6.tex',
 'DGKX_v1':'sources/papers/arXiv_2610.00250v1_Du_Guo_Kusakabe_Xie_src/v5oka_maps_modifications_deformations.tex',
 'DGKX_v2':'sources/papers/arXiv_2610.00250v2_Du_Guo_Kusakabe_Xie_src/submited-tams.tex'}
Q={
 'E.1.4':['fourfold','Weierstrass','Betti','elliptic.*product'],
 'E.2.1':['fourfold','algebraic.dimension','signature','Weierstrass'],
 'E.2.2':['transverse.fibre.product','transverse.fiber.product','K.nneth'],
 'E.2.3':['shifted','central.extension','Seifert','fivefold'],
 'E.2.4':['2432','76.handle','ordinary.handle','framed.plumbing'],
 'E.2.5':['shifted','parabolic.cohomology','Smith','torsion'],
 'E.2.6':['shifted','Mayer..Vietoris','linking','torsion'],
 'E.2.7':['shifted','stably.parallel','stable.tangent','transverse'],
 'E.2.8':['framed.bordism','null.homotop','transversality','disc.extension'],
 'E.2.9':['framed.bordism','classifying.map','stable.stem','aspherical'],
 'E.2.10':['spun','spinning','peripheral','zero.linking','torus.knot'],
 'E.2.11':['coinvariant','second.homotopy','projective.module','group.ring'],
 'E.2.12':['Alexander','locali[sz]ation','group.ring','universal.cover'],
 'E.2.13':['circle.fib','mapping.torus','return.map','Euler.number'],
 'E.2.14':['splice','return.map','Jordan','twelve.fold'],
 'E.2.15':['Smith','Hermite','Wang','72','cyclic.cover'],
 'E.2.16':['group.ring','Fox','peripheral','Alexander','cyclic.sign'],
 'E.2.17':['splice','amalgam','second.homotopy','group.ring'],
 'E.2.18':['Whitehead','quadratic','connected.sum','S.2.*S.4'],
 'E.2.19':['plumbing','framing','smooth.*cusp','normal.bundle','triple'],
 'E.2.20':['framed.plumbing','normal.disc','normal.disk','meridian','finite.cap'],
 'E.2.21':['ordinary.handle','round.handle','characteristic.embedding','2432','76'],
 'F.2.2':['cyclotomic','finite.order','GL.?6','38','19'],
 'F.2.3':['peripheral','blow.up','homology','filling'],
 'F.2.4':['canonical.representative','integral.conjugacy','unbounded','Kuhn'],
 'F.2.7':['orbifold','triangle.group','multiple.fib','three.finite'],
 'F.2.8':['involut','order.pair','three.connected','rank.six'],
 'F.2.9':['rank.five','coinvariant','fixed.rank','irreducib'],
 'F.2.10':['symplectic','Sp.?4','SO.?5','square.zero','order.pair'],
 'F.2.11':['rational.extension','parabolic.cohomology','rank.five','Jordan'],
 'F.2.12':['five.*twelve','three.adic','square.zero','Tor'],
 'F.2.13':['companion','exterior.square','three.adic','rational.family'],
 'F.2.14':['spectral.pair','cyclotomic','rank.five','order.five'],
 'F.2.15':['complex.structure','finite.action','coprime','spectral'],
 'F.2.16':['unbounded','trace.family','non.self.dual','rank.six'],
 'F.2.17':[r'v\^2.v.1','odd.torsion','three.connected','coinvariant'],
 'F.2.18':['quaternion','HP','non.self.dual','eight.manifold'],
 'F.2.19':['residual','semisimpl','stable.lattice','three.connected'],
 'F.2.20':['rational.normal.form','rank.five','exceptional.line','projective.parameter'],
 'F.2.21':['good.prime','homothety','stable.lattice','absolutely.irreducib'],
 'F.2.22':['lattice.algorithm','conductor','trace.dual','Jordan..Zassenhaus'],
 'F.2.23':['stable.lattice','homothety','rank.six','integral.conjugacy'],
 'F.2.24':['affine.twist','unbounded','logarithmic','three.connected'],
 'F.2.25':['suspension','cyclotomic','multiplicit','three.connected'],
 'F.2.26':['rational.normal.form','exceptional.line','irreducib','rank.five'],
 'F.2.27':['three.primary','order.six','three.connected','pairing'],
 'F.2.28':['fundamental.group','affine.twist','coinvariant','clutch'],
 'F.2.29':['survivor','parabolic.cohomology','Smith','suspension'],
 'F.2.30':['constructive.classification','survivor','quaternion','bounded.cusp'],
 'F.2.31':['orbifold','van.Kampen','affine.power','spherical','clutch'],
 'F.2.32':['Seifert','logarithmic','three.multiple','three.finite','20r'],
 'F.2.36':['simultaneous.*conjugacy','principal.ideal','Bley','Hofmann','Johnston'],
 'F.3.1':['self.dual','parity','Kuhn','eight.manifold'],
 'F.3.2':['rank.pattern','fixed.rank','non.self.dual','fourfold'],
 'F.3.3':['LSAP','period.domain','bounded.cusp','good.reduction','Oka']}
blocks=json.loads((ROOT/'deliverables/work/maps_audit/source_blocks.json').read_text())
meta={'model':'GPT-6 Astra (OpenAI, ChatGPT Pro mode)','effort':'Pro','date':'2026-11-17','timezone':'UTC','reader':'/root/cdp_audit'}
records=[];plan=[];citations=[];union={k:{} for k in SOURCES}
for sid,terms in Q.items():
    bs=blocks[sid]
    text='\n'.join(b['text'] for b in bs)
    locs=[{'source':b['file'],'lines':[b['start_line'],b['end_line']], 'block_sha256':hashlib.sha256(b['text'].encode()).hexdigest()} for b in bs]
    start=text.find('\\begin{proof}')
    statement=text[:start] if start>=0 else text
    plan.append({'source_id':sid,'source_blocks':locs,'statement':statement,'queries':terms})
    for m in re.finditer(r'\\cite(?:\[[^\]]*\])*\{([^}]*)\}',text):
        citations.append({'source_id':sid,'keys':m.group(1).split(','),'context':text[max(0,m.start()-250):min(len(text),m.end()+250)],'source_blocks':locs})
    for baseline,rel in SOURCES.items():
        p=ROOT/rel
        cmd=['rg','-n','-i','--no-heading']+sum((['-e',q] for q in terms),[])+[str(p)]
        r=subprocess.run(cmd,capture_output=True,text=True)
        assert r.returncode in (0,1),r.stderr
        matches=[]
        for line in r.stdout.split('\n'):
            if not line: continue
            n,_,content=line.partition(':');matches.append({'line':int(n),'text':content});union[baseline][int(n)]=content
        records.append({'source_run':'S6_04_MAPS_MANIFOLDS','source_id':sid,'baseline':baseline,'source':rel,'source_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'command':['rg','-n','-i','--no-heading']+sum((['-e',q] for q in terms),[])+[rel],'exit_code':r.returncode,'terms_searched':terms,'matches':matches,'receiving_sources':locs,'reader':meta,'scope':'The complete named file was searched with these exact patterns. Match context and mathematical credit are assessed separately; a negative match is not a worldwide novelty conclusion.'})
(OUT/'search_plan_55.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2)+'\n')
(OUT/'searches_55.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
(OUT/'receiving_citation_contexts.json').write_text(json.dumps(citations,ensure_ascii=False,indent=2)+'\n')
for baseline,lines in union.items():
    (OUT/f'{baseline}_matched_lines.txt').write_text('\n'.join(f'{n}: {t}' for n,t in sorted(lines.items()))+'\n')
print('Executed',len(records),'whole-source result/baseline searches for',len(Q),'distinct results.')
print('Unique matched-line counts:',{k:len(v) for k,v in union.items()})
print('Cited F originals:',sorted({key for c in citations if c['source_id'].startswith('F.') for key in c['keys']}))
