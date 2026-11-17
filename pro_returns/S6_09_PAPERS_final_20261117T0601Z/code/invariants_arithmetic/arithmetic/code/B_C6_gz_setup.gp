\\ Exact base twists and auxiliary central coefficients for the GZ certificate.
default(realprecision,85);
default(parisizemax,1000000000);
default(datadir,"/workspace/scratch/552e69abcf1e/.apt/runtime/usr/share/pari");
idx=[2,4,6,9,10,11];
jj=[54000,16581375,-32768,-884736000,-147197952000,-262537412640768000];
dd=[-11,57,21,21,217,185801];
kk=[-23,-31,-19,-19,-3,-3];
for(k=1,6,t=jj[k]/1728;E=ellminimalmodel(ellinit([0,0,0,-3/4*t^3*(t-1),1/4*t^4*(t-1)^2]));B=ellminimalmodel(elltwist(E,dd[k]));A=ellminimalmodel(elltwist(E,kk[k]));T=ellminimalmodel(elltwist(B,dd[k]));U=ellminimalmodel(elltwist(B,dd[k]*kk[k]));if(T[1..5]!=E[1..5]||U[1..5]!=A[1..5],error("exact twist identity"));c1=sqrt(sqrt(dd[k]^2*B.c4/E.c4));c2=sqrt(sqrt((dd[k]*kk[k])^2*B.c4/A.c4));if(c1!=1||c2!=1,error("nontrivial twist differential scaling"));N0=ellglobalred(B)[1];N=ellglobalred(A)[1];if(N!=N0*(dd[k]*kk[k])^2,error("twist level"));if(gcd(N0,dd[k]*kk[k])!=1,error("noncoprime parameters"));P=factor(N0)[,1];for(j=1,#P,if(kronecker(kk[k],P[j])!=1,error("Heegner splitting")));if(ellrootno(A)!=1,error("auxiliary root sign"));print("INDEX ",idx[k]," base ",B[1..5]," label ",ellidentify(B)[1][1]," N0 ",N0," d ",dd[k]," Kdisc ",kk[k]);print("base_Manin ",ellmaninconstant(B)," twist_minimal_scalings ",[c1,c2]);print("target ",E[1..5]," auxiliary ",A[1..5]," aux_N ",N," aux_torsion ",elltors(A)[1]);print("aux_period ",if(A.disc>0,2,1)*real(A.omega[1])," target_period ",if(E.disc>0,2,1)*real(E.omega[1]));if(k<=5,M=ceil(60*sqrt(N)/(2*Pi));aa=ellan(A,M);fn=Str("S6_05_ARITHMETIC/records/B_C6_aux_coeff_",idx[k],".dat");write(fn,N," ",M);for(n=1,M,write(fn,aa[n]));print("aux_L_numerical ",lfun(A,1)," coefficient_file ",fn," M ",M));print());
quit;
