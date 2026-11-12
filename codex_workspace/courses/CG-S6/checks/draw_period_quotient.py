"""Reproducible labelled diagram for lesson 4. CC0-1.0."""
from pathlib import Path
from xml.sax.saxutils import escape
root=Path(__file__).resolve().parents[1]
parts=['<svg xmlns="http://www.w3.org/2000/svg" width="620" height="830" viewBox="0 0 620 830" role="img" aria-labelledby="title desc">',
       '<title id="title">Every period in the line-bundle quotient</title>',
       '<desc id="desc">First divide by three periods, then by the signed first period. The exact contraction factor is exponential of two pi D.</desc>',
       '<defs><marker id="arrow" markerUnits="userSpaceOnUse" markerWidth="12" markerHeight="10" refX="9" refY="5" orient="auto"><path d="M0 0L10 5L0 10Z" fill="#315e73"/></marker></defs>',
       '<rect width="620" height="830" fill="#fcfaf5"/>']
def text(x,y,s,size=23,fill='#213844'):
    parts.append(f'<text x="{x}" y="{y}" text-anchor="middle" font-family="Georgia,serif" font-size="{size}" fill="{fill}">{escape(s)}</text>')
def box(y,height,title):
    parts.append(f'<rect x="24" y="{y}" width="572" height="{height}" rx="12" fill="#eef4f3" stroke="#315e73" stroke-width="2"/>')
    text(310,y+35,title,27)
def arrow(y1,y2):
    parts.append(f'<path d="M310 {y1}V{y2}" stroke="#315e73" stroke-width="3" marker-end="url(#arrow)"/>')
text(310,37,'The four original periods',29)
box(64,107,'ℂ² with coordinates (ξ, η)')
text(310,143,'Π = ((6μ, τ, 1, 0), (β, μ, 0, 1))',24)
arrow(215,242)
text(310,203,'(ξ, η) ↦ (ξ, exp(2πiη))',22)
box(253,172,'Lμ× over Eτ = ℂ / (ℤ + τℤ)')
text(310,324,'(ξ, W) ∼ (ξ + 1, W)')
text(310,362,'(ξ, W) ∼ (ξ + τ, exp(2πiμ)W)')
text(310,402,'Lμ = O([μ] − [0])',25)
arrow(501,519)
text(310,460,'A⁻¹(ξ, W) = (ξ − 6μ, exp(−2πiβ)W)',22)
text(310,493,'covers translation by −6[μ]',22)
box(532,97,'Lμ× / ⟨A⁻¹⟩  ≅  ℂ² / ΠΛ')
text(310,602,'Every column of Π is retained.',23)
parts.append('<rect x="24" y="653" width="572" height="148" rx="12" fill="#f5eee0" stroke="#977446" stroke-width="2"/>')
text(310,688,'N(A⁻¹x) / N(x) = exp(2πD)',25)
text(310,729,'D = Im β − 6(Im μ)² / Im τ',25)
text(310,768,'D < 0 gives the contracting direction.',23)
parts.append('</svg>')
(root/'assets/period-line-quotient.svg').write_text('\n'.join(parts)+'\n',encoding='utf-8')
