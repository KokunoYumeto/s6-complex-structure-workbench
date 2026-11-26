#!/usr/bin/env python3
"""Write local 02LV proposals; no canonical or shared ledger mutation."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import csv,re

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'agents/continuation8_iii_lv'
sid='maps:src:D.2.53'
now=datetime.now(timezone.utc).isoformat()
canonical=(ROOT/'S6_SERIES_PUBLISH_III.tex').read_text()
start=canonical.index(r'\begin{theorem}[complete primitive cubic, fundamental-class and refined invariants of the weighted OS45 example]')
stop=canonical.index(r'\subsection{Moving the zero of the linearization}',start)
old=canonical[start:stop].rstrip()+'\n'
assert sha256(old.encode()).hexdigest()=='23e824f47d167303825e55eea340ccea3bd1b7250e2ac8ebaf2905722bbc1568'
end=old.index(r'\end{theorem}')+len(r'\end{theorem}')
oldstatement=old[:end]+'\n'
oldproof=old[end:].strip()+'\n'
newstatement=(OUT/'S6_SERIES_PUBLISH_III_02LV_receiving_statement.tex').read_text()
newproof=(OUT/'S6_SERIES_PUBLISH_III_02LV_receiving_proof.tex').read_text()
new=(OUT/'S6_SERIES_PUBLISH_III_02LV_receiving.tex').read_text()
assert new==newstatement+'\n'+newproof
assert sha256(new.encode()).hexdigest()=='dd2d7970e3f5d0734dfebd1048976b4ad0a13cfbdc02b1db7ebe509673bebff8'

def write(name,fields,rows):
    p=OUT/name
    with p.open('w',newline='') as f:
        w=csv.DictWriter(f,fields,delimiter='\t',lineterminator='\n')
        w.writeheader();w.writerows(rows)
    assert b'\r' not in p.read_bytes()

replacements=[]
transformed=canonical
for name,a,b in [('sole statement',oldstatement,newstatement),('both original proof environments',oldproof,newproof)]:
    assert transformed.count(a)==1,(name,transformed.count(a))
    transformed=transformed.replace(a,b,1)
    replacements.append(dict(statement_id=sid,old_text=a,new_text=b,
        reason='02LV '+name+': complete original/fresh comparison, exact maps and bounded coupled support/character repair; all69 permanent labels/targets retained in one theorem/one proof.'))
back=transformed
for r in reversed(replacements):
    assert back.count(r['new_text'])==1
    back=back.replace(r['new_text'],r['old_text'],1)
assert back==canonical
assert sorted(re.findall(r'\\label\{([^}]+)\}',old))==sorted(re.findall(r'\\label\{([^}]+)\}',new))
assert sorted(re.findall(r'\\hypertarget\{([^}]+)\}',old))==sorted(re.findall(r'\\hypertarget\{([^}]+)\}',new))
assert new.count(r'\begin{proof}')==new.count(r'\end{proof}')==1
write('S6_SERIES_PUBLISH_III_02LV_replacements.tsv',['statement_id','old_text','new_text','reason'],replacements)

edits=list(csv.DictReader((OUT/'S6_SERIES_PUBLISH_III_02LV_edit_records.tsv').open(),delimiter='\t'))
fields=['change_id','type','statement_id','old_location','old_page','new_location','new_page','old_text','new_text','reason','review_status']
defects=[]
def defect(key,typ,loc,a,b,reason):
    defects.append(dict(change_id='c8-III-02LV-'+key,type=typ,statement_id=sid,
        old_location=loc,old_page='pending final page concordance',
        new_location='Theorem maps:src:D.2.53, sole receiving proof',new_page='pending final build',
        old_text=a,new_text=b,reason=reason,
        review_status='receiving mathematics and exact final diff root-read; canonical application, unit editing and final page reading pending'))

# Each surviving original edit has its own exact local quotation. The
# chronology-only edit log also retains superseded assembly clauses.
skip={10,12,15,16,17,18,19,20}
for i,r in enumerate(edits[:32],1):
    if i in skip:continue
    if i==8:r['new_text']=r['new_text'].replace(edits[32]['old_text'],edits[32]['new_text'])
    assert r['old_text'] in old,(i,r['reason'])
    assert not r['new_text'] or r['new_text'] in new,(i,r['reason'])
    defect('edit-'+str(i).zfill(2),r['defect_type'],r['location'],r['old_text'],r['new_text'],r['reason'])

def excerpt(text,a,b):
    i=text.index(a);j=text.index(b,i);return text[i:j]

defect('smith-quotient-map','D22','original D.OF2 core relation quotient',
    edits[9]['old_text'],
    excerpt(new,'the marked relation matrix of that construction.','We specify a literal cochain'),
    'The actual quotient and inverse, named Smith diagonal Delta and chain lift replace the saved-array assertion. Delta is distinct from the graph differential.')
defect('primitive-core-generator','D22','original D.OF2 negative Smith generator',
    excerpt(old,r'For the negative Smith generator',r'primitive on the order-eight core image.')+r'primitive on the order-eight core image.',
    excerpt(new,'The core quotient has order eight,','The ambient graph row'),
    'The literal fibre generator -[e1 wedge e2], detected by the unchanged u, fixes the order and sign without depending on an unspecified Smith basis.')
defect('support-thom-involution','D25','original D.OF6, D.OF8-D.OF11 support/positive-Thom identification',
    'The relative component Thom cochains identify',
    excerpt(new,'Let $e_v$ be the positive relative Thom class','identify\n')+'identify',
    'The displayed wall degrees correspond exactly to positive divisor coefficients h=-Psi. The inverse is negation. The final proof carries this map through the connecting covector, the entire Aff module, both constants and the actual period line maps with eighth tensor factors. No cyclic u sign change is made.')
defect('literal-character','D25','original D.OL7 in the fixed delta-circle convention',
    excerpt(old,'The scalar fibre character supplied by the support',r'This is periodic'),
    excerpt(new,'The circle used here is generated by',r'This is periodic'),
    'For the actual u and retained wall degrees, canonical positive O(D_h) has weight +m(delta), with h=-Psi. Thus lambda=(0,-3r). The original +(3r) fails the actual O(d) endpoint relation and is not corrected by a common character; theorem evaluations remain zero.')
defect('finite-character-extension','D22','original D.OL7 common-character comparison',
    edits[16]['old_text'],
    excerpt(new,'Each connecting orbit curve has scalar tangent weight','The integral component divisors'),
    'The connected actual orbit graph and the explicit O(d) transition/inverse prove the finite-coefficient assertion, including the example of degree6 and weights0,-6.')
defect('signed-integer-representatives','D25','original D.OL10-D.OL11 integer representative formulas',
    r'\sum d_{r,s}\lambda_{r,s}=336,',
    r'\sum d_{r,s}\lambda_{r,s}=-336,',
    'The linear sum, P2(u)y integer representative and complete common-character polynomials are changed consistently with the corrected literal lambda. All full-modulus evaluations remain zero; this is a consequence of the same coupled sign repair.')
defect('staged-frame-action','D25','staged v003 receiver, support-to-fibre frame paragraph',
    edits[42]['old_text'],edits[42]['new_text'],
    'The staged shorthand confused a rational frame exponent with its canonical fibre action. Root found it during review. v005 proves the contragredient section action, the h=-Psi map and the delta/W relation explicitly. This is a review repair, not an additional independent check.')
defect('transfer-degree','D22','staged v003 receiver, complete critical chain',
    edits[32]['old_text'],edits[32]['new_text'],
    'A degree16 transfer has p_*tr=16id, with chart inverses only on individual lifted simplices. The receiver now states the exact map.')
record=re.search(r'\\StatementRecord\{maps:src:D.2.53\}.*',oldstatement).group(0)
defect('statement-header','D10','original theorem header',record,'',
    'Remove the process/uses header while retaining the permanent label and hypertarget. Final printed small-tag formatting belongs to the root unit pass; this proposal does not close that unit criterion.')
defect('statement-title','D02','original theorem title',
    'complete primitive cubic, fundamental-class and refined invariants of the weighted OS45 example',
    'Invariants of the marked weighted OS45 manifold','Use a short mathematical title for the retained single statement.')
write('S6_SERIES_PUBLISH_III_02LV_defects.tsv',fields,defects)

eventfields=['statement_id','date','who','type','outcome','event_id','phase','source_file','source_row','source_event_type','evidence_group','publish_input_file','publish_input_row','date_utc','where']
events=[]
def event(key,typ,outcome):
    events.append(dict(statement_id=sid,date='2026-11-25',
      who='GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; numerical effort not separately exposed; continuation eight with attributed continuation seven inputs',
      type=typ,outcome=outcome,event_id='publish:c8:III:02LV:'+key,
      phase='continuation8-support-admission',source_file='S6_SERIES_PUBLISH_III.tex',source_row='21458',
      source_event_type=typ,evidence_group='publish:c7-c8:III:02LV',
      publish_input_file='agents/continuation8_iii_lv/S6_SERIES_PUBLISH_III_02LV_CHECK_EVENTS.tsv',
      publish_input_row=str(len(events)+2),date_utc=now,
      where='agents/continuation8_iii_lv/S6_SERIES_PUBLISH_III_02LV_comparison.md'))
event('inherited-fresh-targeted','targeted proof check',
 'Admit the completed936-line pre-exposure derivation frozen2026-11-25T11:16:04.388868+00:00 before the11:18:22.502431 original release. Checkpoint91 records its actual fresh executions and whole-source/output readings. Root and the receiving checker reread all936 lines in continuation eight. It proves the actual marked periods, primitive lattice, full cubic/finite target, global primitive sphere, reference parity1 and integral critical-chain link-1. The final comparison adapts its Thom-Gysin argument to the retained original source sphere and explicitly reconciles the support/Thom convention. This imports completed prior work; it claims no new blind derivation in continuation eight and closes no required identity.')
event('coupled-sign-repair','refuted, with the refined statement\'s id',
 'Refined statement id: maps:src:D.2.53. All theorem conclusions stand. Repair only the coupled original OF6 positive-Thom identification and OL7 positive fixed character for the fixed cyclic u and delta-circle. The exact involution h=-Psi, negative connecting/affine module map, actual period line map with eighth tensor factors and oriented clutch preserve u(e1 wedge e2)=1 and all wall/mixed values; canonical +m fibre action then gives lambda=(0,-3r). The actual degree6 orbit has endpoint weights0,-6, refuting the old positive weight in that fixed convention. Signed integer representatives change consistently while the full mod8/mod16 evaluations stay zero. The staged v003 negative-frame shorthand was also corrected during review. These are bounded D25 proof repairs, with no D26/D27 theorem refutation.')
event('post-exposure-exact-comparison','computation or formal certificate',
 'Executed five wholly read unchanged attached historical programs at15:31:10-15:31:11 UTC; all exit0, actual separate stdout/stderr retained and checker-read. The new160-line arithmetic comparison proves the two-way23-row quotient map and integer relation lifts, all680 cubic and120 mixed coordinates, exact Picard map/inverse, integral critical-prism difference and source endpoint identities. Root read that whole source and18 actual stdout lines. The new character-transport program at15:54:15 verifies all-integer period identities, all32 actual orbit transitions, normal weights and full character polynomials; checker read its whole source and10 stdout lines. All mathematical-program stderr files are empty. These are post-exposure computations, not a fresh independent implementation of the historical programs; they do not themselves prove framing or refined linking. No whole manual JSON reading is claimed.')
event('whole-comparison','used and rechecked in this run',
 'Whole original statement56 lines, main proof870 lines and following refined proof380 lines were read by root and the receiving checker, together with the entire936-line fresh derivation. The complete receiving mathematics is1365 lines: root read all1304 staged lines and the exact final diff; the checker did the same. All69 labels and hypertargets remain in one theorem/one proof. Exact boundary Ext terms, actual original edge and theta/Phi source map, Bott degree4 reference, full Wang detector, integral critical nullchain and Thom-Gysin injectivity prove P_ref=0. The comparison/source records distinguish actual primary readings, historical replays, inherited fresh runs and non-read JSON. Canonical source application, unit editing, final build/page reading and provenance remain open. 02LV is supporting work outside the128 required identities; LG original/history remain closed throughout this comparison.')
write('S6_SERIES_PUBLISH_III_02LV_CHECK_EVENTS.tsv',eventfields,events)
print('UTC',now)
print('REPLACEMENTS',len(replacements),'EXACT_GUARDS_AND_INVERSE',True)
print('DEFECT_ROWS',len(defects),'EVENTS',len(events))
print('LABELS_TARGETS',69,69,'ONE_STATEMENT_ONE_PROOF',True)
print('CANONICAL_UNCHANGED',sha256((ROOT/'S6_SERIES_PUBLISH_III.tex').read_bytes()).hexdigest())
