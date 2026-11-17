\\ Exact coefficients for independent, explicitly truncated L-derivatives.
default(realprecision,80);
default(parisizemax,500000000);
J=[8000,54000,287496,16581375,-3375,-32768,-884736,-12288000,-884736000,-147197952000];
for(k=1,#J,t=J[k]/1728;E=ellminimalmodel(ellinit([0,0,0,-3/4*t^3*(t-1),1/4*t^4*(t-1)^2]));N=ellglobalred(E)[1];r=if(k==1||k==8,2,1);B=ceil(180*sqrt(N)/(2*Pi));A=ellan(E,B);fn=Str("/workspace/scratch/037cd144174c/deliverables/code/invariants_arithmetic/arithmetic/records/Crank_coeff_",k,".dat");write(fn,N," ",r," ",B);for(n=1,B,write(fn,A[n]));print("index ",k," j ",J[k]," conductor ",N," root_number ",ellrootno(E)," coefficient_cutoff ",B," file ",fn));
quit;
