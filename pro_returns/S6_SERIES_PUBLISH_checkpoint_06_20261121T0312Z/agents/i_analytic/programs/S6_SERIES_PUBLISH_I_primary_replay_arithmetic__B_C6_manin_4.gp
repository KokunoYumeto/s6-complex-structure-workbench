default(parisizemax,2000000000);
E=ellinit([0, 0, 0, -2380, 44688]);
c=ellmaninconstant(E);
print("INDEX 4 Manin ",c);
if(c!=1,error("Manin constant differs from1"));
quit;
