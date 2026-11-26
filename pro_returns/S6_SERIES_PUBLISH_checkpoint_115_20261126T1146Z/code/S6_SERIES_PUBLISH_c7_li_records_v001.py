"""Write LI's exact defect rows and scope-specific check events, without admission."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import csv
import io
import re

ROOT=Path(__file__).resolve().parents[1]
LANE=ROOT/'agents/continuation7_iii_all_parity_receiving'
P='S6_SERIES_PUBLISH_III_02LI'
ID='maps:src:D.2.41'
raw=(ROOT/'S6_SERIES_PUBLISH_III.tex').read_bytes()
assert sha256(raw).hexdigest()=='9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0'
canonical=raw.decode()
receiver=(LANE/f'{P}_receiving.tex').read_text()
assert sha256(receiver.encode()).hexdigest()=='90cfbed90db4de6dfbadd2b495733d2bd35eebe845ad2dc516c10999c8138d3f'
with (LANE/f'{P}_replacements.tsv').open(newline='') as stream:
    guards=list(csv.DictReader(stream,delimiter='\t'))
assert len(guards)==2
assert receiver.rstrip('\n')=='\n\n'.join(g['new_text'].rstrip('\n') for g in guards)
old_statement,old_proof=[g['old_text'] for g in guards]
new_statement,new_proof=[g['new_text'] for g in guards]
for g in guards:
    assert canonical.count(g['old_text'])==1
    for pattern in (r'\\label\{([^}]+)\}',r'\\hypertarget\{([^}]+)\}',r'\\tag\{([^}]+)\}'):
        assert sorted(re.findall(pattern,g['old_text']))==sorted(re.findall(pattern,g['new_text']))
assert receiver.count(r'\begin{proof}')==receiver.count(r'\end{proof}')==1
assert r'\textnormal{\small tag 02LI.}' in new_statement
assert r'\StatementRecord' not in receiver and r'\path{' not in receiver

def span(text,start,end):
    a=text.index(start)
    return text[a:text.index(end,a)+len(end)]

defects=[]
def add(kind,suffix,old,new,reason,destination=None):
    assert canonical.count(old)==1,(suffix,'old text')
    if destination is None:
        assert new in receiver,(suffix,'new text')
        destination=str((LANE/f'{P}_receiving.tex').relative_to(ROOT))
    defects.append(dict(change_id=f'c7-III-02LI-{suffix}',type=kind,statement_id=ID,
        old_location='S6_SERIES_PUBLISH_III.tex:'+str(canonical[:canonical.index(old)].count('\n')+1),
        old_page='',new_location=destination,new_page='pending final typeset page concordance',
        old_text=old,new_text=new,reason=reason,
        review_status='staged; root admission, source application and final page review pending'))

add('D26','pattern-scope',
    span(old_statement,'Every positive iterate', 'Star caps remain\noriginal.'),
    span(new_statement,'There are $495$', 'replacements.'),
    'The broad pattern family has495 and allows finite-good III*/IV* choices; its all-star-original subset has459. The explicit inclusion j and replacement pi satisfy pi j=identity and describe all36 additional patterns. Every integral formula holds on both sets. Only the conflated scope/count is refuted.')
add('D10','machine-header',
    next(line for line in old_statement.splitlines() if line.startswith(r'\StatementRecord')),
    r'\textnormal{\small tag 02LI.}',
    'Replace the machine record by the small permanent tag and a mathematical title. All16 labels/targets and15 equation tags remain.')
add('D22','bar-section-inverse',
    span(old_proof,'Both cone homologies', 'directly.'),
    span(new_proof,'We specify its inverse.', 'and the integral isomorphism in \\eqref{maps:eq:D.BC11}.'),
    'The original five-lemma argument is valid. Give the chosen graph-cycle section, fibre correction, coordinate torus representatives and both inverse composites within the same bar proof. This adds explicit marking data and does not refute the isomorphism.')
add('D22','full-integral-gluing',
    span(old_proof,'Finally the relative pair sequence', 'unchanged.'),
    span(new_proof,'Fill the finite and regular logarithms first', '$T=\\operatorname{Tor}\\mathcal C$.'),
    'Prove the relative splitting with injective finite-disc boundary P, the full equation Mz=Pz\u2032, its integer kernel index, and actual closing chains including g delta. The original torsion conclusion stands; the expanded argument specifies every quotient and inverse at common even factors.')
add('D22','peripheral-shear-inverse',
    span(old_proof,'These\nare exactly the full normal Thom generators', 'normal-line cases.'),
    span(new_proof,'The integral marking is also explicit', 'also on the even part of $C$.'),
    'Give the full core relation map and the peripheral root shear, including p(lambda,lambda), the norm/root identity and inverse column operation. All five original normal columns are valid and retained.')
add('D18','bar-source-pages',
    r'\cite[Chapter I, Section 5]{manBrown82}.',
    r'\cite[Chapter I, Section 5, pp.~18--19]{manBrown82}.',
    'Root visually opened both printed pages18–19 of the exact1982 book scan. These contain the standard resolution, contraction, bar differential and induced degenerate-quotient contraction used here.')
bibold=span(canonical,r'\bibitem[Brown(1982)]{manBrown82}',r'\newblock \emph{Verified}.')
bibnew=(LANE/f'{P}_staged_bibliography.bib').read_text().rstrip('\n')
add('D18,D08','brown-book-record',bibold,bibnew,
    'Preserve the cited1982 book, volume87 and its DOI; use its publisher record as the URL and move source-verification history to the comparison. Staged for the final bibliography integration.',
    str((LANE/f'{P}_staged_bibliography.bib').relative_to(ROOT)))
add('D09,D13','following-executable-scope',
    span(old_proof,'The executable', 'homology.'),'',
    'The complete historical source and saved results were compared at their exact scopes. Move the executable and output narrative to the check/program records; state the quantified natural-row scope positively in the theorem and retain the full homology algorithm in its single proof.')
add('D02','defensive-formality',
    'This is a model for the actual linear torus bundle,\nnot an assertion of equivariant formality.',
    'The graph of bar models has the same marked\n$\\Lambda\\rtimes F_r$ group; the period maps induce the indicated\nmaps on each vertex and cylinder, hence on each peripheral torus.',
    'Give the geometric period and mapping-cylinder morphisms, including their peripheral marking, as the mathematical justification.')

now=datetime.now(timezone.utc).isoformat()
group='publish:c7:III:02LI'
events=[]
def event(kind,suffix,outcome,source,when=now,phase='after original exposure'):
    events.append(dict(statement_id=ID,date=when[:10],
        who='GPT-6 Astra (OpenAI), ChatGPT Pro mode, continuation seven; root and attributed fresh/peer checkers',
        type=kind,outcome=outcome,event_id=group+':'+suffix,phase=phase,
        source_file=source,source_row='',source_event_type=kind,evidence_group=group,
        publish_input_file=str((LANE/f'{P}_CHECK_EVENTS.tsv').relative_to(ROOT)),
        publish_input_row=str(len(events)+2),date_utc=when,
        where=str((LANE/f'{P}_comparison.md').relative_to(ROOT))))

event('targeted proof check','fresh',
    'Complete1262-line fresh derivation, attributed root270-line bar core and full LH local inputs, written and root-read before individual release. Proves integral binomial and descending-word comparison, explicit cycle inverse, full five-column Thom/core maps, even peripheral shear, all-weight free-cap cover/transfer, indexed component-disc splitting, Seifert maps and full duality for every positive weight and permitted affine parameter. The later bounded peer has its separately dated review. No original/history exposure is credited to this fresh derivation.',
    'agents/continuation7_iii_all_parity/S6_SERIES_PUBLISH_III_02LI_fresh_derivation.md',
    '2026-11-25T06:12:23.652753+00:00','before original exposure')
event('computation or formal certificate','new-ordered-and-saved-comparison',
    'Fresh ordered-word v01 failed at an integral matrix represented over a rational domain; v02 checked integrality and succeeded. Retain both608-line sources and complete19/28-line combined streams. Root read all1601 saved-data lines. Success scope:4002 global presentations,1074 shared-even cases,17192 lifts,15468 cover/transfer maps,5726 five-column maps,1380 finite-power/shear cases. Separately, the post-exposure validator rebuilt172 raw rows and checked all35 stored historical matrices,141 whole quadratic coefficient blocks and65 nonidentity-power tests; its first run succeeded, with39 stdout lines and empty stderr. No historical target program was executed or missing historical stdout inferred. The deletion witnesses are not equated with the legitimate odd coordinate algorithm.',
    'code/S6_SERIES_PUBLISH_c7_li_ordered_words_v01.py; code/S6_SERIES_PUBLISH_c7_li_ordered_words_v02.py; code/S6_SERIES_PUBLISH_c7_li_saved_output_check_v001.py')
event('refuted, with refined statement\u0027s id maps:src:D.2.41','scope-refined',
    'D26 refutes the joint495 count with all star caps original. The broad family has495; the subset has459. Inclusion j and sitewise replacement pi satisfy pi j=identity and locate exactly36 extra finite-star choices. The same complete integral proof establishes the algorithm on both families. Every BC formula and all stated homology conclusions stand.',
    str((LANE/f'{P}_comparison.md').relative_to(ROOT)))
event('used and rechecked in this run','whole-original-and-receiver',
    'After the06:26:55.413316 individual release, root read the entire statement, all199 proof lines, all11 original proof items, all15 BC displays and following14 auxiliary lines, then the entire498-line replacement. The final499-line version adds only the small printed tag with an exact inverse patch. Fresh author read the whole498-line receiver against frozen Sections6–12 and bar formulas, finding no lost hypothesis or map. Root read the entire202-line historical source, all new receiving/retrieval/validator sources and actual streams, and visually read Brown printed18–19. Historical JSON was parsed by the new validator; root does not claim manual reading of every historical serialized entry. One bar proof, two exact guards and16labels/targets15tags are preserved; the alternative central-extension splitting remains check evidence. Canonical, unit, build and final-page gates are unchanged.',
    str((LANE/f'{P}_comparison.md').relative_to(ROOT)))

def write(path,fields,rows):
    with path.open('x',newline='') as stream:
        writer=csv.DictWriter(stream,fields,delimiter='\t',lineterminator='\n')
        writer.writeheader();writer.writerows(rows)

assert len(defects)==9 and len(events)==4
write(LANE/f'{P}_defects.tsv',list(defects[0]),defects)
write(LANE/f'{P}_CHECK_EVENTS.tsv',list(events[0]),events)
assert (ROOT/'S6_SERIES_PUBLISH_III.tex').read_bytes()==raw
print('Staged at',now,'9 defect rows;4 scope-specific events;2 exact guards.')
for name in ('receiving.tex','comparison.md','replacements.tsv','defects.tsv','CHECK_EVENTS.tsv'):
    path=LANE/f'{P}_{name}'
    print(name,'SHA256',sha256(path.read_bytes()).hexdigest())
print('Canonical unchanged; root admission and all later publication gates remain open.')
