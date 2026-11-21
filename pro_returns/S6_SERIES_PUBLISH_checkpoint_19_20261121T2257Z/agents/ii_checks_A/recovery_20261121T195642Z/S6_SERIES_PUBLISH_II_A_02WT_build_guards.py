from pathlib import Path
import datetime, hashlib, json, re
ROOT=Path('/workspace/scratch/08a92fb2355d/S6_SERIES_PUBLISH')
R=ROOT/'agents/ii_checks_A/recovery_20261121T195642Z'
O=R/'group07_WT'; O.mkdir(exist_ok=True)
source=ROOT/'agents/ii_infra/released_proofs/02WT/4ec836de6b7b601c/S6_SERIES_PUBLISH_full_owning_block.tex'
old=source.read_text(); new=old; guards=[]
h=lambda s:hashlib.sha256(s.encode()).hexdigest()
rel=lambda p:str(p.relative_to(ROOT))
def edit(a,b,types,reason,transport):
    global new
    assert new.count(a)==1,(a,new.count(a))
    after=new.replace(a,b,1)
    guards.append(dict(tag='02WT',guard_id=f'A_REC_WT_{len(guards)+1:03}',
        defect_types=types,literal_old=a,literal_new=b,reason=reason,
        mathematical_transport=transport,offset_before=new.index(a),
        intermediate_before_sha256=h(new),intermediate_after_sha256=h(after),
        full_original_path=rel(O/'S6_SERIES_PUBLISH_II_02WT_full_original.tex'),
        full_proposed_path=rel(O/'S6_SERIES_PUBLISH_II_02WT_full_proposed.tex')))
    new=after

edit('[P4.21]','[Positive Euler number for rational normalization]',
     ['D04','D16'],'Give the proposition a mathematical title.',
     'The same irreducible singular support S and smooth rational normalization T; the strict inequality is unchanged.')
edit(r'\SeriesRef{night:P4.12}, \SeriesRef{night:P4.13}, \SeriesRef{night:P4.20}, \SeriesRef{night:P4.6}, \SeriesRef{night:P4.8}, \SeriesRef{night:P4R.1}, \SeriesRef{night:P4R.3}',
     r'\SeriesRef{cdp:st:A.5.3}, \SeriesRef{night:P4.12}, \SeriesRef{night:P4.13}, \SeriesRef{night:P4.20}, \SeriesRef{night:P4.6}, \SeriesRef{night:P4R.1}',
     ['D04','D06'],'Align the hidden dependency list with the explicit proof uses.',
     'The local conductor formula uses A.5.3 with identity resolution of T; the single-support calculation replaces the all-supports P4.8 application, and the pushout is established directly.')
edit('In the standing torus-fibration setting of this section, an irreducible singular support $S$\nwith smooth rational normalization $T$ has $e(S)>0$.',
     'Let $f:Y\\to B$ be a proper surjective holomorphic map with connected\n'
     'fibres from a smooth compact complex threefold with $b_1(Y)=b_2(Y)=0$\n'
     'to a smooth compact curve, with smooth general fibre a complex two-torus.\n'
     'Let $mS$ be a fibre with irreducible singular reduced support, and let\n'
     '$\\nu:T\\to S$ be its smooth rational normalization. Then $e(S)>0$.',
     ['D20','D22'],'State the full receiving hypotheses and the normalization morphism.',
     'This is exactly the standing compact torus-fibration setting supplied in the safe scope packet; S is the reduced support and mS the same full fibre.')
a=new.index('\\item Let $D$ be the conductor divisor'); b=new.index('\\item We give the complete minimal-surface case split.',a)
edit(new[a:b],r'''\item Let $D$ be the conductor divisor on $T$, with its scheme
multiplicities, and put $C=\operatorname{Sing}(S)_{\mathrm{red}}$.
Propositions~\ref{cdp:st:A.5.3} and~\ref{night:P4.12} give
$\omega_T(D)\simeq\nu^*\omega_S$, a torsion line bundle.
The minimal resolution in the first proposition is the identity of the
smooth surface $T$. Pullback to a common point-blowup resolution of
$T$ and $\mathbb P^2$ injects $\operatorname{Pic}(T)$ into a free
abelian Picard group; see \cite[II.3, pp.~17--18; II.12, p.~24]{Beauville1978}.
Thus $D\sim-K_T$. Contract $T$ to a minimal rational surface $T_0$,
which is $\mathbb P^2$ or a Hirzebruch surface $\mathbb F_n$ with
$n\ne1$ \cite[V.10, pp.~79--80]{Beauville1978}, and push $D$ forward
to $D_0$. For each reversed point blowup $q$ with exceptional curve $E$,
the canonical formula $K_{\mathrm{new}}=q^*K_{\mathrm{old}}+E$
gives $D_{\mathrm{new}}=q^*D_{\mathrm{old}}-E$.
Its exceptional coefficient is $\mu-1$, where $\mu$ is the
conductor multiplicity at the centre. Effectivity therefore puts
every centre on the conductor.

''',['D04','D06','D17','D18','D22'],
     'Give the exact conductor map, torsion-to-triviality step, primary minimal models and blowup coefficient.',
     'A.5.3 uses h=nu and the identity minimal resolution; the pullback Picard injection gives D=-K linearly. The proper blowdown sends D to D0, and K_new=q*K_old+E gives the same coefficient mu-1 at every reversed blowup.')
edit('\\item We give the complete minimal-surface case split. On\n$\\mathbb P^2$, the divisor $D_0$ is a plane cubic.',
     '\\item On $\\mathbb P^2$, the divisor $D_0$ is a plane cubic.',
     ['D08'],'Introduce the first minimal model directly.',
     'The complete cubic classification and all subsequent incidence cases remain unchanged.')
edit('\\item On a Hirzebruch surface, write $F$ for a ruling fibre.\nSince $D_0\\cdot F=2$, its horizontal part is a double',
     '\\item On $\\mathbb F_n$, write $h$ for the tautological class\n'
     'and $F$ for a ruling fibre. The formulas\n'
     '$h^2=n$, $h\\cdot F=1$, $F^2=0$, and\n'
     '$K_{\\mathbb F_n}=-2h+(n-2)F$ are\n'
     '\\cite[III.18, pp.~46--47; IV.1, pp.~53--54]{Beauville1978}.\n'
     'Thus $D_0\\cdot F=2$, and its horizontal part is a double',
     ['D17','D18','D22'],'Bind the ruled intersection basis and canonical formula to the opened primary edition.',
     'The h,F basis is the monograph’s tautological/fibre basis; adjunction on F fixes the h coefficient at -2 and adjunction on a section fixes n-2. All printed section and bisection equations follow in this same basis.')
edit('Consequently $S$ has ordinary\ndouble curves outside finitely many points. P4.20 makes\n$S$ normal crossing everywhere, and P4.6--P4.8 give\n$e(S)=2$ for this rational normalization.',
     r'''Consequently $S$ has ordinary double curves outside finitely
many points. Proposition~\ref{night:P4.20} makes $S$ normal crossing
everywhere. Write $t$ for its number of ordinary triple points.
On each normal-crossing chart the composite $T\to S\subset Y$
is the inclusion of a smooth coordinate plane, hence is immersive.
The exact sequence
\[
0\longrightarrow T_T\longrightarrow\nu^*(T_Y|_S)
 \longrightarrow L\longrightarrow0
\]
has line quotient. Since $H^2(Y,\mathbb Q)=H^4(Y,\mathbb Q)=0$,
the pulled-back first and second Chern classes vanish. Thus
$c_1(L)=K_T$ and $e(T)=K_T^2$. Rationality gives
$\chi(\OO_T)=1$ \cite[III.20--21, pp.~48--50]{Beauville1978};
Noether's formula therefore gives $e(T)=6$.
The reduced nodal anticanonical conductor is either smooth elliptic
or a cycle of rational curves. Adjunction on a rational component
gives exactly two node preimages. Its number of components therefore
equals its number of nodes, and its Euler number equals that number;
the smooth elliptic case has Euler number zero and no nodes. Every triple point
of $S$ has three node preimages on $D$, so $e(D)=3t$.
Over the smooth part of $C$ the conductor has two points per fibre,
whereas a triple point has three. Hence
\[
e(D)=2e(C\setminus\{\text{triple points}\})+3t
     =2e(C)+t,
\]
and $e(C)=t$. Additivity gives $e(S)=6-2t$.
Proposition~\ref{night:P4.6}, applied to this reduced divisor $S$,
gives $e(S)=t$. Therefore $t=2$ and $e(S)=2$.''',
     ['D04','D25'],'Prove the stronger normal-crossing value in the exact single-support scope.',
     'P4.8’s all-supports normal-crossing hypothesis is not established for the other fibres. The replacement uses the identical maps T->S->Y, conductor D->C, and the single-divisor P4.6. Each triple point has three nodes above it; the generic conductor degree is two. These give eD=3t=2eC+t and eS=6-2t=t, preserving eS=2.')
edit('The conductor pushout verified in P4R.3\ngives',
     'Triangulate the analytic pair $(T,D_{\\mathrm{red}})$ and the finite\n'
     'map $D_{\\mathrm{red}}\\to C$. The inclusion is a cofibration, so\n'
     'its pushout has the fundamental group of the corresponding mapping\n'
     'cylinder. Van Kampen gives',
     ['D04','D06','D22'],'Supply the conductor-pushout map directly in this rational setting.',
     'The quotient identifies only points in D_red having the same image in C; compactness gives the same topological space S. The connected rational surface T is simply connected by the point-blowup common-resolution map, and D_red is connected and simply connected in this case.')
edit('P4R.1 makes\n$\\pi_1(C)$ virtually abelian.',
     'Proposition~\\ref{night:P4R.1} makes\n$\\pi_1(C)$ virtually abelian.',
     ['D04'],'Resolve the virtually abelian input.',
     'The exact group pi1(S)=pi1(C) receives the abelian normal subgroup with finite cyclic quotient of order dividing the same multiplicity m.')
edit('P4.13 gives $e(S_{\\mathrm{reg}})\\ge0$.',
     'Proposition~\\ref{night:P4.13} gives $e(S_{\\mathrm{reg}})\\ge0$.',
     ['D04'],'Resolve the smooth-locus Euler input.',
     'The same proper local torus degeneration around the full fibre mS satisfies P4.13, and T minus D_red identifies with S_reg.')

op=O/'S6_SERIES_PUBLISH_II_02WT_full_original.tex';np=O/'S6_SERIES_PUBLISH_II_02WT_full_proposed.tex'
op.write_text(old);np.write_text(new)
anchors=lambda t:re.findall(r'\\(?:hypertarget|label)\{[^}]*\}',t)
assert anchors(old)==anchors(new)
manifest=dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
    checker='ii_check_a',canonical_writes=False,guards=guards,
    blocks=[dict(tag='02WT',original_path=rel(op),original_sha256=h(old),
      proposed_path=rel(np),proposed_sha256=h(new),original_characters=len(old),
      proposed_characters=len(new),guards=[g['guard_id'] for g in guards],anchors_exact=True)],
    note='Complete original seven-step proof preserved, with exact receiving-scope repairs. Enumeration wrapper remains for the root-owned global map.')
mp=O/'S6_SERIES_PUBLISH_II_A_02WT_editorial_proposals.json';mp.write_text(json.dumps(manifest,indent=2)+'\n')
bib=r'''\bibitem[Beauville(1978)]{Beauville1978}
Arnaud Beauville.
\newblock \emph{Surfaces alg\'ebriques complexes}.
\newblock Ast\'erisque, volume 54. Soci\'et\'e math\'ematique de France, 1978.
\newblock URL \url{https://www.numdam.org/item/AST_1978__54__R1_0/}.

'''
(O/'S6_SERIES_PUBLISH_II_A_02WT_bibliography_entry.tex').write_text(bib)
print(json.dumps(dict(manifest=rel(mp),sha256=h(mp.read_text()),guard_count=len(guards),
                     proposed_sha256=h(new)),indent=2))
