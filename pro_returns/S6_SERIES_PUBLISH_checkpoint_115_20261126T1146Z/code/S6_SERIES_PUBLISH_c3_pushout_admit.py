from S6_SERIES_PUBLISH_c3_edit import *
import json
folder=ROOT/'agents/continuation3_foundations/sec07'
s=SOURCE.read_text();after=s
for g in json.loads((folder/'S6_SERIES_PUBLISH_sec07_pushout_guards.json').read_text()):
 assert after.count(g['old'])==1,g['key']
 after=after.replace(g['old'],g['new'],1);print('Applied',g['key'])
preserve_identifiers(s,after)
for old,new in zip(identifiers(s),identifiers(after)):
 for name,count in old.items():assert new[name]==count,name
SOURCE.write_text(after,newline='\n')
for suffix,target,key in [('defects.tsv','S6_SERIES_PUBLISH_defects_II.tsv','change_id'),('CHECK_EVENTS.tsv','CHECK_EVENTS.tsv','event_id')]:
 _,rows=read_tsv(folder/('S6_SERIES_PUBLISH_sec07_pushout_'+suffix));print(suffix,append_rows(ROOT/target,rows,key))
add_event('lem:II:proper-conductor-pushout; prop:II:minimal-boundary-complements; night:P4R.3; night:P4R.7','II-C3-ROOT-PUSHOUT-ADMISSION','used and rechecked in this run',
 'Root read the complete receiving P294, all seven guard applications and the complete source-map comparison. Hatcher exact opened loci supply the CW-cofibration, canonical homotopy-pushout collapse, Mayer–Vietoris and connected van Kampen theorem. The explicit compact proper quotient, prescribed h/inclusion maps, inverse k_*j_*^-1, and disconnected conjugacy presentation remain; no injective-edge-map hypothesis is added. The foundations complete original/receiving P210,R3,R7 readings are imported as exposed events. All old identifiers retain their multiplicity. Final whole-paper placement and page reading remain open.',
 'S6_SERIES_PUBLISH_II.tex: common proper conductor pushout and ruling applications',source='code/S6_SERIES_PUBLISH_c3_pushout_admit.py')
# Exact editions needed by the next vector-field unit.
file=ROOT/'agents/continuation3_provenance/S6_SERIES_PUBLISH_c3_provenance_bibliography_guillot_edits.tsv'
_,rows=read_tsv(file)
for row in rows:
 current=SOURCE.read_text();assert current.count(row['old_text'])==1,row['change_id']
 SOURCE.write_text(current.replace(row['old_text'],row['new_text'],1),newline='\n')
print('Guillot bibliography',append_rows(ROOT/'S6_SERIES_PUBLISH_defects_II.tsv',rows,'change_id'))
add_event('bib:Guillot2019; bib:Guillot2024','II-C3-GUILLOT-EDITIONS-ADMISSION','used and rechecked in this run',
 'Read both exact old/new bibliography entries and admitted the exposed primary metadata comparison. Guillot2019 is pinned to arXiv1603.02288v2,5August2019. The2024chapter retains its publisher DOI withpp1–37/editors and explicitly separates the32-page author preprint pagination used in the body; no inferred edition date is printed. Full mathematical-locus readings belong to the conductor events. No global bibliography gate closes.',
 'S6_SERIES_PUBLISH_II.tex: bibliography',source=str(file.relative_to(ROOT)))
print('Admitted proper-pushout owner and exact Guillot editions.')
