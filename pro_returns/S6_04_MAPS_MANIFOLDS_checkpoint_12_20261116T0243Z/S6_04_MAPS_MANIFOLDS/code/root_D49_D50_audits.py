"""Persist independent root proof and replay audits for D49 and D50."""
from pathlib import Path
import datetime
import hashlib
import json

root = Path(__file__).resolve().parents[1]
assert '95' in (root / 'records/root_D49_star_log_audit.out').read_text()
assert '1638' in (root / 'records/root_D49_star_log_audit.out').read_text()
assert 'ALL 16 marked examples passed' in (root / 'records/root_D50_corrected_examples_audit.out').read_text()
assert 'PASS 227 local pairs; 5696 global residues; 82 actual component cocycles' in (
    root / 'records/root_D50_vertical_audit.out').read_text()
record = {
    'reviewed_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'D.2.49': {
        'decision': 'PASS: approved registration',
        'scope': 'Canonical n=1,3 zero-free star block, all m=2k, all integer phase and affine twists with primitive gamma power; full local boundary map and the stated one-star global family.',
        'proof': 'code/manifolds_star_log_caps_proof.tex',
        'independent_geometric_checks': [
            'Actual root translation norm, extension over every toric stratum and primitive gamma freeness.',
            'Normalization/conductor incidence tree, odd sphere bundles at fixed vertices, exact bisection and fixed-edge degrees.',
            'Integral H2 presentation, absence of hidden H1 bridges, and the aspherical cap group.',
            'Independently derived H2(Gamma)=Z z plus Z2 t and the beta-long torus bar correction -kn z-(kn+aR)t.',
            'Independently expanded (beta g)^a for odd a; its endpoint period gives D1=z-t, forcing both fibre tau terms.',
            'Literal delta and long normal sweeps, including the j=j0+hq change L=-R D0+h tau.',
            'The exact kernel forces an even long-sweep coefficient in the no-fixed-vertex case; only then the h tau correction cancels.',
            'Full boundary cokernel is free, projected indices k,k/2,2k, and the all-order one-star Smith reductions are integral.',
        ],
        'root_replay': 'records/root_D49_star_log_audit.out',
        'counts': {'actual_positions': 12, 'normalization_comparisons': 95,
                   'one_star_Smith_cases': 1638},
        'peer': 'Fourfolds independently checked the delicate aspherical marking and integer phase correction.',
        'remaining_scope': 'Nonprimitive gamma root powers, other integral star blocks, and complete smooth classification of the new star outputs.',
    },
    'D.2.50': {
        'decision': 'PASS: approved registration',
        'proof': 'sections/fourfolds_D2_vertical_corrections.tex',
        'scope': 'All integral component corrections to section-difference line bundles on all21 MW=Z profiles; exact punctured monodromy and16 explicitly marked all-Mumford examples.',
        'root_geometry': [
            'Originated and proved the local invariant-multidegree equation (sigma-I)(c+JD)=0.',
            'Proved exact ambiguity ker((sigma-I)J)=ker(sigma-I) using the finite permutation norm and primitive multiplicity kernel.',
            'Generic trivialization extends to a vertical divisor; zero component intersections imply an integral whole-fibre divisor, hence an actual base pullback.',
            'Telescoping to hQ narrow fixes the added divisor literally and computes the exact base degree ab/d0.',
            'Proved the multiplicative discriminant criterion n divides pq; exact star cases and actual unit component maps give d0 divides ab.',
            'The h-fold punctured period comparison gives gamma_h=h gamma and A S=S A_h, hence the original D.GI2 matrix without assuming any cap covering.',
            'The16 new examples use only existing toric caps and full bar corrections; actual vertical normal closure plus ordinary gamma clutch proves simple connectivity.',
        ],
        'root_replays': ['records/root_D50_vertical_audit.out',
                         'records/root_D50_corrected_examples_audit.out'],
        'counts': {'local_pairs': 227, 'global_residues': 5696,
                   'actual_component_cocycles': 82, 'new_marked_filled_examples': 16},
        'result': 'Corrected initial compatibility iff d0 divides ab, with exact base degree ab/d0. OS45/default corrected pairs(2,4) and(4,2), four I1 zeros and both clutch signs have H2=H3=Z/b.',
        'remaining_scope': 'New corrected original-cap boundary maps and the smooth invariants of the new examples are not inferred from their homology.',
    },
}
for entry in record.values():
    if isinstance(entry, dict) and 'proof' in entry:
        entry['proof_sha256'] = hashlib.sha256((root / entry['proof']).read_bytes()).hexdigest()
(root / 'records/root_D49_D50_completion_audits.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
