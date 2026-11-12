import mpmath as m
v=m.iv;v.dps=50
T0=v.sqrt(3)/2;r0=v.exp(-2*v.pi*T0)
S=1+v.exp(-v.pi*T0)/(1-v.exp(-3*v.pi*T0))
Bs=2*v.exp(v.pi/6)*S*v.exp(r0/(1-r0)**2)
r=v.exp(-4*v.pi)
cosh=lambda x:(v.exp(x)+v.exp(-x))/2
sinh=lambda x:(v.exp(x)-v.exp(-x))/2
error=1/sinh(v.pi)**2+8*(r/(1-r)**3+v.mpf('.5')*(v.exp(-2*v.pi)/(1-v.exp(-2*v.pi))**2+v.exp(-6*v.pi)/(1-v.exp(-6*v.pi))**2)/(1-r))
Bl=2*cosh(v.pi)*v.exp(-v.pi/3)*v.exp(2*cosh(2*v.pi)*r/(1-r)+r*r/(1-r*r))
print('Interval precision decimal digits',v.dps)
for name,x in [('Bs',Bs),('Wp error',error),('Bl',Bl),('D bound small',6/v.pi*v.ln(Bs/(2*v.sqrt(3)))),('D bound large',6/v.pi*v.ln(Bl/(2*v.sqrt(3)))),('counterexample Imc bound',-v.mpf(185)/8+3/v.pi*v.ln(3))]:print(name,x)
assert error.b<v.mpf(1)/3
assert (6/v.pi*v.ln(Bs/(2*v.sqrt(3)))).b<2
assert (6/v.pi*v.ln(Bl/(2*v.sqrt(3)))).b<2
print('Three strict inequalities certified by interval endpoints.')
