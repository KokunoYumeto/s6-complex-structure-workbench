"""Prepare reviewed editorial changes to unrestricted-Euler proofs 1--3."""
from pathlib import Path
import datetime,hashlib,json
R=Path(__file__).resolve().parents[1]
source=R/'S6_SERIES_PUBLISH_II.tex';before=source.read_text();s=before
sha=lambda x:hashlib.sha256(x.encode() if isinstance(x,str) else x).hexdigest()
assert sha(before)=='a6a843671854ec136279c42ef53eb3b9a2950787adb07d9fb84db2d3cbe30bf4'
meta=json.loads((R/'agents/ii_infra/S6_SERIES_PUBLISH_II_structure_metadata.json').read_text())
frozen=(R/'agents/ii_infra/S6_SERIES_PUBLISH_II_original_source_embargoed.tex').read_text()
owners=['cdp:st:C.2.UN.1','cdp:st:C.2.UN.2','cdp:st:C.2.UN.3']
blocks={}
for owner in owners:
 x=next(x for x in meta['statements'] if x['owner']==owner)
 p=x['proofs'][0]
 b=frozen[x['start']:p['end']]
 assert b in before
 blocks[owner]=dict(original=b,statement=x,proof=p)
patches=[]
def change(owner,old,new,typ,reason):
 global s
 assert old!=new
 label='\\label{'+owner+'}'
 start=s.rfind('\\begin{proposition}',0,s.index(label))
 end=s.index('\\end{proof}',s.index(label))+len('\\end{proof}')
 b=s[start:end];assert b.count(old)==1,(owner,old,b.count(old))
 pos=start+b.index(old)
 a,z=pos,pos+len(old)
 while s.count(s[a:z])!=1:
  a=max(start,a-100);z=min(end,z+100)
  assert a<pos or z>pos+len(old)
 oldguard=s[a:z];newguard=s[a:pos]+new+s[pos+len(old):z]
 patches.append(dict(old=oldguard,new=newguard,type=typ,statement_id=owner,reason=reason,
                     changed_old_literal=old,changed_new_literal=new))
 s=s[:a]+newguard+s[z:]

enum=r'\begin{enumerate}[label={$\langle1\rangle$\arabic*.},leftmargin=*]'
for owner in owners:
 change(owner,enum,r'\begin{enumerate}[label=\arabic*.,leftmargin=*]','D10',
 'Remove the imported outline-depth marker from this proof enumeration. The order, number and complete mathematical content of its steps are identical.')

change(owners[0],'''This assertion allows arbitrary multiplicities and singularities and
imposes no K\\"ahler or Betti-number hypothesis on $Y$.''',
'''The fibres may have arbitrary multiplicities and singularities.''','D02',
'The initial hypothesis already quantifies over every proper holomorphic map from a smooth complex threefold as stated, without a Kähler or Betti restriction. The replacement preserves arbitrary multiplicities and support singularities explicitly; no hypothesis is inserted or removed from that quantified class.')
change(owners[0],'''We verify that $\\operatorname{rank}(G-I)$ is even without a
semisimplicity assumption.''', '''The rank $\\operatorname{rank}(G-I)$ is even.''','D02',
'The following generalized-eigenspace and Cayley-transform proof is unchanged, including the nonsemisimple case. The scope is precisely the already defined orthogonal transformation G with determinant one.')
change(owners[0],'''This proves the assertion. Since $\\dim\\Lambda^2\\Q^4=6$, $a_2$ is''',
'''Since $\\dim\\Lambda^2\\Q^4=6$, $a_2$ is''','D08',
'Delete a closing recap between the unchanged even-rank calculation and its unchanged six-dimensional kernel consequence.')
change(owners[1],'''In $A\\times\\PP^1$ retain the smooth horizontal surface
$R=C_2\\times\\PP^1$.''', '''In $A\\times\\PP^1$ let
$R=C_2\\times\\PP^1$ be the smooth horizontal surface.''','D08',
'The surface R and its ambient embedding are identical; the construction is stated directly.')
change(owners[1],'''The exact arithmetic and exterior-square checks are in
\\path{code/root_unrestricted_euler.py} and its output.
This family supplies further members of the requested unrestricted
zero-Euler classification; it does not claim that every zero-Euler
fibre has this construction.''','', 'D09',
'Move the historical file attribution and scope recap to this check record. The complete construction, Euler computation, integral Betti tuple and structure-sheaf direct-image argument remain in the proof. The stated existential family, not a classification of every filling, is unchanged. The historical program is not in the attached program source/file list; no unverified program URL is introduced. Its already recorded historical checks remain untouched.')
change(owners[2],'''The other is the local filling
(D.23), whose central support''', '''The other is the local filling
\\eqref{cdp:eq:D.23}, whose central support''','D06',
'The unique displayed tag D.23 has the permanent label cdp:eq:D.23. Replace its literal old number with that exact label; the referred local filling is unchanged.')
change(owners[2],'''with the given punctured
family retained.''', '''with the given punctured
family fixed.''','D08',
'The isomorphism on the punctured family remains part of the assertion; replace its workflow verb by the fixed mathematical datum.')
change(owners[2],'''Here is the analytic justification, without
using a global function field.''', '''The analytic justification is as follows.''','D02',
'The proof by properness, dimension and finite modifications is unchanged in full; remove only the unnecessary contrast with a different proof method.')
change(owners[2],'''divisors correspond birationally, rather
than only by a generically finite map.''', '''divisors correspond birationally.''','D02',
'Keep the proved birational correspondence, which follows from the degree-one strict-transform map just established. Remove its closing comparison with a weaker conclusion.')
change(owners[2],'''\\item We now give the actual local models. Put''', '''\\item Put''','D08',
'The complete explicit local model immediately follows unchanged; delete its workflow introduction.')
change(owners[2],'''These identifications and the integral
transgression are also calculated in
(D.23)--(D.25).''', '''The identifications and the integral
transgression are calculated in
\\eqref{cdp:eq:D.23}--\\eqref{cdp:eq:D.25}.''','D06',
'The unique old displayed tags D.23 and D.25 have the permanent labels cdp:eq:D.23 and cdp:eq:D.25. This is the exact old-to-new reference map; all calculations are unchanged.')
change(owners[2],'''\\item Here is the comparison after a finite base
change, with its ramification retained.''', '''\\item Consider a finite base change.''','D08',
'The immediately following equation t=u(s)s^m, the nonzero unit, its exact root parameter change and the ramified local charts all remain unchanged.')
change(owners[2],'''\\item For completeness the corresponding calculation
for $P_n$ retains the extension class.''', '''\\item For $P_n$, the corresponding calculation
also determines the extension class.''','D08',
'The circle-bundle Chern number, central extension presentation, injective fibre group and H1 calculation are preserved exactly.')

directory=R/'records/S6_SERIES_PUBLISH_II_root_proof_edits_01'
assert not directory.exists();directory.mkdir()
comparisons=[]
for owner,info in blocks.items():
 old=info['original'];label='\\label{'+owner+'}'
 start=s.rfind('\\begin{proposition}',0,s.index(label));end=s.index('\\end{proof}',s.index(label))+len('\\end{proof}')
 new=s[start:end]
 slug=owner.replace(':','_').replace('.','_')
 (directory/(slug+'_before.tex')).write_text(old)
 (directory/(slug+'_after.tex')).write_text(new)
 comparisons.append(dict(owner=owner,original_source_sha256=sha(frozen),
   original_statement_lines=[info['statement']['start_line'],info['statement']['end_line']],
   original_proof_lines=[info['proof']['start_line'],info['proof']['end_line']],
   before_path=str((directory/(slug+'_before.tex')).relative_to(R)),before_sha256=sha(old),
   after_path=str((directory/(slug+'_after.tex')).relative_to(R)),after_sha256=sha(new),
   printed_proof_read_before_editorial_preparation=True,
   independent_derivation_claimed=False,comparison_after_preparation='pending actual reread'))
guard=dict(paper='II',created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
 source_before_sha256=sha(before),patches=patches,comparisons= comparisons,
 mathematical_events_added=0,visual_reading_credit=0)
(directory/'guard.json').write_text(json.dumps(guard,indent=2)+'\n')
print(json.dumps(dict(path=str((directory/'guard.json').relative_to(R)),sha256=sha((directory/'guard.json').read_bytes()),patches=len(patches),comparison_owners=owners),indent=2))
