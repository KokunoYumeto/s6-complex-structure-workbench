"""Exact rational recognition after a proved Gross--Zagier denominator bound.

All periods use Arb E4 and exact Weierstrass invariants. Both L-values use
MPFR intervals with directed rounding, explicit block Taylor bounds and
infinite tails. Heights are the independent Arb certificates from C.6.
The arithmetic integrality inputs are proved in records/B_C6_gz_lemma.tex.
"""
from pathlib import Path
from fractions import Fraction as F
import json,re,csv,math
from flint import arb,ctx

ctx.prec=512
ROOT=Path(__file__).resolve().parents[1];REC=ROOT/'records';CODE=ROOT/'outputs'
models={r['i']:r for r in json.loads((REC/'C_cm_exact_local_data.json').read_text())}
heights={r['index']:arb(r['height_O']) for r in json.loads((REC/'C_cm_height_arb.json').read_text())}
cases=[(2,3,-12,-11,-23,2,8),(4,7,-28,57,-31,2,32),
       (6,11,-11,21,-19,1,8),(9,43,-43,21,-19,1,16),
       (10,67,-67,217,-3,1,16),(11,163,-163,185801,-3,1,576)]

def invariants(a):
 a1,a2,a3,a4,a6=a;b2=a1*a1+4*a2;b4=a1*a3+2*a4;b6=a3*a3+4*a6
 c4=b2*b2-24*b4;c6=-b2**3+36*b2*b4-216*b6
 disc=(c4**3-c6**2)//1728
 assert c4**3-c6**2==1728*disc and c4>0 and disc
 return c4,c6,disc

def period(a,cm_d,rectangular):
 c4,c6,disc=invariants(a);T=arb(cm_d).sqrt()/(1 if rectangular else 2)
 r=(-2*arb.pi()*T).exp();q=r if rectangular else -r
 assert r<arb('0.0001')
 # E6 has positive sign at this reduced CM parameter. Use sigma_5(n)<2n^5
 # and n^5<=32^(n-1) to bound its absolute deviation from one.
 assert 1-1008*r/(1-32*r)>0
 M=100;sig=[0]*(M+1)
 for d in range(1,M+1):
  for n in range(d,M+1,d):sig[n]+=d**3
 e4=arb(1);qn=arb(1)
 for n in range(1,M+1):qn*=q;e4+=240*sig[n]*qn
 # sigma_3(n)<2n^3. Sum the polynomial-geometric tail exactly.
 a0=M+1
 tail=480*r**a0*(a0**3/(1-r)+3*a0*a0*r/(1-r)**2+
                  3*a0*r*(1+r)/(1-r)**3+r*(1+4*r+r*r)/(1-r)**4)
 e4+=arb(0,tail.upper());assert e4>0
 scale=2*arb.pi()*(e4/c4).sqrt().sqrt()
 ncomp=2 if disc>0 else 1
 direction=arb(1) if c6>0 else (T if disc>0 else 2*T)
 omega=ncomp*direction*scale
 return omega,dict(terms=M,E4=e4.str(80),E4_tail=tail.str(20),c4=str(c4),c6=str(c6),discriminant=str(disc),components=ncomp,Omega=omega.str(80))

def interval(path):
 s=path.read_text();lo=re.search(r'^L_lower (\S+)$',s,re.M);hi=re.search(r'^L_upper (\S+)$',s,re.M)
 assert lo and hi and 'PASS:' in s,path
 return arb(lo[1]).union(arb(hi[1]))

out=[]
for i,cm_d,cm_disc,d,D,tors,qtarget in cases:
 E=models[i]['model'];a1,a2,a3,A,B=E
 assert a1==a2==0
 # Complete the square, twist by odd D=1 mod4, and return to a3=0 or1.
 newa3=a3;newB=(D**3*(4*B+a3*a3)-newa3*newa3)//4
 aux=[0,0,newa3,D*D*A,newB]
 assert 4*newB+newa3*newa3==D**3*(4*B+a3*a3)
 ec4,ec6,edisc=invariants(E);ac4,ac6,adisc=invariants(aux)
 assert ac4==D*D*ec4 and ac6==D**3*ec6 and adisc==D**6*edisc
 omega,pdata=period(E,cm_d,i in [2,4]);omega_aux,adata=period(aux,cm_d,i in [2,4])
 assert (omega/omega_aux).overlaps(arb(cm_d*abs(D)).sqrt())
 central_file=CODE/(f'B_C6_central_file_{i}.out' if i!=11 else 'B_C6_central_11.out')
 L0=interval(central_file);assert L0>0
 r=L0/omega_aux;den=tors*adata['components'];z=(den*r).unique_fmpz();assert z is not None
 # This uniqueness identifies r because den*r is proved integral.
 exact_r=F(int(z),den);assert exact_r>0
 L1=interval(CODE/f'B_C6_derivative_{i}.out');h=heights[i];q=L1/(omega*h)
 Bden=4*abs(exact_r.numerator)
 assert q.contains(qtarget) and abs(q-qtarget)<arb(1)/Bden
 # q is rational with denominator <=Bden; a distinct rational differs
 # from this integer by at least1/Bden. Thus q=qtarget exactly.
 az=F(qtarget)*exact_r*(2 if edisc>0 else 1);aa=math.isqrt(az.numerator)
 assert az.denominator==1 and aa*aa==az.numerator
 item=dict(index=i,base_twist=d,Heegner_discriminant=D,auxiliary_model=aux,
           target_period=pdata,auxiliary_period=adata,Lprime=L1.str(80),
           L_aux=L0.str(80),r_aux_enclosure=r.str(80),r_aux_exact=str(exact_r),
           height_O=h.str(80),q_enclosure=q.str(80),denominator_bound=Bden,
           exact_q=qtarget,genus_trace_integer_absolute=aa,
           rational_separation_margin=(arb(1)/Bden-abs(q-qtarget)).str(30))
 out.append(item)
 print('INDEX',i,'auxiliary ratio',r.str(25),'EXACT',exact_r)
 print('q enclosure',q.str(50),'denominator bound',Bden,'EXACT q',qtarget)
 print('Genus trace square integer',aa,'PASS: unique rational in certified enclosure.')
(REC/'B_C6_exact_factors.json').write_text(json.dumps(out,indent=2)+'\n')
with (REC/'B_C6_exact_factors.csv').open('w',newline='') as f:
 w=csv.writer(f);w.writerow(['index','base_twist','Heegner_discriminant','exact_auxiliary_L_over_period','q_denominator_bound','exact_q','absolute_genus_trace_integer'])
 for r in out:w.writerow([r['index'],r['base_twist'],r['Heegner_discriminant'],r['r_aux_exact'],r['denominator_bound'],r['exact_q'],r['genus_trace_integer_absolute']])
print('PASS: ALL SIX REMAINING RATIONAL LEADING FACTORS ARE EXACTLY CERTIFIED.')
