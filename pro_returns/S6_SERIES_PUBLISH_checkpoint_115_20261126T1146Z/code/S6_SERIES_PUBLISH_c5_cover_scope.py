#!/usr/bin/env python3
"""Record the reviewed statement scope for the three cusp-cover checks."""
import csv
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
P=ROOT/'S6_SERIES_PUBLISH_required_progress_III.tsv'
with P.open(newline='') as f:
    reader=csv.DictReader(f,delimiter='\t');fields=reader.fieldnames;rows=list(reader)
target={'037X','037Y','0382'}
for r in rows:
    if r['tag'] not in target:continue
    assert r['status']=='open' and not r['proof_released_utc']
    r['assigned_checker']='fifth continuation carriers checker /root/iii_02ja'
    r['statement_packet']='agents/continuation5_iii_infra/S6_SERIES_PUBLISH_III_037X_037Y_0382_claim_inputs.tex'
    r['statement_status']='manually_separated_statement_and_definitions_available'
    r['packet_status']='bounded_claim_inputs_available'
    r['source_ownership_status']='manually_reviewed_separate_theorem_and_two_following_argument_paragraphs'
    r['alias_clause_map']='037X: six-part theorem and its complete separate proof; 0382: following exact comparison paragraph; 037Y: following exact-scope paragraph. Each requires its own complete derivation and exact release scope.'
    r['notes']+=' Root supplied only the exact theorem, bounded fan/action definitions, and argument-free mathematical claims of the two paragraphs. The original ownership index is not overridden or treated as a proof release; a bounded individual release will record the exact source spans after completed fresh work.'
with P.open('w',newline='') as f:
    writer=csv.DictWriter(f,fields,delimiter='\t',lineterminator='\n');writer.writeheader();writer.writerows(rows)
print('Recorded bounded statement scopes for 037X, 037Y, 0382; all proofs remain embargoed and all three rows remain open.')
