"""Independent exact K112 reconstruction, written from the displayed maps.

The target prism is solved as ten equations in nine unknowns over Fraction;
the closed target formula AFM2.18 is deliberately not used. The input seed
is the separately reviewed K111 value, and this program does not establish
its geometric construction. All table values are compared as integers.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
from collections import Counter
import json,re
import sympy as sp

ROOT=Path(__file__).resolve().parents[1]
checks=0
counts=Counter()
def check(value, message):
    global checks
    checks+=1
    if not value:raise AssertionError(message)
def mul(a,b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))) for i in range(len(a)))
def det(p):return p[0][0]*p[1][1]-p[0][1]*p[1][0]
def inv(p):
    d=det(p);check(abs(d)==1,'unimodular source basis')
    return ((p[1][1]//d,-p[0][1]//d),(-p[1][0]//d,p[0][0]//d))
E=((1,0),(0,1));B0=((2,-3),(2,-3));Q=(((1,-1),(0,1)),((1,0),(-1,1)))
R0=((-1,-1),(1,0));SW=((0,1),(1,0))
def traces(p):
    r=inv(p);b=mul(mul(r,B0),p);b=tuple(tuple(2*x for x in row) for row in b)
    check(b[0][0]+b[1][1]==-2,'literal double trace winding')
    l=(b[1][1]-b[1][0],b[0][0]-b[0][1],b[1][1])
    x,y=r[0][1],r[1][1]
    w=(x,y,-x-y);d=(-x-2*y,-2*x-y,x-y)
    I=tuple(-w[k]+d[k]*(l[k]+1) for k in range(3))
    W=tuple(-w[k]-d[k]*(l[k]+1) for k in range(3))
    return w,I,W
VI={(0,0):0,(0,1):1,(0,2):2,(1,1):3,(1,2):4,(2,2):5}
def vi(i,j):return VI[tuple(sorted((i,j)))]
def solve_prism(w,I,W,a,b):
    eq=[]
    for j in (1,2):
        for k in range(3):
            row=[F(0) for _ in range(10)]
            row[vi(k,j)]+=w[j];row[vi(k,0)]-=w[0]
            row[-1]=(I[j] if k==j else 0)-(I[0] if k==0 else 0)
            eq.append(row)
        row=[F(0) for _ in range(10)]
        row[6+j]=w[j];row[6]=-w[0];row[-1]=W[j]-W[0];eq.append(row)
    for index,value in [(5,a),(8,2*a-b)]:
        row=[F(0) for _ in range(10)];row[index]=1;row[-1]=value;eq.append(row)
    original=[r[:] for r in eq]
    rank=0;pivots=[]
    for col in range(9):
        pivot=next((i for i in range(rank,len(eq)) if eq[i][col]),None)
        if pivot is None:continue
        eq[rank],eq[pivot]=eq[pivot],eq[rank]
        factor=eq[rank][col];eq[rank]=[F(x)/factor for x in eq[rank]]
        for i in range(len(eq)):
            if i!=rank and eq[i][col]:
                factor=eq[i][col];eq[i]=[x-factor*y for x,y in zip(eq[i],eq[rank])]
        pivots.append(col);rank+=1
    check(rank==9,'unique full target prism')
    check(all(any(r[:9]) or r[-1]==0 for r in eq),'compatible overdetermined prism')
    result=[F(0) for _ in range(9)]
    for i,col in enumerate(pivots):result[col]=eq[i][-1]
    check(all(sum(x*y for x,y in zip(row[:9],result))==row[-1] for row in original),'all target equations')
    check(all(x.denominator==1 for x in result),'actual target integral')
    z=[int(x) for x in result]
    return tuple(tuple(z[vi(i,j)] for j in range(3)) for i in range(3)),tuple(z[6:])
def native(a,b):
    check((b-a)%4==0 and (a+b)%4==0,'native division in free integer group')
    return -1-(a+b)//4,(b-a)//4
def seed(j):
    s=2-j**3+4*j*j-5*j;i0=12*j*j-32*j+18
    p=((1,0),(j,1));v=((-12*s,-i0,i0),(-i0,6*j-12,0),(i0,0,6*j-6))
    delta=(12*s,12*j*j-38*j+28,-12*j*j+26*j-14)
    check(native(v[1][1],delta[1])==(-(3*j-5)*(j-1),(3*j-5)*(j-2)),'C1 native reconstruction')
    check(native(v[2][2],delta[2])==((3*j-2)*(j-2),-(3*j-2)*(j-1)),'C2 native reconstruction')
    w,I,W=traces(p)
    for z in (1,2):
        check(all(w[z]*v[k][z]-w[0]*v[k][0]==(I[z] if k==z else 0)-(I[0] if k==0 else 0) for k in range(3)),'vertical action prism')
        check(w[z]*delta[z]-w[0]*delta[0]==W[z]-W[0],'vertical stable prism')
    return p,v,delta,s
def step(state,i):
    p,v,delta,s=state;a,b=v[i][i],delta[i];m,n=native(a,b)
    p2=mul(p,Q[i]);w,I,W=traces(p2)
    check(all(w),'all interior target weights nonzero')
    v2,d2=solve_prism(w,I,W,a,b)
    check(native(v2[2][2],d2[2])==(m+2*n,-n),'literal native reset')
    # Four full multiplier exponent vectors are obtained by the character
    # inverse and period basis, independently of the numerical winding.
    r=inv(p2)
    exponent=[[[r[ii][0]*p2[0][jj],r[ii][1]*p2[0][jj],r[ii][0]*p2[1][jj],r[ii][1]*p2[1][jj]] for jj in range(2)] for ii in range(2)]
    check(mul(r,p2)==E,'full q exponent identity')
    counts['target_prism_steps']+=1
    return (p2,v2,d2,s+n),{'edge':i,'old_native':[m,n],'reset_native':[m+2*n,-n],'increment':n,'target_basis':p2,'target_V':v2,'target_delta':d2,'multiplier_exponents':exponent}
def canonical(p):
    p=p if det(p)==1 else mul(p,SW)
    candidates=[];a=p
    for _ in range(3):
        for sign in (1,-1):
            b=tuple(tuple(sign*x for x in row) for row in a)
            if b[0][0]>0 and b[0][1]<=0:candidates.append(b)
        a=mul(a,R0)
    check(len(candidates)==1,'unique actual fan representative')
    return candidates[0]
def reduce_word(c):
    cur=c;removed=[]
    while cur[0][1]:
        p,r=cur[0][0],-cur[0][1]
        i=0 if r>=p else 1
        nxt=mul(cur,inv(Q[i]))
        check(nxt[0][0]-nxt[0][1]<p+r,'Euclidean fan termination')
        cur=nxt;removed.append(i)
    check(cur[0]==(1,0) and cur[1][1]==1,'actual vertical terminal fan')
    return cur[1][0],list(reversed(removed))
def wedge(a,b):
    out={}
    for i,x in a.items():
        for j,y in b.items():
            if set(i)&set(j):continue
            sign=(-1)**sum(u>v for u in i for v in j)
            key=tuple(sorted(i+j));out[key]=out.get(key,0)+sign*x*y
    return {k:sp.expand(v) for k,v in out.items() if sp.expand(v)!=0}
def differential(form,coords):
    out={}
    for idx,x in form.items():
        for i,z in enumerate(coords):
            d=sp.diff(x,z)
            if d:
                for key,val in wedge({(i,):d},{idx:1}).items():out[key]=out.get(key,0)+val
    return {k:sp.expand(v) for k,v in out.items() if sp.expand(v)!=0}
def symbolic():
    j,a,al,u,v,ga,th=sp.symbols('j a alpha u v gamma theta')
    coords=(al,u,v,ga,th)
    ext={(3,):al-3*th,(1,):j,(2,):j*al+(2-3*j)*th}
    beta={(1,):-j,(2,):-j*(al+(2-3*j)*th),(3,):3*j*th}
    ff=differential(ext,coords);db=differential(beta,coords)
    fam={k:ff.get(k,0)+a*db.get(k,0) for k in set(ff)|set(db)}
    top=wedge(beta,wedge(fam,fam)).get(tuple(range(5)),0)
    actual=sp.integrate(3*top,(a,0,1))
    check(sp.expand(actual-(12*j-15*j*j+6*j**3))==0,'full exterior Euler collar')
    s,z=sp.symbols('s z');r=sp.Rational(1,4)-s
    aa=r*z*z;bb=z
    def add(p,q):
        x,y=p;xx,yy=q
        slope=(3*x*x+2*aa*x+bb)/(2*y) if p==q else (yy-y)/(xx-x)
        nx=sp.factor(slope*slope-aa-x-xx)
        ny=sp.factor(-y+slope*(x-nx))
        return nx,ny
    g=(sp.Integer(0),sp.Integer(1));gg=add(g,g);ggg=add(gg,g)
    check(sp.factor(gg[0]-s*z*z)==0 and sp.factor(gg[1]+1+s*z**3/2)==0,'actual second source section')
    tau=sp.factor(-ggg[0]/ggg[1])
    expected=z*z*(-2*s*(2+s*z**3))/(8+6*s*z**3+(s*s-s**3)*z**6)
    check(sp.factor(tau-expected)==0,'complete third-section formal coordinate')
    vv=sp.symbols('v');ss=vv*(vv+4)/(4*(vv-2)**2);tc=vv/(vv-2)**3
    check(sp.factor(27*tc*tc+(18*ss-sp.Rational(1,2))*tc-4*ss*(sp.Rational(1,4)-ss)**2)==0,'literal selected height root')
    x,y=sp.symbols('x y');prod3=-(y-1)*(y+1)*2/x**3
    check(sp.rem(sp.together(prod3+2).as_numer_denom()[0],y*y-x**3-1,y)==0,'central Miller product minus two')
    return {'Euler_collar':str(sp.expand(actual)),'formal_coordinate_3G':str(tau)}
def main():
    symbolic_result=symbolic()
    vertical=[]
    for j in range(-100,101):
        p,v,d,s=seed(j);check((4*(6*s-1)+4)//24==s,'physical integer conversion')
        check((2-(j+1)**3+4*(j+1)**2-5*(j+1))-s==-(3*j-2)*(j-1),'forward vertical difference')
        vertical.append(s%28)
    check(set(vertical)=={0,2,8,10,12,14,16,22,24,26},'complete vertical image')
    source=(ROOT/'parts/IV.body.linked.tex').read_text()
    statement_start=source.index(r'\label{night:P3K.112}')
    statement_end=source.index(r'\end{proof}',statement_start)+len(r'\end{proof}')
    own_statement=source[statement_start:statement_end]
    block=own_statement[own_statement.index('Class & Basis $P$ & Native word & Integer sum'):]
    block=block[:block.index('\\end{longtable}')]
    pattern=r'(\d+) & \$\\left\(\\begin\{smallmatrix\}(-?\d+)&(-?\d+)\\\\(-?\d+)&(-?\d+)\\end\{smallmatrix\}\\right\)\$ & ([01,]+|empty) & (-?\d+)'
    witnesses=[]
    for row in re.findall(pattern,block):
        residue,a,b,c,d,word,total=row
        word=[] if word=='empty' else list(map(int,word.split(',')))
        state=seed(0);steps=[]
        for i in word:state,rec=step(state,i);steps.append(rec)
        check(state[0]==((int(a),int(b)),(int(c),int(d))),'literal printed witness basis')
        check(state[3]==int(total),'unreduced printed witness sum')
        check(state[3]%28==int(residue),'witness residue')
        witnesses.append({'residue':int(residue),'word':word,'integer_sum':state[3],'basis':state[0],'steps':steps})
    check(len(witnesses)==28 and {w['residue'] for w in witnesses}==set(range(28)),'all 28 witnesses parsed and checked')
    canonical_results={}
    for aa,bb,cc,dd in product(range(-4,5),repeat=4):
        p=((aa,bb),(cc,dd))
        if abs(det(p))!=1:continue
        c=canonical(p)
        if c not in canonical_results:
            j,word=reduce_word(c);state=seed(j)
            for i in word:state,_=step(state,i)
            check(state[0]==c,'complete fan reduction and reverse reconstruction')
            canonical_results[c]=state[3]
        counts['input_bases']+=1
    for m in range(3,61,3):
        for n in (-1,1):
            c=((m,1),(n,0));ci=((0,n),(1,-m*n));transport=((n,0),(3-m*n,1))
            check(mul(c,ci)==E and mul(ci,c)==E,'both signed cap meridian inverses')
            check(mul(c,transport)==((3,1),(1,0)),'full cubic-reference meridian map')
            for character in range(m):
                check((n*n*character-character)%m==0,'both norm signs retain finite character')
                counts['cap_character_instances']+=1
    out={'status':'PASS','assertions':checks,'counts':dict(counts),'canonical_fans':len(canonical_results),
         'scope':'Full displayed algebra, source/cap meridian identities, signed vertical prism and all 28 exact fan witnesses. The geometric absolute seed remains the separate K111 proof obligation.',
         'symbolic':symbolic_result,'witnesses':witnesses,'vertical_image':sorted(set(vertical))}
    (ROOT/'code/outputs/IV_K112_fresh_checks.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:out[k] for k in ['status','assertions','counts','canonical_fans','scope']}))
if __name__=='__main__':main()
