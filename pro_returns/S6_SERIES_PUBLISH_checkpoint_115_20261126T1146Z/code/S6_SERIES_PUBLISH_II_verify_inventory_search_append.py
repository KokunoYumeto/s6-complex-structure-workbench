"""Apply the two reviewed search-field additions with exact multiline CSV data."""
from pathlib import Path
import csv,datetime,hashlib,io,json
R=Path(__file__).resolve().parents[1];csv.field_size_limit(100_000_000)
sha=lambda b:hashlib.sha256(b).hexdigest()
p=R/'S6_SERIES_PUBLISH_inventory.csv';rp=R/'records/S6_SERIES_PUBLISH_II_primary_reads_01_inventory_apply.json'
rec=json.loads(rp.read_text())
base=R/'agents/continuation_infra/metadata_I_20261121T182443860099Z/generated/S6_SERIES_PUBLISH_inventory.csv'
raw=base.read_bytes();assert sha(raw)==rec['before_sha256']
reader=csv.DictReader(io.StringIO(raw.decode(),newline=''));rows=list(reader);fields=reader.fieldnames
for row in rows:
 for c in rec['changes']:
  if row['paper']=='II' and row['label']==c['label']:
   assert row['literature_searches']==c['before'];row['literature_searches']=c['after']
def serialize(rows):
 s=io.StringIO(newline='');w=csv.DictWriter(s,fieldnames=fields);w.writeheader();w.writerows(rows);return s.getvalue().encode()
new=serialize(rows)
for row in rows:
 for c in rec['changes']:
  if row['paper']=='II' and row['label']==c['label']:row['literature_searches']=c['before']
assert serialize(rows)==raw,'Every unedited field and byte must be reversible.'
attempt=p.read_bytes();archive=R/'records/S6_SERIES_PUBLISH_II_inventory_search_attempt_before_repair.csv';assert not archive.exists();archive.write_bytes(attempt)
p.write_bytes(new)
rec['initial_attempt_sha256']=rec['after_sha256'];rec['after_sha256']=sha(new)
rec['exact_inverse_csv_bytes_verified']=True
rec['repair_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
rec['repair']='The first administrative write used splitlines before CSV parsing, which lost embedded newlines. Reconstructed the exact prior inventory from its hash-matched metadata copy, applied only the two reviewed literature_searches fields with StringIO(newline=""), and verified the inverse serialization equals every original byte. No mathematical field changed.'
rec['preserved_attempt']=str(archive.relative_to(R));rec['verified_original_copy']=str(base.relative_to(R))
rp.write_text(json.dumps(rec,indent=2)+'\n')
print(json.dumps(dict(after_sha256=sha(new),exact_inverse_csv_bytes_verified=True,only_two_fields_changed=True,administrative_repair_record=str(rp.relative_to(R)))))
