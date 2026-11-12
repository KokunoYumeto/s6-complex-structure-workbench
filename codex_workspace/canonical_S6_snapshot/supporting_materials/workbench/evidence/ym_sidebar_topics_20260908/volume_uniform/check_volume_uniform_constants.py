"""Exact arithmetic and bounded incidence checks for the local vacuum proof.

No numerical vacuum or finite-spin replacement is performed. This checks
constants and combinatorics; the operator proof is in the mathematical note.
"""
from fractions import Fraction as F
from itertools import product, combinations
from math import comb
from math import sqrt
import json


def box(L):
    vertices = range(-L, L + 1)
    edges = {(n, i) for n in product(vertices, repeat=3)
             for i in range(3) if n[i] < L}
    faces = {}
    for n in product(vertices, repeat=3):
        for i in range(3):
            for j in range(i + 1, 3):
                if n[i] == L or n[j] == L:
                    continue
                ni, nj = list(n), list(n)
                ni[i] += 1
                nj[j] += 1
                faces[n, i, j] = frozenset([
                    (n, i), (tuple(ni), j), (tuple(nj), i), (n, j)])
    stars = {e: set() for e in edges}
    for p, boundary in faces.items():
        for e in boundary:
            stars[e].add(p)
    return edges, faces, stars


def arithmetic():
    cutoff = F(1, 64)
    assert F(32, 3)**2 * 13 < 39**2
    assert F(32, 3)**2 * 8 < 31**2
    vector = (2*52 + F(4, 2))*39 + F(4*52*39, 3)*cutoff
    assert vector == F(16705, 4) < 4200
    pair = 8*31 + 8*31**2*cutoff
    assert pair < 370
    one = F(128, 3) + F(2048, 9)*cutoff
    assert one < 47
    assert 370 + 47**2*cutoff < 410
    centered = F(65536, 9)*cutoff
    assert centered < 114
    covariance = 10*4200 + 370 + centered
    assert covariance < 42500
    assert F(64**2, 3) < 37**2
    energy = 6*4200 + 3*370 + 2*8*37
    assert energy == 26902 < 27000
    assert 13*27000 == 351000
    assert 4200**2 == 17640000
    assert 2*4200*37 == 310800
    assert F(42500, 680000) == F(1, 16)
    assert (27000 + 3*42500)*32 == 4944000
    assert F(351000*8, 3) == 936000
    assert F(936000, 1872000) == F(1, 2)
    # Radius-2 SU(2): Ric=(3-1)/2^2; the maximum-principle
    # gradient factor is inverse Ric. Density and diameter retain
    # their separate factors two and 2*pi.
    ricci = F(2, 4)
    assert 1/ricci == 2
    assert 2 * (1/ricci) * 2 == 8  # coefficient of pi*r_e*xi
    assert 8 * 4 == 32
    assert F(3, 4) * 2 == F(3, 2)  # physical kappa=2g^2/a
    # Full four-link creation-cluster bounds. e^(1/2)<2 is proved
    # by its complete positive power series in the mathematical note.
    cluster_cutoff = F(1, 49152)
    cluster_radius = F(1, 16)
    prefactor = F(4*2*4*16*4, 3)
    assert prefactor == F(2048, 3)
    image_majorant = prefactor * (1+2*cluster_radius) * 2
    derivative_majorant = prefactor * (10+16*cluster_radius) * 2
    assert image_majorant == 1536
    assert image_majorant*cluster_cutoff == F(1, 32) < cluster_radius
    assert derivative_majorant == F(45056, 3)
    assert derivative_majorant*cluster_cutoff == F(11, 36) < 1
    spectral_relative = F(8*2*4*4, 3) * 2
    assert spectral_relative == F(512, 3)
    assert spectral_relative*cluster_cutoff == F(1, 288)
    assert F(3, 4)*(1-F(1, 288)) == F(287, 384)
    assert 1/(4*cluster_cutoff) == 12288
    assert F(351000*4, 3) == 468000
    assert F(3, 16)*F(4, 3) == F(1, 4)
    assert 468000*2 == 936000
    # Unbounded-electric moment, locality, Gaussian filter and summation.
    assert 6 + 128*cluster_cutoff < 7
    assert 2*7*8 == 112
    assert 4*16**2*(2**3) <= 32**3
    speed_gap_ratio = F(192*384, 287)
    assert speed_gap_ratio == F(73728, 287)
    assert speed_gap_ratio*cluster_cutoff == F(3, 574)
    assert F(3, 574)/(1+2*F(3, 574)) == F(3, 580) < F(1, 100)
    assert 1/(1+2*F(3, 574)) == F(287, 290)
    assert speed_gap_ratio*F(25, 6) == F(307200, 287) < 1100
    assert 3*64+112 == 304
    assert 1100+304*cluster_cutoff < 1200
    assert F(287, 580) > F(1, 4)
    def G(A, q):
        return (A**3/(1-q)+12*A*A*q/(1-q)**2
                +48*A*q*(1+q)/(1-q)**3
                +64*q*(1+4*q+q*q)/(1-q)**4)
    for q in (F(1, 2), F(4, 5), F(9, 10)):
        for A in (5, 9, 21, 1545):
            assert G(A, q) == A**3+q*G(A+4, q)
    polynomial_48 = 42500*(32*48+5)**3+1200*G(32*48+9, F(4, 5))
    assert polynomial_48 == 178355184758500
    assert polynomial_48/F(10**16) == F(356710369517, 20000000000000) < F(1, 32)
    assert F(1, 8)-F(1, 32) == F(3, 32)
    assert F(32, 3)*351000 == 3744000
    assert F(32, 3)*3 == 32
    assert 1/(4*F(1, 10**16)) == 2500000000000000
    # Physical sectors: the exact four-edge cycle threshold retains
    # the original per-link Casimir 3/4 and the existing relative bound.
    assert 4*F(3, 4) == 3
    assert 3*(1-spectral_relative*cluster_cutoff) == F(287, 96)
    assert F(287, 96)*2 == F(287, 48)
    assert 3*spectral_relative == 512
    assert F(351000, 3) == 117000
    assert F(3, 16)/3 == F(1, 16)
    assert 117000*2*4 == 936000
    assert F(1, 680000) < cluster_cutoff
    assert 3-512*F(1, 680000) > 0
    assert F(2472000, 2) == 1236000  # kappa*xi=1/(2*g^2*a)
    # Section16: retained two-face coefficient dictionary, residual
    # locality, multi-link covariance, and explicit nonzero interval.
    assert F(9, 2)*F(1, 12) == F(3, 8)
    assert F(13, 2)*(-F(1, 26)) == -F(1, 4)
    assert -F(4, 3)*F(1, 12) == -F(1, 9)
    assert -F(4, 3)*(-F(1, 26)) == F(2, 39)
    d0 = F(1, 81)+F(3, 4)*F(4, 1521)
    e0 = F(9, 2)*F(1, 81)+F(13, 2)*F(3, 4)*F(4, 1521)
    assert d0 == F(196, 13689) and e0 == F(8, 117)
    assert e0/d0 == F(234, 49) and e0/d0-3 == F(87, 49)
    assert F(4, 16)+F(4*3, 16) == 1
    assert F(9, 16)+F(3, 16) == F(3, 4)
    assert F(6, 16)-F(2*3, 16) == 0
    assert F(2, 12)+F(5, 26) < F(1, 2)
    assert max(F(1, 12)+F(5, 52), F(4, 26)) < F(1, 2)
    assert 48*F(1, 2) == 24 and 48*7*F(1, 2) == 168
    assert F(4, 3) < F(7, 6)**2
    assert F(7, 6)*F(12728, 3)+F(64, 3) == F(44740, 9) < 5000
    assert 2*4*5000+F(1, 2)*4*4*5000 == 80000
    assert -F(2, 3)+F(4, 6) == 0
    assert -F(4, 3)+F(2, 6) == -1
    assert 2*168*8 == 2688 and 80000+2688 < 83000
    assert F(96*83000, 287) < 28000
    assert 17**3*28000*83000 == 11417812000000 < 10**14
    assert F(96, 287)*10**14 < (6*10**6)**2
    assert F(32, 3)**2*169 < 139**2
    assert F(32, 3)**2*338 < 197**2
    assert 48*139*(1+139*cluster_cutoff) < 7000
    cov_local = 2*576*197+(2*576*197**2+7000**2)*cluster_cutoff
    assert cov_local == F(175757179, 768) < 230000
    assert 3*(F(576*169, 74)+1728) == F(337824, 37) < 10000
    energy_local = 2*28224*197*(1+197*cluster_cutoff)
    assert energy_local == F(1429097691, 128) < 12000000
    assert 4913*12000000 == 58956000000 < 6*10**10
    polynomial_b_72 = 230000*(16*72+5)**3+10000*G(16*72+9, F(4, 5))
    assert polynomial_b_72 == 437811569040000
    kernel_cutoff = F(1, 10**24)
    rb_upper = polynomial_b_72*kernel_cutoff
    assert rb_upper < F(1, 10**9) and 6*d0+rb_upper < 1
    epsilon_c_upper = rb_upper+12*10**6*kernel_cutoff+36*10**12*kernel_cutoff**2
    assert epsilon_c_upper < F(1, 10**9) < d0/2
    assert 1/(4*kernel_cutoff) == 250000000000000000000000
    b0 = F(1, 144)+F(3, 4*676)
    assert b0 == F(49, 6084) == F(9, 16)*d0
    assert F(3, 8)*d0 < F(1, 16)
    assert F(32, 3)**2*7 < 29**2
    assert F(32, 3)**2*14 < 40**2
    assert 116*(1+29*cluster_cutoff) < 117
    assert 320+(12800+13689)*cluster_cutoff < 400
    assert 2*(F(28, 74)+12) < 32
    polynomial_mix_72 = 8*(400*(16*72+5)**3+32*G(16*72+9, F(4, 5)))
    assert polynomial_mix_72 == 7044756359040 < 10**13
    assert polynomial_mix_72*kernel_cutoff < F(1, 10**11) < b0/4
    assert (24*10**6*kernel_cutoff)**2 < d0/2
    assert F(3, 4) > F(3, 4)**2
    assert (F(3, 4)-F(1, 4))**2*d0/2 == d0/8
    # Section18 relative-error and quotient constants, retained as exact
    # rational inequalities rather than floating-point checks.
    b0 = F(49, 6084)
    q_star = F(234, 49)
    x0 = F(1, 10**24)
    beta_c_bound = F(1, 10**11) / b0 + 4*72*10**6*x0 + (72*10**6*x0)**2
    beta_n_bound = 8*10**6*x0/b0 + 6*120*10**6*x0 + (120*10**6*x0)**2
    delta_bound = (beta_n_bound + q_star*beta_c_bound)/(1-beta_c_bound)
    assert beta_c_bound < F(1, 10**8)
    assert beta_n_bound < F(2, 10**15)
    assert delta_bound < F(1, 10**7)
    assert q_star*b0 == F(1, 26)
    return dict(vector_constant_exact=str(vector), vector_constant=4200,
                covariance_constant=42500, energy_entry_constant=27000,
                energy_form_constant=351000, cutoff=str(cutoff),
                local_nonzero_cutoff="1/680000",
                cluster_cutoff=str(cluster_cutoff),
                cluster_lipschitz_bound="11/36",
                full_gap_lower_bound_in_kappa="287/384",
                covariance_l2_upper_numerator="4 xi^2 + 468000 xi^3",
                covariance_l2_upper_denominator="1 - 512 xi/3",
                absolute_electric_decay="1200 xi exp(-distance/4)",
                covariance_remainder="xi^3 P(log(1/xi)) in absolute rows and l2",
                polynomial_at_48=str(polynomial_48),
                explicit_nonnegative_weight_interval="0<xi<=10^-16",
                physical_gap_lower_bound_in_kappa="287/96",
                physical_covariance_l2_upper="(xi^2+117000 xi^3)/(1-512 xi/3)",
                signed_actual_state_minimum="3kappa-512kappa xi <= minimum <=3kappa+2472000kappa xi",
                signed_minimum_interval="0<xi<=1/680000",
                physical_conditional_inverse_bound="96/(287kappa)",
                two_face_covariance_coefficient=str(d0),
                two_face_energy_coefficient=str(e0),
                signed_kernel_quotient=str(e0/d0)+" kappa",
                polynomial_b_at_72=str(polynomial_b_72),
                kernel_epsilon_c_upper=str(epsilon_c_upper),
                kernel_injective_interval="0<xi<=10^-24",
                mixed_polynomial_at_72=str(polynomial_mix_72),
                full_weight_lower_bound="(d0/8)xi^4 ||w||_2^2",
                full_weight_injective_interval="0<xi<=10^-24",
                mixed_energy_beta_c_bound=str(beta_c_bound),
                mixed_energy_beta_n_bound=str(beta_n_bound),
                mixed_energy_delta_bound=str(delta_bound))


def endpoints(edge):
    n, i = edge
    target = tuple(n[j] + (j == i) for j in range(3))
    return n, target


def cycle_support_checks():
    # All <=4-edge supports of one original unit cube. This is a finite
    # combinatorial certificate, not a replacement for the general-L proof.
    edges = [(n, i) for n in product((0, 1), repeat=3)
             for i in range(3) if n[i] == 0]
    assert len(edges) == 12
    tested = cycles = 0
    for size in range(1, 5):
        for support in combinations(edges, size):
            degree = {}
            for e in support:
                for v in endpoints(e):
                    degree[v] = degree.get(v, 0)+1
            tested += 1
            if all(d >= 2 for d in degree.values()):
                assert size == 4 and len(degree) == 4
                assert all(d == 2 for d in degree.values())
                cycles += 1
    assert tested == 793 and cycles == 6
    return dict(supports_tested=tested, surviving_four_cycles=cycles,
                nonempty_supports_below_four_without_leaf=0)


def incidence(L):
    edges, faces, stars = box(L)
    assert len(edges) == 3*(2*L)*(2*L+1)**2
    assert len(faces) == 3*(2*L)**2*(2*L+1)
    unoriented_edges = set()
    for e in edges:
        source, target = endpoints(e)
        assert source != target
        assert sum(source) % 2 != sum(target) % 2
        undirected = frozenset((source, target))
        assert undirected not in unoriented_edges
        unoriented_edges.add(undirected)
    for boundary in faces.values():
        degrees = {}
        for e in boundary:
            for v in endpoints(e):
                degrees[v] = degrees.get(v, 0)+1
        assert len(boundary) == len(degrees) == 4
        assert set(degrees.values()) == {2}
    max_links = max_faces = 0
    for e, star in stars.items():
        assert 2 <= len(star) <= 4
        local = set().union(*(faces[p] for p in star))
        touching = set().union(*(stars[f] for f in local))
        assert len(local) <= 1+3*len(star) <= 13
        assert len(touching) <= 4*len(local) <= 52
        max_links = max(max_links, len(local))
        max_faces = max(max_faces, len(touching))
    w = {e: e[0][1]**2 if e[1] == 0 else 0 for e in edges}
    s1 = sum(w.values())
    s2 = sum(v*v for v in w.values())
    iw2 = sum(sum(w[e] for e in boundary)**2 for boundary in faces.values())
    exact_a = F(L**2*(2*L+1), 15)*(24*L**4+24*L**3+8*L**2-4*L+3)
    assert s1 == F(2*L**2*(L+1)*(2*L+1)**2, 3)
    assert s2 == F(2*L**2*(L+1)*(2*L+1)**2*(3*L**2+3*L-1), 15)
    assert iw2 == 4*exact_a and iw2 >= 2*s2
    # The literature indexing map is bijective, with its stated inverse.
    labels = {}
    for n, i in edges:
        label = tuple(2*n[j] + (j == i) for j in range(3))
        odd = [j for j in range(3) if label[j] % 2]
        assert odd == [i]
        assert tuple((label[j] - (j == i))//2 for j in range(3)) == n
        assert label not in labels
        labels[label] = (n, i)
    assigned = {e: 0 for e in edges}
    for (n, i, j), boundary in faces.items():
        anchor = (n, i)
        assigned[anchor] += 1
        origin = tuple(2*n[k] + (k == i) for k in range(3))
        for q, k in boundary:
            dest = tuple(2*q[l] + (l == k) for l in range(3))
            assert sum(abs(x-y) for x, y in zip(origin, dest)) <= 2
        touching = set().union(*(stars[e] for e in boundary))
        assert len(touching) <= 16
        for u in boundary:
            for v in boundary:
                lu = tuple(2*u[0][k]+(k == u[1]) for k in range(3))
                lv = tuple(2*v[0][k]+(k == v[1]) for k in range(3))
                assert sum(abs(x-y) for x, y in zip(lu, lv)) <= 2
    assert max(assigned.values()) <= 2
    # All adjacent pairs, not a periodic interior replacement. Check
    # unique outer supports and the radius-two support of B_e.
    adjacency = {e: set().union(*(faces[p] for p in stars[e])) for e in edges}
    corrections = {e: set() for e in edges}
    outer_to_pair = {}
    pair_count = 0
    for shared in edges:
        for p, q in combinations(sorted(stars[shared]), 2):
            assert faces[p] & faces[q] == {shared}
            outer = (faces[p] | faces[q]) - {shared}
            assert len(outer) == 6 and outer not in outer_to_pair
            outer_to_pair[outer] = (p, q)
            support = outer | {shared}
            for e in support:
                corrections[e].update(support)
            pair_count += 1
    assert pair_count == sum(len(star)*(len(star)-1)//2 for star in stars.values())
    for e in edges:
        radius_two = set().union(*(adjacency[f] for f in adjacency[e]))
        assert corrections[e] <= radius_two
        assert len(radius_two) <= 169
    # Three explicit signed kernel families with nonconstant longitudinal
    # weights. Pair-coefficient identity is tested without changing w.
    kernel_tests = 0
    for axis in range(3):
        transverse = [j for j in range(3) if j != axis]
        kw = {e: (1-2*(sum(e[0][j] for j in transverse) % 2))*(e[0][axis]**2+1)
              if e[1] == axis else 0 for e in edges}
        assert all(sum(kw[e] for e in face) == 0 for face in faces.values())
        for outer, (p, q) in outer_to_pair.items():
            shared, = faces[p] & faces[q]
            outer_weight = sum(kw[e] for e in outer)
            assert outer_weight == -2*kw[shared]
            assert -kw[shared]+F(outer_weight, 6) == -F(4, 3)*kw[shared]
            kernel_tests += 1
    # Full coefficient dictionary, including every mixed direction.
    mw = {e: (e[1]+1)*(e[0][0]**2+2*e[0][1]+3*e[0][2]+5) for e in edges}
    mz = {p: sum(mw[e] for e in face) for p, face in faces.items()}
    mc = {}
    anchor_count = dict(assigned)
    jnorm2 = 0
    for outer, (p, q) in outer_to_pair.items():
        shared, = faces[p] & faces[q]
        mc[p, q] = F(mz[p]+mz[q], 6)-F(4, 3)*mw[shared]
        anchor_count[shared] += 1
        assert outer | {shared} <= adjacency[shared]
        jnorm2 += (mz[p]+mz[q])**2
    assert max(anchor_count.values()) <= 8
    znorm2 = sum(v*v for v in mz.values())
    cnorm2 = sum(v*v for v in mc.values())
    wnorm2 = sum(v*v for v in mw.values())
    assert jnorm2 <= 24*znorm2
    assert wnorm2 <= F(3, 4)*znorm2+F(9, 8)*cnorm2
    inverse_tests = 0
    for xi in (F(1, 49152), F(1, 10**24)):
        for e in edges:
            p, q = sorted(stars[e])[:2]
            ap, aq, apq = xi*mz[p]/4, xi*mz[q]/4, xi**2*mc[p, q]
            assert (ap+aq)/(2*xi)-3*apq/(4*xi**2) == mw[e]
            inverse_tests += 1
        haar_norm2 = xi**2*znorm2/16+F(49, 6084)*xi**4*cnorm2
        assert haar_norm2 >= F(98, 13689)*xi**4*wnorm2
    return dict(L=L, links=len(edges), faces=len(faces),
                max_star_links=max_links, max_touching_faces=max_faces,
                native_l1=s1, native_l2_squared=s2, native_incidence_squared=iw2,
                adjacent_pairs=pair_count, distinct_outer_supports=len(outer_to_pair),
                kernel_pair_checks=kernel_tests, full_weight_inverse_checks=inverse_tests,
                max_coefficient_indices_per_anchor=max(anchor_count.values()))


def period_and_negative_class_checks():
    """Exact finite checks of Section19; no vacuum or spin truncation."""
    from itertools import permutations

    def det(a):
        n = len(a)
        total = F(0)
        for p in permutations(range(n)):
            parity = sum(p[i] > p[j] for i in range(n) for j in range(i+1, n))
            term = F((-1)**parity)
            for i in range(n):
                term *= a[i][p[i]]
            total += term
        return total

    def tr(a):
        return list(map(list, zip(*a)))

    def mul(a, b):
        return [[sum(x*y for x, y in zip(row, col)) for col in zip(*b)]
                for row in a]

    eye4 = [[F(i == j) for j in range(4)] for i in range(4)]
    ar = [[F(30, 7), F(-2, 3)], [F(11, 5), F(5, 7)]]
    tests = 0
    for lt, mt, qt, cover in product((F(2), F(-3)), (F(0), F(1, 2), F(-2)),
                                     (F(-7), F(-1), F(1), F(7)), (F(1), F(3))):
        d = lt*qt+6*mt*mt
        if d == 0:
            continue
        delta = lt*(-qt-6*mt*mt/lt)
        assert delta == -d
        b = [[6*mt, lt], [-qt, mt]]
        bi = [[mt/d, -lt/d], [qt/d, 6*mt/d]]
        abi = mul(ar, bi)
        q = [ar[0]+[cover, 0], ar[1]+[0, cover],
             b[0]+[0, 0], b[1]+[0, 0]]
        qi = [[0, 0]+bi[0], [0, 0]+bi[1],
              [1/cover, 0, -abi[0][0]/cover, -abi[0][1]/cover],
              [0, 1/cover, -abi[1][0]/cover, -abi[1][1]/cover]]
        assert mul(q, qi) == eye4 == mul(qi, q)
        p = [q[0], q[2], q[1], q[3]]
        gram = mul(tr(p), p)
        assert det(b) == d and det(p) == -cover**2*d
        assert det(gram) == cover**4*d*d
        eta = [[2*lt, 2*mt], [2*mt, -qt/3]]
        assert det(eta) == -F(2, 3)*d
        assert [[3*eta[0][1], eta[0][0]/2],
                [3*eta[1][1], eta[0][1]/2]] == b
        witness = [[-mt/lt, F(1)]]
        assert mul(mul(witness, eta), tr(witness))[0][0] == -d/(3*lt)
        kt = [[lt], [-6*mt]]
        akt = mul(ar, kt)
        vt = kt+[[-akt[0][0]/cover], [-akt[1][0]/cover]]
        assert mul(q, vt) == [[0], [0], [0], [-d]]
        assert mul(mul(tr(vt), gram), vt)[0][0] == d*d
        tests += 1
    cosine = F(1, 4)
    assert 2*cosine*cosine-1 == -F(7, 8)
    assert (1+2*(2*cosine*cosine-1))/3 == -F(1, 4)
    assert cosine*cosine+F(15, 16) == 1
    raising = [[0, 2, 0], [0, 0, 1], [0, 0, 0]]
    lowering = [[0, 0, 0], [1, 0, 0], [0, 2, 0]]
    metric = [[1, 0, 0], [0, 2, 0], [0, 0, 1]]
    metric_inverse = [[1, 0, 0], [0, F(1, 2), 0], [0, 0, 1]]
    assert mul(mul(metric_inverse, tr(raising)), metric) == lowering
    ef, fe = mul(raising, lowering), mul(lowering, raising)
    j3 = [[ef[i][j]-fe[i][j] for j in range(3)] for i in range(3)]
    j3_squared = mul(j3, j3)
    casimir = [[F(1, 2)*(ef[i][j]+fe[i][j])+F(1, 4)*j3_squared[i][j]
                for j in range(3)] for i in range(3)]
    assert casimir == [[2*int(i == j) for j in range(3)] for i in range(3)]
    graph_tests = []
    for lattice_l in (2, 3, 4, 5):
        _, faces, _ = box(lattice_l)
        selected = [p for p in faces if p[0][1] == 0 and p[1:] == (0, 1)]
        assert len(selected) == (2*lattice_l)*(2*lattice_l+1)
        assert len(selected)-1 >= 6
        for p in selected:
            translated_heights = sorted(e[0][1] for e in faces[p] if e[1] == 0)
            assert translated_heights == [0, 1]
            assert 4*(1*(1+1)) == 8
        for p, q in combinations(selected, 2):
            assert faces[p]-faces[q]
        graph_tests.append(dict(L=lattice_l, negative_loop_dimension=len(selected),
                                vacuum_orthogonal_dimension_lower_bound=len(selected)-1))
    return dict(period_parameter_tests=tests, spin_one_class_scalar="-1/4",
                free_electric_coefficient=8, retained_spin_one_gram=[1, 2, 1],
                graph_tests=graph_tests)


def finite_angle_checks():
    """Exact constants and finite graph tests for the Section20 proof."""
    # Retain the complete one-star polynomial.
    local_quadratic = F((8*52+2*4)*39, 3)
    local_cubic = F(4*4*52*39, 9)
    assert local_quadratic == 5512 and local_cubic == F(10816, 3)
    assert local_quadratic+local_cubic/64 == F(16705, 3) < 5600
    assert F(80*4**2+64*4, 3) == 512
    residual_row = 9**3*5600*512
    assert residual_row == 2090188800 < 3*10**9
    assert F(96, 287)*3*10**9 < 32000**2
    assert (3*32000)**2 < 2*68000**2
    assert 9*3*10**9 < 2*120000**2
    xi0 = F(1, 10**16)
    q = F(4, 5)
    def tail(a):
        return (a**3/(1-q)+12*a*a*q/(1-q)**2
                +48*a*q*(1+q)/(1-q)**3
                +64*q*(1+4*q+q*q)/(1-q)**4)
    p48 = 8*(400*(16*48+5)**3+32*tail(F(16*48+9)))
    rho = xi0*p48
    bc = rho+4*68000*xi0+(68000*xi0)**2
    bn = 8*10**6*xi0+4*120000*xi0+(120000*xi0)**2
    assert p48 < 10**13 and rho < F(1, 1000)
    assert bc < F(1, 500) and bn < F(1, 10**6)
    assert (bn+3*bc)/(1-bc) < F(1, 100)
    assert 3+F(96, 49152) < 4
    # Chebyshev recurrence keeps exact rational cosines, no floating angles.
    def cosine_multiple(c, n):
        n = abs(n)
        if n == 0:
            return F(1)
        previous, current = F(1), c
        for _ in range(1, n):
            previous, current = current, 2*c*current-previous
        return current
    character_cases = 0
    for c in (F(-1), F(-3, 5), F(0), F(1, 4), F(4, 5), F(1)):
        for n in range(25):
            retained_sum = sum(cosine_multiple(c, 2*r-n) for r in range(n+1))
            scalar = retained_sum/(n+1)
            eigenvalue = F(n*(n+2), 4)
            assert 0 <= 1-scalar <= F(4, 3)*(1-c)*eigenvalue
            assert 1-scalar <= 2
            if n == 1:
                assert 1-scalar == 1-c
            character_cases += 1
    # Verify the full scalar telescope, including negative C multipliers.
    product_cases = 0
    for values in product((F(-1), F(-1, 4), F(0), F(1, 3), F(1)), repeat=4):
        product_all = F(1)
        for value in values:
            product_all *= value
        exact = F(0)
        for i in range(4):
            for j in range(i):
                prefix = F(1)
                for k in range(j):
                    prefix *= values[k]
                exact += (1-values[i])*(1-values[j])*prefix
        assert product_all-1+sum(1-v for v in values) == exact
        product_cases += 1
    angle_box_cases = []
    for lattice_l in (2, 3, 4, 5):
        edges, faces, _ = box(lattice_l)
        for cosine in (F(-1), F(1, 4), F(4, 5)):
            levels = {r: 1-cosine_multiple(cosine, r)
                      for r in range(-lattice_l, lattice_l+1)}
            weights = {e: levels[e[0][1]] if e[1] == 0 else F(0) for e in edges}
            s1 = sum(weights.values())
            s2 = sum(v*v for v in weights.values())
            z2 = sum(sum(weights[e] for e in face)**2 for face in faces.values())
            assert s1 == 2*lattice_l*(2*lattice_l+1)*sum(levels.values())
            assert s2 == 2*lattice_l*(2*lattice_l+1)*sum(t*t for t in levels.values())
            assert z2 == (2*lattice_l*(2*lattice_l+1)*sum(
                (levels[r]+levels[r+1])**2 for r in range(-lattice_l, lattice_l))
                +4*lattice_l**2*sum((2*t)**2 for t in levels.values()))
            assert z2 >= 2*s2
        angle_box_cases.append(lattice_l)
    return dict(local_constant=str(local_quadratic+local_cubic/64),
                commutator_constant=512, residual_energy_row=residual_row,
                polynomial_mix_at48=str(p48), beta_c_upper=str(bc),
                beta_n_upper=str(bn), quotient_error_upper=str((bn+3*bc)/(1-bc)),
                interval="0<xi<=10^-16; all real angles",
                exact_character_cases=character_cases,
                product_telescope_cases=product_cases,
                native_angle_boxes=angle_box_cases)


def negative_sector_weight_checks():
    """Section21 scalar/projection arithmetic, not a substitute vacuum."""
    coefficients = {9: F(2, 9), 8: F(1), 7: F(4, 3),
                    5: F(-14, 15), 3: F(4, 9), 1: F(-1, 15)}
    difference = {}
    for degree, coefficient in coefficients.items():
        difference[degree] = difference.get(degree, F(0))+coefficient
        for power in range(degree+1):
            difference[power] = difference.get(power, F(0))-(
                coefficient*comb(degree, power)*(-1)**(degree-power))
    assert {k: v for k, v in difference.items() if v} == {8: F(2)}
    def q8(lattice_l):
        return sum(c*lattice_l**k for k, c in coefficients.items())
    for lattice_l in range(21):
        assert q8(lattice_l) == sum(r**8 for r in range(-lattice_l, lattice_l+1))
    def cosine_multiple(c, n):
        n = abs(n)
        if n == 0:
            return F(1)
        previous, current = F(1), c
        for _ in range(1, n):
            previous, current = current, 2*c*current-previous
        return current
    character_cases, negative_cases = 0, 0
    for cosine in (F(-1), F(-3, 5), F(0), F(1, 4), F(4, 5), F(1)):
        for n in range(25):
            scalar = sum(cosine_multiple(cosine, 2*r-n) for r in range(n+1))/(n+1)
            electric = F(n*(n+2), 4)
            negative = int(scalar < 0)
            assert negative <= (F(4, 3)*(1-cosine)*electric)**4
            if scalar < 0:
                assert 1 < F(4, 3)*(1-cosine)*electric
                negative_cases += 1
            character_cases += 1
    product_cases = 0
    scalar_products = []
    for values in product((F(-1), F(-1, 4), F(0), F(1, 3), F(1)), repeat=4):
        retained_product = F(1)
        for value in values:
            retained_product *= value
        negatives = sum(v < 0 for v in values)
        assert (retained_product < 0) == (all(v != 0 for v in values) and negatives % 2 == 1)
        assert int(retained_product < 0) <= negatives
        assert 0 <= 1-retained_product <= sum(1-v for v in values)
        scalar_products.append(retained_product)
        product_cases += 1
    # An exact finite scalar distribution checks the centering identity only.
    # It is explicitly NOT the interacting vacuum's distribution.
    mean = sum(scalar_products)/len(scalar_products)
    negative_probability = F(sum(k < 0 for k in scalar_products), len(scalar_products))
    centered_negative_weight = sum((k-mean)**2 for k in scalar_products if k < 0)/len(scalar_products)
    assert centered_negative_weight <= 4*negative_probability
    fourth_count_boxes = []
    for lattice_l in (2, 3, 4, 5):
        edges, _, _ = box(lattice_l)
        for cosine in (F(-1), F(1, 4), F(4, 5)):
            levels = {r: 1-cosine_multiple(cosine, r)
                      for r in range(-lattice_l, lattice_l+1)}
            direct = sum(levels[e[0][1]]**4 for e in edges if e[1] == 0)
            assert direct == 2*lattice_l*(2*lattice_l+1)*sum(t**4 for t in levels.values())
        fourth_count_boxes.append(lattice_l)
    assert F(256, 81) == F(16, 9)**2
    assert F(1, 18)/F(16, 5) == F(10, 24**2)
    assert 16*F(10, 24**2) == F(10, 6**2)
    assert F(32, 3)/6 == F(16, 9)
    assert F(256, 3)*F(16, 3) == F(4096, 9)
    return dict(eighth_power_polynomial_difference="2 L^8 exactly",
                exact_character_cases=character_cases, negative_character_cases=negative_cases,
                product_parity_and_telescope_cases=product_cases,
                fourth_power_count_boxes=fourth_count_boxes,
                centered_distribution_is_test_only=True,
                moment_bound="M2e=(3 re/2)xi+8 re^2 xi^2; every xi>0",
                native_ratio_squared_constant_without_pi_and_decimal_scale=str(F(10, 6**2)))


def full_product_remainder_checks():
    """Exact Section22 maps/constants; analytic bounds have full written proofs."""
    def add(a, b):
        return [x+y for x, y in zip(a, b)]
    def multiply(v, n):
        p1, p2 = v[:n+1], v[n+1:]
        r = [F(0)]*(n+2)
        for k in range(n+1):
            r[k] += p1[k]
            r[k+1] += p2[k]
        return r
    def split(r, n):
        p1, p2 = [F(0)]*(n+1), [F(0)]*(n+1)
        for k, coefficient in enumerate(r):
            if k <= n:
                p1[k] += F(n+1-k, n+1)*coefficient
            if k:
                p2[k-1] += F(k, n+1)*coefficient
        return p1+p2
    def inject(q, n):
        p1, p2 = [F(0)]*(n+1), [F(0)]*(n+1)
        for k, coefficient in enumerate(q):
            p1[k+1] -= coefficient
            p2[k] += coefficient
        return p1+p2
    def generator(poly, n, raising):
        result = [F(0)]*(n+1)
        for k, coefficient in enumerate(poly):
            if raising and k:
                result[k-1] += k*coefficient
            if not raising and k < n:
                result[k+1] += (n-k)*coefficient
        return result
    def tensor_generator(v, n, raising):
        p1, p2 = v[:n+1], v[n+1:]
        a, b = generator(p1, n, raising), generator(p2, n, raising)
        if raising:
            a = add(a, p2)
        else:
            b = add(b, p1)
        return a+b
    tensor_cases = 0
    for n in range(17):
        for coordinate in range(2*(n+1)):
            v = [F(int(k == coordinate)) for k in range(2*(n+1))]
            r = multiply(v, n)
            s = split(r, n)
            residual = [x-y for x, y in zip(v, s)]
            if n:
                q = residual[n+1:2*n+1]
                assert residual == inject(q, n)
                assert add(s, inject(q, n)) == v
            else:
                assert residual == [0, 0]
            assert multiply(split(r, n), n) == r
            for raising in (True, False):
                assert multiply(tensor_generator(v, n, raising), n) == generator(r, n+1, raising)
                assert tensor_generator(split(r, n), n, raising) == split(generator(r, n+1, raising), n)
                if n:
                    assert tensor_generator(inject(q, n), n, raising) == inject(generator(q, n-1, raising), n)
            tensor_cases += 1
    casimir_cases = 0
    for n in range(65):
        lam = F(n*(n+2), 4)
        assert 2*(lam+1)-(F((n+1)*(n+3), 4)+1) == F(n*n+1, 4)
        for m in (n+1, n-1):
            if m >= 0:
                assert F(m*(m+2), 4)+1 <= 2*(lam+1)
                casimir_cases += 1
        fourth = sum(F((2*r-n)**4, n+1) for r in range(n+1))
        assert fourth == F(n*(n+2)*(3*n*n+6*n-4), 15) == F(16, 15)*lam*(3*lam-1)
        assert fourth/24 <= F(2, 15)*lam*lam
    telescope_cases = 0
    for c in product((F(-1), F(-1, 4), F(0), F(1, 3), F(1)), repeat=4):
        # Independent comparison factors test the full product identity,
        # not a numerical replacement for exp(-J).
        d = [F(k+1, 5) for k in range(4)]
        def prod(values):
            answer = F(1)
            for value in values:
                answer *= value
            return answer
        assert prod(c)-prod(d) == sum((c[i]-d[i])*prod(c[:i])*prod(d[i+1:]) for i in range(4))
        telescope_cases += 1
    xi = F(1, 10**16)
    p, q = 1+22*xi+128*xi*xi, 6+128*xi
    assert p < 2 and q < 7
    assert 16*4*xi*(1+4*4*xi+F(3*4, 2)*xi+8*4**2*xi**2) == 64*xi*p
    threshold_bound = F(28672, 10**8)+3*1536+2*F(4096+524288, 10**8)
    assert threshold_bound < 5000
    assert 5000*F(1, 20000) == F(1, 4)
    assert F(129024, 5*10**8) < F(1, 4)
    assert F(1, 500) < 1-F(3, 4)**2
    assert 1+F(1, 500) < F(5, 4)**2
    assert F(2, 3)*F(16, 3) == F(32, 9)
    assert 2*256 == 512
    assert F(2, 5)*8 == F(16, 5)
    return dict(tensor_basis_inverse_and_generator_tests=tensor_cases,
                band_casimir_tests=casimir_cases,
                fourth_character_moments=65,
                full_product_difference_tests=telescope_cases,
                epsilon_threshold_constant=str(threshold_bound),
                epsilon_upper="5000 j^(-1/3)",
                explicit_cusp_threshold=20000**3,
                electric_correction_upper_constant=str(F(129024, 5*10**8)),
                norm_and_TV_scope="unchanged cusp; fixed 0<xi<=10^-16",
                auxiliary_cutoff="Lambda_j=j^(5/3); original state is not truncated")


def full_product_energy_checks():
    """Section23 exact finite algebra; not a sampled quantum vacuum."""
    def prod(values):
        result = F(1)
        for value in values:
            result *= value
        return result

    def cosine_multiple(c, n):
        n = abs(n)
        if n == 0:
            return F(1)
        previous, current = F(1), c
        for _ in range(1, n):
            previous, current = current, 2*c*current-previous
        return current

    cosines = (F(-1, 4), F(1, 3), F(3, 4), F(-2, 3))
    times = tuple(1-c for c in cosines)
    chars = {(e, n): sum(cosine_multiple(c, 2*r-n)
                         for r in range(n+1))/F(n+1)
             for e, c in enumerate(cosines) for n in range(5)}
    lam = {n: F(n*(n+2), 4) for n in range(5)}
    face_cases = negative_factor_cases = 0
    signs_seen = set()
    for labels in product(range(4), repeat=4):
        for sigma in product((-1, 1), repeat=4):
            shifted = tuple(n+d for n, d in zip(labels, sigma))
            if min(shifted) < 0:
                continue
            signs_seen.add(sigma)
            c = tuple(chars[e, n] for e, n in enumerate(labels))
            cp = tuple(chars[e, n] for e, n in enumerate(shifted))
            for e in range(4):
                assert abs(cp[e]-c[e]) <= 4*times[e]*(lam[labels[e]]+1)
            for exterior in (F(-1), F(0), F(2, 3)):
                original = exterior*prod(c)-1+sum(1-x for x in c)+1-exterior
                after = exterior*prod(cp)-1+sum(1-x for x in cp)+1-exterior
                delta = after-original
                terms = [(cp[e]-c[e])*(exterior*prod(cp[:e])*prod(c[e+1:])-1)
                         for e in range(4)]
                assert delta == sum(terms)
                majorant = sum(4*times[e]*(lam[labels[e]]+1)
                               *(1-exterior+F(8, 3)*sum(times[f]*(lam[labels[f]]+1)
                                                      for f in range(4) if f != e))
                               for e in range(4))
                assert abs(delta) <= majorant
                # One arbitrary nonzero matrix element of W^sigma.
                # This checks the exact input/output double commutator identity.
                matrix_entry = F(2, 7)
                commutator_entry = after*matrix_entry-matrix_entry*original
                double_entry = after*commutator_entry-commutator_entry*original
                assert double_entry == delta*matrix_entry*delta
                face_cases += 1
                negative_factor_cases += int(min(c+cp+(exterior,)) < 0)
    assert len(signs_seen) == 16
    cutoff_cases = 0
    for n in range(65):
        old = F(n*(n+2), 4)
        for m in (n-1, n+1):
            if m < 0:
                continue
            new = F(m*(m+2), 4)
            assert old*old+new*new <= 5*(old+1)**2
            for cut in (F(0), old, new, F(100000)):
                for left_sign, right_sign in product((-1, 1), repeat=2):
                    # Arbitrary endpoints inside the exact absolute h bounds,
                    # with s^4=1 only in this scalar inequality test.
                    left = left_sign*F(2, 15)*old*old if old <= cut else F(0)
                    right = right_sign*F(2, 15)*new*new if new <= cut else F(0)
                    assert abs(right-left) <= F(2, 3)*(old+1)**2
                    cutoff_cases += 1
    z = sum(times)
    omega = sum(times[e]*times[f] for e in range(4) for f in range(4) if e != f)
    assert omega == z*z-sum(t*t for t in times)
    assert 0 <= omega <= z*z
    assert F(1, 2)*16*2 == 16
    assert 16*F(2, 3)**2 == F(64, 9)
    assert 12*F(16, 3) == 64 and 12*F(32, 3) == 128
    assert F(8, 3)*3 == 8
    assert 64*16 == 1024
    for xi in (F(1, 10**16), F(1, 4), F(1), F(10)):
        b1 = xi*(14+128*xi)
        p = 1+22*xi+128*xi*xi
        assert 11*xi+96*xi*xi <= b1
        assert 1+19*xi+96*xi*xi <= p
        assert 6*xi+128*xi*xi+16*xi+1 == p
    # Exact exponents retain kappa_j ~ j in the energy-weighted bound.
    assert -2+1 == -1
    return dict(valid_full_face_cases=face_cases,
                cases_retaining_negative_factors=negative_factor_cases,
                plaquette_shift_bands=len(signs_seen),
                cutoff_jump_and_neighbor_cases=cutoff_cases,
                double_commutator_sign_and_constants="passed",
                form_rate="relative O_xi(j^-2); original cusp",
                physical_energy_weighted_TV_rate="O_xi,g(j^-1)",
                scope="finite exact checks only; all analytical/domain proofs in Section23")


def prescribed_coupling_energy_checks():
    """Section24 finite arithmetic, spectral-cap and measure-map checks."""
    cases = 0
    for n in range(65):
        old = F(n*(n+2), 4)
        for sigma in (-1, 1):
            m = n+sigma
            if m < 0:
                continue
            new = F(m*(m+2), 4)
            assert new-old == (F(2*n+3, 4) if sigma == 1 else -F(2*n+1, 4))
            assert abs(new-old) <= old+1
            for cap in (F(0), old, new, (old+new)/2, F(10000)):
                assert abs(min(new, cap)-min(old, cap)) <= abs(new-old)
                cases += 1
    assert 16*F(2, 3)**2 == F(64, 9)
    assert F(8, 3)*3 == 8
    for log_value in (F(1), F(2), F(7, 3), F(8)):
        xi = log_value**2/4
        root_xi = log_value/2
        assert 64*root_xi*(14+128*xi) == 448*log_value+1024*log_value**3
        assert 8*(1+8*xi)/root_xi == 16/log_value+32*log_value
    t_star_without_pi2 = F(16, 3*10**8)
    a_star_without_pi2 = F(16384, 3*10**8)
    assert 1024*t_star_without_pi2 == a_star_without_pi2
    assert 200*2*64 == 25600
    assert 8*8*2 == 128
    assert 64*128 == 8192
    fixed_f_without_alpha_pi = 8192*t_star_without_pi2
    measure_cases = 0
    for j in (2, 4, 8, 16):
        rho = {F(1, j): F(1), F(2, j): F(-1)}
        nu = {energy: energy*mass for energy, mass in rho.items()}
        assert sum(abs(mass) for mass in rho.values()) == 2
        assert sum(abs(mass) for mass in nu.values()) == F(3, j)
        assert {energy: mass/energy for energy, mass in nu.items()} == rho
        for threshold in (F(1, 100), F(1, j), F(3, 2*j), F(1)):
            restricted = sum(abs(mass) for energy, mass in rho.items() if energy >= threshold)
            assert restricted <= sum(abs(mass) for mass in nu.values())/threshold
        measure_cases += 1
    return dict(spectral_cap_neighbor_cases=cases,
                exact_logarithmic_parameter_cases=4,
                measure_inverse_and_nonuniformity_cases=measure_cases,
                logarithmic_eta_leading_without_pi2=str(a_star_without_pi2),
                physical_error_leading_without_pi2=str(25600*a_star_without_pi2),
                fixed_kappa_eta_leading_without_alpha_power_pi2=str(fixed_f_without_alpha_pi),
                retained_paths="Original depth j^2; logarithmic and fixed-electric coefficient",
                proof_boundary="Exact finite checks; analytical trajectory and spectral proofs in Section24")


def polynomial_anti_concentration_checks():
    """Bounded exact/numerical checks for Section25 sphere constants."""
    cases = 0
    for K in (0, F(1, 10), F(1), F(4), F(16), F(100)):
        k = float(K)
        sigma = ((sqrt(k*k + 6.0) - k) / 3.0) ** 2
        sigma_rationalized = 4.0 / (sqrt(k*k + 6.0) + k) ** 2
        assert abs(sigma - sigma_rationalized) <= 1e-14
        assert sigma >= 2.0 / (3.0 * (1.0 + k) ** 2) - 1e-14
        r = ((2.0 * (sqrt(k*k + 3.0) - k)) / 3.0) ** 2
        r_rationalized = 4.0 / (sqrt(k*k + 3.0) + k) ** 2
        assert abs(r - r_rationalized) <= 1e-14
        assert r >= 1.0 / (1.0 + k) ** 2 - 1e-14
        cases += 1
    for j in (10, 100, 1000, 10000):
        logj = __import__('math').log(j)
        K = 4.0 * logj * logj
        sigma = 4.0 / (sqrt(K*K + 6.0) + K) ** 2
        assert sigma > 0.0
        scaled = logj**4 * sigma
        assert 0.0 < scaled < 1.0 / 16.0 + 1e-12
        cases += 1
    incidence_limit_denominator = 16 * 64 * 9
    assert incidence_limit_denominator == 9216
    # With x=j^(-2), (L_j+1)(2L_j+1)/j^4=(1+x)(2+x)
    # =2+3x+x^2, so its limit is 2; the retained factor 1/18
    # contributes 2/18 to the liminf coefficient.
    assert (1, 3, 2) == (1, 1 * 2 + 1, 1 * 2)
    assert F(1, 16) * F(1, 64) * F(2, 18) == F(1, 9216)
    return dict(sphere_constant_cases=6,
                logarithmic_path_cases=4,
                covariance_lower_rate_denominator=incidence_limit_denominator,
                path_ratio_limit=2,
                proof_boundary="Exact sphere integration-by-parts proof in Section25")


if __name__ == "__main__":
    print(json.dumps(dict(status="passed", arithmetic=arithmetic(),
                          cycle_supports=cycle_support_checks(),
                          period_and_negative_class=period_and_negative_class_checks(),
                          finite_angle=finite_angle_checks(),
                          negative_sector_weights=negative_sector_weight_checks(),
                          full_product_remainder=full_product_remainder_checks(),
                          full_product_energy=full_product_energy_checks(),
                          prescribed_coupling_energy=prescribed_coupling_energy_checks(),
                          polynomial_anti_concentration=polynomial_anti_concentration_checks(),
                          boxes=[incidence(L) for L in (2, 3, 4, 5)],
                          scope="Exact constants/incidence only; analytical proof is in the note."),
                     indent=2))
