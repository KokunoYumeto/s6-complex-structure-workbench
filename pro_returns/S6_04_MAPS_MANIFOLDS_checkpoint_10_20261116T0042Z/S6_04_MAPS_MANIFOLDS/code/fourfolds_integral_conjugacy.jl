"""
Exact simultaneous GL(Z) conjugacy for tuples containing a rank-half
square-zero unipotent.  P*A[i] == B[i]*P is the convention.

The semisimple centralizer is split over number fields in dimension six.
The radical reduction and principal-ideal step are Bley--Hofmann--Johnston,
Forum Math. Sigma 10 (2022), e87, Theorem 3.4 and Algorithm 8.3.
Hecke 0.41.1 is pinned.  All number-field class/unit groups used below are
certified with GRH=false before a negative ideal decision is accepted.
There is no height cutoff in this decision procedure.
"""
module FourfoldsIntegralConjugacy
using Hecke
using TOML
export simultaneously_conjugate

function integral_basis(As, Bs)
    Hecke._basis_of_integral_commutator_algebra(As, Bs)
end

function rational_isomorphism(H, n)
    isempty(H) && return nothing
    for h in H
        !iszero(det(h)) && return h
    end
    candidate = sum(H)
    !iszero(det(candidate)) && return candidate
    R, xs = polynomial_ring(QQ, ["c$i" for i in eachindex(H)])
    M = matrix(R,n,n,[sum(R(h[i,j])*xs[k] for (k,h) in enumerate(H))
                     for i in 1:n for j in 1:n])
    f = det(M)
    iszero(f) && return nothing
    cs = zeros(Int,length(H))
    # Each variable degree is at most n.  At most n of n+1 values can
    # annihilate a nonzero polynomial over the remaining fraction field.
    for i in eachindex(H)
        selected = false
        for a in 0:n
            v = [j==i ? R(a) : xs[j] for j in eachindex(H)]
            g = evaluate(f,v)
            if !iszero(g)
                f=g; cs[i]=a; selected=true; break
            end
        end
        @assert selected
    end
    P = sum(cs[i]*H[i] for i in eachindex(H))
    @assert !iszero(det(P))
    P
end

function coefficient_matrix(v)
    matrix(QQ,[coefficients(x) for x in v])
end

"Install an exact full-matrix representation of a split simple Q-algebra."
function refine_rational_matrix_component!(C)
    d=dim(C); n=isqrt(d)
    @assert n*n==d && n in (2,3)
    bas=basis(C)
    L=nothing
    function attempt(e)
        R=coefficient_matrix([b*e for b in bas])
        rr,RR=rref(R)
        rr==n ? RR[1:n,:] : nothing
    end
    for b in bas
        L=attempt(b)
        L!==nothing && break
    end
    height=0
    # A rank-one matrix exists over Q. Clearing denominators expresses it
    # as an integral combination of this basis, so these shells terminate.
    while L===nothing
        height+=1
        for cs in Iterators.product(ntuple(_->(-height:height),d)...)
            maximum(abs,cs)==height || continue
            e=sum(cs[i]*bas[i] for i in 1:d)
            L=attempt(e)
            L!==nothing && break
        end
    end
    left_basis=[C([L[i,j] for j in 1:d]) for i in 1:n]
    R,x=polynomial_ring(QQ,"x")
    K,_=number_field(x-1,"r")
    MB=matrix_algebra(K,n)
    images=elem_type(MB)[]
    for b in bas
        Y=coefficient_matrix([b*l for l in left_basis])
        ok,V=can_solve_with_solution(L,Y;side=:left)
        @assert ok
        push!(images,MB(map_entries(K,transpose(V))))
    end
    forward=matrix(K,[coefficients(z) for z in images])
    rational_forward=matrix(QQ,[[QQ(coeff(c,0)) for c in coefficients(z)]
                                for z in images])
    f=Hecke.AbsAlgAssMorGen(C,MB,forward,inv(rational_forward))
    @assert f(one(C))==one(MB)
    for a in bas,b in bas
        @assert f(a*b)==f(a)*f(b)
    end
    C.isomorphic_full_matrix_algebra=MB,f
    K
end

function certify_field!(K,certificates)
    @assert degree(K)<=3
    O=maximal_order(K)
    Cl,_=class_group(O;GRH=false)
    U,_=unit_group(O;GRH=false)
    push!(certificates,Dict("degree"=>degree(K),
                           "polynomial"=>string(defining_polynomial(K)),
                           "class_number"=>string(order(Cl)),
                           "unit_group"=>string(U),"GRH"=>false))
end

function refine_and_certify!(B,certificates)
    for (C,_) in decompose(B)
        if is_commutative(C)
            ZC,ZCtoC=Hecke._as_algebra_over_center(C)
            @assert dim(ZC)==1
            certify_field!(base_ring(ZC),certificates)
            Hecke._rewrite_algebra_which_is_center(C,ZCtoC)
            for (K,_) in Hecke._as_number_fields(C)
                certify_field!(K,certificates)
            end
        else
            certify_field!(refine_rational_matrix_component!(C),certificates)
        end
    end
    Z,_=center(B)
    for (K,_) in Hecke._as_number_fields(Z)
        certify_field!(K,certificates)
    end
    unit_group(maximal_order(Z);GRH=false)
    if is_commutative(B)
        for (K,_) in Hecke._as_number_fields(B)
            certify_field!(K,certificates)
        end
        unit_group(maximal_order(B);GRH=false)
    end
end

function simultaneously_conjugate(As0,Bs0;check_hypothesis=true)
    @assert length(As0)==length(Bs0)>0
    As=[change_base_ring(QQ,A) for A in As0]
    Bs=[change_base_ring(QQ,B) for B in Bs0]
    n=nrows(As[1]); @assert n==6
    @assert all(size(M)==(n,n) && denominator(M)==1 for M in vcat(As,Bs))
    if check_hypothesis
        @assert any(begin N=M-identity_matrix(QQ,n); rank(N)==3 && iszero(N*N) end for M in As)
    end
    cert=Dict{String,Any}("size"=>n,"tuple_length"=>length(As),
                          "field_certificates"=>Any[])
    H=integral_basis(As,Bs)
    D=rational_isomorphism(H,n)
    if D===nothing
        cert["decision"]="not rationally isomorphic"
        return false,nothing,cert
    end
    @assert all(D*As[i]==Bs[i]*D for i in eachindex(As))
    O=integral_basis(As,As)
    E=matrix_algebra(QQ,O;is_basis=true)
    J=radical(E)
    B,pi=quo(E,J)
    cert["centralizer_dimension"]=dim(E)
    cert["radical_dimension"]=dim(J)
    cert["semisimple_dimension"]=dim(B)
    refine_and_certify!(B,cert["field_certificates"])
    invD=inv(D)
    ordergens=[pi(E(o)) for o in O]
    idealgens=[pi(E(invD*h)) for h in H]
    OO=order(B,ordergens)
    OI=Hecke.ideal_from_lattice_gens(B,idealgens)
    if right_order(OI)!=OO
        cert["decision"]="projected right order differs"
        return false,nothing,cert
    end
    OI.order=OO
    ok,y=is_principal_with_data(OI,OO;side=:right)
    if !ok
        cert["decision"]="projected ideal is not principal"
        return false,nothing,cert
    end
    @assert y*OO==OI
    den=denominator(OI,OO)
    Y=matrix(ZZ,[coordinates(OO(den*z)) for z in idealgens])
    target=matrix(ZZ,[coordinates(OO(den*y))])
    lifted,v=can_solve_with_solution(Y,target;side=:left)
    @assert lifted
    P=sum(v[1,i]*H[i] for i in eachindex(H))
    @assert denominator(P)==1
    @assert all(P*As[i]==Bs[i]*P for i in eachindex(As))
    cert["lift_determinant"]=string(det(P))
    if abs(det(P))!=1
        cert["decision"]="principal quotient generator has nonunit determinant"
        return false,nothing,cert
    end
    cert["decision"]="integrally conjugate"
    true,map_entries(ZZ,P),cert
end

function main(args)
    data=TOML.parsefile(args[1])
    readmatrix(a)=matrix(ZZ,[[parse(BigInt,string(x)) for x in row] for row in a])
    As=readmatrix.(data["A"]); Bs=readmatrix.(data["B"])
    ok,P,cert=simultaneously_conjugate(As,Bs)
    cert["conjugate"]=ok
    if ok
        cert["conjugator"]=[[string(P[i,j]) for j in 1:ncols(P)] for i in 1:nrows(P)]
    end
    open(args[2],"w") do io; TOML.print(io,cert;sorted=true); end
end

if abspath(PROGRAM_FILE)==@__FILE__
    main(ARGS)
end
end
