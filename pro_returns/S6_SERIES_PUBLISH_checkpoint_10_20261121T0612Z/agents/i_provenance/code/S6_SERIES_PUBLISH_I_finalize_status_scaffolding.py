from pathlib import Path
import csv
import datetime
import hashlib
import json
import re

ROOT = Path('/workspace/scratch/653608133b22')
P = ROOT / 'work/agents/i_provenance'
SOURCE = ROOT / 'work/S6_SERIES_PUBLISH_I.tex'
BIB = ROOT / 'work/S6_SERIES_PUBLISH_references.bib'
NOW = datetime.datetime.now(datetime.timezone.utc).isoformat()
source = SOURCE.read_text()
source_sha = hashlib.sha256(SOURCE.read_bytes()).hexdigest()
pin = '83d76022bcd442278b760db9ff438afceed6c6ea'
pin_url = 'https://github.com/KokunoYumeto/s6-complex-structure-workbench/tree/' + pin

def save(name, value):
    (P / name).write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n')

def main_statement(letter):
    i = source.index('\\label{series:I:' + letter + '}')
    a = source.rfind('\\begin{maintheorem}', 0, i)
    b = source.index('\\end{maintheorem}', i) + len('\\end{maintheorem}')
    return source[a:b]

queries = [
    {'q': 'complex six-spheres Bott Chern cohomology h11', 'domains': ['arxiv.org', 'alpo.ge'], 'recency': 120},
    {'q': 'complex six-spheres Picard twists tangent deformations Du Guo Kang Xiao', 'domains': ['arxiv.org'], 'recency': 120},
    {'q': 'six-sphere degeneration logarithmic transformations Engel', 'domains': ['arxiv.org'], 'recency': 120},
    {'q': 'six-sphere "natural boundary" OR "Chabauty" OR "Hausdorff"', 'domains': ['arxiv.org'], 'recency': 120},
    {'q': '"complex six-spheres" "Picard"', 'recency': 120},
    {'q': '"six-sphere" "Bott-Chern" Alpöge', 'recency': 120},
    {'q': '"six-sphere" logarithmic degeneration Engel', 'recency': 120},
    {'q': '"torus" "six-spheres" "boundary"', 'recency': 120},
]
search = {
    'recorded_utc': NOW,
    'engine': 'system1_search_query',
    'queries': queries,
    'raw_result': 'literature/S6_SERIES_PUBLISH_I_DG_status_search_raw.json',
    'direct_primary_opens': [
        {'url': 'https://arxiv.org/abs/2610.00250', 'ref': 'turn660718013view0', 'finding': 'Current official version is v2, revised23October2026; its current title and abstract concern Oka geometry. Version-specific v1 deformation/classification citations remain necessary.'},
        {'url': 'https://arxiv.org/abs/2609.38442', 'ref': 'turn660718013view1', 'finding': 'Official Engel version remains v1,25pages,29September2026.'},
        {'url': 'https://alpo.ge/s6.pdf', 'ref': 'turn660718013view2', 'finding': 'Official108-page primary PDF opened. Its retained actual-page receipts supply the exact theorem/remark comparisons. Direct redownload returned403, so current binary equality is not claimed.'},
    ],
    'additional_primary_results': [
        'Engel author homepage, https://people.math.harvard.edu/~engel/, gives the elliptic-surface/logarithmic interpretation and links the paper.',
        'McHugh arXiv1708.03251 and the primary journal article Narrowing Cohomology for Complex S6 provide general Bott–Chern/Aeppli background; the receiving paper applies explicitly cited general identities to its computed invariants.',
    ],
    'excluded_as_independent_evidence': [
        'The series own Hexagon page and PaperV PDF returned by search; these are the work under review, not an external novelty check.',
        'Third-party arXiv mirrors and unrelated results; operative scope claims use the official or author/institution primary texts.',
    ],
    'outcome': 'The returned primary sources do not change the exact source/application division recorded below. This bounded search does not establish exhaustive novelty, general literature absence or priority.',
    'mathematical_check_events': 0,
}
save('S6_SERIES_PUBLISH_I_DG_literature_search_scope.json', search)

rows = [
    {'id': 'I-D-status-01', 'main': 'series:I:D', 'claim': 'The numerical Hodge table and the evaluated connecting scalar.', 'records': 'Current mainD and root global_DE_derivation: delta=-i C4/4 is nonzero and gives h12=1,h11=2.', 'primary': 'AC2026 Theorem9.1(vi)p65 and Proposition9.20p80 prove the holomorphic-form vanishings; Remark9.21p81 leaves h12 undetermined and records its expected value1.', 'relation': 'The receiving calculation supplies the scalar and evaluates the remaining integer in that same marked family.', 'status': 'Additional evaluated content beyond the cited AC statements; credit their vanishings and one-integer reduction.'},
    {'id': 'I-D-status-02', 'main': 'series:I:D', 'claim': 'Full Bott–Chern/Aeppli dimensions, four Frolicher arrows and square-zero positive-degree algebra.', 'records': 'Current D; root global_DE_derivation points to inv:C1.1,C2.1,C3.3, with h=1 and the four rank-one d1 arrows.', 'primary': 'The already opened McHugh v4 Theorem6.3p20, Proposition6.4p23, equation(7)p23 and Section7.1pp24–25 give general dimension relations; Angella v2Section4pp13–16 and Figure5p16 give general complex-six-sphere constraints.', 'relation': 'The receiving paper inserts the computed invariants into the general identities and proves the multiplication law for its actual classes.', 'status': 'General identities credited; numerical specialization and explicit algebra are receiving-paper content.'},
    {'id': 'I-D-status-03', 'main': 'series:I:D', 'claim': 'Ordinary relative differentials retain degree and scheme multiplicity.', 'records': 'Current D displays the modules for t=xy,t=xyz,t=s^m and the distinct degree-one/degree-two torsion supports.', 'primary': 'AC2026 Remark9.21p81 says Omega1 relative has torsion along W union S1 union S2; Remark1.3p5 discusses the needed ordinary relative modules.', 'relation': 'The receiving quotient R^3/R(yz,xz,xy) is torsion-free at the cusp, while its degree-two exterior quotient has the displayed conductor torsion. At a multiple fibre the quotient is by s^(m-1), not merely its reduction.', 'status': 'Exact local-module correction of the cited ordinary degree-one cusp-torsion statement; retain the equation-level comparison.'},
    {'id': 'I-D-status-04', 'main': 'series:I:D', 'claim': 'Specified global coefficient atlas for G and Q.', 'records': 'Current D and inv:C3.8 give the locally finite weights, scalar/one-form Cech cocycles and complete coefficient recursion.', 'primary': 'The opened AC and general cohomology sources supply the period/fibre classes and general identities, not this particular common-refinement coefficient formula.', 'relation': 'The displayed representatives satisfy [G]=g_gamma, i_b*[Q]=eta and exp(12[G])=f*O(1) via the receiving atlas maps.', 'status': 'Explicit representative construction in the receiving paper; avoid claiming an exhaustive literature first.'},
    {'id': 'I-E-status-01', 'main': 'series:I:E', 'claim': 'Untwisted tangent tuple, smooth reduced Kuranishi line, local miniversality and full automorphism group.', 'records': 'Current E specializes the integral-twist formula at n=0 and retains the credited re-derived proofs.', 'primary': 'DGKX arXiv2610.00250v1 Theorems1.3–1.4p3, Theorem6.12pp81–82, Proposition6.16p85 and Theorem7.14p95 already give these standard-family conclusions.', 'relation': 'Identify the source parameter by a=c+(beta_part-beta0), with the constant difference and the same affine/period arrows; the derivative and the period2Z are preserved by this translation.', 'status': 'Known standard-family conclusions, explicitly re-derived under the user-required appendix exception. The current v2 must not be cited as though it contains the omitted v1 statements.'},
    {'id': 'I-E-status-02', 'main': 'series:I:E', 'claim': 'All Picard twists and the actual locally discrete tangent-cohomology jump loci.', 'records': 'Current E gives all integral twists by U,V,epsilon and every nonintegral twist by distinct regular resonance points plus finite/cusp lengths.', 'primary': 'The exact opened DGKXv1 locators above concern the untwisted tangent bundle of the standard family. AC provides the Picard/structure-sheaf inputs used by the receiving calculation.', 'relation': 'The receiving primitive coordinate M_n=O(n(S1-S2)) and resonance equations specify the extension from n=0 to every M_z; the n=0 tuple agrees with DGKX.', 'status': 'All-twist formulas and local-discreteness proof are additional content beyond those cited standard-family statements.'},
    {'id': 'I-E-status-03', 'main': 'series:I:E', 'claim': 'Coprime (3k,4l) tangent cohomology and local miniversality for every fixed sphere datum.', 'records': 'Current E and push:E2.1 specify the weighted root stack P(3k,4l), z0=kl, d0=3k+4l, E=O+O(-z0), canonical line and the groupoid KS classes.', 'primary': 'DGKXv1 gives the standard (3,4) case and its groupoid/normal-line mechanism. Douady1974 VII.8pp598–599 and VIII.1p600 supply deformation existence/naturality at their opened scope.', 'relation': 'At k=l=1, the receiving bundle and direct-image expressions specialize to DGKX. For general coprime k,l, the actual root weights and the same e tensor gamma derivative are computed in the body.', 'status': 'Explicit higher-multiplicity application and extension; general deformation existence is credited, and the receiving nonzero KS map proves its local miniversality.'},
    {'id': 'I-F-status-01', 'main': 'series:I:F', 'claim': 'Partial semistable fillings and obstruction to every proper Hausdorff analytic filling for the admissible logarithmic data.', 'records': 'Current F and its cited body proofs retain the component cover and the two exact origin deck differences; the radial class is -pn gamma.', 'primary': 'Engelv1 Remark8.1p22 supplies the parameter-degeneration context. Proposition2.8pp6–7 supplies periodic triangular cusp fillings. These cited passages do not state the receiving all-data, all-finite-cover filling obstruction.', 'relation': 'The coefficient p=12l0-4l1-3l2 (or its higher-multiplicity analogue) is the same integer computed from the logarithmic translations; the obstruction is transported through the displayed origin difference, not inferred from a generic toric degeneration.', 'status': 'Receiving-paper obstruction and component calculation, with exact maps to the prior geometric construction. No blanket claim that the two constructions are unrelated.'},
    {'id': 'I-F-status-02', 'main': 'series:I:F', 'claim': 'Untwisted quotient admits a proper flat filling, while the particular one-component model in EngelConjecture8.2 fails its Euler test.', 'records': 'Current F refers to the two-projective-line-bundle plumbing, proper modification and finite quotient; the chosen small-resolution marking is being reconciled by the topology agent.', 'primary': 'Engelv1 Conjecture8.2p22 specifies the proposed one-component central model; the current source page was actually read. Proposition2.8 allows the triangular fan construction without prescribing PaperI’s labelled anti-diagonal.', 'relation': 'Setting the logarithmic data to zero gives p=0 and zero corner winding. The explicit plumbing maps construct the filling, while the proposed single central model has virtual Euler0 versus e(X(u))=2.', 'status': 'Exact proposed-model correction and explicit filling; retain the topology agent’s final selected-diagonal correction before declaring the global statement finalized.'},
    {'id': 'I-G-status-01', 'main': 'series:I:G', 'claim': 'No flat proper continuation through any point of |w|=216.', 'records': 'Current G uses the intrinsic divisor2S2 and its Albanese nome iw/216 to transport the modular invariant to a proposed continuation.', 'primary': 'AC2026 canonical/anticanonical statements provide intrinsic fibration inputs. The modular invariant and its cusp behavior are classical; the current body supplies the exact pullback and continuation argument.', 'relation': 'The concrete map w->iw/216 identifies the outer circle with the nome unit circle; the intrinsic divisor supplies the same invariant in every putative family.', 'status': 'Receiving boundary application; credit the classical modular input and retain the exact intrinsic Albanese transport.'},
    {'id': 'I-G-status-02', 'main': 'series:I:G', 'claim': 'All Hausdorff reflections and marked additive lattice limits.', 'records': 'Current G specifies the four period vectors, L_a, primitive K and the limiting homomorphism ell; topology’s global check owns the exact occurrence proof.', 'primary': 'Cornulier2011 Theorem3.1p2017, proofp2018, gives the duality map used for closed-group convergence; its primary pages were actually viewed by the topology agent.', 'relation': 'The annihilator map is applied to the real vector space underlying C², with the receiving integral-label equations. The rational/irrational outcomes follow from those exact equations and scales.', 'status': 'Classical closed-group duality credited; explicit complete limit classification is receiving-paper content.'},
]
payload = {'recorded_utc': NOW, 'source_sha256': source_sha, 'scope': 'Literature-status and provenance comparison only. No new proof, numerical check, count refresh or final-PDF reading is claimed.', 'search_receipt': 'S6_SERIES_PUBLISH_I_DG_literature_search_scope.json', 'rows': rows, 'main_statement_sha256': {L: hashlib.sha256(main_statement(L).encode()).hexdigest() for L in 'DEFG'}, 'remaining_gate': 'Bind final F selected-diagonal correction and final root source/count snapshot; no mathematical checking event is created by this table.'}
save('S6_SERIES_PUBLISH_I_DG_literature_status.json', payload)
md = ['# Paper I: D–G literature-status comparison', '', 'Source SHA256: `' + source_sha + '`.', '', 'This is a bounded literature/source comparison, with zero mathematical events. The search supports the specific source/application division below; it does not prove exhaustive novelty or priority.', '']
for r in rows:
    md += ['## ' + r['id'] + ': ' + r['claim'], '', '**Records.** ' + r['records'], '', '**Opened primary scope.** ' + r['primary'], '', '**Exact relation.** ' + r['relation'], '', '**Disposition.** ' + r['status'], '']
(P / 'S6_SERIES_PUBLISH_I_DG_literature_status.md').write_text('\n'.join(md))

# Bibliography corrections, guarded against the current receiving files.
bib = BIB.read_text()
inline_changes = []
old = r'\newblock Generalized logarithmic transformations---elliptic bundle case.'
new = r'\newblock Logarithmic transformations on elliptic fiber spaces. II.---elliptic bundle case.'
assert source.count(old) == 1
inline_changes.append({'id': 'I-Fujimoto-primary-title', 'old': old, 'new': new, 'reason': 'Current primary title page actually read by topology agent; preserve the existing citation key and proceedings metadata.'})
old = '\\url{https://mathweb.tifr.res.in/Documents/Publications/Lectures/tifr58.pdf}.\n\\newblock \\emph{Verified}.'
new = '\\url{https://mathweb.tifr.res.in/Documents/Publications/Lectures/tifr58.pdf}.\n\\newblock Citations use the page numbers of this official TIFR retypeset edition.\n\\newblock \\emph{Verified at the cited loci}.'
assert source.count(old) == 1
inline_changes.append({'id': 'I-Oda-retypeset-pages', 'old': old, 'new': new, 'reason': 'Official catalogue distinguishes the retypeset foliation from original marginal page numbers; current citations use the retypeset foliation.'})
shared_changes = []
for key in ['Oda1978D', 'Fujimoto1990AB']:
    m = re.search(r'@\w+\{' + key + r',', bib)
    end = bib.find('\n@', m.end())
    oldentry = bib[m.start():end if end >= 0 else len(bib)]
    newentry = oldentry
    if key == 'Oda1978D':
        source_note = 'Current run actually viewed official TIFR retypeset Section13 pp116--118 (PDF128--130), and Theorem15.1 plus following paragraph pp130--131 (PDF142--143),21November2026. Historical additional verification scopes remain in the attached records.'
        note = 'Official retypeset edition; original page numbers appear in the margins. Citations use retypeset page numbers. Current primary receipt: S6_SERIES_PUBLISH_I_Oda1978_locator_receipt.json.'
    else:
        newentry = newentry.replace('title = {Generalized Logarithmic Transformations---elliptic bundle case}', 'title = {Logarithmic Transformations on Elliptic Fiber Spaces. II.---elliptic bundle case}')
        source_note = 'Current topology agent actually viewed primary HUSCAP title p81, Cartier construction p85, Definition1.1 and Remark1.4p86, Proposition1.14pp92--93 and Example1.15pp93--94. The DOI identifies the full proceedings. The source leaves general relative compactification open in Example1.15.'
        note = 'Current primary receipt: S6_SERIES_PUBLISH_I_Fujimoto_Cartan_Fujiki_primary_receipt.json. Title and exact page scopes corrected21November2026; historical wording retained in the guarded comparison record.'
    newentry = re.sub(r'  source_note = \{[^\n]*\},', '  source_note = {' + source_note + '},', newentry)
    newentry = re.sub(r'  verification = \{[^\n]*\},', '  verification = {verified at current listed scope},', newentry)
    newentry = re.sub(r'  note = \{[^\n]*\}', '  note = {' + note + '}', newentry)
    assert oldentry != newentry
    shared_changes.append({'id': 'I-bib-current-' + key, 'old': oldentry, 'new': newentry, 'reason': 'Replace inaccurate title or pagination wording by exact current primary receipts, preserving historical text in this guard.'})
save('S6_SERIES_PUBLISH_I_primary_citation_guards_07.json', {'source_sha256': source_sha, 'changes': inline_changes})
save('S6_SERIES_PUBLISH_I_shared_bib_guards_07.json', {'bib_sha256': hashlib.sha256(BIB.read_bytes()).hexdigest(), 'changes': shared_changes})

print('Wrote11 D–G status rows,8 recorded queries,2 inline and2 shared-bibliography guards; zero math events.')
