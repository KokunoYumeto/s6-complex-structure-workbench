#!/usr/bin/env python3
"""Prepare exact unapplied presentation/scope guards for four read II blocks."""
from pathlib import Path
import datetime,hashlib,json,re
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'agents/ii_infra';DEST=OUT/'first_four_guard_blocks'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def digest(s):return hashlib.sha256(s.encode()).hexdigest()
def math(s):return re.findall(r'(?<!\\)\$(?:\\.|[^$])*(?<!\\)\$',s)
def refs(s):return re.findall(r'\\(?:ref|eqref|SeriesRef|CompendiumRef)(?:\{[^}]*\})?\{[^}]*\}',s)
source=ROOT/'S6_SERIES_PUBLISH_II.tex';current=source.read_text();source_hash=sha(source)
changes={
 '01F8':[
  ('title','D03/D16',r'[Refuted surface assertion, with explicit example]',r'[A secondary Kodaira surface with torsion-free first homology]',
   'Give the retained constructed surface a mathematical title, without a refutation/process header.'),
  ('preface','D03','The assertion that every secondary Kodaira surface has torsion in\n$H_1(-;\\Z)$ is false. ', '',
   'Retain the positive existence statement and its full proof. Its isomorphism H1(Q;Z)=Z already implies that the universal torsion assertion fails: under this isomorphism a finite-order class maps to an integer n with kn=0, hence n=0. Thus the deleted negation is logically entailed by the retained example.'),
  ('checktail','D09',' The matrix and lattice\ncalculations have been checked exactly by the attached program.','',
   'Remove the check-record sentence. The actual lattice, matrix, determinant and descent arguments remain in the proof, and the new exact computations are bound in the check comparison record.')],
 '01F9':[
  ('title','D03/D16',r'[Refuted surface assertion, with explicit example]',r'[A secondary Hopf surface with torsion-free first homology]',
   'Give the retained constructed surface a mathematical title.'),
  ('preface','D03','The assertion that a secondary Hopf surface has torsion in\n$H_1(-;\\Z)$ is false. ', '',
   'Retain the positive existence statement and proof. H1(Q_H;Z)=Z forces its torsion subgroup to vanish by the integer equation kn=0, so the removed blanket-assertion refutation follows from the retained example.')],
 '01FA':[
  ('title','D16',r'\begin{proposition}\hypertarget{tag-01FA}',r'\begin{proposition}[Obstruction to K\"ahler resolutions]\hypertarget{tag-01FA}',
   'Supply a mathematical title for the main-chain statement.'),
  ('smoothscope','D25','Let $Y$ be a compact complex threefold with $b_2(Y)=0$,','Let $Y$ be a smooth compact complex threefold with $b_2(Y)=0$,',
   'Make explicit the smooth ambient hypothesis used by the printed proof to make each component Cartier. This is a scope clarification/repair of the stated setup, not a claim that the broader singular reading is false or proved. Root receiving-use audit binds the intended smooth uses.'),
  ('stepmarker','D08',r'\noindent\textbf{Step 1.} ','',
   'Remove the redundant manually printed Step1 marker inside the already numbered proof item.')],
 '01G8':[
  ('title','D16',r'[Proved obstruction]',r'[Components under trivial torus monodromy]',
   'Replace the status header with a mathematical title.'),
  ('smoothscope','D25','A compact complex threefold with $b_1=b_2=0$','A smooth compact complex threefold with $b_1=b_2=0$',
   'Name the smooth ambient hypothesis required by the C.3.4 application. Root audited all coded receiving uses; the only incoming reference is a further-results inventory entry.'),
  ('proofparagraph','D08/D22',
   r'''\noindent\textbf{Step 1.} The base is $\PP^1$ by \ref{cdp:st:D.1.2}. Trivial monodromy on the
four-dimensional $H_1(F;\Q)$ gives $t'=4$, so the corrected formula
gives $r=s+3$. If all removed fibres were irreducible one would have
$r=s$, which is impossible. The assertion about each component is
Statement \ref{cdp:st:C.3.4}, applied to this threefold. The last assertion follows
by combining these two conclusions.''',
   r'''Pullback on first rational cohomology from the base is injective because
the fibres are connected. Thus the base is $\PP^1$. Trivial monodromy on
the four-dimensional $H_1(F;\Q)$ gives $t'=4$, and the count in
Proposition~\ref{cdp:st:D.1.2} gives $r=s+3$. If all removed fibres were
irreducible one would have $r=s$, which is impossible. The assertion
about each component is Proposition~\ref{cdp:st:C.3.4}, applied to this
threefold. Such a reducible fibre prevents all fibre components from
admitting compact K\"ahler resolutions.''',
   'Supply the actual rational base-genus argument from connected fibres and b1(Y)=0 before applying the general component-count identity. The printed D.1.2 base=P1 conclusion is stated under stronger integral assumptions, so it is not used as an unqualified citation here. Keep every numerical formula and both reference targets, replace the corrected-formula/process wording, and state the final deduction explicitly.')]
}
owners={'01F8':'cdp:st:C.3.2','01F9':'cdp:st:C.3.3','01FA':'cdp:st:C.3.4','01G8':'cdp:st:D.2.1'}
DEST.mkdir(exist_ok=False);guards=[];blocks=[]
audit=ROOT/'records/S6_SERIES_PUBLISH_II_01FA_01G8_root_receiver_audit.json';assert audit.exists()
for tag,edits in changes.items():
 release_paths=list((OUT/'released_proofs'/tag).glob('*/S6_SERIES_PUBLISH_full_owning_block.tex'));assert len(release_paths)==1
 before=release_paths[0].read_text();assert current.count(before)==1,(tag,'current complete block mismatch')
 after=before;local=[]
 for name,typ,old,new,reason in edits:
  assert after.count(old)==1,(tag,name,'guard uniqueness');after=after.replace(old,new,1)
  local.append({'id':f'II-infra-{tag}-{name}','statement_id':owners[tag],'tag':tag,'source_sha256':source_hash,
                'before':old,'after':new,'type':typ,'reason':reason})
 bp=DEST/f'S6_SERIES_PUBLISH_II_{tag}_before.tex';ap=DEST/f'S6_SERIES_PUBLISH_II_{tag}_after.tex';bp.write_text(before);ap.write_text(after)
 before_math=math(before);after_math=math(after);removed=[]
 if tag in ['01F8','01F9']:
  expected=r'$H_1(-;\Z)$';assert before_math.count(expected)==1;before_math.remove(expected);removed=[expected]
 assert before_math==after_math,(tag,'unexpected inline-math change')
 assert refs(before)==refs(after),(tag,'reference target/order change')
 for guard in local:
  guard.update({'original_full_block':str(bp.relative_to(ROOT)),'original_full_block_sha256':sha(bp),
                'proposed_full_block':str(ap.relative_to(ROOT)),'proposed_full_block_sha256':sha(ap),
                'frozen_target_source_sha256':'74497bfe327fae25c9cdcb17334b3bf42a9793a9df7c0a4404d97568f2f760f0',
                'inline_math_preservation':'exact order after only the named removal of the redundant H1(-;Z) phrase in01F8/01F9' if removed else 'exact sequence',
                'removed_inline_segments':removed if guard['id'].endswith('preface') else [],
                'reference_sequence_identical':True,'mathematical_check_record':'agents/ii_infra/S6_SERIES_PUBLISH_II_first_four_comparison.json'})
  if name=='smoothscope' or tag in ['01FA','01G8']:guard['receiving_use_evidence']={'path':str(audit.relative_to(ROOT)),'sha256':sha(audit)}
 guards.extend(local);blocks.append({'tag':tag,'statement_id':owners[tag],'original_full_block':str(bp.relative_to(ROOT)),'original_full_block_sha256':sha(bp),'proposed_full_block':str(ap.relative_to(ROOT)),'proposed_full_block_sha256':sha(ap),'guard_ids':[x['id'] for x in local],'inline_math_named_removal':removed,'references_identical':True})
result={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'UNAPPLIED; requires root review and complete proposed-block comparative reading','source_sha256':source_hash,'guards':guards,'blocks':blocks,'mathematical_events_added':0,'canonical_files_modified':False,
        'remaining_finding':{'tag':'01F9','type':'D09','description':'Finite quaternion enumeration is stated via an attached-program reference without a pinned repository/file citation. New independent exact2x2 algebraic-field matrix verification is complete; root must supply the final once-only program citation/table binding. This pending finding is not claimed closed by the present presentation guards.'}}
p=OUT/'S6_SERIES_PUBLISH_II_first_four_unapplied_guards.json';assert not p.exists();p.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'path':str(p.relative_to(ROOT)),'sha256':sha(p),'guards':len(guards),'blocks':len(blocks),'source_sha256':source_hash},indent=2))
if __name__=='__main__':pass
