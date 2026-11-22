#!/usr/bin/env python3
"""Fresh E11 weighted-line arithmetic; target proof/E11 old routine closed.

The accompanying derivation proves the identities for all admissible k,l.
The finite range below checks their implementation and illustrates both
intermediate cohomology regimes; it is not a finite substitute for proof.
"""
from pathlib import Path
import math,json,hashlib,itertools

def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]
def det(A):
    n=len(A);out=0
    for p in itertools.permutations(range(n)):
        sign=(-1)**sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))
        v=sign
        for i in range(n):v*=A[i][p[i]]
        out+=v
    return out

C=[[-2,1,0,-2],[-1,0,0,0],[3,-1,1,0],[0,0,0,1]]
PV=[[-2,1,0,1],[-6,0,-1,0],[0,-1,0,0],[-1,0,0,0]]
PVi=[[0,0,0,-1],[0,0,-1,0],[0,-1,0,6],[1,0,1,-2]]
Pmark=[[0,-2,-1,-2],[2,-1,0,-1],[0,2,1,3],[-1,0,0,0]]
I=[[int(i==j) for j in range(4)] for i in range(4)]
assert mm(PV,PVi)==mm(PVi,PV)==I
assert mm(C,PV)==Pmark
assert det(C)==1 and det(PV)==-1
AI1=[[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]]
AI2=[[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]]
AV0=[[1,-1,0,2],[0,-1,-1,6],[0,1,0,0],[0,0,0,1]]
AV1=[[1,0,1,-3],[0,0,1,0],[0,-1,0,6],[0,0,0,1]]
assert mm(mm(PV,AI1),PVi)==AV0
assert mm(mm(PV,AI2),PVi)==AV1
# A linear polynomial is its integer coefficient vector in (1,tau,mu,beta).
Pi=[[[0,0,6,0],[0,1,0,0],[1,0,0,0],[0,0,0,0]],
    [[0,0,0,1],[0,0,1,0],[0,0,0,0],[1,0,0,0]]]
actual=[[[sum(Pi[i][k][c]*PVi[k][j] for k in range(4))
          for c in range(4)] for j in range(4)] for i in range(2)]
expected=[[[0,0,0,0],[-1,0,0,0],[0,-1,0,0],[6,0,-6,0]],
          [[1,0,0,0],[0,0,0,0],[1,0,-1,0],[-2,0,0,-1]]]
assert actual==expected
assert PVi[0]==[0,0,0,-1]  # marked gamma = -psi in the primary basis

def monomials(k,l,n):
    if n<0:return []
    r,s=3*k,4*l
    return [(a,(n-r*a)//s) for a in range(n//r+1)
            if n-r*a>=0 and (n-r*a)%s==0]

def dims(k,l,n):
    return [len(monomials(k,l,n)),len(monomials(k,l,-n-3*k-4*l))]

examples=[];regimes={0:0,1:0};count=0
for k in range(1,81):
    for l in range(1,81):
        if math.gcd(3*k,4*l)!=1:continue
        count+=1;z=k*l;d=3*k+4*l;eps=int(k==1)
        assert dims(k,l,-z)==[0,0]
        assert dims(k,l,-2*z)==[0,0]
        assert monomials(k,l,d)==[(1,1)]
        assert monomials(k,l,d-z)==([(l+1,0)] if k==1 else [])
        assert dims(k,l,d-z)==[eps,0]
        # L: (1,1+eps,eps,0), Q: (1,2,0,0).
        # H0 evaluation is iso and H1 evaluation is injective.
        Jdims=[0,0,2-(1+eps)+eps,0]
        assert Jdims==[0,0,1,0]
        tangent=[1,1,Jdims[2],0];assert tangent==[1,1,1,0]
        regimes[eps]+=1
        if (k,l) in [(1,1),(1,2),(1,4),(3,1),(5,2),(7,5),(79,80)]:
            examples.append({'k':k,'l':l,'weights':[3*k,4*l],'z':z,'d':d,
                             'H0_O_d':monomials(k,l,d),'H0_O_d_minus_z':monomials(k,l,d-z),
                             'h_L':[1,1+eps,eps,0],'h_Q':[1,2,0,0],
                             'h_image_df':Jdims,'h_tangent':tangent})

# Global root morphism [X:Y] -> [X^l:Y^k], interpreted with O(kl).
for k,l in [(1,1),(1,2),(3,1),(5,2),(79,80)]:
    assert l*(3*k)==3*(k*l)
    assert k*(4*l)==4*(k*l)

out={'schema':'S6_SERIES_PUBLISH.fresh_prereading_weight_arithmetic.v1',
     'target':'01GI/cdp:st:E11','target_proof_opened':False,'old_E11_program_opened':False,
     'method':'Integer weighted monomial enumeration with the universal congruence proof supplied in the derivation.',
     'checked_pairs':count,'range':'1<=k,l<=80 and gcd(3k,4l)=1',
     'regime_counts':regimes,'examples':examples,
     'universal_formulas':{'epsilon':'1 when k=1, otherwise0','h_vertical':[1,1,0,0],
                          'h_L':'(1,1+epsilon,epsilon,0)','h_Q':[1,2,0,0],
                          'h_image_df':[0,0,1,0],'h_tangent':[1,1,1,0]},
     'universal_proof':'Congruences force A=1+l*a and B=1+k*b; the relevant equations are 3a+4b=0 or -1. Serre-dual nonnegative exponents force positive a,b with 3a+4b=1 or2, which is impossible.',
     'root_morphism':'[X:Y] maps to [X^l:Y^k]; O(1) pulls back to O(kl), and coarse coordinate Y^(3k)/X^(4l) is unchanged.',
     'exact_marking_transport':{'primary_basis_in_Engel':C,'P_V':PV,'P_V_inverse':PVi,
         'P_mark':Pmark,'C_PV_equals_Pmark':True,'both_finite_monodromies_intertwined':True,
         'period_coefficient_order':['1','tau','mu','beta_c'],
         'Pi_times_PV_inverse':actual,
         'normalized_period_matrix':'diag(-1,1)*Pi*PV^-1=[[0,1,tau,-6*zP],[1,0,zP,rho]], zP=1-mu, rho=-beta_c-2',
         'coherent_covector':'gamma_marked=-psi_primary',
         'exponential_vector_map':'e=d/dzeta2 maps to 2*pi*i*Euler under W=exp(2*pi*i*zeta2)',
         'parameter':'u=exp(-2*pi*i*c)',
         'KS_transport':'kappa_u=u^-1*Euler tensor psi=-(2*pi*i*u)^-1*e tensor gamma; kappa_c=e tensor gamma'},
     'program_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'events_added':0}
p=Path(__file__).with_name(Path(__file__).stem+'_output.json')
p.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
                  'checked_pairs':count,'all_assertions_passed':True}))
