"""Record complete first-part text readings without closing global proof gates."""
from S6_SERIES_PUBLISH_c3_edit import *

event = 'II-C3-FIRSTPART-STATEMENTS-OUTLINES-TEXT'
bases = {
    'D01': 'The complete two subsections state the mathematics without narration of drafts, runs or readings.',
    'D02': 'The hypotheses and scope clauses are positive mathematical conditions; no defensive draft comparison remains.',
    'D03': 'The nodal example is stated for its conormal maps and dimensions, with its full body owner; no prompt proposal is the subject of a statement.',
    'D04': 'All visible references use current statement numbers; permanent machine labels remain hidden in source arguments.',
    'D05': 'The integral CDP domain is numbered and the marked family conventions have their body owner; no prompt item is used as a mathematical reference.',
    'D06': 'All 49 outline links retain their exact labels and now print the current statement kind and number. Internal theorem and equation targets exist. Precise literature-version verification remains at D18.',
    'D07': 'No worker, agent or internal run is named in these mathematical subsections.',
    'D08': 'Each use of original, fixed, prescribed or retains refers to the displayed family, morphism, marking, multiplicity or attachment data. No production-state marker remains.',
    'D09': 'There are no program paths, data-file names, check counts, saved-matrix indices or execution options in either subsection.',
    'D11': 'The local, integral, compact and marked scopes stand in the hypotheses; no repeated statement disclaims an unproved neighbouring result.',
    'D12': 'The mandatory front main-theorem statements have one outline each, with their proofs at the identified body owners. No second proof is inserted here.',
    'D13': 'The standing integral assumptions are a numbered Definition. The only text outside the theorem blocks is the required mechanism and literature-status prose; every outline claim belongs to its theorem list.',
    'D17': 'The outlines identify the body argument and its exact maps; no textbook result is re-proved at length in these front units.',
    'D19': 'The front displayed summaries have no inherited manual equation tags; their body equations use unchanged current labels.',
    'D20': 'Full fibres F_b and supports S_b are distinguished by the explicit reduction map. Integer/noninteger Picard parameters, root coordinates and scalar covering maps retain their stated conversions.',
    'D21': 'The front states exact cohomology dimensions, identities, ranks and covering degrees. No numerical agreement is offered as a theorem.',
    'D22': 'The nodal radius now names the other discriminant value -4/27, verified from the same family equation. All other displayed values are the formulas or specified cases of the cited body owners.'
}
text = SOURCE.read_text()
a = text.index(r'\subsection{The proofs in outline}')
b = text.index(r'\subsection{Known and new}', a)
assert r'\hyperref[' not in text[a:b]
assert len(re.findall(r'\\cref\{', text[a:b])) == 49
for unit in ['series:II:main-theorems', 'series:II:outline']:
    for kind, basis in bases.items():
        set_unit_status(unit, kind, 'done', basis + ' Root read the complete old and final current unit. D10/D16 stand. D14/D15/D18/D23/D24/D25 and structure remain open for the global proof, provenance, layout and body correspondence gates.', 'CHECK_EVENTS.tsv: ' + event)
add_event('series:II:main-theorems;series:II:outline', event, 'used and rechecked in this run',
    'Root read the entire integral-domain definition, all seven full main-theorem statements, their mechanism and literature paragraphs, and every step of all seven outlines, before and after the bounded edits. The 49 outline target identities are unchanged and now use typed current references. The nodal discriminant explanation is the exact t=0,-4/27 calculation from the same body family. The sign-line grammar is corrected. All formulas, hypotheses, scope, covering maps and permanent identifiers remain. Seventeen local text classes close in each of the two stable existing units; D10/D16 stand. Final main-theorem derivation/body correspondence, literature/provenance, organization, typesetting and final-page gates remain open. No independent-check or required-check credit.',
    'Complete main-theorems and proofs-in-outline actual subsections', source=__file__)
add_event('cdp:st:C.2.UN.70;cdp:st:C.2.UN.83', 'II-C3-FURTHER-COMMON-MODEL-OWNER', 'used and rechecked in this run',
    'Compared both original Further-results entries with the entire admitted common surface-model statement and proof. Replaced their duplicate navigation by one line describing the elliptic, nonlinear Hopf and one-section ruled models. UN70 remains the exact nonnegative-coefficient specialization under its preserved label and permanent target. Full-list and organization closure remains pending.',
    'Further results; common torsion-normal boundary owner', source=__file__)
print('34 stable local text rows closed; global main-theorem and final gates remain open.')
