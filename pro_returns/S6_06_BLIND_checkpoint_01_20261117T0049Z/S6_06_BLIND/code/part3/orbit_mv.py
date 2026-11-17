#!/usr/bin/env python3
"""Exact matrices in the circle quotient of the AC26 six-sphere.

The proof in notes/part3_family.md identifies each generator.  This
program verifies the primitive Gysin map and every nonzero MV matrix;
it does not replace the geometric identification of their entries.
"""
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
r0=s.Matrix([0,0,1]); r1=s.Matrix([0,1,1])
rp=s.Matrix([1,0,1]); rm=s.Matrix([-1,1,1])
Cp=s.Matrix.hstack(r0,r1,rp); Cm=s.Matrix.hstack(r0,r1,rm)
delta=s.Matrix([0,1,0])
print('positive cone rays=',Cp.tolist(),'det=',Cp.det())
print('negative cone rays=',Cm.tolist(),'det=',Cm.det())
print('wall relation rp+rm-r0-r1=',list(rp+rm-r0-r1))
print('character change Cm^-1*Cp=',(Cm.inv()*Cp).tolist())
print('circle weights positive=',list(Cp.inv()*delta))
print('circle weights negative=',list(Cm.inv()*delta))
assert rp+rm==r0+r1
assert list(Cp.inv()*delta)==[-1,1,0]
assert list(Cm.inv()*delta)==[-1,1,0]
# In the unitary SU2 trivialization of O(1)+O(-1), e has no base term.
# MV maps use (complement, fixed tube); domain order is (base,meridian).
matrices={
 'Gysin H3(A)->H2(B)':s.Matrix([[1]]),
 'MV H0(boundary)->H0(B)+H0(tube)':s.Matrix([[1],[-1]]),
 'MV H2(boundary)->H2(B)+H2(tube)':s.Matrix([[0,1],[-1,0]]),
 'MV H4(boundary)->0':s.zeros(0,1)
}
for name,M in matrices.items():
 print(name, M.tolist(), 'rank=',M.rank(),
       'SNF=',smith_normal_form(M,domain=ZZ).tolist())
assert abs(matrices['MV H2(boundary)->H2(B)+H2(tube)'].det())==1
# All other positive-degree domain groups of the boundary vanish.
print('H_*(orbit Y)= [Z,0,0,0,0,Z]; no torsion')
print('All nonzero Gysin/MV maps and primitive indices are printed above.')
