#!/usr/bin/env python3
"""Save an independently read locator review; never mutate a manuscript."""
from pathlib import Path
import datetime
import hashlib
import json
import re

BASE = Path(__file__).resolve().parents[2]
INPUT = BASE / 'work/maps_audit/III_course_additional_named_reference_candidates.json'
OUT = BASE / 'work/cdp_audit/course_reference_locator_review.json'
source = json.loads(INPUT.read_text())

names = {
    'belt': 'belt-sphere-complements-and-the-whitney-disk',
    'move': 'whitney-move-with-controlled-support',
    'morse': 'relative-morse-functions-and-original-handles',
    'trajectory': 'morse-trajectories-and-critical-value-lowering',
    'slides': 'framed-handle-slides-and-index-one-removal',
    'chains': 'integral-handle-chains-and-signed-incidences',
    'pair': 'creating-an-original-cancelling-handle-pair',
    'cancel': 'morse-cancellation-with-controlled-support',
    'middle': 'realizing-framed-handles-and-middle-cancellation',
    'arrangement': 'rearranging-the-original-framed-handles',
    'twist': 'sphere-twists-and-the-original-smooth-six-sphere-comparison',
    'frame': 'the-original-six-dimensional-framing-invariant',
    'pt': 'framed-manifolds-and-the-pontryagin-thom-map',
    'receiving': 'whitney-moves-in-the-receiving-dimensions',
    'zero': 'removing-the-original-zero-and-top-handles',
    'spin': 'spin-six-and-the-framing-comparison',
    'duality': 'manifold-duality-the-diagonal-and-wu-classes.source',
}
def lab(short, tail):
    return f'courseIII:{names[short]}:{tail}'
def secs(short, *numbers):
    return [lab(short, 'section-'+str(n)) for n in numbers]
def cref(labels):
    return r'\cref{' + ','.join(labels) + '}'
def eq(label):
    return r'\eqref{' + label + '}'

rows = {i: {'record_number': i, **source[i-1], 'scope': 'The candidate paragraph was read for its raw or named companion locator; this is not a new full proof audit.', 'status': 'No new raw companion locator to repair in this paragraph', 'mappings': []} for i in list(range(1,47))+list(range(67,75))}
def add(i, phrase, labels, content, suggested=None, note=None):
    assert phrase in rows[i]['paragraph'], (i, phrase)
    rows[i]['status'] = 'Explicit target mapping supplied'
    d = {'exact_original_phrase': phrase, 'target_labels': labels, 'matched_target_content': content}
    if suggested is not None: d['suggested_tex'] = suggested
    if note is not None: d['qualification'] = note
    rows[i]['mappings'].append(d)

add(2, 'the CW companion, Section 2', ['mapsI:cw:cw-manifolds'], 'Paper I lines31019–31049 construct the finite embedding from positive chart blocks, the normal-tube map, and its retraction.', cref(['mapsI:cw:cw-manifolds']))
add(3, 'Its Sections 3--5', secs('move',3,4,5), 'The targets extend the full collar germ, parametrize the original corner disk, and give exact coordinates for both sheets.', 'Its '+cref(secs('move',3,4,5)))
add(4, r'\cref{mapsI:cw:cw-manifolds}, Section 2', ['mapsI:cw:cw-manifolds'], 'The already correct named Paper I target is the full finite embedding/tube/bump provider; the appended source section number is redundant.', cref(['mapsI:cw:cw-manifolds']))
add(8, 'equation (1.12) in the trajectory companion', [lab('trajectory','eq:1.12')], 'The actual displayed equation is H(B_mu)=W^s(p_mu) intersect f^{-1}(b); both inclusions are proved from the original local flow.', 'equation '+eq(lab('trajectory','eq:1.12'))+' in the trajectory companion')
add(9, 'the trajectory companion, Section 1.1', secs('trajectory','1.1'), 'The belt-section subsection proves both inclusions by x-dot=x, y-dot=-y and the outer level map.', cref(secs('trajectory','1.1')))
add(15, 'the handle-chain chapter, equation (3.9)', [lab('chains','eq:3.9')], 'The full signed incidence formula is I_ij=epsilon_{p,i}(-1)^p c_ij and a_ij=epsilon_{p,i}(-1)^p times the ambient boundary intersection.', 'the handle-chain chapter, equation '+eq(lab('chains','eq:3.9')))
add(18, 'its formula (2.6)', ['mapsI:cw:eq:2.6'], 'The formula is the exact radial homotopy u -> (1-tau)u+tau max(u,R_i) on the actual punctured cobordism.', 'its formula '+eq('mapsI:cw:eq:2.6'))
add(18, 'Theorem 5.1', ['mapsI:pf:theorem:5.1'], 'The printed theorem states that an integral homology equivalence between simply connected spaces with specified CW comparisons is a homotopy equivalence.', cref(['mapsI:pf:theorem:5.1']))
add(18, 'Its equation (5.12)', ['mapsI:pf:eq:5.12'], 'The equation gives h_j=bar h_j beta_C, h_j i_j homotopic to1 and i_j h_j homotopic to1 for the two actual boundary inclusions.', 'Its equation '+eq('mapsI:pf:eq:5.12'))
add(19, 'Its Sections 4.2--4.4', secs('morse','4.2','4.3','4.4'), 'The exact targets treat the smooth attachment corner, the complete outer collar map, and the extreme indices/full decomposition.', 'Its '+cref(secs('morse','4.2','4.3','4.4')))
add(19, 'Section 6 of that companion', secs('pair',6), 'The lower attaching sphere and its framed bounding disk are written as the exact ellipsoid D_in in the original height level.', cref(secs('pair',6)))
add(19, 'Section 8.1 of that companion', secs('slides','8.1'), 'The subsection explicitly weakens simple connectivity to the surjectivity pi_1(M_-)->pi_1(C) and retains Gamma*F and its kernel word.', cref(secs('slides','8.1')))
add(20, 'Its Section 5', secs('cancel',5), 'The supported cutoff uses the original disk radius R(u), beta(|y|^2/R(u)^2), eta(|z|^2), and complete derivatives.', 'Its '+cref(secs('cancel',5)))
add(20, 'its second exercise', [lab('cancel','exercise-7.2')], 'The exercise computes the three critical points of -y^2+z^2-d(1-y^2)^2 when d>1/2.', cref([lab('cancel','exercise-7.2')]))
add(20, 'Sections 2--6', secs('middle',2,3,4,5,6), 'The targets successively realize the full stage, compare levels, identify actual incidences, prove escape/compact support, and complete the dimension-six/seven reductions.', cref(secs('middle',2,3,4,5,6)))
add(21, 'Its Sections 1--3', secs('belt',1,2,3), 'The named belt-complement targets contain the full complement map, avoidance, and homotopy comparison.', 'Its '+cref(secs('belt',1,2,3)))
add(21, 'Section 5 constructs', secs('belt',5), 'The relative embedded-disk construction fixes the entire prescribed collar, avoids K, and avoids specified surface interiors.', cref(secs('belt',5))+' constructs')
add(21, 'Sections 6--7', secs('belt',6,7), 'The full normal-frame extension and the original framed Whitney boundary retain the metric, triangular coefficients, and intersection signs.', cref(secs('belt',6,7)))
add(26, 'The sphere-twist companion, Section 4', secs('twist',4), 'The exact-sequence calculation gives free rank2r H_3(P), primitive isotropic lower belts, and a second primitive isotropic subgroup of equal rank from the reversed stage.', cref(secs('twist',4)))
add(27, 'Section 6 of that companion', secs('twist',6), 'The actual twist-cancellation subsection verifies the geometric intersections, unique trajectories, escape and compact supports, then cancels all pairs and gives both product-map inverses.', cref(secs('twist',6)))
add(28, 'Its Sections 6--7', secs('slides',6,7), 'These sections compare the old two-handle complement/descending maps and remove the selected one-handle after verifying holonomy, unique trajectory, escape and support.', 'Its '+cref(secs('slides',6,7)))
add(29, r'Section 4.2 of the \cref{courseIII:relative-morse-functions-and-original-handles:relative-morse-attachment}', secs('morse','4.2'), 'The target defines U=f-a, V=B-beta and the exact outward corner rounding.', cref(secs('morse','4.2')))
add(29, '(1.14)-(1.16) in the arrangement companion', [lab('arrangement','eq:1.14'),lab('arrangement','eq:1.15'),lab('arrangement','eq:1.16')], 'The targets give Xi, its full derivative including both radial columns, and its pullback metric.', eq(lab('arrangement','eq:1.14'))+'--'+eq(lab('arrangement','eq:1.16'))+' in the arrangement companion', 'The later Section1 in this same paragraph is LOCAL to realizing-framed-handles-and-middle-cancellation; it must not be moved to the arrangement namespace.')
add(30, 'Sections 5-6 of that companion', secs('chains',5,6), 'Section5 retains exact unit contractions; Section6 uses the integer section S and gives U_3=[S B] with its explicit inverse and neighboring matrices.', cref(secs('chains',5,6)), 'The section S itself is constructed by the earlier integer algorithm, equation4.6, then explicitly used in section6; no new mathematical change is proposed.')
add(34, 'from lesson 7', ['mapsI:cw:eq:2.5'], 'Paper I equation2.5 is exactly C=X minus the interiors of the two specified coordinate disks, with original radii and boundaries.', 'of '+eq('mapsI:cw:eq:2.5'))
add(35, r'equations \eqref{courseIII:morse-trajectories-and-critical-value-lowering:eq:1.2}--\eqref{courseIII:morse-trajectories-and-critical-value-lowering:eq:1.9}', [lab('trajectory','eq:1.2'),lab('trajectory','eq:1.9')], 'The first eq1.2 is the full holonomy coordinate change F and inverse; eq1.9 is the conjugated time-s flow. These are correctly companion targets.', None)
add(35, r'stable sets from \(N\) downwards used in \eqref{courseIII:morse-trajectories-and-critical-value-lowering:eq:1.2}', [lab('zero','eq:1.2')], 'This SECOND eq1.2 refers to the local stable set W^s(p_j) intersect N, printed at removing-the-original-zero-and-top-handles.tex lines43–45. It is not the trajectory coordinate change.', r'stable sets from \(N\) downwards used in '+eq(lab('zero','eq:1.2')), 'Concrete overbroad-replacement defect. Author maps_audit confirmed correction by replacing only the first occurrence in course-ref-077.')
add(36, 'the proved included companion, Theorem 2.1 and Sections 3--5', [lab('cancel','morse-cancellation-data')]+secs('cancel',3,4,5), 'The receiving cancellation data contain the stated theorem2.1; sections3–5 construct disk fibers, monotone minorant, and the supported cutoff.', cref([lab('cancel','morse-cancellation-data')]+secs('cancel',3,4,5)), 'The later Sections1–3 of Laudenbach are external-source locators and must remain attached to that source, not be converted to local labels.')
add(37, 'the geometric framing chapter, Sections 1--2', [lab('frame','eq:1.3')]+secs('frame',1,2), 'The quaternion conjugation double cover explicitly yields pi_2(SO(3))=0 in eq1.3. The next section retains the normal/tangent framing comparison.', cref([lab('frame','eq:1.3')]+secs('frame',1,2)))
add(38, 'Section 8.2 of the geometric framing chapter', secs('frame','8.2'), 'The target carries out interior framed surgeries killing pi_1 and pi_2 while retaining both boundary maps and stable frames.', cref(secs('frame','8.2')))
add(38, 'Section 8.3 then', secs('frame','8.3'), 'The target reduces the same C-prime to indices3 and4 using only the two relative H_2 vanishings, without assuming H_3 acyclic or torsion-free.', cref(secs('frame','8.3'))+' then')
add(42, 'Sections 2--3 of that chapter', secs('receiving',2,3), 'These targets give the original orientation/normal blocks and the full rank-four rotation-obstruction calculation; the following supported-flow target is section4 of this same chapter.', cref(secs('receiving',2,3)))
add(43, 'The finite projection transport proved in lesson 11 constructs', ['courseIII:almost-complex-structures-and-integrability:section-10.1'], 'The exact printed provider at almost-complex-structures-and-integrability.tex lines958–966 constructs the trivial-bundle embedding and proves q:im(p)->im(q) invertible when norm(p-q)<1, with a uniform finite interval partition and continuous inverse. I reopened this entire paragraph after maps_audit identified it. The identical projection inequality applies over the real numbers in the receiving tangent-bundle application.', 'The finite projection transport of '+cref(['courseIII:almost-complex-structures-and-integrability:section-10.1'])+' constructs', 'This supersedes the initial provisional suggestion to remove the historical preface without a target. The complete receiving construction remains retained.')
add(44, 'Its equation (8.11)', [lab('pt','eq:8.11')], 'The exact involution is S_m(v,a,b)=(Qa,P_nu a+Jv,b), S_m^2=I and tau_E=tau_st S_m, with all original coordinate orders.', 'Its equation '+eq(lab('pt','eq:8.11')))
add(45, 'equation (8.11) of the Pontryagin--Thom chapter', [lab('pt','eq:8.11')], 'This is the same exact tangent/normal involution S_m, rather than a frame equation in the sphere-twist chapter.', 'equation '+eq(lab('pt','eq:8.11'))+' of the Pontryagin--Thom chapter')
add(67, r'Sections 2--5 of the included companion \emph{Whitney moves in the original receiving dimensions}', secs('receiving',2,3,4,5), 'The targets comprise the original normal blocks, rank-four frame extension, supported move, and complete exercises. The operative proof is in sections2–4; including section5 retains the stated original range.', cref(secs('receiving',2,3,4,5)))
add(68, 'The actual tube compression of the handle companions', [lab('arrangement','arrangement-tube-compression')], 'The explicit compactly supported radial field gives C_t(psi(theta,z))=psi(theta,e^{-t}z) on the entire original tube, retaining its domain and derivative.', 'The actual tube compression of '+cref([lab('arrangement','arrangement-tube-compression')]))
add(69, 'the later classification argument for lesson 7', [lab('twist','twist-original-smooth-map')], 'The paragraph already has the exact named smooth-sphere comparison target. The historical lesson number adds no separate dependency.', 'the later smooth classification of the original homotopy six-sphere')
add(71, "that chapter's equation (1.13a)", [lab('belt','eq:1.13a')], 'The full derivative differentiates both radial factors of the complement map and is followed by the original Dvarphi at its actual point.', 'equation '+eq(lab('belt','eq:1.13a')))
add(72, 'Section 7.2 of the belt-complement chapter', secs('belt','7.2'), 'The compactness/local-embedding argument yields a uniform width for the two strips; it separately checks the endpoint quadrants and positive separation from all other sheets.', cref(secs('belt','7.2')))
add(73, 'the earlier chapter, Section 6.6', secs('belt','6.6'), 'The target retains R=QT with all triangular entries, extends T positively, and proves epsilon(e T_rot)=-epsilon(e) while keeping the first direction fixed.', cref(secs('belt','6.6')))
add(74, 'Section 6.1 of the belt-complement chapter', secs('belt','6.1'), 'The target constructs P=P_M-P_D, K=dot P P-P dot P and dot U=KU; the commutator identity transports the whole original normal space and works unchanged in rank4.', cref(secs('belt','6.1')))

# The supplied snapshot already contains the author's corrections.  Keep exact
# evidence for the independently discovered distinction rather than resnapshot it.
rows[41]['note'] = 'Sections1–2 in this paragraph are LOCAL to the sphere-twist chapter (its actual tube diffeomorphisms); do not retarget them to the preceding geometric-framing reference.'
rows[46]['note'] = 'The named duality target is correct; its explicit Euler-number equation is courseIII:manifold-duality-the-diagonal-and-wu-classes.source:eq:4.7. Lines375–400 were opened, including the complete corollary proof.'
rows[6]['note'] = 'The attaching equations and Gamma L_0 transport here are local to pair creation.'
rows[70]['note'] = 'Equation5.1 is local to the supported-move chapter and is the full ambient tube map; its compact injectivity argument is also local.'

# Archive only target excerpts needed for this locator review.  These are exact
# current statements/formulas, not claims that all intervening proofs were reread.
all_labels = sorted({t for r in rows.values() for m in r['mappings'] for t in m['target_labels']})
target_evidence = {}
for target in all_labels:
    if target.startswith('mapsI:'):
        f = BASE/'S6_09_PAPERS_I.tex'
    else:
        name = target.split(':',2)[1]
        f = BASE/'editorial/III_course'/(name+'.tex')
    lines = f.read_text().splitlines()
    exact = r'\label{'+target+'}'
    hits = [i for i,l in enumerate(lines) if exact in l]
    assert len(hits)==1, (target,hits)
    i=hits[0]; start=max(0,i-4); end=min(len(lines),i+15)
    target_evidence[target]={'file':str(f.relative_to(BASE)), 'label_line':i+1,
        'excerpt_lines':[start+1,end], 'text':'\n'.join(lines[start:end]),
        'file_sha256':hashlib.sha256(f.read_bytes()).hexdigest()}

d={
 'reader':'GPT-6 Astra (OpenAI, ChatGPT Pro mode)', 'effort':'Pro', 'date':'2026-11-17',
 'timestamp_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'scope':'Independent receiving-target check of the54 assigned geometric raw-locator candidates (records1–46 and67–74); exact named equations/sections and their relevant content were matched as recorded. Not a second full proof audit. Existing named references without a new raw locator are retained without a blanket new source-check claim.',
 'input':str(INPUT.relative_to(BASE)), 'input_sha256':hashlib.sha256(INPUT.read_bytes()).hexdigest(),
 'rows':[rows[i] for i in sorted(rows)], 'target_evidence':target_evidence,
 'counts':{'candidate_rows':len(rows),'rows_with_explicit_mappings':sum(bool(r['mappings']) for r in rows.values()),'mapping_items':sum(len(r['mappings']) for r in rows.values()),'target_labels':len(all_labels)},
 'concrete_correction':'Candidate35/course-ref-077 has two different eq1.2 references. Holonomy goes to the trajectory chapter, while the later stable-set reference remains local to zero/top removal. The author confirmed the one-occurrence correction.',
 'manuscripts_or_converter_modified_by_reviewer':False,
}
OUT.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'path':str(OUT),'counts':d['counts']},indent=2))
