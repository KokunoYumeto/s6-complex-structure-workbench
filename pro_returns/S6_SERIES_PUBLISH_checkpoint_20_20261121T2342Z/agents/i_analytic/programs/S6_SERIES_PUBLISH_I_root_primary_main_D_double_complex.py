#!/usr/bin/env python3
"""Exact fresh matrix verification of Paper I C1.1/C2.1 and main D.

Uses Python Fraction Gaussian elimination, not a symbolic-algebra library.
Authored after reading the receiving proof, 19 November 2026.  It checks
the finite dot/arrow/square model; the applicability to the smooth-form
complex is the printed specialization of Stelzig's decomposition theorem.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import platform
import time

START=time.monotonic()
CHECKS=[]
RESULTS=[]


def check(name,claim):
    CHECKS.append({'name':name,'pass':bool(claim)})
    if not claim:
        raise AssertionError(name)


def zeros(m,n):
    return [[F(0) for _ in range(n)] for _ in range(m)]


def add(A,B):
    return [[x+y for x,y in zip(a,b)] for a,b in zip(A,B)]


def multiply(A,B):
    m,n=len(A),len(B[0]) if B else 0
    return [[sum((A[i][k]*B[k][j] for k in range(len(B))),F(0)) for j in range(n)] for i in range(m)]


def rank(A,n=None):
    n=len(A[0]) if A else (0 if n is None else n)
    B=[list(map(F,row)) for row in A]
    pivot=0
    for c in range(n):
        k=next((k for k in range(pivot,len(B)) if B[k][c]),None)
        if k is None:
            continue
        B[pivot],B[k]=B[k],B[pivot]
        a=B[pivot][c]
        B[pivot]=[x/a for x in B[pivot]]
        for j in range(pivot+1,len(B)):
            a=B[j][c]
            if a:
                B[j]=[x-a*y for x,y in zip(B[j],B[pivot])]
        pivot+=1
        if pivot==len(B):
            break
    return pivot


def nullspace(A,n):
    B=[list(map(F,row)) for row in A]
    pivots=[]
    for c in range(n):
        k=next((k for k in range(len(pivots),len(B)) if B[k][c]),None)
        if k is None:
            continue
        r=len(pivots)
        B[r],B[k]=B[k],B[r]
        a=B[r][c]
        B[r]=[x/a for x in B[r]]
        for j in range(len(B)):
            if j!=r:
                a=B[j][c]
                B[j]=[x-a*y for x,y in zip(B[j],B[r])]
        pivots.append(c)
    free=[j for j in range(n) if j not in pivots]
    out=zeros(n,len(free))
    for a,j in enumerate(free):
        out[j][a]=F(1)
        for r,c in enumerate(pivots):
            out[c][a]=-B[r][j]
    return out


def columns(A,indices):
    return [[row[j] for j in indices] for row in A]


def join(A,B):
    return [a+b for a,b in zip(A,B)]


def finite_model(h):
    vertices=[]
    horizontal=[]
    vertical=[]
    arrows=[]

    def vertex(p,q):
        vertices.append((p,q))
        return len(vertices)-1

    vertex(0,0);vertex(3,3)
    shape=[((0,1),(1,1),1),((1,1),(2,1),h),((1,2),(2,2),h),((2,2),(3,2),1)]
    for source,target,count in shape:
        for _ in range(count):
            a=vertex(*source);b=vertex(*target)
            horizontal.append((a,b,1));arrows.append((a,b))
            a=vertex(source[1],source[0]);b=vertex(target[1],target[0])
            vertical.append((a,b,1));arrows.append((a,b))
    # An acyclic square with anticommuting signs; no BC/A contribution.
    ll=vertex(1,1);lr=vertex(2,1);ul=vertex(1,2);ur=vertex(2,2)
    horizontal.extend([(ll,lr,1),(ul,ur,1)])
    vertical.extend([(ll,ul,1),(lr,ur,-1)])
    n=len(vertices)
    d1,d2=zeros(n,n),zeros(n,n)
    for a,b,c in horizontal:d1[b][a]=F(c)
    for a,b,c in vertical:d2[b][a]=F(c)
    return vertices,d1,d2,arrows


for h in range(6):
    vertices,d1,d2,arrows=finite_model(h)
    n=len(vertices)
    mixed=multiply(d1,d2)
    check(f'h={h}: both differentials square to zero',multiply(d1,d1)==multiply(d2,d2)==zeros(n,n))
    check(f'h={h}: anticommutation',add(mixed,multiply(d2,d1))==zeros(n,n))
    bc=[[0]*4 for _ in range(4)]
    ae=[[0]*4 for _ in range(4)]
    dol=[[0]*4 for _ in range(4)]
    d1ranks=[[0]*4 for _ in range(4)]
    bc_count=[[0]*4 for _ in range(4)]
    ae_count=[[0]*4 for _ in range(4)]
    for p,q in [(0,0),(3,3)]:bc_count[q][p]+=1;ae_count[q][p]+=1
    for a,b in arrows:
        p,q=vertices[a];ae_count[q][p]+=1
        p,q=vertices[b];bc_count[q][p]+=1
    for p in range(4):
        for q in range(4):
            here=[i for i,z in enumerate(vertices) if z==(p,q)]
            left=[i for i,z in enumerate(vertices) if z==(p-1,q)]
            below=[i for i,z in enumerate(vertices) if z==(p,q-1)]
            diagonal=[i for i,z in enumerate(vertices) if z==(p-1,q-1)]
            right_below=[i for i,z in enumerate(vertices) if z==(p+1,q-1)]
            bc[q][p]=len(here)-rank(columns(d1,here)+columns(d2,here))-rank(columns(mixed,diagonal))
            ae[q][p]=len(here)-rank(columns(mixed,here))-rank(join(columns(d1,left),columns(d2,below)))
            dol[q][p]=len(here)-rank(columns(d2,here))-rank(columns(d2,below))
            K=nullspace(columns(d2,here),len(here))
            image=multiply(columns(d1,here),K)
            boundary=columns(d2,right_below)
            # Empty source requires an n-by-zero image, which is represented
            # by n empty rows by columns(), and handled explicitly here.
            if not here:image=zeros(n,0)
            d1ranks[q][p]=rank(join(image,boundary))-rank(boundary)
    expected_bc=[[1,0,0,0],[0,2,h,0],[0,h,2*h,1],[0,0,1,1]]
    expected_ae=[[1,1,0,0],[1,2*h,h,0],[0,h,2,0],[0,0,0,1]]
    expected_dol=[[1,0,0,0],[1,h+1,h,0],[0,h,h+1,1],[0,0,0,1]]
    expected_rank=[[0,0,0,0],[1,h,0,0],[0,h,1,0],[0,0,0,0]]
    check(f'h={h}: BC kernels/images equal corner count',bc==bc_count)
    check(f'h={h}: A kernels/images equal corner count',ae==ae_count)
    check(f'h={h}: complete BC table',bc==expected_bc)
    check(f'h={h}: complete A table',ae==expected_ae)
    check(f'h={h}: complete Dolbeault table',dol==expected_dol)
    check(f'h={h}: induced d1 ranks on column cohomology',d1ranks==expected_rank)
    d=add(d1,d2)
    betti=[]
    for k in range(7):
        here=[i for i,z in enumerate(vertices) if sum(z)==k]
        prev=[i for i,z in enumerate(vertices) if sum(z)==k-1]
        betti.append(len(here)-rank(columns(d,here))-rank(columns(d,prev)))
    check(f'h={h}: total cohomology',betti==[1,0,0,0,0,0,1])
    RESULTS.append({'h':h,'dimensions':n,'bidegrees':vertices,
                    'd_partial':[[int(x) for x in row] for row in d1],
                    'd_barpartial':[[int(x) for x in row] for row in d2],
                    'BC_rows_q_ascending':bc,'A_rows_q_ascending':ae,
                    'Dolbeault_rows_q_ascending':dol,'d1_ranks_q_ascending':d1ranks,'betti':betti})

OUT={'reviewer':'GPT-6 Astra (OpenAI), ChatGPT Pro mode, inherited effort; same model family',
     'method':'Fresh Python Fraction Gaussian elimination on kernels, images, induced column-cohomology maps, plus separate corner counts',
     'chronology':'After reading receiving proofs; no earlier code imported',
     'python':platform.python_version(),'all_pass':all(x['pass'] for x in CHECKS),
     'check_count':len(CHECKS),'checks':CHECKS,'models':RESULTS,
     'elapsed_seconds':round(time.monotonic()-START,6)}
target=Path(__file__).with_suffix('.output.json')
target.write_text(json.dumps(OUT,indent=2)+'\n')
print(json.dumps({'all_pass':OUT['all_pass'],'check_count':len(CHECKS),
                  'h_values':list(range(6)),'elapsed_seconds':OUT['elapsed_seconds'],
                  'output':str(target),'output_sha256':hashlib.sha256(target.read_bytes()).hexdigest()},indent=2))
