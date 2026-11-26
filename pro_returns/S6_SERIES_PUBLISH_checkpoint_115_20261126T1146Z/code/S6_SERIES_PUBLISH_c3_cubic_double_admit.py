"""Admit the complete cubic-double-line unit and its exact conductor criterion."""
from S6_SERIES_PUBLISH_c3_edit import *
import json

folder=ROOT/'agents/continuation3_foundations/sec07'
prefix='S6_SERIES_PUBLISH_sec07_cubic_double_'
guards=json.loads((folder/(prefix+'guards.json')).read_text())
assert len(guards)==3
before=SOURCE.read_text();after=before
for row in guards:
 assert after.count(row['old'])==1,row['key']
 after=after.replace(row['old'],row['new'],1)
 print('Applied',row['key'])
preserve_identifiers(before,after)
for old,new in zip(identifiers(before),identifiers(after)):
 for name,count in old.items():assert new[name]==count,name
 for name,count in (new-old).items():assert new[name]==1,name
SOURCE.write_text(after,newline='\n')
for suffix,target,key in [('defects.tsv','S6_SERIES_PUBLISH_defects_II.tsv','change_id'),('CHECK_EVENTS.tsv','CHECK_EVENTS.tsv','event_id')]:
 _,rows=read_tsv(folder/(prefix+suffix));print(suffix,append_rows(ROOT/target,rows,key))
_,statuses=read_tsv(folder/(prefix+'unit_progress.tsv'))
for row in statuses:
 kind='structure' if row['row']=='restructuring' else row['row']
 if kind in ['D10','D16']:continue
 set_unit_status('night:P4.53',kind,row['status'],row['basis'],row['fragment'])
add_event('lem:II:conductor-duality;lem:II:proper-conductor-divisor;night:P4.53',
 'II-C3-ROOT-CUBIC-DOUBLE-UNIT-ADMISSION','used and rechecked in this run',
 'Root read the complete original and receiving P222 and P453, the entire P300 before its single-paragraph application change, and the complete comparison. The finite normalization criterion uses c outside q, q intersect R=m_R, c a unit in R and cB contained in R, giving B=R on all branches. P300/P453 apply it to their exact local rings. The same compact strict transform and canonical generator give2=n+a. All cubic degree, valuation and residue maps, discriminant partitions, weighted-vertex calculations and Euler bounds remain. The weighted transport now precedes its application and uses the exact reduced g, full Phi=u g^m, root g_u=h and identity local-level inclusion. P322 receives the identical weights(1,2,1),degree5,free action and compact-core inclusions; rank lower8 and upper3 retain gap5. A53 gives positivity on the whole exceptional block, yielding the original simple elliptic conclusion. Every old identifier is retained; no independent or final-page credit.',
 'Complete P453 and P222, bounded exact P300 application',source=__file__)
append_rows(ROOT/'S6_SERIES_PUBLISH_c3_primary_readings.tsv',[dict(
 source='Reid 1994 (third-continuation cubic conductor application)',
 url='https://ems.press/content/serial-article-files/40537',
 version='Publications RIMS30(5)(1994),695–727; DOI10.2977/prims/1195165581; publisher PDF',
 locus='Complete Proposition2.3/proof2.4, printedp703, and Theorem2.6/proof2.7, pp704–705; foundations reviewer read text and page images, including diagrams',
 date_utc=now(),sha256='8786c3c9560d262a174a2a3be343507f59240b62935df08dc6a60993f8b254d7',
 own_word_summary='Finite normalization duality identifies the canonical sheaf with the conductor twist and gives the normalization quotient and conductor dualizing comparisons. The proof supplies the module maps used by the local Gorenstein calculation.',
 use='P222 retains the exact multiplication and Ext maps, then proves the local semilocal unit-conductor criterion. P300 and P453 apply that criterion to the same normalization germs and all their local branches.')],'source')
print('Complete cubic double-line unit admitted; original stable unit id night:P4.53 retained.')
