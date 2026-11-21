\\ Simplified models, exact local data, periods and L-derivatives.
default(realprecision,100);
default(parisizemax,1000000000);
{
 E=ellinit([0,0,0,-2,1]);P=[0,1];om=2*real(E.omega[1]);
 print("rational curve ",E[1..5]," rank ",ellrank(E)," torsion ",elltors(E));
 print("full_real_period ",om," Lprime/Omega ",lfun(E,1,1)/om," L1/Omega ",lfun(E,1)/om);
 ms=msfromell(E,1);print("plus_modular_symbol_0_oo ",mseval(ms[1],ms[2],[0,oo]));
 print("exact_Lprime_ratio_formula ",(Euler+log(2*Pi/sqrt(40)))/8);
 print("hO ",ellheight(E,P)/2," logN ",log(10)/12," D ",6/Pi*(log(10)/12-log(2*sqrt(3))));
}
{
 K=bnfinit(y^2-3,1);a=Mod(y,y^2-3);E=ellinit([0,0,0,-18-10*a,21+12*a],K);P=[0,3+2*a];Q=[1,-1-a];
 print("quadratic curve ",E[1..5]," j ",E.j," P ",P," Porder ",ellorder(E,P)," torsion ",elltors(E));
 print("Delta ",E.disc," globalred ",ellglobalred(E));
 print("nontorsion_Q ",Q," on_curve ",ellisoncurve(E,Q)," order ",ellorder(E,Q)," height2O ",ellheight(E,Q));
 s=sqrt(3);Eminus=ellinit([0,0,0,-18-10*s,21+12*s]);Eplus=ellinit([0,0,0,-18+10*s,21-12*s]);
 omminus=if(Eminus.disc>0,2,1)*real(Eminus.omega[1]);omplus=if(Eplus.disc>0,2,1)*real(Eplus.omega[1]);
 print("full_real_period_tminus ",omminus," full_real_period_tplus ",omplus);
 omprod=omminus*omplus;print("period_product ",omprod," BSD_period_with_discriminant_factor ",omprod/sqrt(12));
 Ld=lfuncreate(E);print("Ldata_gamma_weight_conductor_sign ",Ld[3..6]);lp=lfun(Ld,1,1);
 print("L1 ",lfun(Ld,1)," Lprime ",lp," Lprime/period_product ",lp/omprod," Lprime/BSDperiod ",lp*sqrt(12)/omprod);
 print("hO(P) ",ellheight(E,P)/2," finite_sum ",log(11)/12);
 print("tminus logN ",log(17+10*s)/12," N ",(17+10*s)^(1/12)," D ",6/Pi*(log(17+10*s)/12-log(2*sqrt(3))));
 print("tplus logN ",log(10*s-17)/12," N ",(10*s-17)^(1/12)," D ",6/Pi*(log(10*s-17)/12-log(2*sqrt(3))));
 print("sumlogN ",(log(17+10*s)+log(10*s-17))/12);
}
quit;
