#!/usr/bin/env python3
"""Keep the pre-build integration check separate from the earlier draft13 audit."""
from pathlib import Path
import json
code = Path(__file__).resolve().parent
current = code/'deliverable_audit_draft13.json'
prebuild = code/'deliverable_audit_before_draft14.json'
raw = current.read_text()
data = json.loads(raw)
assert data['missing_in_registry'] == ['C.3.20'] and not data['passed']
assert not prebuild.exists()
prebuild.write_text(raw)
original = (code/'audit_deliverables_draft13.out').read_text()
prior = json.loads(original)
assert prior['passed'] and prior['build_tag'] == 'draft13'
current.write_text(original)
print('Retained the mid-integration check separately and restored the draft13 JSON from its original saved output.')
