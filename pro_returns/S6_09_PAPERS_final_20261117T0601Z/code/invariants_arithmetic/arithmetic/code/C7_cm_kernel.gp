default(realprecision,100);
E=ellinit([0,0,1,-38,90]);
print("periods_and_quasiperiods=",ellperiods(E,1));
print("Q_log=",ellpointtoz(E,[4,-2]));
dp=elldivpol(E,19);
print("division_polynomial_degree=",poldegree(dp));
fac=factor(dp);
for(i=1,matsize(fac)[1], print("factor_degree=",poldegree(fac[i,1])," multiplicity=",fac[i,2]); if(poldegree(fac[i,1])<20,print("factor=",fac[i,1])));
quit;
