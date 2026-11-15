"""Exact local three-branch conductor patterns.

These are local hypersurfaces only, not compact torus degenerations.
They invalidate an attempted conclusion from reduced conductor topology
alone; global anticanonical weights and smoothing must still be used.
"""
from pathlib import Path
import sympy as s
x,y,z,a,b=s.symbols('x y z a b')
lines=[]
for exponent in (2,3):
    F=y**2-x**3*z**exponent
    G=x**2-y**3*z**exponent
    # Modulo F,G, (xy)^2*(1-xy*z^(2k))=0. The second factor is a unit.
    I=s.groebner([F,G],x,y,z,order='lex')
    relation=(x*y)**2*(1-x*y*z**(2*exponent))
    assert I.reduce(relation)[1] == 0
    lines.append(f'k={exponent}: F={F}; G={G}.')
    lines.append('Intersection identity: (xy)^2(1-xy*z^(2k)) is in (F,G); '
                 'therefore (F=G=0)_red is the z-axis as an analytic germ.')
    if exponent==2:
        param={x:a**2,z:b,y:a**3*b}
        assert s.expand(F.subs(param))==0
        assert s.expand(G.subs(param)-a**4*(1-a**5*b**5))==0
        # Membership in C[a²,b,a³b] is exact by parity and exponents.
        def member(i,j):
            return i%2==0 or (i>=3 and j>=1)
        assert all(member(i,j) for i in range(2,25) for j in range(1,25))
        assert not member(1,10) and not member(3,0)
        lines += [
            'Normalization: x=a²,z=b,y=a³b, with fraction-field inverse a=y/(xz).',
            'Intrinsic conductor = a²b C{a,b}; semigroup membership is i even OR (i>=3 AND j>=1).',
            'Other factor pulls back a⁴(1-a⁵b⁵).',
            'Full-union conductor divisor on this branch: 6{a=0}+{b=0}.',
            'Symmetric branch has the same weights. Reduced conductor image is exactly three coordinate axes.',
        ]
    else:
        # Normalization B=C[x,z,u]/(u²-xz), y=u³.
        u=s.symbols('u')
        B=s.groebner([u*u-x*z],u,x,z,order='lex')
        assert B.reduce(F.subs(y,u**3))[1]==0
        assert B.reduce(G.subs(y,u**3)-x**2*(1-u**5*z**5))[1]==0
        lines += [
            'Normalization: B=C{x,z,u}/(u²-xz), y=u³; inverse u=y/(xz).',
            'A=C{x,z} + u³ C{x,z}; B=C{x,z}+u C{x,z}.',
            'Intrinsic conductor=(xz)B=(u²)B; other factor=x²(1-u⁵z⁵).',
            'Full conductor=(x³z)B, Weil divisor 6D_x+2D_z.',
            'On minimal A1 resolution: pullback x=2C_x+E, z=2C_z+E, so conductor=6C_x+4E+2C_z.',
            'This shows private conductor coefficient two is compatible with the same local reduced three-axis image.',
        ]
lines += ['Neither example is asserted to occur in a compact torus smoothing.']
out='\n'.join(lines)+'\n'
print(out,end='')
Path(__file__).with_suffix('.out').write_text(out)
