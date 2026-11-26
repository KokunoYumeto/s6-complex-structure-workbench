"""Reconstruct reviewed A02/A03 proposals after the 2026-11-21 reset.

Only released original blocks are read.  No canonical source is changed.
Historical manifest hashes are recorded as history, not claimed for these bytes.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'agents/ii_checks_A/recovery_20261121T195642Z'
OUT.mkdir(parents=True, exist_ok=True)
STEMS = {
    '01FY': 'e8ee86f0f98e7433', '02WG': 'de38aaf64023ad6b',
    '02WR': 'b83423f47049211f', '02X2': '5bbb9d08c5c6c56f',
    '02XO': 'cad2012a632183fc', '02XY': '61c9603279b34974',
    '02XZ': '9c10c12f51dece30', '02Y0': '55f4880e6eb36610',
    '02Y1': '33b59b800d669103', '02WH': 'f549a0438516041c',
}
owners = {'01FY': 'cdp:st:D.1.13'}
owners.update(dict(zip(['02WG','02WR','02X2','02XO','02XY','02XZ','02Y0','02Y1','02WH'],
                      ['night:P4.1','night:P4.2','night:P4.3','night:P4.5','night:P4.6','night:P4.7','night:P4.8','night:P4.9','night:P4.10'])))
original = {}
current = {}
edits = {t: [] for t in STEMS}
for tag, stem in STEMS.items():
    p = ROOT / f'agents/ii_infra/released_proofs/{tag}/{stem}/S6_SERIES_PUBLISH_full_owning_block.tex'
    original[tag] = current[tag] = p.read_text()


def edit(tag, old, new, types, identity):
    assert current[tag].count(old) == 1, (tag, old, current[tag].count(old))
    current[tag] = current[tag].replace(old, new, 1)
    edits[tag].append({'defect_types': types, 'old': old, 'new': new,
                       'occurrences': 1, 'mathematical_reference_identity': identity})


def title(tag, old, new):
    edit(tag, '['+old+']', '['+new+']', ['D04','D16'],
         'Only the optional title changes. The statement owner, mathematical hypotheses and conclusions, label, and hypertarget are unchanged.')


title('01FY', 'Refuted printed surjectivity and positivity, with a second example', 'Higher direct images of Wang\'s threefold')
edit('01FY', r'''$H^1(Y;\Z)=H^2(Y;\Z)=0$, $a(Y)=1$, and is a second
counterexample to CDP20 Corollary 5.2 and Proposition 5.5.
Its integral homology torsion distinguishes it from the retained
integral homology sphere.''', r'''$H^1(Y;\Z)=H^2(Y;\Z)=0$ and $a(Y)=1$. Its rank-one
restriction map and direct-image splitting contradict the conclusions of
\cite[Corollary~5.2 and Proposition~5.5, pp.~688--689]{CDP20}.
For the threefold $Y_0$ of \SeriesRef{maps:src:B.5.2}, one has
$H_2(Y_0;\Z)=0$, whereas $H_2(Y;\Z)=\Z/2\Z$; hence a
biholomorphism $Y_0\to Y$ would induce an impossible isomorphism of
these two homology groups.''', ['D01','D06','D18','D25'],
     'The same Wang threefold has the same sheaf and cohomology conclusions. The published claims are located in the opened journal edition, p.688 (statements) and p.689 (Proposition 5.5 proof). The comparison uses the exact current series theorem maps:src:B.5.2 and the functor H_2 applied to a putative biholomorphism; its inverse would induce an inverse homomorphism, impossible for 0 and Z/2.')
edit('01FY', 'through the actual local fillings.', 'through the local fillings.', ['D08'],
     'The fillings and all displayed coordinate maps are identical; only the process adjective is removed.')
edit('01FY', 'Its line-bundle lift changes $d\\log v$\nonly by a base one-form.', 'Its line-bundle lift changes $d\\log v$\nby a one-form pulled back from $S$.', ['D20','D25'],
     'The line bundle projection is M^times to S. A lift multiplies v by a nonzero function on S, so its logarithmic derivative is pulled back from S and wedges to zero with the pulled-back surface two-form. This specifies the exact base of that cotangent morphism.')
edit('01FY', r'Statement \ref{cdp:st:D.1.12}', r'Proposition~\ref{cdp:st:D.1.12}', ['D23'],
     'The reference continues to resolve to exactly cdp:st:D.1.12; its environment is a proposition.')
edit('01FY', r'''theorem give $H^1(Y;\Z)=H^2(Y;\Z)=0$; specifically the torsion
in $H_2$ contributes to $H^3$, not to $H^2$.''', r'''theorem give $H^1(Y;\Z)=H^2(Y;\Z)=0$. More explicitly,
$H_1(Y;\Z)=0$ gives
$H^2(Y;\Z)\simeq\operatorname{Hom}(H_2(Y;\Z),\Z)=0$,
and the universal-coefficient injection in degree three is
$\operatorname{Ext}^1(H_2(Y;\Z),\Z)\simeq\Z/2\Z
\hookrightarrow H^3(Y;\Z)$.''', ['D02','D25'],
     'This spells out the exact universal-coefficient morphisms: in degree two Ext(H_1,Z)=0 and Hom(Z/2,Z)=0; in degree three Ext(H_2,Z)=Z/2 injects. The same integral cohomology claims follow.')
edit('01FY', r'''The retained six-sphere has zero second integral homology, whereas
$H_2(Y;\Z)=\Z/2\Z$. An isomorphism of complex manifolds would
induce an isomorphism of these groups, which is impossible.
This completes the independent counterexample.''', r'''The threefold of \SeriesRef{maps:src:B.5.2} has zero second
integral homology, whereas $H_2(Y;\Z)=\Z/2\Z$. A biholomorphism
and its inverse induce mutually inverse homomorphisms on $H_2$;
the displayed groups therefore exclude such a biholomorphism.''', ['D01','D06','D07','D08'],
     'The exact comparison object is the series construction with label maps:src:B.5.2. Functoriality sends the proposed inverse maps to inverse H_2 maps, establishing the claimed exclusion for precisely those two objects.')

title('02WG', 'P4.1', 'An elliptic bundle degeneration')
edit('02WG', 'give the specified holomorphic product trivialization', 'give the holomorphic product trivialization', ['D08'],
     'The product trivialization is still the same map lambda_A/u=lambda_B/s.')
edit('02WG', r'''circle-bundle calculation in P4.3 gives $b_1=3$. The surface classification
The classification \cite[Chapter~VI, Theorem~1.1 and Table~10, pp.~243--244]{BHPV2004E} consequently identifies this surface as
a primary Kodaira surface.''', r'''circle bundle over $B'$ has primitive Euler class one: in its
fundamental-group presentation the commutator of the two base generators
is the fibre generator. Abelianization therefore gives $H_1=\Z^2$.
The logarithm of the fibre norm modulo $\log q$ gives the further
circle factor, so the surface has $b_1=3$. The classification
\cite[Chapter~VI, Theorem~1.1 and Table~10, pp.~243--244]{BHPV2004E}
identifies this surface, whose canonical bundle is trivial, as a primary
Kodaira surface.''', ['D04','D23','D25'],
     'This is the exact restriction of the line bundle to B\' used in the original proof. The primitive Euler relation kills the fibre in abelianization; the norm-circle product adds one free generator. Thus the printed b_1=3 is established in this block, with the identical trivial-canonical surface and opened BHPV classification locator.')

title('02WR', 'P4.2', 'A compact torus fibration with three singular fibres')
edit('02WR', r'''The three markings and the principal-bundle clutch in the prompt define a
smooth compact complex threefold $f:Y\to\Pp^1$ with connected fibres,
exactly three singular fibres of the form in P4.1, and identity monodromy
on $H_1$ of the regular fibre.''', r'''Let $E=\C/(\Z+i\Z)$ and $A=E^2$. Glue a principal $A$-bundle
over $\Pp^1$ by
$a_{\rm out}=a_{\rm in}+(\ell(t),0)$, where
$\ell(t)=\log(t)/(2\pi i)\in E$. Over disjoint discs about
$0,1,\infty$, replace its product models by the degeneration of
Proposition~\ref{night:P4.1}, using, respectively, the markings
\[
 C_i\times B_i\longrightarrow A,\qquad
 (z,w)\longmapsto(w,z),\quad(iz,iz+w),\quad(z,iz+w),
\]
and the punctured-disc product trivialization from the canonical section
of $\OO(R)$. These transitions define a smooth compact complex
threefold $f:Y\to\Pp^1$ with connected fibres, exactly three singular
fibres of the form in Proposition~\ref{night:P4.1}, and identity
monodromy on $H_1$ of the regular fibre.''', ['D04','D05','D13'],
     'The three maps, ell clutch, centres, and punctured-disc marking are exactly the isolated construction data bound by SHA a906434924d29bcdb3be186b5f238185b87e5326abd0bb8dca31764bd4d3428a. The preceding setup has E=C/(Z+iZ), q=e^(-2pi), A=E^2. No gluing datum is replaced; the undefined prompt reference is expanded to those same data.')
edit('02WR', 'by P4.1 using the holomorphic group isomorphisms', r'by Proposition~\ref{night:P4.1} using the holomorphic group isomorphisms', ['D04'],
     'The local model is still night:P4.1; only its printed reference is resolved.')
edit('02WR', r'''Each lattice matrix $S_i$ displayed below has determinant
one. These maps, $\lambda_B=v\lambda_A$, the canonical punctured-disc
trivialization in P4.1, and the clutch $\ell$ specify all transitions.''', r'''Multiplication by $i$ preserves $\Z+i\Z$. The three inverse maps
are $(x,y)\mapsto(y,x)$, $(x,y)\mapsto(-ix,y-x)$ and
$(x,y)\mapsto(x,y-ix)$, respectively. Their Gaussian-integer matrices
have determinants $-1,i,1$ and hence their real lattice determinants
are all one. These maps, $\lambda_B=v\lambda_A$, the canonical
punctured-disc trivialization in Proposition~\ref{night:P4.1}, and
the clutch $\ell$ specify all transitions.''', ['D04','D09','D25'],
     'The inverses are composed directly with the exact three original markings. A complex Gaussian unit determinant has real determinant its norm, equal to one. This supplies the same unimodularity and gluing maps within the block instead of an absent matrix display.')

title('02X2', 'P4.3', 'Integral homology of the local degeneration')
edit('02X2', r'''Order the local fibre lattice as $(a,c,b,d)$, where $(a,c)$ are the cycles''', r'''For the degeneration $U$ of Proposition~\ref{night:P4.1}, order the
regular fibre lattice as $(a,c,b,d)$, where $(a,c)$ are the cycles''', ['D04','D13'],
     'This names the same local space U already used in the proof; the fibre, lattice ordering and inclusion maps remain identical.')
edit('02X2', r'''product orientation for $rc$. The complete differential matrices are
printed below. The complex has free homology of ranks $(1,3,5,5,2)$;
the inclusion of the torus subcomplex gives exactly the two quotient maps.''', r'''product orientation for $rc$. The pairs $(r,a)$ and $(rc,a\wedge c)$
are integral contractible summands: the degree-one homotopy sends
$a$ to $r$ and $a\wedge c$ to $rc$, and is zero on the remaining
basis cells. Deleting these pairs leaves the zero differential and
free homology of ranks $(1,3,5,5,2)$. The inclusion of the torus
subcomplex kills exactly $a$ in degree one and $a\wedge c$ in
degree two, giving the asserted quotient maps.''', ['D09','D25'],
     'The same two unit differentials are contracted by h(a)=r and h(a wedge c)=rc. The identity dh+hd=id-ip on the full 20-cell complex gives an explicit integral chain equivalence and the same torus inclusion kernels; every other cell is fixed by ip.')

title('02XO', 'P4.5', 'Invariants of the compact torus fibration')
edit('02XO', 'For this example,', r'For the threefold $Y$ of Proposition~\ref{night:P4.2},', ['D04','D13'],
     'The example is identified with its existing construction night:P4.2, with the same map Y to P1.')
edit('02XO', 'Duality and P4.4 give', r'Duality and Proposition~\ref{night:P4.4} give', ['D04'],
     'The same integral homology input night:P4.4 is retained and resolved locally.')

title('02XY', 'P4.6', 'Euler characteristic of a normal crossing divisor')
edit('02XY', r'''This assertion concerns the reduced support, regardless of the
multiplicities with which it occurs in a fibre.''', r'''For a fibre $\sum_j m_jF_j$ with this reduced support, the divisor
in the formula is $F=\sum_jF_j$.''', ['D02','D11'],
     'The precise morphism is the reduction of the same fibre subscheme, with underlying union of the same F_j. The hypothesis and formula concern that exact reduced divisor and retain arbitrary positive m_j.')
edit('02XY', r'''The alternating count is also verified directly at a point with one,
two or three branches. This proves the identity and parity, without
using fibre multiplicities or a base change.''', r'''At a point with $r=1,2,3$ local branches, the alternating
contribution is $r-\binom r2+\binom r3=1$. This gives the
displayed Euler additivity formula and proves the identity and parity.''', ['D02','D08','D25'],
     'The exact local inclusion-exclusion multiplicities are displayed for the same one-, two-, and three-branch strata. The proof and its treatment of arbitrary fibre multiplicities are preserved by the statement\'s explicit reduction map.')

title('02XZ', 'P4.7', 'The Chern number of a normal crossing fibration')
edit('02XZ', r'''The numerical conclusion does not require the general fibre to be a
torus.
''', '', ['D02','D11'],
     'The complete statement already quantifies over all proper connected-fibre holomorphic maps with the displayed b_1=b_2=0 and normal crossing support hypotheses. No torus hypothesis is inserted anywhere; its full scope is unchanged.')
edit('02XZ', '\\item \n\\noindent\\textbf{Step 1.} Connected fibres', '\\item Connected fibres', ['D10','D23'],
     'The existing enumerated proof step is retained; only its duplicated manual step heading is removed.')
edit('02XZ', 'Euler additivity and P4.6 give', r'Euler additivity and Proposition~\ref{night:P4.6} give', ['D04'],
     'The exact same normal crossing Euler identity is cited by its local label.')

title('02Y0', 'P4.8', 'Normal crossing torus fibres and their normalizations')
edit('02Y0', r'''For a torus fibration in P4.7 whose reduced supports have normal
crossings,''', r'''For a fibration in Proposition~\ref{night:P4.7} with general fibre
a complex two-torus,''', ['D04','D12'],
     'Proposition P4.7 already requires every reduced support to have normal crossings. The same additional general-two-torus hypothesis is retained exactly.')
edit('02Y0', 'In the zero case the supports have the\nforms stated in the prompt:', 'The supports of Euler number zero have the following forms:', ['D05','D08'],
     'All three listed geometric forms are retained verbatim; the undefined workflow reference is replaced by their mathematical property.')
edit('02Y0', 'proved\nin P4.6.', 'proved\nin Proposition~\\ref{night:P4.6}.', ['D04'],
     'The Chern identity e(S_i)=K^2_(S_i) is the same input with the same normalization component.')
edit('02Y0', r'''\cite[Theorem~4.2 and proof, pp.~17--21; Theorem~5.1 and proof, pp.~27--29]{OVV2020}''', r'''\cite[arXiv version~3, Theorem~4.2, pp.~17--18; Theorem~5.1 and proof, pp.~27--29]{OVV2020}''', ['D18'],
     'The cited pages belong to the opened arXiv 1810.05768v3 edition. The exact Theorem 4.2 statement and Theorem 5.1 proof were opened; this correction does not claim that all of the intervening proof was read.')
edit('02Y0', 'non-Kähler elliptic surface are smooth elliptic curves.', 'minimal non-Kähler elliptic surface are smooth elliptic curves.', ['D25'],
     'The proof applies this fact only to the minimal model before counting blowups. Stating that scope explicitly retains exactly the map used and does not claim that exceptional curves on a blowup are elliptic fibres.')
edit('02Y0', r'''The class-VII case has $b_2=0$. Theorem 1 of
Buonerba--Bogomolov--Kurnosov \cite[Theorem~1, p.~1]{BBK2019} supplies a finite unramified Hopf or
Inoue cover. The conductor excludes an Inoue cover: Inoue surfaces
have no compact curves, by Inoue's theorem as stated and credited in
\cite[Theorem~3.1, p.~303]{KhaledTeleman2026Journal}.
The type-III family has the explicit type-II unramified double cover
of \cite[proof of Remark~3.5, p.~305]{KhaledTeleman2026Journal}. A finite unramified quotient of a Hopf surface has universal
cover $\C^2\setminus\{0\}$ and is therefore a Hopf surface.''', r'''The class-VII case has $b_2=0$. The finite-cover classification
\cite[arXiv version~3, Theorem~1, p.~1]{BBK2019} gives a finite
unramified map $p:\widehat S_i\to S_i$ with $\widehat S_i$ Hopf
or Inoue. The inverse image $p^{-1}(D_i)$ is a nonempty compact
curve: surjectivity makes it nonempty, and an unramified map preserves
its local codimension. Inoue surfaces have no compact curves
\cite[Theorem~3.1, p.~303]{KhaledTeleman2026Journal}; the type-III
family is covered by the explicit unramified type-II double cover
of \cite[proof of Remark~3.5, p.~305]{KhaledTeleman2026Journal}.
Thus $\widehat S_i$ is Hopf. Its universal covering
$\C^2\setminus\{0\}\to\widehat S_i$, composed with $p$, is a
universal covering of $S_i$, which is therefore a Hopf surface.''', ['D08','D18','D25'],
     'The exact finite unramified map p is retained. Pullback of the nonempty conductor proves the Inoue exclusion through a concrete curve morphism. Composition with the simply connected Hopf universal cover proves the quotient identification. The opened BBK v3 statement and Khaled--Teleman published locators support those exact maps.')
edit('02Y0', 'P4.6 gives $T=2', r'Proposition~\ref{night:P4.6} gives $T=2', ['D04'],
     'The same normalization and triple-point identity is used.')
edit('02Y0', 'P4.12 proves that the', r'Proposition~\ref{night:P4.12} proves that the', ['D04'],
     'The same irreducible-support dualizing-sheaf statement is retained as an input; this proposal gives no independent credit for its then-unread proof.')
edit('02Y0', 'already described in P4.6.', r'already described in Proposition~\ref{night:P4.6}.', ['D04'],
     'The branch-pair map is the same finite unramified map on the normalized double locus.')
edit('02Y0', r'''\cite[Theorem~2.1]{Catanese2004}''', r'''\cite[definition of deformation equivalence, p.~261; Theorem~2.1 and proof, pp.~264--268]{Catanese2004}''', ['D18'],
     'The opened author-hosted published edition defines deformation by a proper holomorphic submersion and proves the torus theorem at the stated pages. These are the exact family hypotheses constructed by the normalized cyclic base change.')
edit('02Y0', r'''disc, with no Kähler hypothesis on the total space. We have verified
all these hypotheses. The new central fibre is therefore a torus;''', r'''disc. The normalized cyclic base change constructed above is such
a proper holomorphic submersion, so its central fibre is a torus;''', ['D02','D08','D11'],
     'The map in the cited deformation theorem is explicitly the same normalized cyclic base-change family. Its hypotheses were proved by the local m-th root charts and properness; no total-space Kähler assumption is introduced.')
edit('02Y0', 'the new central fibre maps finitely and unramifiedly to $G$, and\nthat the new map to the $u$-disc', 'the central fibre of the base-changed family maps finitely and\nunramifiedly to $G$, and that its map to the $u$-disc', ['D08'],
     'The family and central-fibre covering are precisely the normalized cyclic base change t=u^m already constructed; this replaces a process adjective with its defining map.')
edit('02Y0', 'the required finite unramified cover of $G$.', 'the finite unramified torus cover of $G$.', ['D05'],
     'The exact source of this covering was proved to be a torus in the preceding sentence. Its finite unramified map to G is unchanged.')

old_y1 = original['02Y1']
new_y1 = r'''\begin{remark}[Euler values of irreducible fibre supports]\hypertarget{tag-02Y1}{}\label{night:P4.9}\label{stmt:P4.9}
\StatementRecord{night:P4.9}{proved}{02Y1}{\SeriesRef{night:P4.26}, \SeriesRef{night:P4.32}, \SeriesRef{night:P4.35}, \SeriesRef{night:P4.37}, \SeriesRef{night:P4.54}, \SeriesRef{night:P4.57}, \SeriesRef{night:P4.58}, \SeriesRef{night:P4R.18}, \SeriesRef{night:P4R.20}}

The sign and equality classifications are given by Theorem~\ref{night:P4.58}
for the same morphism $f:Y\to B$ and the same reduced fibre supports.
In particular, each irreducible singular support whose normalization has
a rational resolution has Euler number two, and every other irreducible
support has Euler number zero. This is the identity specialization of
that theorem to the irreducible supports of its fibration.
\end{remark}
'''
edit('02Y1', old_y1, new_y1, ['D04','D05','D10','D12','D16'],
     'The frozen independent derivation proves exactly the implication P4.58 to P4.9 by the identity on f,Y,B and every reduced support. The duplicate proposition and outline of the same theorem are replaced by a numbered remark with that exact identity specialization. Both explicit Euler values, sign/equality reference, all labels, hypertarget and StatementRecord arguments remain. No proof of P4.58 or its auxiliary targets was opened for this implication check.')

title('02WH', 'P4.10', 'A projective torus fibration with Chern number twenty-four')
edit('02WH', r'''Consequently the hypothesis $b_2=0$ cannot be omitted, even in the
intersection of the two classes of fibres in the question.''', r'''This example has $b_2(Z)>0$ and the fibre types of
Proposition~\ref{night:P4.7}; its value $c_3[Z]=24$ shows that the
bound in that proposition depends on the hypothesis $b_2=0$.''', ['D05','D11'],
     'The same example retains b_1=0, general two-torus fibre, and irreducible normal crossing special supports. Its b_2>0 is proved by the ample class below, and comparison with the exact 0-or-2 bound of P4.7 identifies the omitted hypothesis.')
edit('02WH', r'''\begin{gathered}
h=ar,\quad y=-au,\quad x=u+r,\quad f=-aux;
 \qquad
 \\
r=bh,\quad u=-by,\quad x=-bv,\quad f=-byv.
\end{gathered}''', r'''\begin{aligned}
h&=ar, & y&=-au, & x&=u+r, & f&=-aux,\\
r&=bh, & u&=-by, & x&=-bv, & f&=-byv.
\end{aligned}''', ['D23'],
     'Every chart equation, variable and sign is identical; only alignment and the redundant blank line are changed.')
edit('02WH', 'For completeness we compute $\\pi_1(Z)$.', 'We compute $\\pi_1(Z)$.', ['D08'],
     'The full fundamental-group proof remains; only the process qualifier is removed.')
edit('02WH', r'''This
identifies the omitted hypothesis: $b_2(Z)>0$.''', r'''Thus $b_2(Z)>0$, as asserted.''', ['D08','D11'],
     'The preceding positive integral of the projective Kähler class proves the same nonvanishing in H^2; the reference to the precise bound is now in the statement.')


def sha(data):
    return hashlib.sha256(data).hexdigest()


proposals = []
for tag in STEMS:
    # Label identity is checked mechanically in addition to the full rereading.
    marker = r'\\(?:label|hypertarget)\{[^}]+\}'
    assert re.findall(marker, original[tag]) == re.findall(marker, current[tag]), tag
    group = 'group02' if tag in ['01FY','02WG','02WR','02X2','02XO','02XY'] else 'group03'
    folder = OUT / group
    folder.mkdir(exist_ok=True)
    oldp = folder / f'S6_SERIES_PUBLISH_II_A_{tag}_original_block.tex'
    newp = folder / f'S6_SERIES_PUBLISH_II_A_{tag}_proposed_block.tex'
    oldp.write_text(original[tag])
    newp.write_text(current[tag])
    proposals.append({
        'tag': tag, 'statement_owner': owners[tag],
        'release_receipt': f'agents/ii_infra/released_proofs/{tag}/{STEMS[tag]}/S6_SERIES_PUBLISH_release_receipt.json',
        'original_block_path': str(oldp.relative_to(ROOT)),
        'original_block_sha256': sha(oldp.read_bytes()),
        'proposed_block_path': str(newp.relative_to(ROOT)),
        'proposed_block_sha256': sha(newp.read_bytes()),
        'literal_edits': edits[tag],
        'labels_and_hypertargets_identical': True,
        'D10_statement_header_disposition': 'Root-owned StatementRecord definition prints the tag only. All four metadata arguments remain unchanged.',
        'actual_comparative_rereading_record': None, 'approved': False,
    })
for group, tags, historical in [
    ('group02', ['01FY','02WG','02WR','02X2','02XO','02XY'], '18fe41d5f496851ad6dd76ad752954da00f1848c0667424ef725fd79305f5569'),
    ('group03', ['02XZ','02Y0','02Y1','02WH'], 'aa4b00deab03f5ebd38581409cc876d7244e6a399f1626ca9e9c5acb4003079d')]:
    manifest = {
        'created_utc': datetime.now(timezone.utc).isoformat(), 'checker': 'ii_check_a',
        'recovery_status': 'New reconstruction from restored frozen blocks and retained reasoning. These are fresh bytes and timestamps, not a claim to reproduce the historical manifest byte-for-byte.',
        'historical_unrestored_manifest_sha256': historical,
        'proposals': [p for p in proposals if p['tag'] in tags],
        'canonical_source_changed': False, 'events_added': 0,
    }
    p = OUT / group / f'S6_SERIES_PUBLISH_II_A_recovery_{group}_editorial_proposals.json'
    p.write_text(json.dumps(manifest, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps({'path': str(p.relative_to(ROOT)), 'sha256': sha(p.read_bytes()),
                      'owners': len(manifest['proposals']), 'edits': sum(len(x['literal_edits']) for x in manifest['proposals'])}))
