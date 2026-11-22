"""Extract cited construction definitions, excluding all six boundary target proofs."""
from pathlib import Path
import hashlib,json,datetime
R=Path(__file__).resolve().parents[1]
sources={p:(R/p).read_text() for p in ['S6_SERIES_PUBLISH_I.tex','S6_SERIES_PUBLISH_II.tex']}
items=[]
def take(p,title,start,end,include_end=True,scope='Construction definition or coordinate formula only.'):
    s=sources[p];assert s.count(start)==1,(title,'start')
    a=s.index(start);z=s.index(end,a)+(len(end) if include_end else 0)
    t=s[a:z]
    items.append(dict(title=title,source_path=p,source_sha256=hashlib.sha256((R/p).read_bytes()).hexdigest(),
       char_start=a,char_end=z,byte_start=len(s[:a].encode()),byte_end=len(s[:z].encode()),
       line_start=s[:a].count('\n')+1,line_end=s[:z].count('\n')+1,
       fragment=t,fragment_sha256=hashlib.sha256(t.encode()).hexdigest(),scope=scope))
I='S6_SERIES_PUBLISH_I.tex';II='S6_SERIES_PUBLISH_II.tex'
take(I,'Base, meridian orientation, integral marking and finite matrices',
 r'\begin{definition}[Base and integral marking]',r'\end{definition}')
take(I,'Finite affine vectors and untwisted cusp convention',
 r'\begin{definition}[The parameter and the finite translations]',r'\end{definition}')
take(I,'Finite root action in the holomorphic and real markings',
 'At a finite root chart the family action is',
 r'In the real marking it is $(z,c,u)\mapsto(g_jz,c,A_ju+v_j/m_j)$.',
 scope='Literal construction formula in the cited Paper I family proof, ending before its freeness argument. No Paper II target argument.')
take(I,'Punctured connector translation',
 'Their punctured connectors are\n\\begin{equation}',
 '\\label{pub:I:eq:PD8}\n\\end{equation}',
 scope='Literal connector definition in the cited Paper I construction, ending before its intertwining argument. No target slant, Chern-class or boundary calculation.')
take(I,'Cusp affine coordinates',
 r'$q=z_0z_1z_2$, $x_1=z_1$, $x_2=z_2$',
 r'$q=z_0z_1z_2$, $x_1=z_1$, $x_2=z_2$',
 scope='Coordinate identification only from the cited Paper I statement; the rest of that statement and proof is excluded.')
take(I,'Cusp ray indexing',
 'The toric covering has rays',r'for all $v\in\mathbb Z^2$.',
 scope='Literal fan definition only in a cited Paper I proof; all ensuing fundamental-group argument is excluded.')
take(II,'Cusp setup before the local Picard proposition',
 'Retain the cusp notation of\n',
 r'\begin{proposition}[an explicit nonzero local cusp restriction]',False,
 scope='The complete non-proof setup immediately preceding 03IN: W.61–W.64, Phi/Psi action, divisor indexing and character convention. The target statement and proof are excluded.')
blocked=['03IM','03IC','03IE','03ID','03IL','03IN']
for x in items:
    assert not any(('\\hypertarget{tag-'+tag+'}') in x['fragment'] for tag in blocked)
    if x['source_path']==II:
        s=sources[II][:x['char_start']]
        assert s.count(r'\begin{proof}')==s.count(r'\end{proof}')
        assert r'\begin{proof}' not in x['fragment'] and r'\end{proof}' not in x['fragment']
p=R/'agents/ii_checks_provenance/recovery_20261121T2000Z/S6_SERIES_PUBLISH_II_boundary_construction_inputs.json'
assert not p.exists()
d=dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
 purpose='Exact cited construction data for IM/IC/IE/ID/IL/IN independent prerelease derivations.',
 scope='No target proof, boundary sweep construction, cohomology slant evaluation or local Picard factor calculation is supplied. Some raw definitions occur inside cited Paper I construction proofs; their exact fragment extent is recorded.',
 target_proofs_excluded=blocked,fragments=items)
p.write_text(json.dumps(d,indent=2)+'\n')
print(json.dumps(dict(path=str(p.relative_to(R)),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),fragments=len(items))))
