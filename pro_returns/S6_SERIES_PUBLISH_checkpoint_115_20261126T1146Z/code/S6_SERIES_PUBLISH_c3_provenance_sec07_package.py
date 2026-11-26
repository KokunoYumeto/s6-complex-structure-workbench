from pathlib import Path
from collections import Counter
from datetime import datetime, timezone
import csv, re, hashlib, bisect

ROOT=Path('/workspace/scratch/9fcd229a9ed4/base/S6_SERIES_PUBLISH_checkpoint_35')
OUT=ROOT/'agents/continuation3_provenance/sec07_tail'
REL='agents/continuation3_provenance/sec07_tail'
stamp=datetime.now(timezone.utc).isoformat()
main=(ROOT/'S6_SERIES_PUBLISH_II.tex').read_text()

def read(key, suffix='proposed'):
    return (OUT/f'S6_SERIES_PUBLISH_{key}_{suffix}.tex').read_text()
def shared(key):
    return (OUT/f'S6_SERIES_PUBLISH_{key}.tex').read_text()
def tsv(name,rows,fields=None):
    with (OUT/name).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields or list(rows[0]),delimiter='\t',lineterminator='\n')
        w.writeheader();w.writerows(rows)
def loadtsv(name):
    with (OUT/name).open() as f:return list(csv.DictReader(f,delimiter='\t'))

groups=[
 ('subsec:II:reduced-horizontal-boundaries','Reduced horizontal boundaries',['IRR_1']),
 ('subsec:II:rational-boundary-attachments','Rational boundaries and attachment maps',['P360','RAT_1','RAT_3','RAT_2_4','RAT_5']),
 ('subsec:II:normal-cubic-covers','Normal cubics, cyclic covers and rational images',['P361','P362','RAT_6','D4_1','D4_2','RAT_7','RAT_8','RAT_9','D4_3']),
 ('subsec:II:irreducible-sign-criteria','Irreducible fibres and zero Euler number',['UN_7','UN_12','MH_4']),
 ('subsec:II:elliptic-interface-signs','Elliptic interfaces and reducible fibres',['INT_1','INT_2','INT_3'])
]
pieces=[]; receiving={}
for label,title,keys in groups:
    pieces.append(r'\subsection{'+title+r'}\label{'+label+'}\n\n')
    for key in keys:
        s=shared(key) if key.startswith('P36') else read(key,'original' if key=='RAT_6' else 'proposed')
        # Exact cited block remains byte-for-byte; join boundaries add only inter-block whitespace.
        receiving[key]=s
        pieces.append(s+'\n\n')
new_tail=''.join(pieces)
old_tail=(OUT/'S6_SERIES_PUBLISH_reduced_horizontal_body_original.tex').read_text()
(OUT/'S6_SERIES_PUBLISH_reduced_horizontal_proposed.tex').write_text(new_tail)
guards=[dict(change_id='II-C3-SEC07-TAIL',old_text=old_tail,new_text=new_tail)]
guards+=loadtsv('S6_SERIES_PUBLISH_A5_16_scope_guard.tsv')
guards+=loadtsv('S6_SERIES_PUBLISH_sec07_earlier_owner_guards.tsv')

bm_start=main.index(r'\bibitem[Br{\^i}nz{\u a}nescu and Moraru(2005)]{BrinzanescuMoraru2005}')
bm_stop=main.index(r'\bibitem',bm_start+9)
bm_old=main[bm_start:bm_stop]
bm_new=bm_old.replace('https://arxiv.org/pdf/math/0306191','https://aif.centre-mersenne.org/item/AIF_2005__55_5_1659_0.pdf')
assert bm_old!=bm_new
guards.append(dict(change_id='II-C3-SEC07-BM-PUBLISHED-LOCATOR',old_text=bm_old,new_text=bm_new))
program_old=next(l for l in main.splitlines(True) if 'Symbolic-square and symbolic-cube saturations' in l and 'A_low_delta_cusp.py' in l)
program_new=program_old.replace(r'\cref{cdp:st:A.5.19}',r'\cref{cdp:st:A.5.18,cdp:st:A.5.19,cdp:st:C.2.RAT.1}')
guards.append(dict(change_id='II-C3-SEC07-PROGRAM-SCOPE',old_text=program_old,new_text=program_new))
tsv('S6_SERIES_PUBLISH_sec07_guards.tsv',guards)

virtual=main
for g in guards:
    assert virtual.count(g['old_text'])==1,(g['change_id'],virtual.count(g['old_text']))
    virtual=virtual.replace(g['old_text'],g['new_text'],1)
old_join=''.join(g['old_text'] for g in guards)
new_join=''.join(g['new_text'] for g in guards)
for pattern in (r'\\label\{([^}]+)\}',r'\\hypertarget\{([^}]+)\}'):
    a=Counter(re.findall(pattern,old_join));b=Counter(re.findall(pattern,new_join))
    bad={k:(v,b[k]) for k,v in a.items() if b[k]!=v}
    assert not bad,(pattern,bad)
for n in ('P360','P361','P362'):
    assert main.count(r'\hypertarget{tag-'+n+'}')==0
    assert virtual.count(r'\hypertarget{tag-'+n+'}')==1
assert receiving['RAT_6']==read('RAT_6','original')
assert r'\part{' not in new_tail
assert not re.search(r'\\tag\{',new_tail)
for m in re.finditer(r'\\begin\{(equation\*?|align\*?|gather\*?|multline\*?)\}(.*?)\\end\{\1\}',new_join,re.S):
    assert not re.search(r'\n[ \t]*\n',m.group(2)),m.group(0)[:150]
    assert m.group(2).count(r'\SsixEquationAliases{')<=1,m.group(0)[:150]
for body in re.findall(r'\\SsixEquationAliases\{((?:\\label\{[^}]+\})*)\}',new_join):
    assert r'\hypertarget' not in body

owner_env=r'\\begin\{(?:proposition|lemma|corollary|theorem|cited|definition|remark|example)\}'
starts=[m.start() for m in re.finditer(owner_env,virtual)]
labels={}
for m in re.finditer(r'\\label\{([^}]+)\}',virtual):
    labels.setdefault(m.group(1),[]).append(m.start())
new_tail_start=virtual.index(new_tail)
forward=[];unresolved=[]
for m in re.finditer(r'\\(?:cref|Cref|eqref|ref|SeriesRef)\{([^}]+)\}',new_tail):
    pos=new_tail_start+m.start()
    oi=bisect.bisect_right(starts,pos)-1
    oi_start=starts[oi];oi_stop=starts[oi+1] if oi+1<len(starts) else len(virtual)
    for label in m.group(1).split(','):
        label=label.strip()
        dest=labels.get(label,[])
        if not dest:
            unresolved.append(label);continue
        if min(dest)>=oi_stop:
            forward.append((label,virtual.count('\n',new_tail_start,pos)+1,virtual.count('\n',0,min(dest))+1))
assert not unresolved,sorted(set(unresolved))
assert not forward,forward

earlier=['A5_16','P228','A5_18','P232','P4_13','NC_1']
for key in earlier:receiving[key]=read(key)
old_keys=['IRR_1','RAT_1','RAT_2','RAT_3','RAT_4','RAT_5','RAT_6','RAT_7','RAT_8','RAT_9','D4_1','D4_2','D4_3','UN_7','UN_12','INT_1','INT_2','INT_3','MH_4']
original={key:read(key,'original') for key in old_keys}

move_maps={
 'P228':'The two original embedded ideals occur as the two rows of A.T.14; the ambient coordinate lift and inverse-function map identify the identical convergent curve rings. RA.7 is the cusp-plus-line row; RA.8 is the (3,4,5) row.',
 'A5_18':'The identical g1,g2,g3,F (respectively G,z) identities and normalized conormal frame are retained at A.T.15/A.T.16 and the three annihilating-product display. Only the rank-one Hessian calculation transfers to the A2 receiver; its nonzero radical cubic and pole inequalities remain proved in RAT1.',
 'P232':'The old blowup identity is the specialization (Z1,Z2,D1,D2,m,a)=(W,Wprime,DW,sigma_*DW,d,a). The numerical-zero clause gives a=d-1 and the same downstairs class. CIR4 is an alias of the complete Jacobian identity.',
 'P4_13':'The exact substitution is f|U, central irreducible full mS, minimum m0=m and cohomology monodromy T=T1. The inherited integer H1 action A is related by T=A^T, and determinant/transposed exterior-trace identities preserve UI8.',
 'NC_1':'The same local equation g=product z_i^{a_i}, angular coordinates u_i=z_i/|z_i|, and argument theta give the same angular fibre, including full multiplicities and branch permutations.',
 'P360':'The same proper f,mS,eta,pi,D and G satisfy torsion omega and chiO=0 by P281. A5.16 supplies the entire conductor/complement block. UI13 is the kernel map induced by the same h|D in the P294 double mapping cylinder.',
 'P361':'The same H,N,M,P and full function f=u*s0^m give s^{-3m}f(tau(sv))->P(v)^m. The right-inverse flow and its reverse identify compact neighbourhoods with the nearby full fibre and preserve the complex orientation and compact pairing.',
 'P362':'The complete receiving formula uses the same cyclic cover, inverse evaluation w(v)=1, actual boundary components and projective resolution. Product cases specialize N=O(-1)^2,L=O(1,1). The individual parameter substitutions and weighted-contact generator maps are recorded in the full comparison.'
}
equations=[]
def display(s,label):
    p=s.index(r'\label{'+label+'}')
    candidates=[(s.rfind(x,0,p),x) for x in (r'\begin{equation}',r'\begin{align}',r'\begin{gather}')]
    candidates += [(m.start(),r'\[') for m in re.finditer(r'(?<!\\)\\\[',s[:p])]
    begin,token=max(candidates)
    endtoken={r'\begin{equation}':r'\end{equation}',r'\[':r'\]',r'\begin{align}':r'\end{align}',r'\begin{gather}':r'\end{gather}'}[token]
    try:end=s.index(endtoken,p)+len(endtoken)
    except ValueError:raise ValueError((label,token,s[max(0,p-200):p+200]))
    return s[begin:end]
for key,s in original.items():
    for label in re.findall(r'\\label\{([^}]+)\}',s):
        if not label.startswith('cdp:eq:'):continue
        destinations=[k for k,v in receiving.items() if r'\label{'+label+'}' in v]
        assert len(destinations)==1,(key,label,destinations)
        dest=destinations[0]
        equations.append(dict(label=label,old_owner=key,receiving_owner=dest,old_formula=display(s,label),new_formula=display(receiving[dest],label),comparison=move_maps.get(dest,'Same full statement/proof owner, with the explicit local parameter, cover or Euler calculation retained. Manual numbering is replaced by the current equation environment; the permanent target and mathematical conclusion remain.'),status='complete source comparison; integrated numbering pending'))
tsv('S6_SERIES_PUBLISH_sec07_equation_map.tsv',equations)
print('READY CONTENT CHECK: nine unique guards; all original labels/targets preserved; RAT6 unchanged; no manual display tags, blank equation paragraphs, repeated alias calls, unresolved tail targets or later-owner tail dependencies. No main/shared writes.')
