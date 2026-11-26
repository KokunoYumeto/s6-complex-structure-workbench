#!/usr/bin/env python3
"""Record completed exposed readings in the local CHECK_EVENTS and defects files."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'agents/continuation8_iii_later'
UNITS = ROOT / 'agents/continuation8_iii_integration/units/later'
source = UNITS / 'further_cusp_carriers.tex'
limits = UNITS / 'limits_and_open_points.tex'
assert hashlib.sha256(source.read_bytes()).hexdigest() == '7c14f683021dce61503f2c5d7d79b711924b4f0daf4b365fb85de8c242f9ef5e'
defects = OUT / 'S6_SERIES_PUBLISH_III_carriers_publication_defects.tsv'
with defects.open(newline='') as stream:
    reader = csv.DictReader(stream, delimiter='\t')
    defect_fields, defects_rows = reader.fieldnames, list(reader)
assert len(defects_rows) == 74
for row in defects_rows:
    if row['change_id'] == 'c8-III-carriers-001':
        row['review_status'] = 'Whole original and identical relocated 037J block read; its publication rewrite remains pending with fixed_target_metrics; no final placement credit.'
    elif row['change_id'] in {'c8-III-carriers-025', 'c8-III-carriers-074'}:
        row['review_status'] = 'Whole final problem and exact edit row read; question remains open; actual final-part placement and global publication gates remain root-owned.'
    else:
        row['review_status'] = 'Whole repaired source, admitted comparison, final source and exact edit row read as exposed publication recheck; no independent or global/render/placement credit.'
with defects.open('w', newline='') as stream:
    writer = csv.DictWriter(stream, fieldnames=defect_fields, delimiter='\t', lineterminator='\n')
    writer.writeheader()
    writer.writerows(defects_rows)

readings = [
('0370', 'wb:cusp-cone-native-descent', 'Whole admitted and final descent proof read: logarithmic deck and inverse, exponentiation/local logarithms, pM0 identity, connected kernel, radial inverse and Gram/systolic formulas preserved.'),
('035X', 'wb:cusp-cone-S12-route', 'Whole admitted and final two-torus quotient proof read: all endpoint collars, onto map, based rotation and ordered source inverse, radial restriction, intrinsic balls, homology and local-homology obstructions preserved.'),
('0365', 'wb:cusp-cone-S24-local-route', 'Whole admitted and final localized-circle proof read. Four-circle metrics identified with the earlier owner by the coordinate concatenation isometry and inverse; full quotient, source and homology remain.'),
('036A', 'wb:cusp-cone-S24-route', 'Whole admitted and final finite-filled quotient proof read: both original finite targets, full overlap/root/shear inverse maps, clockwise meridians, reflection, integral Mayer-Vietoris matrix and primitive boundary kernel preserved.'),
('037N', 'wb:cusp-cone-target-slice-embeddings', 'Whole admitted definition-with-verification and final definition read. All map and inverse formulas remain; the entire embedding and endpoint proof is now Q30T. Attached manifold notation is consistently mathcal M.'),
('036W', 'wb:cusp-cone-metric-scope', 'Whole admitted and final metric proof read. Uniform compact radial collapse, shortest-period intrinsic bounds and the identity homeomorphism preserve the all-sufficiently-large-T failure of isometry.'),
('0374', 'wb:cusp-cone-obstructions', 'Whole admitted and final obstruction proof read. Same physical quotient identifies earlier bounded-period proof; all-power monodromy, nonnormal finite-cover saturation, M=1 endpoint, cover lattices, sections, singular completions and finite normal factorization remain.'),
('0375', 'wb:cusp-cone-optimal-exponents', 'Whole admitted and final minimum proof read. Primitive quotient/character duality, literal G*=H*=U inverse, full metric maps and remainder, equality kernels, kappa section, both finite fillings, C/M inverse and all radial/smash identities preserved.'),
('036J', 'wb:cusp-cone-angle-forgotten-sphere-carriers', 'Whole admitted and final sphere-target proof read: cube and skeleton inverses, degree-one collapse, exact fibres, two-stage metric equality, hyperplane projection and onto entire-ball isometries retained.'),
('037K', 'wb:cusp-cone-sphere-map-homotopy-status', 'Whole admitted and final remark read. Alpha explicitly belongs to Q011; beta and beta inverse identify whole maps including W/exterior. 02Q7 supplies exact based nullhomotopies. All graded, Hurewicz and ordinary-degree assertions preserved.'),
('035Z', 'wb:cusp-cone-S12-sphere-map-null', 'Whole admitted and final remark read. The earlier universal 038V square theorem applies to the actual based hat q3 through the displayed sphere coordinates; no new independent proof is claimed.'),
('036E', 'wb:cusp-cone-S24-sphere-map-null', 'Whole admitted proof and final factorization remark read. Sole earlier nullhomotopy owner applies after full marking comparison. All old anchors, twists/inverse, stable group locator, r>=2 values, initial quotient and radial metric maps preserved.'),
('036V', 'wb:cusp-cone-literal-R4-open-cells', 'Whole admitted and final open-cell proof read. Exact quotient restrictions, eta inverse, ambient projections, boundary sequence, finite diameter and entire-ball inverses preserve every topology and metric assertion.'),
('036Z', 'wb:cusp-cone-moving-S4-null-homotopy', 'Whole admitted and final height-homotopy proof read. All based sections, positive arclength coordinates, product quotient with time and fundamental-class maps preserved.'),
('036O', 'wb:cusp-cone-explicit-carriers', 'Whole admitted and final compact-cone proof read. Link/cone inverses, full embeddings and radial squares, contractions, oriented local-pair connecting maps and every manifold-chart obstruction preserved.'),
('037M', 'wb:cusp-cone-target-homotopy-types', 'Whole admitted and final homotopy-type proof read. Full finite-cap group, relative Hurewicz lift, based equivalences/inverses, all wedge multiplicities, Samelson words and null/nonzero surjective representatives remain. Neither specified raw class is determined; Q30V preserves that question.'),
('036N', 'wb:cusp-cone-exact-decompactification-space', 'Whole admitted and final decompactification proof read. Open quotient and closed relation, all charts and boundary components, exact entire-ball maps, beta/inverse and escaping half-period witness preserve the nonproper/nonquotient topology comparison.'),
('Q30P', 'mapsIII:def:cone-cusp-data', 'Whole new numbered definition read. It gathers the inherited fixed sphere map, cusp disc, quotient lattice, ordered basis and closed-ball convention before use; no new mathematical premise.'),
('Q30Q', 'mapsIII:def:two-torus-suspension', 'Whole new numbered definition read. It owns the inherited carrier A and its explicit radial rescaling with inverse; original equation anchors remain.'),
('Q30R', 'mapsIII:def:circle-suspension', 'Whole new numbered definition read. It owns the inherited carrier B with its base/character circles and explicit radial inverse; original equation anchor remains.'),
('Q30S', 'mapsIII:def:finite-filled-circle-carrier', 'Whole new numbered definition read. It includes the original pair-of-pants core, both original finite targets and full boundary gluing, remaining torus and attached cone with identity attachment.'),
('Q30T', 'mapsIII:lem:radial-slice-embeddings', 'Whole separated lemma and full proof read against the complete admitted 037N verification. The same angular/ordered-tuple inverses and all zero/outer endpoints remain. This is proof relocation and exposed recheck, not a fresh derivation.'),
('Q30U', 'mapsIII:problem:finite-cusp-cover-compactification', 'Whole final open problem read. Exact M>1 local degree-M^2 cover, additional branching, every pulled-back fibre normalization/resolution, lifted metric and total-space topology obligations retained. No solution or theorem closure claimed.'),
('Q30V', 'mapsIII:problem:raw-conical-quotient-classes', 'Whole final open problem read. Both specified geometric maps, source identifications and target groups are explicit. Actual pA and pC postcompositions give the known zero image classes; no raw class value inferred. No solution claimed.'),
]
stamp = datetime.now(timezone.utc).isoformat()
who = 'GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; numerical effort not separately exposed'
event_path = OUT / 'S6_SERIES_PUBLISH_III_carriers_publication_CHECK_EVENTS.tsv'
review_path = OUT / 'S6_SERIES_PUBLISH_III_carriers_publication_review.md'
fields = ['statement_id','date','who','type','outcome','event_id','phase','source_file','source_row','source_event_type','evidence_group','publish_input_file','publish_input_row','date_utc','where']
records = []
for i, (tag, sid, outcome) in enumerate(readings, 2):
    path = limits if tag in {'Q30U','Q30V'} else source
    text = path.read_text()
    marker = r'\label{' + sid + '}'
    assert text.count(marker) == 1
    line = text[:text.index(marker)].count('\n') + 1
    records.append(dict(statement_id=sid, date=stamp[:10], who=who,
        type='used and rechecked in this run',
        outcome=outcome + ' Exposed source-local reading only; no independent derivation, historical-output credit, required-row closure or global/render/placement credit.',
        event_id='publish:c8:III:' + tag + ':carriers-publication-recheck',
        phase='continuation8-later-publication', source_file=str(path.relative_to(ROOT)),
        source_row=str(line), source_event_type='used and rechecked in this run',
        evidence_group='publish:c8:III:later-unit-editing',
        publish_input_file=str(event_path.relative_to(ROOT)), publish_input_row=str(i),
        date_utc=stamp, where=str(review_path.relative_to(ROOT))))
with event_path.open('w', newline='') as stream:
    writer = csv.DictWriter(stream, fieldnames=fields, delimiter='\t', lineterminator='\n')
    writer.writeheader()
    writer.writerows(records)
print('Local exposed reading events:', len(records))
print('Exact defect rows with completed local reading status:', len(defects_rows))
print('037J publication work remains with fixed_target_metrics; Q30U/Q30V remain open problems.')
print('Event time:', stamp)
