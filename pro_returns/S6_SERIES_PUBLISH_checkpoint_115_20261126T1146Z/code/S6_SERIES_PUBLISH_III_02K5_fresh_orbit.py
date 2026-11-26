"""Fresh integral orbit certificate from the safe final-II monodromy data.

No Paper III proof, previous proof outcome or existing orbit program is read.
Integer matrix identities prove the two-parameter family for every modulus;
the finite enumerations are supplementary checks of those identities only.
"""
from datetime import datetime, timezone
from pathlib import Path
import json


def mul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def add(a, b):
    return [[x + y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def scale(c, a):
    return [[c * x for x in row] for row in a]


def power(a, k):
    result = [[int(i == j) for j in range(len(a))] for i in range(len(a))]
    for _ in range(k):
        result = mul(result, a)
    return result


def calculate():
    identity = [[int(i == j) for j in range(4)] for i in range(4)]
    zero = [[0] * 4 for _ in range(4)]
    a1 = [[1, 0, 0, 0], [6, 0, 1, 0], [-6, -1, -1, 0], [-2, 1, 0, 1]]
    a2 = [[1, 0, 0, 0], [0, 0, -1, 0], [-6, 1, 0, 0], [3, 0, 1, 1]]
    assert power(a1, 3) == power(a2, 4) == identity
    u = mul(power(a2, 3), power(a1, 2))
    assert mul(mul(a1, a2), u) == mul(u, mul(a1, a2)) == identity
    v = mul(mul(power(a2, 2), u), power(a2, 2))
    m, k = add(u, scale(-1, identity)), add(v, scale(-1, identity))
    assert mul(m, m) == mul(k, k) == mul(m, k) == mul(k, m) == zero
    expected_m = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 0, 0], [-1, 0, 0, 0]]
    expected_k = [[0, 0, 0, 0], [0, 0, 0, 0], [-6, 1, 0, 0], [5, -1, 0, 0]]
    assert m == expected_m and k == expected_k

    # Nilpotence and the vanishing products above prove this identity for
    # all integers r,s, including negative powers via I-rM and I-sK.
    family = lambda r, s: add(identity, add(scale(r, m), scale(s, k)))
    for r, s in [(-17, 23), (0, 0), (1, 0), (0, 1), (37, -11)]:
        matrix = family(r, s)
        assert mul(matrix, family(-r, -s)) == identity
        assert matrix == [[1, 0, 0, 0], [0, 1, 0, 0],
                          [-6*s, r+s, 1, 0], [-r+5*s, -s, 0, 1]]
    counts = {}
    for n in range(1, 65):
        graphs = set()
        for r in range(n):
            for s in range(n):
                graph = ((-6*s) % n, (r+s) % n, (-r+5*s) % n, (-s) % n)
                recovered_s = (-graph[3]) % n
                recovered_r = (graph[1] - recovered_s) % n
                assert (recovered_r, recovered_s) == (r, s)
                graphs.add(graph)
        assert len(graphs) == n*n
        counts[n] = len(graphs)
    return dict(
        target='02K5 / maps:src:C.1.4',
        input_scope='Safe statement-only local Kummer lattice and final-II P309 monodromy; no target proof or previous result read.',
        basis=['hat_gamma', 'hat_u', 'hat_w', 'hat_delta'],
        A1=a1, A2=a2, U=u, V=v, M=m, K=k,
        group_words={'U': '(A1*A2)^(-1)=A2^3*A1^2', 'V': 'A2^2*U*A2^(-2)=A2^2*U*A2^2'},
        universal_integer_certificate='M^2=K^2=MK=KM=0; U^r V^s=I+rM+sK for all integers r,s; inverse is I-rM-sK.',
        graph_matrix=[['-6s', 'r+s'], ['-r+5s', '-s']],
        inverse_parameter_map={'s': '-B22 mod N', 'r': 'B12+B22 mod N'},
        orbit_lower_bound='N^2 for every positive integer N, by the exact inverse parameter map over Z/NZ.',
        supplemental_enumeration_counts=counts,
        limitation='The global Stein-base and monodromy component argument is proved in the accompanying written derivation; finite enumeration alone supplies no all-N proof.',
    )


if __name__ == '__main__':
    result = calculate()
    result['completed_utc'] = datetime.now(timezone.utc).isoformat()
    result['attribution'] = 'GPT-6 Astra (OpenAI), ChatGPT Pro mode; numerical reasoning effort not separately exposed; fourth continuation, root fresh orbit check'
    out = Path(__file__).resolve().parents[1] / 'agents/continuation4_iii_root/S6_SERIES_PUBLISH_III_02K5_fresh_orbit.json'
    out.write_text(json.dumps(result, indent=2) + '\n', newline='\n')
    print('Exact integer identities and inverse graph-parameter map verified.')
    print('Supplementary moduli 1 through 64: each family has exactly N^2 distinct graphs.')
    print('Global finite-extension argument is in the written fresh derivation.')
    print(out)
