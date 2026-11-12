"""Reproducible exact canonical-ring and fibration diagram. CC0-1.0."""
from pathlib import Path
from xml.sax.saxutils import escape
root=Path(__file__).resolve().parents[1]
out=['<svg xmlns="http://www.w3.org/2000/svg" width="620" height="1020" viewBox="0 0 620 1020" role="img" aria-labelledby="title desc">',
 '<title id="title">Recovering the original fibration from the anticanonical ring</title>',
 '<desc id="desc">The finite characters give evaluation orders zero and two. The canonical line is O of minus two S2. Its anticanonical ring has generators u of degree one and v of degree two. The degree-two pencil is the original map f followed by beta, with full fibre divisors W, 3 S1 and 4 S2.</desc>',
 '<defs><marker id="arrow" markerWidth="10" markerHeight="10" refX="9" refY="5" orient="auto"><path d="M0 0L10 5L0 10Z" fill="#315e73"/></marker></defs>',
 '<rect width="620" height="1020" fill="#fcfaf5"/>']
def text(y,s,size=24,x=310):
 markup=escape(s).replace("_X",'<tspan baseline-shift="sub" font-size="70%">X</tspan>').replace("_B",'<tspan baseline-shift="sub" font-size="70%">B</tspan>')
 out.append(f'<text x="{x}" y="{y}" xml:space="preserve" text-anchor="middle" font-family="Georgia,serif" font-size="{size}" fill="#213844">{markup}</text>')
def box(y,h):
 out.append(f'<rect x="28" y="{y}" width="564" height="{h}" rx="12" fill="#eef4f3" stroke="#315e73" stroke-width="2"/>')
def arrow(y1,y2):
 out.append(f'<path d="M310 {y1}V{y2}" stroke="#315e73" stroke-width="2.5" marker-end="url(#arrow)"/>')
text(38,'The original fibres inside the graded ring',27)
box(64,160)
text(102,'Base covers: t₁ = s₁³, t₂ = s₂⁴',27)
text(142,'m₁ = 3, a₁ = 2',23,x=165)
text(142,'m₂ = 4, a₂ = 1',23,x=455)
text(180,'Evaluation order kⱼ = mⱼ − 1 − aⱼ',23)
text(210,'k₁ = 0',23,x=165)
text(210,'k₂ = 2',23,x=455)
arrow(234,267)
box(280,125)
text(317,'Hodge line: 𝔎 ≅ O_B(p₀)',27)
text(354,'div(ev) = 2S₂;  fibre at p₂ = 4S₂',23)
text(388,'ω_X ≅ O_X(−2S₂)',29)
arrow(417,451)
box(464,161)
text(504,'R(X, −K_X) = ℂ[u, v]',29)
text(544,'deg u = 1,   deg v = 2',26)
text(582,'Degree m: uᵐ⁻²ʲvʲ,  0 ≤ j ≤ ⌊m/2⌋',22)
text(610,'div(u) = 2S₂;  u² pulls back σp₂',23)
arrow(637,670)
box(683,154)
text(724,'x ↦ [u(x)² : v(x)] = β(f(x))',25)
text(764,'β(t) = [t − 1 : A + B(t − 1)]',24)
text(806,'A ≠ 0;  β is a base isomorphism.',23)
text(885,'Original scheme-theoretic fibres',26)
text(930,'p₀ = ∞',23,x=115)
text(930,'p₁ = 0',23,x=310)
text(930,'p₂ = 1',23,x=505)
text(970,'W',26,x=115)
text(970,'3S₁',26,x=310)
text(970,'4S₂',26,x=505)
text(1005,'Exact maps and coefficients: Sections 2–7.',20)
out.append('</svg>')
(root/'assets/canonical-ring-fibration.svg').write_text('\n'.join(out)+'\n',encoding='utf-8')
