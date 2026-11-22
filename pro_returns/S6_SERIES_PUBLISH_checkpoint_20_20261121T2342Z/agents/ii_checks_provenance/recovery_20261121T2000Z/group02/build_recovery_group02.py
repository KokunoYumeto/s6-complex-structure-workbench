from pathlib import Path
import copy,hashlib,json,re
from datetime import datetime,timezone

ROOT=Path(__file__).resolve().parents[4]
HERE=Path(__file__).resolve().parent
OLD=ROOT/'agents/ii_checks_provenance/group02'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def ref(p):return {'path':str(p.relative_to(ROOT)),'sha256':sha(p)}
def write_json(p,o):p.write_text(json.dumps(o,indent=2,ensure_ascii=False)+'\n')
def check_ref(o):
    if isinstance(o,dict):
        if 'path' in o and 'sha256' in o and isinstance(o['path'],str):
            p=ROOT/o['path'];assert p.is_file(),p
            assert sha(p)==o['sha256'],p
        for v in o.values():check_ref(v)
    elif isinstance(o,list):
        for v in o:check_ref(v)

prior_path=OLD/'S6_SERIES_PUBLISH_II_B_group02_proposals.json'
prior=json.loads(prior_path.read_text())
methods_path=OLD/'S6_SERIES_PUBLISH_II_B_group02_methods_addendum.json'
methods=json.loads(methods_path.read_text())
check_ref(prior);check_ref(methods)
source_path=ROOT/'S6_SERIES_PUBLISH_II.tex';source=source_path.read_text()
now=datetime.now(timezone.utc).isoformat()
targets=[]
for old in prior['targets']:
    tag=old['tag'];o=copy.deepcopy(old)
    original=(ROOT/o['original_full_block']['path']).read_text()
    proposal=(ROOT/o['proposed_full_block']['path']).read_text()
    assert source.count(original)==1,(tag,'source original')
    extra=[]
    def change(cid,typ,before,after,reason):
        global proposal
        assert proposal.count(before)==1,(tag,cid,proposal.count(before))
        proposal=proposal.replace(before,after,1)
        extra.append({'change_id':cid,'defect_type':typ,'old':before,'new':after,'reason':reason,'recovery_new_guard':True})
    change('II-REC02-'+tag+'-ENUM','D04,D23',
           r'\begin{enumerate}[label={$\langle1\rangle$\arabic*.},leftmargin=*]',
           r'\begin{enumerate}[label=\arabic*.,leftmargin=*]',
           'Remove the inherited iteration marker; retain the order and all proof steps.')
    if tag=='01BM':
        change('II-REC02-01BM-CASTELNUOVO','D18',
          "Castelnuovo's rationality criterion, in the form $q=P_2=0$ for a smooth projective surface, makes $E$ rational.",
          r"The invariants $q$ and $P_2$ are unchanged under point blowups. Castelnuovo's criterion \cite[Theorem~2.26, p.~178]{Hassett2009Rational}, applied to a smooth minimal model of $E$, therefore makes $E$ rational.",
          'Bind the precise primary theorem and the birational invariance required for its minimal-surface hypotheses.')
    if tag=='01BL':
        # Only the equation-tag/label association is extracted; this does not
        # display or read the proof containing the target equation.
        matches=re.findall(r'\\tag\{B\.2\}(?:\\hypertarget\{[^}]*\}\{\})?\\label\{([^}]+)\}',source)
        assert len(matches)==1,matches
        change('II-REC02-01BL-B2REF','D06',
          'the normalization calculation in (B.2)',
          'the normalization calculation in '+r'\eqref{'+matches[0]+'}',
          'Use the exact existing equation label for the retained normalization calculation.')
    original_copy=HERE/f'S6_SERIES_PUBLISH_II_{tag}_recovery_original.tex'
    proposed_copy=HERE/f'S6_SERIES_PUBLISH_II_{tag}_recovery_proposed.tex'
    original_copy.write_text(original);proposed_copy.write_text(proposal)
    pointer=json.loads((ROOT/'agents/ii_checks_provenance/derivations'/f'S6_SERIES_PUBLISH_II_{tag}_freeze_pointer.json').read_text())
    freeze_path=ROOT/pointer['receipt'];assert sha(freeze_path)==pointer['sha256']
    freeze=json.loads(freeze_path.read_text())
    frozen=ROOT/freeze['frozen_derivation_path'];assert sha(frozen)==freeze['derivation_sha256']
    o.update({
      'original_full_block':ref(original_copy),'restored_v1_proposed_full_block':old['proposed_full_block'],
      'proposed_full_block':ref(proposed_copy),'durable_frozen_derivation':ref(frozen),
      'guards':old['guards']+extra,
      'recovery_scope':'New reconstruction based on exact CP14-restored records. Lost later proposal bytes are not claimed recovered.',
      'actual_original_complete_proof_reread_in_recovery':True,
      'actual_restored_v1_complete_proof_reread_in_recovery':True,
      'recovery_final_complete_proof_read':False,
      'manual_pair_read_completed_utc':None,
      'source_application_pending':True,
      'program_method_comparison_status':'Durable methods addendum plus new post-reset node/chart certificate; no new independence from recovery.',
      'events_added':0
    })
    if tag=='01BL':
        o['fresh_programs'].append({
          'program':ref(HERE/'S6_SERIES_PUBLISH_II_01BL_recovery_node_certificate.py'),
          'output':ref(HERE/'S6_SERIES_PUBLISH_II_01BL_recovery_node_certificate.output.json'),
          'timing':'Newly written and executed after reset and prior target exposure; replacement supplement, not recovered old bytes.',
          'method':'Dual-number first-variation coefficient convolution at a node; degree-certified seven-point interpolation for the affine section; Laurent exponent transport for the whole infinity chart. The old routine used a multivariate singularity Groebner basis and direct symbolic section substitution.',
          'scope':'Together with the durable squarefreeness certificate, proves the nonzero total-space node derivative. It also checks P on the finite/infinity charts and the zero-section partial.',
          'new_independent_events':0})
    targets.append(o)

bib=r'''\bibitem{Hassett2009Rational}
B.~Hassett, \emph{Rational surfaces over nonclosed fields},
in \emph{Arithmetic Geometry}, H.~Darmon, D.~Ellwood, B.~Hassett and Y.~Tschinkel (eds.),
Clay Mathematics Proceedings \textbf{8}, American Mathematical Society and Clay Mathematics Institute, 2009, pp.~155--209.
\url{https://www.claymath.org/wp-content/uploads/2022/03/cmip08c.pdf}.
'''
assert 'Hassett2009Rational' not in source
bib_path=HERE/'S6_SERIES_PUBLISH_II_Hassett2009Rational_proposed_entry.tex';bib_path.write_text(bib)
receipt={
 'schema_version':1,'paper':'II','allocation':'B','checker':'i_provenance',
 'created_utc':now,'record_kind':'post-reset reconstruction with new complete comparisons',
 'canonical_source_at_review':ref(source_path),
 'restored_group02_proposals':ref(prior_path),'restored_methods_addendum':ref(methods_path),
 'durable_prerelease_evidence':'All three actual pre-target derivations and their original freeze/release receipts were restored byte-for-byte from CP14 and verified again here.',
 'lost_later_records':'The post-CP14 v2 and final-event JSONs are not available as historical bytes. This new bundle reconstructs their mathematical scope and adds fresh after-exposure verification.',
 'targets':targets,'bibliography_proposal':ref(bib_path),
 'bibliography_guard':{'change_id':'II-REC02-HASSETT-BIB','defect_type':'D18','old':r'\end{thebibliography}','new':bib+'\n'+r'\end{thebibliography}','reason':'Supply the primary reference used by the exact Castelnuovo locator.'},
 'primary_receipts':[{'url':'https://www.claymath.org/wp-content/uploads/2022/03/cmip08c.pdf','web_reference':'turn361322681view0','location':'Hassett Theorem 2.26, printed p.178, PDF zero-based page184','actual_scope_read':'Complete theorem and attached proof were reopened during recovery; q and P2 are explicitly birational invariants, and the theorem is stated for a smooth projective minimal surface.','reopened_utc':now}],
 'proposed_event_counts':{'targeted proof check':3,'used and rechecked':3},
 'event_scope':'These are the same three unique owning statements. Prerelease support comes only from durable original freezes. Recovery adds no duplicate event and no independent computation credit.',
 'canonical_mutations':0,'events_added':0,
 'status':'Complete final source-pair rereading pending before parent approval.'}
out=HERE/'S6_SERIES_PUBLISH_II_B_group02_recovery_proposals.json';write_json(out,receipt)
print(json.dumps({'proposal':ref(out),'targets':len(targets),'guards':sum(len(x['guards']) for x in targets),'bibliography_guard':1},indent=2))
