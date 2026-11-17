#!/usr/bin/env python3
"""Break long displays and use aligned for multiple equation pairs."""
from pathlib import Path

root = Path(__file__).resolve().parents[1]
path = root / 'sections/C_critical.tex'
text = path.read_text()
text = text.replace(r'\begin{split}', r'\begin{aligned}')
text = text.replace(r'\end{split}', r'\end{aligned}')
changes = [
    (r''' r_0=2-\sqrt3,\quad A=E_4(i),\quad k=\pi^2A,
 \quad v=\pi\sqrt A\,w,\quad z=v^2=kw^2,
 \quad z_0=kr_0^2,\quad c_0=1-\frac1{\sqrt3}.''',
     r''' \begin{gathered}
 r_0=2-\sqrt3,\qquad A=E_4(i),\qquad k=\pi^2A,\\
 v=\pi\sqrt A\,w,\qquad z=v^2=kw^2,\\
 z_0=kr_0^2,\qquad c_0=1-\frac1{\sqrt3}.
 \end{gathered}'''),
    (r''' \sqrt A f_2(v)=\frac{E_2(\tau)}{(1-w)^2}
                         -\frac3{\pi(1-w)},\quad
 A f_4(v)=\frac{E_4(\tau)}{(1-w)^4},\quad
 A^{3/2} f_6(v)=\frac{E_6(\tau)}{(1-w)^6}.''',
     r''' \begin{gathered}
 \sqrt A f_2(v)=\frac{E_2(\tau)}{(1-w)^2}
                         -\frac3{\pi(1-w)},\\
 A f_4(v)=\frac{E_4(\tau)}{(1-w)^4},\qquad
 A^{3/2} f_6(v)=\frac{E_6(\tau)}{(1-w)^6}.
 \end{gathered}'''),
    (r''' f_2'=\frac{f_4-f_2^2}{3},\qquad
 f_4'=\frac43(f_6-f_2f_4),\qquad
 f_6'=2(f_4^2-f_2f_6),\qquad
 (f_2,f_4,f_6)(0)=(0,1,0).''',
     r''' \begin{gathered}
 f_2'=\frac{f_4-f_2^2}{3},\qquad
 f_4'=\frac43(f_6-f_2f_4),\qquad
 f_6'=2(f_4^2-f_2f_6),\\
 (f_2,f_4,f_6)(0)=(0,1,0).
 \end{gathered}'''),
]
for before, after in changes:
    assert text.count(before) == 1, before
    text = text.replace(before, after)
path.write_text(text)
print('Replaced split by aligned; split constants, modular functions, and ODE displays.')
