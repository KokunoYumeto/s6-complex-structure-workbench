"""Exact finite certificates for the 50/II and 56/II modular constructions.

The accompanying TeX proves geometric realization and the identification of the
section cocycle lattice.  This program checks the finite group, polynomial and
integral-linear-algebra steps of that proof.  It does not infer geometry from
matrix products.  Only Python's standard library is needed for these checks;
the archived section module is additionally compared as a separate check.
"""
from collections import deque
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import importlib.util
import json

CODE = Path(__file__).resolve().parent
OUT = CODE / 'maps_D_review'
OUT.mkdir(parents=True, exist_ok=True)
I = (1, 0, 0, 1)
S = (0, -1, 1, 0)
R = (0, -1, 1, 1)
T = (1, 1, 0, 1)


def mul(a, b):
    return (a[0]*b[0]+a[1]*b[2], a[0]*b[1]+a[1]*b[3],
            a[2]*b[0]+a[3]*b[2], a[2]*b[1]+a[3]*b[3])


def inv(a):
    assert a[0]*a[3]-a[1]*a[2] == 1
    return a[3], -a[1], -a[2], a[0]


def power(a, n):
    if n < 0:
        return power(inv(a), -n)
    b = I
    for _ in range(n):
        b = mul(b, a)
    return b


def neg(a):
    return tuple(-x for x in a)


def psl(a):
    return a if next(x for x in a if x) > 0 else neg(a)


def conj(a, b):
    return mul(mul(a, b), inv(a))


def mv(a, x):
    return (a[0]*x[0]+a[1]*x[1], a[2]*x[0]+a[3]*x[1])


def difference(a):
    return a[0]-1, a[1], a[2], a[3]-1


def wedge(a, b):
    return a[0]*b[1]-a[1]*b[0]


def product(mats):
    a = I
    for b in mats:
        a = mul(a, b)
    return a


def mat_json(a):
    return [list(a[:2]), list(a[2:])]


def word_matrix(word):
    return product(S if x == 's' else R if x == 'r' else inv(R)
                   for x in word)


def matrix_word(a):
    """Euclidean decomposition in PSL2Z; checked against the input matrix."""
    b, word = a, ''
    while b[2]:
        n = b[0] // b[2]
        word += ('sr'*n if n >= 0 else 'Rs'*(-n)) + 's'
        b = mul(mul(S, power(T, -n)), b)
    n = b[1] // b[0]
    word += 'sr'*n if n >= 0 else 'Rs'*(-n)
    assert psl(word_matrix(word)) == psl(a)
    return word


def act(table, q, word):
    for x in word:
        q = table[q][{'s': 0, 'r': 2, 'R': 3}[x]]
    return q


def cycles(p):
    seen, result = set(), []
    for i in range(len(p)):
        if i not in seen:
            j, cyc = i, []
            while j not in seen:
                seen.add(j)
                cyc.append(j)
                j = p[j]
            assert j == i
            result.append(cyc)
    return result


def check_coset_table(table, generators):
    n = len(table)
    for q in range(n):
        assert act(table, q, 'ss') == q
        assert act(table, q, 'rrr') == q
        assert act(table, q, 'rR') == q
        assert table[q][0] == table[q][1]
    reps, queue = {0: ''}, deque([0])
    while queue:
        q = queue.popleft()
        for x in 'srR':
            j = act(table, q, x)
            if j not in reps:
                reps[j] = reps[q] + x
                queue.append(j)
    assert len(reps) == n
    words = [matrix_word(a) for a in generators]
    assert all(act(table, 0, w) == 0 for w in words)
    # Schreier's elementary rewriting: each stabilizer word is a product of
    # rep(q)*x*rep(q.x)^(-1).  Supply a checked peripheral word for EVERY such
    # generator, proving the reverse containment without Todd--Coxeter.
    targets = {}
    raw = []
    for q in range(n):
        for x in 'srR':
            j = act(table, q, x)
            a = psl(mul(mul(word_matrix(reps[q]), word_matrix(x)),
                        inv(word_matrix(reps[j]))))
            targets[a] = None
            raw.append((q, x, j, a))
    letters = [(i+1, a) for i, a in enumerate(generators)]
    letters += [(-i-1, inv(a)) for i, a in enumerate(generators)]
    known, queue = {I: ()}, deque([I])
    todo = set(targets)-{I}
    while todo:
        assert queue, 'Peripheral generators do not generate the stabilizer'
        a = queue.popleft()
        w = known[a]
        assert len(w) < 9, 'Increase the independent membership-search bound'
        for letter, g in letters:
            if w and w[-1] == -letter:
                continue
            b = psl(mul(a, g))
            if b not in known:
                known[b] = w+(letter,)
                queue.append(b)
                todo.discard(b)
    witnesses = []
    for q, x, j, a in raw:
        w = known[a]
        check = product(generators[i-1] if i > 0 else inv(generators[-i-1])
                        for i in w)
        assert psl(check) == a
        witnesses.append({'coset': q, 'letter': x, 'next_coset': j,
                          'matrix_PSL': mat_json(a), 'peripheral_word': list(w)})
    sp = [act(table, q, 's') for q in range(n)]
    rp = [act(table, q, 'r') for q in range(n)]
    tp = [act(table, q, 'sr') for q in range(n)]
    ram = sum(n-len(cycles(p)) for p in (sp, rp, tp))
    assert ram == 2*n-2
    return {'index': n, 'table_columns': ['s','s^-1','r','r^-1'],
            'table': table, 'representatives': reps,
            'generator_words_s_r': words, 's_cycles': cycles(sp),
            'r_cycles': cycles(rp), 'cusp_cycles': cycles(tp),
            'ramification_sum': ram, 'genus': 0,
            'schreier_membership_witnesses': witnesses}


def peripheral_ribbon_certificate(table, boundary_words):
    """The actual punctured-surface group, before imposing the cone relation.

    Vertices b_i and w_i are r- and s-orbits; edge q joins them, subdivided
    at a vertex also called q.  A fixed r-orbit is punctured, so its r-loop
    is retained as a free generator, not subjected to r^3=1.  Contracting
    a specified spanning tree computes the full peripheral words in a
    free group.  This is stronger than their identity in PSL2Z.
    """
    n = len(table)
    rc = cycles([act(table,q,'r') for q in range(n)])
    sc = cycles([act(table,q,'s') for q in range(n)])
    black = {q:'b'+str(i) for i,c in enumerate(rc) for q in c}
    white = {q:'w'+str(i) for i,c in enumerate(sc) for q in c}
    adjacency, edges = {}, []
    for q in range(n):
        for v in [black[q],white[q]]:
            e = len(edges); edges.append((str(q),v))
            adjacency.setdefault(str(q),[]).append((v,e))
            adjacency.setdefault(v,[]).append((str(q),e))
    tree, seen, queue = set(), {'0'}, deque(['0'])
    while queue:
        v = queue.popleft()
        for u,e in adjacency[v]:
            if u not in seen:
                seen.add(u);tree.add(e);queue.append(u)
    extra = {e:i+1 for i,e in enumerate(e for e in range(len(edges)) if e not in tree)}
    ell = {q:len(extra)+i+1 for i,q in enumerate(q for q in range(n) if act(table,q,'r')==q)}

    def reduce(word):
        reduced = []
        for x in word:
            if reduced and reduced[-1] == -x:
                reduced.pop()
            else:
                reduced.append(x)
        return reduced

    def translate(word):
        q, result = 0, []
        for x in word:
            j = act(table,q,x)
            if x != 's' and j == q:
                result.append(ell[q] if x == 'r' else -ell[q])
            else:
                e0 = 2*q+(x=='s');e1 = 2*j+(x=='s')
                if e0 in extra:result.append(extra[e0])
                if e1 in extra:result.append(-extra[e1])
            q = j
        assert q == 0
        return reduce(result)

    boundary = {name:translate(w) for name,w in boundary_words}
    assert reduce(sum(boundary.values(),[])) == []
    expected = ([2,-1],[1],[-2]) if n==4 else ([3,-2],[1],[-1,2],[-3])
    assert list(boundary.values()) == list(map(list,expected))
    return {'black_orbits_clockwise':rc,'white_orbits':sc,
            'oriented_half_edges':edges,'spanning_tree_edge_indices':sorted(tree),
            'non_tree_half_edges':{i:{'edge_index':e,'oriented_edge':edges[e]} for e,i in extra.items()},
            'punctured_elliptic_loops':ell,
            'boundary_words_in_s_r':dict(boundary_words),
            'boundary_words_in_free_generators':boundary,
            'boundary_product_reduces_freely_to_identity':True,
            'full_surface_group_rank':len(extra)+len(ell),
            'generation':'Displayed boundary words recover each free generator directly.'}


def poly_mul(a, b):
    c = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    return c


def polynomial_50():
    c4 = poly_mul([0,0,1], poly_mul([27,1], [3,1]))
    c6 = poly_mul([0,0,0,1], poly_mul([27,1], [-27,18,1]))
    delta = poly_mul([0]*7+[1], poly_mul([27,1], [27,1]))
    a, b = poly_mul(poly_mul(c4,c4),c4), poly_mul(c6,c6)
    z = [x-y for x,y in zip(a,b)]
    assert z == [1728*x for x in delta] + [0]*(len(z)-len(delta))
    return {'c4_coefficients_ascending': c4, 'c6_coefficients_ascending': c6,
            'Delta_coefficients_ascending': delta,
            'identity': 'c4^3-c6^2=1728*Delta',
            'orders_c4_c6_Delta': {'t=0':[2,3,7], 't=-27':[1,1,2],
                                  't=infinity':[0,0,3]}}


def section_certificate(mats, q, z, ii_index, height):
    assert product(mats) == I
    prefix, charges, diagonal = I, [], []
    for a, v, lift in zip(mats, q, z):
        assert mv(difference(a), lift) == tuple(v)
        charges.append(mv(prefix, v))
        diagonal.append(wedge(lift, v))
        prefix = mul(prefix, a)
    assert tuple(map(sum,zip(*charges))) == (0,0)
    cross = [wedge(charges[i],charges[j]) for i in range(len(mats))
             for j in range(i+1,len(mats))]
    central = sum(diagonal)-sum(cross)
    assert central == -height
    a = difference(mats[ii_index])
    assert a[0]*a[3]-a[1]*a[2] == 1
    gauge = mv(inv(a), q[ii_index])
    q0 = [tuple(x-y for x,y in zip(v,mv(difference(a),gauge)))
          for a,v in zip(mats,q)]
    assert q0[ii_index] == (0,0)
    # Independently check that the displayed q0 spans the complete gauged
    # integral cocycle lattice.  All remaining local rank-one coordinates
    # are their primitive columns.  For 50 the last rank-two charge is
    # uniquely determined; for 56 the relation has rank two and primitive
    # kernel (1,1,1).
    if len(mats) == 3:
        assert q0 == [(0,0),(-2,1),(2,-1)]
        local = q0[1]
        assert abs(local[1]) == 1
        relation_description = 'After q_II=0, q_I3=k*(-2,1) and q_I1star=k*(2,-1), uniquely, for every k in Z.'
    else:
        assert q0 == [(-2,1),(0,0),(4,-3),(1,-1)]
        nonzero = [v for i,v in enumerate(charges) if i != ii_index]
        assert nonzero == [(-2,1),(1,0),(1,-1)]
        assert wedge(nonzero[0],nonzero[1]) == -1
        assert tuple(map(sum,zip(*nonzero))) == (0,0)
        relation_description = 'After q_II=0, the relation columns (-2,1),(1,0),(1,-1) have integral kernel Z*(1,1,1).'
    # Explicit conversion to Fukae's reverse-product/inverse-circuit convention.
    prefix, circuits, fcharges, fpreimages = I, [], [], []
    for a,v,lift in zip(mats,q,z):
        k = conj(prefix,inv(a))
        y = mv(prefix,v)
        pre = mv(prefix,tuple(x+y for x,y in zip(lift,v)))
        assert tuple(x-y for x,y in zip(pre,mv(k,pre))) == y
        circuits.append(k); fcharges.append(y); fpreimages.append(pre)
        prefix = mul(prefix,a)
    assert product(circuits) == I
    assert sum(wedge(x,y) for x,y in zip(fpreimages,fcharges)) == sum(diagonal)
    fukae_order = list(reversed(range(len(mats))))
    fukae_cross = sum(wedge(fcharges[i],fcharges[j])
                       for a,i in enumerate(fukae_order) for j in fukae_order[a+1:])
    assert fukae_cross == -sum(cross)
    assert sum(diagonal)+fukae_cross == -height
    return {'cocycle':q,'local_rational_preimages':z,'prefix_charges':charges,
            'diagonal_wedges':diagonal,'ordered_cross_wedges':cross,
            'central_entry':central,'height':height,'II_gauge':gauge,
            'gauged_cocycle':q0,'primitive_generator_proof':relation_description,
            'torsion':[],'Fukae_circuits_in_reversed_order':
              [mat_json(circuits[i]) for i in fukae_order],
            'Fukae_charges_in_reversed_order':[fcharges[i] for i in fukae_order]}


H = conj(S,inv(R))
V = conj(inv(R),T)
B3 = power(V,3)
stem7 = mul(mul(R,S),inv(R))
C2 = conj(stem7,power(T,2))
assert H == (0,1,-1,1)
assert V == (2,1,-1,0)
assert C2 == (5,2,-8,-3)

data = {
  50: {'table':[[1,1,2,3],[0,0,1,1],[3,3,3,0],[2,2,0,2]],
       'canonical':[H,power(T,3),neg(V)],'conjugator':V,
       'matrices':[(3,7,-1,-2),(7,12,-3,-5),(-2,-1,1,0)],
       'q':[(-5,2),(-8,4),(0,1)],
       'z':[(Q(1),Q(-1)),(Q(-4,3),Q(0)),(Q(1,4),Q(-3,4))],
       'types':['II','I3','I1*'],'ii':0,'height':Q(1,12)},
  56: {'table':[[1,1,2,3],[0,0,1,1],[4,4,3,0],[5,5,0,2],
               [2,2,6,7],[3,3,8,9],[9,9,7,4],[8,8,4,6],
               [7,7,9,5],[6,6,5,8]],
       'canonical':[C2,H,power(T,5),B3],'conjugator':B3,
       'matrices':[(5,8,-2,-3),(27,37,-19,-26),(61,80,-45,-59),(4,3,-3,-2)],
       'q':[(-2,1),(0,0),(4,-3),(1,-1)],
       'z':[(Q(-1,2),Q(0)),(Q(0),Q(0)),(Q(-1,5),Q(1,5)),(Q(1,3),Q(0))],
       'types':['I2','II','I5','I3'],'ii':1,'height':Q(1,30)}}

profile_path = CODE/'maps_D_project/records/explorer/api/engine/collision_profiles.json'
engine_path = profile_path.with_name('os_monodromy.py')
profiles = json.loads(profile_path.read_text())['profiles']
spec = importlib.util.spec_from_file_location('archived_os_monodromy',engine_path)
engine = importlib.util.module_from_spec(spec)
spec.loader.exec_module(engine)
certificate = {'schema':1,'date':'2026-11-17 UTC',
 'checker':'GPT-6 Astra (OpenAI, ChatGPT Pro mode), effort Pro',
 'scope':'Finite exact checks; geometry and marking proved in maps_modular_collision_realizations.tex',
 'profile_data_sha256':hashlib.sha256(profile_path.read_bytes()).hexdigest(),
 'archived_engine_sha256':hashlib.sha256(engine_path.read_bytes()).hexdigest(),
 'models':{}}
for n,d in data.items():
    canonical = d['canonical']
    assert product(canonical) == I
    assert [conj(d['conjugator'],a) for a in canonical] == d['matrices']
    profile = next(x for x in profiles if x['os_entry']==n and x['profile']=='II')
    assert profile['matrices'] == [mat_json(a) for a in d['matrices']]
    assert profile['cocycles'] == [[list(v) for v in d['q']]]
    group = check_coset_table(d['table'],canonical)
    boundary_words = ([('T3','sr'*3),('V','R'+'sr'+'r'),('H','sRs')]
                      if n==50 else
                      [('T5','sr'*5),('B3','R'+'sr'*3+'r'),
                       ('C2','rsR'+'sr'*2+'rsR'),('H','sRs')])
    ribbon = peripheral_ribbon_certificate(d['table'],boundary_words)
    sec = section_certificate(d['matrices'],d['q'],d['z'],d['ii'],d['height'])
    fibers = [{'type':t,'A':mat_json(a)} for t,a in zip(d['types'],d['matrices'])]
    free,torsion = engine.section_generators(fibers)
    assert free == [[list(v) for v in d['q']]] and torsion == []
    assert engine.cocycle_pairing(fibers,d['q'],d['q']) == d['height']
    certificate['models'][n] = {'types':d['types'],
      'canonical_matrices':[mat_json(a) for a in canonical],
      'simultaneous_conjugator':mat_json(d['conjugator']),
      'archived_matrices':[mat_json(a) for a in d['matrices']],
      'modular_curve':group,'based_peripheral_marking':ribbon,'section':sec,
      'archived_engine_agrees':True}
certificate['models'][50]['Weierstrass'] = polynomial_50()

def encode(x):
    if isinstance(x,Q):
        return str(x)
    raise TypeError(type(x).__name__)

dest = OUT/'modular_collision_realizations.json'
dest.write_text(json.dumps(certificate,default=encode,indent=2)+'\n')
for n,d in certificate['models'].items():
    g = d['modular_curve']
    print(f'{n}/II: index {g["index"]}, genus 0, cusp widths {[len(c) for c in g["cusp_cycles"]]}; '
          f'{len(g["schreier_membership_witnesses"])} Schreier generators certified; '
          f'primitive cocycle, no torsion, height {d["section"]["height"]}; archived data agree.')
    print('  Actual punctured-surface peripheral words:',d['based_peripheral_marking']['boundary_words_in_free_generators'])
print('50/II: c4^3-c6^2=1728*Delta exactly; local valuations (2,3,7),(1,1,2),(0,0,3).')
print('All exact assertions passed.')
print('Certificate SHA256:',hashlib.sha256(dest.read_bytes()).hexdigest())
