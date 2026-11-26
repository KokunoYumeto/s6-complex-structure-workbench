from S6_SERIES_PUBLISH_c3_edit import *
import json

folder=ROOT/'agents/continuation3_foundations/sec07'
prefix='S6_SERIES_PUBLISH_sec07_cusp_'
s=SOURCE.read_text();after=s
for guard in json.loads((folder/(prefix+'guards.json')).read_text()):
    assert after.count(guard['old'])==1,guard['key']
    after=after.replace(guard['old'],guard['new'],1)
    print('Applied',guard['key'])
preserve_identifiers(s,after)
for old,new in zip(identifiers(s),identifiers(after)):
    for name,count in old.items():assert new[name]==count,name
SOURCE.write_text(after,newline='\n')
for suffix,target,key in [('defects.tsv','S6_SERIES_PUBLISH_defects_II.tsv','change_id'),('CHECK_EVENTS.tsv','CHECK_EVENTS.tsv','event_id')]:
    _,rows=read_tsv(folder/(prefix+suffix))
    print(suffix,append_rows(ROOT/target,rows,key))
add_event('lem:II:boundary-deformation-transport; night:P4.28; cdp:st:C.2.CR.4',
 'II-C3-ROOT-CUSP-OWNER-ADMISSION','used and rechecked in this run',
 'Root read the complete receiving P295 and cusp theorem/proof and the full consumer/scope comparison against the prior complete cusp proof. Checked local irreducibility, exact xi∘F=g^m, the product-chart boundary correction V−dρ(V)W/dρ(W), target/parameter transports and nested inclusions, DVR quadratic diagonalization, both distinct perturbation families and their exact relation through Phi_delta, weighted unit-coordinate maps, both spherical squares, and the explicit cusp normalization/inverse. Both original theorem identities and C.CR.15–18 survive once. The four agent complete old/new readings are imported as exposed checks. The unequal-multiplicity consumers R14/R15/P441/P445 retain their original domains and their explicit open D25 premise; this admission does not close them. No independent or final PDF credit.',
 'S6_SERIES_PUBLISH_II.tex: local cusp and boundary transport',source='code/S6_SERIES_PUBLISH_c3_cusp_owner_admit.py')
set_unit_status('night:P4.28','D12','done',
 'Complete original and receiving cusp proofs compared after the exact two-family transfer. The second cusp statement is now its preserved alias; no duplicated proof remains. Full-fibre multiplicity premises of other consumer units remain explicitly open.',
 'CHECK_EVENTS.tsv: II-C3-ROOT-CUSP-OWNER-ADMISSION')
print('Admitted common cusp owner and boundary transport; unequal-power consumer premise remains open.')
