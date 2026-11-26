from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import csv
import json
import re

ROOT=Path('/workspace/scratch/9fcd229a9ed4/base/S6_SERIES_PUBLISH_checkpoint_35')
OUT=ROOT/'agents/continuation3_provenance/resolution_locator'
REL=OUT.relative_to(ROOT).as_posix()
OUT.mkdir(exist_ok=True)
main=(ROOT/'S6_SERIES_PUBLISH_II.tex').read_text()
original=(OUT/'S6_SERIES_PUBLISH_UN11_original.tex').read_text()
assert main.count(original)==1
stamp=datetime.now(timezone.utc).isoformat()

def tsv(name,rows):
    with (OUT/name).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t',lineterminator='\n')
        w.writeheader();w.writerows(rows)

old1=r'\StatementRecord{cdp:st:C.2.UN.11}{proved}{01CO}{\cref{night:P4.13,cdp:st:C.2.UN.1,cdp:st:C.2.UN.4}; \cite[Theorem~1.6]{BierstoneMilman1997}}'
new1=r'\StatementRecord{cdp:st:C.2.UN.11}{proved}{01CO}{\cref{night:P4.13,cdp:st:C.2.UN.1,cdp:st:C.2.UN.4}; \cite[published version, (0.1)(1), p.~208; Theorem~1.6 and Remarks~1.7(2), pp.~215--216]{BierstoneMilman1997}}'
old2=r'''Resolve the projective quotient and then its
two central supports by projective blowups
over $0$ and $\infty$, using
\cite[Theorem~1.6]{BierstoneMilman1997}.
The resulting threefold is smooth and projective,
with SNC supports, and the punctured family is
unchanged.'''
new2=r'''Choose a projective embedding $X\hookrightarrow\PP^N$.
Apply \cite[published version, (0.1)(1), p.~208; Theorem~1.6
and Remarks~1.7(2), pp.~215--216]{BierstoneMilman1997}
first to this reduced algebraic $X$, obtaining
$\rho:X_1\to X$ with $X_1$ smooth, and then to the reduced
divisor $D=((f\circ\rho)^{-1}\{0,\infty\})_{\rm red}$
in $X_1$. Denote the second composite by $\sigma:X_2\to X_1$.
The first centers lie over $\operatorname{Sing}X$, which is
contained in the two central fibres; the second centers lie
over $D$. Every blowup is algebraic and projective.
Thus $X_2$ is smooth and projective, the reduced inverse image
of $D$ is SNC, and $f\circ\rho\circ\sigma$ restricts to the
same quotient family over $\PP^1\setminus\{0,\infty\}$.'''
guards=[]
proposed=original
for i,(old,new) in enumerate([(old1,new1),(old2,new2)],1):
    assert main.count(old)==1 and proposed.count(old)==1
    proposed=proposed.replace(old,new)
    guards.append(dict(change_id=f'II-C3-UN11-RESOLUTION-{i:02d}',old_text=old,new_text=new))
(OUT/'S6_SERIES_PUBLISH_UN11_proposed.tex').write_text(proposed)
for pat in [r'\\label\{([^}]+)\}',r'\\hypertarget\{([^}]+)\}']:
    assert Counter(re.findall(pat,original))==Counter(re.findall(pat,proposed))
statement_end=original.index(r'\end{proposition}')
assert original[:statement_end].replace(old1,new1)==proposed[:proposed.index(r'\end{proposition}')]
tsv('S6_SERIES_PUBLISH_UN11_resolution_guards.tsv',guards)
defects=[]
for row in guards:
    defects.append(dict(change_id=row['change_id'],type='D18',statement_id='cdp:st:C.2.UN.11',
        old_location='Exact current UN11 input record or projective quotient resolution paragraph',old_page='Final concordance pending',
        new_location='Same UN11; projective embedding and two exact embedded-resolution applications',new_page='Integrated PDF pending',
        old_text=row['old_text'],new_text=row['new_text'],
        reason='Identify the published layout and algebraic scope, then expose the exact quotient embedding, central divisor, two resolution maps and unchanged punctured restriction. The entire printed statement, 19-row table, Euler adjustments and monodromy calculations are preserved.',
        review_status='Source ready after complete old/receiving comparison; bounded D18 repair only, no new containing-unit or final-PDF closure.'))
tsv('S6_SERIES_PUBLISH_UN11_resolution_defects.tsv',defects)
with (ROOT/'agents/continuation3_provenance/equivariant_lift/S6_SERIES_PUBLISH_lift_sources.tsv').open() as f:
    source=next(r for r in csv.DictReader(f,delimiter='\t') if r['source_key']=='BierstoneMilman1997')
source.update(locus_read='Published algebraic/analytic scope (0.1)(1)–(2), p.208; embedded setup pp.212–213; complete Theorem1.6 and Remarks1.7, pp.215–216; complete Theorem1.10 statement and normal-crossings interpretation, pp.216–217',
    own_paraphrase='The algebraic version supplies a finite tower of algebraic smooth-center blowups for a quasi-compact reduced embedded space, preserving its regular locus and making the final strict transform smooth with normal crossings against the exceptional divisors. For a reduced divisor in a smooth ambient space, this gives SNC total support.',
    exact_application='UN11 uses the same projective finite quotient X=(A×P1)/<g,zeta_M>. Embed X in PN, use Theorem1.6 to obtain rho:X1→X, and apply it again to the reduced central divisor D in X1. The composite f rho sigma is unchanged off0/infinity; every blowup is projective and all centers are over those two values. The proof subsequently uses its original parity and vertical-blowup maps unchanged.',
    read_extent='Reopened the same published primary PDF already freshly retrieved in this continuation and read the complete named setup/statements/remarks. The full constructive algorithm proof in ChaptersII–III was not reread or credited. Theorem1.10 was read for scope comparison; the receiving application uses Theorem1.6. The complete original and receiving UN11 statement/proof were read; this is exposed used-and-rechecked work, not an independent source or theorem check.',date_utc=stamp)
tsv('S6_SERIES_PUBLISH_UN11_resolution_sources.tsv',[source])
eid='publish:c3:UN11:published-resolution-application'
events=[dict(statement_id='cdp:st:C.2.UN.11',date='2026-11-22',who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; inherited effort not separately exposed; continuation3 provenance',
    type='used and rechecked in this run',outcome='Read complete original and receiving UN11, including all19 signatures, the elliptic/Jacobian/Gaussian realizations, quotient monodromy, two resolution applications, exact vertical Euler adjustments and SNC charts. Reopened the published BM algebraic setup and complete named statements. Preserve every printed assertion and target; repair only the exact source locator and its projective embedded application. No source algorithm-proof, independent, computation or final-PDF credit.',
    event_id=eid,phase='bounded primary-source application comparison',source_file=REL+'/S6_SERIES_PUBLISH_UN11_resolution_CHECK_EVENTS.tsv',source_row='',
    source_event_type='used and rechecked in this run',evidence_group=eid,publish_input_file='',publish_input_row='',date_utc=stamp,where='Complete original/receiving UN11; published BM (0.1)(1) p208 and Theorem1.6/Remarks1.7 pp215–216')]
tsv('S6_SERIES_PUBLISH_UN11_resolution_CHECK_EVENTS.tsv',events)
print(json.dumps({'guards':len(guards),'defects':len(defects),'events':len(events),'sources':1,'statement_unchanged_except_hidden_input_record':True,'all_targets_preserved':True,'shared_main_written':False}))
