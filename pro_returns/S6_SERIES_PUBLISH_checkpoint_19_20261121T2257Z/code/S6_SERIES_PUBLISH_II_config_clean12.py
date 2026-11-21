from pathlib import Path
import hashlib,json
R=Path(__file__).resolve().parents[1]
def b(p):return dict(path=p,sha256=hashlib.sha256((R/p).read_bytes()).hexdigest())
c=dict(batch_id='CLEAN12',record_directory='records/S6_SERIES_PUBLISH_II_clean_checks_12',
 event_bundle='records/S6_SERIES_PUBLISH_zzz_continuation_017_clean_CHECK_EVENTS.tsv',
 prior_admission=b('records/S6_SERIES_PUBLISH_II_clean_checks_11/manifest.json'),
 proposal=b('records/S6_SERIES_PUBLISH_II_GW_reviewed_proposals.json'),
 event_proposal=b('agents/ii_checks_provenance/recovery_20261121T2000Z/clean_group07/S6_SERIES_PUBLISH_II_clean_group07_event_proposals.json'),
 root_review=b('records/S6_SERIES_PUBLISH_II_GW_editorial_guard.json'),
 source_applications=[b('records/S6_SERIES_PUBLISH_II_GW_editorial_apply.json')],
 before_ledger_sha256='bd1a353a50903286ebe5d2bf6573e6ad48ad918c71b5250b11bd7fd10138f988',
 source_sha256='733c17e5a967547ea6866752a0337e4db77dc6037487c251d50332684fbf296e',
 independent_checks=1,events=2,
 who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; reasoning effort inherited, no separate numerical setting exposed; i_provenance and root',
 event_scope_suffix='All thirteen exact source edits are now applied. Root read the complete pair, frozen derivation, full comparison, all owner and bibliography guards, fresh determinant code and output, primary locator reading and official version receipts. Source-image readings are credited to the checker. No extra computation event or Paper II page-image reading is claimed.',
 scope='One independent prerelease Kodaira–Spencer rank check, with the actual full comparative rereading recorded separately. The lattice quotient, Cech sign, per-family exponential coordinates and residue determinant calculation are explicit. The frame-name D25 error is repaired without changing the statement or rank. Three bibliography entries are pinned to the verified official source versions.',
 proof_repairs=[dict(statement_owner='cdp:st:E7',tag='01GW',defect_type='D25',
 original_error='The extension frame e_i=alpha_i+ell(q) beta_i, f_i=beta_i was called flat, whereas nabla(e_i)=f_i dq/(2 pi i q) and nabla(f_i)=0.',
 corrected_step='Call alpha,beta the flat frame and e,f the single-valued holomorphic extension frame. The triangular change T=[[I,ell I],[0,I]] has inverse [[I,-ell I],[0,I]]; Hodge rows (I,H_s) in e,f become (I,ell I+H_s) in alpha,beta.',
 statement_changed=False,rank_and_determinant_values_unchanged=True,
 evidence=b('agents/ii_checks_provenance/recovery_20261121T2000Z/clean_group07/S6_SERIES_PUBLISH_II_clean_group07_final_proposals.json'))])
p=R/'records/S6_SERIES_PUBLISH_II_clean_checks_12_config.json';assert not p.exists();p.write_text(json.dumps(c,indent=2)+'\n')
print(json.dumps(b(str(p.relative_to(R)))))
