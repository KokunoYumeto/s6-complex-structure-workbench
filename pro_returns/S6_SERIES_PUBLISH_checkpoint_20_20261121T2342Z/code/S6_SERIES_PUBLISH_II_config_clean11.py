from pathlib import Path
import hashlib,json
R=Path(__file__).resolve().parents[1]
def b(p):return dict(path=p,sha256=hashlib.sha256((R/p).read_bytes()).hexdigest())
c=dict(batch_id='CLEAN11',record_directory='records/S6_SERIES_PUBLISH_II_clean_checks_11',
 event_bundle='records/S6_SERIES_PUBLISH_zzz_continuation_016_clean_CHECK_EVENTS.tsv',
 prior_admission=b('records/S6_SERIES_PUBLISH_II_clean_checks_10/manifest.json'),
 proposal=b('records/S6_SERIES_PUBLISH_II_SX_033C_033O_reviewed_proposals.json'),
 event_proposal=b('records/S6_SERIES_PUBLISH_II_SX_033C_033O_reviewed_event_proposals.json'),
 root_review=b('records/S6_SERIES_PUBLISH_II_SX_033C_033O_editorial_guard.json'),
 source_applications=[b('records/S6_SERIES_PUBLISH_II_SX_033C_033O_editorial_apply.json')],
 before_ledger_sha256='7c22f26f92c0bb01c3fb092a93a96c19471431907c8f13a16faf26559207c790',
 source_sha256='e79da9d0e170bfe2ff2264024fa5c1900089faadf82dab34effb0e03b182de64',
 independent_checks=3,events=6,
 who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; reasoning effort inherited, no separate numerical setting exposed; restore_build and root',
 event_scope_suffix='All seventeen literal edits are applied and bound to the three complete final blocks. Root read the complete pairs, frozen derivations, final comparisons, literal guards and all arithmetic programs and outputs at their recorded scopes. D12 structural ownership for 033C remains open; no extra check of its input owners or exposed 0339/033P is counted.',
 scope='Three prerelease independent checks: the tangent-field counterexample and published-source diagnosis; arbitrary connected-family and deformation-chain corollary from its declared inputs; dual integral monodromy, centralizers and lattices. Three additional events record the actual complete comparative rereading. The extra Gram/Newton arithmetic supports the existing centralizer check without a further independent event. All labels and anchors remain.',
 proof_repairs=[dict(statement_owner='push:src:E.5.2',tag='033O',defect_type='D25',
 original_error='Inverse transpose was invoked on the whole centralizer algebra, which contains the singular matrix E41.',
 corrected_step='The linear bijection C to C^t, with inverse itself, sends the homological centralizer to the cohomological centralizer: CH_i=H_iC is equivalent to C^tT_i=T_iC^t for H_i=T_i^{-t}; I and E41 map to I and E14.',
 statement_changed=False,all_printed_matrices_and_lattice_values_unchanged=True,
 evidence=b('agents/ii_infra/recovery_20261121/S6_SERIES_PUBLISH_II_SX_033C_033O_comparison_v4.json'))])
p=R/'records/S6_SERIES_PUBLISH_II_clean_checks_11_config.json';assert not p.exists();p.write_text(json.dumps(c,indent=2)+'\n')
print(json.dumps(b(str(p.relative_to(R)))))
