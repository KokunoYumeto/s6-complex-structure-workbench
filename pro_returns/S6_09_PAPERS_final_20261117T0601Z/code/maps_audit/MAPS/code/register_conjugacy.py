"""Register the independently audited all-input conjugacy decision."""
from pathlib import Path
import csv,json,hashlib,shutil

root=Path(__file__).resolve().parents[1]
src=root/'code/fourfolds_integral_conjugacy_proof.tex'
text=src.read_text().replace('C_E(N)\\subseteq','E\\subseteq')
text += r'''

The exact execution certificate has twelve comparisons. Six algebraic
tests exercise the full $\operatorname{Mat}_3(\mathbb Q)$ quotient,
$\operatorname{Mat}_2(\mathbb Q)\times\mathbb Q$, a rational
multiplicity obstruction, a principal quotient whose lift has
determinant four, a nonprincipal ideal over $\mathbb Q(\sqrt{-5})$
with unconditionally certified class number two, and a cubic
centre with a certified rank-one unit group. Six further comparisons
use the actual admissible order-$(5,4)$ tuples with parameters
$0,1,2$: each is recovered after an explicit large unimodular
conjugation, and all three distinct pairs are rejected. Their word
traces $\operatorname{tr}(M_1M_2^3)=2,1,-10$ independently certify
the latter negative answers. All returned positive matrices satisfy
every exact intertwining equation and have determinant one.
'''
src.write_text(text)
(root/'sections/fourfolds_integral_conjugacy.tex').write_text(text)
section=root/'sections/fourfolds.tex'
s=section.read_text()
marker=r'\input{sections/fourfolds_integral_conjugacy}'
if marker not in s:
    s=s.replace(r'\input{sections/fourfolds_cap_chains}',
                r'\input{sections/fourfolds_cap_chains}'+'\n'+marker)
section.write_text(s)
path=root/'records/fourfolds_root_results.csv'
with path.open(newline='') as f:
    reader=csv.DictReader(f); fields=reader.fieldnames; rows=list(reader)
rows=[r for r in rows if r['id']!='F.2.36']
rows.append(dict(id='F.2.36',statement='Simultaneous integral conjugacy of every rank-six tuple containing a rank-three square-zero unipotent is decided exactly, with a returned unimodular conjugator or a certified obstruction; no entry or conjugator cutoff is used.',status='Proved',where_proved='sections/fourfolds_integral_conjugacy.tex',depends_on='Bley-Hofmann-Johnston2022 Theorem3.4 and Algorithm8.3; split-centralizer lemma; saturated integer kernels',item_of_the_prompt='F.2',findings_of_the_survey_settled='F30',notes='Proof and Julia reduction independently audited by the fourfolds agent. Twelve exact positive/negative comparisons passed, including6 actual admissible tuples; all class/unit groups certified with GRH=false. A complete comparison algorithm is distinguished from an executed global tabulation.'))
with path.open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
cache=root.parent/'external_cache/integral_conjugacy_runtime'
for name in ('Project.toml','Manifest.toml'):
    shutil.copyfile(cache/'env'/name,root/'records'/('conjugacy_runtime_'+name))
records={}
for name in ('fourfolds_integral_conjugacy.jl','test_fourfolds_integral_conjugacy.jl',
             'test_fourfolds_integral_conjugacy_retry03.out',
             'prepare_conjugacy_actual_tests.py','prepare_conjugacy_actual_tests.out',
             'test_fourfolds_conjugacy_actual.jl','test_fourfolds_conjugacy_actual.out'):
    p=root/'code'/name;records[name]={'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size}
(root/'records/conjugacy_audit.json').write_text(json.dumps({'statement':'F.2.36','proof_audit':'independent fourfolds agent PASS','exact_tests':12,'GRH_assumed':False,'files':records},indent=2)+'\n')
print(json.dumps({'registered':'F.2.36','tests_passed':12,'runtime':'Julia1.10.10; Hecke0.41.1'},indent=2))
