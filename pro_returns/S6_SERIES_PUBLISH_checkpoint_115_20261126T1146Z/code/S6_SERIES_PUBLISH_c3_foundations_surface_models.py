from pathlib import Path
import csv
import datetime
import json
import re

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'agents/continuation3_foundations'
LEMMA = 'lem:II:negative-kodaira-models'
lemma = (OUT / 'S6_SERIES_PUBLISH_II_P244_surface_models.tex').read_text()
inputs = {
    'night:P4.15': (OUT / 'S6_SERIES_PUBLISH_II_P244_P415_input.tex').read_text(),
    'night:P4R.2': (OUT / 'S6_SERIES_PUBLISH_II_P244_P4R2_input.tex').read_text(),
}
receiving = dict(inputs)
guards = []
def span(owner, first, after):
    text = receiving[owner]
    return text[text.index(first):text.index(after, text.index(first))]

def change(owner, key, old, new, reason, defect='D12'):
    assert receiving[owner].count(old) == 1, (owner, key)
    receiving[owner] = receiving[owner].replace(old, new, 1)
    guards.append(dict(owner=owner, key=key, old=old, new=new, reason=reason, defect=defect))

change('night:P4.15', 'classification_application',
       span('night:P4.15', 'For a K\\"ahler $T_0$', 'For a projective-line bundle'),
       r'''Lemma~\ref{lem:II:negative-kodaira-models} applies to this smooth
compact minimal $T_0$. In its K\"ahler case, $T_0$ is
$\mathbb P^2$ or a projective-line bundle; in its non-K\"ahler case,
$T_0$ is of class VII with $\chi(\mathcal O_{T_0})=0$.

''',
       'The complete projective embedding and OVV elliptic-to-class-VII arguments have one earlier proved owner P244. The already proved smoothness, compactness, minimality and negative Kodaira dimension map to its exact hypotheses; consumer Chern and Euler calculations stay here.')
change('night:P4.15', 'class_vii_chi_application',
       '''The equalities $b_1=1$, $p_g=0$ and
$b_1=2h^1(\\mathcal O)-1$ give $\\chi(\\mathcal O_{T_0})=0$.
''',
       r'''The invariants in
Lemma~\ref{lem:II:negative-kodaira-models}\textup{(ii)} give
''',
       'Assign the repeated class-VII coherent Euler calculation to P244(ii), retaining the precise invariant used by this consumer.')
# Join the resulting two sentences without changing the Euler formulas.
change('night:P4.15', 'class_vii_euler_join',
       'give\nThus $e(T)=k_0+r$',
       'give\n$e(T)=k_0+r$',
       'Connect the exact invariant application to the unchanged Euler and canonical-square formulas.', 'D23')
change('night:P4.15', 'hopf_application',
       span('night:P4.15', 'By \\cite[Theorem~1, p.~1]{BBK2019}', 'For rational $T$'),
       r'''Its reduced conductor $R$ is a nonempty curve, so
Lemma~\ref{lem:II:negative-kodaira-models}\textup{(iii)}, applied to
this $T$, proves that $T$ is Hopf.

''',
       'The preceding Chern identity gives minimal class VII with b2=0 and ell=0; the conductor was proved nonempty earlier in this proof. P244(iii) now owns the same finite-etale inverse-image and composed universal-cover argument.')
change('night:P4R.2', 'classification_application',
       span('night:P4R.2', 'The classification\ngives rational', 'Blowing up a smooth point'),
       r'''Pluricanonical sections descend across these point blowups by
Hartogs' extension away from their centres, so $\kappa(T_0)=-\infty$.
Lemma~\ref{lem:II:negative-kodaira-models} therefore applies to
the smooth compact minimal $T_0$: its K\"ahler alternatives are
$\mathbb P^2$ and projective-line bundles, and its non-K\"ahler
alternative is class VII with $b_1(T_0)=1$.
''',
       'The full shared reduction is proved once at P244. The actual contraction q supplies the negative-Kodaira-dimension hypothesis by the same pluricanonical descent used in P4.15. Preserve the entire following van Kampen and p_*q_*(nu_*)^{-1} argument.')
change('night:P4R.2', 'hopf_application',
       span('night:P4R.2', 'By \\cite[Theorem~1, p.~1]{BBK2019}', 'The converse follows'),
       r'''The reduced support of this effective divisor is a nonempty
curve. Lemma~\ref{lem:II:negative-kodaira-models}\textup{(iii)}
applies to the resulting minimal class-VII surface $T$ with
$b_2(T)=0$ and proves that $T$ is Hopf. ''',
       'All Hopf-recognition hypotheses are proved at this equality case. P244(iii) owns the identical finite cover and universal-cover composition; the conductor argument, equality criterion and converse remain at this consumer.')
for owner in inputs:
    old = re.search(r'\\StatementRecord\{[^\n]+', receiving[owner]).group()
    new = old[:-1] + r', \SeriesRef{' + LEMMA + '}}'
    change(owner, 'dependency_record', old, new,
           'Record the new single proved premise P244 in the nonprinting dependency apparatus; all existing dependencies and D10 closure remain.', 'D14')

for owner, stem in (('night:P4.15', 'P415'), ('night:P4R.2', 'P4R2')):
    original = inputs[owner]
    revised = receiving[owner]
    assert re.findall(r'\\label\{([^}]+)\}', original) == re.findall(r'\\label\{([^}]+)\}', revised)
    assert re.findall(r'\\hypertarget\{([^}]+)\}', original) == re.findall(r'\\hypertarget\{([^}]+)\}', revised)
    assert original[:original.index(r'\begin{proof}')] == revised[:revised.index(r'\begin{proof}')].replace(
        r', \SeriesRef{' + LEMMA + '}}', '}')
    (OUT / f'S6_SERIES_PUBLISH_II_P244_{stem}_receiving.tex').write_text(revised)

placement = dict(
    insert_before='\\begin{proposition}[Finite rank drop of a normalization]',
    lemma_file='agents/continuation3_foundations/S6_SERIES_PUBLISH_II_P244_surface_models.tex',
    tag='P244', label=LEMMA,
    instructions='Insert the complete P244 lemma immediately before P4.15. Apply only these exact guarded consumer-span replacements, preserving concurrent root edits elsewhere. Complete receiving proofs are supplied for reading/comparison, not as whole-owner overwrite instructions.',
    edits=guards,
)
(OUT / 'S6_SERIES_PUBLISH_P244_guards.json').write_text(json.dumps(placement, ensure_ascii=False, indent=2) + '\n')

def write_tsv(name, header, rows):
    with (OUT / name).open('w', newline='') as stream:
        writer = csv.writer(stream, delimiter='\t', lineterminator='\n')
        writer.writerow(header)
        writer.writerows(rows)

defect_rows = []
for index, edit in enumerate(guards, 1):
    defect_rows.append([
        f'II-C3-P244-{index:03}', edit['defect'], edit['owner'],
        edit['key'], 'cp35; final concordance pending',
        'P244 and exact scoped application at ' + edit['owner'], 'integrated build pending',
        edit['old'], edit['new'], edit['reason'],
        'Complete original and receiving proofs read; exact hypothesis, conclusion and morphism map supplied. Root admission pending.',
    ])
extras = [
    ('D13', 'New common lemma owner', 'Repeated classification and Hopf-recognition paragraphs in P4.15 and P4R.2', lemma,
     'Give the shared mathematical result one numbered owner before both consumers. All existing consumer labels, tags, hypotheses and conclusions stay fixed.'),
    ('D14', 'Earlier premise placement', 'Two duplicated proofs embedded at different locations', 'P244 immediately before P4.15; P4.15 and P4R.2 cite P244 at their exact input scopes.',
     'The shared premise is proved before either use. The local conductor, Euler and fundamental-group deductions remain at their consumer owners.'),
    ('D17', 'Exact literature-to-analytic maps', 'Repeated short transfers from Kodaira, Beauville, OVV, BBK and Inoue', 'One short transfer proof at P244 with the explicit embedding Phi, quotient differential Q to p^*T_B, and finite cover a.',
     'Published theorems retain exact statement/page citations. Their special analytic scope and the curve-to-Hopf transfer are proved once; no published theorem is expanded into a second full proof.'),
    ('D18', 'Common exact citation scope', 'Kodaira Main Theorem cited as p314 in P4.15 and pp314-315 in P4R.2', 'Kodaira Main Theorem and proof pp314-315; all other exact cited loci retained at P244.',
     'The publisher reprint was opened at the actual main theorem and full proof outline. Other source edition/page bindings are retained.'),
    ('D20', 'Repeated local fibration notation', 'P4.15 p:T0 to B0 with R_p; P4R.2 pi:T0 to C0 with R_pi and quotient Q', 'P244 p:T0 to B0, Q=T_T0/O, R_p=sum(m_i-1)E_i, Q isomorphic to p^*T_B0(-R_p).',
     'The old pi is the same role as p and old C0 the role of B0 in the extracted local argument; the quotient differential and its vanishing divisor give the exact identification. Consumer ruling maps and q,nu remain unchanged.'),
    ('D22', 'Multiplicity and Chern-square reason', 'Consequently K^2=0 after the cyclic quotient differential', 'The same differential is written as a line-bundle isomorphism; disjoint fibres and zero fibre self-intersections justify K^2=0 where used.',
     'Make the existing inference explicit without strengthening its scope; the source model retains e of exact order m and all multiple-fibre terms.'),
]
for offset, (kind, location, old, new, reason) in enumerate(extras, len(defect_rows) + 1):
    defect_rows.append([f'II-C3-P244-{offset:03}', kind, LEMMA, location,
                       'cp35; final concordance pending', 'Common lemma P244', 'integrated build pending',
                       old, new, reason, 'Complete common proof and both consumer proofs read and compared; root admission pending.'])
write_tsv('S6_SERIES_PUBLISH_P244_defects.tsv',
          ['change_id','type','statement_id','old_location','old_page','new_location','new_page','old_text','new_text','reason','review_status'], defect_rows)

maps = [
    [LEMMA, '(i)', 'Minimal smooth compact T0 with kappa=-infinity, Kahler', 'p_g=0; rational Kahler perturbation and scaling; Phi:T0 embeds into projective space; projective classification is transported through Phi.', 'P4.15 step1 and P4R.2 step2', 'All original rational/ruled alternatives, and actual ruling maps, retained.'],
    [LEMMA, '(ii)', 'Minimal smooth compact T0 with kappa=-infinity, non-Kahler', 'OVV elliptic-or-class-VII; cyclic translation model; Q=T_T0/O maps by dp with divisor R_p; K=p^*K_B0(R_p), K^2=c2=0; q=1 and b1=1.', 'P4.15 step1 and P4R.2 step2', 'Original elliptic overlap and class-VII invariant arguments retained under the same hypotheses.'],
    [LEMMA, '(iii)', 'Minimal class-VII T0, b2=0, nonempty curve R', 'Etale compact cover a:Tprime to T0 is finite; a^{-1}R is a curve; Inoue alternatives excluded at exact source loci; C^2 minus0 to Tprime to T0 is universal cover.', 'P4.15 step1 after k0=r=ell=0; P4R.2 step3 equality case', 'Same Hopf conclusion and universal-cover morphism; no conclusion for a curve-free surface.'],
    ['night:P4.15', 'Consumer-only deductions', 'Original full-fibre, normalization and finite differential-rank-drop hypotheses unchanged', 'Exact sequence, e(T)=K_T^2-ell, conductor and torsion, q, blowup formulas, ell conclusions, all five proof steps.', 'All original consumers', 'Only shared classification and Hopf-recognition passages replaced by exact applications.'],
    ['night:P4R.2', 'Consumer-only deductions', 'Original standing setting, singular irreducible support, smooth bijective normalization unchanged', 'nu is a homeomorphism; p_*q_*(nu_*)^{-1}; finite-index surface-group argument; Euler cases and equality characterization.', 'All original consumers', 'All exact fundamental-group maps, conductor argument, Euler formulas and converse retained.'],
]
write_tsv('S6_SERIES_PUBLISH_P244_conclusion_map.tsv', ['owner','scope','hypotheses','map_or_argument','consumers','preservation'], maps)

status = []
for number in range(1, 26):
    kind = f'D{number:02}'
    state = 'done'
    reason = 'P244 and the four shared argument spans checked in full at this bounded scope; no additional instance found. Other root-owned edits to the two larger units are outside this status.'
    if kind == 'D10':
        reason = 'New tag P244 and stable label use the existing nonprinting dependency macro; prior D10 closures preserved.'
    elif kind == 'D12':
        reason = 'Both duplicate classification and both duplicate Hopf-recognition arguments have one complete common proved owner; both consumers use exact scoped applications.'
    elif kind == 'D13':
        reason = 'The common result is a numbered lemma, with its full proof and no orphan conclusion.'
    elif kind == 'D14':
        state, reason = 'open', 'Exact P244 insertion boundary and guarded application spans supplied; root must admit them into final body order.'
    elif kind == 'D16':
        reason = 'P244 has the mathematical title Minimal models of negative Kodaira dimension; both original owner titles preserved.'
    elif kind == 'D17':
        reason = 'Known inputs keep exact source statements/pages; the analytic embedding, quotient differential and finite-cover transfer are retained as one short proved application.'
    elif kind == 'D18':
        reason = 'Existing citation keys and editions retained; exact Kodaira Main Theorem/proof locator unified to pp314-315; source readings documented at their actual scope.'
    elif kind == 'D19':
        reason = 'The moved displays were unnumbered and uncited; no manual equation tag was added, removed or changed.'
    elif kind == 'D20':
        reason = 'The shared elliptic fibration uses p:T0 to B0, with explicit equality Q=T_T0/O and differential identification Q=p^*T_B0(-R_p); consumer q,nu,ruling p unchanged.'
    elif kind == 'D22':
        reason = 'Exact-order translations, multiple-fibre divisor, zero Chern square and finite covering reasons are present where used.'
    elif kind == 'D24':
        state, reason = 'open', 'No headline conclusion changes; final numbering/front-matter concordance is assigned to root integration.'
    elif kind == 'D25':
        reason = 'All original and rewritten proof inferences compared, including exact projective, tangent-quotient and covering maps; no refuted original assertion claimed and no hypothesis weakened.'
    status.append([LEMMA, kind, state, reason])
status.append([LEMMA, 'restructuring', 'open', 'Concrete complete lemma and exact guard spans finished; root admission into final body remains.'])
write_tsv('S6_SERIES_PUBLISH_P244_unit_progress.tsv', ['unit','row','status','basis'], status)

# These readings were performed before adding these rows: complete source and
# receiving proofs; exact published/preprint source loci stated below.
event_specs = [
    (LEMMA, 'common-proof', 'Complete common lemma and proof read and compared with both source proof passages. Kodaira embedding Phi, its pulled-back ruling, OVV cyclic quotient and tangent-line map Q to p^*T_B, Chern/Noether invariants, compact finite etale cover a and composed universal cover are all explicit. Exact minimal/smooth/compact/kappa and curve hypotheses preserved; no new required check claimed.'),
    ('night:P4.15', 'consumer-P415', 'Complete original 186-line proof owner and complete receiving proof read. All hypotheses and statement conclusions, the tangent exact sequence, maximal-minor scheme, Chern identity, full conductor, q contraction, ruled/class-VII Euler calculations and all conductor branch maps are unchanged in scope. Only shared classification and Hopf recognition use earlier P244; tags and labels preserved.'),
    ('night:P4R.2', 'consumer-P4R2', 'Complete original 89-line proof owner and complete receiving proof read. The normalization homeomorphism, exact p_*q_*(nu_*)^{-1} fundamental-group map, finite-index surface-group argument, Euler formulas, conductor and converse remain. The same negative-Kodaira minimal model and equality-case curve satisfy P244 hypotheses.'),
    (LEMMA, 'source-Kodaira', 'Actually opened the original Kodaira1954 PNAS pp313-316 in the publisher Collected Works II reprint, including Main Theorem p314 and complete proof outline pp314-315. The section map is a projective embedding of the smooth compact Hodge surface produced by rational Kahler perturbation and integral scaling. Local source S6_PUBLISH_c3_foundations_sources/S6_SERIES_PUBLISH_Kodaira1954_reprint.pdf sha256 31941a9bb011549e01b7c299ef4fb346ec8626f83a0af776f0af51179ecdb886; primary URL https://api.pageplace.de/preview/DT0400.9781400869862_A26058233/preview-9781400869862_A26058233.pdf.'),
    (LEMMA, 'source-Beauville', 'Actually read the original Numdam Beauville1978 monograph at III.10 p40, V.10 pp79-80, VI.17 p111 and VI.18 p112, complete statements and their displayed proofs, both attached primary text extraction and newly downloaded exact PDF pages. The classified object is the projective image Phi(T0), and its isomorphism/ruling is transported by Phi. PDF sha256 a2bdff071df610a8e39200a16ad7675149c1ddf601157b3e3e56cbf285994e4e; primary URL https://numdam.org/item/AST_1978__54__R1_0.pdf.'),
    (LEMMA, 'source-OVV', 'Actually read the attached OVV2020 arXiv1810.05768v3 source at the class-VII definition, complete Theorem2.5 proof, complete Theorem4.2 proof and Remark4.4, complete Proposition4.5 proof, and complete Theorem5.1 proof. Newly opened PDF pp7-9,17,21-22,27 confirms numbering and local quotient/minimality hypotheses. Explicit exact-order cyclic translation and Q=p^*T_B(-R_p) preserve the elliptic overlap. PDF sha256 2f9159e3e9dfd6c9ab575419b0fcf0a12010cf2ece542f99ebdf7999e52ec350; primary URL https://arxiv.org/pdf/1810.05768v3.'),
    (LEMMA, 'source-BBK', 'Actually opened BBK2019 arXiv1709.00062v3 Theorem1 p1 and adjacent discussion, plus the attached original source theorem. The etale cover has compact Hopf or Inoue domain and hence is finite. This is a theorem-statement and exact application reading, not a reading of the full group-theoretic proof. Primary URL https://arxiv.org/pdf/1709.00062v3.'),
    (LEMMA, 'source-Inoue', 'Actually viewed original Inoue1974 journal pages274,275,277,279 from the recovered Gottingen volume: Proposition2(i) and its complete proof, Proposition3(i) and its reference to that argument, and the paragraph after (21) identifying S-plus as the unramified double cover of S-minus and its no-curves conclusion. These exact loci exclude all three Inoue families after pulling back a nonempty curve by a. Original volume sha256 a99fd305ebc90570262794a9f11e62cd3752bb3017d553f93bfbde4cbd159738; primary URL https://gdz.sub.uni-goettingen.de/download/pdf/PPN356556735_0024/PPN356556735_0024.pdf.'),
]
now = datetime.datetime.now(datetime.timezone.utc)
event_file = 'agents/continuation3_foundations/S6_SERIES_PUBLISH_P244_CHECK_EVENTS.tsv'
events = []
for owner, key, outcome in event_specs:
    event_id = 'publish:c3:P244:' + key
    events.append([owner, now.date().isoformat(),
                   'GPT-6 Astra (OpenAI), ChatGPT Pro mode; inherited effort not separately exposed; continuation3 foundations',
                   'used and rechecked in this run',
                   outcome + ' Exposed editorial/source comparison only; no independent re-proof, computation rerun or final PDF credit.',
                   event_id, 'publication common-premise consolidation', event_file, '',
                   'used and rechecked in this run', event_id, '', '', now.isoformat(),
                   'P244 before P4.15; exact applications in P4.15 and P4R.2'])
write_tsv('S6_SERIES_PUBLISH_P244_CHECK_EVENTS.tsv',
          ['statement_id','date','who','type','outcome','event_id','phase','source_file','source_row','source_event_type','evidence_group','publish_input_file','publish_input_row','date_utc','where'], events)
print('P244 generated: 1 common owner, 2 receiving proof fragments,', len(guards), 'guarded edits,', len(defect_rows), 'defect instances,', len(maps), 'exact scope maps.')
