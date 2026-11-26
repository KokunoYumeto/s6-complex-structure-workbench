"""Admit exact marked lifts, cusp winding and bounded literature locators."""
from S6_SERIES_PUBLISH_c3_edit import *

folder=ROOT/'agents/continuation3_provenance/firstpart_locators'
prefix='S6_SERIES_PUBLISH_firstpart_'
before=SOURCE.read_text();after=before
_,guards=read_tsv(folder/(prefix+'guards.tsv'))
assert len(guards)==11
for row in guards:
    assert after.count(row['old_text'])==1,row['change_id']
    after=after.replace(row['old_text'],row['new_text'],1)
for old,new in zip(identifiers(before),identifiers(after)):
    assert old==new
SOURCE.write_text(after,newline='\n')
for suffix,target,key in [('defects.tsv','S6_SERIES_PUBLISH_defects_II.tsv','change_id'),('CHECK_EVENTS.tsv','CHECK_EVENTS.tsv','event_id')]:
    _,rows=read_tsv(folder/(prefix+suffix))
    if suffix=='CHECK_EVENTS.tsv':
        assert all(r['type']=='used and rechecked in this run' and 'effort' in r['who'] for r in rows)
    print(suffix,append_rows(ROOT/target,rows,key))
_,rows=read_tsv(folder/(prefix+'sources.tsv'))
sources=[dict(source=r['source_key']+' (third-continuation marked conventions)',
    url=r['url'],version=r['version'],locus=r['locus_read'],date_utc=r['date_utc'],sha256=r['sha256'],
    own_word_summary=r['own_paraphrase'],use=r['exact_application']+' Reading limits: '+r['read_extent']) for r in rows]
print('Sources',append_rows(ROOT/'S6_SERIES_PUBLISH_c3_primary_readings.tsv',sources,'source'))
event='II-C3-ROOT-FIRSTPART-LOCATORS-ADMISSION'
add_event('def:II:marked-conventions;series:II:E;cdp:st:C5c;known-and-new',event,'used and rechecked in this run',
    'Root read all eleven exact old/new guards, full P202 receiving definition, full comparison and source scopes; root also reread all current main theorems, outlines and the seven short status rows before this admission. Provenance read complete current and receiving conventions/E/C5c, the complete E8 lattice comparison and named primary loci. The marked lifts satisfy pi(z_j)=p_j and g_j z_j=z_j; their cubic/quartic branch choices are exactly the permitted I.12.8 statement metadata. The E8 identity-induced index-six lattice inclusion identifies beta=beta_c=beta^part+c. The cusp cocycle, first-coordinate functional and inversion of peripheral base loops supply the exact cited AC Theorem7.17 group formula. A now cites section10.4 on pp89-90; F retains its stated open twelve-tooth locus. Four bounded I reader destinations are matched to attached current metadata without opening I source/PDF or proof. No whole dictionary/derived refresh, independent proof, required-check increment or final-page credit.',
    'Common conventions, Theorem E, bounded C5c references and known/new table',source=__file__)

criteria={
 'D01':'The seven status rows contain no production history.',
 'D02':'Every qualification describes the exact theorem domain; no defensive clause remains.',
 'D03':'The correction claims identify the named published results and the exact earlier recorded mathematical comparisons.',
 'D04':'Rows use theorem letters, current typed body references and exact literature locators.',
 'D05':'No prompt item defines a mathematical claim or hypothesis.',
 'D06':'Every cited external theorem/section is identified by its source and exact locator.',
 'D07':'The table contains no worker, run or model claim.',
 'D08':'The table states concise mathematical statuses without process narration.',
 'D09':'The table contains no program path, output or implementation detail.',
 'D11':'The fixed-data and open-locus qualifications appear in the rows where they apply.',
 'D12':'Exactly one brief row per main theorem; the repeated status paragraphs were removed in the earlier table edit.',
 'D13':'No unnumbered mathematical result or definition is introduced by this status table.',
 'D15':'The complete subsection is the required seven-row short known-and-new table; A pagination and F open-locus scope now match the precise comparisons.',
 'D17':'Published inputs are cited at exact locators; the table re-proves none.',
 'D19':'There is no manual equation identifier in this table.',
 'D20':'The table uses the same A-G theorem identities and fixed-data conventions as the current main statements.',
 'D21':'No numeric or program agreement is presented as proof or priority evidence.',
 'D22':'All qualifiers refer to the specified theorem hypotheses and the recorded source applications.',
 'D25':'The bounded source-status comparison corrects A pagination and retains F scope; it makes no universal absence-of-antecedents assertion. The previous complete primary claim records supply the seven statuses.'
}
for kind,basis in criteria.items():
    set_unit_status('known-and-new',kind,'done',basis+' Root read the full current table and exact receiving guards. D14/D18/D23/D24/structure retain their final global gates.','CHECK_EVENTS.tsv: '+event)
for kind in ['D06','D22']:
    set_unit_status('sec:II:conventions',kind,'done',
        'The complete marked-conventions definition now specifies the orbifold lifts, cubic/quartic branches, beta_c, admissible affine coefficients, cusp class and first-coordinate map. Exact cited I metadata locators and the source-matched AC winding/peripheral maps resolve the formerly broad references. Root read the complete old/new definition and comparison; provenance read the complete listed source loci, with closed I source/PDF gate preserved.',
        'CHECK_EVENTS.tsv: '+event)
print('Eleven bounded guards admitted; nineteen known/new local rows and two convention rows closed.')
