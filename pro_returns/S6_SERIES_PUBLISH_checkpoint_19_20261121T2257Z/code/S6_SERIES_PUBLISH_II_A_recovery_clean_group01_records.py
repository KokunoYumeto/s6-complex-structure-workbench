"""Finalize already-read recovery check records; no canonical source/ledger writes."""
from pathlib import Path
import hashlib,json,datetime,re
ROOT=Path(__file__).resolve().parents[1]
REC=ROOT/'agents/ii_checks_A/recovery_20261121T195642Z'
OUT=REC/'clean_group01'
sha=lambda b:hashlib.sha256(b).hexdigest()
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
manifest_path=OUT/'S6_SERIES_PUBLISH_II_A_recovery_clean_group01_editorial_proposals.json'
m=json.loads(manifest_path.read_text())
comp=REC/'S6_SERIES_PUBLISH_II_A_recovery_clean_group01_comparisons.md'
s=comp.read_text().replace('|a1+a2|²+|a1−a2|²=2(|a1|²+|a2|²)','norm(a1+a2)²+norm(a1−a2)²=2(norm(a1)²+norm(a2)²)').replace('|a1|²+|a2|²+2|a3|²','norm(a1)²+norm(a2)²+2 norm(a3)²')
s+='\nFinal complete proposed blocks, including the numbered equation environments, were reread in full before this record at '+now+'. The final paired-read hashes are in the companion rereading JSON.\n'
comp.write_text(s)
validation=[]
for b in m['blocks']:
    tag=b['tag']
    before=(ROOT/b['original_path']).read_text()
    after=(ROOT/b['proposed_path']).read_text()
    cur=before
    gs=[g for g in m['guards'] if g['tag']==tag]
    for g in gs:
        assert sha(cur.encode())==g['intermediate_before_sha256']
        assert cur.count(g['literal_old'])==1
        at=g['offset_before']
        assert cur[at:at+len(g['literal_old'])]==g['literal_old']
        cur=cur[:at]+g['literal_new']+cur[at+len(g['literal_old']):]
        assert sha(cur.encode())==g['intermediate_after_sha256']
    assert cur==after
    for g in reversed(gs):
        at=g['offset_before']
        assert cur[at:at+len(g['literal_new'])]==g['literal_new']
        cur=cur[:at]+g['literal_old']+cur[at+len(g['literal_new']):]
    assert cur==before
    anchors=lambda x:re.findall(r'\\(?:label|hypertarget)\{([^}]*)\}',x)
    assert anchors(before)==anchors(after)
    validation.append({'tag':tag,'forward_exact':True,'inverse_exact':True,'ordered_anchors_equal':True,
       'original_sha256':sha(before.encode()),'proposed_sha256':sha(after.encode()),'guard_count':len(gs)})
details={
'01AZ':'Read the complete original and final proposed blocks. Followed b tensor [F] to b dF, tensor A and projection formula, the full reduced fibre frame [t composed with f], and the exact kernel of V tensor A to Q tensor A. Opened the CDP journal subcase on pp.693–694. The added explicit ambient group is precisely H0(S,V tensor A); no normal-crossing hypothesis is introduced.',
'01B4':'Read the complete original six-item proof and the final six-item proposed proof. Compared the frozen Hom(I_D,omega_S) method to the complete Ext conductor map preserving A.J.31. Checked the same canonical evaluation and full-fibre torsion argument, both e=0/1 genus cases, branch-count inequality, explicit node/cusp ring isomorphisms and ambient regular sequence. All three equation anchors are kept inside numbered environments.',
'01FJ':'Read the complete original seven-item proof, all of pinned C_jets.py, and the complete final seven-item proposed proof. Checked dual-bundle transport M=Q_old*, Q_new=R_old*, Delta_new=4 Delta_old, the parameter-preserving normal forms, every degree and cover, and all three fractional modules. The triple program branches map by permutation (1 2). After correcting the new proposal’s preliminary pole-bound scope, reread the entire final block. All three equation anchors are retained in numbered environments.',
'01BB':'Read all four original items and all five final proposed items. Checked pi=mu sigma, p=p_prime sigma, C to C_prime to C_T, the minimal-resolution conductor supplied by A.5.3, the section-square formula and negative exceptional form, the explicit analytic local-function transport of Mumford p.6, and the final normalization homeomorphism/Euler map. The original pi remains arbitrary and original V receives no added effectiveness assumption.'
}
rereads={'recorded_utc':now,'basis':'Actual complete outputs read by the checker, followed by mathematical comparison; not inferred from word scans or the validator.',
 'records':[dict(v,complete_original_and_proposed_read=True,comparison=details[v['tag']],comparison_path=str(comp.relative_to(ROOT)),comparison_sha256=sha(comp.read_bytes())) for v in validation]}
reread_path=OUT/'S6_SERIES_PUBLISH_II_A_recovery_clean_group01_rereads.json'
reread_path.write_text(json.dumps(rereads,indent=2)+'\n')
val_path=OUT/'S6_SERIES_PUBLISH_II_A_recovery_clean_group01_guard_validation.json'
val_path.write_text(json.dumps({'recorded_utc':now,'scope':'in-memory literal forward/inverse transport of the four immutable original blocks','records':validation},indent=2)+'\n')

owners={'01AZ':'cdp:st:A.5.1','01B4':'cdp:st:A.5.14','01FJ':'cdp:st:C2d','01BB':'cdp:st:A.5.20'}
freezes=json.loads((REC/'S6_SERIES_PUBLISH_II_A_recovery_clean_group01_freezes.json').read_text())
releases=json.loads((REC/'S6_SERIES_PUBLISH_II_A_recovery_clean_group01_releases.json').read_text())
targeted={
'01AZ':'Before opening the proof, derived the canonical normalization/conormal injection, the base-coordinate trivialization on the full reduced fibre, nonvanishing on each compact normalization component, and compatibility through the exact quotient kernel. Froze at 20:16:19 UTC, released, and compared the entire printed proof and published receiving subcase. All conclusions agree through the same sheaf maps.',
'01B4':'Before opening the proof, proved the genus bound through Hom(I_D,omega_S) and the conductor determinant trick, then classified delta-one curve rings and proved their lci embeddings in the given threefold. Froze at 20:16:19 UTC. The complete six-step printed proof was compared; its additional labelled conductor-duality equality was proved by the exact sheaf Ext map and retained. All original genus and constant-type conclusions follow.',
'01FJ':'Before opening the proof or C_jets.py, derived all three jet tensor laws, genus inequalities, constant normal forms, covering and normal-degree maps, and entire inverse-Jacobian modules. A fresh exact program was run and bound before the 20:16:19 UTC freeze. After release, all seven printed steps and the entire old program were compared through the explicit dual-bundle, factor-four and branch-permutation maps. Postrelease transport computations add no prereading credit.',
'01BB':'Before opening the proof, derived the finite degree-one cusp-curve map, the descent pi=mu sigma and p=p_prime sigma, the effective conductor on the minimal resolution, ruling contraction, analytic exceptional negative definiteness, and Euler equality. The exact A.5.3 input and new cell/matrix program were bound before the 20:19:04 UTC freeze. After release all four printed steps were compared and expanded through these same maps, preserving the arbitrary initial resolution.'
}
events=[]
def event(tag,kind,outcome,suffix,extra=''):
    b=next(b for b in m['blocks'] if b['tag']==tag)
    fr=next(x for x in freezes if x['owner']==owners[tag])
    rel=next(x for x in releases if '/'+tag+'/' in x['receipt'])
    events.append({'statement_id':owners[tag],'date':'2026-11-21',
      'who':'GPT-6 Astra Pro (OpenAI), inherited effort, S6_SERIES_PUBLISH checker ii_check_a_recovery_blind',
      'phase':'publish-II','source_file':b['proposed_path'],'evidence_group':'II-A-recovery-clean01-'+tag,
      'date_utc':now,'where':str(comp.relative_to(ROOT))+'; '+fr['receipt']+'; '+rel['receipt']+'; '+str(reread_path.relative_to(ROOT))+extra,
      'type':kind,'outcome':outcome,'event_id':f'S6_SERIES_PUBLISH_II_A_recovery_clean01_{tag}_{suffix}_20261121'})
for tag in ['01AZ','01B4','01FJ','01BB']:
    event(tag,'targeted proof check',targeted[tag],'targeted')
    event(tag,'used and rechecked in this run',details[tag],'wording')
event('01FJ','computation or formal certificate',
'Prefreeze exact interpolation on the square-completion and tensor-weight identities, the GL2 wedge formula, and explicit conductor coefficient/preimage maps was compared to the same pinned old C_jets.py inputs. The old routine uses symbolic expansion, discriminant and linsolve plus a finite cusp scan. The postrelease coefficient-to-factor interpolation and Hermitian norm certificates verify the identical old discriminant and constraint kernels by different methods. Old and new postrelease runs exited zero at 20:23:58 UTC; exact timings/hashes and the prefreeze bindings are recorded. No extra blind event is claimed.',
'computation','; '+str((REC/'S6_SERIES_PUBLISH_II_A_recovery_clean_group01_program_runs.json').relative_to(ROOT)))
event('01BB','computation or formal certificate',
'The new prefreeze cell program computes the sphere and elliptic Euler factors by tensor cell counts and checks the weighted intersection identity by exact coefficient dictionaries. The full derivation proves the matrix formula for arbitrary size and applies it to the local holomorphic divisor, while the product cell count is used only for Euler characteristic of the ruled bundle. The run at 20:19:04 UTC and its exact source/output hashes are bound before BB freeze.',
'computation','; '+str((REC/'S6_SERIES_PUBLISH_II_A_recovery_blind_01BB_run.json').relative_to(ROOT)))
ep=OUT/'S6_SERIES_PUBLISH_II_A_recovery_clean_group01_event_proposals.json'
ep.write_text(json.dumps({'created_utc':now,'canonical_events_added':0,'root_review_required':True,'events':events},indent=2)+'\n')
index={'created_utc':now,'owners':list(owners),'guard_count':len(m['guards']),'event_proposal_count':len(events),'canonical_writes':False,
 'files':[{'path':str(p.relative_to(ROOT)),'sha256':sha(p.read_bytes())} for p in [manifest_path,comp,reread_path,val_path,ep,
 REC/'S6_SERIES_PUBLISH_II_A_recovery_clean_group01_freezes.json',
 REC/'S6_SERIES_PUBLISH_II_A_recovery_clean_group01_releases.json',
 REC/'S6_SERIES_PUBLISH_II_A_recovery_clean_group01_program_runs.json']]}
ip=REC/'S6_SERIES_PUBLISH_II_A_recovery_clean_group01_final_index.json'
ip.write_text(json.dumps(index,indent=2)+'\n')
print(json.dumps({'index':str(ip.relative_to(ROOT)),'sha256':sha(ip.read_bytes()),'files':index['files'],'guard_count':len(m['guards']),'event_proposals':len(events)},indent=2))

