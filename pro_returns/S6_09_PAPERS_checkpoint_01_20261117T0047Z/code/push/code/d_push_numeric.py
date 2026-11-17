"""Two numerical evaluations of the equianharmonic crossing height.
These are supporting numerical evidence, not a proof of the closed form.
"""
import mpmath as mp
mp.mp.dps=110
rho=mp.e**(mp.pi*1j/3)
v=(2-rho)/3
Q=mp.e**(2*mp.pi*1j*rho)
eta=mp.e**(mp.pi*1j*rho/12)*mp.fprod(1-Q**n for n in range(1,301))
R1=mp.jtheta(1,mp.pi*v,mp.e**(mp.pi*1j*rho))/eta
N1=abs(R1)*mp.e**(-mp.pi*mp.im(v)**2/mp.im(rho))
H1=-6/mp.pi*mp.log(N1/(2*mp.sqrt(3)))
R2=2*mp.sin(mp.pi*v)*mp.e**(mp.pi*1j*rho/6)
z=mp.e**(2*mp.pi*1j*v)
for n in range(1,401):
    R2*= (1-Q**n*z)*(1-Q**n/z)
N2=abs(R2)*mp.e**(-mp.pi*mp.im(v)**2/mp.im(rho))
H2=-6/mp.pi*mp.log(N2/(2*mp.sqrt(3)))
guess=3/(2*mp.pi)*mp.log(48)
print('arithmetic precision: 110 decimal digits')
print('method 1: mpmath theta series, 300 eta-product factors')
print('height 1:',mp.nstr(H1,85))
print('method 2: theta/eta product after exact factor cancellation, 400 factors')
print('height 2:',mp.nstr(H2,85))
print('difference:',mp.nstr(abs(H1-H2),8))
print('proposed height:',mp.nstr(guess,85))
print('difference from proposed exact form:',mp.nstr(abs(H1-guess),8))
print('STATUS: numerical evidence only; exact equality not inferred.')
