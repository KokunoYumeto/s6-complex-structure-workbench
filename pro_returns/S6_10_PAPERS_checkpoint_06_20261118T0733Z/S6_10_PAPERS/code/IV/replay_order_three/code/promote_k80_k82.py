"""Integrate three audited proofs, preserving the prior complete master and scope."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil

root=Path(__file__).resolve().parents[1]
def read(name): return json.loads((root/name).read_text())
def sha(name): return hashlib.sha256((root/name).read_bytes()).hexdigest()

proofs={80:'part3_source_zero_reduced_attachment',
        81:'part3_os49_higher_smooth_caps',82:'part3_source_zero_vertical_fans'}
for n,stem in proofs.items():
    q=read(f'records/k{n}_standalone_visual_qa.json')
    assert q['status']=='PASS',n
    assert q.get('tex_sha256',q.get('include_sha256'))==sha(f'notes/{stem}.tex'),n
assert read('records/root_audit_source_zero_reduced_global_attachment.json')['status']=='PASS_REDUCED_A2_FULL_GLOBAL_ATTACHMENT'
assert read('records/checks_audit_source_zero_reduced_global_attachment.json')['status']=='PASS'
assert read('records/root_audit_os49_order_two_cap_working.json')['status']=='PASS_OT1_TO_OT7'
assert read('records/fourfold_audit_source_zero_vertical_fans.json')['status']=='PASS'

archive=root/'records/checkpoint19_prior_master64'
archive.mkdir(exist_ok=False)
for name in ('S6_06_BLIND_paper.pdf','S6_06_BLIND_paper.log',
             'notes/part3.tex','notes/part3_remaining_return_obligations.tex',
             'code/update_report.py','code/part3/results_mapping.json'):
    dest=archive/name;dest.parent.mkdir(parents=True,exist_ok=True)
    shutil.copy2(root/name,dest)

p=root/'notes/part3.tex';s=p.read_text()
for n,stem in proofs.items():
    line='\\input{notes/'+stem+'.tex}'
    assert line not in s
    s+='\n'+line+'\n'
p.write_text(s)

p=root/'notes/part3_remaining_return_obligations.tex';s=p.read_text()
s=s.replace('The remaining source-zero return is specified by the actual family',
            'The source-zero return is specified by the actual family')
old=r'''including the marked Cartier line, finite character and complete
annular cochain. On the initial and reflected fans the proved
constraints are precisely
\[
 (Z_{\mathcal T},Z_{J\mathcal T})=
 (kA_{\rm scalar}+14e,a+kA_{\rm scalar}+14e),\qquad
 e\in\{0,1\},
\]
where \(A_{\rm scalar}=0\) on the first branch and
\(A_{\rm scalar}=3p-1\) on the second. Determining \(e\)
from the actual oriented global attachment remains an obligation.
The smallest cases are \((0,1)\) or \((14,15)\), and
\((2,4)\) or \((16,18)\), respectively.'''
new=r'''including the marked Cartier line, finite character and complete
annular cochain. K80 completes the reduced branch by the actual
global attachment. Its fixed-scalar initial physical integer is
zero, its reflected class is two, and its coupled classes are
\[
 (Z_{\mathcal T},Z_{J\mathcal T})
       =(k(3p-1),2+k(3p-1))\pmod {28}.
\]
For every vertical-edge fan \(T_j=T(e_1+je_2,e_2)\), K82 gives
\[
 Z_j=k(3p-1)+2\binom{j+2}{3}
                    -k(4p-1)\binom j2\pmod {28}
\]
on that branch. Its actual single-loop native \(C_1\) comparison
also gives, on either branch with \(N=km\),
\[
 Z_j-Z_0=2b\binom{j+1}{3}+(3-b)\binom{j+1}{2}
                                     -N\binom j2\pmod {28}.
\]
The good branch retains the two possibilities
\((Z_0,Z_1)=(0,1)\) or \((14,15)\) until its separate
two-primitive global proof is promoted. Its full finite cut,
two intermediate cap characters and upper source-moment trace
are recorded in the good-cut working proof. Source-zero returns
on nonvertical fans require their own completed comparison.'''
assert old in s;s=s.replace(old,new)
old=r'''Remaining parts of item 3.4 include the further ordinary and
singular-site sectors beyond that scope, the remaining marked
source-moduli loops, and endpoint sectors outside this completed
fixed-source OS49 calculation. No value is assigned here to those
remaining sectors.'''
new=r'''K81 excludes every effective smooth cap of order greater than
one for this OS49 source: its degree-two specialization quotient
\((\mathbb Z/r)^3\) retains nonzero cohomology after the single
global invariant relation. It also excludes the actual good-II
caps by an explicit fundamental-group quotient \(\mathbb Z/3\).
The reduced-II roots of order \(6l+1\) retain their separate
source and Cartier calculation under audit. Remaining parts of
item 3.4 include those singular-site sectors, source-zero
nonvertical fans, the remaining marked source-moduli loops and
endpoint sectors outside the completed fixed-source scope.
No value is assigned here to those remaining sectors.'''
assert old in s;s=s.replace(old,new)
old=r'''\begin{proof}[Recorded reductions, attempted completions and the next exact maps]
\par\medskip\noindent\textbf{The source-zero integer that remains.}\par\nopagebreak[4]'''
new=r'''\begin{proof}[Recorded reductions, attempted completions and the next exact maps]
K80 now supplies the complete reduced period-strip bordism:
\[
 \partial\mathcal W=-N-\mathbb {CP}^{3}_{2}-B_F-B_4
                                      +\mathbb {CP}^{3}_{1}.
\]
The respective auxiliary physical indices are \(-1,1,0,0\),
giving \(A(N)=0\). Its full inverse period and mixed-face
charts identify this outside boundary with the actual parameter
return through K68. The whole fixed trace occurs once; its
normal clutch remains in the proof. K82 carries the resulting
initial class through every actual vertical \(C_1\) flop.

The following paragraphs retain the earlier attempted routes
and the exact intermediate obstructions. The prior full status
text is preserved in
\path{records/checkpoint19_prior_master64/notes/part3_remaining_return_obligations.tex}.
The unresolved good branch has its own chronological two-step
construction; no result on it is inferred from the reduced proof.

\par\medskip\noindent\textbf{The earlier paired source-zero constraint.}\par\nopagebreak[4]'''
assert old in s;s=s.replace(old,new)
old=r'''These maps complete the local face and spin comparisons.
The global period-strip equation, its horizontal fixed cap
and the assignment of every retained or excised face remain
under audit. No source-zero integer has been assigned from
these local pairs.'''
new=r'''These maps completed the local face and spin comparisons.
The subsequent reduced global period-strip equation, its whole
fixed cap and every retained or excised face are proved in K80.
The good branch has a separate two-primitive finite strip and
the exact upper free source trace in
\path{notes/part3_source_zero_good_cut_working.md}; its final
actual-return comparison remains under independent review at
this stage of the record.'''
assert old in s;s=s.replace(old,new)
p.write_text(s)

p=root/'code/update_report.py';s=p.read_text()
s=s.replace('P3K.5–P3K.79; exact corrected scopes below',
            'P3K.5–P3K.82; exact corrected scopes below')
old='The source-zero paired constraints remain (k*A_scalar+14e,a+k*A_scalar+14e), e=0 or1, with A_scalar=0 or3p-1. The smallest good pair is(0,1) or(14,15); reduced p=k=1 gives(2,4) or(16,18). The active finite real cut construction has the explicit source resolution, Cartier line, associated UV=q chart, cap endpoint and charged ruling-end data, but the complete oriented attachment has not been proved.'
new='K80 proves the complete reduced source-zero global attachment, with fixed-scalar initial physical integer0 and reflected class2. The full charged boundary has index-1, the whole fixed trace has index1, and the retained S4 and charge-one faces have index0. Its actual inverse-period and K68 Hopf arrows give the coupled pair(k*(3p-1),2+k*(3p-1)). K82 proves the actual vertical C1 recurrence on both branches and gives every reduced vertical class Z_j=k*(3p-1)+2*binom(j+2,3)-k*(4p-1)*binom(j,2) modulo28. The good branch still retains(0,1) or(14,15) while its separate full two-primitive attachment and actual-return comparison receive final review.'
assert s.count(old)==2;s=s.replace(old,new)
old='K75 retains the source-zero global attachment, further ordinary/singular-site scopes, marked source-moduli loops and endpoint sectors outside this completed fixed-source OS49 scope. Source-zero now has the exact two-node/Tate/Cartier map, both full finite faces with their oriented product-ball boundary, a positive-width charged-shape comparison and the actual spin lift. The global fixed-cap and period-strip equation remains under audit; its exceptional class and each end must be counted once. No unknown central class is assigned.'
new='K81 excludes every effective OS49 smooth cap of order greater than one by its actual degree-two specialization quotient (Z/r)^3 and the retained global invariant relation. Its explicit order-two example has pi1=0 and H2=H3=(Z/2)^2. The actual good-II caps have an explicit Z/3 fundamental-group quotient. The reduced-II order6l+1 source/Cartier topology is recorded separately under audit. K75 retains the good source-zero attachment, source-zero nonvertical fans, further singular-site scopes, marked source-moduli loops and endpoint sectors outside the completed fixed-source OS49 scope. K80 supplies every reduced global fixed-cap and period-strip face with its full units and retained normal clutches; no unknown free characteristic integer is inferred from a finite-group residue.'
assert s.count(old)==2;s=s.replace(old,new)
p.write_text(s)

p=root/'code/part3/results_mapping.json';m=json.loads(p.read_text())
rows=m.setdefault('additional_source_loop_results',[])
add=[{'id':'P3K.80','status':'Proved','item_of_prompt':'3.4',
      'statement':'Complete reduced source-zero global attachment: initial integer0, reflected class2, coupled pair(k*(3p-1),2+k*(3p-1)).',
      'proof':'notes/part3_source_zero_reduced_attachment_working.md',
      'latex_file':'notes/part3_source_zero_reduced_attachment.tex',
      'root_audit':'records/root_audit_source_zero_reduced_global_attachment.json',
      'peer_audit':'records/checks_audit_source_zero_reduced_global_attachment.json',
      'visual_qa':'records/k80_standalone_visual_qa.json'},
     {'id':'P3K.82','status':'Proved','item_of_prompt':'3.4',
      'statement':'Actual source-zero recurrence on every vertical fan; all reduced absolute classes evaluated.',
      'proof':'notes/part3_source_zero_vertical_fans_working.md',
      'latex_file':'notes/part3_source_zero_vertical_fans.tex',
      'certificate':'code/part3_root/source_zero_vertical_fans.json',
      'symbolic_checks':19,'integer_checks':6804,
      'peer_audit':'records/fourfold_audit_source_zero_vertical_fans.json',
      'visual_qa':'records/k82_standalone_visual_qa.json',
      'relative_formula':'2*b*binom(j+1,3)+(3-b)*binom(j+1,2)-N*binom(j,2)',
      'reduced_absolute':'k*(3*p-1)+2*binom(j+2,3)-k*(4*p-1)*binom(j,2) mod28'}]
for row in add:
    if not any(x.get('id')==row['id'] for x in rows):rows.append(row)
p.write_text(json.dumps(m,indent=2)+'\n')
(root/'records/k80_k82_promotion.json').write_text(json.dumps({
 'utc':datetime.now(timezone.utc).isoformat(),
 'status':'PROMOTED_AFTER_FULL_PROOF_AUDITS_AND_STANDALONE_QA',
 'statements':['P3K.80','P3K.81','P3K.82'],
 'tex_sha256':{str(n):sha(f'notes/{stem}.tex') for n,stem in proofs.items()},
 'archive':str(archive.relative_to(root)),'next_master_build':65,
 'remaining_good_absolute':'unassigned pending final actual-return audit',
 'remaining_reduced_II':'working actual source/Cartier topology under audit'
},indent=2)+'\n')
print('K80--82 integrated; prior master64 and complete scope text preserved.')
