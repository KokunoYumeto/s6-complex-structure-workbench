#!/usr/bin/env python3
"""Record the final total-coordinate Picard sign in the live root audit."""
from pathlib import Path

root = Path(__file__).resolve().parents[1]
old = 'The normal factor a=exp(-2pi i mu) represents P; the independent scaling a^(-6) represents6P. These are distinct data and are correctly distinguished.'
new = ('In the stated total-coordinate convention W=exp(-2pi i zeta2), '
       'the normal factor a=exp(-2pi i mu) represents M^(-1)=O(O-P); '
       'the independent scaling a^(-6)=exp(12pi i mu) represents translation by6P. '
       'The final Picard-sign clarification was adopted before integration. '
       'These are distinct data and are correctly distinguished.')
for rel in ('sections/root_eighth_hour_audit.md', 'code/update_eighth_hour_report.py'):
    p = root / rel
    s = p.read_text()
    assert old in s, rel
    p.write_text(s.replace(old, new))
    print(rel, 'corrected the Picard label; exact coordinate factors unchanged')
