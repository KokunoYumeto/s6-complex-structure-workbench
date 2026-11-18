#!/usr/bin/env python3
"""Exact source/Cartier fractional periods of the actual E7 cap branches.

The computations retain the integral h-period in A^m and the central
two-torsion representative.  They do not construct the cyclic action
on collision root sheets or a compact filling.
"""
from pathlib import Path
from fractions import Fraction as Q
from math import lcm
from datetime import datetime,timezone
import json
ROOT=Path(__file__).resolve().parents[2]

def dot(x,y): return sum(a*b for a,b in zip(x,y))
def add(x,y): return [a+b for a,b in zip(x,y)]
def scale(c,x): return [c*a for a in x]

def one(p,k,n,good):
    a,b=(1,2) if good else (2,1)
    m=4*p if good else 4*p-1
    N=k*m
    # Coordinates of logarithms are (log Q, log P, log g_V).
    hs=[Q(1),Q(0),Q(0)]
    hl=[Q(0),Q(a),Q(0)]
    gs=[Q(0),Q(-b),Q(0)]
    gl=[Q(0),Q(0),Q(1)]
    R=([Q(1,m),Q(2,m),Q(0)] if good else
       [Q(-(m-1),2*m),Q(1,m),Q(0)])
    f=([Q(-n,m),Q(n,m)] if good else
       [Q(n*(m-1),2*m),Q(n,m)])
    As=add(scale(f[0],hs),scale(f[1],gs))
    Al=add(scale(f[0],hl),scale(f[1],gl))
    assert As==scale(-n,R)
    Rnorm=add(scale(m,R),[Q(0),Q(-b),Q(0)])
    assert Rnorm[1:]==[0,0] and Rnorm[0].denominator==1
    assert (m*f[0]).denominator==1 and m*f[1]==n
    assert lcm(*(x.denominator for x in f))==m
    # On the central E annulus log Q=-2 log P, log g_V=log P+log C.
    central_R=dot(R,[-2,1,1])
    assert central_R==(0 if good else 1)
    central_source_P=dot(As,[-2,1,1])
    central_line_P=dot(Al,[-2,1,1])
    central_line_C=Al[2]
    assert central_line_C==Q(n,m)
    assert central_source_P==(0 if good else -n)
    assert central_line_P==(0 if good else n)
    # Reduced central Cartier frame is Z*V.
    assert central_source_P+central_line_P==0
    inv=scale(-1,f)
    scalar=[Q(b*n,2*m),Q(-n,m)]
    E=((0,0),(0,N));H=((2,b),(-a,N-1))
    Einv=[dot(row,inv) for row in E]
    Hinv=[dot(row,inv) for row in H]
    Hscalar=[dot(row,scalar) for row in H]
    assert Einv==[0,-n*k]
    assert Hscalar==[0,-n*k]
    diff=add(Hinv,scale(-1,Hscalar))
    assert diff==([0,0] if good else [-n,n])
    assert add(inv,scale(-1,scalar))==([0,0] if good else [Q(-n,2),0])
    return {
       'a':a,'b':b,'m':m,'N':N,'n':n,
       'R_log_Q_P_gV':list(map(str,R)),
       'A_h_g_coefficients':list(map(str,f)),
       'A_power_m_h_g':[int(m*f[0]),n],
       'inverse_h_g_coefficients':list(map(str,inv)),
       'central_inverse_E':list(map(str,Einv)),
       'central_inverse_H':list(map(str,Hinv)),
       'scalar_only_inverse_h_g':list(map(str,scalar)),
       'central_source_correction_H':list(map(str,diff)),
       'actual_fractional_period_order':m,
       'scalar_only_order':lcm(*(x.denominator for x in scalar))}

rows=[one(p,k,n,good) for good in (True,False)
      for p in range(1,13) for k in range(1,13) for n in (-1,1)]
out={
 'utc':datetime.now(timezone.utc).isoformat(),
 'status':'PASS: source branch, retained integral norm, central Cartier constant, and exact full fractional period',
 'rows_checked':len(rows),
 'checks_per_row':15,
 'scope':'Actual Tate lift and cap norm comparison; collision root-sheet cyclic action, '
         'central annular attachment and global source return remain unassigned.',
 'rows':rows}
dest=ROOT/'code/part3_fourfold/source_zero_cap_fractional_period.json'
dest.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='rows'},indent=2))
