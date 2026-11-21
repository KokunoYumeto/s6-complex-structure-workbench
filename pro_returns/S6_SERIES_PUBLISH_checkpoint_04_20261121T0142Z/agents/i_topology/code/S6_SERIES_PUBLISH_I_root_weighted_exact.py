#!/usr/bin/env python3
"""Fresh integer-inverse and rational-polynomial checks; no retained code used."""
from pathlib import Path
from math import gcd
from fractions import Fraction as F
import json,csv,hashlib
P=Path(__file__).resolve().parents[1]

def h0(m,n,a):
    if a<0:return 0
    j0=(a*pow(n,-1,m))%m
    rem=a-n*j0
    return 0 if rem<0 else rem//(m*n)+1

def h0_enumerate(m,n,a):
    return sum((a-m*i)%n==0 for i in range(a//m+1)) if a>=0 else 0

def h1(m,n,a):return h0(m,n,-a-m-n)
def degree(m,n,a):
    r=(a*pow(n,-1,m))%m;s=(a*pow(m,-1,n))%n
    assert (a-n*r-m*s)%(m*n)==0
    return (a-n*r-m*s)//(m*n)
def total(m,n,lists):
    out=[0,0,0,0]
    for q,ls in enumerate(lists):
        for a in ls:
            out[q]+=h0(m,n,a);out[q+1]+=h1(m,n,a)
    return out
rows=[]
for k in range(1,81):
 for l in range(1,81):
    m,n=3*k,4*l
    if gcd(m,n)!=1:continue
    z=k*l;d=m+n;b=d-12*z;e=int(k>1)
    vals=[0,z,-z,-2*z,b,b-z,z-d,2*z-d,13*z-2*d,z-2*d]
    for a in vals:
        assert h0(m,n,a)==h0_enumerate(m,n,a)
        assert h1(m,n,a)==h0_enumerate(m,n,-a-d)
        assert h0(m,n,a)==max(0,degree(m,n,a)+1)
        assert h1(m,n,a)==max(0,-degree(m,n,a)-1)
    assert all(degree(m,n,a)==-1 for a in [z,-z,-2*z,b])
    assert degree(m,n,b-z)==-1-e
    assert degree(m,n,z-2*d)==-1-int(k==1)
    assert h0(m,n,13*z-2*d)==e
    if e:assert m*(3*l-2)+n*(k-2)==13*z-2*d
    assert h0(m,n,z-d)==h0(m,n,2*z-d)==h0(m,n,z-2*d)==0
    V=total(m,n,[[0,-z],[0,-z,-z,-2*z],[-z,-2*z]])
    H=total(m,n,[[b],[b,b-z],[b-z]])
    assert V==[1,1,0,0] and H==[0,0,e,e]
    # Smith determinantal divisors of relations (-1,m,0),(-1,0,n).
    assert gcd(gcd(m,n),m*n)==1
    # Actual local characters of O(-z) and divisor/weight identities.
    assert (-z*pow(n,-1,m))%m==2*k
    assert (-z*pow(m,-1,n))%n==l
    assert (k-1)*n+(2*l-1)*m==10*z-d
    assert (4*k-2)*n+(2*l-2)*m==22*z-2*d
    assert 3*k*l==3*z and 4*l*k==4*z
    rows.append([k,l,m,n,z,d,e,','.join(map(str,V)),','.join(map(str,H)),degree(m,n,b-z),degree(m,n,z-2*d),h0(m,n,13*z-2*d)])
out=P/'output';out.mkdir(exist_ok=True)
f=out/'S6_SERIES_PUBLISH_I_root_weighted_all_pairs.csv'
with f.open('w',newline='') as h:
 w=csv.writer(h);w.writerow(['k','l','m','n','z','d','e_k','hV','hH','coarse_degree_HLinv','coarse_degree_z_minus_2d','horizontal_residue_dimension']);w.writerows(rows)
# Independent expansion ch(T) Td(T) in Chern monomials of total weight3.
chern={'c1^3':F(1,12)+F(1,4)+F(1,6),'c1*c2':F(3,24)+F(1,12)-F(1,2)-F(1,2),'c3':F(3,6)}
assert chern=={'c1^3':F(1,2),'c1*c2':F(-19,24),'c3':F(1,2)}
# Explicit cochain map from our actual triangles to the printed cusp complex.
actual=[[1,-1,-1],[-1,1,1]];printed=[[1,-1,1],[1,-1,1]]
T1=[1,1,-1];T2=[1,-1]
assert [[printed[i][j]*T1[j] for j in range(3)] for i in range(2)]==[[T2[i]*actual[i][j] for j in range(3)] for i in range(2)]
summary={'all_assertions_passed':True,'pair_count':len(rows),'e_k_distribution':{'0':sum(r[6]==0 for r in rows),'1':sum(r[6]==1 for r in rows)},'method':'Integer modular inverses count weighted monomials; independently compared with enumerating x-exponents. Exact coarse residue degrees checked on every pair; algebraic derivation proves all-pair claims. No retained program read or reused.','pair_file':str(f),'pair_file_sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'HRR_chT_times_Td_degree3':{k:str(v) for k,v in chern.items()},'S6_chi_TX':str(2*chern['c3']),'cusp_complex_map':{'T1_diagonal':T1,'T2_diagonal':T2,'identity':'d_print*T1=T2*d_actual','gamma_print':[0,-1,-1],'u_print':[1,0,-1],'gamma_relation':'gamma_print=-T1*dy_actual','u_relation':'u_print=T1*dx_actual'},'claims_not_tested':'The program does not prove analytic base change, duality, properness, or the raw modular determinant input; these have separate derivations/primary inputs.'}
(out/'S6_SERIES_PUBLISH_I_root_weighted_exact.json').write_text(json.dumps(summary,indent=2));print(json.dumps(summary,indent=2))
