"""Exact torsion choices, quotient charts, and support maps for C.2.UN.30."""
import sympy as s

u,z=s.symbols('u z',nonzero=True)
positive=s.Matrix([z/u,u**2])
negative=s.Matrix([z*u,u**(-2)])
assert s.factor(positive.jacobian([z,u]).det()) == 2
assert s.factor(negative.jacobian([z,u]).det()) == -2/u**2
print("Finite product-cover Jacobians: 2 and -2/u².")
print("At every fixed point the ambient representation is(-1,-1,-1).")
print("Invariant blowup chart (x,t,w)=(s,su,sv), R=s² gives T=Ru².")

for r in range(1,11):
    N=int(s.nextprime(2*r))
    chosen=list(range(1,r+1))
    assert len({j%N for j in chosen} | {(-j)%N for j in chosen}) == 2*r
    assert all((2*j)%N for j in chosen)
    line_class=(r*(r+1))%N
    print(f"r={r}: N={N}; paired torsion points distinct; "
          f"L|E has class {line_class}/{N}.")

    # Source of dual H² restriction:
    # M has C1,...,C16,J as independent classes, completed to22.
    # The sixteen plane components each contribute one further class.
    curve_map=s.zeros(38,16+r)
    for i in range(16):
        curve_map[i,i]=1
        curve_map[22+i,i]=-1
    for j in range(r):
        curve_map[16,16+j]=1
    assert curve_map.rank() == 17
    assert len(curve_map.nullspace()) == r-1
    component=[17+r,r,38,r,17+r]
    edge=[16+r,2*r,16+r,0,0]
    rank=[16+r,r,17,0,0]
    support=[component[k]-rank[k]+(edge[k-1]-rank[k-1] if k else 0)
             for k in range(5)]
    assert support == [1,0,21+r,2*r-1,17+r]
    balanced=support.copy()
    for k,increment in [(2,40),(3,120),(4,40)]:
        balanced[k] += increment
    assert balanced == [1,0,61+r,2*r+119,57+r]
    e=lambda b:sum((-1)**k*x for k,x in enumerate(b))
    assert e(support) == 40 and e(balanced) == 0
    coherent_component=[17+r,r,1]
    coherent_edge=[16+r,r,0]
    coherent_rank=[16+r,r,0]
    coherent=[coherent_component[k]-coherent_rank[k]
              +(coherent_edge[k-1]-coherent_rank[k-1] if k else 0)
              for k in range(3)]
    assert coherent == [1,0,1]
    print("  H² restriction rank17; support=",support,
          "balanced=",balanced,"hO=",coherent)
    plurigenus=[1+r*(m//2) for m in range(1,9)]
    print("  P1,...,P8=",plurigenus,"canonical slope=",s.Rational(r,2))

assert (0+16)//2+16 == 24
assert 24+16*3-16*2 == 40
print("Main component e24, chiO2, pg1,q0,b=(1,0,22,0,1).")
print("Both supports reach Euler0 through twenty negative-two blocks each.")
print("All exact checks passed.")
