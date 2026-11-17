# Check of S6_01 A2.2: mu_s(0) at the order-four point, from the expansion
# (mu-(1-tau)/2)^2 = (2i/(3 pi))(tau-i)+..., tau-i = a s^2+..., j(tau)=1728 t, t-1=s^4.
import mpmath as mp
mp.mp.dps = 40
J = lambda tau: 1728*mp.kleinj(tau)          # mpmath kleinj = j/1728
j2 = mp.diff(J, 1j, 2)                        # j''(i)
a2 = 2*1728/j2                                # (tau-i)^2 = 2*1728 s^4 / j''(i)
a = mp.sqrt(a2)
mus2 = 2j*a/(3*mp.pi)
print("j''(i) =", j2)
print("a^2 =", a2, " a =", a)
print("mu_s(0)^2 =", mus2, " and with the other sign of a:", -mus2)
print("|mu_s(0)| =", mp.sqrt(abs(mus2)), "  claimed 0.2366093140807852246877051134504496062943")
G = mp.gamma(mp.mpf(1)/4)
print("j''(i) closed form guess  -2*3^4*Gamma(1/4)^8/pi^4 ... value:", -2*81*G**8/mp.pi**4)
