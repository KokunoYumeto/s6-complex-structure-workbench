#!/usr/bin/env python3
"""Actual E7 two-boundary source cone and every joint III*/II cap map."""
from pathlib import Path
import sys,json
import sympy as S
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'part3'))
from integer_chain import ints,hom,cone
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
OUT=Path(__file__).resolve().parent
def syms(M):return [[str(x) for x in row] for row in M.tolist()]
A=2*S.eye(7)
for i,j in [(0,1),(1,2),(2,3),(3,4),(4,5),(2,6)]:A[i,j]=A[j,i]=-1
marks=S.Matrix([2,3,4,3,2,1,2])
B=S.zeros(10);B[0,0]=B[9,9]=-1
B[0,1]=B[1,0]=B[9,1]=B[1,9]=1
B[2:9,2:9]=-A;B[9,7]=B[7,9]=1
assert B.det()==-1
E=S.eye(10);O,F,G=E[:,0],E[:,1],E[:,9]
rr=S.zeros(10,1);rr[2:9,0]=A.inv()[:,5]
phi=G-O-F+rr
assert (phi.T*B*phi)[0]==-S.Rational(1,2)
def section(n):
    corr=rr if n%2 else S.zeros(10,1)
    local=S.Rational(3,2) if n%2 else 0
    po=(S.Rational(n*n,2)-2+local)/2
    P=O+(po+1)*F+n*phi-corr
    ints(P);assert (P.T*B*P)[0]==-1
    return P
aff=F-E[:,2:9]*marks
Tp=S.eye(10);Tp[:,0]=G;Tp[:,9]=section(2)
for i,j in [(0,4),(1,3),(2,2),(3,1),(4,0),(6,6)]:Tp[:,2+i]=E[:,2+j]
Tp[:,7]=aff
assert Tp.T*B*Tp==B
Lstar=S.Matrix.hstack(aff,E[:,2:9]);Lii=F
L=Lstar.row_join(Lii)
Pstar=S.zeros(8)
for i,j in enumerate([6,5,4,3,2,1,0,7]):Pstar[j,i]=1
P=S.diag(Pstar,S.eye(1))
assert Tp*L==L*P
result={'source':'y^2=x^3+t*x-t, G=(1,1)','NS_gram':ints(B),'translation_plus_G':ints(Tp),
        'component_inclusion':ints(L),'cases':[]}
ks,ki,ns,ni,ms,mi=S.symbols('kappa_star kappa_II n_star n_II m_star m_II',integer=True)
seif=S.Matrix([[1,0,-1,0],[0,1,0,1],[ns,-ms,0,0],[0,0,ni,-mi]])
D=mi*ns+ms*ni
assert S.expand(seif.det())==-D
for a,b in [(2,1),(1,2)]:
    T=Tp**(-b);Pc=P**(-b)
    M=section(a)-O
    assert T*M-M==-F
    dims={0:1,1:9,2:10,3:2,4:1}
    ds={1:S.zeros(1,9),2:L.T*B,3:S.zeros(10,2),4:S.ones(2,1),5:S.zeros(1,0)}
    fs={0:S.eye(1),1:Pc.inv().T,2:T,3:S.eye(2),4:S.eye(1)}
    wd,wdims=cone(ds,fs,dims)
    WH={j:hom(wd[j],wd[j+1]) for j in range(1,5)}
    case={'a':a,'b':b,'line':ints(M),'source_action':ints(T),
          'source_differentials':{str(j):ints(x) for j,x in ds.items()},
          'orbit_differentials':{str(j):ints(x) for j,x in wd.items()},
          'exterior_groups':{str(j):WH[j][0] for j in WH},
          'exterior_representatives':{str(j):ints(WH[j][1]) for j in WH},
          'exterior_projections':{str(j):ints(WH[j][2]) for j in WH},'boundaries':{}}
    parts=[]
    for index,(name,Li,Pi,mult) in enumerate([
        ('IIIstar',Lstar,Pstar**(-b),S.Matrix([1,*list(marks)])),
        ('II',Lii,S.eye(1),S.ones(1,1))]):
        count=Li.cols;J=Li.T*B*Li
        ndims={0:1,1:count,2:count,3:1}
        nd={1:S.zeros(1,count),2:J,3:S.zeros(count,1),4:S.zeros(1,0)}
        nf={0:S.eye(1),1:Pi.inv().T,2:Pi,3:S.eye(1)}
        ed,edims=cone(nd,nf,ndims)
        EH={j:hom(ed[j],ed[j+1]) for j in range(1,5)}
        emb=S.zeros(9,count);start=0 if index==0 else 8
        emb[start:start+count,:]=S.eye(count)
        inc={0:S.eye(1),1:emb,2:Li,3:S.eye(2)[:,index],4:S.zeros(1,0)}
        iw={j:S.diag(inc.get(j,S.zeros(dims.get(j,0),ndims.get(j,0))),
                     inc.get(j-1,S.zeros(dims.get(j-1,0),ndims.get(j-1,0)))) for j in range(1,5)}
        for j in range(2,5):assert wd[j]*iw[j]==iw[j-1]*ed[j]
        maps={j:WH[j][2]*iw[j]*EH[j][1] for j in range(1,5)}
        fcoord=EH[2][2]*mult.col_join(S.zeros(count,1))
        # Source alpha follows the O component.  N is the oriented
        # entire source-boundary class.  Fgamma is the full invariant fibre.
        alpha=S.zeros(count+1,1);alpha[0]=1
        gamma=S.zeros(count+1,1);gamma[count]=1
        N=S.zeros(count+1,1);N[0]=1
        Fg=S.zeros(count+1,1);Fg[1:,0]=mult
        marked={'alpha':EH[1][2]*alpha,'gamma':EH[1][2]*gamma,
                'N':EH[3][2]*N,'Fgamma':EH[3][2]*Fg}
        outmarked={key:maps[1 if key in ('alpha','gamma') else 3]*z for key,z in marked.items()}
        orders=EH[2][0];tors=[i for i,o in enumerate(orders) if o];free=[i for i,o in enumerate(orders) if not o]
        assert len(free)==2 and len(tors)<=1
        fc=S.Matrix([fcoord[i] for i in free])
        div=2 if index==0 and b==1 else 1
        fv=fc/div;assert all(x.q==1 for x in fv)
        U,V,g=S.gcdex(fv[0],fv[1]);assert g==1
        basis=S.Matrix([[fv[0],-V],[fv[1],U]])
        assert basis.det()==1
        change=S.diag(S.eye(len(tors)),basis)
        adapted=maps[2]*change
        cap=S.Matrix([[0]*(len(tors))+[1,ks if index==0 else ki]])
        rec={'groups':{str(j):EH[j][0] for j in EH},
             'differentials':{str(j):ints(x) for j,x in ed.items()},
             'inclusions':{str(j):ints(x) for j,x in iw.items()},
             'maps':{str(j):ints(x) for j,x in maps.items()},
             'marked_boundary':{key:ints(z) for key,z in marked.items()},
             'marked_exterior':{key:ints(z) for key,z in outmarked.items()},
             'fibre_H2':ints(fcoord),'H2_change':ints(change),'H2_adapted':ints(adapted),
             'cap_H2_adapted':syms(cap)}
        case['boundaries'][name]=rec
        parts.append((adapted,cap,outmarked))
    i2=parts[0][0].row_join(parts[1][0])
    cap2=S.diag(parts[0][1],parts[1][1]);D2=i2.col_join(-cap2)
    case['raw_complete_D2']=syms(D2)
    # The first target coordinate for b=2 has order two.  Reduce its
    # integer representatives in that actual finite target before using
    # a determinant of a free lift as the isomorphism certificate.
    if b==2:
        assert WH[2][0][0]==2
        for col in range(D2.cols):D2[0,col]=int(D2[0,col])%2
    assert abs(S.expand(D2.det()))==1
    # Exact free marked normalization, retaining the raw maps above.
    X1=parts[0][2]['alpha'].row_join(parts[0][2]['gamma'])
    X3=parts[0][2]['N'].row_join(parts[0][2]['Fgamma'])
    assert abs(X1.det())==abs(X3.det())==1
    assert X1.inv()*parts[1][2]['alpha']==S.Matrix([-1,0])
    assert X1.inv()*parts[1][2]['gamma']==S.Matrix([0,1])
    assert X3.inv()*parts[1][2]['N']==S.Matrix([-1,0])
    assert X3.inv()*parts[1][2]['Fgamma']==S.Matrix([0,1])
    case['complete_D2']=syms(D2);case['D2_determinant']=str(S.expand(D2.det()))
    case['physical_H1_change']=ints(X1);case['physical_H3_change']=ints(X3)
    case['D1_free']=syms(seif);case['D3']=syms(seif)
    case['D4']=[[1,-1]];case['D0']=[[1,1],[-1,0],[0,-1]]
    if b==2:
        cc,dd=S.symbols('c_star d_star',integer=True)
        case['D1_full']=syms(S.Matrix([[0,1,0,-1,0],[0,0,1,0,1],
            [-1,-cc,-dd,0,0],[0,ns,-ms,0,0],[0,0,0,ni,-mi]]))
        case['D1_domain_orders']=[2,0,0,0,0];case['D1_target_orders']=[0,0,2,0,0]
    else:case['D1_full']=syms(seif)
    result['cases'].append(case)
    print('PAIR',a,b,'EXTERIOR',case['exterior_groups'])
    print('D2=',case['complete_D2'],'det=',case['D2_determinant'])
    for name,rrr in case['boundaries'].items():print(name,'marks=',rrr['marked_exterior'])
sample_count=0
for aa in range(1,10):
 for bb in range(1,10):
  for cc in range(-3,4):
   for dd in range(-3,4):
    if S.gcd(aa,cc)!=1 or S.gcd(bb,dd)!=1:continue
    M=seif.subs({ms:aa,mi:bb,ns:cc,ni:dd})
    sm=smith_normal_form(M,domain=ZZ)
    assert [abs(int(sm[i,i])) for i in range(3)]==[1,1,1]
    assert abs(int(sm[3,3]))==abs(bb*cc+aa*dd)
    sample_count+=1
result.update(status='PASS',symbolic_D1_D3_determinant=str(-D),supplementary_Smith_cases=sample_count)
(OUT/'iii_star_ii_joint.json').write_text(json.dumps(result,indent=2)+'\n')
print('PASS: every source-cone inclusion, all marked cycles, symbolic joint maps and',sample_count,'Smith cases.')
