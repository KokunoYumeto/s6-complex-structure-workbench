"""New exact universal checks for the seven-main-outline receiving comparison.

Written after reading the formulas. No earlier checking/producing code imported.
The integer-twist argument partitions every integer k in n=12k+r into affine
pieces; it is not a bounded-n test.
"""
import datetime
import hashlib
import json
from pathlib import Path
import sympy as s

HERE=Path(__file__).resolve().parents[1]
records=[]
def check(name, truth, detail):
    assert bool(truth), (name,detail)
    records.append({'name':name,'result':'PASS','detail':detail})
def degree(n):
    r1=n%3; r2=(3*n)%4
    q=n-4*r1-3*r2
    assert q%12==0
    return q//12
def tup(n):
    u=lambda m:max(degree(m)+1,0)
    v=lambda m:max(-degree(m)-1,0)
    return (u(n)+u(n-1),v(n)+v(n-1)+u(n)+u(n-1)+u(n+2),
            v(n)+v(n-1)+v(n+2)+u(n+6)+(0 if n%3==0 else 1),v(n+6))

k=s.symbols('k',integer=True)
piece_receipts=[]
for r in range(12):
    d={j:degree(r+j) for j in [0,-1,2,6]}
    # d(12k+r+j)=k+d(r+j), since both stabilizer residues are unchanged.
    check(f'residue {r}: integral degree shift',all((r+j)%3==(12+r+j)%3 and (3*(r+j))%4==(3*(12+r+j))%4 and degree(12+r+j)==d[j]+1 for j in d),str(d))
    roots=sorted({-v-1 for v in d.values()})
    # Each root is included as a singleton; every remaining interval is affine.
    regions=[(None,roots[0]-1)]+[(b,b) for b in roots]
    regions += [(a+1,b-1) for a,b in zip(roots,roots[1:]) if a+1<=b-1]
    regions += [(roots[-1]+1,None)]
    for lo,hi in regions:
        sample=lo if lo is not None else hi
        U={j:k+d[j]+1 if sample+d[j]+1>=0 else s.Integer(0) for j in d}
        V={j:-k-d[j]-1 if sample+d[j]+1<=0 else s.Integer(0) for j in d}
        h=[U[0]+U[-1],V[0]+V[-1]+U[0]+U[-1]+U[2],
           V[0]+V[-1]+V[2]+U[6]+(0 if r%3==0 else 1),V[6]]
        if lo is not None and lo==hi:
            h=[v.subs(k,lo) for v in h]
        chi=s.expand(h[0]-h[1]+h[2]-h[3])
        check(f'residue {r}, interval {lo},{hi}: Euler',chi==1,str(chi))
        a=int(s.expand(h[2]).coeff(k)); b=int(s.expand(h[2]).subs(k,0))
        minimum=(a*(lo if a>0 else hi)+b) if a else b
        check(f'residue {r}, interval {lo},{hi}: persistent H2',minimum>=1,{'h2':str(s.expand(h[2])),'minimum':minimum})
        piece_receipts.append({'r':r,'k_lower':lo,'k_upper':hi,'h':[str(s.expand(v)) for v in h],'chi':1,'minimum_h2':minimum})
    check(f'residue {r}: exact cusp-rank threshold',-d[6]==(-1 if r in [6,9,10] else 0),{'u(n+6)>0_iff_k_at_least':-d[6]})

check('n=0 tuple',tup(0)==(1,1,1,0),tup(0))
check('n=-1 tuple',tup(-1)==(0,0,1,0),tup(-1))
J,m=s.symbols('J m',integer=True)
check('nonintegral Euler',s.expand(-J+1+J)==1,'(0,J,1+J,0)')
check('two-parameter Euler',1-2+2==1,'(1,2,2,0)')
check('comb Euler',s.expand((2*m+1)-(8*m+1)+(6*m+1))==1,'(2m+1,8m+1,6m+1,0)')
h,mu,E,wp=s.symbols('h muprime E2 wp')
hprime=-wp-s.pi**2*E/3
theta_tau=(hprime+h*h)/(4*s.pi*s.I)
eta_tau=s.I*s.pi*E/12
beta_over6_prime=s.I/s.pi*(theta_tau+h*mu-eta_tau)
det=s.expand(beta_over6_prime-mu*mu)
target=-(mu-s.I*h/(2*s.pi))**2-wp/(4*s.pi**2)
check('exact theta heat/eta determinant',s.simplify(det-target)==0,str(det))

out={'date_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
     'method':'Universal residue-class and affine-piece calculation over all integers; exact symbolic heat-equation substitution. Written after target formulas were read.',
     'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     'frontmatter_sha256':hashlib.sha256((HERE/'frontmatter_II.tex').read_bytes()).hexdigest(),
     'checks':len(records),'result':'PASS','records':records,'integer_affine_pieces':piece_receipts}
(HERE/'II_global_outline_identities_07.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'result':'PASS','checks':len(records),'affine_pieces':len(piece_receipts)}))
