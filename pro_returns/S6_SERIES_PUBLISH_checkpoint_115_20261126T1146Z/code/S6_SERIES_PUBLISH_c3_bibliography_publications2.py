"""Add DOI-registered publication data while preserving cited preprint loci."""
from S6_SERIES_PUBLISH_c3_edit import *
import hashlib,json

items=[
 ('GCP2026','GCP2024','10.1112/jlms.70699',
  r'''\newblock arXiv:2401.14951v2, 30 January 2024.
\newblock URL \url{https://arxiv.org/abs/2401.14951v2}.''',
  r'''\newblock arXiv:2401.14951v2, 30 January 2024.
\newblock Published in \emph{Journal of the London Mathematical Society},
114(3):e70699, 2026. \doi{10.1112/jlms.70699}.
\newblock The locators used here refer to the arXiv version.
\newblock URL \url{https://arxiv.org/abs/2401.14951v2}.'''),
 ('MPW2007','MPW2005Hirzebruch','10.1142/9789812707499_0032',
  r'''\newblock arXiv:math/0509451v1, 20 September 2005.

\newblock URL \url{https://arxiv.org/pdf/math/0509451v1}.''',
  r'''\newblock arXiv:math/0509451v1, 20 September 2005.
\newblock Published in \emph{Singularity Theory: Proceedings of the
2005 Marseille Singularity School and Conference}, pages 745--760,
World Scientific, 2007. \doi{10.1142/9789812707499_0032}.
\newblock The locators used here refer to the arXiv version.
\newblock URL \url{https://arxiv.org/pdf/math/0509451v1}.''')]
records=[]
for short,key,doi,old,new in items:
 p=Path('/workspace/scratch/9fcd229a9ed4/tmp')/(short+'_doi_metadata.json')
 raw=p.read_bytes();m=json.loads(raw)['message'];assert m['DOI'].lower()==doi.lower()
 if short=='GCP2026':
  assert (m['volume'],m['issue'],m['article-number'],m['published']['date-parts'][0])==('114','3','e70699',[2026,9])
  summary='The publisher DOI registration identifies Journal of the London Mathematical Society114(3), article e70699, September2026, with Giménez Conejero and Pintér as authors.'
 else:
  assert m['page']=='745-760' and m['published']['date-parts'][0][0]==2007
  summary='The publisher DOI registration identifies the Michel–Pichon–Weber chapter in Singularity Theory, World Scientific2007, pages745–760. Pichon’s primary publication list confirms the authors, proceedings and year.'
 apply_edit(old,new,'II-C3-BIB-PUBLICATION-'+short,['D18'],key,'Bibliography',
  'Add the publisher-registered publication metadata. Keep the exact cited preprint version and state that its locators are used; no equivalence of preprint and published theorem numbering or proofs is claimed.',
  'Root read the complete old/new entry, corresponding arXiv metadata and publisher-supplied DOI registration fields. Pichon’s author publication entry was also opened for MPW. Published mathematical proofs were not newly read.')
 records.append(dict(source='II-C3-BIB-PUBLICATION-'+short,url='https://api.crossref.org/works/'+doi,
  version='Publisher-deposited DOI registration read22November2026',locus='Title, authors, container, publisher, publication date and page/article fields',
  date_utc=now(),sha256=hashlib.sha256(raw).hexdigest(),own_word_summary=summary,
  use='Bibliographic metadata only. The cited preprint mathematics and versioned page locators remain unchanged; no fresh published-proof reading or literature-exhaustiveness claim.'))
append_rows(ROOT/'S6_SERIES_PUBLISH_c3_primary_readings.tsv',records,'source')
add_event('GCP2024;MPW2005Hirzebruch','II-C3-BIB-PUBLICATIONS-TWO','used and rechecked in this run',
 'The two publisher-deposited DOI records were opened and their complete relevant bibliographic fields read. GCP has a2026 journal publication; MPW has the2007 proceedings publication. Both entries now include those data and preserve their exact cited preprint editions and locators. Pichon’s own publication list independently confirms the MPW proceedings identity. This is metadata verification, not a new mathematical proof reading, an equivalence of versioned loci, or a complete literature-status gate.',
 'Two bibliography entries and primary DOI-registration fields',source=__file__)
print('Two publisher publication records integrated; exact preprint loci unchanged.')
