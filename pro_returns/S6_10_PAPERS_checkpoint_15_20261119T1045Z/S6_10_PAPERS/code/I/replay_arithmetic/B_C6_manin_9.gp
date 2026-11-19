default(parisizemax,2000000000);
E=ellinit([0, 0, 1, -860, 9707]);
c=ellmaninconstant(E);
print("INDEX 9 Manin ",c);
if(c!=1,error("Manin constant differs from1"));
quit;
