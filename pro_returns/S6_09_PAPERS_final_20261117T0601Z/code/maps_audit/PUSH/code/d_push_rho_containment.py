"""All 400 rho root enclosures lie in the common uniqueness square."""
from d_root_gradient_certificate import *

rho=acb(rat('1/2'),arb(3).sqrt()/2)
zc=((2-rho)/3).mid()
records=json.loads((BASE/'d_root_rho_boxes.json').read_text())
w=arb(0)
for d in records:
    z=acb(arb(d['centre_real']),arb(d['centre_imag']))
    s=(max((z.real-zc.real).abs_upper(),(z.imag-zc.imag).abs_upper())
       +arb(d['radius']).upper()).upper()
    w=max(w,s)
    assert s<rat('1/80')
print('all_400_roots_in_fixed_square_radius_1/80',str(w))
