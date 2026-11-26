#!/usr/bin/env python3
"""Post-exposure LL auxiliary audit in the literal prescribed fan.

Input is the frozen fresh localization data only. The original linking
numbers are compared as stated claims, not used to derive any vector.
All full bases, inverses and integral exterior bounding chains are saved.
This is version 01; preserve this source/output if a correction is needed.
"""
from pathlib import Path
from hashlib import sha256
from math import gcd
import json
import sympy as S

LANE = Path('agents/continuation7_iii_residual_two_primary')
INPUT = LANE / 'S6_SERIES_PUBLISH_III_02LL_fresh_localization_data.json'
OUTPUT = LANE / 'S6_SERIES_PUBLISH_III_02LL_post_critical_cycles_v01.json'
EXPECTED = 'c0d7c507d1faf05366107d3fb5da98e1c54c2a0ad0ff81e11065ee3607c624cd'
assert sha256(INPUT.read_bytes()).hexdigest() == EXPECTED
data = json.loads(INPUT.read_text())
E = S.eye(4)
DELTA, GAMMA = E[:, 2], E[:, 3]
PAIRS = [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]

def ints(m):
    return [[int(x) for x in row] for row in m.tolist()]

def vector(m):
    return [int(x) for x in m]

def wedge(u,v):
    return S.Matrix([u[i]*v[j]-u[j]*v[i] for i,j in PAIRS])

def bezout(a,b):
    aa,bb = abs(a),abs(b)
    p,q,r,s = 1,0,0,1
    while bb:
        t = aa//bb
        aa,bb,p,q,r,s = bb,aa-t*bb,r,s,p-t*r,q-t*s
    p *= 1 if a >= 0 else -1
    q *= 1 if b >= 0 else -1
    assert p*a+q*b == aa
    return aa,p,q

def outer2(T):
    return S.Matrix.hstack(*(wedge(T[:,i],T[:,j]) for i,j in PAIRS))

def support(p,K):
    x,y = p
    return (K[0,0]*x*(x-1) + 2*K[0,1]*x*y + K[1,1]*y*(y-1))/2

def wall_degree(K,edge,other):
    return S.simplify(sum(support(p,K) for p in other)
                      - sum(support(p,K) for p in edge))

# Three edges of the actual unit antidiagonal triangulation.
walls = [([(0,0),(0,1)],[(1,0),(-1,1)]),
         ([(0,0),(1,0)],[(0,1),(1,-1)]),
         ([(1,0),(0,1)],[(0,0),(1,1)])]
forms = [S.diag(1,0),S.Matrix([[0,1],[1,0]]),S.diag(0,1)]
wall_matrix = S.Matrix([[wall_degree(K,*w) for w in walls] for K in forms])
assert wall_matrix == S.Matrix([[1,0,0],[-1,-1,1],[0,1,0]])
assert abs(wall_matrix.det()) == 1
assert wall_matrix*S.ones(3,1) == S.Matrix([1,-1,1])
old_matrix = S.Matrix([[0,-1,0],[1,1,-1],[-1,0,0]])
swap = S.Matrix([[0,1,0],[1,0,0],[0,0,1]])
assert old_matrix == -wall_matrix*swap

rows=[]
print('INPUT',str(INPUT),EXPECTED)
print('PRESCRIBED_WALL_MATRIX',ints(wall_matrix),'INVERSE',ints(wall_matrix.inv()))
print('OLD_SUPPORT_MATRIX = - prescribed_matrix * swap(first_two_curves)')
for row in data['rows']:
    a,c,z = row['a'],row['c'],row['zero']
    omega = S.Matrix([[a,0,0,0,0,-c]])
    cap_vectors = [None]*5
    local=[]
    for item in row['rank_one']:
        i,n,k = item['index'],item['nu'],item['kappa']
        d = gcd(n,a*k)
        l = S.Matrix(item['l'])
        u = S.Matrix([l[0]*d/n,l[1]*d/n,0,0])
        assert all(v.q == 1 for v in u)
        h,p,q = bezout(int(u[0]),int(u[1]))
        assert h == 1
        r = S.Matrix([-q,p,0,0])
        short = S.Matrix([S.Rational(n,d),S.Rational(-a*k,d)])
        h,p,q = bezout(int(short[0]),int(short[1]))
        assert h == 1
        sigma = -q*u+p*DELTA
        rr = S.Matrix([[d,S.Rational(c*k*d,n)]])
        assert all(v.q == 1 for v in rr)
        h,p,q = bezout(int(rr[0]),int(rr[1]))
        assert h == 1
        beta = p*r+q*GAMMA
        ell = -rr[1]*r+rr[0]*GAMMA
        H = S.Matrix.hstack(l,beta,sigma,ell)
        assert H.det() == 1 and H*H.inv() == E
        T=S.Matrix(row['monodromies'][i])
        expected=S.eye(4); expected[0,1]=1
        assert H.inv()*T*H == expected
        v=wedge(sigma,ell)
        degree=(omega*v)[0]
        assert degree == -S.Rational(c*d*d,n)
        cap_vectors[i]=v
        local.append({'index':i,'kind':'rank_one','nu':n,'kappa':k,
                      'd0':d,'H':ints(H),'H_inverse':ints(H.inv()),
                      'preimage':vector(v),'Omega_degree':int(degree)})
    H=S.Matrix(row['cusp']['H'])
    A1,B1,A2,B2 = [H[:,i] for i in range(4)]
    assert H.det() == 1 and H*H.inv() == E
    T=S.Matrix(row['monodromies'][z])
    expected=S.eye(4); expected[0,1]=1; expected[2,3]=1
    assert H.inv()*T*H == expected
    v=wedge(A1,B1)+wedge(B1,A2)+wedge(A2,B2)
    K=S.Matrix(row['cusp']['K'])
    degrees=[wall_degree(K,*w) for w in walls]
    assert (omega*v)[0] == sum(degrees)
    k=row['cusp']['kappa']
    assert sum(degrees) == a-a*c*k-c+a*c*c*k*k
    cap_vectors[z]=v
    local.append({'index':z,'kind':'cusp','kappa':k,'H':ints(H),
                  'H_inverse':ints(H.inv()),'K':ints(K),
                  'wall_degrees':vector(S.Matrix(degrees)),
                  'preimage':vector(v),'Omega_degree':int(sum(degrees))})
    total=sum(cap_vectors,S.zeros(6,1))
    degree=int((omega*total)[0])
    assert degree%c == 0
    F=S.Matrix(row['fibre_basis'])
    Fi=S.Matrix(row['fibre_basis_inverse'])
    R=S.Matrix(row['exterior_relations'])
    Q=S.Matrix(row['exterior_kernel_right_inverse'])
    assert F*Fi==S.eye(6) and Fi[0,:]==omega
    assert R == S.Matrix.hstack(*(outer2(S.Matrix(t))-S.eye(6)
                                for t in row['monodromies']))
    s0=F[:,0]
    difference=total-degree*s0
    coordinate=Fi*difference
    assert coordinate[0]==0
    chain=Q*coordinate[1:6,0]
    assert R*chain==difference
    old_link = ({2:37,3:7,4:27} if row['OS']==55 else {1:4,2:4,3:4,4:4})[z]
    signs=[]
    for e in [-1,1]:
        link=-degree//(c*e)
        normal=-c*e*s0
        assert R*chain+link*normal==total
        # Bounding c*s0 uses -e times the physical delta normal disc.
        assert -e*normal==c*s0
        assert gcd(e,c)==1
        P=(c//2)*(link%2)
        signs.append({'e':e,'delta_Thom_coefficient':link,
                      'torsion_generator_delta_coefficient':-e,
                      'refined_P_from_linking_parity':P,
                      'old_claimed_linking':e*old_link})
    rows.append({'OS':row['OS'],'a':a,'c':c,'zero':z,
                 'locals':sorted(local,key=lambda x:x['index']),
                 'cap_preimages':[vector(v) for v in cap_vectors],
                 'critical_total':vector(total),'Omega_total':degree,
                 'fibre_generator':vector(s0),
                 'exterior_bounding_coefficients':vector(chain),
                 'signs':signs})
    print('OS',row['OS'],'zero',z,'Omega_caps',
          [int((omega*v)[0]) for v in cap_vectors],
          'Omega_total',degree,'link(e=+1)',-degree//c,
          'P',signs[1]['refined_P_from_linking_parity'],
          'old_link',old_link)
    print('  cap_preimages',[vector(v) for v in cap_vectors])
    print('  exact_exterior_chain',vector(chain))

old_example=S.Matrix([-19,-23,-10,0,5,6])
actual=S.Matrix(rows[0]['cap_preimages'][2])
assert actual==S.Matrix([5,-24,-8,0,4,-19])
assert (S.Matrix([[5,0,0,0,0,-4]])*(actual-old_example))[0]==220
payload={'input_sha256':EXPECTED,'scope':'post-exposure; prescribed fan retained',
         'wall_matrix':ints(wall_matrix),'wall_inverse':ints(wall_matrix.inv()),
         'old_support_matrix':ints(old_matrix),'curve_swap':ints(swap),
         'rows':rows}
with OUTPUT.open('x') as f:
    json.dump(payload,f,indent=2);f.write('\n')
print('PASS all fourteen signs; actual local maps/inverses; all integral chains; unit torsion linking')
print('DATA',str(OUTPUT),sha256(OUTPUT.read_bytes()).hexdigest())
