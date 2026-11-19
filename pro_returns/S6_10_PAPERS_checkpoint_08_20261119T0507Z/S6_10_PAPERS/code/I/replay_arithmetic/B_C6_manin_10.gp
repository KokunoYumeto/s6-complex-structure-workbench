default(parisizemax,2000000000);
E=ellinit([0, 0, 1, -7370, 243528]);
c=ellmaninconstant(E);
print("INDEX 10 Manin ",c);
if(c!=1,error("Manin constant differs from1"));
quit;
