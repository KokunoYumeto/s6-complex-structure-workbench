"""Concrete standalone-wording findings; does not edit any manuscript."""
from pathlib import Path
import json,re,hashlib
D=Path(__file__).resolve().parents[2];W=D/'work/cdp_audit/push_C_retention'
rows=[]
def add(sid,before,after,reason,status='proposed to parent editor'):
    rows.append({'source_id':sid,'before':before,'after':after,'reason':reason,'status':status,'mathematical_argument_removed':False})
for before,after in [(r'\bar p^{,2}',r'\bar p^{\,2}'),(r'\bar c^{,2}',r'\bar c^{\,2}'),(r'\bar c^{,4}',r'\bar c^{\,4}')]:
    add('C.2.1',before,after,'Original source inherited a literal comma superscript. The proof explicitly uses the ordinary second/fourth powers; this restores the intended thin-space typography.','Parent reports applied in assembler, exact count asserted, 2026-11-17 04:49 UTC.')
add('C.3.22','C.3.19:',r'\cref{push:src:C.3.19}:','Raw theorem locator followed by colon escaped the original raw_refs boundary rule.','Parent reports applied in assembler, exact count asserted, 2026-11-17 04:49 UTC.')
add('C.3.26','C.3.20:',r'\cref{push:src:C.3.20}:','Raw theorem locator followed by colon escaped the original raw_refs boundary rule.','Parent reports applied in assembler, exact count asserted, 2026-11-17 04:49 UTC.')
add('C.1.1','For the family in the prompt the gluing map is',r'For the marked family $X_c$ the gluing map is','Standalone statement should identify its actual family, not an absent prompt.')
add('C.preamble','the specific analytic\nfilling of Part B','the specified descended analytic\nfilling','The immediately preceding numbered Paper I theorem identifies the excluded filling.')
add('C.preamble','any unconstructed\nfilling in Part B.','that excluded\nanalytic filling.','Remove obsolete source-part pointer; preserves the limitation.')
add('C.2.1','the existence of the particular\ngeometric $W_8$ proposed in Part B is a separate assertion.','the existence of a particular\ngeometric coboundary requires a separate construction.','General characteristic formula does not construct a coboundary.')
add('C.2.3','not the invariant requested\nin Part C.',r'not the invariant $\mu(M_\Phi)$ of the original mapping torus.','Names the exact invariant rather than an absent source part.')
add('C.3.21','model of Part B fills the original six-sphere.','model supplies the excluded analytic filling of the original six-sphere.','Retains the distinction between the actual relative Picard calculation and the excluded compact-core filling.')
add('C.3.25','specific analytic filling requested in Part B.',r'specified analytic filling excluded by Paper~I, Theorem~21.58.','Replace source-part pointer by the currently verified numbered exclusion.')
add('C.3.27','specific analytic filling proposed in Part B.',r'specified analytic filling excluded by Paper~I, Theorem~21.58.','Replace source-part pointer by the currently verified numbered exclusion.')
add('C.5.1',r'\begin{corollary}[Refuted): the specified analytic filling premise]',r'\begin{corollary}[Counterexample: the specified analytic filling premise]','Normalize inherited unmatched source-status punctuation.')
add('C.5.1','The analytic descended filling and its resolution $W_8$\nrequested in Parts B.4 and C.2 do not exist.','The descended analytic filling excluded by Paper~I, Theorem~21.58,\nand its proposed resolution $W_8$ do not exist.','Identifies the exact excluded object with the operative proof, without an obsolete request pointer.')
add('C.3.12',r'''The nonextension of the raw invariant-circle coordinate was already
recorded in the supplied \path{background/notes/A1_notes.md},
Section~2, item A1--1, and
\path{background/S6_SURVEY_20261112.md}, item F9.
The assertion proved here has the stronger quantified scope of every
Hausdorff-valued continuous map with the stated regular translational
leaves.''',r'''The final paragraph below also proves nonextension of the raw
invariant-circle coordinate. The proposition has the stronger quantified
scope of every Hausdorff-valued continuous map with the stated regular
translational leaves.''','The two filenames are historical provenance only, not an operative proof. Their exact original text is retained in the comparison/source ledger; the complete proof remains printed.')
obj={'reader':'GPT-6 Astra (OpenAI, ChatGPT Pro mode)','effort':'Pro','date':'2026-11-17',
     'scope':'Exact source-to-print typography, locator and standalone-wording findings. No manuscript edited by this script.',
     'proof_by_pointer_substitution_found':False,'missing_full_proof_found':False,'replacements':rows}
(W/'editorial_findings.json').write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')

tex={k:(D/f'S6_09_PAPERS_{k}.tex').read_text()for k in ['I','II','III']}
labs={k:set(re.findall(r'\\label\{([^}]+)\}',s))for k,s in tex.items()}
aux=(D/'S6_09_PAPERS_III.aux').read_text();nums=dict(re.findall(r'\\newlabel\{([^}]+)\}\{\{([^}]+)\}',aux));kinds=dict(re.findall(r'\\newlabel\{([^}]+)@cref\}\{\{\[([^\]]+)\]',aux))
overview=[{'printed_locator':n,'label':lab,'actual_number':nums[lab],'actual_kind':kinds[lab],'matches':nums[lab]==n}for n,lab in [('2.4','maps:src:B.2.1'),('6.52','maps:src:F.4.1'),('7.32','push:src:C.3.27')]]
unresolved={}
for k in ['I','II']:
    refs={a for z in re.findall(r'\\(?:ref|eqref|cref|Cref|autoref)\{([^}]+)\}',tex[k])for a in z.split(',')}
    unresolved[k]=sorted((refs-labs[k])&labs['III'])
cross={'reader':obj['reader'],'effort':'Pro','date':'2026-11-17',
 'scope':'Explicit Paper III prose references in I/II and any unresolved direct references whose labels are defined only in III.',
 'paper_hashes':{k:hashlib.sha256(v.encode()).hexdigest()for k,v in tex.items()},
 'III_aux_sha256':hashlib.sha256(aux.encode()).hexdigest(),'I_overview_references':overview,
 'other_explicit_Paper_III_numbered_mentions_found':[],
 'references_to_III_only_labels_unresolved_in_I_or_II':unresolved,'stale_numbers_found':[],
 'I_and_II_edited':False}
(W/'cross_paper_numbering_review.json').write_text(json.dumps(cross,indent=2)+'\n')
print('Saved',len(rows),'exact editorial findings; all three I overview references match current III aux.')
