\\ Exact finite local heights from multiplication into the identity component.
default(realprecision,80);
default(parisizemax,2000000000);
default(datadir,"/workspace/scratch/552e69abcf1e/.apt/runtime/usr/share/pari");
J=[8000,54000,287496,16581375,-3375,-32768,-884736,-12288000,-884736000,-147197952000,-262537412640768000];
psi(E,P,n)={my(x=P[1],y=P[2],m); if(n==0,return(0)); if(n==1,return(1)); if(n==2,return(2*y+E.a1*x+E.a3)); if(n==3,return(3*x^4+E.b2*x^3+3*E.b4*x^2+3*E.b6*x+E.b8)); if(n==4,return(psi(E,P,2)*(2*x^6+E.b2*x^5+5*E.b4*x^4+10*E.b6*x^3+10*E.b8*x^2+(E.b2*E.b8-E.b4*E.b6)*x+E.b4*E.b8-E.b6^2))); if(n%2,m=(n-1)/2;return(psi(E,P,m+2)*psi(E,P,m)^3-psi(E,P,m-1)*psi(E,P,m+1)^3)); m=n/2;return(psi(E,P,m)/psi(E,P,2)*(psi(E,P,m+2)*psi(E,P,m-1)^2-psi(E,P,m-2)*psi(E,P,m+1)^2))};
identity(E,P,p)={if(#P==1,return(1)); if(valuation(P[1],p)<0,return(1)); return(valuation(2*P[2]+E.a1*P[1]+E.a3,p)==0 || valuation(3*P[1]^2+2*E.a2*P[1]+E.a4-E.a1*P[2],p)==0)};
for(k=1,#J,{
  j=J[k]; t=j/1728; E=ellinit([0,0,0,-3/4*t^3*(t-1),1/4*t^4*(t-1)^2]);
  P=[0,t^2*(t-1)/2]; M=ellminimalmodel(E,&v); Q=ellchangepoint(P,v);
  print("INDEX ",k," j ",j," model ",M[1..5]," P ",Q);
  ps=abs(factor(M.disc)[,1]); S=0;
  for(i=1,#ps,{
    p=ps[i]; if(p>1,{
      m=1; while(!identity(M,ellmul(M,Q,m),p),m++;if(m>12,error("component order not <=12")));
      R=ellmul(M,Q,m); valpsi=valuation(psi(M,Q,m),p);
      c=valuation(M.disc,p)/12+(max(0,-valuation(R[1],p))/2-valpsi)/m^2;
      print("p ",p," localred ",elllocalred(M,p)," component_order ",m," vpsi ",valpsi," vxmP ",valuation(R[1],p)," lambda/logp ",c);
      S+=c*log(p);
    })
  });
  ht=ellheight(M,Q)/2;
  print("finite_sum ",S," height_O ",ht," logN_from_height ",S-ht," N ",exp(S-ht));
  print("D ",6/Pi*(S-ht-log(2*sqrt(3))));
  print();
});
quit;
