# Independent referee: local corner resolution candidate B.4.22

Referee: boundary_d. Date: 2026-11-15, 20:33 UTC.
Source read in full: `ab_push_corner_resolution_working.tex`.
Saved exact certificate output read: `../code/ab_push_corner_resolution.out`.
Verdict: PASS at the explicitly local scope. No global origin cap is proved.

For n=1, the q chart of Bl(u,q) gives u=qU and g=fUv; the pullback
ideal (f,g) is already principal. Its u chart gives q=uQ and fv=gQ;
the f and g charts of the second blow-up give respectively v=GQ,
g=fG and Q=Fv, f=gF. These are closures of the dense torus, not the
naive total transform with extraneous components. All three are
smooth and have the displayed product equations for r.

After q=s^n, the only remaining singular factors are uQ=s^n and
uvF=s^n. The height-one unit triangulation of n Delta_2 is unimodular
and covers the cone; its F-invertible edge is i+j=n. The identification
Q=vF matches exactly the minimal A_(n-1) resolution used on the
second chart. The second-to-first overlap has Q nonzero, where that
resolution is an isomorphism. Thus the local proper modifications
glue, and there is no unresolved fan compatibility condition.

On the third resolved chart, g is independent and F is a submersion
above F=1, so r=g(1-F) has two transverse reduced branches. Above
F=0 the other factor is a unit. The analogous second-chart product
f(G-1) and the first-chart product f(Uv-1) verify r normal crossings
everywhere. For n>1, s=0 is the reduced semistable divisor, while
the original q=s^n divisor has multiplicity n. The source's cyclic
base-change language is compatible with this; I requested that the
distinction be made explicit before any q-deck descent.

The collar comparison is exact: h=uv-q, H=h/q, Hf=r give
fuv=(f+r)q. Near H=0, putting F=(1+H)^(-1), g=f(1+H) identifies
the repaired collar with the third chart near F=1. The additional
F=0 charts are proposed local completion charts; this calculation
does not attach them to the complementary global Kato region.

The original period action remains a separate issue. The proven
first collar action is H -> aH, f -> a^(-1)f and is locally conjugated
by the product G. No identity with the full second period, no proper
global cap, no extension across all zeros of that conjugating product,
and no removal of the surviving exceptional-curve obstruction are
inferred. The conditional Mobius formula is explicitly conditional
on a test coordinate, not an asserted marked-period obstruction.
