from pathlib import Path
import csv,datetime,json,hashlib
r=Path(__file__).resolve().parents[1]
out=r/'records/S6_SERIES_PUBLISH_I_root_betti_CHECK_EVENTS.tsv'
assert not out.exists()
who='GPT-6 Astra (OpenAI), ChatGPT Pro mode, reasoning effort inherited (no separate numeric setting exposed), S6_SERIES_PUBLISH root'
rows=[]
for lab,kind,suffix,outcome in [
 ('ari:C.8.9','targeted proof check','C89-derivation','Statement-directed derivation frozen before target proof; all four printed steps compared. Positive Betti Jacobian, global current/mass/no-atoms and both finite density coefficients agree. Prior common-normalization and local-expansion exposure disclosed.'),
 ('ari:C.8.10','targeted proof check','C810-derivation','Statement-directed derivation frozen before target proof; all four steps compared using primary DeMarco--Mavraki theorem, degree normalization, bounded singular-fibre/formal multiplicities and exceptional-orbit averaging. Full divisor and individual-orbit conclusions pass.'),
 ('ari:C.8.9','computation or formal certificate','C89-real-calculation','Fresh exact real-coordinate Betti Jacobian/Gaussian Laplacian and two Puiseux density constants passed before target read; fresh radial cusp density/zero-flux verification passed after target read. Six assertions; scoped factors/coefficients only, no separate global-equidistribution claim.')]:
 rows.append({'statement_id':lab,'date':'2026-11-21','who':who,'type':kind,'outcome':outcome,
 'event_id':'publish-I-root-'+suffix+'-20261121','phase':'Paper I newly reached main dependencies',
 'source_file':'work/records/S6_SERIES_PUBLISH_I_C89_C810_root_comparison.md','source_row':'',
 'source_event_type':kind,'evidence_group':'publish-I-root-betti-targets-20261121'})
with out.open('w') as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t');w.writeheader();w.writerows(rows)
print(json.dumps({'path':str(out),'rows':len(rows),'sha256':hashlib.sha256(out.read_bytes()).hexdigest()}))
