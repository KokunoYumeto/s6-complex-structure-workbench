\\ Independent exact models and Neron--Tate heights for the rational CM list.
\\ PARI's ellheight uses 2*(O); we divide by two for the prompt's (O).
default(realprecision,80);
default(parisizemax,2000000000);
J=[8000,54000,287496,16581375,-3375,-32768,-884736,-12288000,-884736000,-147197952000,-262537412640768000];
for(k=1,#J,{
  j=J[k]; t=j/1728; a=-3/4*t^3*(t-1); b=1/4*t^4*(t-1)^2;
  E=ellinit([0,0,0,a,b]); P=[0,t^2*(t-1)/2];
  M=ellminimalmodel(E,&v); Q=ellchangepoint(P,v); G=ellglobalred(M);
  print("INDEX ",k," j ",j," t ",t);
  print("model ",M[1..5]," change ",v," P_min ",Q);
  print("on_curve ",ellisoncurve(M,Q)," j_check ",M.j==j);
  print("discriminant ",M.disc," factor ",factor(M.disc));
  print("globalred ",G," torsion ",elltors(M)," rootno ",ellrootno(M));
  print("height_O ",ellheight(M,Q)/2);
  print("periods ",M.omega," area ",M.area," norm_localarch ",ellsigma(M,ellpointtoz(M,Q),1));
  
  print();
});
quit;
