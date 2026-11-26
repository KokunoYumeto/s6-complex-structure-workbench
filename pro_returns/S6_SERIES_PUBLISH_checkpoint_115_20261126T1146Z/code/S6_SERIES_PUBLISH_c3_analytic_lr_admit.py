"""Admit the exposed complete analytic-duality/LR comparison and stable source repairs."""
from S6_SERIES_PUBLISH_c3_edit import *
import json

folder=ROOT/'agents/continuation3_provenance/analytic_lr'
meta=json.loads((folder/'S6_SERIES_PUBLISH_analytic_status.json').read_text())
assert meta['old_complete_reading'] and meta['receiving_complete_reading']
old=Path(meta['snapshot']).read_text()
new=(folder/'S6_SERIES_PUBLISH_analytic_lr_proposed.tex').read_text()
s=SOURCE.read_text()
start=r'\section{Analytic duality and the exact Picard restriction maps}'
end=r'\part{The sign theorem for every degeneration}'
a=s.index(start);b=s.index(end,a)
assert s[a:b]==old,'Source changed after the complete exposed comparison'
preserve_identifiers(old,new)
for before,current in zip(identifiers(old),identifiers(new)):
    for name,count in before.items():assert current[name]==count,name
def statement(text,label):
    i=text.index('\\label{'+label+'}',text.index('\\begin{document}'))
    a=text.rfind('\\begin{',0,i)
    env=re.match(r'\\begin\{([^}]+)\}',text[a:]).group(1)
    b=text.index('\\end{'+env+'}',i)+len('\\end{'+env+'}')
    return text[a:b]
protected={x:statement(s,x) for x in ['push:src:E.5.2','push:src:E.5.3']}
after=s[:a]+new+s[b:]
for label,body in protected.items():assert statement(after,label)==body
SOURCE.write_text(after,newline='\n')
for suffix,target,key in [('defects.tsv','S6_SERIES_PUBLISH_defects_II.tsv','change_id'),
                          ('CHECK_EVENTS.tsv','CHECK_EVENTS.tsv','event_id')]:
    _,rows=read_tsv(folder/('S6_SERIES_PUBLISH_analytic_'+suffix))
    print(suffix,append_rows(ROOT/target,rows,key))

# Unit reassignment follows the actual old and new headings. It creates no
# movement or independent-proof credit by itself.
fields,prior=read_tsv(ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv')
oldtitles=set(re.findall(r'\\(?:sub)?section\{([^\n]+)\}',old))
oldunits={r['unit_id'] for r in prior if r['paper']=='II' and r['unit_title'] in oldtitles}
assert len(oldunits)==11,oldunits
retained=[r for r in prior if not(r['paper']=='II' and r['unit_id'] in oldunits)]
titles={x['section']:x['title'] for x in meta['structure']}
_,incoming=read_tsv(folder/'S6_SERIES_PUBLISH_analytic_unit_status.tsv')
seen={(r['paper'],r['unit_id'],r['defect_type'] or r['row_kind']) for r in retained}
for item in incoming:
    kind=item['type'];unit=item['unit']
    if kind in ['restructuring','structure']:kind='structure'
    assert ('II',unit,kind) not in seen,(unit,kind)
    seen.add(('II',unit,kind))
    status='open' if kind in ['D14','D15','D23','D24','structure'] else 'done'
    retained.append(dict(paper='II',unit_id=unit,unit_title=titles[unit],
      row_kind='structure' if kind=='structure' else 'defect',defect_type='' if kind=='structure' else kind,
      status=status,date_utc=now(),evidence=str(folder.relative_to(ROOT)/'S6_SERIES_PUBLISH_analytic_comparison.md'),
      detail='Complete exposed original/receiving comparison by continuation3 provenance. '+item['evidence']+' '+item['status']+'. Unit migration alone earns no movement credit.'))
# Agent's status table carries all 25 defect classes; add explicit structural gates.
for unit,title in titles.items():
    if ('II',unit,'structure') not in seen:
        retained.append(dict(paper='II',unit_id=unit,unit_title=title,row_kind='structure',defect_type='',
          status='open',date_utc=now(),evidence=str(folder.relative_to(ROOT)/'S6_SERIES_PUBLISH_analytic_comparison.md'),
          detail='Local complete statements and proofs are assigned to seven mathematical sections. Whole-paper final placement and one-owner consolidation remain open; migration is not movement credit.'))
write_tsv(ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv',fields,retained)

# Import primary-source records as paraphrases, preserving the exact reading
# extent and the kind of object hashed. No primary passages are copied.
_,srcrows=read_tsv(folder/'S6_SERIES_PUBLISH_analytic_sources.tsv')
out=[]
for r in srcrows:
    out.append(dict(source=r['source_id'],url=r['url'],version=r['version'],locus=r['exact_locus'],
      date_utc=r['date_utc'],sha256=r['source_sha256'],own_word_summary=r['established_scope'],
      use=r['exact_application']+' Reading attribution: continuation3 provenance; '+r['reading_extent']))
print('primary readings',append_rows(ROOT/'S6_SERIES_PUBLISH_c3_primary_readings.tsv',out,'source'))

# Stable bibliographical and locator repairs; no final counts/deposits are touched.
base=ROOT/'agents/continuation3_provenance'
for stem in ['bibliography_guillot','bibliography_dt','bibliography_ulmer']:
    _,rows=read_tsv(base/('S6_SERIES_PUBLISH_c3_provenance_'+stem+'_edits.tsv'))
    s=SOURCE.read_text()
    for r in rows:
        if s.count(r['old_text'])==1:
            s=s.replace(r['old_text'],r['new_text'],1)
        else:
            assert s.count(r['new_text'])==1,r['change_id']
            print(r['change_id']+' already admitted verbatim')
    SOURCE.write_text(s,newline='\n')
    _,admitted=read_tsv(ROOT/'S6_SERIES_PUBLISH_defects_II.tsv')
    known={r['change_id'] for r in admitted}
    print(stem,append_rows(ROOT/'S6_SERIES_PUBLISH_defects_II.tsv',[r for r in rows if r['change_id'] not in known],'change_id'))
    _,sr=read_tsv(base/('S6_SERIES_PUBLISH_c3_provenance_'+stem+'_sources.tsv'))
    mapped=[]
    for r in sr:
        mapped.append(dict(source=r['source_id'],url=r['url'],version=r['version'],locus=r['exact_locus'],
          date_utc=r['date_utc'],sha256=r['sha256'],own_word_summary=r['own_paraphrase'],
          use='Bibliography/locator repair; exact reading attribution: '+r['reader']))
    _,admitted_sources=read_tsv(ROOT/'S6_SERIES_PUBLISH_c3_primary_readings.tsv')
    known_sources={r['source'] for r in admitted_sources}
    print(stem+' sources',append_rows(ROOT/'S6_SERIES_PUBLISH_c3_primary_readings.tsv',[r for r in mapped if r['source'] not in known_sources],'source'))

_,corrections=read_tsv(base/'S6_SERIES_PUBLISH_c3_provenance_A2_correction.tsv')
assert len(corrections)==1
r=corrections[0]
paths=[base/'S6_SERIES_PUBLISH_c3_provenance_literature_claims.tsv',
       base/'S6_SERIES_PUBLISH_c3_provenance_claim_rows.tsv',
       base/'S6_SERIES_PUBLISH_c3_provenance_report.md',
       ROOT/'S6_SERIES_PUBLISH_provenance_checks.tsv']
for p in paths:
    text=p.read_text();assert text.count(r['old_text'])==1,str(p)
    p.write_text(text.replace(r['old_text'],r['new_text'],1),newline='\n')
print('A2 scope correction',append_rows(ROOT/'S6_SERIES_PUBLISH_defects_II.tsv',corrections,'change_id'))
add_event('II-C3-LIT-A2','II-C3-ROOT-LITERATURE-A2-SCOPE-REPAIR','used and rechecked in this run',
 'The complete CDP98 Lemma 1.5 was freshly read by continuation3 provenance. Corrected exactly the four named established-scope paraphrases: the published local-freeness claim imposes no lower-direct-image vanishing premise. The example separately has those vanishings. Its complete counterexample and manuscript conclusions are unchanged. Root read the entire correction row and exact occurrences. No independent credit.',
 'Four exact records named in II-C3-PROV-151',source='agents/continuation3_provenance/S6_SERIES_PUBLISH_c3_provenance_A2_correction.tsv')

for label,body in protected.items():assert statement(SOURCE.read_text(),label)==body
add_event('wbII:thm:cartier-duality; wbII:prop:analytic-ah-boundary; wbII:thm:analytic-all-picard; ii:LR:covering; night:P3K.36',
 'II-C3-ROOT-ANALYTIC-LR-ADMISSION','used and rechecked in this run',
 'Exact current 3501-line old region equals the fully read agent snapshot. Root read the entire owner-by-owner comparison, all receiving duality/base-change owners, the complete invariant-lattice remark, the old and receiving minimal-cover remark and the closing LR construction; root does not claim an additional complete reread of the whole large fragment. The provenance agent fully read every old and receiving proof, recorded in the 29 exposed comparison events. Both duality scopes and every old label/target multiplicity remain. P3K.36 changes only hidden false-to-proved metadata: its printed fixed-data minimal-cover assertion is exactly 01RO, and its IV reference sentences are unchanged. Five stable bibliography/locator rows and the precise A2 paraphrase correction are admitted. Protected E.5.2/E.5.3 statements are byte-identical. Unit migration, source records and prior proof exposure earn no independent or final-page credit. Whole-paper D14/D15/D23/D24/structure gates remain open.',
 'S6_SERIES_PUBLISH_II.tex: seven analytic-duality through LR sections',
 source='agents/continuation3_provenance/analytic_lr/S6_SERIES_PUBLISH_analytic_comparison.md')
print('Admitted analytic/LR fragment, source records and stable bibliography repairs; final gates remain open.')
