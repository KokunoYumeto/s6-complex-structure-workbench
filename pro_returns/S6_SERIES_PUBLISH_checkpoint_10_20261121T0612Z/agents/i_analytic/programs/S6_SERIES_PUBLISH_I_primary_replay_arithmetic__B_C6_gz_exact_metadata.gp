\\ Exact-arithmetic audit, avoiding repeated high-level Manin computations.
default(realprecision,70);
default(parisizemax,500000000);
onecase(i,j,d,D,cmD)={
 my(t=j/1728,E=ellminimalmodel(ellinit([0,0,0,-3/4*t^3*(t-1),1/4*t^4*(t-1)^2])));
 my(B=ellminimalmodel(elltwist(E,d)),A=ellminimalmodel(elltwist(E,D)));
 my(T=ellminimalmodel(elltwist(B,d)),U=ellminimalmodel(elltwist(B,d*D)));
 if(T[1..5]!=E[1..5]||U[1..5]!=A[1..5],error("exact twist identity"));
 if(E.c4!=d^2*B.c4||E.c6!=d^3*B.c6,error("target minimal differential"));
 if(A.c4!=(d*D)^2*B.c4||A.c6!=(d*D)^3*B.c6,error("auxiliary minimal differential"));
 my(N0=ellglobalred(B)[1],N=ellglobalred(A)[1],pp=factor(N0)[,1]);
 if(N!=N0*(d*D)^2||ellglobalred(E)[1]!=N0*d^2,error("exact conductors"));
 if(gcd(N0,d*D)!=1||gcd(d,D)!=1,error("coprimality"));
 for(k=1,#pp,if(kronecker(D,pp[k])!=1,error("Heegner splitting")));
 if(ellrootno(A)!=1||ellrootno(E)!=-1,error("root signs"));
 print("INDEX ",i," base ",B[1..5]," N0 ",N0," d ",d," Kdisc ",D);
 print("target ",E[1..5]," auxiliary ",A[1..5]," auxiliary_conductor ",N," torsion ",elltors(A)[1]);
 print("EXACT c4,c6 scaling identities; exact conductors; all Heegner splitting and coprimality conditions PASS");
 if(cmD>0,
  my(M=10000,aa=ellan(B,M),bb=vector(M),sturm=(cmD^2+cmD)\6);
  if(M<=sturm,error("insufficient Sturm comparison"));
  for(a=1,sqrtint(M),bb[a^2]+=kronecker(a,cmD)*a);
  for(v=1,sqrtint(4*M\cmD),forstep(u=if(v%2,1,2),sqrtint(4*M-cmD*v^2),2,my(n=(u^2+cmD*v^2)/4);bb[n]+=kronecker((cmD+1)/2*u,cmD)*u));
  if(aa!=bb,error("CM theta coefficient"));
  if(ellan(A,M)!=vector(M,n,bb[n]*kronecker(d*D,n)),error("negative twist coefficient"));
  print("CM theta and auxiliary quadratic-twist coefficients agree exactly for all n<=",M);
  print("GLOBAL IDENTIFICATION: weight 2, level ",cmD^2,", trivial character; valence/Sturm bound ",sturm," < ",M);
 );
};
onecase(2,54000,-11,-23,0);
onecase(4,16581375,57,-31,0);
onecase(6,-32768,21,-19,11);
onecase(9,-884736000,21,-19,43);
onecase(10,-147197952000,217,-3,67);
onecase(11,-262537412640768000,185801,-3,163);
print("PASS: SIX EXACT GROSS--ZAGIER INPUT RECORDS AND FOUR CM THETA COEFFICIENT AUDITS.");
quit;
