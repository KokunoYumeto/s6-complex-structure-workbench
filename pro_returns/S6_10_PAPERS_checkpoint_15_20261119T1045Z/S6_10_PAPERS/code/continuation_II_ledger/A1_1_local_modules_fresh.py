#!/usr/bin/env python3
"""Fresh exact conormal/torsion certificates at a node and a cusp.

The analytic and global sheaf assertions are proved separately before
target reading; these calculations do not infer them from examples.
"""
from pathlib import Path
import hashlib,json
import sympy as s

x,y,t,z=s.symbols('x y t z')
checks=[];certificates=[]
def basis(polys):
 return [s.expand(p.as_expr()) for p in s.groebner(polys,x,y,order='lex').polys]
def same(name,left,right):
 a=basis(left);b=basis(right);assert a==b,(name,a,b)
 checks.append(name);certificates.append({'name':name,'left_basis':list(map(str,a)),'right_basis':list(map(str,b))})
def intersection(left,right):
 gb=s.groebner([z*p for p in left]+[(1-z)*q for q in right],z,x,y,order='lex')
 return basis([p.as_expr() for p in gb.polys if not p.as_expr().has(z)])
def colon_principal(ideal,g):
 common=intersection(ideal,[g]);out=[]
 for p in common:
  q,r=s.div(p,g,x,y);assert r==0,(p,g,r);out.append(q)
 return basis(out)
def zero(name,expr,modulus=None):
 expr=s.expand(expr)
 if modulus is not None:expr=s.groebner([modulus],x,y,order='lex').reduce(expr)[1]
 assert s.expand(expr)==0,(name,expr)
 checks.append(name)

node=x*y;dx=s.diff(node,x);dy=s.diff(node,y)
node_ax=colon_principal([node],dx);node_ay=colon_principal([node],dy)
same('node_ann_dF_first_coordinate',node_ax,[x])
same('node_ann_dF_second_coordinate',node_ay,[y])
same('node_joint_annihilator_is_zero_in_reduced_ring',intersection(node_ax,node_ay),[node])
un=s.Matrix([y,0]);vn=s.Matrix([0,x]);dnode=s.Matrix([dx,dy])
for j in range(2):zero('node_conormal_equals_u_plus_v_'+str(j),dnode[j]-un[j]-vn[j])
for j in range(2):
 zero('node_x_u_zero_'+str(j),x*un[j],node)
 zero('node_y_v_zero_'+str(j),y*vn[j],node)
zero('node_u_restricts_zero_on_x_branch',un[0].subs(y,0))
zero('node_u_restricts_zero_on_y_branch',un[1].subs(x,0))
zero('node_v_restricts_zero_on_x_branch',vn[0].subs(y,0))
zero('node_v_restricts_zero_on_y_branch',vn[1].subs(x,0))

cusp=y*y-x**3;cx=s.diff(cusp,x);cy=s.diff(cusp,y)
cusp_ax=colon_principal([cusp],cx);cusp_ay=colon_principal([cusp],cy)
same('cusp_first_partial_has_zero_annihilator',cusp_ax,[cusp])
same('cusp_second_partial_has_zero_annihilator',cusp_ay,[cusp])
same('cusp_joint_annihilator',intersection(cusp_ax,cusp_ay),[cusp])
uc=s.Matrix([-3*y,2*x]);vc=s.Matrix([-3*x*x,2*y]);dcusp=s.Matrix([cx,cy])
for j in range(2):zero('cusp_v_is_dF_'+str(j),vc[j]-dcusp[j])
nu={x:t*t,y:t**3};restriction=s.Matrix([[2*t,3*t*t]])
zero('cusp_u_normalization_differential',(restriction*uc.subs(nu,simultaneous=True))[0])
zero('cusp_v_normalization_differential',(restriction*vc.subs(nu,simultaneous=True))[0])
for j in range(2):
 zero('cusp_relation_yu_xv_'+str(j),y*uc[j]-x*vc[j],cusp)
 zero('cusp_relation_x2u_yv_'+str(j),x*x*uc[j]-y*vc[j],cusp)
same('cusp_torsion_annihilator_quotient_relations',[cusp,y,x*x],[y,x*x])
same('node_torsion_annihilator_quotient_relations',[node,x,y],[x,y])

def standard_monomials(ideal,expected):
 gb=s.groebner(ideal,x,y,order='lex');lead=[p.LM(order=gb.order).exponents for p in gb.polys]
 # Pure powers bound the staircase exactly, so this enumeration is complete.
 bx=min(a for a,b in lead if b==0 and a>0)
 by=min(b for a,b in lead if a==0 and b>0)
 mon=[x**a*y**b for a in range(bx) for b in range(by)
      if not any(a>=i and b>=j for i,j in lead)]
 assert mon==expected,(mon,expected)
 checks.append('torsion_basis_'+str(expected));return list(map(str,mon))
node_basis=standard_monomials([node,x,y],[s.Integer(1)])
cusp_basis=standard_monomials([cusp,y,x*x],[s.Integer(1),x])

P=Path(__file__).resolve().parents[2]
out=P/'analysis/continuation_II_ledger/A1_1_local_modules_fresh.output.json'
result={'all_passed':True,'checks':len(checks),'check_names':checks,
 'method':'Exact lexicographic elimination for ideal intersections and colon ideals; actual normalization differential and conormal syzygy matrices; complete finite quotient staircases.',
 'ideal_certificates':certificates,'node_torsion_basis':node_basis,'cusp_torsion_basis':cusp_basis,
 'program_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'scope':'Exact singular local conormal/torsion checks only. The complete analytic filtration and connecting-map proof is in A1_1_before_read.md; finite examples do not establish it.'}
out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'all_passed':True,'checks':len(checks),'node_torsion_basis':node_basis,'cusp_torsion_basis':cusp_basis,'program_sha256':result['program_sha256']},indent=2))
