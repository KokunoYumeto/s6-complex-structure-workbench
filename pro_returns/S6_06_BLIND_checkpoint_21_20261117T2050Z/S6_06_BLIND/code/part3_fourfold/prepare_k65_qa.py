#!/usr/bin/env python3
"""Create the isolated K65 QA runner from the established full-page pipeline."""
from pathlib import Path
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parents[2]
source=ROOT/'code/part3_fourfold/qa_scalar_outer_clutch_audit.py'
with (ROOT/'records/literature_fourfold.md').open('a') as log:
 log.write('\n- '+datetime.now(timezone.utc).isoformat()+' — Opened own K61 standalone QA runner. Reason: prepare the same isolated compile, render and all-page audit for K65. Material: verified preamble/runtime, compilation and image-audit pipeline.\n')
s=source.read_text().replace('K61','K65').replace('k61','k65').replace('P3K.61','P3K.65')
s=s.replace('part3_scalar_outer_clutch_obstruction.tex','part3_os49_corrected_returns.tex')
s=s.replace('audited source, fan, cap, excision and return proof','complete actual source/cap/native-trace/shorter-endpoint return proof')
(ROOT/'code/part3_fourfold/qa_os49_corrected_returns.py').write_text(s)
print('Created isolated K65 QA runner; master files untouched.')
