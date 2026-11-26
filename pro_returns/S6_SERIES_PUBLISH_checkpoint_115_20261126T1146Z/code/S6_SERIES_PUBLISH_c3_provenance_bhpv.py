#!/usr/bin/env python3
"""Prepare the exact rational-surface source application; no shared writes."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'agents/continuation3_provenance/final_sources'
OUT.mkdir(exist_ok=True)
main = (ROOT / 'S6_SERIES_PUBLISH_II.tex').read_text()
old = r'''$\pi_*\OO_S=\OO$. Leray yields $h^1(\OO_S)=0$, while all
positive plurigenera vanish. The classification \cite[Chapter~VI, Theorem~1.1, p.~243]{BHPV2004E} makes $S$
rational; in the ruled case the base genus equals $h^1(\OO_S)=0$.
'''
new = r'''$\pi_*\OO_S=\OO$. Leray yields $h^1(\OO_S)=0$, while all
positive plurigenera vanish. Since $S$ is projective, its degree-one
Hodge decomposition gives $b_1(S)=2h^1(\OO_S)=0$.
Apply \cite[Chapter~VI, Theorem~1.1 and Table~10, pp.~243--244]{BHPV2004E}
to its minimal model $S_0$. The contraction $S\to S_0$ preserves
the plurigenera and $b_1$, so $\kappa(S_0)=-\infty$ and
$b_1(S_0)=0$. Table~10 identifies $S_0$ as rational; the
birational contraction then makes $S$ rational as well.
'''
assert main.count(old) == 1
row = dict(change_id='II-C3-BHPV-P410', type='D18;D20',
    statement_id='night:P4.10', old_location='P4.10 proof, step2 classification application',
    old_page='source guard; final concordance pending',
    new_location='P4.10 proof, step2 exact minimal-model application',
    new_page='integrated build pending', old_text=old, new_text=new,
    reason='The complete classification statement is on p.243; its kappa=-infinity entries and first Betti numbers are in Table10 on p.244. For the same projective Weierstrass surface S, Hodge decomposition sends h1(O)=0 to b1=0. The contraction to S0 preserves b1 and plurigenera as stated in the source context. The rational row is therefore the exact class; the contraction is birational. Every construction, conclusion and later fundamental-group map is unchanged.',
    review_status='Complete current P4.10 statement/proof read; complete primary theorem/table and bounded receiving application read. Used and rechecked, not independent.')


def write(name, rows):
    with (OUT / name).open('w', newline='') as f:
        w = csv.DictWriter(f, list(rows[0]), delimiter='\t', lineterminator='\n')
        w.writeheader()
        w.writerows(rows)


write('S6_SERIES_PUBLISH_bhpv_guard.tsv', [row])
path = ROOT.parents[1] / 'tmp/c3_provenance_primary/BHPV2004_VI.pdf'
raw = path.read_bytes()
assert hashlib.sha256(raw).hexdigest() == 'a566954023fd786219fd0185f97ea0e13a045999ec02d9ef30728dd3aa05f1a4'
now = datetime.now(timezone.utc).isoformat()
write('S6_SERIES_PUBLISH_bhpv_sources.tsv', [dict(
    source_key='BHPV2004E',
    url='https://page-one.springer.com/pdf/preview/10.1007/978-3-642-57739-0_7',
    version='Compact Complex Surfaces, second edition, Springer2004; official two-page ChapterVI preview',
    locus_read='Complete Theorem1.1 p.243; complete Table10 and its preceding/following context p.244; page244 rendered and visually read',
    sha256=hashlib.sha256(raw).hexdigest(), bytes=len(raw),
    own_paraphrase='Every compact connected complex surface has a minimal model in the listed classes. The classes are identified by plurigenera and first Betti number, both unchanged by blowups. In Kodaira dimension minus infinity, the rational row has b1=0, classVII has b1=1, and a ruled surface of positive base genus g has b1=2g.',
    exact_application='The projective surface S in P4.10 has h1(O_S)=0 and all positive plurigenera zero by its displayed relative-duality/Leray computation. Its Hodge decomposition gives b1=0. Transfer these invariants through S→S0 and select the rational row. The birational contraction identifies S as rational. This leaves all explicit Weierstrass, small-resolution and fundamental-group constructions untouched.',
    read_extent='Both complete preview pages read, including the entire theorem and table. The later classification proof is outside the official preview and is not claimed read. Fresh direct HTTP200 PDF retrieval has identical393360bytes/hash. No publication bytes are written to checkpoint outputs.',
    date_utc=now)])
write('S6_SERIES_PUBLISH_bhpv_CHECK_EVENTS.tsv', [dict(
    statement_id='night:P4.10', date=now[:10],
    who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; continuation3 provenance',
    type='used and rechecked in this run',
    outcome='Read the complete current P4.10 owner/proof and exact BHPV Theorem1.1/Table10 in the second-edition publisher preview. The source is applied to the same projective surface via Hodge decomposition and its minimal-model contraction. Checked the full bounded receiving paragraph. No independent derivation, complete classification-proof read, final-PDF or P4.11 credit.',
    event_id='publish:c3:provenance:BHPV-P410', phase='publication exact primary application',
    source_file='agents/continuation3_provenance/final_sources/S6_SERIES_PUBLISH_bhpv_CHECK_EVENTS.tsv',
    source_row='', source_event_type='used and rechecked in this run',
    evidence_group='publish:c3:provenance:BHPV-P410', publish_input_file='', publish_input_row='',
    date_utc=now, where='P4.10 step2; BHPV second-edition VI1.1 and Table10')])
print('Prepared one exact P4.10 guard, one primary-source row and one exposed event; no shared writes.')
