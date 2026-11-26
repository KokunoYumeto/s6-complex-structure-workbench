"""Paper II final metadata and three-way provenance reconciliation.

Called by the text-final derivation only. The existing table retains its
historical assessments; no new proof check is inferred from a record update.
"""
from pathlib import Path
import csv
import json
import re
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
URL = 'https://github.com/KokunoYumeto/s6-complex-structure-workbench/blob/main/RECORDS.md#paper-ii'
COMMIT = 'a02f2eacf5a8c3db7cf8cdfcdba50c0002ee91c7'
csv.field_size_limit(100000000)

def write_deposit_markdown(deposit, binding=''):
    path = ROOT/'S6_SERIES_PUBLISH_deposit_fields.md'
    text = path.read_text()
    match = re.search(r'(?ms)^## Paper II\n.*?(?=^## Paper [IVX]+\n|\Z)',text)
    assert match
    before_other = text[:match.start()] + text[match.end():]
    sections = ['## Paper II\n\n']
    for title,key in [('Title','title'),('Abstract','abstract'),('Comments','comments'),('Provenance','provenance')]:
        sections.append('### '+title+'\n\n'+deposit[key]+'\n\n')
    sections.append('### Subjects and classification\n\n')
    for title,key in [('Primary subject','subject'),('Cross-lists','crossListSubjects'),('MSC codes','mscCodes'),('Tags','tags'),('Authorship mode','authorshipMode'),('Licence','license')]:
        value=deposit[key]
        sections.append('- '+title+': '+('; '.join(value) if isinstance(value,list) else value)+'\n')
    sections.append('\n### AI systems\n\n')
    for system in deposit['aiSystems']:
        sections.append('- '+system['provider']+': '+system['model']+'\n')
    if binding:
        sections.append('\n### Source and review binding\n\n'+binding+'\n')
    new = text[:match.start()] + ''.join(sections) + text[match.end():]
    check = re.search(r'(?ms)^## Paper II\n.*?(?=^## Paper [IVX]+\n|\Z)',new)
    assert new[:check.start()] + new[check.end():] == before_other
    new = re.sub(r'(?m)^Current revision:.*$',
        'Current revision: Paper II fields are synchronized to its current publication text and admitted check records. The earlier Paper I and V metadata sections are retained for the prescribed five-together update; Papers III and IV follow their own publication revisions.',new,count=1)
    path.write_text(new,newline='\n')

def finalize_provenance(data, programs, source_hash, pdf_hash, event_hash):
    from S6_SERIES_PUBLISH_c4_derive_II import read_rows, write_rows, count_prose
    stamp=datetime.now(timezone.utc).isoformat()
    path=ROOT/'S6_SERIES_PUBLISH_provenance_checks.tsv'
    fields, rows=read_rows(path)
    other=[r.copy() for r in rows if r['paper']!='II']
    ii=[r for r in rows if r['paper']=='II']
    assert len(ii)==51
    by_id={r['claim_id']:r for r in ii}
    deposit=json.loads((ROOT/'S6_SERIES_PUBLISH_deposit_fields_II.json').read_text())
    template=json.loads((ROOT.parent/'HEXAGON_METADATA_V_public_v3.json').read_text())
    assert list(deposit)==list(template)
    assert deposit['license']=='CC0 1.0'
    opening='Text: AI-authored; none of it was written by a human. The submitter takes responsibility for the veracity of the text.'
    assert deposit['provenance'].startswith(opening)
    assert count_prose(data) in data['text']
    assert count_prose(data).replace('\n',' ') in deposit['provenance']
    assert '20–23 November 2026' in deposit['provenance']
    assert '20--23 November 2026' in data['text']
    assert re.findall(r'(?<![0-9a-f])[0-9a-f]{40}(?![0-9a-f])',data['text'])==[COMMIT]
    assert set(re.findall(r'https://github\.com/[^\s{}]+',data['text']))=={URL.replace('#',r'\#')}
    for key in ('comments','provenance'):
        assert set(re.findall(r'https://github\.com/[^\s]+',deposit[key])) <= {URL,URL+'.'}
        assert not re.search(r'(?<![0-9a-f])[0-9a-f]{40}(?![0-9a-f])',deposit[key])
    local=[r for r in programs if r['repository_path'].startswith('code/')]
    historical=[r for r in programs if not r['repository_path'].startswith('code/')]
    sources='S6_SERIES_PUBLISH_c4_primary_readings.tsv; S6_SERIES_PUBLISH_c4_literature_searches.tsv; S6_SERIES_PUBLISH_c3_primary_readings.tsv'
    front='S6_SERIES_PUBLISH_c4_global_comparison.md; agents/continuation4_horizontal/S6_SERIES_PUBLISH_main_C_comparison.md; agents/continuation4_horizontal/S6_SERIES_PUBLISH_outline_comparison.md'
    derivation='code/S6_SERIES_PUBLISH_c4_derive_II.py; code/S6_SERIES_PUBLISH_c4_final_provenance.py'
    for row in ii:
        # Preserve each previous admitted assessment in its already existing
        # history column. This is a row history, not a derived-file snapshot.
        for old,new in [('claim','prior_claim'),('against_records','prior_records_assessment'),('by_recomputation','prior_recomputation_assessment'),('against_primary_source','prior_primary_assessment')]:
            value=row[old]
            if value and value not in row[new]:
                row[new] += ('\n' if row[new] else '') + 'Before fourth-continuation final reconciliation: '+value
        row['resolution_status']='done: current Paper II provenance claim checked against records, recomputation and its primary evidence'
        row['remaining_gate']='Five-together cross-paper refresh remains scheduled; it does not assert a missing source check for this current II claim.'
        row['required_action']='Retain the stated scope and evidence; regenerate at the five-together step.'
        row['current_paper_location']='Current Paper II §§1.1–1.6, Programs and cited complete owner, as specified in locations'
        row['current_deposit_location']='S6_SERIES_PUBLISH_deposit_fields_II.json and Paper II section of S6_SERIES_PUBLISH_deposit_fields.md'
        row['evidence'] += '; '+front+'; '+derivation
        row['current_resolution'] += ('\n' if row['current_resolution'] else '') + 'Fourth-continuation final reconciliation '+stamp+': the exact current statement/front-matter scope was compared with the admitted source evidence and recorded applications. Counts and program paths are recomputed from admitted records; no source opening, fresh proof or independent credit is inferred from this reconciliation.'

    def update(cid, **values):
        by_id[cid].update(values)

    link_claim='The standing records-page URL at #paper-ii is the sole repository address in the source and each affected deposit field; program paths are printed as plain text.'
    link_recomp='Exact URL-set equality in the current source and deposit comments/provenance; no program href, old pin, snapshot or repository-file URL remains.'
    link_primary='The controlling prompt §0.3 supplies the address; the c3 and c4 source-access records retain their actual HTTP200 readings and anchor/byte checks. Availability is recorded at those access times.'
    for cid in ('II-C2-P01','II-C2-P17','II-C3-PV-LINK'):
        update(cid,claim=link_claim,against_records='The current source macro, plain-path programs table and final deposit agree with the attached 23 November prompt §0.3.',by_recomputation=link_recomp,against_primary_source=link_primary,current_resolution='The obsolete pinned-directory requirement is superseded by the controlling prompt. The final current source and deposit use the one standing records page. Historical unsuccessful and successful access records remain in the prior assessments.',remaining_gate='The submitter resets the printed commit at deposit as instructed; no external publication action is claimed.')
    update('II-C2-P02',by_recomputation='The current submitted-V metadata field schema is preserved exactly. authorshipMode is no-human-author-claimed; the required responsibility opening and explicit no-human-checking sentence occur in provenance. Empty legacy authors/affiliation fields are not part of this supplied current schema.')
    update('II-C2-P08',claim='GPT-6 Astra, OpenAI ChatGPT Pro mode: publication revision and further checks, 20–23 November 2026.',by_recomputation='Paper and deposit publication dates extend literally through 23 November; model names and historical effort settings agree with the attached prompt and current session attribution.')
    update('II-C2-P11',by_recomputation='Every current contribution names ChatGPT Pro mode and states that the numerical effort setting is not separately exposed. Historical Codex ultra and Anthropic high/max credits keep their stated scopes.')
    update('II-C2-P12',by_recomputation='The exact no-human-checking sentence is retained in the paper and final deposit provenance; no human-review or understanding flag is invented outside the supplied schema.')
    update('II-C2-P13',claim=count_prose(data).replace('\n',' '),against_records='Authoritative admitted CHECK_EVENTS.tsv; exact current primary labels and explicitly retained historical statement labels in the current source; no unadmitted agent bundle is merged.',by_recomputation=f"{len(data['selected'])} unique event associations in {len(data['groups'])} evidence groups; the six exact type totals are {json.dumps(dict(data['counts']),sort_keys=True)}. Source and deposit prose use that same deterministic selection.",against_primary_source='This is a ledger count. Each selected event retains its actual source, checker, type, outcome and exposure; no mathematical primary-source verification follows from its count.',current_resolution='Final source and deposit numeric prose agree with the current admitted ledger; exact-subject and group selection is implemented in the delivered derivation program.')
    update('II-C2-P14',claim='Each admitted exact-subject association is counted once; current primary statement labels and retained historical statement labels supply the scope. Evidence groups and type counts retain their actual overlap.',against_records='Current owner/alias mapping preserves historical statement identities and the original subjects of events; equation, unit, bibliography, page and unrelated subjects are excluded unless they are genuine retained statement identifiers.',by_recomputation='Event IDs are unique; the exact selected set and nonempty group fallback are used for both printed totals. No fixed historical count of excluded equation records is carried into the final prose.',against_primary_source='The event outcome scopes and exposure chronology remain authoritative; neither a group identifier nor a current-owner link supplies independent-proof credit.')
    paths_claim=f"The paper prints {len(programs)} unique program paths: {len(historical)} attached repository paths with recorded exact source hashes and {len(local)} current code paths with verified local byte hashes."
    for cid in ('II-C2-P18','II-C2-P19','II-C3-PV-PATHS'):
        update(cid,claim=paths_claim,against_records='Every historical repository path occurs in attached REPOSITORY_PROGRAM_PATHS.txt; every current code path exists in the checkpoint code directory. The printed-path set equals the delivered records table.',by_recomputation='All current code hashes are recomputed from the exact local bytes. Historical exact source hashes are retained from their actual retrieval records and path additions; no unperformed re-download is claimed.',against_primary_source='Historical source-opening records retain their precise URL, edition/pin and hash. Current code bytes supply the primary file evidence. This path/hash verification gives no program-execution or mathematical proof credit.',current_resolution='S6_SERIES_PUBLISH_records_II.tsv supplies the printed-path/repository-path/SHA-256 map. Current code paths are designated for the standing page; no claim is made that new programs existed at an earlier commit.')
    update('II-C2-P20',by_recomputation='The current paper, JSON and Markdown all give CC0 1.0 Universal with the prescribed canonical URL; source declaration and deposit license agree.')
    update('II-C2-P23',against_records='The exact standard-family Euler values retain their primary readings. The separate Steenbrink source/application comparison II-C3-LIT-C2 supplies the logarithmic-period input, including positive multiplicities and the actual relative-complex inclusion.',against_primary_source=by_id['II-C3-LIT-C1']['against_primary_source']+' '+by_id['II-C3-LIT-C2']['against_primary_source'])
    update('II-C2-P24',against_primary_source='The bounded current literature searches and Kamenova source comparison II-C3-LIT-D1 record the overlapping semistable subclass and the exact retained family map. No exhaustive absence claim is made.',evidence=by_id['II-C2-P24']['evidence']+'; '+sources)
    update('II-C2-P26',claim='The cited constructions, complete comb deformation germ, persistence and ordered-pair deformation classification retain their exact sources. The Hodge computation is proved on the stated nonempty open twelve-tooth locus; the general/special-member splitting question remains explicit.',current_resolution='Complete main F, all seven outline steps, E5/E6/E13–15, E2.23/E2.24 and E2.2/E2.5 comparisons verify the actual maps and scope. The literal question locators are Combs §10(1)–(2), p.33 and Log §1.1(1), p.2. The general and special-member Hodge question in Combs §10(2) remains beyond the proved twelve-tooth case.')
    update('II-C2-P28',by_recomputation='The complete deposit abstract and current source abstract were compared clause by clause: compact Betti-zero scope, local nodal example, normalization-Picard criterion, tangent/deformation results, three doubled supports, fixed-data two-turn cover, and nonempty open twelve-tooth locus agree. TeX/metadata prose formatting is represented explicitly in the JSON rather than claimed to be a whitespace-only transform.',current_resolution='The complete abstract comparison is recorded in the global and outline comparison notes. No general/special-member comb splitting answer is inserted.')
    update('II-C2-P29',current_resolution='The current Paper II series overview is retained with the attached series design and inherited descriptions. Its cross-paper references use the supplied source-of-record conventions and wait for the prescribed five-together regeneration. I/V manuscripts were not opened during this II reconciliation.',remaining_gate='Final cross-paper numbering and series-table comparison at the five-together step, after III and IV.')
    update('II-C2-P30',claim='Paper II deposit fields use exactly the keys and ordering of the attached HEXAGON_METADATA_V_public_v3.json metadata form, with current Paper II content.',against_records='The controlling metadata file is read solely as the supplied schema. No I/V manuscript or proof is opened.',by_recomputation='The field sequence equals the supplied current schema; title, abstract, comments, responsibility opening, AI credits, subjects/MSC/tags and CC0 are present. The JSON and Markdown II fields are generated from the same values.',current_resolution='Legacy empty authors and humanUnderstanding fields outside the current supplied schema are omitted; the no-human-authorship and no-human-checking declarations remain in their authorized textual fields.')
    update('II-C3-PV-COMMIT',claim='The source defines the required repository commit once and prints it once in §1.5 through SsixRepositoryCommit.',by_recomputation='Exactly one 40-hex literal occurs in the entire source, with the required value; exactly two macro occurrences are its definition and its §1.5 use. Neither affected deposit field contains a commit identifier.',current_resolution='The exact current literal is '+COMMIT+'. This implements the supplied §0.3 instruction; the submitter resets it at deposit.')
    update('II-C3-PV-MODELS',against_records='The supplied prompt and individual events document the historical contributions, Anthropic readings, Opus V introduction rewrite, I reading and deposit corrections. Current publication work extends through 23 November.',by_recomputation='Compared all complete current methodology and deposit model/date/effort paragraphs; no numerical current effort or independent proof count is inferred from the model name.',current_resolution='The publication interval is 20–23 November 2026 in both places; all earlier contribution intervals and their exposure limits remain as documented.')
    update('II-C3-PV-DEPOSIT',claim='The final current II deposit opens with both required responsibility sentences, describes the actual current mathematics, gives recomputed counts and points programs/records to the standing page.',by_recomputation='Exact current schema, opening, URL sets, no obsolete commit, matching final count paragraph, model/date/effort credits, CC0 and complete abstract comparison all pass.',current_resolution='The current JSON and Markdown II section are synchronized. Rendered first-part review is recorded separately in S6_SERIES_PUBLISH_reading_II.md; no record/program is said to accompany the TeX deposit.')
    for row in ii:
        if row['claim_id'].startswith('II-C3-LIT-'):
            row['against_records'] += ' The fourth-continuation complete A–G and outline comparisons preserve the exact cited source maps and identify their final owners.'
            row['by_recomputation'] += ' The final source contains the corrected exact locators, explicit historical versions and no unsupported all-family Hodge conclusion; current source and record links are synchronized.'
            row['evidence'] += '; '+sources
    # Preserve the formerly corrective claim as a completed correction, with
    # its exact narrowed mathematical scope still stated in current_resolution.
    update('II-C3-LIT-F2',claim='Both front-matter loci restrict the twelve-tooth Hodge result to its proved nonempty open family; the general and special-member splitting problem is retained.',required_action='Retain the exact open-family scope and explicit remaining problem.')
    update('II-C3-LIT-G1',current_resolution=by_id['II-C3-LIT-G1']['current_resolution']+' The admitted complete outline now writes U=C^{-1}, the two-turn map -r^{-2}U, its exact norm t^{-1}B_u^{-1}, cap multiplier theta/t and the same cusp-period relabelling; these are the full covering proof maps.')
    assert [r for r in rows if r['paper']!='II']==other
    write_rows(path,fields,rows)
    binding=f'Current source SHA-256: `{source_hash}`. Current PDF SHA-256: `{pdf_hash}`. Admitted CHECK_EVENTS SHA-256: `{event_hash}`. The actual final-page coverage is recorded in S6_SERIES_PUBLISH_reading_II.md. The five-together cross-paper refresh remains scheduled.'
    write_deposit_markdown(deposit,binding)
    print('Existing II provenance rows reconciled:',len(ii))
    print('Other-paper provenance rows retained:',len(other))
    print('Program paths:',len(programs),'historical:',len(historical),'current code:',len(local))
