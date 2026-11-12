"""Exact algebra accompanying CG-S6-01. Python 3 and SymPy; CC0-1.0.

These checks verify the displayed algebra. Quotient topology, analytic charts,
freeness for every parameter and line-bundle claims are proved in the lesson.
"""
from pathlib import Path
import hashlib
import json
import sympy as s

ROOT = Path(__file__).resolve().parents[1]
tests = []

def check(name, condition):
    assert condition, name
    tests.append(name)

def zero(value):
    return all(s.simplify(x) == 0 for x in value) if isinstance(value, s.MatrixBase) else s.simplify(value) == 0

I = s.I
rho = (1+s.sqrt(3)*I)/2
beta = s.symbols('beta_1 beta_2')
matrices = [s.Matrix([[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]]),
            s.Matrix([[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]])]
fixed = [s.Matrix([1,2,-4,0]),s.Matrix([1,3,-3,0])]
delta = s.Matrix([0,0,0,1])
u = s.Matrix([0,1,0,0])
moving = [(s.Matrix([0,1,-2,0]),s.Matrix([0,0,-3,1])),
          (s.Matrix([0,1,-1,0]),s.Matrix([0,0,-2,1]))]
periods = [(rho,(2-rho)/3),(I,(1-I)/2)]
R = [s.Matrix([[rho-1,0],[(2-rho)/3,1]]),s.Matrix([[-I,0],[(1+I)/2,1]])]
L = [s.Matrix([[0,1],[1,-s.Rational(1,3)]]),s.Matrix([[0,1],[1,-s.Rational(1,2)]])]
degrees = [3,2]
orders = [3,4]
signs = [1,-1]
fixed_coordinates = [s.Rational(2,3),s.Rational(1,2)]
moving_coordinates = [rho,I]
rotations = [rho-1,-I]
rotation_matrices = [s.Matrix([[-2,-3],[1,1]]),s.Matrix([[1,2],[-1,-1]])]
gamma = s.Matrix([[1,0,0,0]])
a,b,c,d = s.symbols('a b c d')
x = s.Matrix([a,b,c,d])
details = []

for j in range(2):
    A=matrices[j]; e,f=moving[j]; tau,mu=periods[j]
    Pi=s.Matrix([[6*mu,tau,1,0],[beta[j],mu,0,1]])
    kappa=beta[j]+(2 if j==0 else 3)*mu
    B=s.Matrix.hstack(fixed[j],delta,e,f)
    v=signs[j]*fixed[j]
    m=orders[j]; deg=degrees[j]; omega=rotations[j]
    label=f'case_{j+1}:'
    check(label+'exact_order',A**m==s.eye(4) and all(A**k!=s.eye(4) for k in range(1,m)))
    check(label+'fixed_columns',A*fixed[j]==fixed[j] and A*delta==delta)
    check(label+'fixed_dimension',len((A-s.eye(4)).nullspace())==2)
    check(label+'invariant_covector',gamma*A==gamma and (gamma*v)[0]==signs[j])
    expected=s.Matrix.hstack(6*e-2*f,-e+f,e,s.zeros(4,1)) if j==0 else s.Matrix.hstack(3*f,-e,-e+f,s.zeros(4,1))
    check(label+'all_image_columns',A-s.eye(4)==expected)
    check(label+'oriented_index_determinant',B.det()==-deg)
    inv=s.Matrix([a,d+(c+2*b)/3,b-2*a,-(c+2*b)/3]) if j==0 else s.Matrix([a,d+(c+b)/2,b-3*a,-(c+b)/2])
    check(label+'inverse_lattice_coordinates',zero(B*inv-x))
    check(label+'period_covariance',zero(R[j]*Pi-Pi*A))
    check(label+'fixed_period',zero(Pi*fixed[j]-s.Matrix([0,kappa])))
    check(label+'delta_period',Pi*delta==s.Matrix([0,1]))
    ep=rho-2 if j==0 else I-1
    fp=-3 if j==0 else -2
    check(label+'moving_periods',zero(Pi*e-L[j]*s.Matrix([0,ep])) and zero(Pi*f-L[j]*s.Matrix([0,fp])))
    check(label+'linear_cover_determinant',L[j].det()==-1)
    k=s.Matrix([fixed_coordinates[j],moving_coordinates[j]])
    check(label+'kernel_lift',zero(L[j]*k-Pi*u))
    check(label+'kernel_exact_first_coordinate_order',all(not (n*fixed_coordinates[j]).is_integer for n in range(1,deg)) and (deg*fixed_coordinates[j]).is_integer)
    check(label+'kernel_moving_coordinate_period',zero(deg*moving_coordinates[j]-(3*ep-2*fp if j==0 else 2*ep-fp)))
    M=rotation_matrices[j]
    check(label+'rotation_lattice_matrix',zero(s.Matrix([[ep,fp]])*M-omega*s.Matrix([[ep,fp]])) and M.det()==1)
    check(label+'intertwining_linear',zero(L[j]*s.diag(1,omega)-R[j]*L[j]))
    check(label+'intertwining_translation',zero(L[j]*s.Matrix([signs[j]*kappa/m,0])-Pi*v/m))
    check(label+'kernel_rotation_period',zero((omega-1)*moving_coordinates[j]-(-ep+fp if j==0 else -ep)))
    admissible=[(aa,bb) for aa in range(deg) for bb in range(m)
                if s.Rational(signs[j]*bb,m).is_integer and (aa*fixed_coordinates[j]).is_integer]
    check(label+'only_identity_has_period_translation',admissible==[(0,0)])
    check(label+'normal_character_exponent',s.Rational(-signs[j]*(gamma*v)[0],m)==-s.Rational(1,m))
    check(label+'one_form_eigenvalues',s.simplify(omega-1)!=0)
    details.append({'case':j+1,'cover_degree':deg,'affine_order':m,'composite_degree':deg*m,'determinant':int(B.det())})

t,q,h = s.symbols('Im_tau Im_mu Im_beta',real=True)
check('full_real_period_determinant',zero(s.Matrix([[6*q,t],[h,q]]).det()-(-t*(h-6*q*q/t))))
source=ROOT/'src/finite-quotients-and-line-bundles.md'
receipt={'schema':'exact-course-calculation/v1','lesson':'CG-S6-01','passed':len(tests),'checks':tests,
         'cases':details,'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
         'method':'Exact SymPy expressions; no floating point tests.',
         'scope':'Displayed matrix, period, lattice, affine and character identities. Complete geometric proofs are in the lesson; no independent review or global sphere recognition is certified by this script.'}
(ROOT/'checks/EXACT_CHECKS.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'passed':len(tests),'cases':details}))
