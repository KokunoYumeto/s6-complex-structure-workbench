"""Admit the fully compared root, cuspidal and Kummer occurrence units."""
from S6_SERIES_PUBLISH_c3_edit import *
import json

folder=ROOT/'agents/continuation3_occurrence_root'
prefix='S6_SERIES_PUBLISH_c3_occurrence_first_'
guards=json.loads((folder/(prefix+'guards.json')).read_text())
before=SOURCE.read_text();after=before
for row in guards:
    assert after.count(row['old'])==1,row['key']
    after=after.replace(row['old'],row['new'],1)
provenance=ROOT/'agents/continuation3_provenance'
_,programs=read_tsv(provenance/'S6_SERIES_PUBLISH_c3_provenance_program_edits160.tsv')
for row in programs:
    assert after.count(row['old_text'])==1,row['change_id']
    row['new_text']=row['new_text'].replace(
        r'Cuspidal self-product charts, the divisor intersection matrix and cohomology arithmetic (\cref{cdp:st:C.2.UN.8})',
        r'Cuspidal self-product charts, the divisor intersection matrix and cohomology arithmetic (\cref{cdp:st:C.2.UN.8,rem:II:cuspidal-generic-divisors})')
    row['reason']+=' Root has placed the exact generic divisor matrix at P334, so the receiving row cites both UN8 and that same-matrix owner.'
    after=after.replace(row['old_text'],row['new_text'],1)
sources=provenance/'final_sources'
_,bib=read_tsv(sources/'S6_SERIES_PUBLISH_rossi_bib161.tsv')
for row in bib:
    assert after.count(row['old_text'])==1,row['change_id']
    after=after.replace(row['old_text'],row['new_text'],1)
preserve_identifiers(before,after)
for old_ids,new_ids in zip(identifiers(before),identifiers(after)):
    assert all(new_ids[k]==v for k,v in old_ids.items())
    assert all(new_ids[k]==1 for k in new_ids-old_ids)
SOURCE.write_text(after,newline='\n')

_,defects=read_tsv(folder/(prefix+'defects.tsv'))
for row in defects:
    row['review_status']='Root read the complete original and receiving UN6/P328/UN8/P334/UN13 and P234 proofs, including every changed receiving paragraph after revision, and compared all maps and claims with the original proofs. The provenance reviewer separately read the specified complete primary loci and exact applications. Exposed used-and-rechecked comparison only; no independent or final-page credit.'
print('Root defects',append_rows(ROOT/'S6_SERIES_PUBLISH_defects_II.tsv',defects,'change_id'))
print('Program160',append_rows(ROOT/'S6_SERIES_PUBLISH_defects_II.tsv',programs,'change_id'))
print('Bibliography161',append_rows(ROOT/'S6_SERIES_PUBLISH_defects_II.tsv',bib,'change_id'))
for name in ['S6_SERIES_PUBLISH_rossi_CHECK_EVENTS.tsv','S6_SERIES_PUBLISH_rossi_ambient_CHECK_EVENTS.tsv','S6_SERIES_PUBLISH_occurrence_sources_CHECK_EVENTS.tsv']:
    _,rows=read_tsv(sources/name)
    for row in rows:
        if 'effort' not in row['who']:row['who']+='; effort setting not separately exposed'
    print(name,append_rows(ROOT/'CHECK_EVENTS.tsv',rows,'event_id'))
for name,suffix in [('rossi','resolution'),('rossi_ambient','ambient'),('fujimoto','elliptic-domain'),('kummer','arbitrary-A')]:
    _,rows=read_tsv(sources/('S6_SERIES_PUBLISH_'+name+'_sources.tsv'))
    incoming=[]
    for row in rows:
        incoming.append(dict(source=row['source_key']+' (third-continuation occurrence '+suffix+')',
            url=row['url'],version=row['version'],locus=row['locus_read']+'; '+row['read_extent'],
            date_utc=row['date_utc'],sha256=row['sha256'],own_word_summary=row['own_paraphrase'],use=row['exact_application']))
    print('Primary',name,append_rows(ROOT/'S6_SERIES_PUBLISH_c3_primary_readings.tsv',incoming,'source'))

fields,progress=read_tsv(ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv')
old_rows=[r for r in progress if r['paper']=='II' and r['unit_id']=='sec:II:09']
assert len(old_rows)==26
# Preserve the original open identity on the still-unreviewed occurrence remainder.
for row in old_rows:
    row.update(unit_title='Paired roots and projective elliptic components',date_utc=now(),
        evidence='CHECK_EVENTS.tsv: II-C3-ROOT-OCCURRENCE-FIRST-ADMISSION',
        detail='The original open occurrence-unit identity remains on the following unreviewed subsection beginning at UN18. Four preceding actual subsections have complete local comparisons; subdivision earns no closure or movement credit on this original row. '+row['detail'])
new_units=[
    ('subsec:II:elliptic-root-fillings','Elliptic root fillings'),
    ('subsec:II:multiple-elliptic-hopf-threefolds','Multiple elliptic fibrations on Hopf threefolds'),
    ('subsec:II:cuspidal-self-products','Cuspidal self-products'),
    ('subsec:II:kummer-occurrence','Kummer components and vertical modifications')]
for unit,title in new_units:
    for kind in [f'D{i:02}' for i in range(1,26)]+['structure']:
        status='open' if kind in ['D14','D23','structure'] else 'done'
        detail='Complete original and receiving statements/proofs read against all 25 defect classes. Each found instance is logged; original domains, maps and conclusions are preserved. Known ambient source results are cited after the exact resolution isomorphism. No new independent-check or final-page credit.'
        if kind in ['D10','D16']:detail='Original D10/D16 closures preserved; numbered owners retain titles and permanent tags.'
        if kind=='D18':detail='Exact cited source versions and loci freshly opened and matched by provenance review; the receiving maps are explicit. Fujimoto raw PDF bytes were unavailable, so the source record truthfully leaves its SHA blank; the full cited facsimile text was read.'
        if kind in ['D14','structure']:detail='Local one-owner order is complete; the final whole-paper dependency and placement review remains open. This new subsection row carries no migration movement credit.'
        if kind=='D23':detail='Source typography reviewed; integrated pdfLaTeX build and final page-image reading remain open.'
        progress.append(dict(zip(fields,['II',unit,title,'structure' if kind=='structure' else 'defect',
            '' if kind=='structure' else kind,status,now(),'CHECK_EVENTS.tsv: II-C3-ROOT-OCCURRENCE-FIRST-ADMISSION',detail])))
keys=[(r['paper'],r['unit_id'],r['defect_type'] or r['row_kind']) for r in progress]
assert len(keys)==len(set(keys))
write_tsv(ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv',fields,progress)
set_unit_status('subsec:II:blowup-topology','D18','done',
    'The complete current general owner, including its newly transferred full-support map, has been read. This actual subsection contains no bibliographic claim awaiting verification; its exact comparison is proved here. The separate bibliography-wide provenance work retains its own open rows.',
    'CHECK_EVENTS.tsv: II-C3-ROOT-SUPPORT-BLOWUP-ADMISSION')

add_event('cdp:st:C.2.UN.6;prop:II:multiple-elliptic-hopf-threefold;cdp:st:C.2.UN.8;rem:II:cuspidal-generic-divisors;cdp:st:C.2.UN.13',
    'II-C3-ROOT-OCCURRENCE-FIRST-ADMISSION','used and rechecked in this run',
    'Root read the entire original occurrence prefix through UN13 and every receiving statement and proof, including the post-revision UN8/P334 and P328; the exact P233/P234/P236 and original UN3 owners were also read. UN6 retains the free quotient, proper local mu_m chart, inverse punctured-product map, multiplicities, normal elliptic curve, canonical divisor, pushforward/plurigenera, solid-torus boundary matrix, integral homology, non-uniruled strict transforms and base-change component. P328 numbers the existing complete counterexample, verifies constant modulus and smooth complement by inverse product maps, supplies the affine-complement inverse and all divisor multiplicities, and identifies the global disconnected cover normalization and both inverse hypersurface/Hopf maps. UN8 retains every local graph chart and exceptional chain, quotient S/E, integral cohomology, canonical singular-fibre/duality and actual ambient fundamental-group proof. Explicit tensor-by-L and inverse graph-coordinate maps identify the resolved threefold with the correctly indexed Rossi model; its known Calabi-Yau and Hodge conclusions are cited, and the repeated ambient Picard/Hodge derivation is removed to this exact edit record. P334 preserves the generic NS matrix, rank and inverse constant-field substitutions at one numbered owner. UN13 keeps arbitrary A, its quotient ring and invariant form, all ambient/support Gysin maps, coherent formal-functions argument, forty quartic blocks and the exact quadratic normalization. Its general support blowup proof moves to P234 with the same label and an exact receiving application. All existing identifiers remain. Four local occurrence units are reviewed; the original sec09 identity remains open on the unread remainder. No independent or final-page credit.',
    'Complete first four occurrence subsections',source=__file__)
add_event('lem:II:blowup-topology;cdp:st:C.2.UN.13',
    'II-C3-ROOT-SUPPORT-BLOWUP-ADMISSION','used and rechecked in this run',
    "Complete old P234 and old UN13 plus complete receiving P234/UN13 read by root. The transferred formula C.KM.S2 has exactly the original compact analytic full-inverse-image scope. The compact quotient homeomorphism identifies relative cohomology; the compared exact sequences have maps(pi_S*,i_Z*) and j_S*−p*. Restricted ambient Gysin classes map to minus the positive xi powers, making the second map surjective in every degree. The resulting short exact sequence and injectivity of p* prove injectivity of pi_S*, spanning and independence of all extra classes. UN13 substitutes(Y,Z,r,pi_Z,S,S')=(W',C,c,sigma,S,sigma^-1(S)_red), including the four quartic crossing points. The prior ambient integral and fundamental-group proofs are unchanged. No independent or final-page credit.",
    'Full inverse-image blowup cohomology and its Kummer application',source=__file__)
add_event('cdp:st:C.2.UN.6;prop:II:multiple-elliptic-hopf-threefold;cdp:st:C.2.UN.8;rem:II:cuspidal-generic-divisors;cdp:st:C.2.UN.13;cdp:st:C.2.UN.25;cdp:st:C.2.UN.27;cdp:st:C.2.UN.35;cdp:st:C.2.UN.45',
    'II-C3-ROOT-OCCURRENCE-PROGRAM160','used and rechecked in this run',
    'The provenance reviewer read all seven complete pinned program sources and verified each exact attached-inventory path, byte count, SHA and absence of appendix/hash duplication. Root inspected every exact source-scope row. Addition160 names only the finite computations actually present. Enriques filling belongs to UN25, Enriques support to UN25/UN27, equivariant torus to UN35; the cuspidal matrix is now at P334 and is cited alongside UN8. UN13 JSON is represented by its generator. No program was run and no full mathematical construction is credited to finite checks. Later body filename removals remain with their unreviewed units.',
    'Programs appendix addition160',source=__file__)
comparison='''# First occurrence units: completed comparison

Root read the complete original UN6 and its orphan Hopf-threefold argument, UN8 and both source-credit paragraphs, UN13, and the complete earlier P234/P233/P236 and UN3 proofs. Every receiving paragraph was read; after the known-result consolidation, complete receiving UN8 and P334 were read again. The exact P328 additions and its full receiving proof, and the final support-exact-sequence/Gysin map, were read after their changes. This is used-and-rechecked editorial comparison, not an independent re-derivation.

The main admission event records the precise preserved maps. The old and new text of every change is in the defects table. The receiving proof keeps all root quotient and boundary matrices, all local integral cusp-fibre and tube comparisons, and all arbitrary-abelian-surface Kummer maps. P328 gives the existing external counterexample a numbered owner. P334 preserves the generic divisor matrix; the known ambient Hodge calculation is cited through the proved resolution isomorphism, in accordance with the user's known-result rule. P234 is the unique owner of the full-support blowup cohomology formula, with the restricted ambient Gysin isomorphism and its injection/spanning proof.

Four actual occurrence subsections now have complete local reviews. The original sec09 ledger identity stays open on the still-unreviewed subsection beginning with UN18, so this subdivision supplies no false closure or review movement. D14, final restructuring and D23 remain open. Program160 has seven complete-source comparisons without execution. Rossi bibliography161 fixes the exact v3 layout. Fujimoto's primary facsimile text was read at every cited locus; no accessible PDF bytes were returned, and its record states the blank SHA accurately. No primary publication copies belong to the checkpoint.
'''
(folder/(prefix+'comparison.md')).write_text(comparison,newline='\n')
print('UN6/P328/UN8/P334/UN13, support P234, program160 and bibliography161 admitted.')
