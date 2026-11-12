"""Exact, serial J/M cubic-value audit in the original marked coordinates.

Run: python check_jm_values.py
The vendored cubic_engine.py uses Fraction arithmetic and the actual Cayley
product, with no floating arithmetic or external mathematical dependencies.
"""
from fractions import Fraction as Q
from itertools import combinations, product
from functools import reduce
from math import gcd, lcm
import json
import time
from pathlib import Path
import cubic_engine as E


def omega(t):
    return tuple(Q(int(j < t))-Q(t, 6) for j in range(6))


u = omega(2)+omega(4)+omega(0)+omega(2)+(Q(0),)*4
r = lambda X: E.transform_shift(X, 2)
p = E.sub(u, r(u))
q = E.add(E.sub(E.v, r(E.v)), r(u))
IG = E.K[:28]+[E.scale(E.K[28], 3)]
JG = IG+[E.scale(E.v, 3)]
MG = JG+[p, q]
E.check(len(IG)==29 and len(JG)==30 and len(MG)==32, 'I/J/M list lengths')
E.check(E.dot(E.rho,u)==12 and E.dot(u,u)==4, 'marked u')
E.check(E.dot(E.rho,p)==16, 'p original height')

# Independently reconstruct the original marked glue character, so no source
# metadata about beta(g_i), I, or u is substituted for exact membership checks.
C2=[((a^b^c,a^b,a^c,a),(b,c)) for a,b,c in product(range(2),repeat=3)]
C3=[((a+b)%3,(a+2*b)%3,a,b) for a,b in product(range(3),repeat=2)]
GLUE={(tuple((3*w[i]+2*z[i])%6 for i in range(4)),y):z[3]
      for w,y in C2 for z in C3}
DREPS={(0,0):(Q(0),)*4,(1,0):tuple(map(Q,(1,0,0,0))),
       (0,1):(Q(1,2),)*4,(1,1):(Q(-1,2),)+(Q(1,2),)*3}


def marked_class(X):
    t=[]
    for i in range(4):
        part=X[6*i:6*i+6]
        E.check(sum(part)==0 and all((a-part[0]).denominator==1 for a in part), 'A5 dual membership')
        a=-6*part[0]
        E.check(a.denominator==1, 'A5 discriminant class')
        t.append(int(a)%6)
    ys=[y for y,d in DREPS.items()
        if all(a.denominator==1 for a in E.sub(X[24:],d))
        and sum(E.sub(X[24:],d))%2==0]
    E.check(len(ys)==1, 'marked D4 dual class')
    return tuple(t),ys[0]


def beta(X):
    c=marked_class(X)
    E.check(c in GLUE, 'marked N glue membership')
    return GLUE[c]


E.check(len(GLUE)==72, 'original glue size')
E.check([beta(g) for g in E.G]==[0]*28+[1], 'all 29 beta values')
E.check(beta(u)==1, 'marked u beta')
E.check(all(beta(x)==0 and E.dot(E.rho,x)%6==0 for x in IG), 'every I generator')


def extended_gcd(a,b):
    old_r,r0=a,b
    old_s,s=1,0
    old_t,t=0,1
    while r0:
        z=old_r//r0
        old_r,r0=r0,old_r-z*r0
        old_s,s=s,old_s-z*s
        old_t,t=t,old_t-z*t
    if old_r<0:
        old_r,old_s,old_t=-old_r,-old_s,-old_t
    return old_r,old_s,old_t


def bezout_list(values):
    current=0
    coeff=[]
    for v in values:
        current,a,b=extended_gcd(current,v)
        coeff=[a*x for x in coeff]+[b]
    E.check(sum(a*b for a,b in zip(coeff,values))==current, 'Bezout exact equality')
    return current,coeff


def adjugate_from_columns(cols):
    a=[[cols[j][i] for j in range(3)] for i in range(3)]
    adj=[]
    for i in range(3):
        row=[]
        for j in range(3):
            rr=[k for k in range(3) if k!=j]
            cc=[k for k in range(3) if k!=i]
            row.append((-1)**(i+j)*(a[rr[0]][cc[0]]*a[rr[1]][cc[1]]-a[rr[0]][cc[1]]*a[rr[1]][cc[0]]))
        adj.append(row)
    d=E.det3(cols)
    E.check(all(sum(a[i][k]*adj[k][j] for k in range(3))==d*int(i==j)
                for i in range(3) for j in range(3)), 'integer adjugate identity')
    return adj


def value_group(name,gens):
    start=time.monotonic()
    finite=E.finite_value_generators(gens)
    den=[lcm(*(v[k].denominator for _,v in finite)) for k in range(3)]
    num=[reduce(gcd,(int(v[k]*den[k]) for _,v in finite)) for k in range(3)]
    units=[Q(num[k],den[k]) for k in range(3)]
    target={'J':(27,216,18),'M':(27,216,18),
            'N':(27,54,18),'Lambda':(27,216,54)}[name]
    E.check(units==[Q(1,d) for d in target], 'stated axis units '+name)
    cols=[tuple(int(v[k]/units[k]) for k in range(3)) for _,v in finite]
    E.check(all(v[k]/units[k]==cols[i][k] for i,(_,v) in enumerate(finite) for k in range(3)), 'exact integral coordinates '+name)
    # Literal small certificates. Neither normal-form metadata nor a lattice
    # index is used to infer the cubic group. All upper-bound coordinates and
    # all displayed determinants are recomputed from the Cayley coefficient map.
    if name in ('J','M'):
        selected=[('F(g4)','F(g27)','F(g30)'),
                  ('F(g4)','F(g30)','Dplus(2,27)'),
                  ('F(g2)','F(g28)','Dplus(11,21)')]
        expected=(-39859290,11531403,-43244032)
    elif name=='N':
        selected=[('F(g1)','F(g28)','Dplus(21,28)'),
                  ('F(g2)','F(g7)','Dplus(2,27)'),
                  ('F(g2)','Dplus(2,25)','Dplus(2,27)')]
        expected=(1792,-270,-1647)
    else:
        selected=[('F(g2)','F(g28)','F(g30)'),
                  ('F(g2)','F(g30)','Dplus(2,27)'),
                  ('F(g4)','F(g30)','Dplus(2,27)')]
        expected=(-5405504,2315394,1281267)
    lookup={label:i for i,(label,_) in enumerate(finite)}
    chosen=[tuple(lookup[s] for s in labels) for labels in selected]
    minors=[int(E.det3([cols[i] for i in ids])) for ids in chosen]
    E.check(tuple(minors)==expected,'displayed determinant certificate '+name)
    bezg,bez=bezout_list(minors)
    E.check(bezg==1, 'full three-axis span '+name)
    axis_witnesses=[{} for k in range(3)]
    for ids,b in zip(chosen,bez):
        adj=adjugate_from_columns([cols[i] for i in ids])
        for k in range(3):
            for j,i in enumerate(ids):
                label=finite[i][0]
                axis_witnesses[k][label]=axis_witnesses[k].get(label,0)+b*adj[j][k]
    for k,witness in enumerate(axis_witnesses):
        E.check(all(sum(c*cols[lookup[label]][j] for label,c in witness.items())==int(j==k)
                    for j in range(3)), 'explicit axis reconstruction '+name)
    result={
        'lattice_generator_count':len(gens),
        'finite_polarization_count':len(finite),
        'axis_units_1_sqrt2_sqrt3':[str(x) for x in units],
        'denominator_lcm_by_type':{
            prefix:[lcm(*(v[k].denominator for label,v in finite if label.startswith(prefix))) for k in range(3)]
            for prefix in ('F(','Dplus(','Dminus(','D3(')},
        'certificate':[
            {'labels':[finite[i][0] for i in ids],
             'columns':[list(cols[i]) for i in ids],
             'determinant':d,'bezout_coefficient':b}
            for ids,d,b in zip(chosen,minors,bez)],
        'integer_linear_combinations_for_three_axis_units':axis_witnesses,
        'elapsed_seconds':round(time.monotonic()-start,3)}
    expected_types={
        'J':[(27,216,1),(9,36,18),(9,36,18),(9,36,18)],
        'M':[(27,216,1),(9,36,18),(9,36,18),(9,36,18)],
        'N':[(27,27,1),(9,18,18),(9,18,18),(9,18,18)],
        'Lambda':[(27,216,27),(27,108,54),(27,108,54),(9,36,54)]}[name]
    E.check(list(result['denominator_lcm_by_type'].values())==[list(t) for t in expected_types], 'complete denominator table '+name)
    return result,finite


if __name__=='__main__':
    all_results={}
    for name,gens in [('J',JG),('M',MG),('N',E.G),('Lambda',E.LG)]:
        result,finite=value_group(name,gens)
        all_results[name]=result
        print(json.dumps({name:result}),flush=True)
    direct_cases=JG+MG+[u,p,q]
    for X in direct_cases:
        E.check(E.direct_cubic(X)==E.cubic(X)+(Q(0),), 'independent Cayley product at each new generator')
        E.check(E.cubic(r(X))==E.cubic(X), 'r invariance at each new generator')
    # Independent polynomial identity certificate on a real basis of the
    # original 24-dimensional space, not a probabilistic set of test points.
    full_direct_cases=list(E.root)
    for a,b in combinations(E.root,2):
        full_direct_cases.extend((E.add(a,b),E.sub(a,b)))
    full_direct_cases.extend(E.add(E.add(a,b),c) for a,b,c in combinations(E.root,3))
    E.check(len(full_direct_cases)==2600, 'complete real-basis polarization count')
    for X in full_direct_cases:
        E.check(E.direct_cubic(X)==E.cubic(X)+(Q(0),), 'complete direct Cayley polynomial certificate')
    # Exact inclusions use the coefficient bases, never ambient lattice indices.
    inclusion_N_to_JM=(1,4,1)
    inclusion_JM_to_Lambda=(1,1,3)
    for k in range(3):
        n=Q(all_results['N']['axis_units_1_sqrt2_sqrt3'][k])
        jm=Q(all_results['J']['axis_units_1_sqrt2_sqrt3'][k])
        la=Q(all_results['Lambda']['axis_units_1_sqrt2_sqrt3'][k])
        E.check(n==inclusion_N_to_JM[k]*jm and jm==inclusion_JM_to_Lambda[k]*la, 'exact inclusion coordinates')
    out={'status':'PASS','groups':all_results,
         'independent_direct_Cayley_Dickson_checks':len(direct_cases),
         'complete_real_basis_direct_polynomial_checks':len(full_direct_cases),
         'inclusion_N_to_J_equals_M_diagonal':list(inclusion_N_to_JM),
         'inclusion_J_equals_M_to_Lambda_diagonal':list(inclusion_JM_to_Lambda),
         'quotients':{'JM_over_N':'Z/4','Lambda_over_JM':'Z/3','Lambda_over_N':'Z/4 + Z/3','M_values_over_J_values':'0'},
         'extra_generator_values':{name:[str(x) for x in E.cubic(X)] for name,X in [('3v',E.scale(E.v,3)),('u',u),('p',p),('q',q)]}}
    dest=Path(__file__).with_name('EXACT_RESULTS.json')
    dest.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':'PASS','written':str(dest)}),flush=True)
