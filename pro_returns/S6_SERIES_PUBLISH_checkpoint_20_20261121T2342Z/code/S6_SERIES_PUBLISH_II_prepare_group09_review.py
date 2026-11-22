"""Bind group09's actually read pairs and the exact current Paper I cusp inputs."""
from pathlib import Path
import copy,datetime,hashlib,json
R=Path(__file__).resolve().parents[1]
def sha(x):return hashlib.sha256(x.encode() if isinstance(x,str) else x).hexdigest()
def bound(p):return dict(path=p,sha256=sha((R/p).read_bytes()))
def read(p):return json.loads((R/p).read_text())
def write(p,d):
    p=R/p;assert not p.exists();p.write_text(json.dumps(d,indent=2)+'\n')
base='agents/ii_checks_provenance/recovery_20261121T2000Z/clean_group09/'
original=base+'S6_SERIES_PUBLISH_II_clean_group09_final_proposals.json'
events_original=base+'S6_SERIES_PUBLISH_II_clean_group09_event_proposals.json'
assert bound(original)['sha256']=='6eba5ca8ead8a27847dcf458122b6880d8066d39ed3f8e5fafe39ba26a71e81b'
assert bound(events_original)['sha256']=='139b1df5023e57ab9b9b86c7ee0bbb958a3fe867a0f7b445abfd8115af131c35'
assert bound('S6_SERIES_PUBLISH_II.tex')['sha256']=='24b538e301c58b8b6b078437e3e92ef3480c40019a49a47a509567f494b02dfa'
d=read(original)
ds=next(t for t in d['targets'] if t['tag']=='03DS')
old=r'''The cusp result in \CompendiumRef{I}{wb:thm:candidate-cusp-geometry} supplies the full compact
reduced normal-crossings fibre, its $\mathrm{dP}_6$ normalization, and the
trivialization of $\omega_X$ near $W$.  By'''
new=r'''The full cusp fibre $W=f^{-1}(p_0)$ is reduced by
\CompendiumRef{I}{def:common-conventions}.
At $k=l=1$, the cusp charts in the proof of
\CompendiumRef{I}{push:src:E.3.1} are $q=z_0z_1z_2$,
with the two-factor and smooth charts on the other strata,
and the normalization is $\eta:\mathrm{dP}_6\to W$.
The canonical-bundle isomorphism
$\omega_X\simeq\mathcal O_X(-2S_2)$ in
\CompendiumRef{I}{fam:src:A.1.1} gives a trivialization on
$X\setminus S_2$, which contains $W$: the two supports
are fibres over the distinct points $p_0$ and $p_2$. By'''
ds_agent=(R/ds['proposed_full_block']['path']).read_text()
assert ds_agent.count(old)==1
ds_new=ds_agent.replace(old,new,1)
ds_path='records/S6_SERIES_PUBLISH_II_03DS_root_proposed.tex'
assert not (R/ds_path).exists();(R/ds_path).write_text(ds_new)
I=(R/'S6_SERIES_PUBLISH_I.tex').read_text()
assert sha(I)=='179fcc4e85fb7902aaf978bcd809cf9928ebc0a46cda5628d5096e6fa0011d74'
fragments=[]
for label,a,z in [('def:common-conventions',6183,6222),('fam:src:A.1.1',8142,8184),('push:src:E.3.1',10824,10846)]:
    lines=I.splitlines(keepends=True);frag=''.join(lines[a-1:z]);start=sum(map(len,lines[:a-1]))
    fragments.append(dict(label=label,start_line=a,end_line=z,start_offset=start,end_offset=start+len(frag),sha256=sha(frag),text=frag))
input_path='records/S6_SERIES_PUBLISH_II_03DS_current_I_input_transport.json'
write(input_path,dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),source=bound('S6_SERIES_PUBLISH_I.tex'),fragments=fragments,
    transport='Set k=l=1 in the marked family. The cusp atlas has base equation q=z0*z1*z2, with two-factor and smooth strata; its fibre is reduced normal crossing and its normalization is dP6. The definition identifies p0=infinity and p2=1. Restrict the proved isomorphism omega_X=O_X(-2S2) to X minus S2; its canonical divisor section gives a trivialization there, including W. The same normalization map is named eta in II and nu in I.',
    original_citation='wb:thm:candidate-cusp-geometry',current_label_search='Exact label and hypertarget searches in all five current canonical sources found no owning label for this historical identifier. This is an exact-identifier observation, not a global missing-reference audit.',
    original_pair=ds['original_full_block'],agent_proposed_pair=ds['proposed_full_block'],root_proposed_pair=bound(ds_path),
    independent_check_credit_added=0))
expanded=[]
for t in d['targets']:
    cur=(R/t['original_full_block']['path']).read_text();out=[]
    for g in t['guards']:
        count=g['expected_occurrences_in_owning_block'];assert cur.count(g['old'])==count
        for j in range(count):
            pos=cur.index(g['old']);a,z=pos,pos+len(g['old'])
            while cur.count(cur[a:z])!=1:
                previous=a,z;a,z=max(0,a-80),min(len(cur),z+80);assert previous!=(a,z)
            h=copy.deepcopy(g);h['old']=cur[a:z];h['new']=cur[a:pos]+g['new']+cur[pos+len(g['old']):z]
            h['expected_occurrences_in_owning_block']=1
            if count>1:
                h['change_id']+=f'-occurrence-{j+1}'
                h['logical_literal_before']=g['old'];h['logical_literal_after']=g['new'];expanded.append(dict(tag=t['tag'],guard=h))
            assert cur.count(h['old'])==1
            cur=cur.replace(h['old'],h['new'],1);out.append(h)
    assert cur==(R/t['proposed_full_block']['path']).read_text()
    t['guards']=out
    if t['tag']=='03DS':
        t['agent_proposed_full_block']=t['proposed_full_block'];t['proposed_full_block']=bound(ds_path)
        t['guards'].append(dict(change_id='II-ROOT-C09-03DS-current-I-locator',defect_type='D18',old=old,new=new,expected_occurrences_in_owning_block=1,
            reason='Replace the historical identifier with the exact current owning inputs and the explicit restriction of the canonical-bundle isomorphism to X minus S2.'))
        t['comparison']+=' Root follow-up replaces the historical locator with the exact current Paper I definition, cusp-chart construction and canonical-bundle proposition; the restriction and normalization maps are explicitly transported in the bound addendum.'
        t['root_input_transport']=bound(input_path)
for g in d['bibliography_guards']:g['statement_owner']='bib:'+g['key']
assert sum(len(t['guards']) for t in d['targets'])+len(d['bibliography_guards'])==70
d['original_agent_proposal']=bound(original)
d['root_input_transport']=bound(input_path)
d['root_review_status']='Prepared for actual complete final DS pair rereading; other eight complete pairs and all five bibliography pairs were already read.'
proposal='records/S6_SERIES_PUBLISH_II_group09_reviewed_proposals.json';write(proposal,d)
ev=read(events_original)
for x in ev['events']:
    if x['tag']=='03DS':
        x['agent_proposed_full_block']=x['proposed_full_block'];x['proposed_full_block']=bound(ds_path)
        x['scope']=x['scope'].replace('Its historical Compendium I cusp locator is retained as the supplied cited input; no nonexistent current owning label is substituted.','The historical locator is replaced by the exact current Paper I definition, cusp-chart construction and canonical-bundle proposition, with the normalization and open-restriction maps stated explicitly.')
    if x['tag']=='03J0' and x['event_type']=='targeted proof check':
        x['scope']=x['scope'].replace('so its statement is clarified','so its statement domain is corrected to include smoothness')
ev['original_agent_event_proposal']=bound(events_original)
ev['root_proposal']=bound(proposal)
ep='records/S6_SERIES_PUBLISH_II_group09_reviewed_event_proposals.json';write(ep,ev)
print(json.dumps(dict(proposal=bound(proposal),events=bound(ep),root_DS=bound(ds_path),transport=bound(input_path),expanded_duplicate_guards=expanded),indent=2))
