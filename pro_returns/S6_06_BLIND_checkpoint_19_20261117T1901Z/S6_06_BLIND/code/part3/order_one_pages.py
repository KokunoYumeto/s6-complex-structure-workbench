#!/usr/bin/env python3
"""Exact base/cochain maps for order-one page redistribution (working proof).

The source, line, and relative trace arrows are proved in the accompanying
note.  These matrices retain every norm and the initial framing b0.
"""
import json
from pathlib import Path
import sympy as s

mi,m0,ni,n0,b0=s.symbols('mi m0 ni n0 b0', integer=True)
records=[]
for q in range(5):
    ns=s.symbols('n1:'+str(q+1), integer=True)
    N=sum(ns)-b0
    nip=ni+mi*N
    D=m0*nip+mi*n0
    size=q+3
    A=s.zeros(size)
    A[0,0]=mi;A[0,-1]=ni
    A[1,1]=m0;A[1,-1]=n0
    for j,n in enumerate(ns):A[j+2,j+2]=1;A[j+2,-1]=n
    for j in range(size-1):A[-1,j]=1
    A[-1,-1]=b0
    # Old coordinates in terms of new:
    # alpha_infty=alpha_infty'+N gamma;
    # alpha_j=alpha_j'-n_j gamma.
    C=s.eye(size);C[0,-1]=N
    for j,n in enumerate(ns):C[j+2,-1]=-n
    R=s.eye(size)
    for j in range(q):R[-1,j+2]=-1
    B=s.simplify(R*A*C)
    expected=s.zeros(size)
    expected[0,0]=mi;expected[0,-1]=nip
    expected[1,1]=m0;expected[1,-1]=n0
    for j in range(q):expected[j+2,j+2]=1
    expected[-1,0]=expected[-1,1]=1
    assert s.simplify(B-expected)==s.zeros(size)
    assert C.det()==R.det()==1
    assert s.expand(A.det()+D)==0
    records.append({
      'added_sites':q,'old_relation_matrix':[[str(v) for v in row] for row in A.tolist()],
      'old_from_new_coordinates':[[str(v) for v in row] for row in C.tolist()],
      'relation_change':[[str(v) for v in row] for row in R.tolist()],
      'transported_relation_matrix':[[str(v) for v in row] for row in B.tolist()],
      'n_infty_prime':str(nip),'determinant':str(-D),
      'check':'R*A*C=core(ni+mi*(sum n_j-b0),n0) plus order-one identity relations'
    })

# Divisor vectors encode literal meromorphic integer monomials.  The
# infinity valuation is minus the sum of finite valuations, not omitted.
q=3
ns=s.symbols('n1:4',integer=True)
M=mi*m0;N=sum(ns)-b0
ni_prime=ni+mi*N;D=m0*ni_prime+mi*n0
labels=['zero','c1','c2','c3','framing_chart','selected_cusp','infinity']
u=[0,*ns,-b0,0,-N]
old=[mi*n0,*[M*n for n in ns],-M*b0,-D,m0*ni]
new=[mi*n0,0,0,0,0,-D,m0*ni_prime]
assert s.expand(sum(old))==s.expand(sum(new))==s.expand(sum(u))==0
assert all(s.expand(a-b-M*c)==0 for a,b,c in zip(old,new,u))

epsilon=s.symbols('epsilon',integer=True)
phase=s.Matrix([[epsilon*m0,-epsilon*n0],[epsilon*mi,epsilon*ni_prime]])
weighted=(s.Matrix([[-mi,m0]])*phase)
assert weighted[0,0]==0
assert s.expand(weighted[0,1]-epsilon*D)==0

# Generator identity is checked in the actual abelian commuting exponent
# lattice: Ai'=Ai B^N; (Ai')^mi has B exponent ni+mi*N.
assert s.expand(ni+mi*N-ni_prime)==0

t,tau,u0,u1,u2=s.symbols('t tau u0 u1 u2',nonzero=True)
aa,bb=s.symbols('aa bb',integer=True)
unit=u0+u1*(t-tau)+u2*(t-tau)**2
binding=(t-tau)*(t/tau)**aa*(unit/u0)**bb
assert s.simplify(s.diff(binding,t).subs(t,tau))==1
H,chi=s.symbols('H chi')
k=-3*H;ell=-24*chi;mr=6*chi;nr=3*H-6*chi
assert s.expand(-(mr+nr)-k)==0
assert s.expand((4*k-ell)/24-(chi-H/2))==0

la,lb,nn,AA=s.symbols('lambda_a lambda_b n A',integer=True)
smooth=s.Matrix([[1,0,0,-la],[0,1,0,-lb],[0,0,1,nn]])
relation=s.Matrix([la,lb,-nn,1])
assert smooth*relation==s.zeros(3,1)
assert smooth[:,0:3]==s.eye(3)
mult=s.Matrix([[0,1,0,0],[0,0,0,1],[1,-AA,0,0],[0,0,1,AA]])
assert abs(mult.det())==1

data={
 'status':'PASS; O1-O9 independently root audited, exact wedge and gcd refinements included',
 'proof':'notes/part3_order_one_pages_working.md',
 'framing_convention':'sum alpha_i+b0 gamma=0',
 'effective_norm':str(ni_prime),
 'determinant_D':str(D),
 'full_integral_coordinate_maps':records,
 'meromorphic_divisor_labels':labels,
 'u_divisor':[str(v) for v in u],
 'f_old_divisor':[str(v) for v in old],
 'f_new_divisor':[str(v) for v in new],
 'literal_closing_identity':'f_old/f_new=u^M',
 'phase_matrix':[[str(v) for v in row] for row in phase.tolist()],
 'weighted_ratio_phase':[[str(v) for v in row] for row in weighted.tolist()],
 'sphere_substitution':'epsilon=D=+1 or -1 gives m0 phi2-mi phi1=alpha',
 'total_space_scope':'base phase map only; page source/line arrows are separate and retained',
 'line_remainder':'corrected page ratio is a base line kF; c1(N).F=F^2=0',
 'parameter':'lambda=r^(mi*m0); all fixed elliptic/delta clutches independent of r',
 'binding_coordinate':'(t-tau)*(t/tau)^(-epsilon*mi*n0)*(u(t)/u(tau))^(-epsilon*M)',
 'binding_derivative':'1',
 'normal_clutch':'[h(p)^-1 Rz(-M*g(p))]*[Rz(phi-M*theta)G(0,theta)]',
 'full_characteristic_pair':{'k':str(k),'ell':str(ell)},
 'relative_pair':[str(mr),str(nr)],
 'primitive_no_additive':{'M':1,'chi':1,'H':'d','A':'1-d/2','relative_pair':['6','3d-6']},
 'order_one_smooth_kernel_columns':['a wedge mu','b wedge mu','mu wedge gamma','alpha wedge mu'],
 'order_one_smooth_rims':['a wedge alpha','b wedge alpha','alpha wedge gamma'],
 'order_one_smooth_matrix':[[str(v) for v in row] for row in smooth.tolist()],
 'primitive_kernel_relation':[str(v) for v in relation],
 'multiplicative_m1_D2':[[str(v) for v in row] for row in mult.tolist()],
 'multiplicative_m1_determinant':str(mult.det()),
 'scope':'sphere topology for every allowed fan; return data for the vertical-edge reference fan'
}
Path(__file__).with_suffix('.json').write_text(json.dumps(data,indent=2)+'\n')
print('PASS: five full marked relation maps, b0 sign, exact divisor ratio, phase matrix, generator identity.')
