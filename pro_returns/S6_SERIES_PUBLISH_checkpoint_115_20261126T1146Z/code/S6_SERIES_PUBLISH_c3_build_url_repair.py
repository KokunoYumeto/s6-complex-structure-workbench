from S6_SERIES_PUBLISH_c3_edit import *

apply_edit(r'\newcommand{\SsixPublishRecords}{https://github.com/KokunoYumeto/s6-complex-structure-workbench/blob/main/RECORDS.md#paper-ii}',
           r'\newcommand{\SsixPublishRecords}{https://github.com/KokunoYumeto/s6-complex-structure-workbench/blob/main/RECORDS.md\#paper-ii}',
           'II-C3-RECORDS-URL-TEX',['D23'],'sec:II:methodology','Preamble line31',
           'pdfLaTeX found an illegal parameter token in the macro definition. Escape the URL fragment delimiter in TeX; hyperref decodes it to the same required records-page URI.')
add_event('II:standalone-build','II-C3-BUILD-RECORDS-URL-REPAIR','used and rechecked in this run',
          'The integrated working build stopped at the unescaped hash in SsixPublishRecords. Repaired its TeX tokenization without changing the required URL. A fresh complete pdfLaTeX build and the decoded PDF link comparison follow; no clean-build or final-page gate is closed by this repair.',
          'S6_SERIES_PUBLISH_II.tex: preamble',source='code/S6_SERIES_PUBLISH_c3_build_url_repair.py')
print('Records URL TeX token repaired.')
