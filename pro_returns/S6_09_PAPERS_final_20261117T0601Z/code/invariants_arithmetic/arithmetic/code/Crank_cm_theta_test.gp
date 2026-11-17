\\ Exact coefficient comparisons for the -163 CM theta-series.
default(realprecision,60);
E=ellinit([0,0,1,-2174420,1234136692]);
M=ellinit([0,0,1,-75065352465446420,7916029533155605844266842]);
d=185801;
print("base_model ",E[1..5]," conductor ",ellglobalred(E)[1]," j ",E.j);
print("twist ",d," target_j ",M.j," conductor ",ellglobalred(M)[1]);
A=ellan(E,10000); B=vector(10000);
for(a=1,100,B[a^2]+=kronecker(a,163)*a);
for(v=1,sqrtint(4*10000\163),forstep(u=if(v%2,1,2),sqrtint(40000-163*v^2),2,n=(u^2+163*v^2)/4;B[n]+=kronecker(82*u,163)*u));
print("base_theta_equals_coefficients ",A==B);
if(A!=B,for(n=1,#A,if(A[n]!=B[n],print("MISMATCH ",n," ",A[n]," ",B[n]))));
C=ellan(M,10000);D=vector(10000,n,B[n]*kronecker(d,n));
print("twist_theta_equals_coefficients ",C==D);
if(C!=D,for(n=1,#C,if(C[n]!=D[n],print("TWIST_MISMATCH ",n," ",C[n]," ",D[n]))));
print("base ",A[1..100]);
print("twist ",C[1..100]);
quit;
