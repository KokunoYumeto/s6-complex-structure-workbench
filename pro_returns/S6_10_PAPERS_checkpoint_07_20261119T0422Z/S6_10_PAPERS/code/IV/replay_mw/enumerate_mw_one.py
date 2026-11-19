"""Exact MW=Z enumeration, with branched-cover existence certificates.

Input transcribed and visually checked from Oguiso--Shioda (1991),
Main Theorem, printed pp.85--86 (all rank-one rows, 43--61).
Kodaira invariants and existence reduction: Miranda (1990),
Table 1.1, eq.1.11, Proposition 3.4 and Corollary 3.5.
No previously asserted configuration count is used as an input.
"""
from itertools import product, combinations
from fractions import Fraction
from pathlib import Path
import json
import sympy as S

# number, root summands, order of torsion, height of free generator
rows = [
 (43, ('E7',), 1, '1/2'),
 (44, ('A7',), 2, '1/2'),
 (45, ('A7',), 1, '1/8'),
 (46, ('D7',), 1, '1/4'),
 (47, ('A6','A1'), 1, '1/14'),
 (48, ('D6','A1'), 2, '1/2'),
 (49, ('E6','A1'), 1, '1/6'),
 (50, ('D5','A2'), 1, '1/12'),
 (51, ('A5','A2'), 3, '1/2'),
 (52, ('D5','A1','A1'), 2, '1/4'),
 (53, ('A5','A1','A1'), 2, '1/6'),
 (54, ('D4','A3'), 2, '1/4'),
 (55, ('A4','A3'), 1, '1/20'),
 (56, ('A4','A2','A1'), 1, '1/30'),
 (57, ('D4','A1','A1','A1'), 4, '1/2'),
 (58, ('A3','A3','A1'), 4, '1/2'),
 (59, ('A3','A2','A1','A1'), 2, '1/12'),
 (60, ('A3','A1','A1','A1','A1'), 4, '1/4'),
 (61, ('A2','A2','A2','A1'), 3, '1/6'),
]
options = {
 'E7': ('III*',), 'E6': ('IV*',),
 'D7': ('I3*',), 'D5': ('I1*',),
 'A7': ('I8',), 'A6': ('I7',), 'A4': ('I5',),
 'A3': ('I4',), 'A2': ('I3','IV'), 'A1': ('I2','III'),
}
euler = {'III*':9,'IV*':8,'I3*':9,'I1*':7,
         'I8':8,'I7':7,'I5':5,'I4':4,'I3':3,'IV':4,
         'I2':2,'III':3,'II':2,'I1':1}

def compose(p,q):
    """p after q, permutations as 0-based image tuples."""
    return tuple(p[q[i]] for i in range(len(p)))

def inverse(p):
    q=[0]*len(p)
    for i,j in enumerate(p):q[j]=i
    return tuple(q)

def cyc(p):
    seen=set();out=[]
    for i in range(len(p)):
        if i in seen:continue
        a=[];j=i
        while j not in seen:
            seen.add(j);a.append(j+1);j=p[j]
        out.append(tuple(a))
    return out

def typ(p):return sorted(len(c) for c in cyc(p))

def canonical(parts):
    p=[];start=0
    for n in parts:
        p.extend(list(range(start+1,start+n))+[start]);start+=n
    return tuple(p)

def involutions(n,fixed):
    """All involutions with precisely fixed fixed points, no omission."""
    p=list(range(n))
    def rec(left,f):
        if not left:
            if f==0:yield tuple(p)
            return
        a,*tail=left
        if f:
            p[a]=a
            yield from rec(tail,f-1)
        if len(left)>f:
            for j,b in enumerate(tail):
                p[a]=b;p[b]=a
                yield from rec(tail[:j]+tail[j+1:],f)
                p[b]=b
            p[a]=a
    yield from rec(list(range(n)),fixed)

def transitive(gens):
    seen={0};todo=[0]
    while todo:
        i=todo.pop()
        for p in gens:
            j=p[i]
            if j not in seen:seen.add(j);todo.append(j)
    return len(seen)==len(gens[0])

def profile(fs):
    poles=[]
    for f in fs:
        if f.startswith('I') and f[1:2].isdigit():
            poles.append(int(f[1:].rstrip('*')))
    d=sum(poles)
    one0=fs.count('II')+fs.count('IV*')
    two0=fs.count('IV')
    one1=fs.count('III')+fs.count('III*')
    assert (d-one0-2*two0)%3==0 and (d-one1)%2==0
    p0=[1]*one0+[2]*two0+[3]*((d-one0-2*two0)//3)
    p1=[1]*one1+[2]*((d-one1)//2)
    ram=sum(a-1 for a in p0+p1+poles)
    x=2*d-2-ram
    return d,p0,p1,sorted(poles),x

def certificate(d,p0,p1,poles,x):
    assert x in (0,1)
    a=canonical(p0);identity=tuple(range(d));trials=0
    for b in involutions(d,p1.count(1)):
        ab=compose(a,b)
        swaps=[None] if x==0 else combinations(range(d),2)
        for ij in swaps:
            trials+=1
            t=list(identity)
            if ij is not None:
                i,j=ij;t[i],t[j]=t[j],t[i]
            t=tuple(t)
            c=inverse(compose(ab,t))
            if typ(c)!=poles:continue
            if not transitive((a,b,t,c)):continue
            assert compose(compose(compose(a,b),t),c)==identity
            assert sum(d-len(cyc(p)) for p in (a,b,t,c))==2*d-2
            return dict(sigma0=cyc(a),sigma1=cyc(b),sigma_extra=cyc(t),
                        sigma_infinity=cyc(c),trials=trials)
    raise AssertionError(('No certificate found',d,p0,p1,poles,x))

def main():
    selected=[r for r in rows if r[2]==1]
    print('All rank-one OS91 rows:',len(rows))
    print('Torsion-free entries:',len(selected))
    for row in selected:print(row)
    records=[]
    for no,roots,tor,h in selected:
        for red in product(*(options[r] for r in roots)):
            rem=12-sum(euler[f] for f in red)
            for ii in range(rem//2+1):
                fs=list(red)+['II']*ii+['I1']*(rem-2*ii)
                assert sum(euler[f] for f in fs)==12
                d,p0,p1,poles,x=profile(fs)
                r=dict(OS91=no,roots=roots,height=h,fibres=fs,
                       j_degree=d,over0=p0,over1=p1,poles=poles,
                       extra_ramification=x)
                if x<0:
                    r['status']='excluded by Riemann--Hurwitz'
                else:
                    r['status']='realized by permutation certificate'
                    r['certificate']=certificate(d,p0,p1,poles,x)
                records.append(r)
                print(no,'+'.join(fs),'h='+h,'d='+str(d),'x='+str(x),r['status'])
                if x>=0:print(json.dumps(r['certificate']))
    accepted=[r for r in records if r['extra_ramification']>=0]
    rejected=[r for r in records if r['extra_ramification']<0]
    print('Candidate count:',len(records))
    print('Rejected count:',len(rejected))
    print('Realized fibre configurations:',len(accepted))
    print('By OS row:',{no:sum(r['OS91']==no for r in accepted) for no,*_ in selected})
    out=Path(__file__).with_name('mw_one_configurations.json')
    out.write_text(json.dumps(records,indent=2)+'\n')

    # The A7 root system has two embeddings in E8.  Exhibit torsion-free
    # examples for both accepted configurations, so the order-two row44
    # is not inadvertently substituted for row45.
    t=S.symbols('t')
    for s,b in [(1,1),(3,48)]:
        R=t*t+s;A=R*R+b*t;B=R**3+S.Rational(3,2)*b*t*R+S.Rational(3,8)*b*b
        Delta=S.factor(4*((-3*A)**3)+27*(2*B)**2)
        print('A7 torsion-free model parameters s,b=',s,b)
        print('y^2 = x^3 -3*A*x +2*B; A=',S.expand(A),'B=',S.expand(B))
        print('Delta without conventional -16 factor =',Delta)
        print('gcd(A,B)=',S.factor(S.gcd(A,B)))
        print('gcd(Delta,Delta prime)=',S.factor(S.gcd(Delta,S.diff(Delta,t))))
        print('degDelta=',S.degree(Delta,t),'=> I8 at infinity')
    print('No 2-torsion: after x=X+t^2+s, cubic is '
          'X^3+3(t^2+s)X^2-3btX+3b^2/4.')
    print('A rational root must be polynomial of degree<=2. '
          'Its leading coefficient is0 or-3. '
          'Coefficient comparison forces X=0 or X=-3(t^2+s), '
          'neither a root when b!=0. Thus row45 applies.')

if __name__=='__main__':main()
