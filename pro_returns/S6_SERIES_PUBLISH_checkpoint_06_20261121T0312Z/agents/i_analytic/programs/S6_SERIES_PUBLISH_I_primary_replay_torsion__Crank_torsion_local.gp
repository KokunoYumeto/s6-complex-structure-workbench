\\ Exact minimal models and finite local heights at the order-four/six fibres.
default(realprecision,100);
default(parisizemax,1000000000);
psieval(E,P,n)={my(x=P[1],y=P[2],m); if(n==0,return(0)); if(n==1,return(1)); if(n==2,return(2*y+E.a1*x+E.a3)); if(n==3,return(3*x^4+E.b2*x^3+3*E.b4*x^2+3*E.b6*x+E.b8)); if(n==4,return(psieval(E,P,2)*(2*x^6+E.b2*x^5+5*E.b4*x^4+10*E.b6*x^3+10*E.b8*x^2+(E.b2*E.b8-E.b4*E.b6)*x+E.b4*E.b8-E.b6^2))); if(n%2,m=(n-1)/2;return(psieval(E,P,m+2)*psieval(E,P,m)^3-psieval(E,P,m-1)*psieval(E,P,m+1)^3)); m=n/2;return(psieval(E,P,m)/psieval(E,P,2)*(psieval(E,P,m+2)*psieval(E,P,m-1)^2-psieval(E,P,m-2)*psieval(E,P,m+1)^2))};
idQ(E,P,p)={if(#P==1,return(1)); if(valuation(P[1],p)<0,return(1)); return(valuation(2*P[2]+E.a1*P[1]+E.a3,p)==0 || valuation(3*P[1]^2+2*E.a2*P[1]+E.a4-E.a1*P[2],p)==0)};
idK(E,P,K,pr)={if(#P==1,return(1)); if(idealval(K,P[1],pr)<0,return(1)); return(idealval(K,2*P[2]+E.a1*P[1]+E.a3,pr)==0 || idealval(K,3*P[1]^2+2*E.a2*P[1]+E.a4-E.a1*P[2],pr)==0)};
{
 t=32/5; E=ellinit([0,0,0,-3/4*t^3*(t-1),1/4*t^4*(t-1)^2]);
 P=[0,t^2*(t-1)/2];M=ellminimalmodel(E,&v);Q=ellchangepoint(P,v);
 print("t ",t," model ",M[1..5]," change ",v," P ",Q," torsion ",elltors(M)," rank ",ellrank(M));
 print("discriminant ",M.disc," factor ",factor(M.disc)," globalred ",ellglobalred(M));
 S=0;ps=abs(factor(M.disc)[,1]);
 for(i=1,#ps,p=ps[i];if(p>1,m=1;while(!idQ(M,ellmul(M,Q,m),p),m++);c=valuation(M.disc,p)/12-valuation(psieval(M,Q,3),p)/8;print("p ",p," localred ",elllocalred(M,p)," component_order ",m," lambda/logp ",c);S+=c*log(p)));
 print("height_O ",ellheight(M,Q)/2," finite_sum ",S," expected ",log(10)/12," N ",exp(S));
 print("analytic ",ellanalyticrank(M)," real_period ",if(M.disc>0,2,1)*real(M.omega[1]));
}
{
 K=bnfinit(z^2-3);a=Mod(z,z^2-3);
 for(sign=-1,1,if(sign!=0,
  t=(3008+sign*1728*a)/11;E=ellinit([0,0,0,-3/4*t^3*(t-1),1/4*t^4*(t-1)^2],K);
  P=[0,t^2*(t-1)/2];M=ellminimalmodel(E,&v);Q=ellchangepoint(P,v);
  print("t ",t," model ",M[1..5]," change ",v," P ",Q," order ",ellorder(M,Q));
  print("discriminant ",M.disc," idealfactor ",idealfactor(K,M.disc)," globalred ",ellglobalred(M));
  fac=idealfactor(K,M.disc);S=0;
  for(i=1,matsize(fac)[1],pr=fac[i,1];m=1;while(!idK(M,ellmul(M,Q,m),K,pr),m++);c=idealval(K,M.disc,pr)/12-idealval(K,psieval(M,Q,5),pr)/24;print("prime ",pr," e ",pr.e," f ",pr.f," localred ",elllocalred(M,pr)," component_order ",m," raw_lambda/logp ",c," normalized_lambda/logp ",c/pr.e);S+=pr.f*c*log(pr.p));
  print("finite_weighted_sum ",S," expected ",log(11)/12," height_O ",ellheight(M,Q)/2);
  print("embedding logN minus ",log(10*sqrt(3)-17)/12," plus ",log(17+10*sqrt(3))/12," sum ",log(11)/12);
  print();
 ));
}
quit;
