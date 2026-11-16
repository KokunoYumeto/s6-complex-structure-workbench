"""Register the independently audited mixed3-primary smooth classifications."""
from pathlib import Path
import csv,json,datetime
root=Path(__file__).resolve().parents[1]
p=root/'sections/manifolds.tex';s=p.read_text()
inc=r'\input{code/manifolds_three_mixed_smooth_proof}'
if inc not in s:
    marker=r'\subsection{D.3. Moving the zero of the linearization}'
    assert marker in s
    p.write_text(s.replace(marker,inc+'\n\n'+marker))
fields=['id','statement','status','where_proved','depends_on','item_of_the_prompt','findings_of_the_survey_settled','notes']
p=root/'records/manifolds_root_results.csv';rows=list(csv.DictReader(p.open()))
assert not any(r['id']=='D.2.42' for r in rows),'Refuse duplicate registration.'
rows.append(dict(zip(fields,[
    'D.2.42',
    'All14 minimal residual-c=6,15,30 patterns on12 marked initial rows have complete simply connected oriented smooth types: c6 is M_conic#M_(3,0), c15 is M_(3,0)#Z_(5,epsilon), c30 is M_conic#M_(3,0)#Z_(5,0). The c15 orbit is epsilon0 for a1 and1 for a2. All allowed finite multiplicities, affine twists and ordinary clutches are included with primitive multiplicative Mumford caps and no extra regular logs.',
    'Proved','code/manifolds_three_mixed_smooth_proof.tex; sections/manifolds.tex',
    'D.2.26; D.2.35; D.2.36; D.2.38; D.2.39; D.1.10; Zhubr Theorems3and5; Thomas56 odd Pontryagin cube',
    'D.2','F26',
    'Full root derivation and independent fourfolds proof/code audit PASS. Full3-primary mu0 is proved by relativeS1 Borel cohomology overZ9, not ordinarymod3 cube. Complete primary splitting determines all mixed refinements. Exact14patterns/12rows/464semicharacter checks/3finite normalrows and direct adaptedmatrix replay retained.'
])))
with p.open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
audit={'updated_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
       'statement':'D.2.42','decision':'Full independent proof/code audit PASS',
       'proof':'code/manifolds_three_mixed_smooth_proof.tex',
       'outputs':['code/manifolds_three_mixed_AH.out','records/fourfolds_three_mixed_AH_audit.out'],
       'checks':'14patterns,12rows,464semicharacter substitutions,3finite normalrows, all actual adapted matrices',
       'whole_invariant':'The3-primary projection vanishes in the fullZ9 target byThomas operation and the5-dimensional orbifold-pair comparison;2-primary conic class and5-primary0/1 refined orbit determine the complete bordism via coprime splitting',
       'scope':'All simply connected allowed finite orders/twists/clutch in precisely the14 listed minimal patterns; no extra regular logs or original multiplicative replacements'}
(root/'records/root_d42_completion_audit.json').write_text(json.dumps(audit,indent=2)+'\n')
with (root/'S6_04_MAPS_MANIFOLDS_report.md').open('a') as f:
    f.write('''\n\n## Post-checkpoint09: full three-primary and mixed smooth classifications\n\nD.2.39 computes the entire fundamental-class invariant in H6(K(Z/3,2);Z)=Z/9 for all eight minimal c=3 patterns. It vanishes. Thomas's exact odd-prime Pontryagin cube kills both relevant restrictions in full Z/9 coefficients; the remaining locally free circle-action pair has a five-dimensional quotient with isotropy prime to three, giving the required injective restriction in degree six. This proves the oriented model obtained by framed surgery on the graph of a degree-three sphere map and an equatorial sphere in S2xS4. The possible mixed elliptic Borel class is retained and is killed by Thomas's exact external-product formula, not by an assumption that it vanishes.\n\nD.2.42 applies that full invariant and the proved coprime spin-bordism splitting to all14 minimal c=6,15,30 patterns. The resulting connected sums are given in its complete table. An independent proof audit and exact12-row algebraic replay passed. Among the162 potentially simply connected minimal patterns,144 now have smooth classifications: the remaining18 are the5 c=4,8 c=8 and5 c=20 patterns. This is not a completion of the broader D.2 request; original multiplicative replacements, additional regular logarithms and the broader weighted smooth sectors retain the stated remaining tasks.\n''')
print(json.dumps(audit,indent=2))
