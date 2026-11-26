#!/usr/bin/env python3
"""Read-only identification of the complete admitted 039U input."""
from pathlib import Path
import hashlib
import S6_SERIES_PUBLISH_c8_integrate_presentation as presentation

ROOT = Path(__file__).resolve().parents[1]
source_path = ROOT / 'agents/continuation8_iii_integration/units/root/regular_quotients.tex'
receiver_path = ROOT / 'agents/continuation5_iii_carriers/S6_SERIES_PUBLISH_III_039U_receiving.tex'
source = source_path.read_text()
receiver = receiver_path.read_text()
start = source.index(r'\begin{theorem}')
assert source[start:] == receiver + '\n'
proof_start = receiver.index(r'\begin{proof}')
proof_end = receiver.index(r'\end{proof}', proof_start) + len(r'\end{proof}')
print('Input lines', len(source.splitlines()), 'sha256', hashlib.sha256(source.encode()).hexdigest())
print('Receiver lines', len(receiver.splitlines()), 'sha256', hashlib.sha256(receiver.encode()).hexdigest())
print('Exact residual difference after the three relocation headings: one final LF after the receiving block.')
print('Complete receiving block matches, with that final separator retained:', source[start:-1] == receiver)
print('Complete proof lines', len(receiver[proof_start:proof_end].splitlines()))
headers, edits, issues = presentation.statement_records_to_small_tags(source)
candidate, equations, equation_issues, aliases = presentation.remove_manual_equation_tags(headers)
literals = presentation.unresolved_literal_equation_references(candidate, aliases)
print('Bounded helper header edits', len(edits), 'equation edits', len(equations))
print('Manual display tags', ','.join(aliases))
for issue in issues + equation_issues + literals:
    print('Semantic review', issue.line, issue.kind, issue.token, issue.detail)
print('No file writes; no proof credit or publication criterion assigned.')
