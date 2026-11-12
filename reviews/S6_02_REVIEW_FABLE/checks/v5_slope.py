import mpmath as mp
mp.mp.dps = 40
pi = mp.pi
def wp(v, tau):
    q = mp.exp(1j*pi*tau); z = pi*v
    t1 = mp.jtheta(1, z, q); t1d = mp.jtheta(1, z, q, 1); t1dd = mp.jtheta(1, z, q, 2)
    c = mp.jtheta(1, 0, q, 3)/mp.jtheta(1, 0, q, 1)/3
    return pi**2*(-(t1dd*t1 - t1d**2)/t1**2 + c)
for x in (mp.mpc('1e-3','0'), mp.mpc('0','1e-3'), mp.mpc('7e-4','-7e-4'), mp.mpc('1e-5','2e-5')):
    tau = 1j + x
    guess = (1 - tau)/2 + mp.sqrt(2j/(3*pi)*x)
    v = mp.findroot(lambda vv: wp(vv, tau), guess)
    h = v - (1 - tau)/2
    print('x =', mp.nstr(x, 5), ' h^2/x =', mp.nstr(h**2/x, 12), '  2i/(3 pi) =', mp.nstr(2j/(3*pi), 12))
