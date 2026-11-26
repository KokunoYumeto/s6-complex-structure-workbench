#!/usr/bin/env python3
"""Prepare exact version additions 142–145; never admit shared-source edits."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'agents/continuation3_provenance'
TMP = ROOT.parents[1] / 'tmp/c3_provenance_primary'
source = (ROOT / 'S6_SERIES_PUBLISH_II.tex').read_text()

def entry(key):
    at = source.index(']{' + key + '}', source.index(r'\begin{thebibliography}'))
    first = source.rfind(r'\bibitem', 0, at)
    last = source.find(r'\bibitem', at)
    return source[first:last].rstrip()

items = [
    ('AKMW2002',142,Path('/tmp/S6_SERIES_PUBLISH_c3_conductor_primary/AKMW2000_arxiv_v4.pdf'),
     '55bbc2c58f29d4b9dbe965035f80f3844f6968eaf98076ac625132ac3b3977a5',
     'https://arxiv.org/pdf/math/9904135v4','arXiv:math/9904135v4, 31 May 2000',
     '§1.2.4 and Lemma 1.3.1 with proof, p.6; analytic extension in §5.4, p.25',
     'The conductor agent opened and read the complete cited loci. I opened the title page and checked the arXiv v4 margin, date and file hash. Its internal typesetting date is 26 November 2024; the arXiv version identifies the cited layout. This supplies elimination of indeterminacy and its stated analytic extension, not a new factorization assertion.',
     '',
     r'''\newblock Cited preprint edition: arXiv:math/9904135v4,
31 May 2000. Page locators refer to this edition.
\newblock URL \url{https://arxiv.org/pdf/math/9904135v4}.'''),
    ('AbashevaDeev2024AB',143,TMP/'AbashevaDeev_v1.pdf',
     '506d60ef501997ba8e773dd1610a4d2c721dff120e6c5009d55a0e52245a410d',
     'https://arxiv.org/pdf/2303.10764v1','arXiv:2303.10764v1, 19 March 2023',
     'Proof of Proposition 3.1.2, p.13',
     'Read the full proposition and proof. The proof explicitly invokes torsion of the canonical bundle of a minimal compact complex surface of Kodaira dimension zero. The manuscript uses that classification fact, with its own minimality and Kodaira-dimension hypotheses; it does not apply the proposition with its separate elliptic-curve hypothesis.',
     r'\newblock URL \url{https://arxiv.org/pdf/2303.10764}.',
     r'''\newblock Cited preprint edition: arXiv:2303.10764v1,
19 March 2023. Page locators refer to this edition.
\newblock URL \url{https://arxiv.org/pdf/2303.10764v1}.'''),
    ('HondaViaclovsky2025D',144,TMP/'HondaViaclovsky_v1.pdf',
     '17104ceb6d95ae333c284ef5c377a927939a71a6ddb04e848f949456097899a6',
     'https://arxiv.org/pdf/2504.14420v1','arXiv:2504.14420v1, 19 April 2025',
     'Corollary 3.7 and proof, p.11; preceding exact sequence (3.22)',
     'Read the complete corollary and proof, including the preceding local-invariant-cycle sequence. For a fibration with irreducible central fibre it gives the stated H1 invariant-cycle comparison. The manuscript first proves irreducibility before applying it.',
     r'\newblock URL \url{https://arxiv.org/abs/2504.14420}.',
     r'''\newblock Cited preprint edition: arXiv:2504.14420v1,
19 April 2025. Page locators refer to this edition.
\newblock URL \url{https://arxiv.org/pdf/2504.14420v1}.'''),
    ('Fujino2021E',145,TMP/'Fujino2021_author.pdf',
     '1972a3eea074860f2a72360ffc4bf8dc0d76e60c8e323a0f266045bcb40fd187',
     'https://www.math.kyoto-u.ac.jp/~fujino/surfaces-classC2.pdf','author version 0.08, 20 January 2020',
     'Lemma 3.3 and Corollary 3.4, p.6',
     'Read the complete statements and proofs in the author manuscript. A normal compact surface in Fujiki class C has a Kähler resolution, and every resolution is Kähler. The proof applies this only after normalizing the surface and specifying its class-C premise.',
     r'''\newblock URL
  \url{https://www.cambridge.org/core/journals/nagoya-mathematical-journal/article/minimal-model-theory-for-log-surfaces-in-fujikis-class-mathcalc/86AAC54D7E1F3B189DE91969A584D16E}.''',
     r'''\newblock Cited author edition: version 0.08,
20 January 2020. Page locators refer to this edition.
\newblock URL \url{https://www.math.kyoto-u.ac.jp/~fujino/surfaces-classC2.pdf}.''')
]
rows=[]
evidence=[]
for key,num,path,expected,url,version,locus,note,old_tail,new_tail in items:
    data=path.read_bytes(); actual=hashlib.sha256(data).hexdigest()
    assert actual==expected,(key,actual)
    old=entry(key)
    if old_tail:
        assert old.count(old_tail)==1,key
        new=old.replace(old_tail,new_tail)
    else:
        new=old+'\n\n'+new_tail
    rows.append(dict(change_id=f'II-C3-PROV-{num}',type='D18',statement_id='bibliography:'+key,
        old_location='Paper II bibliography: '+key,old_page='cp35; final PDF concordance pending',
        new_location='Paper II bibliography: '+key,new_page='integrated build pending',
        old_text=old,new_text=new,reason=note,
        review_status='Complete entry comparison and exact version metadata reading; proposal only.'))
    evidence.append(dict(bibkey=key,url=url,version=version,sha256=actual,bytes=len(data),locus=locus,
        outcome=note,checked_utc=datetime.now(timezone.utc).isoformat(),
        primary_source_bytes='Outside checkpoint; no published content copied to deliverables.'))
for name,data in [('S6_SERIES_PUBLISH_c3_provenance_bibliography_next_edits.tsv',rows),
                  ('S6_SERIES_PUBLISH_c3_provenance_bibliography_next_sources.tsv',evidence)]:
    with (OUT/name).open('w',newline='') as f:
        w=csv.DictWriter(f,list(data[0]),delimiter='\t',lineterminator='\n')
        w.writeheader();w.writerows(data)
print('Prepared bibliography version additions II-C3-PROV-142–145; no shared source writes.')
