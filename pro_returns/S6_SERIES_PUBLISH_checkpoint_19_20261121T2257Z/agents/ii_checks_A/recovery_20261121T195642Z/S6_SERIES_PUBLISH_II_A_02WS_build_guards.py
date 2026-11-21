from pathlib import Path
import datetime,hashlib,json,re
ROOT=Path('/workspace/scratch/08a92fb2355d/S6_SERIES_PUBLISH')
R=ROOT/'agents/ii_checks_A/recovery_20261121T195642Z'
O=R/'group06_WS';O.mkdir(exist_ok=True)
p=ROOT/'agents/ii_infra/released_proofs/02WS/47e4d167fef4b8cc/S6_SERIES_PUBLISH_full_owning_block.tex'
old=p.read_text();new=old;guards=[]
h=lambda s:hashlib.sha256(s.encode()).hexdigest()
rel=lambda p:str(p.relative_to(ROOT))
def edit(a,b,types,reason,transport):
 global new
 assert new.count(a)==1,(a,new.count(a))
 after=new.replace(a,b,1)
 guards.append(dict(tag='02WS',guard_id=f'A_REC_WS_{len(guards)+1:03}',defect_types=types,literal_old=a,literal_new=b,reason=reason,mathematical_transport=transport,offset_before=new.index(a),intermediate_before_sha256=h(new),intermediate_after_sha256=h(after),full_original_path=rel(O/'S6_SERIES_PUBLISH_II_02WS_full_original.tex'),full_proposed_path=rel(O/'S6_SERIES_PUBLISH_II_02WS_full_proposed.tex')))
 new=after

edit('[P4.20]','[Ordinary double strata and normal crossings]',['D04','D16'],
 'Give the statement a mathematical title.','Identical local normalization and transverse-type hypotheses, with the same normal-crossing conclusion.')
edit('Let $mS$ be an irreducible fibre of a proper holomorphic\ndegeneration',
 'Let $mS$ be a fibre with irreducible reduced support $S$ in a proper\nholomorphic degeneration',['D20'],
 'Name the irreducible reduced support and the full scheme multiplicity.',
 'The same normalization of S and the same full fibre mS; the local base function remains a unit times g^m.')
edit('In the global setting of 4.2, P4.6--P4.8 apply to this subclass.',
 'Propositions~\\ref{night:P4.6}--\\ref{night:P4.8} apply to\nfibrations in the standing compact setting whose reduced supports\nall satisfy these local hypotheses or already have normal crossings.', ['D04','D05','D20','D22'],
 'Resolve the references and state the all-supports receiving scope explicitly.',
 'Each support in the indicated fibration is normal crossing by this proposition or its given hypothesis, so the unchanged hypotheses of P4.6-P4.8 hold. No conclusion about another arbitrary fibre is inferred from one local support.')
edit('\\item We give the boundary and transport arguments explicitly.\nTake a small ball $B$ around an exceptional point, with\nboundary transverse to the smooth and double strata away\nfrom that point. Let $g$ be a reduced equation. An analytic\n$m$-th root of the unit in the actual defining function lets\nus write that function as $g^m$.',
 '\\item Take a small ball $B$ around an exceptional point, with\nboundary transverse to the smooth and double strata away\nfrom that point. Write the local defining function as $a g_0^m$,\nwhere $g_0$ is reduced and $a$ is a unit. Choose a holomorphic\nroot $h^m=a$ and set $g=h g_0$. The local defining function\nis then $g^m$.', ['D08','D20','D22'],
 'Give the exact unit multiplication and remove the process introduction.',
 'The reduced zero divisor is unchanged under g=h g0, and the fibre g=delta embeds in the original fibre of value delta^m.')
edit('the\nverified boundary submersion, identifies',
 'the\nboundary submersion from the preceding step, identifies', ['D08'],
 'Reference the established mathematical property directly.', 'The same restriction G_s|boundary B and same proper Ehresmann transport.')
edit('Its inclusion in the actual torus fibre is impossible.',
 'Its inclusion in the compact torus fibre is impossible.', ['D08'],
 'Name the compact receiving fibre.', 'The same holomorphic open inclusion into the smooth fibre of value t0^m.')
a=new.index('\\item At a normalization preimage');b=new.index('\\item Each transverse rank-one point',a)
edit(new[a:b],r'''\item At a normalization preimage write the map germ as
$\phi:(\mathbb C^2,0)\to(\mathbb C^3,0)$.
Away from the exceptional point it is immersive with transverse
multiple images. The isolated-instability criterion in
\cite[p.~5]{GCP2024} makes this monogerm finitely determined.
Write $I_2(d\phi)$ for the ideal of its maximal minors.
A rank drop gives a nonempty finite scheme, and
\cite[Lemma~2.3, p.~5]{GCP2024} identifies its positive length
\[
 C(\phi)=\dim_{\mathbb C}\mathbb C\{u,v\}/I_2(d\phi)
\]
with the number of cross-caps in a stable deformation.
Apply this formula separately at each normalization preimage.
Generic polynomial perturbations vary the branch jets independently.
The stable multigerms listed in \cite[p.~4]{GCP2024} place each
cross-cap on a single sheet. Concretely, the incidence of its
zero-dimensional critical set with another two-dimensional image
in the three-dimensional target has negative expected dimension;
generic relative perturbations avoid it.

''', ['D17','D18','D22'],
 'Use the opened exact primary length formula, with its monogerm scope and the receiving branch separation stated.',
 'I2(dphi) is the original maximal-minor ideal. Lemma 2.3 gives the same positive conserved cross-cap number; it is applied separately to the smooth normalization branches. The complete original Hilbert-Burch and genericity steps are checked in the comparison record.')
edit('\\item Each transverse rank-one point is a Whitney crosscap, as we\nnow verify. Choose its first target coordinate as a source',
 '\\item For the cross-cap coordinates, choose the first target\ncoordinate at a transverse rank-one point as a source', ['D08'],
 'Introduce the coordinate construction directly.',
 'The following source and target biholomorphisms remain exactly those in the original proof.')
edit('Its image is the crosscap of P4.16, with a compact spherical\nclass of square $-4$ in its nearby fibre.',
 'The target coordinate permutation $(x,y,z)=(uv,u,v^2)$ gives\n$x^2-zy^2=0$. Proposition~\\ref{night:P4.16}, with $n=2$,\ngives a compact spherical class of square $-4$ in its nearby fibre.', ['D04','D20','D22'],
 'Resolve the cited case and display the exact coordinate permutation.',
 'The Whitney map (u,v)->(u,v^2,uv) is transported by (X,Y,Z)->(Z,X,Y) to (uv,u,v^2), whose reduced image equation is x^2-zy^2.')
edit('the boundary property already proved. Transporting the',
 'the boundary property above; compare the stable-image discussion\nin \\cite[\\S5.3, p.~33]{GCP2024}. Transporting the', ['D17','D18'],
 'Move the adjacent primary locator into the precise proof use.',
 'The opened source discusses the stable-deformation nearby-fibre comparison; the present proof gives the exact boundary argument for its branch-image deformation.')

op=O/'S6_SERIES_PUBLISH_II_02WS_full_original.tex';np=O/'S6_SERIES_PUBLISH_II_02WS_full_proposed.tex';op.write_text(old);np.write_text(new)
anchors=lambda t:re.findall(r'\\(?:hypertarget|label)\{[^}]*\}',t)
assert anchors(old)==anchors(new)
manifest=dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),checker='ii_check_a',canonical_writes=False,guards=guards,blocks=[dict(tag='02WS',original_path=rel(op),original_sha256=h(old),proposed_path=rel(np),proposed_sha256=h(new),original_characters=len(old),proposed_characters=len(new),guards=[g['guard_id'] for g in guards],anchors_exact=True)],note='Enumeration wrapper remains for the root-owned global mapping. The next source-location paragraph is not owned by this proposal.')
mp=O/'S6_SERIES_PUBLISH_II_A_02WS_editorial_proposals.json';mp.write_text(json.dumps(manifest,indent=2)+'\n')

orphan=r'''The rank-one count is also stated in Gim\'enez Conejero--Pint\'er,
arXiv:2401.14951v2, Lemma 2.3; Section 5.3, p.~33,
discusses the stable-image/nearby-fibre comparison.
The proof above verifies the boundary transport required here.
It does not extend that argument to cuspidal, tacnodal or
triple-curve transverse types.
'''
canonical=(ROOT/'S6_SERIES_PUBLISH_II.tex').read_text();assert canonical.count(orphan)==1
data=dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),source_sha256=h(canonical),literal_old=orphan,literal_new='',defect_types=['D02','D08','D11','D13','D18'],reason='The exact primary citations have moved into the owning proof. The ordinary-double hypothesis already states the transverse-type scope.',receiving_block=rel(np),receiving_block_sha256=h(new),broader_source_location_paragraph_untouched=True)
(O/'S6_SERIES_PUBLISH_II_A_02WS_adjacent_citation_guard.json').write_text(json.dumps(data,indent=2)+'\n')
bib=r'''\bibitem[Gim\'enez Conejero and Pint\'er(2024)]{GCP2024}
Roberto Gim\'enez Conejero and Gerg\H{o} Pint\'er.
\newblock Signature of the Milnor fiber of parametrized surfaces.
\newblock arXiv:2401.14951v2, 30 January 2024.
\newblock URL \url{https://arxiv.org/abs/2401.14951v2}.

'''
(O/'S6_SERIES_PUBLISH_II_A_02WS_bibliography_entry.tex').write_text(bib)
print(json.dumps(dict(manifest=rel(mp),sha256=h(mp.read_text()),guard_count=len(guards),proposed_sha256=h(new)),indent=2))
