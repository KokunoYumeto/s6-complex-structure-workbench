from S6_SERIES_PUBLISH_c3_edit import *
import hashlib

apply_edit('Indeed $E_i^2<0$ by the preceding identity, and an integral curve',
    'Indeed $E_i^2<0$ by the negative definiteness just proved, and an integral curve',
    'II-C3-POLE-MATRIX-REFERENCE',['D04'],'night:P4R.6',
    'Conductor and exceptional pole divisor, item3',
    'After consolidation, the preceding item invokes the negative-definiteness lemma. Point the sentence to that exact conclusion instead of the removed displayed identity.')

outcomes = {
    'night:P4R.1': 'Complete original and receiving proof read. The exact proper-map neighbourhood retraction replaces its triangulation reproof. Restriction to U preserves r composed with i equal to identity. The semidirect-product, meridian normal closure, multiplicity and quotient maps are unchanged.',
    'night:P4R.6': 'Complete original and receiving proof read. P243 contains the same analytic principal-divisor intersection argument with its explicit diagonal change of variables. The receiving application uses the identical resolution pi:T to N and matrix. All conductor, reflexivity, adjunction, Morse-sphere and support arguments remain complete.',
    'night:P4.33': 'Complete original and receiving proof read. The ruled case now states the exact point-blowup, ruling, section and pole-support hypotheses already used in item4. Finite duality, analytic Serre duality, Leray and conductor-square formulas are unchanged; the exact descent q composed with rho_N equals a and section identity are preserved.',
    'night:P4.12': 'Original proof and receiving proof compared in full context. Only its repeated weighted intersection and inverse-matrix arguments move to earlier P243. Its application identifies the lemma surface N with S and retains this same minimal resolution pi and discrepancy equation.',
    'night:P4.14': 'Complete genus-one cubic proof read. Both local rings, conductor exponents, explicit involution/order-three automorphism, diagonal quotient and normalization inverse maps are unchanged. Its local ambient-threefold continuation now has numbered owner P242.',
    'rem:II:permuted-conductor-branches': 'Original entire orphan construction compared with the receiving remark. The two polynomial-preserving branch permutations, free elliptic translation, quotient map and finite conductor degrees two and three are preserved; no compact smoothing conclusion is introduced.',
}
for statement, outcome in outcomes.items():
    add_event(statement, 'II-C3-ROOT-CONDUCTOR-TOPOLOGY-' + statement.replace(':','-').replace('.','-'),
        'used and rechecked in this run', outcome,
        'S6_SERIES_PUBLISH_II.tex; S6_SERIES_PUBLISH_defects_II.tsv',
        source='code/S6_SERIES_PUBLISH_c3_conductor_topology_review.py')
for unit in ['night:P4R.1','night:P4R.6','night:P4.33']:
    for number in range(1,26):
        kind=f'D{number:02}'
        if kind in ['D10','D16']:
            continue
        status='open' if kind in ['D14','D23'] else 'done'
        detail=('Final whole-paper placement remains open.' if kind=='D14'
            else 'Integrated typesetting and final rendered-page reading remain open.' if kind=='D23'
            else 'Complete original and receiving unit read against this defect type; all found instances logged, with exact maps and proof scopes retained.')
        set_unit_status(unit,kind,status,detail,'code/S6_SERIES_PUBLISH_c3_conductor_topology_review.py')
    set_unit_status(unit,'structure','open','Local single ownership reviewed; final whole-paper placement remains open.',
        'code/S6_SERIES_PUBLISH_c3_conductor_topology_review.py')

path=ROOT/'S6_SERIES_PUBLISH_c3_primary_readings.tsv'
fields,rows=read_tsv(path)
source=ROOT/'agents/ii_checks_A/recovery_20261121T195642Z/S6_SERIES_PUBLISH_Bobadilla_Kollar_2012.p85.txt'
rows.append({
    'source':'Fernandez de Bobadilla–Kollar 2012',
    'url':'https://www.journalofsing.org/volume5/bobadilla-kollar.pdf',
    'version':'Journal of Singularities 5 (2012), 85–93; attached journal-page transcription',
    'locus':'Printed p.85, complete Definition1 and following neighbourhood-retraction paragraph',
    'date_utc':now(),
    'sha256':'text: '+hashlib.sha256(source.read_bytes()).hexdigest()+'; original PDF in attached retrieval record: 27072e45e1fcfd4d96b764eb070f4bf07207d906c35567b07cc06af0d63b1de4',
    'own_word_summary':'For a proper morphism of complex spaces, each fibre admits a neighbourhood in the base whose inverse image retracts onto that fibre. This supplies the retraction used to compare nearby fibres and the central fibre.',
    'use':'P4R.1: apply to f:X to disc, then restrict the supplied retraction to the inverse image of a smaller disc. This retains exactly the left-inverse relation used on fundamental groups.'})
for row in rows:
    if row['source']=='Mumford 1961':
        row['use']='P243: the short analytic adaptation has one lemma owner, using a local holomorphic principal divisor and its exact diagonal change of variables. P4.12, P4R.6 and A.5.20 apply it to their stated normal-surface resolutions.'
write_tsv(path,fields,rows)
print('Six exposed comparisons recorded; three full local all-class reviews closed 63 previously open defect rows.')
print('No independent-check credit; finite-conductor unit closure waits for its surface-classification consolidation.')
