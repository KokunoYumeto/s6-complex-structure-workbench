from pathlib import Path
import datetime as dt, hashlib, json

R = Path(__file__).resolve().parents[1]
source = (R / 'S6_SERIES_PUBLISH_II.tex').read_bytes()
s = source.decode()
p = s.index('\\label{cdp:st:C.2.D4.2}')
start = s.rfind('\\begin{proposition}', 0, p)
end = s.index('\\end{proposition}', p) + len('\\end{proposition}')
proof_end = s.index('\\end{proof}', end) + len('\\end{proof}')
block = s[start:proof_end]
assert hashlib.sha256(block.encode()).hexdigest() == '0d9f67da2888e82ca07785860e7ebf2ec3e62be92f392a8c620dc8fb95219148'
assert all(x not in block for x in ['night:P4.56', 'night:P4.57', 'P4.56', 'P4.57'])
stem = R / 'agents/continuation2_root/S6_SERIES_PUBLISH_II_BX_statement_for_XV_XW'
statement = s[start:end] + '\n'
assert not stem.with_suffix('.tex').exists()
stem.with_suffix('.tex').write_text(statement)
record = dict(recorded_utc=dt.datetime.now(dt.timezone.utc).isoformat(), source_sha256=hashlib.sha256(source).hexdigest(), statement_path=str(stem.with_suffix('.tex').relative_to(R)), statement_sha256=hashlib.sha256(statement.encode()).hexdigest(), complete_BX_block_sha256=hashlib.sha256(block.encode()).hexdigest(), completed_manifest='records/S6_SERIES_PUBLISH_II_clean_checks_56/manifest.json', completed_manifest_sha256='2354bdc6b0117954837d3acf80473640229412c14f43ef25d7d161478a8f1f5a', root_actual_reading='Complete current BX statement and proof reread, together with the complete batch56 root review. The prior BW/RAT.6 dependency audit remains applicable.', applicable_part='First rationality assertion only: a connected degree-two normalization-branch cover over a smooth rational ordinary-triple image, plus its degree-one remaining sheet, has rational smooth complete model; every scalar-zero multiplicity is included.', mathematical_dependencies=[dict(owner='cdp:st:C.2.D4.1', use='Normal tensor, normal-cone compact-core comparison and cyclic-cover/link comparison. Its completed proof and RAT.6 dependency were already audited; no XV/XW input.'),dict(owner='cdp:st:C.2.RAT.6', use='Exact cubic-suspension geometric-genus and exceptional-link bounds.'),dict(locator='cdp:eq:C.RD.2', owner='cdp:st:C.2.RAT.5', disposition='The cross-reference illustrates the tangent-root identification. BX item2 explicitly proves the needed identification itself: the generic branch and its tangent root define the same quadratic function field, and integral closure identifies their complete normal covers. CH Euler positivity is not invoked.'),dict(owner='cdp:st:A.5.19', disposition='Used for the last elliptic-ruled consequence only; that consequence is not needed by the proposed XV/XW check.')], target_hypothesis_map='Use the identity ambient threefold Y, f, full fibre mS and smooth rational curve A from the completed XU result. Its positive-genus horizontal H is the connected degree-two complete cover, and the unique vertical rational component is the degree-one remaining cover. Each identification is through the actual normalization maps.', target_proofs_transmitted=False, independent_events_added=0, source_changed=False)
stem.with_suffix('.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps({k:record[k] for k in ['statement_path','statement_sha256','complete_BX_block_sha256']}, indent=2))
