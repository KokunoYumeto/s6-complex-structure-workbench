using Hecke
Q=QQ
N=zero_matrix(Q,6,6)
for i in 1:3; N[i,i+3]=1; end
U=identity_matrix(Q,6)+N
O=Hecke._basis_of_integral_commutator_algebra([U],[U])
E=matrix_algebra(Q,O;is_basis=true)
J=radical(E)
B,p=quo(E,J)
println("centralizer dimension=",dim(E)," radical dimension=",dim(J)," quotient=",dim(B))
for (C,inc) in decompose(B)
    println("component dimension=",dim(C)," commutative=",is_commutative(C))
end
Z,incZ=center(B)
for (K,f) in Hecke._as_number_fields(Z)
    println("center field degree=",degree(K))
    println("class group certified=",class_group(maximal_order(K);GRH=false)[1])
    println("unit group certified=",unit_group(maximal_order(K);GRH=false)[1])
end
println("PROBE PASSED")
