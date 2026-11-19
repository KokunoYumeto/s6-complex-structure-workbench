#!/usr/bin/env python3
"""Fresh P1A.2 calculation from Gamma6, line weights and Kuhn charts.

No P1A.2 proof or producing code was opened. t denotes pi*c; admissible
parameters satisfy c>1 by P1.16 and P1.8, so t>3.
"""
from pathlib import Path
from itertools import combinations
import sympy as S
import json

t=S.symbols('t',real=True)
lam=S.Rational(-256,3125)
r=S.Rational(625,96)*t
aa=-S.Rational(78125,6)+300*r
bb=-S.Rational(390625,48)-375*r
K=S.Matrix([[aa,bb,0],[120,0,S.Rational(125,2)],[0,120,50]])/3125
fw=[2,1,0];gw=[0,-1,-2]
def subs(n,k):return list(combinations(range(n),k)) if 0<=k<=n else []
def weight(a,w):return sum(w[i] for i in a)
def degree(n):return (4*n)//5+(-3*n)//4
def to_json_matrix(M):return [[str(S.factor(x)) for x in row] for row in M.tolist()]
out={'method':'Fresh exact exterior connecting maps and cusp residue evaluation','old_target_proof_or_code_opened':False,'parameter':'t=pi*c>3','line_degrees':{str(n):degree(n) for n in range(-3,15)},'logarithmic':{},'residue':{}}

# The global-section connecting maps. All relevant H1 on the root base
# vanish. B has a section precisely in total weight0; A precisely when
# the displayed coarse degree equals0. Their canonical monomials are
# lambda^ceil(3n/4), so the K entries below are exact constants.
for p in (1,2,3):
    Adims=[];Bdims=[];ranks=[];maps=[]
    for q in range(4):
        src=[(f,g) for f in subs(3,p) for g in subs(3,q) if weight(f,fw)+weight(g,gw)==0]
        dst=[(f,g) for f in subs(3,p-1) for g in subs(3,q+1) if degree(11+weight(f,fw)+weight(g,gw))==0]
        aa_basis=[(f,g) for f in subs(3,p-1) for g in subs(3,q) if degree(11+weight(f,fw)+weight(g,gw))==0]
        Adims.append(len(aa_basis));Bdims.append(len(src))
        M=S.zeros(len(dst),len(src));didx={v:k for k,v in enumerate(dst)}
        for col,(fs,gs) in enumerate(src):
            for j,f in enumerate(fs):
                rem=fs[:j]+fs[j+1:]
                for g in range(3):
                    if g in gs:continue
                    target=(rem,tuple(sorted(gs+(g,))))
                    coeff=(-1)**(j+sum(k<g for k in gs))*K[g,f]
                    if target in didx:M[didx[target],col]+=coeff
                    else:assert S.simplify(coeff)==0
        rank=M.rank();ranks.append(rank)
        minors=[]
        if rank:
            for ri in combinations(range(M.rows),rank):
                for ci in combinations(range(M.cols),rank):
                    d=S.factor(M.extract(ri,ci).det())
                    if d!=0:minors.append(d)
            gcd=S.factor(S.polys.polytools.terms_gcd(S.gcd_list(minors)))
            roots=S.solve(gcd,t)
            assert all(v.is_real is False or v<3 for v in roots),(p,q,roots)
        else:gcd=S.Integer(0);roots=[]
        maps.append({'q':q,'source_basis':src,'target_basis':dst,'matrix':to_json_matrix(M),'rank_for_t_gt_3':rank,'maximal_minor_gcd':str(gcd),'possible_rank_drop_values':[str(z) for z in roots]})
    dims=[Adims[q]-(ranks[q-1] if q else 0)+Bdims[q]-ranks[q] for q in range(4)]+[0]
    out['logarithmic'][str(p)]={'A_dimensions':Adims,'B_dimensions':Bdims,'connecting_ranks':ranks,'cohomology_dimensions':dims,'maps':maps}

# Residue on the seven edge orbits is the symmetric product of a toric
# logarithmic covector and a period-deck character. The actual cusp
# residue Q identifies these two three-dimensional spaces.
Q=S.Matrix([[aa/lam**2,bb/lam,0],[120/lam**3,0,S.Rational(125,2)/lam],[0,120/lam**3,50/lam**2]])/3125
assert Q.det()!=0
out['residue']['cusp_Q']=to_json_matrix(Q)
out['residue']['cusp_Q_determinant']=str(S.factor(Q.det()))
Qinv=Q.inv()
section_basis=[];symcols=[]
for fi in range(3):
    for gi in range(3):
        n=11+fw[fi]+gw[gi]
        if degree(n)!=0:continue
        exponent=(3*n+3)//4-9
        T=S.zeros(3);T[fi,gi]=lam**exponent
        U=T*Qinv.T
        symcols.append(S.Matrix([U[0,0],U[1,1],U[2,2],U[0,1]+U[1,0],U[0,2]+U[2,0],U[1,2]+U[2,1]]))
        section_basis.append({'f_index':fi,'g_index':gi,'weight':n,'lambda_exponent':exponent})
Sym=S.Matrix.hstack(*symcols)
symdet=S.factor(Sym.det())
assert Sym.shape==(6,6) and symdet!=0
symroots=S.solve(symdet,t)
assert all(x.is_real is False or x<3 for x in symroots)
out['residue']['H1_log_two_form_section_basis']=section_basis
out['residue']['symmetrization_matrix']=to_json_matrix(Sym)
out['residue']['symmetrization_determinant']=str(symdet)
out['residue']['possible_symmetrization_rank_drops']=[str(z) for z in symroots]
edges=[S.Matrix(v) for v in [(1,0,0),(0,1,0),(0,0,1),(1,1,0),(1,0,1),(0,1,1),(1,1,1)]]
Eval=S.Matrix([[v[0]**2,v[1]**2,v[2]**2,v[0]*v[1],v[0]*v[2],v[1]*v[2]] for v in edges])
assert Eval.rank()==6
out['residue']['quadratic_evaluation_matrix']=to_json_matrix(Eval)
out['residue']['quadratic_evaluation_rank']=6
out['residue']['quadratic_evaluation_cokernel_relation']=[str(z) for z in Eval.T.nullspace()[0]]

# The ordinary/log residue complexes give these ranks. H0 log Omega2
# evaluates two independent sections of Klog tensor F at the cusp.
# Higher residue cohomology is C^7 in degree1, with zero C^3->C^7 map,
# since paired normals v and -v cancel exactly.
assert out['logarithmic']['1']['cohomology_dimensions']==[0,1,1,0,0]
assert out['logarithmic']['2']['cohomology_dimensions']==[2,6,5,1,0]
ordinary0=[1,1,0,0,0]
def ordinary_from_residue(logdims,resdims,resranks):
    return [logdims[q]+(resdims[q-1]-resranks[q-1] if q else 0)-resranks[q] for q in range(5)]
ordinary1=ordinary_from_residue(out['logarithmic']['1']['cohomology_dimensions'],[1,0,0,0,0],[0,0,0,0,0])
ordinary2=ordinary_from_residue(out['logarithmic']['2']['cohomology_dimensions'],[3,7,0,0,0],[2,6,0,0,0])
ordinary3=list(reversed(ordinary1));ordinary4=list(reversed(ordinary0))
table=[ordinary0,ordinary1,ordinary2,ordinary3,ordinary4]
assert table==[[1,1,0,0,0],[0,2,1,0,0],[0,1,6,1,0],[0,0,1,2,0],[0,0,0,1,1]]
assert sum((-1)**(p+q)*table[p][q] for p in range(5) for q in range(5))==6
out['ordinary_hodge_table']=table
out['ordinary_residue_ranks']={'Omega1_H0_log_to_residue':0,'Omega2_H0_log_to_residue':2,'Omega2_H1_log_to_residue':6}
out['status']='PASS'
Path(__file__).with_suffix('.output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':out['status'],'logarithmic_dimensions':{k:v['cohomology_dimensions'] for k,v in out['logarithmic'].items()},'Qdet':out['residue']['cusp_Q_determinant'],'symdet':str(symdet),'sym_rank_drops':[str(x) for x in symroots],'table':table},indent=2))
