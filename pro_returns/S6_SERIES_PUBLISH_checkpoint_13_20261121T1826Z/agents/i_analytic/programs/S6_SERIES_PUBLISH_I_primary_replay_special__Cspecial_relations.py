#!/usr/bin/env python3
"""Exact identities for the five closed forms and a rational polynomial
relation for every order-seven norm (including non-real t).
"""
import sympy as s
from Cspecial_division import t,psi,exactorder,D
r=s.sqrt(3)
f5=exactorder(5).as_expr();f6=exactorder(6).as_expr();f7=exactorder(7).as_expr();f8=exactorder(8).as_expr()
for sign in [-1,1]:
 tt=64*(47+sign*27*r)/11
 nn=-sign*17+10*r
 check=s.simplify(f5.subs(t,tt)*nn**2-1728**2)
 assert check==0
 print('t sign',sign,'N^12 =',nn,'exact squared identity:',check)
print('F5=',f5); print('F6=',f6); print('F7=',f7); print('F8=',f8)
print('n=4: R=64/|t|')
print('n=5: R^5=432^5/((1-t)*(5*t-32)^4), both roots are real below 1')
print('n=6: R^2=1728^2/F5(t), both roots are real above 1')
print('n=7: R^35=2^192*3^81/(|t|^8*|t-1|^3*|F6(t)|^12)')
print('n=8: R^4=1728^4/|F7(t)|')
K=s.rem(t**8*(t-1)**3*f6**12,f7,t)
den,num=s.Poly(K,t).clear_denoms()
V=s.symbols('V')
res=s.Poly(s.resultant(f7,V*num.as_expr()-2**384*3**162*den**2,t),V).primitive()[1]
print('n=7 K_num(t)=',num.as_expr())
print('n=7 K_den=',den)
print('n=7 resultant polynomial R(V)=',res.as_expr())
print('n=7 polynomial relation is R((N^12)^70*K_num(t))=0')
print('degree R(V)=',res.degree())
assert res.degree()==4
print('ALL EXACT ASSERTIONS PASSED')
