"""Register the independently audited mixed-prime smooth classification."""
from pathlib import Path
import csv, json, datetime

root=Path(__file__).resolve().parents[1]
paper=root/'sections/manifolds.tex'
s=paper.read_text()
inc=r'\input{code/manifolds_mixed_prime_smooth_proof}'
if inc not in s:
    markers=[r'\input{code/manifolds_weighted_profiles_proof}',
             r'\input{code/manifolds_odd_prime_smooth_proof}']
    marker=next(m for m in markers if m in s)
    s=s.replace(marker,marker+'\n\n'+inc)
    paper.write_text(s)
fields=['id','statement','status','where_proved','depends_on','item_of_the_prompt','findings_of_the_survey_settled','notes']
p=root/'records/manifolds_root_results.csv'
rows=list(csv.DictReader(p.open()))
assert not any(r['id']=='D.2.38' for r in rows),'Refuse duplicate registration.'
rows.append(dict(zip(fields,[
    'D.2.38',
    'All12 minimal residual-c=10 or14 patterns on10 marked initial rows, with primitive multiplicative Mumford caps and no extra regular logs, are orientation-preservingly diffeomorphic to M_conic connected-sum Z_(p,epsilon), where Z_(p,epsilon) is the full odd-primary type ofD2.36. There are two c10 types and one c14 type, for every simply connected allowed finite order, affine twist and ordinary clutch.',
    'Proved','code/manifolds_mixed_prime_smooth_proof.tex; sections/manifolds.tex',
    'D.2.26; D.2.35; D.2.36; D.2.8; D.1.10; Zhubr Theorems3 and5',
    'D.2','F26',
    'Full root derivation and independent fourfolds proof/code audit PASS. The mod2 cube is1; odd mu0 and refined p=(w²−1)/2 in the actual curve-normalized generator. Proved K(Z2,2) wedge K(Zp,2) to product homotopy equivalence and the entire spin-bordism splitting, so no mixed refinement is suppressed. All12 patterns,736 semicharacter substitutions,10 full Tate rows and3 finite normal relations checked.'
])))
with p.open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
audit={
    'updated_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'statement':'D.2.38','status':'Independent full proof and exact-code audit PASS',
    'proof':'code/manifolds_mixed_prime_smooth_proof.tex',
    'outputs':['code/manifolds_mixed_prime_AH.out','records/fourfolds_mixed_prime_AH_audit.out'],
    'scope':'12 minimal patterns/10 rows; arbitrary simply connected allowed finite multiplicity, affine twist and ordinary clutch; primitive multiplicative Mumford caps and no extra regular logarithms',
    'primary':'Zhubr1975 full English primary text reopened: Theorem3 p795, Theorem5 p796 and definitions pp794–795',
    'new_comparison':'Chinese-remainder projections identify the full spin bordism with its2 andp parts. Connected sum is bordant to the disjoint union by one spin1-handle; complete classification applies with actual H2 isomorphism and b3=0.',
    'earlier_failed_computations':['manifolds_mixed_prime_AH_type_attempt.out','manifolds_mixed_prime_AH_expression_attempt.out','manifolds_mixed_prime_AH_basis_sign_attempt.out']
}
(root/'records/root_d38_completion_audit.json').write_text(json.dumps(audit,indent=2)+'\n')
p=root/'records/manifolds_mixed_prime_AH.json';d=json.loads(p.read_text())
d['status']='Exact local certificate; full smooth classification proved and independently audited inD2.38'
p.write_text(json.dumps(d,indent=2)+'\n')
with (root/'S6_04_MAPS_MANIFOLDS_report.md').open('a') as f:
    f.write('''\n\n## Post-checkpoint09: the mixed ten- and fourteen-torsion smooth types\n\nD.2.38 identifies every simply connected member of the twelve listed minimal patterns, with arbitrary allowed finite orders, twists and ordinary clutch, as the conic-surgery six-manifold connected-summed with the specified five- or seven-primary six-manifold of D.2.36. There are two c=10 types and one c=14 type. The proof computes the full mod-two invariant and the complete odd-primary data, then proves the splitting of the whole spin-bordism group by the actual Chinese remainder maps. Zhubr's Theorems 3 and 5 are applied after checking the H2 isomorphism, spin condition and zero middle Betti number. Thus a possible mixed refinement is not omitted. The root and an independent agent read the full proof and ran the exact ten-row/twelve-pattern certificate, including736 semicharacter substitutions and all three finite normal relations. The code and its earlier float-comparison, expression-expansion and primitive-basis-sign failures are retained. D.2 remains open beyond this precisely stated sector.\n''')
print(json.dumps(audit,indent=2))
