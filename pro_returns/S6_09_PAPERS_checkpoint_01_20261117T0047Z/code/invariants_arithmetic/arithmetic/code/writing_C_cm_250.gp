\\ High precision independent global heights and periods for theta comparison.
default(realprecision,270);
default(parisizemax,500000000);
J=[8000,54000,287496,16581375,-3375,-32768,-884736,-12288000,-884736000,-147197952000,-262537412640768000];
for(k=1,#J,{
 j=J[k];t=j/1728;E=ellinit([0,0,0,-3/4*t^3*(t-1),1/4*t^4*(t-1)^2]);P=[0,t^2*(t-1)/2];
 M=ellminimalmodel(E,&v);Q=ellchangepoint(P,v);
 print(j,"|",ellheight(M,Q)/2,"|",real(M.omega[1]),"|",abs(imag(M.omega[2])));
});
quit;
