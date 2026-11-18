"""Canonical representatives for every linear tuple in F.2.

The ordered(2,2) sector uses the complete finite normal form. Other inputs
use a proved finite per-input height box and the exact integral-conjugacy
decision. The latter is a completeness algorithm, not an efficiency claim;
no global entry bound or unexecuted global table is asserted.
"""
from pathlib import Path
from itertools import product
import argparse,json,subprocess,sys,tempfile,tomllib
import sympy as S
from fourfolds_survivor_test import factors
from fourfolds_involution_classes import canonical_pair

ROOT=Path(__file__).resolve().parents[1]
FREE_LINEAR_ORDERS=(1,2,3,4,5,6,8,10,12)
def matrix_rows(M):return [[int(x) for x in row] for row in M.tolist()]
def linear_order(M):
    if (M-S.eye(6)).det()!=0:return None
    for n in FREE_LINEAR_ORDERS:
        if M**n==S.eye(6):return n
    return None
def admissible(T):
    if len(T) not in (3,4) or any(M.shape!=(6,6) for M in T):return False
    if any(x.q!=1 for M in T for x in M):return False
    orders=[linear_order(M) for M in T[:-1]]
    if any(n is None for n in orders):return False
    P=S.eye(6)
    for M in T:P=P*M
    if P!=S.eye(6):return False
    N=T[-1]-S.eye(6)
    return N*N==S.zeros(6) and N.rank()==3 and factors(N)==[1,1,1]

def compare(A,B):
    if all(X==Y for X,Y in zip(A,B)):return S.eye(6)
    work=ROOT.parent/'external_cache/integral_conjugacy_runtime/tmp'
    work.mkdir(parents=True,exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='tuple-',dir=work) as name:
        src=Path(name)/'input.toml';out=Path(name)/'output.toml'
        encode=lambda T:[[[str(x) for x in row] for row in M.tolist()] for M in T]
        src.write_text('A = '+json.dumps(encode(A))+'\nB = '+json.dumps(encode(B))+'\n')
        command=[sys.executable,str(ROOT/'code/run_hecke.py'),
                 str(ROOT/'code/fourfolds_integral_conjugacy.jl'),str(src),str(out)]
        p=subprocess.run(command,capture_output=True,text=True)
        if p.returncode:raise RuntimeError(p.stdout+p.stderr)
        data=tomllib.loads(out.read_text())
        if not data['conjugate']:return None
        P=S.Matrix([[int(x) for x in row] for row in data['conjugator']])
        assert abs(P.det())==1 and all(P*X==Y*P for X,Y in zip(A,B))
        return P

def bounded_candidates(height,targets,orders):
    """Full tuple height exactly height, lexicographic row-major order.

    The recursion is deliberate: itertools.product on matrix generators
    would materialize the enormous pools before yielding one tuple.
    """
    polys=[M.charpoly().all_coeffs() for M in targets]
    traces=[int(M.trace()) for M in targets]
    def matrices(j):
        for entries in product(range(-height,height+1),repeat=36):
            if sum(entries[7*i] for i in range(6))!=traces[j]:continue
            M=S.Matrix(6,6,entries)
            if M.charpoly().all_coeffs()!=polys[j]:continue
            if M**orders[j]!=S.eye(6):continue
            yield M
    def extend(chosen,partial):
        j=len(chosen)
        if j==len(targets):
            M0=partial.inv();T=chosen+[M0]
            if max(abs(int(x)) for M in T for x in M)!=height:return
            if admissible(T):yield T
            return
        for M in matrices(j):yield from extend(chosen+[M],partial*M)
    yield from extend([],S.eye(6))

def canonical_tuple(T):
    T=[S.Matrix(M) for M in T]
    if not admissible(T):raise ValueError('Not an admissible marked F.2 linear tuple')
    orders=[linear_order(M) for M in T[:-1]]
    if len(T)==4 and 1 in orders:
        # A constant identity at its marked position is conjugacy-invariant.
        # Delete it only for the linear normalizer, then restore it.  Its
        # affine order/numerator remain part of the separate gluing datum.
        assert orders.count(1)==1
        position=orders.index(1)
        reduced=canonical_tuple(T[:position]+T[position+1:])
        representative=[S.Matrix(M) for M in reduced['representative']]
        representative.insert(position,S.eye(6))
        P=S.Matrix(reduced['conjugator'])
        assert abs(P.det())==1 and all(P*X==Y*P for X,Y in zip(T,representative))
        return {'method':'marked identity insertion / '+reduced['method'],
                'identity_site':position,'reduced_class':reduced,
                'representative':[matrix_rows(M) for M in representative],
                'conjugator':matrix_rows(P)}
    if orders==[2,2]:
        key,rep,P=canonical_pair(*T)
        return {'method':'complete involution normal form','key':list(key),
                'representative':[matrix_rows(M) for M in rep],
                'conjugator':matrix_rows(P)}
    H=max(abs(int(x)) for M in T for x in M)
    comparisons=0
    for h in range(1,H+1):
        for candidate in bounded_candidates(h,T[:-1],orders):
            comparisons+=1;P=compare(T,candidate)
            if P is not None:
                return {'method':'proved finite height box','input_height':H,
                        'representative_height':h,'comparisons':comparisons,
                        'representative':[matrix_rows(M) for M in candidate],
                        'conjugator':matrix_rows(P)}
    raise AssertionError('The supplied tuple itself must occur in its height box')

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input',type=Path)
    parser.add_argument('output',type=Path)
    args=parser.parse_args()
    data=json.loads(args.input.read_text())
    result=canonical_tuple(data['matrices'])
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(result['method'])
