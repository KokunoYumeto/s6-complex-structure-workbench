#!/usr/bin/env python3
"""Exact fixed-source canonical-scalar catalogue for proposed P3F.53.

The source-factor list is read from K21.  Root branches come from the
proved local cap constructions, and the arithmetic is checked against
the actual page/line/Thom results K26 and K28.  This program does not
identify shorter scalar loops or loops varying the source.
"""
from pathlib import Path
from datetime import datetime, timezone
from itertools import product
from math import gcd
import json
import re
import sympy as S

ROOT = Path(__file__).resolve().parents[2]
INPUTS = {
    'source_reduction':'code/part3_fourfold/source_reduction.json',
    'one_cap':'code/part3/additive_returns.json',
    'joint_caps':'code/part3/joint_additive_returns.json',
}
data = {key:json.loads((ROOT/path).read_text()) for key,path in INPUTS.items()}
l,k = S.symbols('l k', integer=True, nonnegative=True)
fanS = S.symbols('S', integer=True)
LOC = {'l':l,'k':k,'S':fanS}
expr = lambda value:S.sympify(value,locals=LOC)
expanded = lambda value:S.expand(expr(value))
checks=[]

def check(label, condition):
    assert condition,label
    checks.append(label)

def eq(label, left, right):
    check(label,S.simplify(expr(left)-expr(right))==0)

def euler(fibre):
    if fibre in {'II':2,'III':3,'IV':4,'III*':9,'IV*':8}:
        return {'II':2,'III':3,'IV':4,'III*':9,'IV*':8}[fibre]
    found=re.fullmatch(r'I(\d+)(\*)?',fibre)
    if found:
        return int(found.group(1))+(6 if found.group(2) else 0)
    raise ValueError(fibre)

def parsed_profile(profile):
    result=[]
    for token in profile.split('+'):
        found=re.fullmatch(r'(\d+)(I.*)',token)
        count,fibre=(int(found.group(1)),found.group(2)) if found else (1,token)
        result.extend([fibre]*count)
    return result

def choice(fibre,kind,order,var=None,first=None,root_fibre=None,raw=None,extra=None):
    order=expanded(order)
    return dict(source_fibre=fibre,kind=kind,m=order,
                source_euler=0 if fibre is None else euler(fibre),
                root_fibre=root_fibre or 'I0',
                root_euler=0 if root_fibre in (None,'I0') else euler(root_fibre),
                bounds={} if var is None else {str(var):int(first)},
                local_progression=raw or str(order),
                extra_constraints=extra or [])

ABSENT=choice(None,'absent',1)

def root_choices(fibre,b,var,profile):
    if fibre=='III*':
        if b%2==0:
            return [choice(fibre,'good',4*var,var,1)]
        return [choice(fibre,'reduced III',4*var+3,var,0,'III')]
    if fibre=='IV*':
        if b%3==0:
            return [choice(fibre,'good',3*var,var,1)]
        return [choice(fibre,'reduced IV',3*var+2,var,0,'IV')]
    if fibre=='I1*':
        check(profile+' I1* actual translation residue',b%4==2)
        return [choice(fibre,'semistable I2',2,root_fibre='I2')]
    if fibre=='III':
        if b%2==0:
            return [choice(fibre,'good',4*var,var,1)]
        return [choice(fibre,'reduced III',4*var+1,var,0,'III')]
    if fibre=='IV':
        if b%3==0:
            constraints=['k odd'] if 'I1*' in profile else []
            return [choice(fibre,'good',3*var,var,1,extra=constraints)]
        if 'I1*' in profile:
            # The actual local progression is 3*j+1; gcd(2,m)=1
            # forces j even.  Keep both this arrow and its canonical form.
            return [choice(fibre,'reduced IV',6*l+1,l,0,'IV',
                           raw='3*j+1, j>=0',
                           extra=['j=2*l follows from gcd(2,3*j+1)=1'])]
        return [choice(fibre,'reduced IV',3*var+1,var,0,'IV')]
    if fibre=='II':
        return [choice(fibre,'reduced II',6*var+1,var,0,'II'),
                choice(fibre,'good',6*var,var,1)]
    raise ValueError((fibre,b,profile))

def extended_gcd(a,b):
    old_r,r=a,b
    old_s,s=1,0
    old_t,t=0,1
    while r:
        q=old_r//r
        old_r,r=r,old_r-q*r
        old_s,s=s,old_s-q*s
        old_t,t=t,old_t-q*t
    assert old_r==gcd(a,b)
    return old_r,old_s,old_t

def find_witness(caps):
    bounds={}
    for c in caps:
        bounds.update(c['bounds'])
    names=sorted(bounds)
    # This finite search only supplies a concrete witness.  The complete
    # parameter domain is the exact symbolic gcd condition, not this box.
    candidates=product(*(range(bounds[n],bounds[n]+25) for n in names))
    for values in candidates:
        sub={LOC[n]:v for n,v in zip(names,values)}
        mi,m0=[int(c['m'].subs(sub)) for c in caps]
        if mi<1 or m0<1 or gcd(mi,m0)!=1:
            continue
        if any('k odd' in c['extra_constraints'] for c in caps) and sub.get(k,1)%2!=1:
            continue
        number=sum(c['source_fibre'] is not None for c in caps)
        if number==0:
            ni=n0=0;NN=1
        elif number==1:
            ni=1;n0=0;NN=0
        else:
            dd,ni,n0=extended_gcd(m0,mi)
            assert dd==1
            NN=0
        assert m0*ni+mi*n0+mi*m0*NN==1
        assert gcd(mi,ni)==gcd(m0,n0)==1
        return dict(parameters={n:v for n,v in zip(names,values)},
                    m_infty=mi,m_0=m0,
                    positive=dict(n_infty=ni,n_0=n0,N=NN,D=1),
                    negative=dict(n_infty=-ni,n_0=-n0,N=-NN,D=-1),
                    local_norms_primitive=True)
    raise AssertionError(('No concrete coprime witness found',caps))

def serial_choice(c):
    return {name:(str(value) if isinstance(value,S.Basic) else value)
            for name,value in c.items()}

profiles=data['source_reduction']['source_profiles']
check('eight OS entries',len({r['os'] for r in profiles})==8)
check('twenty-one source configurations',len(profiles)==21)
retained=[r for r in profiles if r['remaining_pairs']]
check('sixteen retained profiles',len(retained)==16)
check('twenty-six retained source pairs',
      sum(len(r['remaining_pairs']) for r in retained)==26)

rows=[]
for pidx,source in enumerate(profiles,1):
    fibres=parsed_profile(source['profile'])
    check(source['profile']+' Euler number 12',sum(map(euler,fibres))==12)
    if not source['remaining_pairs']:
        continue
    sites=[f for f in fibres if f in {'III*','IV*','I1*','II','III','IV'}]
    check(source['profile']+' at most two additive sites',len(sites)<=2)
    sites.sort(key=lambda f:0 if '*' in f else 1)
    for a,b in source['remaining_pairs']:
        d=source['height_denominator']
        check(source['profile']+str((a,b))+' ab=d',a*b==d)
        opts=[root_choices(sites[0],b,l,source['profile'])] if sites else [[ABSENT]]
        opts.append(root_choices(sites[1],b,k,source['profile']) if len(sites)==2 else [ABSENT])
        for capi,cap0 in product(*opts):
            caps=(capi,cap0);mi,m0=capi['m'],cap0['m']
            M=S.expand(mi*m0)
            ei,e0=capi['source_euler'],cap0['source_euler']
            eri,er0=capi['root_euler'],cap0['root_euler']
            chi=S.expand((M*(12-ei-e0)+m0*eri+mi*er0)/12)
            H=S.expand(M*S.Rational(a*a,d))
            AA=S.expand(chi-H/2)
            AF=S.expand(chi*(4-3*fanS)+H*(3*fanS**2-7)/8)
            label=f"OS{source['os']} {source['profile']} (a,b)=({a},{b}): {capi['kind']} / {cap0['kind']}"
            excluded=(sites==['III*','II'] and capi['kind']=='good' and cap0['kind']=='good')
            # Every polynomial below is derived from the displayed root
            # Euler counts, rather than copied from a previous return row.
            check(label+' chi integral polynomial',S.Poly(chi,l,k).domain.is_ZZ)
            check(label+' H/2 integral polynomial',S.Poly(H/2,l,k).domain.is_ZZ)
            check(label+' b divides M',S.Poly(S.expand(M/b),l,k).domain.is_ZZ)
            eq(label+' initial fan equals A',AF.subs(fanS,1),AA)
            eq(label+' Jin transfer identity',4*(-3*H)-(-24*chi),24*AA)
            row=dict(id=f'CS{len(rows)+1:02}',os=source['os'],profile=source['profile'],
                     d=d,a=a,b=b,cap_infty=serial_choice(capi),cap_0=serial_choice(cap0),
                     m_infty=str(mi),m_0=str(m0),M=str(M),M_over_b=str(S.expand(M/b)),
                     bounds={**capi['bounds'],**cap0['bounds']},
                     source_euler=[ei,e0],root_euler=[eri,er0],
                     domain_constraints=['gcd(m_infty,m_0)=1']+
                         capi['extra_constraints']+cap0['extra_constraints'],
                     sphere_equation='D=m_0*n_infty+m_infty*n_0+M*(sum_j n_j-b_0)=epsilon, epsilon=+1 or -1',
                     additional_effective_orders='Every other logarithmic site has order one.',
                     chi=str(chi),H=str(H),line_square=str(-H),A=str(AA),
                     all_fan=str(AF),fan_coordinate='S=a_fan^2-a_fan*b_fan+b_fan^2, gcd(a_fan,b_fan)=1',
                     jin_pair=dict(k=str(-3*H),ell=str(-24*chi)),
                     relative_pair=[str(6*chi),str(S.expand(3*H-6*chi))],
                     parameter='lambda=r^M; one positive r-loop',
                     status='excluded_by_sphere_determinant' if excluded else 'proved_canonical_scalar_branch')
            if excluded:
                eq(label+' exact factor two in D',
                   6*k*S.Symbol('ni')+4*l*S.Symbol('n0')+24*k*l*S.Symbol('N'),
                   2*(3*k*S.Symbol('ni')+2*l*S.Symbol('n0')+12*k*l*S.Symbol('N')))
                row.update(exclusion='Both orders are even, hence D is even for every integral norm and every order-one total. It cannot equal ±1.',
                           common_divisor=2,
                           characteristic_scope='Displayed chi/H/A are formal arithmetic only; no sphere or actual Theta7 return is assigned.',
                           actual_return=None)
            else:
                row['witness']=find_witness(caps)
                vv={LOC[n]:v for n,v in row['witness']['parameters'].items()}
                row['witness']['chi']=int(chi.subs(vv))
                row['witness']['H']=int(H.subs(vv))
                row['witness']['A']=int(AA.subs(vv))
                row['witness']['class_mod28']=int(AA.subs(vv))%28
                number=len(sites)
                if number==2:
                    row['all_norm_solutions']='Choose u,v with m_0*u+m_infty*v=1. For every N=sum_j n_j-b_0 and j in Z, n_infty=epsilon*u+m_infty*j and n_0=epsilon*v-m_0*(j+N).'
                elif number==1:
                    row['all_norm_solutions']='n_infty=epsilon-m_infty*(n_0+N), with arbitrary n_0,N in Z and N=sum_j n_j-b_0. The regular order-one slot retains its actual n_0.'
                else:
                    row['all_norm_solutions']='n_infty=epsilon-n_0-N, with arbitrary n_0,N in Z and N=sum_j n_j-b_0. Equivalently n_infty+n_0+N=epsilon; both regular order-one norms are retained.'
            rows.append(row)

check('thirty-one explicit root branches',len(rows)==31)
accepted=[r for r in rows if r['status']=='proved_canonical_scalar_branch']
rejected=[r for r in rows if r['status']=='excluded_by_sphere_determinant']
check('thirty nonempty sphere root branches',len(accepted)==30)
check('one entire gcd-rejected root branch',len(rejected)==1)
check('all twenty-six pairs have an actual witness',
      len({(r['profile'],r['a'],r['b']) for r in accepted})==26)

# Exact general Bezout parametrization, with no bounded search in the
# completeness assertion.
mi,m0,ni,n0,NN,jj,eps,uu,vv=S.symbols('mi m0 ni n0 N j epsilon u v')
normD=m0*(eps*uu+mi*jj)+mi*(eps*vv-m0*(jj+NN))+mi*m0*NN
eq('all integral two-cap norm solutions retain D',
   normD,eps*(m0*uu+mi*vv))
eq('full one-additive-site norm solution retains D',
   (eps-mi*(n0+NN))+mi*n0+mi*NN,eps)
eq('full zero-additive-site norm solution retains D',
   (eps-n0-NN)+n0+NN,eps)
check('every absent cap meridian has order one',
      all(c['m']=='1' for r in rows for c in (r['cap_infty'],r['cap_0'])
          if c['source_fibre'] is None))

# Independently match every proved one-cap polynomial to all compatible
# profiles.  In a two-site source the other reduced root is literally
# order one, achieved by setting its index to zero.
one_checks=[]
for old in data['one_cap']['cases']:
    hits=[]
    om=expr(old['m'])
    for row in accepted:
        if (row['d'],row['a'],row['b'])!=(old['d'],old['a'],old['b']):
            continue
        if row['cap_infty']['source_euler']!=old['source_euler']:
            continue
        if row['cap_infty']['root_euler']!=old['root_euler']:
            continue
        sub={}
        if row['cap_0']['source_fibre'] is not None:
            if row['cap_0']['kind'].startswith('reduced') and expr(row['m_0']).subs(k,0)==1:
                sub={k:0}
            else:
                continue
        if S.simplify(expr(row['m_infty']).subs(sub)-om)!=0:
            continue
        for key,oldkey in [('chi','chi'),('H','height'),('A','actual_positive_return')]:
            eq(old['label']+' -> '+row['id']+' '+key,expr(row[key]).subs(sub),old[oldkey])
        hits.append(dict(catalogue_id=row['id'],substitution={str(a):str(b) for a,b in sub.items()}))
    check(old['label']+' has exact catalogue match',len(hits)>0)
    one_checks.append(dict(prior_label=old['label'],matches=hits))

joint_checks=[]
for old in data['joint_caps']['rows']:
    hits=[r for r in accepted if
          (r['d'],r['a'],r['b'])==(old['d'],old['a'],old['b'])
          and S.simplify(expr(r['m_infty'])-expr(old['m_infty']))==0
          and S.simplify(expr(r['m_0'])-expr(old['m_0']))==0
          and r['root_euler']==[old['root_euler_infty'],old['root_euler_0']]]
    check(old['label']+' unique exact branch match',len(hits)==1)
    row=hits[0]
    for key,oldkey in [('chi','chi'),('H','height'),('A','actual_A'),('M','page_degree')]:
        eq(old['label']+' '+key,row[key],old[oldkey])
    joint_checks.append(dict(prior_label=old['label'],catalogue_id=row['id']))

one_star=[]
for profile in data['joint_caps']['one_star']['profiles']:
    hits=[r for r in accepted if r['profile']==profile and (r['a'],r['b'])==(6,2)
          and r['cap_infty']['source_fibre']=='I1*']
    check(profile+' one-star branch exists',len(hits)==1)
    row=hits[0]
    sub={l:0} if row['cap_0']['source_fibre'] is not None else {}
    for key,want in [('chi',1),('H',6),('A',-2),('M',2)]:
        eq(profile+' one-star '+key,expr(row[key]).subs(sub),want)
    one_star.append(dict(profile=profile,catalogue_id=row['id'],substitution={str(a):str(b) for a,b in sub.items()}))

primitive_checks=[]
for source in retained:
    if [source['height_denominator'],1] not in source['remaining_pairs']:
        continue
    if any('*' in f for f in parsed_profile(source['profile'])):
        continue
    hits=[r for r in accepted if r['profile']==source['profile'] and r['b']==1
          and (r['cap_infty']['kind']=='absent' or r['cap_infty']['kind'].startswith('reduced'))]
    check(source['profile']+' unique order-one representative',len(hits)==1)
    row=hits[0];sub={l:0}
    eq(source['profile']+' primitive chi',expr(row['chi']).subs(sub),1)
    eq(source['profile']+' primitive height',expr(row['H']).subs(sub),source['height_denominator'])
    eq(source['profile']+' primitive return',expr(row['A']).subs(sub),
       1-S.Rational(source['height_denominator'],2))
    primitive_checks.append(row['id'])
check('ten K22 primitive profile crosschecks',len(primitive_checks)==10)

# H is even.  For primitive fan coefficients S is odd, and the exact
# expression (3*S^2-7)/4 is integral.  Substitute S=2z+1 to certify it.
zz=S.symbols('z',integer=True)
check('all-fan integer factor for every odd S',
      S.Poly(S.expand((3*(2*zz+1)**2-7)/4),zz).domain.is_ZZ)
for row in accepted:
    eq(row['id']+' all-fan symmetry at S=1 and S=3',
       expr(row['all_fan']).subs(fanS,3),-5*expr(row['chi'])+S.Rational(5,2)*expr(row['H']))

out=dict(status='PASS',timestamp_utc=datetime.now(timezone.utc).isoformat(),
         inputs=INPUTS,scope='All fixed-source canonical scalar loops lambda=r^M in the proved whole-zero-I1 MW=Z sector. No shorter-loop descent or source-moduli-loop identification.',
         source_profile_count=21,os_entry_count=8,retained_profile_count=16,
         retained_source_pair_count=26,root_branch_count=31,
         nonempty_root_branch_count=30,entirely_rejected_branch_count=1,
         generic_equations={
             'M':'m_infty*m_0',
             'N':'sum_j n_j-b_0',
             'D':'m_0*n_infty+m_infty*n_0+M*N=epsilon, epsilon=+1 or -1',
             'chi':'[M*(12-e_infty-e_0)+m_0*e_infty_root+m_infty*e_0_root]/12',
             'H':'M*a^2/d','A':'chi-H/2',
             'all_fan':'chi*(4-3*S)+H*(3*S^2-7)/8',
             'fan_S':'a_fan^2-a_fan*b_fan+b_fan^2 for a primitive pair',
             'actual_parameter':'one positive r-loop, lambda=r^M'},
         absent_slot_convention='An absent additive site is a regular order-one slot, m_i=1 and source/root Euler zero. Its actual integral norm is retained in the all-solutions field; setting it to zero is used only for the displayed witness.',
         local_root_exclusions={
             'II':'Only residues 0,1 mod6 survive: intermediate IV root cannot be made transitive by the actual fixed identity limit; nonreduced roots are excluded by K19/F43.',
             'III':'Reduced 1 mod4 requires b odd; good 0 mod4 requires b even. Other roots or complementary norms fail the actual component/norm tests.',
             'IV':'Reduced 1 mod3 requires 3 not dividing b; good 0 mod3 requires 3 dividing b.',
             'III*':'Reduced 3 mod4 requires b odd; good 0 mod4 requires b even.',
             'IV*':'Reduced 2 mod3 requires 3 not dividing b; good 0 mod3 requires 3 dividing b.',
             'I1*':'The primitive sphere cap is quadratic with I2 root, b=2 mod4 and odd norm.',
             'smooth_and_multiplicative':'Every additional effective order is one by the actual integral H2 obstruction.'},
         discarded_profiles=[r for r in profiles if not r['remaining_pairs']],
         branches=rows,crosschecks=dict(K26=one_checks,K28=joint_checks,
                                      F36_one_star=one_star,K22_primitive=primitive_checks),
         checks=checks)
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
for row in rows:
    state='EXCLUDED' if row['status'].startswith('excluded') else 'PROVED'
    print(row['id'],state,row['profile'],f"(a,b)=({row['a']},{row['b']})",
          'm=',row['m_infty'],',',row['m_0'],
          'chi=',row['chi'],'H=',row['H'],'A=',row['A'])
print('PASS:',len(checks),'exact checks;',
      '8 entries, 21 configurations, 16 retained profiles, 26 pairs,',
      '31 root branches, 30 nonempty and one gcd-excluded.')
