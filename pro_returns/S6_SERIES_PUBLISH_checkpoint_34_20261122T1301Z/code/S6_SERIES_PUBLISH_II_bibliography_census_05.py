#!/usr/bin/env python3
"""Record a full printed-bibliography reading and an edition-preserving merge map."""
from pathlib import Path
import datetime as dt, hashlib, io, json, re, tarfile

R=Path(__file__).resolve().parents[1]
O=R/'records/S6_SERIES_PUBLISH_II_bibliography_census_05.json'
assert not O.exists()
sha=lambda b:hashlib.sha256(b).hexdigest()
source=(R/'S6_SERIES_PUBLISH_II.tex').read_bytes();s=source.decode()
a=s.index(r'\begin{thebibliography}');z=s.index(r'\end{thebibliography}',a)+len(r'\end{thebibliography}')
positions=list(re.finditer(r'\\bibitem\[.*?\]\{([^}]+)\}',s[a:z],re.S))
entries=[]
for i,m in enumerate(positions):
    end=positions[i+1].start() if i+1<len(positions) else s[a:z].index(r'\end{thebibliography}')
    t=s[a+m.start():a+end]
    entries.append(dict(key=m[1],bytes=len(t.encode()),sha256=sha(t.encode()),
                        first_line=s.count('\n',0,a+m.start())+1))
receipt=R/'agents/ii_infra/recovery_20261121/F7_primary_inputs/S6_SERIES_PUBLISH_II_KT_v4_source_binding_receipt.json'
prior=json.loads(receipt.read_text())
archive=receipt.parent/'S6_SERIES_PUBLISH_II_KT_2406.15158v4_source.download'
b=archive.read_bytes();assert sha(b)==prior['download_sha256']
with tarfile.open(fileobj=io.BytesIO(b),mode='r:*') as t:
    v=t.extractfile('ClassificationInoue-article-new.tex').read()
local=R.parent/'S6_PUBLISH_literature_arxiv/2406.15158/ClassificationInoue-article-new.tex'
assert v==local.read_bytes() and sha(v)==prior['attached_source_sha256']
cites=[]
for m in re.finditer(r'\\cite(?:p|t)?(?:\[[^\]]*\])?\{KhaledTeleman2026(?:Journal)?\}',s[:a]):
    cites.append(dict(line=s.count('\n',0,m.start())+1,exact=m.group(),
                      edition='journal' if 'Journal}' in m.group() else 'arXiv2406.15158v4'))
d=dict(created_utc=dt.datetime.now(dt.timezone.utc).isoformat(),source_sha256=sha(source),
       full_printed_bibliography_reading=dict(first_line=80616,last_line=81948,
          ranges_actually_displayed=[[80616,81038],[81039,81482],[81483,81948]],
          bibliography_sha256=sha(s[a:z].encode()),entries=len(entries),reader='root'),
       entry_bindings=entries,
       primary_metadata_read=[
         dict(url='https://www.numdam.org/item/SSS_1976-1977____A16_0/',ref='turn689383585view1',
              finding='Teissier precedes Merle in the archive author order; existing title, year and pages agree. No correction is indicated.'),
         dict(url='https://arxiv.org/abs/1709.00062',ref='turn361647940view1',
              finding='Version3 dated20May2019 names Buonerba, Bogomolov, Kurnosov in that order. Existing author order and version agree. No correction is indicated.'),
         dict(url='https://arxiv.org/abs/2406.15158',ref='turn361647940view2',
              finding='Version4 dated13July2026, Khaled and Teleman, On the classification of Inoue surfaces. The exact attached source is bound separately.'),
         dict(url='https://www.ms.u-tokyo.ac.jp/journal/33-3-1.pdf',ref='turn361647940view0',
              finding='Original journal title page: same authors and title, volume33(2026),283--357. Theorem3.1 on303 and proof of Remark3.5 on305 were opened as text through turn715682849view1/2. This reading adds no full-source proof credit.')],
       failed_web_opens=['https://arxiv.org/abs/1709.00062v3','https://arxiv.org/abs/2406.15158v4','https://arxiv.org/pdf/2406.15158v4','https://www.ms.u-tokyo.ac.jp/journal/33-3-1.html'],
       exact_preprint_binding=dict(prior_receipt=str(receipt.relative_to(R)),prior_receipt_sha256=sha(receipt.read_bytes()),
          archive_sha256=sha(b),attached_source_sha256=sha(v),member='ClassificationInoue-article-new.tex',all_bytes_identical=True),
       citations_to_merge=cites,
       proposed_map='Map (old bibliography key, edition, cited locus) to (KhaledTeleman2026, same edition, same locus). The merged entry contains both original edition URLs. Each preprint use explicitly says arXivv4; each journal use explicitly says journal edition. No identification of the editions, their numbering or their full mathematical contents is asserted.',
       source_changes=0,check_events_added=0,global_D18_closed=False,
       other_scope='Papikian retains the original dated author notes and their recorded URL, as already resolved in bibliography_editions_04. This census does not reopen that completed edition identity.')
O.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
print(json.dumps(dict(path=str(O.relative_to(R)),sha256=sha(O.read_bytes()),entries=len(entries),edition_specific_citations=len(cites)),indent=2))
