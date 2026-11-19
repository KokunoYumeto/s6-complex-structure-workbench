"""Checkpoint metadata update after the connection, certified bound and fan obstruction."""
from pathlib import Path
import json
p=Path(__file__).parent
j=json.loads((p/'results_mapping.json').read_text())
new=[
{'id':'P1.15','status':'Proved','items':['1.4','1.7'],'value':'Explicit rational rank-six algebraic connection, global splitting and normalized period formula for h; exact residue normalization alpha=(625πi/128)alpha_alg','proof':'notes/part1.tex; de_rham_connection.py/.json/.out; cusp_residue_weight_bases.json'},
{'id':'P1.16','status':'Proved','items':['1.4','1.7'],'value':'Certified h_b(1)=−1.03427662241632179949424884537834605259… with enclosure radius 8.11e−57; closed-loop and independent Frobenius lifted periods agree to 93 digits; exceptional parameter 5/(3π) is inadmissible','proof':'notes/part1.tex; certified_lift_bound.py/.json/.out; frobenius_period_check.py/.json/.out; pencil_period_numerics.py/.json/.out; lift_period_values.py/.json/.out','limitation':'h_b(infinity)=−1.0945402503114027801162682630549457037… and numerical search favor it as global minimum; global-min proof still in progress.'},
{'id':'P1.17','status':'Proved','items':['1.7'],'value':'No anti-biholomorphism, hence no real structure, between any members completed using the fixed cusp marking S of P1.1 and its Kuhn fan','proof':'notes/part1.tex; real_structure_check.py/.out','scope':'The compactification marking is fixed; this statement does not identify differently marked toroidal completions.'}
]
ids={v['id'] for v in new};j['statements']=[v for v in j['statements'] if v['id'] not in ids]+new
j['in_progress']['1.4']='Explicit algebraic connection and independent lifted period computations complete, with interval certification h_b(1)<−1. Integral-primitive and literal-rank errors have their corrected exact maps.'
j['in_progress']['1.7']='Fixed-marking real-structure obstruction complete. Parent owns full analytic invariants, parameter injectivity, Kuranishi and endpoint limits. Global h minimum and normalization-shift numerical value remain under work.'
(p/'results_mapping.json').write_text(json.dumps(j,indent=2,ensure_ascii=False)+'\n')
md=p.parents[1]/'notes/part1.md'
old=md.read_text()
header='''# Current proof status (updated 2026-11-17 01:10 UTC)\n\nThe complete current derivations are in `notes/part1.tex`, statements P1.1–P1.17. The working notes below are retained as a chronological record; their earlier “under development” entries are superseded by those proofs. Current exact status and stated-value comparisons are in `code/part1/results_mapping.json`. Parent-owned analytic invariants and the classification of holomorphic parameters are in `notes/part1_analytic.tex`.\n\nThe remaining tasks owned here are a rigorous global minimum evaluation for the explicitly normalized function h_b, and the separately requested independent full global cellular comparison. The global integral homology theorem itself is already proved by actual low-degree Mayer–Vietoris maps and integral duality (P1.12), without assuming the unknown cusp suspension map vanishes.\n\n---\n\n'''
if not old.startswith('# Current proof status'):md.write_text(header+old)
print('Added P1.15–P1.17 and corrected the live status summary.')
