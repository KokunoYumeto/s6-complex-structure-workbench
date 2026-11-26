#!/usr/bin/env python3
"""Post-release LG count and marked-site comparison; no historical main is run.

Reads the complete saved JSON bytes and checks every count/row/choice field.
It does not recheck the geometric cap matrices or their historical executions.
"""
from ast import literal_eval
from collections import Counter
from datetime import datetime, timezone
from fractions import Fraction
from hashlib import sha1, sha256
from itertools import product
from math import gcd, lcm
from pathlib import Path
import json
import re

W = Path(__file__).resolve().parents[1]
CACHE = W / 'agents/continuation8_iii_lg_receiving/history_counts/source_cache'
GOOD = {'II': (6, 1), 'III': (4, 2), 'IV': (3, 3),
        'III*': (4, 2), 'IV*': (3, 3)}


def key(r):
    return r['entry'], r['profile'], r['a'], r['b'], r['zero_index']


def keytext(k):
    return '/'.join(map(str, k))


def parsekey(t):
    a = t.split('/')
    return int(a[0]), a[1], int(a[2]), int(a[3]), int(a[4])


def mult(f):
    m = re.fullmatch(r'I(\d+)', f)
    return int(m[1]) if m else 0


def subsets(ids):
    return [tuple(i for i, bit in zip(ids, bits) if bit)
            for bits in product((0, 1), repeat=len(ids))]


def h(comp):
    return lcm(*(m // gcd(m, row[0])
                 for m, row in zip(comp['moduli'], comp['rows'])))


def additive_key(p):
    return key(p), tuple(p['finite_indices'])


def full_key(p):
    return (*additive_key(p), tuple(i for i, c in p['multiplicative_choices']
                                  if c == 'original'))


def main():
    print('START', datetime.now(timezone.utc).isoformat())
    source = Path(__file__)
    print('SOURCE', source.name, len(source.read_bytes().splitlines()),
          sha256(source.read_bytes()).hexdigest())
    saved = {}
    for name in ['manifolds_sphere_natural.json', 'manifolds_original_chern.json',
                 'manifolds_original_zero_degree.json',
                 'manifolds_original_multiplicative.json',
                 'manifolds_nonstar_sphere_patterns.json']:
        data = (CACHE / name).read_bytes()
        saved[name] = json.loads(data)
        git = sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()
        print('SAVED_INPUT', name, len(data), sha256(data).hexdigest(), 'git', git)
    rawpath = W / 'agents/continuation6_iii_d2/S6_SERIES_PUBLISH_III_02KY_raw_profiles.json'
    raw = json.loads(rawpath.read_text())
    profiles = {(p['OS'], p['profile']): p for p in raw['rows']}
    outpath = W / 'code/S6_SERIES_PUBLISH_c7_lg_catalogue_v001.out'
    output = outpath.read_text().splitlines()
    print('FRESH_OUTPUT', len(output), sha256(outpath.read_bytes()).hexdigest())
    rows, fresh, minimal = {}, {}, {}
    for line in output:
        if line.startswith('NATURAL '):
            m = re.fullmatch(r'NATURAL (\S+) nu_kappa (-?\d+) (-?\d+) d0 (\d+) finite_sites (.*?) nonzero_mult_sites (.*)', line)
            k = parsekey(m[1])
            rows[k] = dict(n=int(m[2]), kappa=int(m[3]), d0=int(m[4]),
                           good=literal_eval(m[5]), nonzero=literal_eval(m[6]))
        elif line.startswith('PATTERN495 '):
            m = re.fullmatch(r'PATTERN495 (\d+) (\S+) F (.*?) O_mult (.*)', line)
            p = parsekey(m[2]), literal_eval(m[3]), literal_eval(m[4])
            assert p not in fresh
            fresh[p] = int(m[1])
        elif line.startswith('MINIMAL162 '):
            m = re.match(r'MINIMAL162 (\d+) (\S+) F (.*?) c (\d+) ', line)
            minimal[parsekey(m[2]), literal_eval(m[3])] = int(m[4])
    natural = saved['manifolds_sphere_natural.json']['candidates']
    assert len(natural) == len(rows) == 172
    assert len({key(p) for p in natural}) == 172 and {key(p) for p in natural} == set(rows)
    for p in natural:
        k = key(p); r = rows[k]; prof = profiles[k[:2]]; z = k[4]
        assert p['zero_components'] == [0]
        assert p['zero_type'] == prof['fibers'][z] and p['n'] == r['n'] == mult(prof['fibers'][z])
        assert k[2] * k[3] == r['d0'] // r['n']
        assert r['d0'] == Fraction(prof['height_of_generator']).denominator
        assert r['good'] == [i for i, f in enumerate(prof['fibers']) if f in GOOD]
        assert r['nonzero'] == [i for i, f in enumerate(prof['fibers'])
                                if mult(f) and i != z and k[2] % h(prof['component_coordinates'][i])]
    expected_add = {(k, f) for k, r in rows.items() for f in subsets(r['good'])}
    expected_full = {(k, f, o) for k, r in rows.items()
                     for f in subsets(r['good']) for o in subsets(r['nonzero'])}
    add = saved['manifolds_original_chern.json']['patterns']
    oldadd = {additive_key(p): p for p in add}
    assert len(add) == len(oldadd) == 282 and set(oldadd) == expected_add
    for p in add:
        k, f = additive_key(p); prof = profiles[k[:2]]
        inverse = [[i, 'log' if i in f else 'original']
                   for i, typ in enumerate(prof['fibers']) if not mult(typ)]
        assert p['additive_choices'] == inverse
        assert p['nonzero_chern_count'] == sum(k[2] % h(prof['component_coordinates'][i]) != 0
                                               for i, c in inverse if c == 'original')
    zero = saved['manifolds_original_zero_degree.json']['patterns']
    expected_zero = {k for k, p in oldadd.items() if p['nonzero_chern_count'] == 0}
    assert len(zero) == 228 and {additive_key(p) for p in zero} == expected_zero
    assert len({key(p) for p in zero}) == 160 and sum(p['defect'] > 0 for p in zero) == 30
    assert sum(p['nonzero_chern_count'] > 0 for p in add) == 54
    old = saved['manifolds_original_multiplicative.json']['patterns']
    oldfull = {full_key(p): p for p in old}
    assert len(old) == len(oldfull) == len(fresh) == 495
    assert set(oldfull) == expected_full == set(fresh)
    representatives = 0
    for p in old:
        k, f, o = full_key(p); r = rows[k]; prof = profiles[k[:2]]
        assert p['additive_choices'] == oldadd[k, f]['additive_choices']
        assert p['multiplicative_choices'] == [[i, 'original' if i in o else 'mumford'] for i in r['nonzero']]
        equiv = [i for i, typ in enumerate(prof['fibers'])
                 if mult(typ) and i != k[4] and i not in r['nonzero']]
        assert p['homology_equivalent_zero_degree_choices'] == equiv
        assert p['nonzero_chern_count'] == oldadd[k, f]['nonzero_chern_count'] + len(o)
        representatives += 2 ** len(equiv)
    cert = saved['manifolds_original_multiplicative.json']['local']
    assert len(cert) == 120
    assert {(key(p), p['site']) for p in cert} == {(k, i) for k, r in rows.items() for i in r['nonzero']}
    for p in cert:
        assert p['type'] == profiles[key(p)[:2]]['fibers'][p['site']]
        assert p['n'] == mult(p['type']) and p['fibre_relation'] == p['b'] // p['n']
    assert representatives == 1728
    compatible = saved['manifolds_nonstar_sphere_patterns.json']['all_patterns']
    spheres = saved['manifolds_nonstar_sphere_patterns.json']['sphere_patterns']
    assert len(compatible) == 164
    admissible = {additive_key(p): p['residual_c'] for p in compatible if not p['orbifold_obstruction']}
    assert admissible == minimal and len(minimal) == 162
    sphere_set = {additive_key(p) for p in spheres}
    assert len(spheres) == 59 and sphere_set == {k for k, c in minimal.items() if c == 1}
    assert len({k[0] for k in sphere_set}) == 50
    def retract(p):
        k, f, o = p
        return k, tuple(i for i in f if profiles[k[:2]]['fibers'][i] not in ('III*', 'IV*')), o
    small = {p for p in fresh if retract(p) == p}
    difference = set(fresh) - small
    assert len(small) == 459 and len(difference) == 36
    assert {retract(p) for p in fresh} == small
    assert all(retract(p) == p for p in small)
    assert all(sum(retract(q) == p for q in fresh) in (1, 2) for p in small)
    print('MATCH natural172 additive282 zero_additive228_on160 nonzero_additive54 positive_defect30 full495 local_mult120 representative_expansion1728')
    print('MATCH compatible164 minimal162 spheres59_on50; all historical/fresh marked tuples and inverse choice lists agree')
    print('PROFILE_COLUMNS OS/profile natural additive full all_stars_original difference sphere')
    for pr in profiles:
        count = lambda entries: sum(p[0][:2] == pr for p in entries)
        nr = sum(k[:2] == pr for k in rows)
        print('PROFILE', keytext(pr), nr, count(expected_add), count(fresh), count(small), count(difference), count(sphere_set))
    print('DIFFERENCE_COLUMNS fresh495_id OS/profile/a/b/zero finite_sites original_mult_sites retracted_fresh495_id')
    for p in sorted(difference, key=fresh.get):
        print('DIFFERENCE', fresh[p], keytext(p[0]), p[1], p[2], fresh[retract(p)])
    print('EXCLUDED_COMPATIBLE', [(keytext(key(p)), p['finite_indices']) for p in compatible if p['orbifold_obstruction']])
    print('END', datetime.now(timezone.utc).isoformat(), 'ALL_COUNT_AND_INVERSE_MAP_ASSERTIONS_PASSED')


if __name__ == '__main__':
    main()
