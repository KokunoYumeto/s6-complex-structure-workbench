from pathlib import Path
import datetime as dt
import hashlib
import json

R = Path(__file__).resolve().parents[1]
D = R / 'agents/continuation2_C/S6_SERIES_PUBLISH_II_C2_R13_analytic_construction_03'
P = 'S6_SERIES_PUBLISH_II_C2_R13_'

def binding(path):
    p = Path(path)
    b = p.read_bytes()
    try:
        label = p.relative_to(R).as_posix()
    except ValueError:
        label = str(p)
    return {'path': label, 'bytes': len(b), 'sha256': hashlib.sha256(b).hexdigest()}

ip = D / (P + 'A_review_v1') / (P + 'A_research_review_index_v1.json')
assert binding(ip)['sha256'] == '6dec720e7c72bdbaaf42cf14378c8ae057b62934c23edb4a85839ea103a367ef'
index = json.loads(ip.read_text())
evidence = {}

def walk(value):
    if isinstance(value, dict):
        if 'path' in value and 'sha256' in value:
            b = binding(R / value['path'])
            assert b['sha256'] == value['sha256'], value['path']
            if 'bytes' in value:
                assert b['bytes'] == value['bytes'], value['path']
            evidence[b['path']] = b
        for v in value.values():
            walk(v)
    elif isinstance(value, list):
        for v in value:
            walk(v)

walk(index)
guards = []
for name in ['period_family_v2_guard_receipt.json', 'local_extension_v2_guard_receipt.json',
             'local_extension_v3_guard_receipt.json', 'global_gluing_v2_guard_receipt.json']:
    p = D / (P + name)
    d = json.loads(p.read_text())
    walk(d)
    old = (R / d['old']['path']).read_text()
    expected = (R / d['new']['path']).read_text()
    for g in d.get('guards', [d]):
        assert old.count(g['exact_old_text']) == 1
        old = old.replace(g['exact_old_text'], g['exact_new_text'], 1)
    assert old == expected, name
    guards.append(binding(p))

other = [D / (P + name) for name in [
    'local_orientation_certificate.py', 'local_orientation_certificate.out',
    'Grauert_base_change_primary_receipt.json', 'exact_ambient_scope.json',
    'exact_ambient_scope.tex']]
other += [R / f'records/S6_SERIES_PUBLISH_II_R13_root_research_0{i}.json' for i in [4, 5, 6]]
primary_pdf = R.parent / 'temporary_B_pdf/S6_SERIES_PUBLISH_CK_Grauert1960.pdf'
assert binding(primary_pdf)['sha256'] == '0559856be254902e7dd116725732117606912ab7d72b0f0fe88b600566829cde'
images = [binding(R.parent / f'temporary_B_pdf/S6_SERIES_PUBLISH_R13_Grauert1960_verified-{n}.png') for n in [61, 62, 63]]
for image, printed in zip(images, [62, 63, 64]):
    image.update(printed_page=printed, pdf_viewer_page=printed-1, pdf_zero_based_index=printed-2)

out = {
    'created_utc': dt.datetime.now(dt.timezone.utc).isoformat(),
    'owner': 'night:P4R.13', 'tag': '02Y6',
    'status': 'Root mathematical audit of the complete compact-construction research notes, with the independent A audit and original-target comparison still pending.',
    'research_origin': 'C had previously read R13. Its construction is post-reading mathematical research. The fixed extracts exclude the old target proof and target-derived comparisons. A has kept the R13 proof unopened while deriving all cases and auditing the new construction. Root does not award an independent whole-R13 event here.',
    'index': binding(ip), 'bound_index_files': list(evidence.values()), 'exact_guard_receipts': guards,
    'other_bound_evidence': [binding(p) for p in other],
    'reading_scope': [
        'Root actually read the entire fixed period-family extract (10274 bytes), local-extension extract (11070 bytes), and global-gluing extract (6267 bytes), in bounded untruncated returns before this record.',
        'Root actually read the entire period-affine program, its successful output and the failed structural-equality attempt receipt; the integral matrices/program/output and the alternative local Weierstrass quotient had already been read and recorded in research04 and research05.',
        'Root actually read every old and new guard text for period v2, local v2 and v3, and global v2. This program verifies each entire new version is exactly the sequential guard replacement of the bound old version, and rechecks all hashes.',
        'Root actually read the complete orientation certificate and its output. Root read the exact standing setting, P4.12 and R13 statements and their scope receipt. The R13 target proof remains unopened by root.',
        'Root read the full Grauert 1960 printed pages62–64 in text, then viewed and read all three correctly mapped page images on 2026-11-22 at about11:00UTC. The 1963 corrigendum had already been fully read in batch77; no fresh full-corrigendum visual reading is claimed.'
    ],
    'primary_reading': {
        'work': 'Hans Grauert, Ein Theorem der analytischen Garbentheorie und die Modulräume komplexer Strukturen, Publications Mathématiques de l’IHÉS5(1960),5–64, DOI10.1007/BF02684746.',
        'url': 'https://www.numdam.org/article/PMIHES_1960__5__5_0.pdf',
        'pdf': binding(primary_pdf), 'actually_read_page_images': images,
        'loci': '§7 setup and Satz3 on printed62, complete displayed proof on63, restriction construction on63–64, Satz5 and Satz6 on64.',
        'application': 'The proper product projection P1×Delta→Delta has reduced base. E is locally free and parameter torsion-free over the one-variable convergent-power-series DVR, hence flat. Semicontinuity gives h1(E_epsilon)=0 near E0=O4; constant Euler characteristic gives h0=4. Satz5 identifies the locally free pushforward fibre with H0 by restriction. The evaluation determinant is nonzero on the compact central curve, so the proper image of its zero set misses a smaller parameter disc. Character projectors then give the four equivariant line frames.',
        'corrigendum': 'Grauert1963, Publications Mathématiques de l’IHÉS16,35–36, DOI10.1007/BF02684291; full text already read in batch77. The final correction concerns §7 Satz2; the cited Sätze3,5,6 conclusions are retained.',
        'retrieval_correction': 'An initial command used viewer pages58–60 and thus returned printed59–61. That text was read, but did not establish the intended locus. The initial singlefile PNG named p62 actually shows printed59 and was never viewed or credited. The corrected command uses viewer61–63, corresponding to zero-based60–62 and printed62–64. Only the three verified images listed here receive the intended primary-page reading credit.',
        'checkpoint_policy': 'Downloaded primary PDF and temporary images remain outside the lean checkpoint; addresses, hashes and exact reading loci are recorded.'
    },
    'mathematical_review': [
        'The real representations B1_epsilon,B2_epsilon,B3_epsilon have product I and squared-monodromy logarithms -2epsilon E23,-2epsilon E31,epsilon² E21. The diagonal D_epsilon=diag(1,1,epsilon²/4,epsilon/2) conjugates the epsilon2 representation to epsilon. The real lattice D_epsilon P Z4 transports it to the fixed integral matrices, with the exact local markings C_i. These are actual conjugacy maps, not just matching eigenvalues.',
        'The Klein-four cover t=(z+z^-1)²/4 has deck maps -z,-1/z,1/z. The triangle Re z>0,Im z<0,|z|<1, inverse sqrt(t)-sqrt(t-1), marks the three positively ordered loops and their product. Canonical logarithmic frames extend the unipotent pullback jointly in epsilon; semisimple finite deck actions extend. Grauert and the character projectors give an equivariant trivialization, to which the displayed twistor row-plane is applied through z↦-1/z³.',
        'The row/column equality is Pi_per=Pi_can exp(zN), equivalently Pi_per^t=exp(zN^t)Pi_can^t. The rank-one N eliminates the quadratic wedge term and traceN=0 gives the exact linear log-imaginary-part determinant. The limiting expressions are 4(1+2epsilon y),16(1+2epsilon y),16(1+epsilon² y). After dividing the coefficients by epsilon or epsilon², their positivity is uniform on fixed discs of radius less than1 and a fixed small positive epsilon interval. Positivity on the compact complement follows from continuity. The real evaluation map to F1* is therefore an isomorphism at every point, producing the proper holomorphic group family by its transported lattice quotient.',
        'In the local basis a,b,c,d, the half-deck map and the parallel monodromy are inverse maps; their distinction is kept explicitly. With p=2a-c, the doubled-base columns p,c,a,b,d are (1,0),(0,1),(1/2,1/2),(tau,beta),(alpha,2ell+gamma), with tau,gamma even and alpha,beta odd. The sign is Im tau(0)<0: detP=-1/8, detCi=1, and the normalized determinant has log coefficient4 Im tau. The quotient requires |Im tau| bounded away from zero and every norm estimate remains valid with this sign.',
        'The odd coordinate r=s exp(pi i gamma(s)) removes gamma. The infinite charts r=x_k y_k, x_(k+1)=1/y_k, y_(k+1)=r y_k have global punctured coordinate u=r^k x_k. P and B act by the two elliptic periods, while T moves k by2 and maps(z,u) to(z+alpha,r²u). The invariant norm has contraction factor |r|² exp(2pi Im beta Im alpha/Im tau), strictly between0 and1 after shrinking. Its fundamental representatives and the two adjacent charts give uniform boundedness and properness, including the central I2 fibre.',
        'The exact cyclic map g(z,u,r)=(z+1/4,r/u,-r) acts between charts k and -k, satisfies g4=P, and has g²=h translating a noncentral torus by(p+c)/2. This vector is not in the real-independent integral lattice. At the central fibre the elliptic translations by1/2 and1/4 prove freeness. Thus the quotient is smooth and its full central fibre is2S with local equation a unit times(xy)².',
        'The normalization of S is(E_tau×P1)/h=P(O⊕L) over E_tau/<1/2>, where L is the nontrivial sign line of order2. Its two conductor sections map to two different curves E_tau/<1/4>, each by a degree-two isogeny. The two conductor images are smooth elliptic and disjoint. The normalization is minimal elliptic ruled, the germs are ordinary-double products, and e(S)=0.',
        'The punctured local-to-Jacobian map is the translation Phi=x+v, v=(-ell/2,-ell/2+1/8). Its full-loop change is -a; its half-loop difference v(-r)-R v(r)=-(1/4,ell) cancels the actual affine g translation. Phi and its inverse therefore descend to the exact local group family in the same marking used by the global integral matrices.',
        'For the split central model, the graph class of I2 changes sign under g while its two component-area classes are interchanged; elliptic translation acts trivially. The invariant cohomology has dimensions1,2,2,2,1 and the surviving elliptic and component classes restrict independently to the monodromy invariants. The notes supply a compact-parameter deformation of the parity-compatible coefficients and a proper vector-field lift to keep these actual specialization maps fixed. A is independently completing the detailed local maps before the whole construction is sealed.',
        'The conductor pushout gives the free H1 generators t,b and one order-two class, with a mapping to2t. Thus local integral H1 restriction is2Za*+Zb* inside the invariant lattice Za*+Zb*. Under Phi^-1 the zero section is -v; a positive base loop has elliptic displacement1/4. Consequently the invariant covector ua*+vb* evaluates to u/2 on that loop. This is the marked affine term used in global matching, rather than an unchosen torsor class.',
        'The global spaces are glued over the actual open cover B0=P1 minus the closed radius-r0 discs and D_i the radius-r1 discs, r0<r1. The entire overlaps are the annuli r0<|t_i|<r1, and the transitions are the displayed Phi_i with Ci. All overlapping fibres are identified by biholomorphisms. The resulting space is Hausdorff, connected, smooth, proper over P1 and compact.',
        'The common primitive invariant alpha=(1,1,1,2) pulls back under the three Ci to(-1,-1,0,0),(-1,-1,0,0),(1,0,0,0). Outside, H1 is H1(B0) plus Qalpha with the three base-circle values summing to0. Local matching forces those values to c times(-1,-1,1)/2, so their sum is -c/2 and c=0. The integral global R1 section is2alpha and its obstruction is the primitive class -[P1]. Together with H1(P1,j*V)=0, H0(P1,j*Lambda²V)=0 and the actual local specialization identifications, the Leray total-degree-two terms vanish, yielding b1=b2=0. All fibre Euler characteristics vanish; hence e(Y)=0 and b3(Y)=2.',
        'The exact standing domain imposes b1=b2=0, a smooth compact connected threefold and a proper connected torus fibration. The literal setup does not impose b3=0, Euler2, a globally trivial canonical bundle or algebraic-reduction status. The constructed fibres fit that domain. Their two elliptic conductor images collide with the word one in R13. The current statement of02XE also covers these supports. C is recording its item3 coefficient-two-section entry and the exact uses of its earlier local calculations; root has not yet read the02XE proof or the R13 target proof.'
    ],
    'canonical_source': binding(R / 'S6_SERIES_PUBLISH_II.tex'),
    'ledger': binding(R / 'CHECK_EVENTS.tsv'),
    'original_target_opened_by_root': False,
    'independent_A_audit_sealed': False,
    'canonical_source_changes': 0, 'events_added': 0,
    'required_rows_completed': 0, 'global_defect_classes_closed': 0,
    'final_candidate_pdf_pages_credited': 0,
    'remaining': 'Complete and freeze A’s whole-domain derivation/counterexample, bind the final local specialization maps, then release and compare every step of R13 and settle the affected02XE scope and downstream uses before canonical admission.'
}
target = R / 'records/S6_SERIES_PUBLISH_II_R13_root_research_07.json'
assert not target.exists()
target.write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'record': binding(target), 'bound_index_files': len(evidence), 'guards_verified': len(guards), 'events_added': 0}))
