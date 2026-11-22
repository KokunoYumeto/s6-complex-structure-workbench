"""Bind the completed bounded root reading while final proposals remain open."""
from pathlib import Path
import datetime as dt, hashlib, json
R=Path(__file__).resolve().parents[1]
B=R/'agents/ii_checks_provenance/recovery_20261121T2000Z'
def bind(p):
    p=Path(p)
    if not p.is_absolute(): p=R/p
    return {'path':str(p.relative_to(R)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size}
index=json.loads((B/'clean_derivations/S6_SERIES_PUBLISH_II_boundary_freeze_index.json').read_text())
frozen=[]
for item in index:
    rec=json.loads((R/item['receipt']).read_text())
    f=bind(rec['frozen_derivation_path']); assert f['sha256']==rec['derivation_sha256']
    frozen.append({'tag':item['tag'],'receipt':bind(item['receipt']),'complete_frozen_derivation':f})
originals=[bind(B/'clean_group10'/f'S6_SERIES_PUBLISH_II_{tag}_original.tex') for tag in ['03IC','03IH','03IL','03IM','03DR','03IW']]
record={
 'recorded_utc':dt.datetime.now(dt.timezone.utc).isoformat(),
 'root_actual_complete_frozen_derivations_read':frozen,
 'root_actual_complete_original_pairs_read':originals,
 'root_actual_complete_program_read':bind(B/'clean_derivations/S6_SERIES_PUBLISH_II_boundary_preproof_exact.py'),
 'root_actual_all_output_rows_read':bind(B/'clean_derivations/S6_SERIES_PUBLISH_II_boundary_preproof_exact.output.json'),
 'root_actual_complete_input_receipt_read':bind(B/'clean_derivations/S6_SERIES_PUBLISH_II_boundary_prereading_input_receipt.json'),
 'root_actual_complete_convention_addendum_read':bind(B/'clean_group10/S6_SERIES_PUBLISH_II_boundary_deck_convention_addendum.json'),
 'arithmetic_scope':'Exact matrices, finite inverse-norm identity, contractions, quadratic shift and cocycle coefficient basis, all six divisor coefficients/degrees, full -2q Chern matrix, and symmetric support-form recovery read completely. The recorded polynomial degree bounds explain the tensor-grid checks. This does not claim comparison with an unidentified historical routine.',
 'explicit_method_comparisons':['IL derives E=nq directly; the printed proof first establishes E=2nq from its stated finite specialization lattice. Both lead to zero by the explicit contractions; the stronger specialization input is still subject to exact source binding.','IH frozen derivation subtracts the explicit reference cocycle E(lambda,A_g mu)/2; printed proof normalizes the vertical real central extension and gives every vector/root/universal-cover comparison. All printed endpoint and norm steps were read.'],
 'open_items':['Final proposed pairs and guards not yet available.','Root has not yet read the remaining four originals IE,ID,IN,I6 in this reading batch.','Current owning sources for integral degree-two local specialization and topological Leray E2/transgression values remain unresolved.','IC/IH must explicitly identify the left deck-module action and the endpoint-return inverse; IH positive cusp parametrization must be related to its clockwise boundary orientation.'],
 'new_check_events':0,'canonical_mutations':0,'root_primary_page_images_read':0,'manuscript_page_reading_credit':0,
 'scope':'This is a partial preintegration reading record, not a completed batch or whole-paper gate.'}
p=R/'records/S6_SERIES_PUBLISH_II_group10_root_preintegration_reading_01.json'
assert not p.exists();p.write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(bind(p)))
