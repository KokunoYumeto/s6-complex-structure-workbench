"""Recognize the explicit released_utc/derivation-hash receipt without editing it."""
from pathlib import Path
import datetime as dt,difflib,hashlib,json
R=Path(__file__).resolve().parents[1]
p=R/'code/S6_SERIES_PUBLISH_continuation2_admit_v2.py';old=p.read_text();new=old
guards=[(
"        assert dt.datetime.fromisoformat(freeze['created_utc']) < dt.datetime.fromisoformat(release['created_utc'])\n        assert release['freeze_receipt_sha256'] == target['freeze']['sha256']",
"        release_time_field = 'created_utc' if 'created_utc' in release else 'released_utc'\n        release_time = release[release_time_field]\n        assert dt.datetime.fromisoformat(freeze['created_utc']) < dt.datetime.fromisoformat(release_time)\n        if 'freeze_receipt_sha256' in release:\n            assert release['freeze_receipt_sha256'] == target['freeze']['sha256']\n            release_binding = 'explicit freeze-receipt hash'\n        else:\n            assert release_time_field == 'released_utc'\n            assert release['derivation_sha256'] == freeze['derivation_sha256']\n            assert release['target_proof_path'] == freeze['target_proof_path']\n            assert release['target_proof_sha256'] == freeze['target_proof_sha256']\n            assert release['order'] == 'release written only after immutable complete derivation freeze'\n            release_binding = 'exact derivation hash and target-proof path/hash; recorded released_utc'"),(
"        event_date = proposed_events.get('created_utc', proposed_events.get('proposed_utc', release['created_utc']))",
"        event_date = proposed_events.get('created_utc', proposed_events.get('proposed_utc', release_time))"),(
"                           original=target['original'], proposed=target['proposed'], scope=target['scope']))",
"                           original=target['original'], proposed=target['proposed'], scope=target['scope'],\n                           release_time_field=release_time_field, recorded_release_time=release_time, release_binding=release_binding))")]
for a,b in guards:assert new.count(a)==1;new=new.replace(a,b,1)
out=R/'records/S6_SERIES_PUBLISH_continuation2_release_schema_support.json';assert not out.exists()
diff=R/'records/S6_SERIES_PUBLISH_continuation2_release_schema_support.diff'
diff.write_text(''.join(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile=p.name+'.before',tofile=p.name+'.after')))
p.write_text(new)
sha=lambda b:hashlib.sha256(b).hexdigest()
receipt=dict(created_utc=dt.datetime.now(dt.timezone.utc).isoformat(),reason='032W raw release receipt explicitly names its event timestamp released_utc and binds the exact frozen derivation and target proof, rather than including the whole freeze-receipt hash. The immutable receipt is preserved.',
 exact_field_map={'release event time':'release.released_utc copied verbatim; compared to freeze.created_utc','frozen derivation':'release.derivation_sha256 equals freeze.derivation_sha256 equals the actual derivation bytes hash','released target':'release.target_proof_path and target_proof_sha256 equal freeze values and actual target bytes hash'},
 validation='The same complete target proof must occur in the original owning block; the freeze attestation forbids prefreeze target opening. Both original and proposed full blocks and every guarded edit remain hash-bound. The new schema adds no event or changes any timestamp.',
 script_path=str(p.relative_to(R)),before_sha256=sha(old.encode()),after_sha256=sha(new.encode()),exact_diff_path=str(diff.relative_to(R)),exact_diff_sha256=sha(diff.read_bytes()),source_ledger_changes=0,frozen_receipts_changed=0)
out.write_text(json.dumps(receipt,indent=2)+'\n')
cfgp=R/'records/S6_SERIES_PUBLISH_II_continuation2_batch41_config.json';cfg=json.loads(cfgp.read_text());cb=cfgp.read_bytes()
cfg['review_evidence'].append(dict(path=str(out.relative_to(R)),sha256=sha(out.read_bytes())))
cfgp.write_text(json.dumps(cfg,indent=2)+'\n')
(R/'records/S6_SERIES_PUBLISH_II_batch41_schema_binding_update.json').write_text(json.dumps(dict(created_utc=receipt['created_utc'],config_path=str(cfgp.relative_to(R)),before_sha256=sha(cb),after_sha256=sha(cfgp.read_bytes()),added_evidence=cfg['review_evidence'][-1]),indent=2)+'\n')
print(json.dumps(receipt,indent=2))
