#!/usr/bin/env python3
"""Exact selected-I3 fan arithmetic with complete multiplier exponents.

The geometric proof is kept in the companion working note.  The source,
root, point line, identity source closing and native product are the
actual SI3/ASI3/IF3/VI3 data, and the fixed integer seed is IC2 together
with the directed vertical source/line/cap comparison.
"""
from pathlib import Path
from fractions import Fraction as F
from collections import deque,Counter
from datetime import datetime,timezone
import hashlib,json

ROOT=Path(__file__).resolve().parents[2]
ID=(1,0,0,1);Q0=(1,-1,0,1);Q1=(1,0,-1,1)
Q2=(1,1,0,1);Q1INV=(1,0,1,1);R=(-1,-1,1,0);SWAP=(0,1,1,0)
B0=(2,-1,6,-3);counts=Counter()
def ck(n,x):
    assert bool(x),n
    counts[n]+=1
def mul(a,b):return (a[0]*b[0]+a[1]*b[2],a[0]*b[1]+a[1]*b[3],a[2]*b[0]+a[3]*b[2],a[2]*b[1]+a[3]*b[3])
def det(a):return a[0]*a[3]-a[1]*a[2]
def inv(a):
    d=det(a);ck('actual unimodular inverse',d in (-1,1))
    return (d*a[3],-d*a[1],-d*a[2],d*a[0])
def neg(a):return tuple(-x for x in a)
GROUP=(ID,R,mul(R,R),neg(ID),neg(R),neg(mul(R,R)))
def canonical(P):
    ck('unimodular input',det(P) in (-1,1))
    P=P if det(P)==1 else mul(P,SWAP)
    choices=[mul(P,g) for g in GROUP]
    fixed=[q for q in choices if q[0]==1 and q[1]==0 and q[3]==1]
    if fixed:
        ck('unique physical vertical representative',len(fixed)==1);return fixed[0]
    interior=[q for q in choices if q[0]>0 and q[1]<0]
    ck('unique physical cone representative',len(interior)==1)
    return interior[0]
def word(P):
    C=canonical(P);cur=C;back=[]
    while cur[1]:
        p,r=cur[0],-cur[1];ck('positive Euclidean pair',p>0 and r>0)
        before=p+r
        if r>=p:cur=mul(cur,Q2);back.append(0)
        else:cur=mul(cur,Q1INV);back.append(1)
        if cur[1]:ck('strict Euclidean descent',cur[0]-cur[1]<before)
    ck('literal vertical endpoint',cur==(1,0,cur[2],1))
    w=tuple(reversed(back));rebuilt=cur
    for i in w:rebuilt=mul(rebuilt,(Q0,Q1)[i])
    ck('exact full word',rebuilt==C)
    return cur[2],w,C
def coefficient_exponents(P):
    A=inv(P)
    # Order: kappa, alpha, g, eta.  The q exponents are A*P=I.
    E=tuple(tuple((A[2*i]*P[j],A[2*i+1]*P[j],A[2*i]*P[2+j],A[2*i+1]*P[2+j]) for j in range(2)) for i in range(2))
    ck('full height exponents unchanged',mul(A,P)==ID)
    return E
def transformed_exponents(E,Q):
    Qi=inv(Q)
    return tuple(tuple(tuple(sum(Qi[2*i+h]*Q[2*j+k]*E[h][j][r] for h in range(2) for j in range(2)) for r in range(4)) for k in range(2)) for i in range(2))
def local(P):
    Pi=inv(P);B=tuple(2*x for x in mul(mul(Pi,B0),P))
    l=(B[3]-B[2],B[0]-B[1],B[3])
    x,y=Pi[1],Pi[3];w=(x,y,-x-y);d=(-x-2*y,-2*x-y,x-y)
    I=tuple(-w[i]+d[i]*(l[i]+1) for i in range(3))
    W=tuple(-w[i]-d[i]*(l[i]+1) for i in range(3))
    ck('complete double determinant winding',B[0]+B[3]==-2)
    E=coefficient_exponents(P)
    weights=(2,6,-1,-3)
    ck('full multiplier winding agrees',tuple(2*sum(E[i][j][k]*weights[k] for k in range(4)) for i in range(2) for j in range(2))==B)
    return B,l,w,d,I,W
def integer(q):
    q=F(q);ck('actual free-coordinate integrality',q.denominator==1);return q.numerator
def traces(P,V,D):
    _,_,w,_,I,W=local(P)
    ck('complete symmetric variation',all(V[i][j]==V[j][i] for i in range(3) for j in range(3)))
    for j in (1,2):
        for k in range(3):
            ck('full action prism',w[j]*V[k][j]-w[0]*V[k][0]==(I[j] if k==j else 0)-(I[0] if k==0 else 0))
        ck('full derivative prism',w[j]*D[j]-w[0]*D[0]==W[j]-W[0])
def index_vertical(j):return 8-j*(j*j-9*j+26)//3
def seed(j):
    ck('integer vertical polynomial',j*(j*j-9*j+26)%3==0)
    S=index_vertical(j);mu=-1;nu=6*S
    a=-2*(mu+nu)-2;b=a+4*nu
    I0=4*j*j-24*j+34
    V=((a,-I0,I0),(-I0,2*j-8,0),(I0,0,2*j-6))
    D=(b,4*j*j-26*j+40,-4*j*j+22*j-30)
    P=(1,0,j,1);traces(P,V,D)
    ck('fixed native left recovered before finite reduction',integer(F(-4-a-b,4))==mu)
    ck('fixed native right recovered before finite reduction',integer(F(b-a,4))==nu)
    return P,V,D,S
def native(a,b):return integer(-1-F(a+b,4)),integer(F(b-a,4))
def advance(P,V,D,S,i,selected=2,Q=None):
    if Q is None:Q=(Q0,Q1)[i]
    target=mul(P,Q);a,b=V[i][i],D[i]
    _,_,w,_,I,W=local(target)
    ck('canonical target all weights nonzero',all(w))
    c=w[selected]**2*a-w[selected]*I[selected]
    e=w[selected]*(2*a-b)-W[selected]
    VV=tuple(tuple(integer((F(I[j],w[j]) if j==k else 0)+F(c,w[j]*w[k])) for k in range(3)) for j in range(3))
    DD=tuple(integer(F(W[j]+e,w[j])) for j in range(3))
    m,n=native(a,b);mm,nn=native(VV[selected][selected],DD[selected])
    ck('literal selected Cox reset',(mm,nn)==(m+2*n,-n))
    ck('complete selected ordinary reset',VV[selected][selected]==a and DD[selected]==2*a-b)
    ck('full coefficient morphism under fan reset',transformed_exponents(coefficient_exponents(P),Q)==coefficient_exponents(target))
    traces(target,VV,DD)
    return target,VV,DD,S+n,n
def calculate(P,history=False):
    j,steps,target=word(P);cur,V,D,S=seed(j);rows=[]
    for i in steps:
        old=cur;oldpair=native(V[i][i],D[i])
        cur,V,D,S,n=advance(cur,V,D,S,i)
        if history:rows.append({'old_basis':old,'edge':i,'old_single_native_pair':oldpair,'new_basis':cur,'native_right_increment':n,'integer_path_sum':S,'target_variation':V,'target_stable_derivative':D,'full_multiplier_exponents':coefficient_exponents(cur)})
    ck('computed target exact',cur==target)
    out={'input_basis':P,'canonical_basis':target,'vertical_index':j,'word':steps,'integer_path_sum':S,'physical_class_mod28':S%28,'variation':V,'stable_derivative':D}
    if history:out['steps']=rows
    return out
def independent_traversal(j,depth=8):
    P,V,D,S=seed(j);todo=deque([(P,V,D,S,0)]);seen=set();skipped=0
    while todo:
        P,V,D,S,level=todo.popleft();key=(P,V,D,S%28)
        if key in seen:continue
        seen.add(key)
        ck('independent three-edge path matches canonical class',calculate(P)['physical_class_mod28']==S%28)
        if level==depth:continue
        for i,Q in enumerate((Q0,Q1,Q2)):
            T=mul(P,Q);sel=(2,2,0)[i];a,b=V[i][i],D[i]
            _,_,w,_,I,W=local(T);zeros=[k for k in range(3) if w[k]==0]
            m,n=native(a,b)
            if not zeros:
                T,VV,DD,SS,_=advance(P,V,D,S,i,sel,Q)
            elif zeros==[sel]:
                VV=[[0]*3 for _ in range(3)];DD=[0]*3
                VV[sel][sel]=a;DD[sel]=2*a-b
                for k in range(3):
                    if k==sel:continue
                    VV[k][k]=integer(F(I[k],w[k]));VV[k][sel]=VV[sel][k]=integer(F(-I[sel],w[k]));DD[k]=integer(F(W[k]-W[sel],w[k]))
                VV=tuple(map(tuple,VV));DD=tuple(DD);SS=S+n
                ck('selected fixed target inverse free reset',native(VV[sel][sel],DD[sel])==(m+2*n,-n));traces(T,VV,DD)
            else:
                skipped+=1;continue
            todo.append((T,VV,DD,SS,level+1))
    return {'seed':j,'depth':depth,'states':len(seen),'separate_fixed_targets_not_used_as_reconstruction':skipped}
def main():
    # Exact signed vertical and inverse checks are performed before any
    # finite group reduction or selection of a residue witness.
    for j in range(-84,85):
        P,V,D,S=seed(j)
        c1=native(V[1][1],D[1]);c2=native(V[2][2],D[2])
        ck('VI3 exact C1 pair',c1==(-(j-3)**2,(j-3)*(j-4)))
        ck('VI3 exact C2 pair',c2==((j-2)*(j-4),-(j-2)*(j-3)))
        ck('positive signed vertical recurrence',index_vertical(j+1)-S==c2[1])
        ck('negative signed vertical recurrence',index_vertical(j-1)-S==c1[1])
    bound=18;inputs=0;fans={};maxlen=0
    for a in range(-bound,bound+1):
      for b in range(-bound,bound+1):
       for c in range(-bound,bound+1):
        for sign in (-1,1):
         if a:
            num=sign+b*c
            if num%a:continue
            ds=[num//a]
         else:
            if -b*c!=sign:continue
            ds=range(-bound,bound+1)
         for d in ds:
            if abs(d)>bound:continue
            P=(a,b,c,d);row=calculate(P);inputs+=1;maxlen=max(maxlen,len(row['word']))
            key=row['canonical_basis']
            if key in fans:ck('all identical-fan arrows retain value',fans[key]['physical_class_mod28']==row['physical_class_mod28'])
            fans[key]=row
    traversals=[independent_traversal(j) for j in (-3,-1,0,1,3)]
    # Witnesses are built in the single actual T0 component, independently
    # of any other vertical seed. Each full path and native increment stays.
    witnesses={};queue=deque([(ID,())]);depth=0
    while queue and len(witnesses)<28:
        P,ww=queue.popleft();row=calculate(P,True);r=row['physical_class_mod28']
        ck('witness is in actual initial component',row['vertical_index']==0)
        if r not in witnesses:witnesses[r]=row
        depth=max(depth,len(ww))
        ck('finite witness search remains bounded',len(ww)<=14)
        if P==ID:queue.append((Q0,(0,)))
        else:
            for i,Q in enumerate((Q0,Q1)):queue.append((mul(P,Q),ww+(i,)))
    ck('explicit witnesses cover every target class',set(witnesses)==set(range(28)))
    md=['# Explicit selected-I3 witnesses for every physical class','',
        'Every row starts at the actual T0 family. A word lists the successive native C0/C1 flops. The integer column is the full unreduced path sum, beginning at8; the complete step records and full coefficient exponents are in the companion JSON.','',
        '| Physical class | Basis P (rows) | Native word | Integer path sum |',
        '|---:|:---|:---|---:|']
    tex=[r'\begin{center}',r'\small',r'\begin{longtable}{rlll}',
         r'Class & Basis $P$ & Native word & Integer sum\\\hline']
    for residue,row in sorted(witnesses.items()):
        a,b,c,d=row['canonical_basis'];ww=','.join(map(str,row['word'])) or 'empty'
        md.append(f'| {residue} | ({a},{b}; {c},{d}) | {ww} | {row["integer_path_sum"]} |')
        bm=rf'$\left(\begin{{smallmatrix}}{a}&{b}\\{c}&{d}\end{{smallmatrix}}\right)$'
        tex.append(f'{residue} & {bm} & {ww} & {row["integer_path_sum"]}'+r'\\')
    tex.extend([r'\end{longtable}',r'\end{center}'])
    table_md='notes/part3_e6_selected_i3_all_fan_witness_table.md'
    table_tex='notes/part3_e6_selected_i3_all_fan_witness_table.tex'
    (ROOT/table_md).write_text('\n'.join(md)+'\n');(ROOT/table_tex).write_text('\n'.join(tex)+'\n')
    examples=[calculate(P,True) for P in [ID,Q0,(2,-1,-1,1),(1,0,4,1),(3,-2,2,-1),(5,-3,-3,2)]]
    ck('fully marked two-flop example',examples[2]['integer_path_sum']==356 and examples[2]['physical_class_mod28']==20)
    deps=['notes/part3_e6_selected_i3_vertical_integer_working.md','notes/part3_e6_selected_i3_working.md','notes/part3_e6_selected_i3_outer_transfer_working.md','notes/part3_e6_selected_i3_first_flop_working.md','notes/part3_e6_selected_i3_vertical_fans_working.md','notes/part3_e6_selected_i3_moving_c2_working.md','records/blind_audit_e6_selected_i3_moving_c2.json',table_md,table_tex]
    proof=ROOT/'notes/part3_e6_selected_i3_all_fans_working.md'
    def sha(p):return hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
    out={'status':'PASS','utc':datetime.now(timezone.utc).isoformat(),'checks':sum(counts.values()),'check_counts':dict(counts),'script_sha256':sha(str(Path(__file__).relative_to(ROOT))),'source_sha256':hashlib.sha256(proof.read_bytes()).hexdigest() if proof.exists() else None,'geometric_status':'Full source/line/cap comparison is IVP.1--7. Root full AFI read and independent28-witness replay pass; final IVP independent gate is recorded separately. The arithmetic does not choose its integer seed from a residue.','dependencies':{p:sha(p) for p in deps},'entry_bound':bound,'unimodular_inputs':inputs,'canonical_fans':len(fans),'max_word_length':maxlen,'independent_traversals':traversals,'examples':examples,'all28_witnesses':{str(k):v for k,v in sorted(witnesses.items())},'witness_max_depth':depth,'bounded_fan_outputs':list(fans.values()),'full_units_order':['kappa','alpha','g','eta'],'scope':'Original selected-I3 M6,b1,m2,n1 fixed-scalar family; same finite character, root maps, complete reference and identity source closing throughout.'}
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:out[k] for k in ['status','checks','unimodular_inputs','canonical_fans','max_word_length','independent_traversals','witness_max_depth']},indent=2))
if __name__=='__main__':main()
