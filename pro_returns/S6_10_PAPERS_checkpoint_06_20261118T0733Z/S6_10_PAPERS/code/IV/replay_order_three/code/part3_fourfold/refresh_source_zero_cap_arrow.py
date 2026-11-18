from pathlib import Path
from datetime import datetime,timezone
import json
root=Path(__file__).resolve().parents[2]
stamp=datetime.now(timezone.utc).isoformat()
save=root/'records/attempts/source_zero_cap_arrow'
save.mkdir(parents=True,exist_ok=True)
p=root/'notes/part3_source_zero_annular_attachment_working.md'
t=p.read_text()
old=save/'annular_attachment_before_cap_arrow_cleanup.md'
if not old.exists(): old.write_text(t)
t=t.replace('q_\\infty^{-1}h,qquad','q_\\infty^{-1}h,\\qquad')
t=t.replace('U_a^{\\rm Cartier},qquad','U_a^{\\rm Cartier},\\qquad')
t=t.replace('U_{\\rm cap}^{,b},qquad','U_{\\rm cap}^{b},\\qquad')
t=t.replace('\\zeta_m^{ma/2}quad\\text{and}quad -1','\\zeta_m^{ma/2}\\quad\\text{and}\\quad -1')
start=t.index('This is the reduced equality in (EA.7).')
end=t.index('Finally (z^{mab/2}',start)
t=t[:start]+'''This is the reduced equality in (EA.7). It incorporates the actual
Cartier correction (EA.6) and the already constructed reduced III root
line. No coefficient on an uncorrected tensor frame is used as its
extension. The earlier unused raw tensor-coefficient display is preserved
in the attempt record and is withdrawn from this comparison.
'''+t[end:]
p.write_text(t)
p=root/'notes/part3_source_zero_completion_working.md'
t=p.read_text()
old=save/'source_zero_section8_before_physical_label.md'
if not old.exists(): old.write_text(t)
marker='## 8. The local origin link, with its actual circle charge\n'
assert marker in t
note='''
**Physical-line convention correction (17 November, after P3K.68).**
The positively oriented Hopf line denoted by \(a h\) in (SZ.13) is
the meridian-positive dual \(U=M^{-1}\). The actual nonzero-vector
line has \(c_1(M)=-a h\), so its characteristic value on this same
oriented local quotient is \(-a(a^2-1)/6\). This corrects the label
of the local model calculation below; it does not determine the
orientation with which that model occurs in a global boundary. Both
the finite residual \(\\mu_a\) and the retained ruling arrow remain.

'''
if '**Physical-line convention correction (17 November, after P3K.68).**' not in t:
    t=t.replace(marker,marker+note)
p.write_text(t)
record={'utc':stamp,'status':'PASS','scope':'Exact cap-arrow notation and physical line label; no global attachment or index assigned','preserved_originals':str(save.relative_to(root))}
(root/'records/source_zero_cap_arrow_amendment.json').write_text(json.dumps(record,indent=2)+'\n')
with (root/'records/literature_fourfold.md').open('a') as f:
    f.write(f'\n## {stamp}\n- Source: code/part3_fourfold/source_zero_e_annular_deck.py (own current-run code).\n- Reason: inspect existing exact deck certificate before extending cap-character checks.\n- Material taken: 256 admitted branch/sign rows, component permutations and full normal-unit cancellation.\n')
print(json.dumps(record))
