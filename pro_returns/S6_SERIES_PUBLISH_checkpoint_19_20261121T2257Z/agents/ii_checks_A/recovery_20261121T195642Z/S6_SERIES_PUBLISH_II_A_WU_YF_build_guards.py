from pathlib import Path
import datetime,hashlib,json,re
ROOT=Path('/workspace/scratch/08a92fb2355d/S6_SERIES_PUBLISH')
R=ROOT/'agents/ii_checks_A/recovery_20261121T195642Z';O=R/'group08_WU_YF';O.mkdir(exist_ok=True)
h=lambda s:hashlib.sha256(s.encode()).hexdigest()
rel=lambda p:str(p.relative_to(ROOT))
sources={'02WU':'668d97539b684d0d','02YF':'f9f16d06e9d694ee'}
allguards=[];blocks=[]
for tag,receipt in sources.items():
    p=ROOT/f'agents/ii_infra/released_proofs/{tag}/{receipt}/S6_SERIES_PUBLISH_full_owning_block.tex'
    old=p.read_text();new=old;guards=[]
    def edit(a,b,types,reason,transport):
        global new
        assert new.count(a)==1,(tag,a,new.count(a))
        after=new.replace(a,b,1)
        guards.append(dict(tag=tag,guard_id=f'A_REC_{tag}_{len(guards)+1:03}',
            defect_types=types,literal_old=a,literal_new=b,reason=reason,
            mathematical_transport=transport,offset_before=new.index(a),
            intermediate_before_sha256=h(new),intermediate_after_sha256=h(after),
            full_original_path=rel(O/f'S6_SERIES_PUBLISH_II_{tag}_full_original.tex'),
            full_proposed_path=rel(O/f'S6_SERIES_PUBLISH_II_{tag}_full_proposed.tex')))
        new=after
    if tag=='02WU':
        edit('[P4.22]','[Euler number of an elliptic-ruled normalization]',
             ['D04','D16'],'Give the proposition a mathematical title.',
             'Identical standing compact fibration, irreducible singular support, smooth elliptic-ruled normalization and equality criterion.')
        edit(r'\SeriesRef{night:P4.13}, \SeriesRef{night:P4.15}, \SeriesRef{night:P4R.1}, \SeriesRef{night:P4R.3}',
             r'\SeriesRef{cdp:st:A.5.3}, \SeriesRef{night:P4.12}, \SeriesRef{night:P4.13}, \SeriesRef{night:P4.15}, \SeriesRef{night:P4R.1}, \SeriesRef{night:P4R.3}',
             ['D06'],'Record the exact conductor and torsion-line inputs.',
             'The A.5.3 minimal resolution is the identity of the smooth normalization T; its map h is nu.')
        edit('\\item Push the effective conductor to the minimal ruled\nsurface $T_0\\to B$, where $B$ is elliptic. We have\n$K_{T_0}+D_0\\equiv0$.',
             r'''\item Write $\nu:T\to S$ for normalization, $D$ for its full
conductor divisor, and $C=\operatorname{Sing}(S)_{\mathrm{red}}$.
Propositions~\ref{cdp:st:A.5.3} and~\ref{night:P4.12}, with the
identity as the resolution of $T$, give the torsion line
$\omega_T(D)\simeq\nu^*\omega_S$.
Push $D$ to the minimal ruled surface $T_0\to E$, where $E$ is
elliptic. The projective-bundle and canonical formulas are
\cite[III.10, p.~40; III.18, pp.~46--47]{Beauville1978}.
They give $K_{T_0}+D_0\equiv0$ and $D_0\cdot F=2$ for a fibre $F$.''',
             ['D06','D17','D18','D20','D22'],'Define the conductor image and bind the ruled and canonical maps.',
             'The original elliptic ruling base B is renamed E to separate it from the base of the threefold fibration. The blowdown sends D to D0 and the same divisor has degree two on the ruling fibre.')
        edit('whereas its nonconstant map to $B$ gives geometric',
             'whereas its nonconstant map to $E$ gives geometric',
             ['D20'],'Use the declared ruling-base notation.',
             'Identity renaming of the elliptic ruling curve B to E and its same finite horizontal-curve map.')
        edit('The normalization differential\nhas no divisorial rank drop. P4.15 makes $T$ minimal,',
             r'''The coefficient-one branch conductors give two smooth
transverse branches at a general point of each image curve:
the sum of the branch exponents is $2\delta$, while
$\delta\ge q-1$ for $q$ branches, so $q=2$ and $\delta=1$.
Thus the normalization differential has no divisorial rank drop;
its analytic rank-drop locus is finite.
Proposition~\ref{night:P4.15} makes $T$ minimal,''',
             ['D04','D22'],'Justify the finite-rank-drop hypothesis before applying its numerical result.',
             'The generic conductor exponents of the same normalization are all one. The exact conductor-length identity implies the ordinary-double type, and compactness turns the zero-dimensional rank locus into a finite scheme.')
        a=new.index('where $H$ is a smooth elliptic section. As in P4R.3,')
        b=new.index('\\item If $e(S)=0$',a)
        edit(new[a:b],r'''where $H$ is a smooth elliptic section. The canonical blowup
formula in \cite[II.3, pp.~17--18]{Beauville1978}, together with
$K+D\equiv0$, gives conductor coefficient $\mu-1$ on the exceptional
curve. These blowups make $D_{\mathrm{red}}$ a copy of $H$ with rational trees attached:
a smooth-point blowup adds a leaf or no conductor component,
and a node blowup subdivides an edge. Collapsing those rational
trees induces an isomorphism to $\pi_1(H)$. The section
$H\to T_0$ is inverse on fundamental groups to $T_0\to E$,
and every point blowup preserves this inclusion map. Hence
$\pi_1(D_{\mathrm{red}})\to\pi_1(T)$ is an isomorphism.
Apply the finite-normalization pushout and curve-graph calculation
in the proof of Proposition~\ref{night:P4R.3} to the inclusion
$D_{\mathrm{red}}\subset T$ and the finite map
$D_{\mathrm{red}}\to C$. Their pushout is $S$, so
$\pi_1(S)\simeq\pi_1(C)$.
Proposition~\ref{night:P4R.1} makes this group virtually abelian.
Every rational conductor component has rationally normalized image;
only $H$ can dominate an elliptically normalized component.
The curve-graph formula gives $e(C)\ge0$.
Proposition~\ref{night:P4.13} and additivity therefore give $e(S)\ge0$.

''',['D04','D06','D17','D18','D22'],
             'Transport the higher-genus proof arguments through the exact elliptic section and conductor maps.',
             'The cited P4R.3 proof constructs its pushout and graph formula from a connected conductor inclusion inducing a pi1 isomorphism. Those maps are proved here for the genus-one ruling, so its general topological argument applies without asserting the higher-genus statement for this surface.')
        edit('P4.13 forces $v=0$, hence $D=2H$.',
             'Proposition~\\ref{night:P4.13} forces $v=0$, hence $D=2H$.',
             ['D04'],'Resolve the open-stratum sign input.',
             'The same full fibre mS and the normalization complement T minus D_red give the displayed Euler value -v.')
        edit('so its rank-drop set is finite. P4.15\napplies and again gives $e(S)=0$.',
             'so its rank-drop set is finite. Proposition~\\ref{night:P4.15}\napplies and gives $e(S)=0$.',
             ['D04','D08'],'Resolve the finite-rank-drop input and state its conclusion directly.',
             'In the tacnode and ordinary-triple cases the normalization is immersive at the generic point of the sole conductor curve H; all remaining rank drops are isolated, exactly the cited hypothesis.')
    else:
        edit('[P4R.3]','[Conductor topology over a higher-genus ruling]',
             ['D04','D16'],'Give the proposition a mathematical title.',
             'Identical genus-g>=2 normalization, conductor inclusion and pushout isomorphisms, and Euler inequalities; repeated component images remain explicitly allowed.')
        edit(r'\SeriesRef{night:P4.12}, \SeriesRef{night:P4.13}, \SeriesRef{night:P4R.1}, \SeriesRef{night:P4R.2}',
             r'\SeriesRef{cdp:st:A.5.3}, \SeriesRef{night:P4.12}, \SeriesRef{night:P4.13}, \SeriesRef{night:P4R.1}',
             ['D06'],'Align the exact conductor input and self-contained topological arguments.',
             'The conductor formula is A.5.3 with identity resolution; point-blowup and surface-group arguments are stated directly below, so no P4R.2 conclusion is imported.')
        edit('\\item The canonical comparison of P4.12 gives\n$K_T+D\\equiv0$, with $D$ effective. We first determine the\nreduced conductor as an embedded topological space; this\nstep does not require the ruling to descend to $S$.\nLet $\\pi:T\\to T_0$ be the sequence of point blowdowns to\nthe minimal ruled surface $r_0:T_0\\to B$, and put\n$D_0=\\pi_*D$. Then $K_{T_0}+D_0\\equiv0$ and\n$D_0\\cdot F=2$ for a ruling fibre $F$.',
             r'''\item Proposition~\ref{cdp:st:A.5.3}, with the identity as the
minimal resolution of the smooth surface $T$, gives
$\omega_T(D)\simeq\nu^*\omega_S$ with $D$ effective and with its
conductor multiplicities. Proposition~\ref{night:P4.12} makes this
line torsion, so $K_T+D\equiv0$.
Let $\pi:T\to T_0$ be the sequence of point blowdowns to the
minimal ruled surface $r_0:T_0\to B$, and put $D_0=\pi_*D$.
By \cite[III.10, p.~40]{Beauville1978}, write $T_0=\mathbf P_B(V)$
for a rank-two bundle $V$ on $B$. In the basis of the tautological
class $h=c_1(\OO_{\mathbf P_B(V)}(1))$ and the fibre class $F$,
$h^2=\deg V$, $h\cdot F=1$, $F^2=0$ and
$K_{T_0}=-2h+(\deg V+2g-2)F$
\cite[III.18, pp.~46--47]{Beauville1978}.
Thus $K_{T_0}+D_0\equiv0$ and $D_0\cdot F=2$.''',
             ['D02','D04','D06','D08','D17','D18','D22'],
             'Give the exact conductor and ruled-surface formulas in the opened primary basis.',
             'The resolution is the identity, h=nu; pi pushes the effective conductor to D0. The projective-bundle basis has K.F=-2 and fixes the degree-two horizontal part. No descent morphism from S to the ruling base is introduced.')
        edit("let $\\mu$ be the multiplicity of the current conductor\n$D''$ at the centre and $E$ the exceptional curve.",
             "let $\\mu$ be the multiplicity of the conductor $D''$ at the\ncentre and $E$ the exceptional curve.",
             ['D08'],'Name the stage divisor directly.',
             'The same divisor D-double-prime on the same blowup target, with the same centre and multiplicity mu.')
        edit('The canonical blowup\nformula gives',
             'The canonical blowup formula\n\\cite[II.3(iv), pp.~17--18]{Beauville1978} gives',
             ['D17','D18'],'Attach the exact primary blowup formula.',
             'The monograph’s blowup map e is beta:T-prime->T-double-prime here, with the identical exceptional divisor E and K-prime=beta*K+E.')
        edit('A point blowup leaves\n$\\pi_1(T)$ unchanged, as shown in P4R.2.',
             'A point blowup replaces a four-ball by the disc bundle\nof $\\OO_{\\mathbb P^1}(-1)$, with common boundary $S^3$.\nVan Kampen therefore shows that it leaves $\\pi_1(T)$ unchanged.',
             ['D04','D06','D22'],'Specify the point-blowup topological map directly.',
             'Both local pieces and their common S3 boundary are simply connected; the induced isomorphism is the one defined by the same blowdown used in the conductor square.')
        edit('\\item We next verify the pushout for the actual singular\nsupport. The morphism $\\nu$ is finite, is an',
             '\\item The normalization morphism $\\nu$ is finite, is an',
             ['D08'],'Introduce the finite normalization properties directly.',
             'The ensuing full compact-Hausdorff quotient, conductor identification and homotopy-pushout argument are retained.')
        edit('The compatible triangulation used in P4R.1 makes\n$D_{\\rm red}\\subset T$ a subcomplex and hence a',
             'A triangulation compatible with the analytic pair $(T,D_{\\rm red})$\nand the finite curve map $D_{\\rm red}\\to C$ makes\n$D_{\\rm red}\\subset T$ a subcomplex and hence a',
             ['D04','D06','D22'],'State the exact compatible triangulation objects.',
             'The same inclusion is a cofibration and the same finite map supplies the mapping-cylinder pushout; all identifications are preserved.')
        edit('This\nargument retains every identification made by the',
             'This\nargument includes every identification made by the',
             ['D08'],'Describe the quotient identifications directly.',
             'The horizontal/vertical and repeated-image identifications in the given finite conductor map are unchanged.')
        edit('\\item P4R.1 makes this group virtually abelian.',
             '\\item Proposition~\\ref{night:P4R.1} makes this group virtually abelian.',
             ['D04'],'Resolve the virtually abelian input.',
             'The group is the same pi1(S)=pi1(C) just constructed, with cyclic quotient dividing the full fibre multiplicity.')
        edit('A surface factor of genus at least two cannot occur\nin a virtually abelian group, by the finite-cover\nargument of P4R.2.',
             'A genus-$h$ surface factor with $h\\ge2$ cannot be virtually\nabelian: a connected degree-$d$ cover has genus $1+d(h-1)>1$,\nand its fundamental group is nonabelian. Projection onto this\nsurface factor is a quotient map, while every quotient of a\nvirtually abelian group is virtually abelian.',
             ['D04','D06','D22'],'Give the exact surface-group quotient and covering calculation.',
             'The projection from the displayed free product to a normalization surface factor is the receiving group map; finite-index subgroups correspond to the indicated closed-surface covers.')
        edit('P4.13 now give',
             'Proposition~\\ref{night:P4.13} give',
             ['D04'],'Resolve the open-stratum Euler input.',
             'The same degeneration of two-tori at mS gives e(S_reg)>=0.')
        edit('contradicting P4.13. This proves strict positivity.',
             'contradicting Proposition~\\ref{night:P4.13}. This proves strict positivity.',
             ['D04'],'Resolve the final contradiction input.',
             'The computed value is the Euler number of the same complement T minus H, identified with S_reg.')
    op=O/f'S6_SERIES_PUBLISH_II_{tag}_full_original.tex';np=O/f'S6_SERIES_PUBLISH_II_{tag}_full_proposed.tex'
    op.write_text(old);np.write_text(new)
    anchors=lambda s:re.findall(r'\\(?:hypertarget|label)\{[^}]*\}',s)
    assert anchors(old)==anchors(new);assert '\t' not in new
    blocks.append(dict(tag=tag,original_path=rel(op),original_sha256=h(old),
        proposed_path=rel(np),proposed_sha256=h(new),original_characters=len(old),
        proposed_characters=len(new),guards=[g['guard_id'] for g in guards],anchors_exact=True))
    allguards.extend(guards)
manifest=dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),checker='ii_check_a',
    canonical_writes=False,guards=allguards,blocks=blocks,
    existing_bibliography_proposal='group07_WT/S6_SERIES_PUBLISH_II_A_02WT_bibliography_entry.tex',
    note='Complete blocks only. YF following broader paragraph remains root-owned and was not opened here; no receiving-target exposure or independent credit. Global enumeration wrappers remain root-owned.')
p=O/'S6_SERIES_PUBLISH_II_A_WU_YF_editorial_proposals.json';p.write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps(dict(manifest=rel(p),sha256=h(p.read_text()),guard_count=len(allguards),blocks=blocks),indent=2))
