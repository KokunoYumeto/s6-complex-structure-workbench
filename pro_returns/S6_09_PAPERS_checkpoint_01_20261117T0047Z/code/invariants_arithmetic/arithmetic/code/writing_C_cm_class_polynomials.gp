\\ Exact class polynomials establish the CM tau/j matching used by the Arb brackets.
D=[-8,-12,-16,-28,-7,-11,-19,-27,-43,-67,-163];
J=[8000,54000,287496,16581375,-3375,-32768,-884736,-12288000,-884736000,-147197952000,-262537412640768000];
for(k=1,#D,H=polclass(D[k]);if(H!=x-J[k],error("Class polynomial mismatch"));print(D[k]," | ",H));
print("ALL 11 CLASS POLYNOMIALS MATCH EXACTLY");
quit;
