default(parisizemax,1000000000);
J=[54000,16581375,-32768,-884736000,-147197952000];
idx=[2,4,6,9,10];D=[-23,-31,-19,-19,-3];
for(k=1,5,t=J[k]/1728;E=ellminimalmodel(ellinit([0,0,0,-3/4*t^3*(t-1),1/4*t^4*(t-1)^2]));A=ellminimalmodel(elltwist(E,D[k]));N=ellglobalred(A)[1];M=ceil(60*sqrt(N)/(2*Pi));aa=ellan(A,M);fn=Str("code/I/records/B_C6_aux_coeff_",idx[k],".dat");write(fn,N," ",M);for(n=1,M,write(fn,aa[n]));print(idx[k]," ",N," ",M));
quit;
