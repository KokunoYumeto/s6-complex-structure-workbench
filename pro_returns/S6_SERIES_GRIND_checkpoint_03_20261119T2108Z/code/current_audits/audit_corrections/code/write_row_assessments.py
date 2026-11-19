from pathlib import Path
import json, csv

root=Path(__file__).resolve().parents[1]
actor='GPT-6 Astra (OpenAI), ChatGPT Pro mode; reasoning effort inherited from root (not separately exposed)'
rows={}
def add(label,line,routes,risk,state='proved at the stated scope'):
    rows[label]={'confidence_state':state,'confidence_line':line,
                 'independent_routes':routes,'remaining_risk':risk,
                 'format_check':None,'layout_check':None,'completion_state':None}

add('night:P3K.109',
    'Mathematical continuation gate closed: the full EF.1–8 proof supports the exact physical C* automorphism group on the stated U locus and complete caps.',
    ['Retained producing-run full source/period peer audits remain credited at their recorded scopes.',
     'This run read the complete EF proof, including meromorphic-base descent, nonzero Abel class, the primitive invariant vector/covector, full central cochain, compact fixed-curve obstruction, actual cover lifts, integral section lattice, point/O divisor extension, and full root/annular maps.',
     'IV_open_prereading.md and IV_K109_centralizer_prereading.md preserve this run’s independent arguments and exact before-reading boundaries.',
     'Fresh independent_IV_endpoint_checks.py passed 25,796 exact assertions shared across K109/110/113/114; it rederives the source discriminant, j and critical cubic, chord identities, full s=1 M6 specialization, ten-class determinant, arbitrary-cochain matrix multiplication, and endpoint exponents. This count is not a count of independent proofs.'],
    'No unresolved mathematical gap identified. The theorem uses the explicitly retained K96 complete source/root/reference constructions and F35/F46 sphere-topology maps. A new whole independent proof of all those earlier dependencies is not claimed. The bounded external-credit comparison and editorial source-record cleanup remain separate gates; this theorem assigns no numerical Theta7 return.')
add('night:P3K.110',
    'Mathematical continuation gate closed: the full SEF.1–6 and NE.1–4 argument proves exactly the winding groups lZ and mZ, both norm signs, all retained characters, and the explicit primitive M2 endpoint.',
    ['Retained complete source and independent-root audits remain credited at their recorded scopes.',
     'This run read all SEF and NE steps, including full coefficient target arguments, the ordinary/root graph square, all three chronological root phases, scalar equality, the rational divisor necessity, single-valued ordinary/root lifts, and arbitrary annular integer nu.',
     'Independent prereading derived the chronological threefold phase and the full negative obstruction target before proof reading; the fresh exact certificate verifies the finite coefficient, full unit inversion charts, winding divisibility, and retained n+m*nu obstruction.'],
    'No unresolved mathematical gap identified. The finite norm equation alone does not handle m=2; the read NE.2–3 full annular continuation does, by n+m*nu != 0. K109 and K96 are retained exact dependencies. Literature attribution and editorial cleanup are separate from mathematical closure; no division of a return class is inferred.')
add('night:P3K.113',
    'Mathematical continuation gate closed: the complete EB, EBR and EBP proofs extend the endpoint classification to r outside {0,1/4,1/3}, including the auxiliary-centroid-polynomial zeros.',
    ['This run independently derived the j-function divisor and three-fixed-point argument before opening the supplied proof, with the missing cyclic-cover bridge explicitly recorded.',
     'This run then read all three supporting proofs and verified the bridge: the primitive kernel lattice is preserved integrally, the actual line cover lifts with its affine inverse, and quotienting by the primitive physical period gives a degree-one elliptic isomorphism.',
     'The fresh exact certificate rederives the marked-node parameter and inverse, excluded-locus pullback, source invariant and coefficients, full central cochain and section lattice. Retained full peer audits remain credited at their recorded scopes.'],
    'No unresolved mathematical gap identified. The source-domain transport keeps K96 charts, both point modules, selected fan, finite characters and complete reference. Original sources at r=0,1/4,1/3 are outside this statement; r=0 is handled separately by K114. Bounded credit comparison remains editorial/source work, not an open proof condition.')
add('night:P3K.114',
    'Mathematical continuation gate closed: the complete R0E.1–11 proof proves the r=0 endpoint classification with the inherited order-one norm-zero finite III filling and the stated infinity caps.',
    ['This run read the complete primary R0E proof, including both original III components, their tangency, both point/O module graphs, the full M6 coefficient, primitive source lattice, elliptic quotient, genuine infinity-root maps, scalar endpoints and the full negative annular continuation.',
     'The independent prereading computed the exact degree-one invariant j0(t)=6912/(27t+4), before opening the supplied proof; the fresh exact certificate verifies that invariant, the common source/lattice/cochain algebra and endpoint exponents.',
     'Retained producing-run full independent source/root/cap audits remain credited at their recorded scopes. This run does not claim to have newly rederived every duplicate historical peer proof printed after R0E.',
     'The potentially ambiguous reference-zero Cauchy solve was traced to K96 EX.18 at source43190–43235: its residual vanishes at the reference parameter as an entire annular cochain, so its Cauchy transform vanishes there as required.'],
    'No unresolved mathematical gap identified. The finite quartic root is used only at t=0; both infinity roots use their stated original-coordinate substitutions. K96 and F35/F46 remain explicit retained dependencies. The planned additional finite-chart computation is supplementary verification, not a missing proof step. Bounded literature attribution and source-record cleanup remain separate.')

add('night:P3F.34',
    'The all-free-cap integral homology calculation is proved after the precise source-scope repair: the old D2.11 coprime result is extended, not refuted outside its hypotheses.',
    ['Complete printed proof read, with actual primitive boundary lattice, exterior map and signed meridians.',
     'Fresh independent_V_III_checks.py passed25,759 exact assertions including universal transfer minors, integral Smith cases and n=0 cases; direct comparison with the actual D2.11 theorem and its CSV hypothesis.'],
    'Source patch P3F34_proposed_patches.json is required; parent reports it applied. No broader refutation of D2.11 is supported. The algorithm’s analytic/topological inputs retain their named proof scopes.')
add('iv:i3_all_reduced_caps',
    'The complete reduced-cap comparison is proved at the stated K106 reference scope; both characteristic integers agree separately through the actual relative cap products.',
    ['Complete K108 proof and K103 OC.1–3 source/root inputs read.',
     'Fresh independent_IV_checks.py verified full source/chord/Cartier/root/signed-meridian algebra and the unchanged fan algorithm.'],
    'The initial K106 pair(47,-4) remains a retained full source calculation, not a new whole reproof by this audit. The exact Jin v2 coordinates and collar bordism have now also been freshly opened and verified, at the scopes recorded in Jin_primary_verification.md; the source-specific K106 initial-pair derivation remains a retained independent input.')
rows['night:P3K.108']=dict(rows['iv:i3_all_reduced_caps'])
add('iv:rank_two_specialization',
    'The integral specialization isomorphism is proved by the actual unit-preserving family and primitive generator maps.',
    ['Complete supplied proof read; fresh toric restriction Smith computation and all exterior monodromy invariant lattices independently constructed.',
     'The genuine cross Cartier line and its exact quadratic multiplier cocycle supply the primitive cross generator; rank equality alone is not used for integral surjectivity.'],
    'No mathematical gap identified at the precise rank-two setup. The source does not supply a general higher-rank statement, and this audit does not extend the scope.')

for row in csv.DictReader((root/'IV_high_risk_audit.tsv').open(),delimiter='\t'):
    label=row.get('label') or row.get('statement_id')
    if not label: label=next(iter(row.values()))
    if not label.startswith('iv:correction:'): continue
    add(label,
        'The refined receiving statement is proved at its explicitly retained construction/input scope, subject to the single H2 wording repair for P3K.22.',
        ['Independent correction implications frozen before reading all33 receiving proofs; every printed receiving proof then compared.',
         'The physical duality, directed Hopf collars, fixed-edge factor seven, fan algorithms and exact image calculations were recomputed at the scopes recorded in IV_high_risk_report.md and the retained22,697-check certificate.'],
        'This closes the refined statement only; the located historical compound assertion stays refuted. Original source/page/native-product constructions remain named inputs and are not all newly re-proved here. For iv:correction:P3K.22 the cap term is the injective degree-two H2 term, as patched in proposed_patches.json.')

(root/'row_assessments.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
(root/'row_assessments_actor.json').write_text(json.dumps({'actor':actor,'scope':'Mathematical audit states only; no typography, layout or overall completion claim.'},indent=2)+'\n')
print(len(rows),'scoped row assessments written')
