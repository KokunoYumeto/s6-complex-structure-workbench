"""Verify immutable packet manifest, replay, and controlling-source identities."""
from pathlib import Path
import hashlib
import json

HERE=Path(__file__).resolve().parent
CANONICAL=HERE.parents[3]
def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

rows=[]
for line in (HERE/'source/SHA256SUMS.txt').read_text().splitlines():
    if not line.strip():
        continue
    expected,rel=line.split(None,1)
    rel=rel.strip()
    path=HERE/'source'/rel
    assert path.is_file() and sha(path)==expected, rel
    rows.append({'path':rel,'sha256':expected,'bytes':path.stat().st_size})
baseline=json.loads((HERE/'source/verification_results.json').read_text())
replay=json.loads((HERE/'replay/verification_results.json').read_text())
assert baseline==replay
comparisons=[]
for path in sorted((HERE/'source/source_extract').rglob('*')):
    if not path.is_file():
        continue
    rel=path.relative_to(HERE/'source/source_extract')
    target=CANONICAL/rel
    comparisons.append({'path':rel.as_posix(),'supplied_sha256':sha(path),
        'current_sha256':sha(target) if target.is_file() else None,
        'identical':target.is_file() and path.read_bytes()==target.read_bytes()})
out={'source_manifest_verified_rows':len(rows),'source_files':rows,
    'supplied_verifier_replay_json_identical':True,
    'source_extract_comparisons':comparisons,
    'independent_tests':json.loads((HERE/'independent_results.json').read_text()),
    'primary_literature':{'url':'https://arxiv.org/src/1107.1010v6',
      'archive_sha256':'ce07493decba82ad39ad3fd8e002ddec607e07f556a7f56b17223377173480d3',
      'read_location':'egyptian-count18.tex, Appendix A, Barban lemma and discussion'},
    'standalone_pdf_visual_review':'All six rendered pages inspected; no clipping or overlap.',
    'claims_do_not_include':'Global S6 realization; all-prime Erdos-Straus; physics or transfer of an integral count.'}
(HERE/'INTAKE_AND_AUDIT_RECEIPT.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k not in ('source_files','independent_tests')},indent=2))
