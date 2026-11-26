"""Admit the two source-verified plain program paths in the final appendix."""
from S6_SERIES_PUBLISH_c3_edit import *

folder=ROOT/'agents/continuation3_provenance'
_,rows=read_tsv(folder/'S6_SERIES_PUBLISH_c3_provenance_program_edits154.tsv')
before=SOURCE.read_text();after=before
for row in rows:
    assert after.count(row['old_text'])==1,row['change_id']
    after=after.replace(row['old_text'],row['new_text'],1)
preserve_identifiers(before,after)
SOURCE.write_text(after,newline='\n')
print('Program appendix defects',append_rows(ROOT/'S6_SERIES_PUBLISH_defects_II.tsv',rows,'change_id'))
add_event('cdp:st:C.2.UN.29; cdp:st:C.2.UN.36','II-C3-ROOT-PROGRAMS154-ADMISSION',
 'used and rechecked in this run',
 'Root read the complete guarded two-row appendix insertion, source/path/hash records and preparation script. The provenance agent retrieved and read both complete pinned program sources and matched their prescribed repository paths. The return-germ row names finite coefficient extractions and integration identities; the exterior-square row names rational fixed spaces, Gram matrices and signatures, with no integral-saturation claim. No program execution is claimed. The corresponding body moves remain with the conductor package. Full records-table regeneration stays deferred until text-final.',
 'S6_SERIES_PUBLISH_II.tex: Programs table; agents/continuation3_provenance/S6_SERIES_PUBLISH_c3_provenance_program_checks154.tsv',
 source='code/S6_SERIES_PUBLISH_c3_programs154_admit.py')
print('Two plain paths admitted; no derived-table refresh or computation credit.')
