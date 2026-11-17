#!/usr/bin/env python3
"""Update the live outcome table after the independently reviewed B.4.22--27."""
from pathlib import Path
root = Path(__file__).resolve().parents[1]
path = root / 'code' / 'refresh_report.py'
source = path.read_text()
replacements = {
'| B.3 |': '| B.3 | B.3.1–B.3.8; B.4.1–B.4.27 | Stated gluing refuted; global partial filling proved; origin open | The actual family extends properly over (P1 x Delta_r) minus {(infinity,0)}, with all overlap maps and their exact cocycle. A fixed-bidisc completion must have only three-dimensional vertical components over the missing origin. Its associated log-torus torsor cannot extend, even after finite coordinate roots and point blowups. No arbitrary analytic cap has been constructed or excluded. |',
'| B.4 |': '| B.4 | B.4.1–B.4.27 | Open, with local corner resolution and stronger necessary conditions | The actual linear Tate-line collar and its smooth fourfold corner resolution are proved. The exceptional curves cannot be removed by a proper closure over the fixed base; an untouched curve away from conductors would persist in nearby torus fibres. The unblown one-eigenvalue Hopf family has no proper analytic completion. Every component of a fixed-bidisc origin fibre must be vertical of dimension three. The specified log-torus obstruction survives finite base changes and all finite point blowups. A general cap need not be a log torsor; its construction or exclusion, descent and least exponent remain open. |',
'| Lead 5 |': '| Lead 5 | B.3.1–B.5.1; B.4.19–B.4.27 | Proposed gluing false; global partial replacement proved; origin open | All actual finite and punctured-cusp overlaps glue over the complement of the single origin. The local repaired collar and resolved corner are explicit. The remaining cap must have vertical components and evade the proved logarithmic and fixed-base Kato obstructions. The whole second-period action, proper origin completion and compact global filling remain open. |',
}
lines = source.splitlines()
for prefix, replacement in replacements.items():
    positions = [i for i, line in enumerate(lines) if line.startswith(prefix)]
    assert len(positions) == 1, (prefix, positions)
    lines[positions[0]] = replacement
source = '\n'.join(lines) + '\n'
old = "additional_reports = ['D_B4421_review_record.md', 'E_B_general_completion_attempt.md', 'D_exceptional_curve_closure_attempt.md']"
new = "additional_reports = ['D_B4421_review_record.md', 'E_B_general_completion_attempt.md', 'D_exceptional_curve_closure_attempt.md', 'B_log_torsor_report.md', 'D_hopf_resonance_source_audit.md', 'B_origin_fibre_dimension_report.md', 'B_log_base_modification_report.md', 'root_ninth_hour_audit.md']"
assert old in source
source = source.replace(old, new, 1)
path.write_text(source)
print('Updated B.3, B.4 and Lead 5 through B.4.27; added the full ninth-hour proof and source audit records.')
