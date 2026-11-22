"""Record actual F5 prereading/comparison review, without check admission."""
from pathlib import Path
import datetime
import hashlib
import json

R = Path(__file__).resolve().parents[1]


def b(p):
    data = (R / p).read_bytes()
    return dict(path=p, sha256=hashlib.sha256(data).hexdigest(), bytes=len(data))


base = 'agents/ii_infra/recovery_20261121/'
freeze = 'agents/ii_infra/derivation_freezes/01F5/20261121T222622340438Z/S6_SERIES_PUBLISH_derivation_freeze_receipt.json'
release = 'agents/ii_infra/released_proofs/01F5/8f59f1260cf17d1b/S6_SERIES_PUBLISH_release_receipt.json'
f = json.loads((R / freeze).read_text())
r = json.loads((R / release).read_text())
assert r['freeze_receipt_sha256'] == b(freeze)['sha256']
assert b(f['frozen_derivation_path'])['sha256'] == f['derivation_sha256']
assert b(r['full_owning_block_path'])['sha256'] == r['full_owning_block_sha256']
scope = (
    'Root read all 314 lines of the frozen derivation first, then the freeze/release '
    'receipts and the entire released owning statement and twelve-item proof. Root '
    'read the entire prereading input receipt, complete fresh exterior-algebra program '
    'and every output field. Root actually viewed the complete Borcea printed pages '
    '379 and 380 and the complete Schroeer-Siebert author pages 2 and 3. These are '
    'four primary-source images; no Paper II page images were read. The other six '
    'Borcea image readings in the checker receipt belong to the checker. No claim '
    'to have read the next-page continuation of SS Lemma 1.1 is made.'
)
images = []
for doc, page, printed in [('Borcea1984', '08', 379), ('Borcea1984', '09', 380),
                           ('SS2002', '02', 2), ('SS2002', '03', 3)]:
    p = base + 'F5_F7_GD_primary_inputs/S6_SERIES_PUBLISH_II_' + doc + '_pdfp' + page + '.png'
    images.append(dict(document=doc, printed_page=printed, **b(p)))
out = dict(
    created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
    tag='01F5', owner='cdp:st:C.3.10', root_reading_scope=scope,
    freeze_receipt=b(freeze), release_receipt=b(release),
    frozen_derivation=b(f['frozen_derivation_path']),
    complete_original_owner=b(r['full_owning_block_path']),
    checker_prereading_receipt=b(base + 'S6_SERIES_PUBLISH_II_01F5_prereading_input_receipt.json'),
    fresh_program=b(base + 'S6_SERIES_PUBLISH_II_01F5_form_certificate.py'),
    complete_output=b(base + 'S6_SERIES_PUBLISH_II_01F5_form_certificate_output.json'),
    primary_images_actually_viewed=images,
    exact_maps_reviewed=[
        'The D1.9 coefficient map sends the actual integral transgression gamma to beta, with full-fibre restriction naturality.',
        'The D1.12 cup map identifies the quotient E/(O beta) with G.',
        'The fibre-integral identity uses i dt wedge dbar(t), Omega_t wedge bar(Omega_t), and i Omega_3 wedge bar(Omega_3), with the explicitly checked sign.',
        'The primitive local generator has a component with vanishing a<m; division by dt gives exponent a-m+1 and the sheet integral lower bound 4*u0^2*pi^2*r^4/m^2.',
        'The full Borcea homogeneous-coordinate matrix (17) has blocks M, (-2k/m)M, 0, eM; the displayed shear coefficients from (15) are absent. The final comparison must explicitly identify its cohomology-basis pullback.',
        'The invariant-form coefficient maps and Serre pairing determine the constant nonzero derivative of the second section in the intrinsic Picard quotient.',
        'The direct image of the actual exponential line bundle, followed by a base twist, produces ratios nonconstant on the regular fibre.'
    ],
    remaining_before_admission=[
        'Read the complete final comparison, every exact guard and the complete proposed owner.',
        'Bind the family Picard quotient, intrinsic alpha, descent-character convention and full H2 action to exact opened primary loci.',
        'Retain and map every C.PK.1--8 label/tag and all exact external receivers.',
        'Record the explicit smooth-domain repair with its receiver audit; do not invent a singular counterexample.'
    ],
    independent_checks_added=0, canonical_events_added=0, canonical_mutations=0,
    Paper_II_page_image_reading_credit=0)
p = R / 'records/S6_SERIES_PUBLISH_II_F5_root_reading_01.json'
assert not p.exists()
p.write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps(b(str(p.relative_to(R))), indent=2))
