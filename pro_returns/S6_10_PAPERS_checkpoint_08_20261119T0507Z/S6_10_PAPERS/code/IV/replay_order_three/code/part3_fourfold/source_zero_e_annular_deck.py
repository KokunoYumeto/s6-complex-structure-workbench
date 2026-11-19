from pathlib import Path
from datetime import datetime, timezone
import json
import sympy as s

root=Path(__file__).resolve().parents[2]
P,L=s.symbols('P L', nonzero=True)
checks=[]
for p in range(1,9):
    for k in range(1,9):
        for a,b,m in [(1,2,4*p),(2,1,4*p-1)]:
            N=k*m
            for n in [-1,1]:
                c=n*k
                perm=[(j-c)%N for j in range(N)]
                unseen=set(range(N)); lengths=[]
                while unseen:
                    q=next(iter(unseen)); cycle=[]
                    while q not in cycle:
                        cycle.append(q);unseen.remove(q);q=perm[q]
                    assert q==cycle[0]
                    lengths.append(len(cycle))
                assert len(lengths)==k and set(lengths)=={m}
                assert -m*c+n*N==0
                g0=2*(-1)**(b+1)*L*P
                if a==1:
                    # C source is P^(-2n)=Q^n, Q=P^-2.
                    assert s.simplify(P**(-b*n)/(P**(-2))**n)==1
                    normal=s.simplify(g0**n/P**n)
                    assert s.simplify(normal/((-2*L)**n))==1
                else:
                    # The flat frame Z*X includes the actual source multiplier.
                    normal=s.simplify(P**(-b*n)*g0**n)
                    assert s.simplify(normal/((2*L)**n))==1
                    assert s.simplify((P**(-n))**2/(P**(-2))**n)==1
                checks.append({'p':p,'k':k,'a':a,'b':b,'m':m,'n':n,
                               'cycles':k,'cycle_length':m,'normal':str(normal)})
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS',
     'rows':len(checks),'checks':checks,
     'scope':'Actual E-annulus deck and normal units only; no global collision-to-cap completion or source-zero return assigned.'}
(root/'code/part3_fourfold/source_zero_e_annular_deck.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='checks'},indent=2))
