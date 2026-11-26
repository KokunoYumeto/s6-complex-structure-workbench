"""Bounded bibliography placement and exact preprint/publication metadata."""
from S6_SERIES_PUBLISH_c3_edit import *
import hashlib

old = r'''\newblock arXiv:math/0208050v1, 6 August 2002.
\newblock URL \url{https://arxiv.org/pdf/math/0208050v1}.'''
new = r'''\newblock arXiv:math/0208050v1, 6 August 2002.
\newblock Published in \emph{The Ramanujan Journal}, 7(1--3):343--366, 2003.
\newblock \doi{10.1023/A:1026219901284}.
\newblock The locators used here refer to the arXiv version.
\newblock URL \url{https://arxiv.org/pdf/math/0208050v1}.'''
apply_edit(old,new,'II-C3-BIB-ATKIN-PUBLICATION',['D18'],
 'AtkinGarvan2002','Bibliography',
 'Add the related journal publication verified in Garvan\'s primary publication list, retaining the exact 2002 preprint and its locators. The author notes typographical differences in the published version; no identity of numbered loci is assumed.')

old = r'''\newblock arXiv:1810.05768v3, 26 June 2020.
\newblock URL \url{https://arxiv.org/pdf/1810.05768v3}.'''
new = r'''\newblock arXiv:1810.05768v3, 26 June 2020.
\newblock Published as M.~S. Verbitsky, V. Vuletescu, and L. Ornea,
\emph{Russian Mathematical Surveys}, 76(2):261--289, 2021.
\newblock \doi{10.1070/RM9858}.
\newblock The locators used here refer to the arXiv version.
\newblock URL \url{https://arxiv.org/pdf/1810.05768v3}.'''
apply_edit(old,new,'II-C3-BIB-OVV-PUBLICATION',['D18'],
 'OVV2020','Bibliography',
 'Retain the author order and exact v3 preprint whose title page was read; give the related English publication with its own different author order, journal pages and DOI from the primary journal page. No unverified equivalence of numbered source loci is asserted.')

text=SOURCE.read_text()
start=text.index(r'\bibitem[Koenigs(1884)]{Koenigs1884}')
end=text.index(r'\bibitem',start+1)
block=text[start:end]
assert 'Gabriel Koenigs.' in block and block.count('\\bibitem')==1
without=text[:start]+text[end:]
target=r'\bibitem[Kulikov(1977)]{Kulikov1977}'
assert without.count(target)==1
after=without.replace(target,block+target,1)
assert identifiers(text)==identifiers(after)
SOURCE.write_text(after,newline='\n')
append_rows(ROOT/'S6_SERIES_PUBLISH_defects_II.tsv',[
 dict(change_id='II-C3-BIB-KOENIGS-ORDER',type='D18',statement_id='Koenigs1884',
 old_location='Bibliography, after Favre and before Fernandez de Bobadilla',old_page='working PDF',
 new_location='Bibliography, after Kodaira and before Kulikov',new_page='integrated build pending',
 old_text=block,new_text=block,
 reason='Place the byte-identical entry at its alphabetical location.',
 review_status='Root read the complete entry and both old and receiving adjacent bibliography entries; no metadata or mathematical content change.')], 'change_id')

def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
stamp=now()
records=[
 dict(source='II-C3-BIB-ATKIN-PUBLICATION-METADATA',url='https://qseries.org/fgarvan/publist.html; https://arxiv.org/pdf/math/0208050v1',
 version='Author publication list opened by web search 22 November 2026; arXiv v1 6 August 2002',
 locus='Author list entry for Relations between the ranks and cranks of partitions; preprint title page',date_utc=stamp,
 sha256=sha('/workspace/scratch/9fcd229a9ed4/tmp/c3_provenance_primary/AtkinGarvan2002.pdf'),
 own_word_summary='The author lists The Ramanujan Journal 7(1–3), 343–366 (2003), DOI10.1023/A:1026219901284, and notes typographical differences. The preprint title page identifies Atkin and Garvan and the v1 date.',
 use='Bibliographic metadata only. Exact preprint locators remain authoritative. No new reading of the mathematical proofs or published article is claimed.'),
 dict(source='II-C3-BIB-OVV-PUBLICATION-METADATA',url='https://arxiv.org/abs/1810.05768; https://www.mathnet.ru/eng/rm9858; https://arxiv.org/pdf/1810.05768v3',
 version='arXiv v3 26 June 2020 and Russian Mathematical Surveys76(2)(2021),261–289',
 locus='Complete relevant abstract-page metadata, primary journal bibliographic entry, and preprint title-page author/date lines',date_utc=stamp,
 sha256=sha('/workspace/scratch/9fcd229a9ed4/base/S6_PUBLISH_c3_foundations_sources/S6_SERIES_PUBLISH_OVV2020_v3.pdf'),
 own_word_summary='The preprint title page orders the authors Ornea, Verbitsky and Vuletescu. The journal page orders them Verbitsky, Vuletescu and Ornea and identifies DOI10.1070/RM9858 and pages261–289.',
 use='Add related publication metadata with the exact separate author orders. Mathematical citations retain the v3 locators. No new theorem/proof or published-version comparison is claimed.')]
append_rows(ROOT/'S6_SERIES_PUBLISH_c3_primary_readings.tsv',records,'source')
add_event('AtkinGarvan2002;BBK2019;GCP2024;OVV2020;MPW2005Hirzebruch;Steenbrink1999;Koenigs1884',
 'II-C3-BIB-ORDER-PUBLICATION-METADATA','used and rechecked in this run',
 'Root read the complete bibliography in three source ranges, then checked the named primary metadata. BBK v3, GCP v2, MPW v1 and Steenbrink v1 match their arXiv records. Atkin and OVV receive related publication metadata while their precise cited preprint versions remain explicit. OVV preprint and journal author orders were individually read and retained. Koenigs moves byte-identically into alphabetical order. This is bounded bibliographic verification: it does not close every D18 row, prove absence of later literature, or claim additional mathematical source proofs.',
 'Bibliography and source title-page/metadata loci recorded in primary readings',source=__file__)
print('Two version-explicit publication entries added; Koenigs moved byte-identically. Bibliography D18 remains open for pending source receivers.')
