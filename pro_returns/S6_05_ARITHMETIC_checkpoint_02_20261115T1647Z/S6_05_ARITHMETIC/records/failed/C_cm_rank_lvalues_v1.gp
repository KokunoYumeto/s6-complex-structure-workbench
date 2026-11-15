\\ Algebraic rank bounds and analytic evidence, explicitly distinguished.
default(realprecision,65);
default(parisizemax,2000000000);
default(datadir,"/workspace/scratch/552e69abcf1e/.apt/runtime/usr/share/pari");
J=[8000,54000,287496,16581375,-3375,-32768,-884736,-12288000,-884736000,-147197952000,-262537412640768000];
for(k=1,#J,{
  j=J[k]; t=j/1728; E=ellinit([0,0,0,-3/4*t^3*(t-1),1/4*t^4*(t-1)^2]);
  P=[0,t^2*(t-1)/2]; M=ellminimalmodel(E,&v); Q=ellchangepoint(P,v);
  print("INDEX ",k," j ",j," conductor ",ellglobalred(M)[1]);
  print("rank_start");
  R=ellrank(M,1,[Q]); print("ellrank ",R);
  print("rational_real_period ",if(M.disc>0,2,1)*real(M.omega[1]));
  if(k<=10,{
    print("analytic_start"); A=ellanalyticrank(M); print("analytic_rank_and_derivative ",A);
    print("leading_derivative/real_period ",A[2]/(if(M.disc>0,2,1)*real(M.omega[1])));
    print("leading_derivative/(factorial_rank*ellbsd) ",A[2]/(factorial(A[1])*ellbsd(M)));
  });
  print();
});
quit;
