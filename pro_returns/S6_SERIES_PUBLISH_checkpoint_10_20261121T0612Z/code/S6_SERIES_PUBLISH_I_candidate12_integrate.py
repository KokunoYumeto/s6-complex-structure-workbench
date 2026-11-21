"""One-shot integration of fully compared candidate11 proof/order guards."""
from pathlib import Path
import collections, csv, datetime, hashlib, json, re
from S6_SERIES_PUBLISH_editing import Editor, block

r = Path(__file__).resolve().parents[1]
ed = Editor('I')
base = '7479a42f0c18cb2853e483ba3b0b222087e800a6a720ca5f2a21313ff6706cc6'
assert hashlib.sha256(ed.before.encode()).hexdigest() == base
subjects = ['fam:src:A.3.1', 'fam:src:A.5.1', 'fam:src:B.2.1']
before = {lab: block(ed.text, lab) for lab in subjects}
tag = 'PI00'
for p in list(r.glob('S6_SERIES_PUBLISH_*.tex')) + list((r.parent/'source').rglob('*.tex')):
    assert 'tag-'+tag not in p.read_text(errors='replace'), p

struct_path = r/'agents/i_provenance/S6_SERIES_PUBLISH_I_candidate11_structure_guards.json'
struct = json.loads(struct_path.read_text())
assert hashlib.sha256(struct_path.read_bytes()).hexdigest() == 'ae6bcc58a53f114e043e4aba41dfeca82fcd51d5a75d6c9f5aac356adff12956'
for g in struct['changes']:
    kind = 'D04' if g['id'] in ['IP-C11-S07', 'IP-C11-S08', 'IP-C11-S09'] else 'D14'
    ed.replace(g['old'], g['new'], kind, g['reason'], g['statement_scope'])

residue = json.loads((r/'agents/i_analytic/S6_SERIES_PUBLISH_I_residue_order_guards.json').read_text())
for g in residue['guards']:
    ed.replace(g['old'], g['new'].replace('S6_NEW_RESIDUE_TAG', tag), 'D14',
               g['action'] + '; complete original/current/replacement proof comparison archived by analyst and read by root; no independent credit.',
               'inv:A1.3' if g['id']=='I-RES-01' else 'inv:A2.4')

component = json.loads((r/'agents/i_topology/editorial/S6_SERIES_PUBLISH_I_P26_component_resolution_guarded.json').read_text())
for g in component['patches']:
    ed.replace(g['old'], g['new'], 'D25', g['reason'], g['statement_ids'][0])

visual = json.loads((r/'agents/i_analytic/S6_SERIES_PUBLISH_I_final_candidate11_reading_analytic_guards.json').read_text())
for g in visual['guards']:
    kind = g['defect_type'].split('/')[0]
    ed.replace(g['old'], g['new'], kind, g['reason'],
               'candidate11 page '+str(g['page']), count=g['expected_count'])

anchor = r'\crefname{maintheorem}{theorem}{theorems}'
envs = ['theorem','proposition','lemma','corollary','claim','statement','definition','remark','example','problem','question','auditrecord','test','conjecture','cited','refuted','computed','openq','maintheorem']
protection = '\n'.join(r'\BeforeBeginEnvironment{'+e+r'}{\Needspace{5\baselineskip}}' for e in envs)
ed.replace(anchor, anchor+'\n'+protection, 'D23',
           'Actual candidate11 page reading found statement headings stranded on pages29,61,71,74,248 and250. Reserve five text baselines before every statement-like environment; inspect every changed final page.', 'preamble statement layout')
ed.replace(r'\subsection{Known and new}\label{pub:I:known-new}',
           r'\Needspace{8\baselineskip}'+'\n'+r'\subsection{Known and new}\label{pub:I:known-new}',
           'D23', 'Candidate11 page15 stranded the subsection title before its table; reserve room for title and first table rows.', 'pub:I:known-new')

ed.save()
after = {lab: block(ed.text, lab) for lab in subjects}
receipt = {'created_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
           'source_before_sha256': base, 'source_after_sha256': hashlib.sha256(ed.text.encode()).hexdigest(),
           'new_permanent_tag': {'label':'pub:I:residue-kernel-rank','tag':tag,'collision_scope':'all five working TeX files and every attached TeX file'},
           'comparison_scope':'Root read the complete proposed proper-family proof, the full former coherent proof, the complete old/new classification proof and old/new discrete proof. Original proper-family and discrete proofs were already actually read in candidate11 images. The precise finite-data and covariance equations occur before the construction. No statement clauses changed. Root also read the full original/current/replacement cotangent and scalar blocks and the full component-resolution repair. Analyst/topology evidence groups retain their own exposed scopes; no extra independent or computational credit.',
           'subjects':{lab:{'before':before[lab],'after':after[lab]} for lab in subjects},
           'guard_files':[str(struct_path.relative_to(r)), 'agents/i_analytic/S6_SERIES_PUBLISH_I_residue_order_guards.json','agents/i_topology/editorial/S6_SERIES_PUBLISH_I_P26_component_resolution_guarded.json','agents/i_analytic/S6_SERIES_PUBLISH_I_final_candidate11_reading_analytic_guards.json']}
rp = r/'records/S6_SERIES_PUBLISH_I_candidate12_integration_comparison.json'
rp.write_text(json.dumps(receipt,indent=2)+'\n')
rows=[]
for i,lab in enumerate(subjects,1):
    rows.append({'statement_id':lab,'date':'2026-11-21',
                 'who':'GPT-6 Astra (OpenAI), ChatGPT Pro mode, reasoning effort inherited (no separate numeric setting exposed), S6_SERIES_PUBLISH root',
                 'type':'used and rechecked in this run',
                 'outcome':'Complete exposed old/new proof comparison. All statement clauses, exact chart maps, local/cusp gluing, vector-sheaf sequence, group law and quotient assertions retained; supporting construction is moved to first use and its references resolved. No targeted, independent or computational credit.',
                 'event_id':f'ce:publish-I-structure-root-{i}-20261121','phase':'publication structure comparison',
                 'source_file':str(rp.relative_to(r)),'source_row':lab,
                 'source_event_type':'used and rechecked in this run','evidence_group':'eg:publish-I-structure-root-20261121'})
with (r/'records/S6_SERIES_PUBLISH_I_candidate12_structure_CHECK_EVENTS.tsv').open('w') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t');w.writeheader();w.writerows(rows)
print(json.dumps({'new_exposed_associations':len(rows),'new_evidence_groups':1,'independent_credit':0,'new_tag':tag}))
