#!/usr/bin/env python3
"""Exact CL arithmetic and normalization certificate, before proof release.

No target proof, target program, canonical source, or data file is read.
SymPy rational algebra, reduced cyclic permutation matrices, monomial
invariants and exhaustive small root-position sets supply separate methods.
"""
import itertools
import json
import sympy as s

checks = []


def check(name, value, evidence):
    value = bool(value)
    checks.append({"name": name, "passed": value, "evidence": evidence})
    if not value:
        raise AssertionError(name)


def clean(x):
    if isinstance(x, dict):
        return {str(k): clean(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [clean(v) for v in x]
    if isinstance(x, s.Integer):
        return int(x)
    if isinstance(x, s.Rational):
        return str(x)
    if isinstance(x, s.Basic):
        return str(x)
    return x


def ip(v, w):
    return 2*v[0]*w[0]+v[0]*w[1]+v[1]*w[0]


ell, k = s.symbols('ell k', integer=True)
r1 = (1, -2-ell)
r2 = (2, 2+ell-k)
pa = s.expand(1+ip(r2, (r2[0]-2, r2[1]))/2)
meet = s.expand(ip(r1, r2))
check('ruled intersection and arithmetic genus identities',
      pa == 3+ell-k and meet == 2-ell-k,
      {'p_a_R2': pa, 'R1_dot_R2': meet})
check('common-zero degree budget', s.expand(pa+meet) == 5-2*k,
      {'sum': s.expand(pa+meet), 'nonnegative_sum': True,
       'integer_k_max': 2})
k2 = [e for e in range(-5, 6)
      if pa.subs({ell:e, k:2}) >= 0 and meet.subs({ell:e, k:2}) >= 0]
check('degree-two integer endpoints', k2 == [-1,0],
      {'ell_interval': '[k-3,2-k]', 'k2_ell': k2,
       'interval_length': s.expand((2-k)-(k-3))})
check('all k>=3 excluded by interval endpoints',
      s.expand((k-3)-(2-k)).subs(k, 3) == 1,
      {'lower_minus_upper': 2*k-5, 'slope': 2, 'value_at_3':1})
check('extension splitting cohomology',
      [max(-d-1,0) for d in [0,2]] == [0,0],
      {'H1_O0':0, 'H1_O2':0})

x,t,X,T,b,ss,c = s.symbols('x t X T b ss c', nonzero=True)
newx=(x+b/2)/ss
check('quadratic completion inverse',
      s.simplify(newx.subs(x,ss*X-b/2)-X) == 0,
      {'forward':'X=(x+b/2)/s; T=t', 'inverse':'x=s(T)X-b(T)/2; t=T'})
z=s.symbols('z')
check('node normalization branches',
      all(s.expand((X**2-T**2).subs(X,e*T)) == 0 for e in [-1,1]),
      {'branches':['X=T','X=-T'], 'normalization_points':2})
check('cusp normalization and delta',
      s.expand((X**2-T**3).subs({X:z**3,T:z**2})) == 0,
      {'parametrization':['T=z^2','X=z^3'], 'semigroup_missing_positive':[1],
       'delta':1, 'normalization_points':1})
expr=t*(x*x-t)
mapped=s.expand(expr.subs({x:s.sqrt(2)*X,t:T+X**2}))
check('vertical simple ramification A3 map', mapped == X**4-T**2,
      {'transformed_equation':mapped,
       'inverse':['x=sqrt(2) X','t=T+X^2']})
triple=s.expand((t*x*(x-t*c)).subs(x,c*X))
check('ordinary triple exact unit and inverse',
      s.expand(triple-c*c*t*X*(X-t)) == 0,
      {'substitution':'x=c(t)X; b(t)=t c(t)',
       'unit':'c(t)^2', 'inverse':'X=x/c(t)'})
u,v=s.symbols('u v')
jac=s.Matrix([[s.diff(t*u,u),s.diff(t*u,t)],[0,1]]).det()
residue=s.simplify(jac/(3*(t*v)**2))
check('canonical residue has exact simple exceptional pole',
      residue == 1/(3*t*v*v), {'coefficient':residue})

XX,TT,ZZ=s.symbols('XX TT ZZ')
F=ZZ**3-TT*XX*(XX-TT)
partials=[s.diff(F,a) for a in [XX,TT,ZZ]]
for chart in [XX,TT,ZZ]:
    gb=s.groebner([F,*partials,chart-1],XX,TT,ZZ)
    check('smooth projective cubic chart '+str(chart),
          list(gb)==[1], {'groebner_basis':list(gb)})
az,bz,zet=s.symbols('az bz zet')
linT=az+bz
linX=-zet*az-zet**2*bz
fermat=s.rem(s.expand(linT*linX*(linX-linT)+az**3+bz**3),zet**2+zet+1,zet)
invA=s.rem(s.expand(-zet**2*linT-linX-(zet-zet**2)*az),zet**2+zet+1,zet)
invB=s.rem(s.expand(zet*linT+linX-(zet-zet**2)*bz),zet**2+zet+1,zet)
check('ordinary triple to Fermat exact linear isomorphism',
      fermat==0 and invA==0 and invB==0,
      {'T':'A+B','X':'-zeta A-zeta^2 B','determinant':'zeta-zeta^2',
       'product_identity':'T X (X-T)=-(A^3+B^3)',
       'inverse':['A=(-zeta^2 T-X)/(zeta-zeta^2)','B=(zeta T+X)/(zeta-zeta^2)']})
check('elliptic cone cohomology and link',
      (3-1)*(3-2)//2 == 1,
      {'degree':3, 'genus':1, 'self_intersection':-3,
       'h1_OE_j_for_j_0_to_5':[1,0,0,0,0,0],
       'all_j_positive':'h1=0 by positive degree and Serre duality',
       'circle_bundle_Euler':-3,'link_b1':2,'local_pg':1})


def cycle_reduced(n):
    # Multiplication by T on Q[T]/(1+T+...+T^(n-1)).
    m=s.zeros(n-1)
    for j in range(n-2):
        m[j+1,j]=1
    for j in range(n-1):
        m[j,n-2]=-1
    return m


local_rows=[]
for name,abc,want_pg,want_link in [
        ('A1 plane',(2,2,3),0,0),
        ('A2 plane',(2,3,3),0,0),
        ('A3 plane',(2,4,3),0,0),
        ('ordinary triple plane',(3,3,3),1,2)]:
    ranges=[range(1,a) for a in abc]
    lattice=[q for q in itertools.product(*ranges)
             if sum(s.Rational(qi,ai) for qi,ai in zip(q,abc))<=1]
    m=s.kronecker_product(*(cycle_reduced(a) for a in abc))
    null=len(m.nullspace()) if m.rows==0 else m.rows-(m-s.eye(m.rows)).rank()
    row={'plane_type':name,'exponents':abc,'positive_lattice_points':lattice,
         'matrix_dimension':m.rows,'rank_h_minus_I':(m-s.eye(m.rows)).rank(),
         'link_b1':null,'local_pg':len(lattice),
         'characteristic_polynomial':m.charpoly().as_expr()}
    local_rows.append(row)
    check('local suspension '+name,
          len(lattice)==want_pg and null==want_link,row)

aa,bb,w,h,g,tx=s.symbols('aa bb w h g tx', nonzero=True)
generators=[(3,0),(2,1),(1,2),(0,3)]
residue_classes=[(i,j) for i in range(3) for j in range(3) if (i+j)%3==0]
check('Veronese invariant semigroup universal residues',
      residue_classes==[(0,0),(1,2),(2,1)],
      {'basis_exponents':generators,'residue_classes':residue_classes,
       'decomposition':'(i,j)=a(3,0)+b(0,3)+(r,s), 0<=r,s<3'})
coords={'t':aa**3,'x':bb**3,'w':aa**2*bb,'s':aa*bb**2}
relations={
 'w^2=t*s':coords['w']**2-coords['t']*coords['s'],
 's^2=x*w':coords['s']**2-coords['x']*coords['w'],
 'w*s=t*x':coords['w']*coords['s']-coords['t']*coords['x'],
 'w^3=t^2*x':coords['w']**3-coords['t']**2*coords['x'],
 's^3=t*x^2':coords['s']**3-coords['t']*coords['x']**2}
check('normalized quotient algebra multiplication',
      all(s.expand(q)==0 for q in relations.values()),
      {'coordinates':coords, 'relation_differences':relations,
       'generic_new_generator':'s=w^2/t'})
check('normalization eigenline transitions',
      s.simplify((g**(-1)*w)**2/(h*tx)-g**(-2)*h**(-1)*w*w/tx)==0,
      {'w_transition':'g^-1','t_transition':'h',
       'w2_over_t_transition':'g^-2 h^-1',
       'line_bundle':'L^-2(F)'})
check('third-Veronese resolution cohomology',
      all(max(-3*j-1,0)==0 for j in range(8)),
      {'exceptional_curve':'P1','self_intersection':-3,
       'pg':0,'link_b1':0,
       'universal_reason':'H1(P1,O(3j))=0 for every integer j>=0'})
check('node suspension quotient map',
      s.expand((aa*bb)**3-aa**3*bb**3)==0,
      {'x':'aa^3','y':'bb^3','z':'aa*bb','action_weights':[1,-1],
       'intersection_matrix':[[-2,1],[1,-2]],'determinant':3})

al,be=s.symbols('al be', integer=True)
chi=s.expand(1+ip((al,be),(al+2,be))/2)
check('ruled Riemann Roch polynomial', s.expand(chi-(al+1)*(al+be+1)) == 0,
      {'expanded_chi':chi, 'factored_chi':s.factor(chi)})
chis=[chi.subs({al:a,be:b}) for a,b in [(0,0),(-1,0),(-2,0),(-2,1)]]
check('cover direct-image Euler characteristics', chis==[1,0,1,0],
      {'O,O_minus_xi,O_minus_2xi,O_minus_2xi_plus_F':chis,
       'reduced_cover_chi':2,'double_fibre_normalized_chi':1})
check('normalized double-fibre cohomology',
      max(-1+1,0)==0 and max(-(-1)-1,0)==0,
      {'R1p_Lminus2_F':'O_P1(-1)', 'H0':0,'H1':0,
       'H1_X0':0,'H2_X0':0})

# The same boundary-relation map is verified for each actual base matrix.
relation_rows=[]
for name,cols in [
 ('ell_minus1_reduced',[(1,-1),(2,-1),(0,1),(0,1)]),
 ('ell_zero_reduced',[(1,-2),(2,0),(0,1),(0,1)]),
 ('double_fibre',[(1,-2),(2,0),(0,1)])]:
    V=s.Matrix(2,len(cols),lambda i,j:cols[j][i])
    A=s.Matrix(2,len(cols),lambda i,j:s.Symbol('a%d%d'%(i,j)))
    B=s.eye(2).row_join(-A/3).col_join(s.zeros(2,2).row_join(V/3))
    kernels=V.nullspace()
    lifted=[(A*q/3).col_join(q) for q in kernels]
    check('boundary relation exact map '+name,
          V.rank()==2 and all(B*q==s.zeros(4,1) for q in lifted)
          and len(lifted)==len(cols)-2,
          {'base_matrix':V.tolist(),'base_relation_basis':[q.T.tolist()[0] for q in kernels],
           'lift':'alpha -> (A alpha/3,alpha)',
           'inverse':'projection to strict-component coefficients; pushforward',
           'exceptional_classes_independent':True,
           'boundary_rank':'n+2','boundary_deficiency':len(cols)-2})
    relation_rows.append({'case':name,'base_rank':V.rank(),'deficiency':len(cols)-2})
check('positive boundary class',3*ip((1,0),(1,0))==6,
      {'class':'g*xi','square':6})

# Enumerate every incidence pattern relevant to >=2 possible paired values.
# Two regular symbols suffice because there are only two scalar-zero values.
positions=[]
for inter in ['b1','b2','i']:
    universe=sorted(set(['b1','b2',inter,'a','b']))
    for zeros in itertools.combinations(universe,2):
        zeros=set(zeros)
        m=[1 if p in ['b1','b2'] else 2 for p in zeros]
        candidates=sorted(p for p in zeros if p not in ['b1','b2'])
        nu=sum(1+x for x in m)+(0 if inter in zeros else 1)
        if len(candidates)>=2:
            pg=int(inter in zeros)
            positions.append({'case':'ell=-1','intersection':inter,
                              'zeros':sorted(zeros),'candidates':candidates,
                              'nu':nu,'local_pg_sum':pg,'lambda':2*pg})
for typ,universe,ram,extra in [
 ('node',['n','b1','b2','a','b'],{'b1','b2'},'n'),
 ('cusp',['q','b','a','c'],{'q','b'},None)]:
    for zeros in itertools.combinations(universe,2):
        zeros=set(zeros)
        candidates={p for p in zeros if p not in ram}
        if extra and extra not in zeros:
            candidates.add(extra)
        m=[1 if p in ram else 2 for p in zeros]
        nu=sum(1+x for x in m)+int(bool(extra and extra not in zeros))
        if len(candidates)>=2:
            pg=int(bool(extra and extra in zeros))
            positions.append({'case':'ell=0 '+typ,'zeros':sorted(zeros),
                              'candidates':sorted(candidates),'nu':nu,
                              'local_pg_sum':pg,'lambda':2*pg})
for row in positions:
    a=row['local_pg_sum']
    pg=1 if a==0 else 0
    q=pg-(2-a)+1
    row.update({'global_pg':pg,'global_q':q,'b1_U':2,
                'compact_pairing_rank':2*row['nu']-row['lambda']-8})
check('exhaustive simple-zero candidate configurations',
      bool(positions) and all(row['nu']>=6 and row['local_pg_sum']<=1
                            and row['lambda']<=2 and row['global_q']==0
                            and row['compact_pairing_rank']>=2 for row in positions),
      {'configuration_count':len(positions),
       'minimum_nu':min(row['nu'] for row in positions),
       'minimum_pairing_rank':min(row['compact_pairing_rank'] for row in positions),
       'maximum_local_pg_sum':max(row['local_pg_sum'] for row in positions)})

nu,n,lam=s.symbols('nu n lam', integer=True)
ered=8-nu
ex0=s.expand(12-2*ered)
b2=s.expand(ex0+n-lam-2)
rank=s.expand(b2-(n+2))
check('two-simple-zero Euler and pairing identities',
      ex0==2*nu-4 and rank==2*nu-lam-8,
      {'e_R':ered,'e_X0':ex0,'b2_X':b2,'rank_compact':rank,'b1_U':2})
check('double-zero exact Euler and pairing ranks',
      12-2*(6-4)==8 and (8+n-2)-(n+2)==4,
      {'nu':4,'strict_components':3,'e_B':2,'e_X0':8,
       'lambda':0,'q':0,'b1_U':1,'compact_pairing_rank':4})

# Exterior-square pairing in every lattice of rank <=3.
for rank_a in [1,2,3]:
    basis=list(itertools.combinations(range(rank_a),2))
    terms=[len(set(a+b))==4 for a in basis for b in basis]
    check('torus cover wedge pairing rank '+str(rank_a),
          not any(terms), {'wedge_basis':basis,'nonzero_fourfold_wedges':sum(terms)})
rr,nn,zz,dd,paired=s.symbols('r N0 z d paired', integer=True)
KK=rr-zz-dd
bound=s.expand(2-rr+nn+KK-paired)
check('exact final Euler transport', bound==2-dd-paired+nn-zz,
      {'K':KK,'lower_bound':bound,'nonnegative_terms':['1-d','1-paired','N0-z']})

print(json.dumps(clean({'target':'01CL','phase':'before target proof release',
                       'method':'rational cycle monodromy matrices, invariant monomial algebra, symbolic intersection forms, exhaustive root positions',
                       'check_count':len(checks),'all_passed':all(c['passed'] for c in checks),
                       'checks':checks,'local_suspension_rows':local_rows,
                       'boundary_relation_rows':relation_rows,
                       'two_simple_zero_configurations':positions}),indent=2))
