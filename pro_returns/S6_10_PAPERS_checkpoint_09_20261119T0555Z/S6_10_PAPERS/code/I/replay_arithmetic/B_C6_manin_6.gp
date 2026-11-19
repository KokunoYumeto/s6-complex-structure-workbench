default(parisizemax,2000000000);
E=ellinit([0, -1, 1, -7, 10]);
c=ellmaninconstant(E);
print("INDEX 6 Manin ",c);
if(c!=1,error("Manin constant differs from1"));
quit;
