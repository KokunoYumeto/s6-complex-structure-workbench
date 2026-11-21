#!/usr/bin/env python3
"""Serialize the manually completed D08/D09 audit of the frozen candidate14.

The assistant read all 250 inherited contexts and the indicated fuller proof
passages. The program supplies occurrence correspondence and immutable hashes;
it creates no additional source-reading, page-reading or mathematical credit.
It refuses any source/PDF pair beyond the pair actually examined here.
"""
from pathlib import Path
import collections,csv,datetime,hashlib,json,re
import fitz

ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).resolve().parent
SOURCE_SHA='1f2d0d376f71e7843265976aeeb72cf8e1ff77aea176ff5dbb4e67446c25b36f'
PDF_SHA='1abe0fc16350045cd2ce0aae57ce377dcfe2400de0b0bf58ba7e559d360bcb37'

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

source=ROOT/'S6_SERIES_PUBLISH_I.tex'
pdf=ROOT/'build/I_candidate14/S6_SERIES_PUBLISH_I.pdf'
scan=ROOT/'records/S6_SERIES_PUBLISH_I_continuation_rendered_residue_scan.json'
assert sha(source)==SOURCE_SHA
assert sha(pdf)==PDF_SHA
old=json.loads(scan.read_text())['rows']
selected=[(i+1,row) for i,row in enumerate(old) if row['type'] in ('D08','D09')]
assert len(selected)==250
patterns={
    'D08':re.compile(r'\b(?:actual|retain\w*|supplied|specified|fresh|executed|saved|receipt|candidate|survivor|verified|probe)\b',re.I),
    'D09':re.compile(r'\.py\b|\.jsonl?\b|code/|audit_|receipt|SHA-256|rows \(4|columns numbered|identities at their recorded scopes|--fresh',re.I)}
current=collections.defaultdict(list)
for page in fitz.open(pdf):
    # This exact map collapses extracted whitespace only. It does not alter any
    # mathematical token. Both old and new contexts are retained in the output.
    text=' '.join(page.get_text().split())
    for typ,pattern in patterns.items():
        for match in pattern.finditer(text):
            current[typ].append({'page':page.number+1,'type':typ,'hit':match[0],
                                 'text_offset':match.start(),
                                 'context':text[max(0,match.start()-100):match.end()+200]})
for typ in patterns:
    prior=[row['hit'] for _,row in selected if row['type']==typ]
    assert prior==[row['hit'] for row in current[typ]]
assert len(current['D08'])==192 and len(current['D09'])==58

special={
    1:'The contents title names the coefficient gauge whose exact changes are stated in §14.3.',
    2:'The contents title describes a local resolution preserving the cusp factor; its construction is Proposition 22.44.',
    19:'This occurrence is in the permitted methodology section: the sentence states the scopes of recorded algebraic, numerical and analytic checks.',
    127:'The fuller proof gives the three holomorphic comparison maps and their inverses, including the cusp unit action and its descent. Verified describes those displayed identities in that proof.',
    134:'The fuller proof projects the product-cover translations, explicitly giving (1/3)(Z+kappa1 Z) and (1/2)Z+(1/4)kappa2 Z. Verified describes this mathematical lattice calculation.',
    147:'The phrase refers to the exact norm identity in Proposition 6.3, immediately displayed and then substituted into the local Taylor calculation.',
    164:'The fuller proof displays the maps L1,L2, their kernels and finite affine generators. Verified refers to substitution of the four displayed product periods.',
    180:'Candidate tetrahedra are the finite geometric objects in the enumeration. The proof gives their common-face and volume tests and proves exhaustiveness.',
    173:'Supplied attributes the marked triangular filling to Engel Proposition 2.8 at the stated pages, after the complete local chart and transition comparison.',
    204:'Supplied attributes analytic resolution to Bierstone–Milman Theorem 1.6 and its specified noncompact extension.',
    232:'The coordinate u=xy supplies the smoothing section of the product of the two explicitly computed normal lines.',
    298:'Supplied refers to coherent extensions obtained from the proper mathematical family under the stated identification.',
    323:'The fuller proof gives b_j as an explicit finite binomial sum in Q(sqrt(3)), two example coefficients and rational endpoints. Verified refers to integer multiplication and squaring of those stated numbers.',
    338:'This is a comparison of the contents of the two cited external DGKX editions. Retains identifies the period construction and Oka conclusions present in version 2.',
    339:'Specified versions are the two cited external DGKX editions. The passage limits its comparison to their displayed mathematical contents.'}
source_text=source.read_text()
program_start=source_text.index(r'\section*{Programs}')
bib_start=source_text.index(r'\begin{thebibliography}',program_start)
program_text=source_text[program_start:bib_start]
assert program_start<bib_start
occurrence=collections.Counter()
rows=[]
for scan_row,oldrow in selected:
    typ=oldrow['type'];newrow=current[typ][occurrence[typ]];occurrence[typ]+=1
    word=oldrow['hit'].lower()
    if typ=='D09':
        assert newrow['page'] in (332,333,334)
        reason='This filename occurs in the end-of-paper Programs table, where the prompt requires the program list and pinned source links. Its table row names the computation and receiving mathematical statement.'
        disposition='allowed program-table citation'
    elif scan_row in special:
        reason=special[scan_row]
        disposition='permitted methodology statement' if scan_row==19 else 'ordinary mathematical or bibliographic usage'
    elif word=='specified':
        reason='The context identifies mathematically prescribed data, a coordinate, branch, family, representative or map through the displayed formulas or a numbered mathematical construction. The adjective states that mathematical choice.'
        disposition='ordinary mathematical usage'
    elif word.startswith('retain'):
        reason='The context keeps an explicit mathematical datum, component, coefficient, branch, marking, multiplicity or invariant in the stated operation. Its object and the relevant map or selection are given in the mathematical passage.'
        disposition='ordinary mathematical usage'
    elif word=='supplied':
        reason='The subject is a mathematical construction or cited theorem that provides the indicated object; this occurrence carries no file-delivery or run-history assertion.'
        disposition='ordinary mathematical usage'
    elif word=='verified':
        reason='The occurrence describes the explicit mathematical substitution, identity or bound in the proof itself. Its inputs and method are printed at this location.'
        disposition='ordinary mathematical usage'
    elif word=='candidate':
        raise AssertionError('The finite-enumeration candidate needs its explicit reviewed disposition.')
    else:
        raise AssertionError('No manually reviewed disposition for '+repr((scan_row,word)))
    rows.append({'scan_row_index_1based':scan_row,'type':typ,'hit':oldrow['hit'],
                 'candidate13_page':oldrow['page'],'candidate13_context':oldrow['context'],
                 'candidate14_page':newrow['page'],'candidate14_context':newrow['context'],
                 'same_type_occurrence_index_1based':occurrence[typ],
                 'disposition':disposition,'reason':reason,'confirmed_defect':False,
                 'source_reading_credit':'context audit only','full_page_reading_credit':False,
                 'mathematical_check_event_added':False})
assert len(rows)==250 and {r['scan_row_index_1based'] for r in rows}=={i for i,_ in selected}

fuller_passages=[]
for label,pattern in [
    ('three comparison maps and inverses',r'We have now\s+verified'),
    ('Albanese product-cover projections',r'The precise Albanese lattices'),
    ('local norm identity',r'The identity verified in'),
    ('finite-generator period substitutions',r'These formulas are verified'),
    ('finite tetrahedron enumeration',r'Since the candidate\s+tetrahedra'),
    ('Bernstein coefficient endpoint arithmetic',r'verifies every entry by integer multiplication')]:
    found=re.search(pattern,source_text)
    assert found,label
    fuller_passages.append({'label':label,'source_line':source_text.count('\n',0,found.start())+1,
                            'text':source_text[max(0,found.start()-1200):found.end()+900]})
result={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'paper':'I',
        'source_sha256':SOURCE_SHA,'pdf_sha256':PDF_SHA,'scan_file':str(scan.relative_to(ROOT)),
        'scan_sha256':sha(scan),'candidate14_pdf':str(pdf.relative_to(ROOT)),
        'counts':dict(collections.Counter(r['type'] for r in rows)),
        'all_250_inherited_candidate_contexts_read':True,
        'current_pattern_occurrence_sequences_exactly_equal_to_inherited':True,
        'current_context_mapping':'Within each defect type, the complete extracted hit sequence is exactly equal, including case. The order-preserving bijection binds every reviewed row to its current page and printed context; old and new contexts are both retained.',
        'rows':rows,'fuller_source_passages_examined':fuller_passages,
        'confirmed_new_defects':[],'proposed_guards':[],
        'page_reading_credit_added':0,'mathematical_events_added':0,
        'scope':'Manual contextual audit of all supplied D08 and D09 candidates, with exact current-source/PDF and occurrence correspondence. This record contributes only that bounded residue disposition to the overall defect-type gate; final page reading and the other defect types retain their own evidence.'}
dest=OUT/'S6_SERIES_PUBLISH_I_cont_D08_D09_dispositions.json'
dest.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
fields=['scan_row_index_1based','type','hit','candidate13_page','candidate14_page','disposition','reason','confirmed_defect','full_page_reading_credit','mathematical_check_event_added']
with (OUT/'S6_SERIES_PUBLISH_I_cont_D08_D09_dispositions.tsv').open('w',newline='') as stream:
    writer=csv.DictWriter(stream,fieldnames=fields,delimiter='\t',extrasaction='ignore')
    writer.writeheader();writer.writerows(rows)
print(json.dumps({k:result[k] for k in ['source_sha256','pdf_sha256','counts','all_250_inherited_candidate_contexts_read','current_pattern_occurrence_sequences_exactly_equal_to_inherited','confirmed_new_defects','page_reading_credit_added','mathematical_events_added']},indent=2))
