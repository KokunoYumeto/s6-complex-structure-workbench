include("fourfolds_integral_conjugacy.jl")
using .FourfoldsIntegralConjugacy
using Hecke
using TOML
data=TOML.parsefile("records/fourfolds_conjugacy_actual_inputs.toml")
readmatrix(a)=matrix(ZZ,[[parse(BigInt,x) for x in row] for row in a])
tuples=[readmatrix.(a) for a in data["tuples"]]
P=identity_matrix(QQ,6)
for (i,j,a) in ((1,4,17),(2,6,-19),(6,3,7),(4,2,-11),(3,1,5))
    E=identity_matrix(QQ,6);E[i,j]=a;global P=E*P
end
records=Dict{String,Any}[]
for (j,As) in enumerate(tuples)
    Bs=[P*change_base_ring(QQ,A)*inv(P) for A in As]
    println("ACTUAL POSITIVE PARAMETER ",j-1);flush(stdout)
    ok,T,cert=simultaneously_conjugate(As,Bs)
    @assert ok && abs(det(T))==1
    cert["parameter"]=j-1
    cert["test"]="known unimodular conjugate"
    push!(records,cert)
    println(cert);flush(stdout)
end
for i in 1:3,j in i+1:3
    println("ACTUAL DISTINCT PARAMETERS ",i-1,",",j-1);flush(stdout)
    ok,T,cert=simultaneously_conjugate(tuples[i],tuples[j])
    @assert tr(tuples[i][1]*tuples[i][2]^3)!=tr(tuples[j][1]*tuples[j][2]^3)
    # The different word traces independently certify the negative cases.
    @assert !ok
    cert["parameters"]=[i-1,j-1]
    cert["test"]="distinct actual tuples"
    push!(records,cert)
    println(cert);flush(stdout)
end
open("records/fourfolds_conjugacy_actual_tests.toml","w") do io
    TOML.print(io,Dict("tests"=>records,"all_passed"=>true);sorted=true)
end
println("ALL SIX ACTUAL ADMISSIBLE TUPLE CONJUGACY TESTS PASSED")
