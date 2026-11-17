"""Register the independently audited odd-primary smooth classification."""
from pathlib import Path
import csv,json,datetime
root=Path(__file__).resolve().parents[1]
source=root/'code/manifolds_odd_prime_smooth_proof.tex'
s=source.read_text().replace('and half\nthe equivariant Chern class','and the correspondingly scaled half of\nthe equivariant Chern class')
source.write_text(s)
p=root/'sections/manifolds.tex';s=p.read_text()
inc=r'\input{code/manifolds_odd_prime_smooth_proof}'
if inc not in s:
    marker=r'\input{sections/fourfolds_D2_c2}'
    assert marker in s
    s=s.replace(marker,marker+'\n\n'+inc)
    p.write_text(s)
fields=['id','statement','status','where_proved','depends_on','item_of_the_prompt','findings_of_the_survey_settled','notes']
p=root/'records/manifolds_root_results.csv'
rows=list(csv.DictReader(p.open())) if p.exists() else []
assert not any(r['id']=='D.2.36' for r in rows),'Refuse duplicate registration.'
rows.append(dict(zip(fields,[
 'D.2.36',
 'All36 minimal residual-c=5 or7 additive-filling patterns on30 marked initial rows, with primitive multiplicative Mumford caps and no extra regular logs, have a complete simply connected smooth classification at every allowed finite order and twist: two oriented types for c=5 and one for c=7. Their complete Zhubr invariants are H2=Z/p, b3=0, mu=0, and refined p in the0/1 automorphism orbit determined by the actual local normal weight w: zero iff w squared=1 modp.',
 'Proved','code/manifolds_odd_prime_smooth_proof.tex; sections/manifolds.tex',
 'D.2.26; D.1.10; Zhubr Theorem1; actual Tate markings; equivariant Thom localization',
 'D.2','F26',
 'Full independent proof audit by fourfolds agent and exact30-row program replay PASS. Wall sign ambiguity resolved by the actual unique cohomology generator with evaluation1 on the complex-oriented rational fixed curve; in that basis p1=-2(1-w^2), refined p=(w^2-1)/2, mu0. No original multiplicative replacements, extra regular logs, or higher weights are silently included.'
 ])))
with p.open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
audit={'updated_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'statement':'D.2.36','status':'Full independent proof and exact-code audit PASS',
 'reviewer':'fourfolds agent; root exact derivation and all source/code review',
 'proof':'code/manifolds_odd_prime_smooth_proof.tex',
 'executed_outputs':['code/manifolds_odd_prime_AH.out','records/fourfolds_odd_prime_AH_audit.out'],
 'normalization':'Actual u(C)=1 on the complex-oriented rational fixed curve; signed support wall value retained separately.',
 'scope':'36 patterns /30 rows; every simply connected allowed finite order/twist; primitive multiplicative Mumford caps; no additional regular logs',
 'earlier_failed_attempt':'An unnecessary h1-centering constant failed the exact inversion assertion. It was removed; the original h=z^(-2a) factor passes. Failed output retained as manifolds_odd_prime_AH_centering_attempt.out.',
 'primary':'Zhubr1975 Theorem1 and definitions pp794-795, reopened full primary PDF; D.1.10 proves full odd-prime H6(K(Z/p,2)) detection.'}
(root/'records/root_d36_completion_audit.json').write_text(json.dumps(audit,indent=2)+'\n')
print(json.dumps(audit,indent=2))
