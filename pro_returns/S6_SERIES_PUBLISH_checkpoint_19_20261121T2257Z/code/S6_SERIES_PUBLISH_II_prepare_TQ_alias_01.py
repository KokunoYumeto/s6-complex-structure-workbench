"""Retire one production-history remark with an explicit claim/identity map."""
from pathlib import Path
from collections import Counter, defaultdict, deque
import datetime, hashlib, json, re
R=Path(__file__).resolve().parents[1]
O=R/'records/S6_SERIES_PUBLISH_II_TQ_alias_01'
assert not O.exists();O.mkdir()
sha=lambda x:hashlib.sha256(x.encode() if isinstance(x,str) else x).hexdigest()
s=(R/'S6_SERIES_PUBLISH_II.tex').read_text();before=s
a=s.index(r'\begin{theorem}[uniform non-torsion]')
t=s.index(r'\begin{remark}[provenance of the repair]',a)
z=s.index(r'\end{remark}',t)+len(r'\end{remark}')
original=s[a:z];remark=s[t:z]
assert remark==(R/'records/S6_SERIES_PUBLISH_II_root_recovery_edits_01/TQ_before.tex').read_text()
edits=[]
def edit(old,new,typ,reason):
    global s
    assert s.count(old)==1,(old[:80],s.count(old))
    edits.append(dict(old=old,new=new,type=typ,statement_id='wb:thm:uniform-nontorsion-audit',reason=reason))
    s=s.replace(old,new,1)
edit(r'\begin{theorem}[uniform non-torsion]',r'\begin{theorem}[Uniform non-torsion]','D23','Capitalize the mathematical title; every mathematical claim remains.')
old=r'\hypertarget{tag-03DQ}{}\label{wb:thm:uniform-nontorsion-audit}'
new=old+'\n'+r'\hypertarget{tag-01TQ}{}\label{inv:wb:uniform-nontorsion-provenance}'
edit(old,new,'D01/D12','Move the production remark label/tag to the theorem that owns its mathematical argument. Every original identity is retained; the full occurrence-index permutation is explicitly recorded and checked, including the relative order of every other identity.')
old=r'\ There is a line bundle \(L\in\operatorname{Pic}(X)\) such that'
edit(old,old[2:],'D23','Remove a stray TeX control-space at the start of the statement.')
old=r'''whereas \(h^0(X,\mathcal O_X)=1\).  Rescale the additive coordinate in
\SeriesRef{inv:C3.1} so that'''
new=r'''whereas \(h^0(X,\mathcal O_X)=1\). Write \(M_u=\exp(ug)\) for the
additive Picard isomorphism of \SeriesRef{inv:C3.1}. There is a unique
\(u_0\ne0\) with \(M_{u_0}=f^*\mathcal O_B(1)\). The complex-linear
isomorphism
\[
 \phi:\mathbb C\longrightarrow\mathbb C,\qquad
 \phi(z)=u_0z/12,\qquad \phi^{-1}(u)=12u/u_0
\]
defines \(L_z=M_{\phi(z)}\). On a fibre \(F_q\), put
\(\iota_q(z)=(u_0z/12)g|_{F_q}\); its exponential is \(L_z|_{F_q}\).
Multiplication by the nonzero scalar \(u_0/12\) preserves the image
line \(\mathbb C\gamma^{0,1}\) of the restriction map. Thus'''
edit(old,new,'D20/D22','Replace the coordinate-rescaling instruction by its exact complex-linear isomorphism, inverse and induced restriction map. Nontriviality of f*O(1) proves u0 is nonzero. The Picard family, its restriction image and L12=f*O(1) are transported explicitly.')
old=r'''\SeriesRef{inv:A1.0}, \CompendiumRef{I}{mapsI:top:thm:p0-integral-specialization} and \SeriesRef{inv:C3.1}, restriction'''
new=r'''\SeriesRef{inv:C3.1}, restriction'''
edit(old,new,'D06','Use the current Paper I proposition that states and proves injectivity on every full scheme fibre. Its exact Cartier sequence and Leray edge map identify the same H1(O_X) restriction map; the original compendium references are archived in the ownership map.')
old=r'''\CompendiumRef{I}{wb:ffcert:thm:normal-trivialization} says that
\[
 L_{12/m_j}|_{S_j}=\mathcal O_X(S_j)|_{S_j}
\]
is nontrivial.'''
new=r'''the root model of \SeriesRef{fam:src:A.1.2} identifies
\(\mathcal N_j:=\mathcal O_X(S_j)|_{S_j}\) with the normal line of
the reduced fibre. Its connected degree-\(m_j\) cover
\(\widehat S_j\to S_j\) has free deck generator \(a_j\). In the
root coordinate \(s_j\), the generator acts by
\(s_j\mapsto\zeta_j s_j\), with \(\zeta_j\) primitive of order
\(m_j\). The derivative therefore identifies the line with
\[
 \mathcal N_j\simeq
 (\widehat S_j\times\mathbb C)/
       ((x,v)\sim(a_jx,\zeta_jv)).
\]
A trivializing section of \(\mathcal N_j^{\otimes r}\) pulls back
to a nowhere-zero holomorphic function \(h\) on the compact connected
torus \(\widehat S_j\), with \(h(a_jx)=\zeta_j^r h(x)\).
The function is constant, so \(m_j\mid r\). Conversely the constant
section descends for \(r=m_j\); hence the order is exactly \(m_j\).
In particular,
\[
 L_{12/m_j}|_{S_j}=\mathcal N_j\ne\mathcal O_{S_j}.
\]'''
edit(old,new,'D06/D22','Replace the unresolved compendium normal-order reference by the explicit quotient normal line from the current Paper I root model. The derivative character and pullback of a trivializing section prove the precise order; both maps concern the same reduced fibre and its actual connected root cover.')
edit(remark,'','D01/D12','Remove the production-history remark after moving its identity to its mathematical owner. Its entire text and four claim-to-proof mappings remain in the records; no independent proof event is assigned to the retired remark.')
# The outer enumeration is the exact unchanged proof wrapper in this block.
new_end=s.index(r'\end{proof}',s.index(r'\begin{theorem}[Uniform non-torsion]'))+len(r'\end{proof}')
start=s.index(r'\begin{theorem}[Uniform non-torsion]');block=s[start:new_end]
old=r'\begin{enumerate}[label={$\langle1\rangle$\arabic*.},leftmargin=*]'
assert block.count(old)==1
pos=s.index(block)+block.index(old);guard=s[pos-100:pos+len(old)+100]
edit(guard,guard.replace(old,r'\begin{enumerate}[label=\arabic*.,leftmargin=*]'),'D04/D23','Replace the iteration marker by ordinary step numbering without changing the seven proof items.')
start=s.index(r'\begin{theorem}[Uniform non-torsion]');end=s.index(r'\end{proof}',start)+len(r'\end{proof}')
proposed=s[start:end]
(O/'original_theorem_and_remark.tex').write_text(original)
(O/'proposed_theorem.tex').write_text(proposed)
(O/'retired_remark.tex').write_text(remark)
permutations={};moved={'labels':['inv:wb:uniform-nontorsion-provenance'],'targets':['tag-01TQ']}
for kind,pat in [('labels',r'\\label\{([^}]+)\}'),('targets',r'\\hypertarget\{([^}]+)\}')]:
    b=re.findall(pat,before);c=re.findall(pat,s);assert Counter(b)==Counter(c)
    assert [x for x in b if x not in moved[kind]]==[x for x in c if x not in moved[kind]]
    positions=defaultdict(deque)
    for i,ident in enumerate(c):positions[ident].append(i)
    permutations[kind]=[dict(identity=ident,before_index=i,after_index=positions[ident].popleft()) for i,ident in enumerate(b)]
    assert sorted(x['after_index'] for x in permutations[kind])==list(range(len(c)))
mapping=[
    dict(claim='The period equation and countability argument',owner='wb:thm:uniform-nontorsion-audit',scope='Steps 3–5, equation inv:wb:eq:9.25 and the same marked lattice classes; all these mathematical sentences remain unchanged.'),
    dict(claim='The exact normal-character order on S_j',owner='wb:thm:uniform-nontorsion-audit',scope='Step 7 now gives the derivative-character quotient and both directions of the order argument explicitly, using the actual root cover of I fam:src:A.1.2. Original compendium input wb:ffcert:thm:normal-trivialization is archived as a historical locator.'),
    dict(claim='Extension to the cusp and full special fibres',owner='inv:C3.1 in current Paper I; step 6 here',scope='The same cohomological restriction H1(O_X)→H1(O_Xb) is injective by the current I Cartier-sequence/Leray proof. The old intrinsic integral-specialization input mapsI:top:thm:p0-integral-specialization remains a historical source claim, not a separately restated result here.'),
    dict(claim='Identification with the global gamma^(0,1) summand',owner='inv:C3.1 in current Paper I; steps 1–3 here',scope='The exact coordinate isomorphism phi(z)=u0*z/12 has inverse12*u/u0, and restriction sends z to (u0*z/12)g|F. Its nonzero scalar preserves the same coherent image line C*gamma^(0,1).')]
g=dict(paper='II',created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),source_before_sha256=sha(before),source_after_sha256=sha(s),patches=edits,
       identity_permutations=permutations,moved_labels=moved['labels'],moved_targets=moved['targets'],claim_owner_map=mapping,
       original_full_block=dict(path=str((O/'original_theorem_and_remark.tex').relative_to(R)),sha256=sha(original)),
       proposed_full_block=dict(path=str((O/'proposed_theorem.tex').relative_to(R)),sha256=sha(proposed)),
       actual_pair_rereading_pending=True,mathematical_events_added=0,visual_reading_credit=0)
(O/'guard.json').write_text(json.dumps(g,indent=2)+'\n')
print(json.dumps(dict(guard=str((O/'guard.json').relative_to(R)),guard_sha256=sha((O/'guard.json').read_bytes()),source_after_sha256=sha(s),patches=len(edits),label_occurrences=len(permutations['labels']),target_occurrences=len(permutations['targets']),proposed_bytes=len(proposed.encode())),indent=2))
