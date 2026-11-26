from S6_SERIES_PUBLISH_c3_edit import *
folder=ROOT/'agents/continuation3_provenance/normalization_owner'
before=SOURCE.read_text();after=before
owner=(folder/'S6_SERIES_PUBLISH_normalization_owner_proposed.tex').read_text()
anchor=r'\begin{proposition}[The canonical normal-crossings formula]\hypertarget{tag-01AE}{}\label{cdp:st:A.1.2}'
assert after.count(anchor)==1 and r'\label{cdp:st:A.2.3}' not in after
after=after.replace(anchor,owner+'\n'+anchor,1)
_,defects=read_tsv(folder/'S6_SERIES_PUBLISH_normalization_owner_defects.tsv')
change=defects[1];assert after.count(change['old_text'])==1
after=after.replace(change['old_text'],change['new_text'],1)
_,bibs=read_tsv(folder/'S6_SERIES_PUBLISH_bibliography_146_edits.tsv')
_,more=read_tsv(ROOT/'agents/continuation3_provenance/S6_SERIES_PUBLISH_c3_provenance_bibliography_next_edits.tsv')
for row in more+bibs:
 assert after.count(row['old_text'])==1,row['change_id']
 after=after.replace(row['old_text'],row['new_text'],1)
 print('Applied',row['change_id'])
preserve_identifiers(before,after)
for old,new in zip(identifiers(before),identifiers(after)):
 for name,count in old.items():assert new[name]==count,name
SOURCE.write_text(after,newline='\n')
print('Defects',append_rows(ROOT/'S6_SERIES_PUBLISH_defects_II.tsv',defects+more+bibs,'change_id'))
_,events=read_tsv(folder/'S6_SERIES_PUBLISH_normalization_owner_CHECK_EVENTS.tsv')
print('Events',append_rows(ROOT/'CHECK_EVENTS.tsv',events,'event_id'))
add_event('cdp:st:A.2.3; lem:II:persistent-normalization-pullback','II-C3-ROOT-NORMALIZATION-RESTORE','used and rechecked in this run',
 'The working build exposed a missing owner, not a renamed label: A.2.3 existed in the supplied compendium and stale reference dictionary but not the current standalone text. The agent read its complete original statement and application against GS2014v7. Root read the complete receiving cited owner, its exact multiplier/tensor/projection maps, and all nine steps of the current receiving P263 proof. The complete original P263 statement is unchanged. Restored legacy tag01AH, repaired its application, and pinned GS2014v7. Also admitted primary version locators142–145 after reading the proposed bibliography entries and source-reading limits. No new required-check or independent-proof credit; integrated build and final pages remain open.',
 'S6_SERIES_PUBLISH_II.tex: conormal criterion and persistent-normalization lemma',source='code/S6_SERIES_PUBLISH_c3_normalization_restore.py')
print('Restored cited normalization owner and exact bibliography editions.')
