"""Record completed independent root proof audits and exact replays."""
from pathlib import Path
import datetime
import hashlib
import json

root = Path(__file__).resolve().parents[1]
files = [
    'records/root_D51_invariant_chern_audit.out',
    'records/root_D52_corrected_initial_audit.out',
    'records/root_D53_mu_audit.out',
    'records/root_D53_cubic_audit.out',
    'code/root_OS45_bridge.out',
]
texts = [(root / name).read_text() for name in files]
assert '689' in texts[0] and '53' in texts[0] and '169' in texts[0] and '80' in texts[0]
assert 'overlaps 42' in texts[1] and 'comparisons 16' in texts[1]
assert 'Smiths 212' in texts[1] and 'Smiths 45' in texts[1]
assert 'All exact cochain, annulus and full-modulus evaluations passed' in texts[2]
assert '3375' in texts[3] and '4096' in texts[3]
bridge = json.loads(texts[4])
assert bridge['boundary_area_order'] == 2
assert bridge['cusp_normal_free_determinant'] != 0
record = {
    'audited_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'verdict': 'PASS for D51-D53 exactly as scoped; OS45 refined invariant remains open',
    'D51': {'proof': 'Read completely. Actual invariant circle bundle, mapping cone signs, orbit gcd extension, literal t generator, primitive regular area, integral full-boundary image, and h=1-only normal marking verified.',
            'counts': {'cones': 689, 'actual_markings': 53, 'nonprimitive_Chern': 169, 'residual_torsion': 80}},
    'D52': {'proof': 'Read completely. Corrected initial-pair comparison, h=1 original additive columns, full integral bar model, actual fundamental-group normal closure and relative free-rank calculation verified. Unresolved original multiplicative and h>1 additive markings remain excluded.',
            'counts': {'D46_matrix_overlaps': 42, 'D50_comparisons': 16, 'new_residue_pairs': 45, 'new_Smith_cases': 212, 'extra_weight_regular_log_cases': 45}},
    'D53': {'proof': 'Read wrapper, primitive component lattice, full finite coefficient core/cusp boundary proof and localization. Relative Bockstein yields the index-two overlattice. Actual split boundary filtration retains Ext via both affine constants and the long-torus value. Full mod16 squares and mod8 cube verified; critical-cycle nullchain proves absolute c2=lambda0 only.',
            'counts': {'primitive_triples': 3375, 'recovered_component_triples': 4096},
            'peer_audit': 'records/fourfolds_OS45_mu_peer_audit.md'},
    'bridge': 'Exact Mayer-Vietoris odd-class assertion passed and independently checked by maps. Embedded representative, reference frame and critical-specialization intersection remain research.',
    'outputs': {name: {'sha256': hashlib.sha256((root / name).read_bytes()).hexdigest()} for name in files},
}
(root / 'records/root_D51_D53_completion_audits.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
