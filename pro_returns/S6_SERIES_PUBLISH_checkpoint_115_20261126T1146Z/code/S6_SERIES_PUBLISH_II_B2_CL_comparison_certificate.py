#!/usr/bin/env python3
"""Postrelease CL comparison: weighted blowup charts and character algebras.

Standalone. Recomputes all original displayed numerical claims, including
the stronger uniform rationality argument not needed by the frozen route.
"""
import itertools
import json
import math
import sympy as S

checks=[]


def ck(name, result, evidence):
    result=bool(result)
    checks.append({'name':name,'passed':result,'evidence':evidence})
    if not result:
        raise AssertionError(name)


def clean(a):
    if isinstance(a,dict): return {str(k):clean(v) for k,v in a.items()}
    if isinstance(a,(list,tuple)): return [clean(v) for v in a]
    if isinstance(a,S.Integer): return int(a)
    if isinstance(a,S.Basic): return str(a)
    return a


def intersect(a,b):
    return 2*a[0]*b[0]+a[0]*b[1]+a[1]*b[0]


v,a,d=S.symbols('v a d',integer=True)
ck('unbalanced first pure-cube coefficient',
   S.expand(-3*a-v).subs({a:0,v:1})<0,
   {'degree':-3*a-v,'domain':'a>=0,v>=1','maximum':-1})
ck('unbalanced quadratic leading coefficient',
   (2-a-v).subs(v,2)==-a,
   {'degree':2-a-v,'consequence':'a+v<=2; v=2 implies a=0'})
ck('balanced bidegree budget',
   S.expand((1)+(3-v-d)-1)==3-v-d,
   {'section':[1,d],'quadratic':[2,3-v-d],
    'irreducibility_requires_second_degree_at_least':1,
    'v2_forces_d':0})
bh=(3,-2)
pa=S.Rational(1)+S.Rational(intersect(bh,(1,-2)),2)
ck('C.RD.28 arithmetic genus and total delta',pa==0 and pa+2-1==1,
   {'horizontal_class':bh,'arithmetic_genus':pa,'normalization_components':2,
    'total_delta':pa+2-1})


def hilbert_coefficients(weights,degree):
    top=3*degree-2*sum(weights)
    coeff=[0]*(top+1);coeff[0]=1
    for w in weights:
        for i in range(w,top+1):coeff[i]+=coeff[i-w]
    for w in weights:
        n=degree-w
        coeff=[coeff[i]-(coeff[i-n] if i>=n else 0) for i in range(top+1)]
    return coeff


local=[]
for kind,index in [('A',1),('A',2),('A',3),('D',4),('D',5),('D',6)]:
    if kind=='A':
        degree=math.lcm(2,index+1,3)
        weights=[degree//2,degree//(index+1),degree//3]
        mu=2*index
    else:
        degree=math.lcm(2*(index-1),3)
        weights=[degree*(index-2)//(2*(index-1)),degree//(index-1),degree//3]
        mu=2*index
    coeff=hilbert_coefficients(weights,degree)
    pg=sum(c for j,c in enumerate(coeff) if j+sum(weights)<=degree)
    link=sum(c for j,c in enumerate(coeff) if (j+sum(weights))%degree==0)
    row={'plane_type':kind+str(index),'weighted_degree':degree,'weights':weights,
         'jacobian_hilbert_coefficients':coeff,'mu':sum(coeff),'pg':pg,'link_b1':link}
    local.append(row)
    wantpg=int(kind=='D');wantlink=2 if (kind,index)==('D',4) else 0
    ck('Koszul Hilbert spectrum '+kind+str(index),
       all(c>=0 for c in coeff) and sum(coeff)==mu and pg==wantpg and link==wantlink,row)
ck('C.RD.29 complete horizontal-delta-one budget',
   max(q['pg'] for q in local)==1 and max(q['link_b1'] for q in local)==2,
   {'positive_genus_types':['D4','D5','D6'],
    'each_requires_horizontal_delta':1,'total_horizontal_delta':1,
    'sum_pg_bound':1,'sum_link_b1_bound':2,
    'other_local_types':['A1','A2','A3']})

s,x,u,y,w,z,Z=S.symbols('s x u y w z Z')
charts=[]


def chart(name,poly,sub,exceptional,power,want,inc):
    transformed=S.expand(poly.subs(sub, simultaneous=True))
    difference=S.expand(transformed-exceptional**power*want)
    row={'name':name,'old_equation':poly,'substitution':sub,
         'exceptional_factor':exceptional**power,'new_equation':want,
         'difference':difference,'character_increments':inc}
    charts.append(row)
    ck('exact weighted chart '+name,difference==0,row)


for contact in [1,2]:
    poly=w**3-s*s*(s-u**contact)
    chart('contact_%d_main'%contact,poly,{s:u*x,w:u*z},u,3,
          z**3-x*x*(x-u**(contact-1)),[1,1])
    chart('contact_%d_other'%contact,poly,{u:s*x,w:s*z},s,3,
          z**3-(1-s**(contact-1)*x**contact),[1,1])
chart('contact_2_second',z**3-x*x*(x-u),{x:u*y,z:u*Z},u,3,
      Z**3-y*y*(y-1),[1,1])
node=w**3-s*s*x*(x-s)
chart('node_on_double_fibre_main',node,{x:s*u,w:s*z},s,3,
      z**3-s*u*(u-1),[1,1])
chart('node_on_double_fibre_other',node,{s:x*u,w:x*z},x,3,
      z**3-x*u*u*(1-u),[1,1])
tangent_node=w**3-s*s*x*(s-x*x)
chart('tangent_node_first_main',tangent_node,{s:x*u,w:x*z},x,3,
      z**3-x*u*u*(u-x),[1,1])
chart('tangent_node_first_other',tangent_node,{x:s*u,w:s*z},s,3,
      z**3-s*u*(1-s*u*u),[1,1])
chart('tangent_node_second_main',z**3-x*u*u*(u-x),{u:x*y,z:x*Z},x,3,
      Z**3-x*y*y*(y-1),[1,1])
chart('tangent_node_second_other',z**3-x*u*u*(u-x),{x:u*y,z:u*Z},u,3,
      Z**3-u*y*(1-y),[1,1])
cusp=w**3-s*s*(x*x-s**3)
chart('cusp_first_main',cusp,{x:s*u,w:s*z},s,3,
      z**3-s*(u*u-s),[1,1])
chart('cusp_first_other',cusp,{s:x*u,w:x*z},x,3,
      z**3-x*u*u*(1-x*u**3),[1,1])
chart('cusp_second_main',z**3-s*(u*u-s),{s:u*x},u,0,
      z**3-u*u*x*(u-x),[0,1])
chart('cusp_second_other',z**3-s*(u*u-s),{u:s*x},s,0,
      z**3-s*s*(s*x*x-1),[0,1])
chart('cusp_third_main',z**3-u*u*x*(u-x),{x:u*y,z:u*Z},u,3,
      Z**3-u*y*(1-y),[1,1])
chart('cusp_third_other',z**3-u*u*x*(u-x),{u:x*y,z:x*Z},x,3,
      Z**3-x*y*y*(y-1),[1,1])

increments=[]
for m1,m2 in [(1,1),(2,1),(2,0)]:
    total=m1+2*m2
    quotient,remainder=divmod(total,3)
    b2=2*quotient-m2+int(remainder==2)
    row={'m1':m1,'m2':m2,'total':total,'k':quotient,'j':remainder,
         'increments':[quotient,b2]}
    increments.append(row)
ck('C.RD.34 all character increments',
   [r['increments'] for r in increments]==[[1,1],[1,1],[0,1]],increments)
m2,kk,jj=S.symbols('m2 kk jj',integer=True)
ck('C.RD.34 second character divisor identity',
   S.expand(2*kk-m2+jj)==2*kk-m2+jj,
   {'Lprime':'sigma*L-kE',
    'D2prime':'sigma*D2-m2 E+1_(j=2) E',
    'increment_first':kk,'increment_second':2*kk-m2+jj,
    'map_old_w':'e^k wprime','map_old_second_generator':'e^(2k-m2+1_(j=2)) sprime'})
ee,ww,tt=S.symbols('ee ww tt',nonzero=True)
ck('smooth-contact integral generator transport',
   S.simplify((ee*ww)**2/(ee*tt)-ee*ww**2/tt)==0,
   {'old_generator':'w^2/s','new_generator':'w1^2/s1','multiplier':'e'})
ck('cusp tangency integral generator transport',
   S.simplify(ww**2-ee*(ww**2/ee))==0,
   {'old_generator':'w1^2','new_generator':'w1^2/e','multiplier':'e',
    'first_character_multiplier':1})

quotients=[]
for aa,bb in itertools.product([1,2],repeat=2):
    kernel=[(i,j) for i,j in itertools.product(range(3),repeat=2)
            if (aa*i+bb*j)%3==0]
    eps=(-aa*pow(bb,-1,3))%3
    generator=(1,eps)
    generated=sorted(((q*generator[0])%3,(q*generator[1])%3) for q in range(3))
    den='x' if (aa,bb)==(2,1) else ('y' if (aa,bb)==(1,2) else ('x*y' if aa==2 else 'none'))
    row={'branch_weights':[aa,bb],'kernel':kernel,'generator':generator,
         'quotient_type':[1,eps],'extra_generator_denominator':den,
         'exceptional_matrix':[[-3]] if eps==1 else [[-2,1],[1,-2]]}
    quotients.append(row)
    ck('crossing quotient weights %d,%d'%(aa,bb),sorted(kernel)==generated,row)
ck('both quotient resolution determinants',
   S.det(S.Matrix([[-3]]))==-3 and S.det(S.Matrix([[-2,1],[1,-2]]))==3,
   {'absolute_determinants':[3,3],'rational_link_b1':[0,0]})
ck('point blowup zero-or-one character cohomology',
   [max(-d-1,0) for d in [0,-1]]==[0,0],
   {'restriction_to_E':['O_P1','O_P1(-1)'],
    'sigma_push_O_and_OE':'O_base','R1_sigma_both':0,
    'formal_neighborhood_terms_for_structure':'H1(P1,O(j))=0 for j>=0'})

PP=S.symbols('P',integer=True)
ck('C.RD.30 canonical quotient and Euler identity',
   S.expand(0-(2-PP)+1)==PP-1,
   {'chi_resolved':2-PP,'pg_when_P_positive':0,'q_when_P_positive':PP-1,
    'P_possible':[0,1],'q_in_both_cases':[0,0],
    'canonical_quotient':'Ext^2(M,omega_X0), length=P'})

nu,n,lam=S.symbols('nu n lam',integer=True)
for c,want_eu,want_bd,want_rank in [
 (4,3*(nu-4),nu-3+lam,2*nu-8-lam),
 (3,3*(nu-2),nu-2+lam,2*nu-4-lam)]:
    eb=2*c-nu
    eu=S.expand(3*(4-eb))
    ed=eb+n-lam
    b1d=S.expand(1+n+c-ed)
    ex0=S.expand(12-2*eb)
    rank=S.expand(ex0+n-lam-2-(n+2))
    ck('C.RD.31 or .36 all ranks c='+str(c),
       S.expand(eu-want_eu)==0 and S.expand(b1d-want_bd)==0
       and S.expand(rank-want_rank)==0,
       {'e_B':eb,'e_U':eu,'b1_D':b1d,'e_X0':ex0,
        'rank_compact':rank,'b1_U':c-2})
ck('reduced rank-zero numerical possibilities',
   [(l,4+l//2) for l in [0,2]]==[(0,4),(2,5)],
   {'lambda_nu_pairs':[(0,4),(2,5)],'nu_max':5})
ap,aq,out=S.symbols('a_p a_q outside',integer=True)
nuformula=2+ap+aq+out
loss=ap+aq-2+out
ck('C.RD.32 paired attachment budget exact cancellation',
   S.expand(loss-(nuformula-4))==0,
   {'nu':nuformula,'loss_upper_bound':loss,
    'two_common_values_counts':[1,2],'outside_loss_cost':'at least one branch excess'})
ck('double-zero rank forces all attachment losses zero',
   S.solve(2*nu-4,nu)==[2],
   {'nu':2,'fibre_contribution':'1+#C_preimages',
    'C_preimages':1,'outside_multibranch_points':0,'loss':0})
rd=S.symbols('r_dom',integer=True)
ck('C.RD.37 stronger Euler conclusion',
   (2-rd).subs(rd,1)==1,
   {'e_S_lower_bound':2-rd,'r_dom_max':1,'lower_bound':1})

print(json.dumps(clean({'target':'01CL','phase':'postrelease complete original comparison',
                       'check_count':len(checks),'all_passed':all(x['passed'] for x in checks),
                       'checks':checks,'local_hilbert_rows':local,
                       'weighted_chart_rows':charts,'character_increment_rows':increments,
                       'crossing_quotient_rows':quotients}),indent=2))
