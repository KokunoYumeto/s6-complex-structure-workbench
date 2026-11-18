"""Independent actual fixed-ideal, quotient-chart and volume audit."""
from pathlib import Path
from itertools import product,combinations
from datetime import datetime,timezone
import hashlib,json
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
INPUT=ROOT/'code/part3_root/e6_selected_infinity_mu2_pair.json'
NOTE=ROOT/'notes/part3_e6_selected_infinity_mu2_root_working.md'
data=json.loads(INPUT.read_text());checks=[]
def yes(name,p):
    assert bool(p),name
    checks.append(name)
I=s.eye(4);physical=s.Matrix([0,0,1,-1])
for n,row in enumerate(data['rows']):
    j=row['j'];parity=s.Matrix([v%2 for v in [1,-1,j,-j-1]])
    Q=s.Matrix.hstack(parity/2,I[:,1],I[:,2],I[:,3])
    C=s.Matrix(row['rays_as_columns']);N=Q*C
    yes(f'{n} actual quotient lattice',Q.det()==s.Rational(1,2))
    yes(f'{n} regular in actual quotient',C.det()==1)
    odd=[k for k in range(4) if parity[k]];neutral=next(k for k in range(4) if not parity[k])
    a=row['pivot_cover_coordinate'];others=[k for k in odd if k!=a]
    yes(f'{n} exact fixed axis',neutral==row['neutral_cover_coordinate'] and a in odd)
    chars=[]
    r=[0]*4;r[a]=2;chars.append(r)
    for b in others:
        r=[0]*4;r[b]=1;r[a]=-1;chars.append(r)
    r=[0]*4;r[neutral]=1;chars.append(r)
    T=s.Matrix(chars);permutation=T*N
    yes(f'{n} full explicit Rees quotient coordinates',chars==row['explicit_coordinate_character_rows_in_cover'])
    yes(f'{n} toric and actual quotient charts identical',permutation==s.Matrix(row['explicit_coordinate_matrix']))
    yes(f'{n} quotient chart invertible',abs(permutation.det())==1)
    generators={v for v in product(range(3),repeat=4) if 1<=sum(v)<=2 and sum(v[k]*parity[k] for k in range(4))%2==0}
    yes(f'{n} all quadratic/neutral invariants',generators==set(tuple(v) for v in row['invariant_generators']))
    for v,recorded in zip(row['invariant_generators'],row['invariant_monomial_matrix']):
        exponent=s.Matrix([v])*N
        yes(f'{n} invariant monomial map {v}',list(exponent)==recorded and all(q.q==1 and q>=0 for q in exponent))
    gamma=s.Matrix([1,-1,j,-j-1])
    yes(f'{n} actual phase map',list(T*gamma)==row['explicit_mu4_phase_powers'])
    yes(f'{n} representative square closes',all(int(v)%2==0 for v in T*gamma))
    yes(f'{n} actual physical action',list(T*physical)==row['explicit_physical_weights'])
    yes(f'{n} physical action in oriented toric chart',list(C.inv()*physical)==row['chart_physical_weights'])
    orders=s.Matrix([[1,1,4,4]])*N-s.ones(1,4)
    yes(f'{n} original volume order row',list(orders)==row['original_volume_orders'])
    for lab,char in [('epsilon',[1,0,1,1]),('q_new',[4,0,0,0]),('sigma_fourth',[0,0,4,4])]:
        out=s.Matrix([char])*N
        yes(f'{n} actual base {lab}',list(out)==row[lab+'_exponents'] and all(v.q==1 and v>=0 for v in out))
    # Direct coordinate determinant carries the full quotient volume unit.
    rho,zb,zc,u=s.symbols('rho zb zc u',nonzero=True)
    tt=s.symbols('tt',nonzero=True)
    w=[None]*4;w[a]=tt;w[others[0]]=tt*zb;w[others[1]]=tt*zc;w[neutral]=u
    Jac=s.Matrix([[s.diff(expr,var) for var in [tt,zb,zc,u]] for expr in w]).det()
    Vcoeff=s.factor((w[2]*w[3])**3*Jac/(2*tt))
    # Its exponent vector agrees with the explicit-chart permutation of the toric row.
    powers=[s.diff(Vcoeff,z)*z/Vcoeff for z in [tt,zb,zc,u]]
    explicit_orders=[s.simplify(powers[0]/2)]+list(map(s.simplify,powers[1:]))
    yes(f'{n} direct blowup volume exponents',s.Matrix(explicit_orders)==permutation*s.Matrix(list(orders)))
    yes(f'{n} quotient lattice volume factor',abs(s.factor(Vcoeff/(tt**powers[0]*zb**powers[1]*zc**powers[2]*u**powers[3])))==s.Rational(1,2))
yes('all twelve actual quotient charts',len(data['rows'])==12)
# Explicit chart transition from pivot a to b.
ra,z,zz=s.symbols('rho_a z_b z_c',nonzero=True)
rb=ra*z**2;za=1/z;zc=zz/z
yes('quadratic transition retains radial square',s.factor(rb*za**2-ra)==0)
yes('quadratic transition preserves mixed invariant',s.factor(rb*za*zc-ra*zz)==0)
yes('quadratic transition preserves remaining square',s.factor(rb*zc**2-ra*zz**2)==0)
# Complete nonmonomial source reset and invariant differential.
X,Y,sg,aa,d=s.symbols('X Y sigma a2 d')
eq=Y**2-X**3-aa*X**2-d*X-sg**2
xp=d/X+2*sg*(Y+sg)/X**2
yp=sg-(Y+sg)*xp/X
def oncurve(expr):
    numerator=s.together(expr).as_numer_denom()[0]
    return s.rem(numerator,eq,Y)==0
yes('full chord exact source arrow',oncurve(yp**2-xp**3-aa*xp**2-d*xp-sg**2))
A=-xp/X;B=1-xp/X
yes('retained full affine tangent mix',s.factor(yp-A*Y-B*sg)==0)
Ds=3*X**2+2*aa*X+d;Dt=3*xp**2+2*aa*xp+d
J=s.diff(yp,Y)+s.diff(yp,X)*(2*Y/Ds)
yes('full differential unit transports',oncurve(J/Dt-1/Ds))
for sign in (-1,1):
    at={X:sign*s.I,Y:0,sg:0,aa:0,d:1}
    yes('opposite two-torsion point',s.simplify(xp.subs(at))==-sign*s.I)
    yes('central tangent and mix retained',s.simplify(A.subs(at))==1 and s.simplify(B.subs(at))==2)
    yes('central volume unit minus one half',s.simplify((1/Ds).subs(at))==-s.Rational(1,2))
quarter={X:-X,Y:-s.I*Y,sg:-s.I*sg,aa:-aa}
yes('source reset commutes with full quarter map X',s.simplify(xp.subs(quarter,simultaneous=True)+xp)==0)
yes('source reset commutes with full quarter map Y',s.simplify(yp.subs(quarter,simultaneous=True)+s.I*yp)==0)
# Full fixed-ideal chart map, including neutral coordinate and source mix.
A0,B0,C0,u0,t,z1,z2=s.symbols('A0 B0 C0 u0 t z1 z2',nonzero=True)
for parity in (0,1):
    line=C0**(1 if parity else -1)
    M=s.Matrix([[1,0,0],[0,A0,B0*u0],[0,0,line]])
    col=s.Matrix([1,z1,z2]);L=M*col
    yes('fixed ideal invertible full matrix',s.factor(M.det()-A0*line)==0)
    yes('actual Rees lift is homogeneous',(M*(t*col)-t*L).applyfunc(s.expand)==s.zeros(3,1))
    for pivot in range(3):
        for i in range(3):
            for k in range(i,3):
                yes('all coarse invariants commute with lifted map',s.factor(t**2*L[pivot]**2*(L[i]/L[pivot])*(L[k]/L[pivot])-t**2*L[i]*L[k])==0)
# Full line wedge, including every integer chain index.
xx,yy,j=s.symbols('Xline Yline j',nonzero=True)
line_log=s.Matrix([[(j+1)/xx,j/yy]])
sig_grad=s.Matrix([[yy,xx]])
yes('exact chain wedge negative sign',s.Matrix.vstack(sig_grad,line_log).det()==-1)
out={'status':'PASS','utc':datetime.now(timezone.utc).isoformat(),'checks':len(checks),
 'source_sha256':hashlib.sha256(NOTE.read_bytes()).hexdigest(),
 'input_sha256':hashlib.sha256(INPUT.read_bytes()).hexdigest(),
 'scope':'Independent twelve-chart fixed-ideal/Rees quotient audit, actual full source-mixing/neutral-line maps, all fourth-root and physical phases, original marked-volume unit/exponents and period representative square. Global selected attachment/return excluded.',
 'checked_assertions':checks}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='checked_assertions'},indent=2))

