\\ Deterministic number-field two-descent using Denis Simon's published code.
default(realprecision,80);
default(parisizemax,1000000000);
read("code/I/replay_torsion/Crank_Sage_ellcommon.gp");
read("code/I/replay_torsion/Crank_Sage_ell.gp");
default_ell(3,2,4,2,20,0);
K=bnfinit(y^2-3,1);a=Mod(y,y^2-3);
print("bnfcertify ",bnfcertify(K));
E=[0,0,0,-18-10*a,21+12*a];P=[0,3+2*a];
print("curve ",E," point ",P);
print("RESULT ",bnfellrank(K,E,[P]));
quit;
