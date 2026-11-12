"""The exact parameter quotient and finite parity obstruction. CC0-1.0."""
from pathlib import Path
import re
from xml.sax.saxutils import escape
root=Path(__file__).resolve().parents[1]
out=['<svg xmlns="http://www.w3.org/2000/svg" width="620" height="1080" viewBox="0 0 620 1080" role="img" aria-labelledby="title desc">',
 '<title id="title">The complete family remembers the parity of a period shift</title>',
 '<desc id="desc">The middle periods identify every integer shift. The order-four filling retains the shift modulo two. The complete objects are therefore parametrized by c modulo twice the integers, with w equal to exp minus pi i c. The two different values w and minus w have the same middle reference parameter lambda zero times w squared. Their finite classes differ.</desc>',
 '<defs><marker id="arrow" markerWidth="10" markerHeight="10" refX="9" refY="5" orient="auto"><path d="M0 0L10 5L0 10Z" fill="#315e73"/></marker></defs>',
 '<rect width="620" height="1080" fill="#fcfaf5"/>']
def text(y,s,size=24,x=310):
 markup=re.sub(r"_\{([^}]+)\}|_([A-Za-z0-9]+)",lambda m:'<tspan baseline-shift="sub" font-size="70%">'+(m.group(1) or m.group(2))+'</tspan>',escape(s))
 out.append(f'<text x="{x}" y="{y}" xml:space="preserve" text-anchor="middle" font-family="Georgia,serif" font-size="{size}" fill="#213844">{markup}</text>')
def box(x,y,w,h):
 out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="#eef4f3" stroke="#315e73" stroke-width="2"/>')
def arrow(x1,y1,x2,y2):
 out.append(f'<path d="M{x1} {y1}L{x2} {y2}" stroke="#315e73" stroke-width="2.5" marker-end="url(#arrow)"/>')
text(38,'Which period shifts identify the whole object?',25)
box(28,65,564,120)
text(103,'Middle family: every integer shift n',25)
text(145,'Π_{c+n} = Π_c(I + nE),  E = δ̂ ⊗ γ,  E² = 0',22)
arrow(310,197,310,233)
box(28,248,564,173)
text(285,'Retain the actual finite equations',26)
text(326,'Nⱼℓⱼ = −(1 − a)vⱼ − nεⱼδ̂',25)
text(365,'Order three: a = +1',24)
text(402,'Order four: n must be even',24)
arrow(310,433,310,469)
box(28,484,564,124)
text(525,'Full threefold: c′ − c ∈ 2ℤ',29)
text(567,'All even shifts extend over the original cusp.',22)
text(640,'w = exp(−πic) parametrizes the full objects.',23)
box(47,683,222,114);box(351,683,222,114)
text(723,'w',32,x=158);text(723,'−w',32,x=462)
text(761,'X_c',27,x=158);text(761,'X_{c+1}',27,x=462)
text(829,'Different order-two finite classes',25)
arrow(158,849,272,930);arrow(462,849,348,930)
box(124,944,372,93)
text(979,'Same middle parameter',25)
text(1016,'u_{ref} = λ₀w²,  λ₀ ≠ 0',26)
text(1064,'Exact quotient maps: Sections 5–8 and Exercise 9.3.',20)
out.append('</svg>')
(root/'assets/period-identifications.svg').write_text('\n'.join(out)+'\n',encoding='utf-8')
