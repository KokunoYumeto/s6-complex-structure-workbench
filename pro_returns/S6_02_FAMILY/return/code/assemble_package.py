"""Combine section ledgers and research records, checking every prompt item."""
from pathlib import Path
from collections import Counter
import csv, re, sys

ROOT=Path(__file__).resolve().parents[1]
FIELDS=['id','statement','status','where_proved','depends_on','item_of_the_prompt',
        'findings_of_the_survey_settled (F-numbers)','notes']
rows=[]
for part in ['AB','CD','E','F']:
    with (ROOT/'sections'/f'{part}_results.csv').open(newline='',encoding='utf-8') as f:
        reader=csv.DictReader(f)
        assert reader.fieldnames==FIELDS,(part,reader.fieldnames)
        rows.extend(reader)
ids=[r['id'] for r in rows]
assert len(ids)==len(set(ids))
statements={}
for part in ['AB','CD','E','F']:
    text=(ROOT/'sections'/f'{part}.tex').read_text()
    for ident,status in re.findall(r'\\begin\{(?:theorem|proposition|lemma|corollary|problem|remark)\}\[([A-F]\.\d+\.\d+);\s*([^\]]+)\]',text):
        assert ident not in statements,ident
        statements[ident]=status.split(',')[0].strip()
assert set(ids)==set(statements),{'ledger_only':set(ids)-set(statements),'paper_only':set(statements)-set(ids)}
for row in rows:
    assert row['status']==statements[row['id']],(row['id'],row['status'],statements[row['id']])
with (ROOT/'S6_02_FAMILY_results.csv').open('w',newline='',encoding='utf-8') as f:
    writer=csv.DictWriter(f,fieldnames=FIELDS);writer.writeheader();writer.writerows(rows)

items=[f'{part}.{i}' for part,n in [('A',5),('B',4),('C',4),('D',2),('E',2),('F',3)] for i in range(1,n+1)]
by_item={item:[r['id'] for r in rows if item in re.split(r'[;, ]+',r['item_of_the_prompt'])] for item in items}
assert all(by_item.values())
outcomes={item:'(a)' for item in items}
outcomes.update({'B.2':'(b)','D.1':'(b)','F.2':'(b)','C.3':'(c) — unfinished','E.1':'(c) — unfinished','E.2':'(c) — unfinished'})
missing={item:'None within the stated prompt scope.' for item in items}
missing.update({
 'B.3':'Complete for Viaclovsky’s stated coprime sphere multiplicities and admissible vectors; the comparison gives step 2klZ.',
 'C.3':'Compact replacement across the boundary, including the collapsed order-four neighbourhood, remains unconstructed. The actual rank-three quotient, its separation properties, and the Albanese natural boundary are proved.',
 'E.1':'Equivariant periodic gluing at xy=u*z*v with the prescribed general Mumford resolution and proposed central normalization.',
 'E.2':'Compatible nonreduced finite-fibre neighbourhoods and infinity filling, and descent of the auxiliary base change. Global central topology is therefore uncomputed. The smooth monodromy is reduced to the explicit invariant permitted in the prompt.'})
table=['| Item | Statements | Outcome | Missing work / exact scope |','| --- | --- | --- | --- |']
table += [f"| {i} | {', '.join(by_item[i])} | {outcomes[i]} | {missing[i]} |" for i in items]
body=r'''

# S6_02_FAMILY research record

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 12 November 2026. No human authorship or priority is claimed for this deliverable. Source authors are named only in citations to their own works.

**This is a partial research package with three unfinished prompt items: C.3, E.1 and E.2.** Every one of the twenty items has numbered mathematics, and each unfinished item contains constructed cases, executed computations, and a specific smallest remaining target. The compact degeneration is not presented as settled.

## Principal mathematical outcomes

For the original retained sphere data, A.1–A.5 prove that the fibration is intrinsic, that every biholomorphism preserves its base, and that `X_c ≅ X_cprime` exactly for `cprime-c ∈ 2Z`. The local cyclic-cover lifts, integral norm obstruction, cusp-stratum maps, collar identities, coherent shift action, and proper family descent are written out. The automorphism group is exactly C*, including its components. Under the declared cusp normalization, the conjugate member is `X_(1-barc)`, so the real locus in the parameter disc is `w=-barw`.

A.5.2 also proves `h^q(X_c,T_Xc)=(1,1,1,0)` and a smooth reduced one-dimensional Kuranishi germ for every admissible retained member. The family is locally miniversal. The calculation uses an actual morphism to the root curve P(3,4), pointwise base change on its finite atlases, a multiplicative cusp resolution, the nonzero gamma class, and the branchwise normal-derivative quotient. The invariant-exponent calculation is independently checked in code. It answers the small-deformation question for the retained (3,4) family.

For all admissible (3,4) discrete data, including arbitrary cusp sections and both fibre-linear signs, the complete invariants are

`(|p|, exp(-pi*i*(c+k2)))`, with `p=12*l0-4*r1-3*r2`.

The proof gives exactly two sphere classes at fixed Engel u, interchanged by a circuit around zero. For coprime sphere multiplicities `(3k,4l)`, B.3.1 gives every norm congruence; the fixed-data shift subgroup is `2klZ`, and fixed u has `2kl` classes in one cycle. The explicit integral marking matrix on the first page fixes the signs in the dictionary.

With `(beta_part+tau)(infinity)=0` and Engel’s reference linearization chosen to be the transported period lift at c=0, the scalar is `lambda0=1` and `u=w^2`. The theta formula for beta is proved from its actual transformation laws. The global maximum is

`M=-(3/pi)*log(6) = -1.71100425815613411418…`, attained only at `t=1`.

Consequently the exact class disc is `0<|w|<216`, and the corresponding quotient parameter disc is `0<|u|<46656`. These values include the declared reference choice; rescaling that reference changes the u radius by the explicit scalar in B.1.4. They are not claimed invariant under such a rescaling.

The maximum proof combines a quantitative analytic neighbourhood of tau=i, an analytic cusp bound for Im(tau)>=2, and a completed outward interval cover of the remaining compact region. The independent partition checker verifies 19,911 exact rational leaves: 19,701 strict norm certificates, 36 local-proof boxes, and 174 exact exclusions outside the modular domain. There are zero pending or undecided boxes. The exact rational area is 23/40. The largest reported squared-norm bound is `9999999982782673130994674616307871/5000000000000000000000000000000000`, strictly less than 2. Thus the numerical exploration has been replaced by a global proof.

Part D gives an exact classification for every smooth fibre through the displayed six-integer Neron–Severi equation. Nonzero isotropic integral classes give the elliptic-quotient locus; negative Pfaffian classes give the abelian locus, with the sign derived from the complex orientation. These explicit countable zero sets determine algebraic dimensions zero, one and two. They are exact equations, not a finite list of exceptional t-values. All compact curves are classified through their actual elliptic-kernel, theta-section, finite-cover, or normalization maps. All irreducible compact surfaces are reduced fibres. Rational curves occur only in W, while ordinary fibres do contain elliptic curves.

Part F determines the monodromy group as an explicit integral central extension and an index-twelve subgroup of the primitive-vector stabilizer (index twenty-four in the line stabilizer). Its Zariski closure and Levi image are proved. Full-domain properness is false: a displayed rational complex structure has an infinite integral unipotent stabilizer. The largest proper-action open set is exactly `psi(delta_hat,J*delta_hat) != 0`. Every admissible period lies in its positive component. The quotient period curve is an injective immersion; adding the two finite punctures gives a proper embedded affine line, and the cusp escapes compact subsets.

## Corrections and dispositions of the proposed leads

| Source / claim | Disposition and exact correction |
| --- | --- |
| Lead 1 | Proved by the exact centralizer and the two integral norm images, including the normalized-cover lift and exact generator commutation. |
| Lead 2 | Proved with the stated finite translations, cusp cocharacter, vanishing H1 of the correction sheaf, and coherent cocycle identity. |
| Lead 3 | Proved, including the precise Albanese moduli and their j-functions. The generic necessity argument has an explicitly countable exceptional set, and the full classification uses the integral norm proof. |
| Lead 4 | Proved for the positive linear part and extended to both signs and arbitrary cusp data. The resulting complete invariant uses absolute p together with the corrected exponential coordinate. |
| Lead 5 | Proved with the explicit branch `exp(2*pi*i*mu0)=-(5+2*sqrt6)`, the zero-of-wp identification, and gluing units `(-a^-1,a^6,-a^-7*w^2)`. Every hexagon automorphism is checked to obtain the abstract surface criterion `cprime-c ∈ Z`. |
| Lead 6 | **False in its unrestricted elliptic-quotient wording.** At t=32/5 the section has exact order four, yet the explicitly admissible member in D.1.3 has a surjection onto E_t with connected elliptic kernel. The four period images under `3*zeta1+4*zeta2` are `(-101*tau,2*tau+2,3,4)` and generate the target lattice. The specified first-coordinate projection has the exact two-point criterion claimed in the workbench. D.1.6 gives the full replacement for arbitrary elliptic quotients. |
| Lead 7 | Proved for the full automorphism group; B.4.2 additionally gives all antiholomorphic maps and the split extended group on the real locus. |
| Engel Remark 8.1 | The fixed-sphere-data family requires the double-cover qualification `u=w^2` for global descent. B.2.3 supplies two independent obstructions to descent over the original u-disc, and constructs the corrected global family and valid local u-families. |
| Engel shift-vector comparison | In the first-page integral marking and declared root orientation, `c -> c+1` gives `(a0,a1) -> (a0-delta/3,a1+delta/4)`. B.2.2 supplies the actual lattice and complex-period comparison maps fixing this sign. |
| Course, cusp-and-compact-threefold §10.2 | For its displayed section `P_*=(0,sqrt2*t^2*(t-1))`, the chart value `Y2=y/t^2` tends to `-sqrt2`. Its component label must be `E_(2,-)`. Both endpoint inverse-Cartan entries equal 4/3, so the height conclusion survives. |
| AC26 Lemma 9.4, orientation comparison | The formal coefficient `eta wedge eta=12 vol` is correct. The displayed period map has real determinant `T*D<0`, so its integral in the complex orientation is -12. D.1.4 gives the exact comparison; it does not call the coefficient identity false. |
| Rank-three boundary quotient | Real rank three of the period matrix does not guarantee a discrete image of Z^4. C.3.1 gives the exact rational-kernel criterion. The quotient is noncompact in the discrete case and non-Hausdorff in the other case. |
| Klingler full-domain proposal | False for the actual monodromy group and the full line parabolic. F.2.1 is a complete exact counterexample; F.2.2 supplies the uniquely largest invariant proper-action open set. |

## Sources actually read

The archive identity check verified all 43 manifest entries, including nine PDFs totalling 329 pages. This count records file identities, not a claim to have read every page. The report sections below state the inspected locations. The original AC26 PDF was extracted and compared with its supplied transcription; page66 was visually inspected for the orientation-sensitive formula. Engel’s initial construction, line-bundle lemma and proof, finite modifications, integral monodromy, and final questions were read directly.

Yang’s Section6.2 and Viaclovsky’s logarithmic-transform Theorem1.1, Questions1.1 and Proposition4.7 were read for their exact hypotheses and comparison maps. The introductions and principal stated results of the two-parameter, combs, Liu–Rollenske, and Wang papers were inspected to delimit the present period system. The attached Duke–Imamoglu theorem and its relation to Eichler–Zagier were read; our required zero and cusp constant are independently derived, and no unopened original Eichler–Zagier text is a premise.

Public searching located arXiv:2610.00250v1 and its later v2. The historical version states the classification and deformation results; the current version omits those sections. We checked the actual v1 argument rather than drawing a conclusion from that version change. A.5.2 gives the written derivation, and `ab_deformation.py` checks its root-character arithmetic and local algebra. The source versions have separate verified bibliography entries. No reason for the deletion and no priority is asserted.

The public search queries, dates and primary URLs are in `evidence/literature_search_log.md`. The mathematical derivations from Schnell’s Appell–Humbert and Riemann criteria, and from the Cerf/Smale/Eells–Kuiper comparisons, are explicit in the paper. Every bibliography entry says `verified` and records what was opened.

## Executed computations and their evidentiary roles

| Program group | Arithmetic / precision | Independent comparison and role |
| --- | --- | --- |
| `ab_exact.py`, `ab_geometry.py` | Exact integer and rational | Centralizer, norms, Smith/Hermite forms, product lattices, affine identities, cocharacters, automorphism cocycles, geometric-height and conjugation checks. Proofs establish extension and global gluing. |
| `ab_deformation.py` | Exact integer and rational | 481 weighted root characters compared by coarse invariant exponents and weighted monomial counts; cusp cup, gamma class, Leray terms, and volume/normal calculations checked. |
| `cd_numerics.py`, `cd_periods.py`, `cd_special_intervals.py` | 90-digit evaluations; independent 60-digit intervals | Jacobi series versus 120-factor triple product, independent cusp root, and certified special-value intervals. Twenty digits are displayed. |
| `cd_bounds.py`, `cd_local_bound.py` | 50-digit intervals and analytic estimates | Coarse global bound and a quantitative local maximum radius, with explicit analytic tails. |
| `f_interval_cert.py`, `f_interval_parallel.py` | Outward interval arithmetic at 30 decimal digits; rational boxes | Complete strict compact-domain cover. Fourier, theta and eta tails are included. |
| `f_interval_verify.py` | Exact `Fraction` arithmetic | Independently reconstructs the binary partition, area, strict bound comparisons, local omissions and modular-domain exclusions. It checks coverage rather than substituting a second floating-point grid. |
| `cd_multiples_initial.py`, `cd_torsion_independent.py`, `cd_exact.py` | Exact rational polynomial and matrix arithmetic | Independent point addition versus division-polynomial recurrence; torsion roots, counterexample images, Neron–Severi/Pfaffian identities, boundary kernel, and all dihedral gluing actions. |
| `e_degeneration.py` | Exact integer and rational | Translation, local modification, Smith forms and both independent Euler computations; topology assigned only to actually constructed spaces. |
| `f_exact.py` | Exact SymPy and a separate `Fraction` matrix implementation | Integral monodromy, character, group law, null-stabilizer counterexample, orientation/signature and period comparison checked independently. |

The exploratory grid of 5,151 points and early interval experiments are retained and identified as exploratory. The global theorem uses the completed corrected certificate. The two radius computations compare interval exponentials with the exact integers `6^3` and `6^6`. No sampled decimal is used as a substitute for a proof.

All computation outputs are retained beside their scripts. The detailed section records below give the mathematical dependency and precision for each. Source identity, ledger assembly, compiler and visual audit scripts are also included. The rebuild uses LuaLaTeX and BibTeX; the workspace-local bootstrap handles the supplied minimal TeX installation without changing system files. On a configured TeX Live installation the ordinary LuaLaTeX build applies directly.

## Exact remaining targets and smallest instances

**C.3, boundary replacement.** The unique degeneration occurs over t=1 when `Im(c)=(3/pi)*log6`. The exact rank-three quotient and rational/irrational separation criterion are proved. The second Albanese j-function has a natural boundary on the corresponding real parameter line. The smallest missing construction is a compact complex-space replacement for the order-four neighbourhood at this boundary, with the stated nonreduced structure and compatible parameter maps. The quotient calculation and natural-boundary obstruction do not establish nonexistence of every possible compactification.

**E.1, untwisted compact limit.** The projective-line-bundle pushout Q is constructed as a compact complex space, its integral topology is computed, and its proper flat smoothing is constructed over every finite-base disc. The smallest missing point is one lift of the nodal point at infinity, where `xy=u*z*v`. The explicit blow-up resolves the general-fibre node and changes one central branch. The required equivariant periodic gluing must retain the prescribed general Mumford resolution, yield a proper quotient, and settle the proposed central normalization. It has not been constructed or ruled out.

**E.2, sphere-family compact limit.** The two reduced special surfaces have actual semistable finite-quotient fillings after `w=s^6`; their topology is computed. The first missing finite-place germ is the order-three action on a two-parameter plumbing with its original normal character and central multiplicity, followed by descent from s to w. The order-four germ and the infinity filling must be compatible. No global central threefold has been constructed, so no Euler characteristic, fundamental group or homology is assigned to such a limit. The smooth monodromy is identity on integral cohomology and is reduced to the explicit Eells–Kuiper residue of the displayed clutching map, meeting that alternative of the prompt. The numerical residue itself remains unevaluated.

## Detailed section records
'''
sections=[]
for part in ['AB','CD','E','F']:
    sections.append((ROOT/'sections'/f'{part}_report.md').read_text())
report='\n'.join(table)+body+'\n\n'.join(sections)
(ROOT/'S6_02_FAMILY_report.md').write_text(report,encoding='utf-8')
print('NUMBERED_STATEMENTS',len(rows))
print('STATUSES',dict(Counter(r['status'] for r in rows)))
print('PROMPT_ITEMS',len(items))
print('UNFINISHED_ITEMS','C.3 E.1 E.2')
print('All numbered statements and statuses match the paper.')
