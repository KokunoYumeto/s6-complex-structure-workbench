include("fourfolds_integral_conjugacy.jl")
using .FourfoldsIntegralConjugacy
using Hecke
using TOML

function blockdiag(A,B)
    vcat(hcat(A,zero_matrix(QQ,nrows(A),ncols(B))),
         hcat(zero_matrix(QQ,nrows(B),ncols(A)),B))
end
I6=identity_matrix(QQ,6)
N=zero_matrix(QQ,6,6)
for i in 1:3;N[i,i+3]=1;end
U=I6+N
P=deepcopy(I6)
for (i,j,a) in ((1,4,17),(2,6,-19),(6,3,7),(4,2,-11),(3,1,5))
    E=deepcopy(I6);E[i,j]=a;global P=E*P
end
@assert det(P)==1
results=Dict{String,Any}[]
function run_case(name,As,Bs,expected)
    println("CASE ",name);flush(stdout)
    ok,T,cert=simultaneously_conjugate(As,Bs)
    @assert ok==expected
    if ok
        @assert abs(det(T))==1
        @assert all(T*As[i]==Bs[i]*T for i in eachindex(As))
    end
    cert["name"]=name;cert["expected"]=expected
    push!(results,cert)
    println(cert);flush(stdout)
end

run_case("full_Mat3_semisimple_quotient",[U],[P*U*inv(P)],true)
D=diagonal_matrix(QQ,[1,-1,1])
A=blockdiag(D,D)
run_case("Mat2_times_Q_positive",[U,A],[P*U*inv(P),P*A*inv(P)],true)
A2=deepcopy(A);A2[1,5]=1
@assert A*A==I6 && A2*A2==I6
run_case("radical_lift_obstruction",[U,A],[U,A2],false)
D2=diagonal_matrix(QQ,[1,-1,-1])
run_case("rational_multiplicity_obstruction",[U,A],[U,blockdiag(D2,D2)],false)
C=matrix(QQ,[0 -5;1 0]);J=matrix(QQ,[2 1;0 1])
C3=blockdiag(C,matrix(QQ,1,1,[3]))
J3=blockdiag(J,matrix(QQ,1,1,[1]))
AA=blockdiag(C3,C3);JJ=blockdiag(J3,J3)
BB=inv(JJ)*AA*JJ
@assert denominator(BB)==1
run_case("nonprincipal_ideal_Qsqrt_minus5",[U,AA],[U,BB],false)
Cubic=matrix(QQ,[0 0 1;1 0 1;0 1 0])
AC=blockdiag(Cubic,Cubic)
run_case("cubic_center_certified_positive",[U,AC],[P*U*inv(P),P*AC*inv(P)],true)
open("records/fourfolds_integral_conjugacy_tests.toml","w") do io
    TOML.print(io,Dict("tests"=>results,"all_passed"=>true);sorted=true)
end
println("ALL SIX EXACT SIMULTANEOUS CONJUGACY TESTS PASSED")
