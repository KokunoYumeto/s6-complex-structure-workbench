"""Apply the results of checkpoint 01 of S6_02_PUSH and S6_03_CDP to the prompts S6_04 and S6_05.

Edits PROMPT.md by line prefix (the backups PROMPT_before_20261115.md are the input, so the script can be rerun),
and rebuilds each background zip from its backup with the notes file, the checkpoint sections and new manifest rows.
"""
import hashlib
import io
import os
import re
import zipfile

DOCS = r'C:\Users\user\Documents'
P = DOCS + r'\s6_pro_prompts_20261112'
WORK = DOCS + r'\s6_pro_prompts_20261112_work'
INTAKE = WORK + r'\checkpoint_intake_20261115'
PUSH = WORK + r'\returns\S6_02_PUSH_checkpoint_01_20261115T1339Z_unzipped\S6_02_PUSH'
CDP = WORK + r'\returns\S6_03_CDP_checkpoint_01_20261115T1336Z_unzipped\S6_03_CDP'

ORIGIN = 'checkpoint 01 of the run %s (GPT-6 Astra, ChatGPT Pro mode), 15 November 2026; run in progress, unreviewed'


def load(path):
    return io.open(path, encoding='utf-8').read().split('\n')


def find(lines, prefix):
    hits = [i for i, l in enumerate(lines) if l.startswith(prefix)]
    if len(hits) != 1:
        raise SystemExit('prefix %r: %d hits' % (prefix, len(hits)))
    return hits[0]


def append(lines, prefix, text):
    i = find(lines, prefix)
    lines[i] = lines[i].rstrip() + ' ' + text


def insert_after(lines, prefix, block):
    i = find(lines, prefix)
    lines[i + 1:i + 1] = block.split('\n')


# ---------------------------------------------------------------- S6_04
K04 = """
From checkpoint 01 of the runs S6_02_PUSH and S6_03_CDP (GPT-6 Astra, ChatGPT Pro mode; 15 November 2026). Both runs were still in progress when the checkpoints were saved; nobody has reviewed these results; the status is the one each run states. `S6_CHECKPOINT_01_20261115.md` lists them with their source files, and the sections with the proofs are in `checkpoint_01/`. Do not prove them again: read the proof of each one you use, check it, and build on it; where a proof fails, say where and repair it.

- **K1 (S6_02_PUSH E.1.1, E.1.2; Proved).** The dictionary that R4 lacked. The integral change of marking to the data (ρ_i, N_i) of arXiv:2610.39102 is PV = [[−2,1,0,1],[−6,0,−1,0],[0,−1,0,0],[−1,0,0,0]] (determinant −1); w₁ = N₀ε − ρ₀δ̂, w₂ = N₁ε′ − (ρ₁ + N₁)δ̂; l₀ = 0 and p = −(nN₀ + mN₁). In these coordinates the criterion of R4 is proved with its analytic gluing: for fixed data the period is 2klZ, and at fixed u there are 2kl classes.
- **K2 (S6_02_PUSH E.1.3, C.4.1; Proved).** The comparison maps vary holomorphically, locally in c. For the multiplicities (3,4) every admissible sphere twist datum gives W = (−1)^{s₂}w and the same class of the monodromy in π₀Diff⁺(S^6).
- **K3 (S6_02_PUSH C.1.1, C.1.2, C.2.1; Known, with derivation).** The conventions for Θ₇: the mapping torus of the monodromy against the glued sphere, with the positive-loop convention and its boundary orientation; the Eells-Kuiper invariant is the same for both spin structures; the positive generator has Euler class 1, p₁ = 6, p₁² = 36, signature 1 and μ = 1/28; the spin and spin-c characteristic-number formulas, independent of the lifts.
- **K4 (S6_02_PUSH C.3.1; Proved).** The effective circle of Aut(X_c) acts freely off a fixed 2-sphere, with normal weights (1, −1); an equivariant monodromy exists; on a regular fibre its linear part is I − 2E.
- **K5 (S6_02_PUSH C.3.2; Proved).** A global invariant scalar circle gauge on a simply connected manifold is isotopically trivial, and the primitive γ-coordinate of a regular fibre cannot extend over X. So the global scalar-gauge isotopy of Φ to a twist is not valid.
- **K6 (S6_02_PUSH C.3.3; Known, with derivation).** Every one of the 28 classes of π₀Diff⁺(S^6) has a representative for a fixed semifree circle action with fixed S². Equivariance alone does not determine [Φ].
- **K7 (S6_02_PUSH C.3.4; Proved).** After the sixfold base change of the parameter two residues remain possible; they differ by 14.
- **K8 (S6_02_PUSH C.3.5; Proved).** The coherent even-shift maps have an explicit affine lift. The closing map of the positive loop has scalar t⁴/(t−1)³ (orders 4 and −3 at the finite points, −1 at the cusp); at the cusp it also has a holomorphic unit representative, which differs from the scalar one by one γ deck period. Not proved there: the patching of the scalar and cusp-unit isotopies; no bound on the order of [Φ].
- **K9 (S6_02_PUSH C.4.2; Proved).** The antiholomorphic symmetry negates both sides and gives no order-two restriction on [Φ].
- **K10 (S6_02_PUSH C.5.1; Open in that run).** The value of [Φ].
- **K11 (S6_02_PUSH E.5.1, Refuted; E.5.2, E.5.3, Proved).** For the two-parameter family of arXiv:2609.33785 the Weierstrass equation y² = x³ + tx + 1 has a fibre III* at infinity, not III, and the torus degeneration orders are (1,0), (1,0), (1,1): two rank-one fibres and one hexagonal rank-two fibre. The exact monodromy matrices, their centralizers, all fixed lattices, the finite norm group 4Zℓ + 2Zδ and the primitive vanishing lattices are computed; on the stated parameter domain two members are biholomorphic exactly when μ′ = μ and c′ − c ∈ 2Z.
- **K12 (S6_02_PUSH E.2.1, E.2.2, E.2.3; Proved).** For every coprime pair (3k, 4l): (h⁰, h¹, h², h³)(T) = (1, 1, 1, 0) and the Kuranishi germ is a smooth reduced miniversal line; the multiplicity pair is locally constant in deformations; the Kodaira dimension is given by the sign of kl − 3k − 4l; different pairs do not occur in one proper holomorphic submersion over a connected irreducible reduced base.
- **K13 (S6_02_PUSH A.1.1, A.1.2, A.2.1, A.2.2, A.4.1, A.4.2; Proved).** The untwisted X(u) has free integral homology with Betti numbers (1, 1, 8, 14, 8, 1, 1). For the degeneration u → 0 there is a fan with chart xy = uzv, q = zv, a proper flat global nodal plumbing that contracts one diagonal (−1,−1)-curve of X(u), and exactly two minimal semistable refinements with joint flatness, with the integral homology, fundamental groups and Euler numbers of the central fibres.
- **K14 (S6_03_CDP D.1.6, D.1.13; stated there as a second counterexample to the printed count and to the printed surjectivity).** Wang's threefold X₂(λ) has H₀ = H₆ = Z, H₂ = H₃ = Z/2 and no other reduced homology; its fibration has four exceptional values; K = f*O(−1), R¹f_*O = O ⊕ O(−1), R²f_*O = O(−1).
- **K15 (S6_03_CDP C2a, Proved; C2b, Refuted; C2c, Proved).** Euler localization for torus fibrations: c₃(Y) = e(Y) = Σ e((Y_c)_red) over the critical values. Nonnegativity of the Euler number of every fibre is false for unrestricted torus fibrations. The Euler numbers in the semistable toric rank-two models.
- **K16 (S6_03_CDP E6, E7, E13, E14, E15; Proved; statements only, in `checkpoint_01/S6_03_CDP_results.csv`).** Every deformation of a rank-two torus fibration over P¹ keeps the map to P¹, and all the named torus-fibred families satisfy the hypothesis at their hexagonal cusp. Tangent cohomology: the two-parameter family and the family of Liu and Rollenske (1, 2, 2, 0); the positive combs (2m+1, 8m+1, 6m+1, 0); each with a smooth miniversal germ."""

M04 = ("- **Checkpoint 01 of the runs S6_02_PUSH and S6_03_CDP** (`S6_CHECKPOINT_01_20261115.md`; `checkpoint_01/`: the "
       "sections `S6_02_PUSH_AB_push.tex`, `S6_02_PUSH_C_push.tex`, `S6_02_PUSH_C_closing_cocycle.tex`, "
       "`S6_02_PUSH_E_push.tex`, `S6_02_PUSH_conventions_push.tex`, `S6_03_CDP_part_D.tex`, "
       "`S6_03_CDP_part_C2_C4_C5.tex`, `S6_03_CDP_conventions.tex`, and the registers `S6_02_PUSH_results.csv`, "
       "`S6_03_CDP_results.csv`): AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 15 November 2026, saved by two "
       "runs that were still in progress; reviewed by no one. Statement numbers written \"S6_02_PUSH C.3.5\" or "
       "\"S6_03_CDP D.1.6\" refer to these files; the results used here are K1-K16.")


def edit_04():
    src = os.path.join(P, 'S6_04_MAPS_MANIFOLDS', 'PROMPT_before_20261115.md')
    L = load(src)
    append(L, 'Development prompt, 12 November 2026; revised 13 November 2026',
           'Revised 15 November 2026 after checkpoint 01 of the runs S6_02_PUSH and S6_03_CDP, both still in progress '
           '(results K1-K16; they change Lead 8 and the items A.1, B.4, B.6, D.1, D.2, D.3 and F.1).')
    insert_after(L, '- **R6 (S6_02 D.2.1, D.2.2).**', K04)
    append(L, '- **Lead 8 (the monodromy of the family as a twist).**',
           '**After checkpoint 01 of S6_02_PUSH:** the statements on ρ and on an equivariant Φ are proved there (K4), '
           'the statement on the antiholomorphic involution is proved (K9), the isotopy to the twist is refuted as a '
           'global scalar-gauge statement (K5), and equivariance alone cannot give the value (K6). The value of [Φ] is '
           'still not known (K10).')
    append(L, 'A.1. Prove or refute Lead 1',
           'S6_02_PUSH C.3.2 proves that the γ-coordinate of a regular fibre does not extend over X (K5): compare its '
           'argument with the two-path argument of Lead 1 and say which statement each one proves.')
    i = find(L, 'B.4. ')
    new, n = re.subn(r'For X_\{3k,4l\} use R4, and write the dictionary .*? that R4 lacks\.',
                     'For X_{3k,4l} use R4 with the dictionary K1: check K1 against (2.11)-(2.12) of arXiv:2610.39102 and '
                     'use it; do not derive it again. For the two-parameter family use the monodromy matrices, fixed '
                     'lattices and vanishing lattices of K11, with its correction of the fibre at infinity.', L[i])
    if n != 1:
        raise SystemExit('B.4 sentence not found')
    L[i] = new
    append(L, 'B.6. ',
           '**After checkpoint 01 of S6_02_PUSH.** That run has fixed the conventions and compared the mapping torus '
           'with the glued sphere (K3), proved the circle action and an equivariant Φ (K4), the independence of the '
           'twist data (K2), the closing map (K8) and the two residues left after the sixfold base change (K7); it has '
           'not computed [Φ] (K10), and it has shown that the equivariant structure alone cannot give it (K6) and that '
           'the global scalar-gauge isotopy fails (K5). So here: adopt the conventions of K3; check K2-K9 and do not '
           'prove them again; go straight to the value. Compute it by the handle decomposition of B.5 carried along '
           'the circle of parameters, and by the step that K8 leaves: patch the scalar and cusp-unit isotopies into '
           'one isotopy class of S^6 and identify that class in Θ₇. Decide which of the two residues of K7 occurs. '
           'For the families X_{3k,4l} use K1 and K12.')
    append(L, 'D.1. ',
           'The count of biholomorphism classes at fixed u, in the coordinates of arXiv:2610.39102, is K1; the tangent '
           'cohomology and the Kodaira dimension of the members X_{3k,4l} are K12: use them in the comparison.')
    append(L, 'D.2. ',
           'Further checks from checkpoint 01: the untwisted X(u), with free homology and Betti numbers '
           '(1, 1, 8, 14, 8, 1, 1) (K13); Wang\'s threefold (K14); the Euler number of every filling by the localization '
           'formula and the semistable toric rank-two values (K15); the two-parameter family with the configuration '
           'as corrected in K11.')
    append(L, 'D.3. ',
           'S6_02_PUSH constructs, for the degeneration u → 0, a proper flat nodal plumbing that contracts a '
           '(−1,−1)-curve of X(u), in a fan with chart xy = uzv, with its two minimal semistable refinements and '
           'their homology (K13; `checkpoint_01/S6_02_PUSH_AB_push.tex`, A.1.1-A.4.4). That is a different degeneration '
           'from the one of this item. Take its fan and its proofs of properness and flatness as the model for the '
           'construction here, and say exactly how the two degenerations are related.')
    append(L, 'F.1. ',
           'The Euler localization and the values in the semistable toric models of rank two are K15; prove the '
           'rank-three value by the same method.')
    insert_after(L, '- **The return of the run S6_02_FAMILY**', M04)
    out = os.path.join(P, 'S6_04_MAPS_MANIFOLDS', 'PROMPT.md')
    io.open(out, 'w', encoding='utf-8', newline='\n').write('\n'.join(L))


# ---------------------------------------------------------------- S6_05
K05 = """
From checkpoint 01 of the run S6_02_PUSH, with one item from S6_03_CDP (GPT-6 Astra, ChatGPT Pro mode; 15 November 2026). Both runs were still in progress when the checkpoints were saved; nobody has reviewed these results; the status is the one each run states. `S6_CHECKPOINT_01_20261115.md` lists them with their source files, and the sections with the proofs are in `checkpoint_01/`. Do not prove them again: read the proof of each one you use, check it, and build on it; where a proof fails, say where and repair it. They concern problem III only.

- **K1 (S6_02_PUSH D.4.5; Proved).** N((2−ρ)/3, ρ) = 3^{1/4} exactly, hence D_part(z₁) = −(3/(2π))·log 48. The proof is a third derivation, by an isogeny: multiplication by α = 1 + ρ has degree 3 and kernel {0, μ, −μ}; log N(αz) and Σ_{v ∈ ker α} log N(z + v) have the same distributional Laplacian and both have mean zero, so they are equal, and z → 0 gives N(μ)² = |α| = √3.
- **K2 (S6_02_PUSH D.1.1, D.1.2, D.1.3; Proved).** j(Alb S₂(w)) = J(i·w/216), with no meromorphic continuation through any point of |w| = 216; and no reduced proper flat complex-space extension of the family through any boundary point exists, even under fibrewise biholomorphism alone.
- **K3 (S6_02_PUSH D.2.1; Proved).** With h = μ − (1−τ)/2 near τ = i: τ = i − (3πi/2)h² + O(h⁴), D_part = −(3/π)·log 6 − 3|h|² + O(|h|⁴) and log N = log √2 − (π/2)|h|² + O(|h|⁴). In the proof (`checkpoint_01/S6_02_PUSH_D_push.tex`, lines 207-218): g₂(i) = 4π⁴A² and e₂′(i) = 2π³iA²/3 with the constant A defined there, which is the identity 3e₂′(i) = (2/π)·i·g₂(i)/4.
- **K4 (S6_02_PUSH D.4.4, Proved; D.4.6, Open in that run).** On ordinary modulus charts ∂_τ D = i·Z·(3Z℘′ − 2g₂)/(4π²℘′), with Z = ∂_μ log ϑ₁ + 2πi·Im μ/Im τ; D is superharmonic on the root charts; its critical points lie in the zero sets of the two factors. Not proved there: that D has no further local maximum, and the global topology of its level sets.
- **K5 (S6_02_PUSH D.4.1, D.4.2, D.4.3; Proved).** For the height H* + ε with ε small and positive the degeneracy set is one analytic Jordan curve, |t − 1| = (π⁴E₄(i)/4)·ε²·(1 + O(ε)); for every supercritical height the exact level equation of the modular norm, the regular locus and the connected negative-sign region; the closure of the period group at every rank-three point.
- **K6 (S6_02_PUSH E.4.1, E.4.2, E.4.3; Proved).** The 19,701 boxes of the certificate of S6_02 C.2.3 are recertified with a second interval library (Arb through python-flint, 192 bits; only the exact rational box endpoints reused), with largest certified upper bound below 1.999877571767410525; an exact rational sweep checks the cover; the local argument on |τ − i| ≤ 3/20000 is re-derived with all its constants. So max D_part = −(3/π)·log 6, attained only at t = 1, now rests on two independent certificates.
- **K7 (S6_03_CDP E16; Proved).** The rank divisors of the root Kodaira-Spencer morphism of the period family (`checkpoint_01/S6_03_CDP_part_E_rank.tex`)."""

M05 = ("- **Checkpoint 01 of the runs S6_02_PUSH and S6_03_CDP** (`S6_CHECKPOINT_01_20261115.md`; `checkpoint_01/`: the "
       "sections `S6_02_PUSH_D_push.tex`, `S6_02_PUSH_E4_push.tex`, `S6_02_PUSH_conventions_push.tex`, "
       "`S6_03_CDP_part_E_rank.tex` and the register `S6_02_PUSH_results.csv`): AI-produced by GPT-6 Astra (OpenAI, "
       "ChatGPT Pro mode), 15 November 2026, saved by two runs that were still in progress; reviewed by no one. "
       "Statement numbers written \"S6_02_PUSH D.4.5\" refer to these files; the results used here are K1-K7.")


def edit_05():
    src = os.path.join(P, 'S6_05_ARITHMETIC', 'PROMPT_before_20261115.md')
    L = load(src)
    append(L, 'Development prompt, 12 November 2026; revised 13 November 2026',
           'Revised 15 November 2026 after checkpoint 01 of the runs S6_02_PUSH and S6_03_CDP, both still in progress '
           '(results K1-K7 for problem III; they change R4, Leads 7, 8, 9 and 12 and the items C.1, C.2, C.3 and C.8).')
    insert_after(L, '- **R5 (S6_02 A.4.1, A.5.1).**', K05)
    append(L, '- **R4 (S6_02 C.2.2, C.2.3).**',
           'Checkpoint 01 of S6_02_PUSH has recertified the 19,701 boxes with a second interval library and re-derived '
           'the local argument (K6).')
    append(L, '- **Lead 7 (the value at the order-three point).**',
           '**After checkpoint 01 of S6_02_PUSH (K1):** N(z₁)⁴ = 3 and D_part(z₁) = −(3/(2π))·log 48 are proved there '
           'by a third derivation, the isogeny 1 + ρ; with Re β^part(z₁) = −1/2 (R3) this gives β^part(z₁).')
    append(L, '- **Lead 8 (the Albanese curves).**',
           '**After checkpoint 01 (K1, K2):** j(Alb S₂) = J(i·w/216) with its natural boundary is proved there, and '
           '|q(Alb S₁)| = |w|²/48³ follows from K1.')
    append(L, '- **Lead 9 (the expansion at the maximum).**',
           '**After checkpoint 01 (K3):** the expansion of μ at τ = i, the identity for e₂′(i) and the expansion of '
           'D_part to second order in h are proved there.')
    append(L, '- **Lead 12 (the two special radii).**',
           '**After checkpoint 01 (K1, K2):** both radii and the natural boundary of j(Alb S₂) are proved there; the '
           'holomorphy of j(Alb S₁) up to |w| = 48^{3/2} is not.')
    append(L, 'C.1. ',
           '**After K1** the modulus at z₁ and D_part(z₁) are proved: check the isogeny argument of K1 and do not '
           'derive the modulus again. What this item now asks: the argument of ϑ₁((2−ρ)/3, ρ)/η(ρ), and with it '
           'β^part(z₁); the same isogeny argument at τ = i with α = 1 + i, as the re-derivation of R3; and the general '
           'identity that the argument proves, log N(αz) = Σ_{v ∈ ker α} log N(z + v) for every endomorphism α of a '
           'curve with complex multiplication, with its consequence for the product of N over the non-zero points of '
           'ker α, stated and proved in the generality in which C.4 and C.5 use it. The two derivations named in '
           'Lead 7 then test the normalizations of Leads 13 and 14.')
    append(L, 'C.2. ',
           '**After K1 and K2**, j(Alb S₂), its natural boundary, the two radii of Lead 12 and the non-existence of a '
           'proper flat extension across |w| = 216 are proved in S6_02_PUSH: check them and do not prove them again. '
           'What this item now asks: κ₁ with its real part and its branch; q(Alb S₁) = −w²/48³ with its sign; the '
           'relation q(Alb S₁) = (27/64)·q(Alb S₂)²; the holomorphy of j(Alb S₁) beyond the boundary of the family; '
           'and the statement on the real structures.')
    append(L, 'C.3. ',
           '**After K3** the leading terms at τ = i and the identity are proved: check them, and go on to the next '
           'term of each expansion and to τ = ρ. At τ = ρ use K4: g₂(ρ) = 0, so on ordinary charts near ρ the '
           'derivative formula reduces to a multiple of Z², and D_part is superharmonic; pass to the root chart at '
           'the elliptic point.')
    append(L, 'C.8. ',
           '**After checkpoint 01:** K6 is a second, independent certificate for R4; this item still asks for the '
           'proof without enumeration. K4 gives a fourth route: the critical points of D_part on the base lie in the '
           'zero sets of Z and of 3Z℘′ − 2g₂, and D_part is superharmonic; determine every critical point from these '
           'two equations by explicit estimates, and with them the global topology of the level sets, which is the '
           'statement S6_02_PUSH has open as its D.4.6. K5 gives the level sets just above the maximum.')
    insert_after(L, '- **The return of the run S6_02_FAMILY**', M05)
    out = os.path.join(P, 'S6_05_ARITHMETIC', 'PROMPT.md')
    io.open(out, 'w', encoding='utf-8', newline='\n').write('\n'.join(L))


# ---------------------------------------------------------------- zips
def sha(data):
    return hashlib.sha256(data).hexdigest()


def rebuild(folder, zipname, notes_file, extra):
    """extra: list of (source path, path in zip, origin, why)."""
    before = os.path.join(P, folder, zipname.replace('.zip', '_before_20261115.zip'))
    out = os.path.join(P, folder, zipname)
    new = [(os.path.join(INTAKE, notes_file), 'S6_CHECKPOINT_01_20261115.md',
            'compiled 15 November 2026 by Claude (Fable 5.2, effort high) from the two checkpoints; unverified',
            'the results of checkpoint 01 that this prompt builds on, each with its status and source file')] + extra
    rows = []
    blobs = []
    for src, rel, origin, why in new:
        data = open(src, 'rb').read()
        if b'user' in data:
            raise SystemExit('name found in ' + src)
        rows.append('\t'.join([rel, origin, str(len(data)), sha(data), why]))
        blobs.append((rel, data))
    with zipfile.ZipFile(before) as zin, zipfile.ZipFile(out, 'w', zipfile.ZIP_DEFLATED) as zout:
        names = set(zin.namelist())
        for rel, _ in blobs:
            if rel in names:
                raise SystemExit('already in zip: ' + rel)
        for info in zin.infolist():
            data = zin.read(info.filename)
            if info.filename == 'MANIFEST.tsv':
                text = data.decode('utf-8').rstrip('\n') + '\n' + '\n'.join(rows) + '\n'
                data = text.encode('utf-8')
            zout.writestr(info, data)
        for rel, data in blobs:
            zout.writestr(rel, data)
    with zipfile.ZipFile(out) as z:
        bad = z.testzip()
        print(folder, 'entries', len(z.namelist()), 'bad', bad, 'bytes', os.path.getsize(out))


def sec(run_dir, run, name, rel, why):
    return (os.path.join(run_dir, name), 'checkpoint_01/' + rel, ORIGIN % run, why)


def main():
    edit_04()
    edit_05()
    rebuild('S6_04_MAPS_MANIFOLDS', 'S6_04_MAPS_MANIFOLDS_background.zip', 'S6_04_CHECKPOINT_01_20261115.md', [
        sec(PUSH, 'S6_02_PUSH', r'sections\AB_push.tex', 'S6_02_PUSH_AB_push.tex', 'K13: untwisted X(u), the nodal plumbing and its refinements'),
        sec(PUSH, 'S6_02_PUSH', r'sections\C_push.tex', 'S6_02_PUSH_C_push.tex', 'K2-K7, K9, K10: the monodromy class in Theta_7'),
        sec(PUSH, 'S6_02_PUSH', r'sections\C_closing_cocycle.tex', 'S6_02_PUSH_C_closing_cocycle.tex', 'K8: the closing map'),
        sec(PUSH, 'S6_02_PUSH', r'sections\E_push.tex', 'S6_02_PUSH_E_push.tex', 'K1, K2, K11, K12: the dictionary, the higher twists, the two-parameter family'),
        sec(PUSH, 'S6_02_PUSH', r'sections\conventions_push.tex', 'S6_02_PUSH_conventions_push.tex', 'conventions of that run'),
        sec(PUSH, 'S6_02_PUSH', 'S6_02_PUSH_results.csv', 'S6_02_PUSH_results.csv', 'the full register of that checkpoint'),
        sec(CDP, 'S6_03_CDP', r'sections\part_D.tex', 'S6_03_CDP_part_D.tex', 'K14: the threefold of Wang'),
        sec(CDP, 'S6_03_CDP', r'sections\part_C2_C4_C5.tex', 'S6_03_CDP_part_C2_C4_C5.tex', 'K15: Euler localization and the toric rank-two values'),
        sec(CDP, 'S6_03_CDP', r'sections\conventions.tex', 'S6_03_CDP_conventions.tex', 'conventions of that run'),
        sec(CDP, 'S6_03_CDP', 'S6_03_CDP_results.csv', 'S6_03_CDP_results.csv', 'the full register of that checkpoint (K16 is read from it)'),
    ])
    rebuild('S6_05_ARITHMETIC', 'S6_05_ARITHMETIC_background.zip', 'S6_05_CHECKPOINT_01_20261115.md', [
        sec(PUSH, 'S6_02_PUSH', r'sections\D_push.tex', 'S6_02_PUSH_D_push.tex', 'K1-K5: the values at z_1, the boundary, the expansion at i, the derivative of D'),
        sec(PUSH, 'S6_02_PUSH', r'sections\E4_push.tex', 'S6_02_PUSH_E4_push.tex', 'K6: the second certificate'),
        sec(PUSH, 'S6_02_PUSH', r'sections\conventions_push.tex', 'S6_02_PUSH_conventions_push.tex', 'conventions of that run'),
        sec(PUSH, 'S6_02_PUSH', 'S6_02_PUSH_results.csv', 'S6_02_PUSH_results.csv', 'the full register of that checkpoint'),
        sec(CDP, 'S6_03_CDP', r'sections\part_E_rank.tex', 'S6_03_CDP_part_E_rank.tex', 'K7: rank divisors of the root Kodaira-Spencer morphism'),
    ])


if __name__ == '__main__':
    main()
