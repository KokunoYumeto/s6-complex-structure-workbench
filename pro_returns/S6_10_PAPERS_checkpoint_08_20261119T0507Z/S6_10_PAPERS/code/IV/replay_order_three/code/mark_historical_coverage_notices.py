"""Mark older working coverage records with their proved replacement sources."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil
root=Path(__file__).resolve().parents[1]
now=datetime.now(timezone.utc)
archive=root/'records/attempts/checkpoint19_historical_coverage_notices'
archive.mkdir(exist_ok=False)
updates={
 'notes/part3_named_loop_coverage.md':'''## Correction and current scope — 17 November 2026

This is the preserved checkpoint10 coverage audit. Its numerical all-fan formulas and its OS49 return values were subsequently refuted by the explicit counterexamples in **P3K.74** (notes/part3_scalar_formula_corrigendum.tex). The complete corrected scalar-fan calculation is **P3K.72–73**; the component-supported OS49 calculations are **P3K.65–66 and P3K.76–78**, with exact all-fan image and actual shorter endpoints in K77. The source/line/cap comparisons retained from the older arguments are used only in the precise scope proved in those later statements. The former numerical formulas below are historical claims, not current proved values. The current open register is **P3K.75**. The original bytes of this audit are retained in the accompanying attempts directory.

---

''',
 'notes/part3_source_moduli_loops_working.md':'''## Current-status notice — 17 November 2026

This file preserves the successive source-coordinate calculations. The selected-cusp double-loop transport left open in SM.4–6 was subsequently completed, including every lattice-basis fan, by **P3K.71** and its cited exact source/period/Cox/cap maps. The source-zero problem identified in SM.7 is the actual remaining attachment recorded in **P3K.75** and the EA/RT/TL working notes; its absolute residual value remains unassigned. The historical statements of what had not yet been computed below describe their original stage, not a withdrawal of K71. All displayed source-coordinate maps remain available for their stated uses. The original file is preserved before this notice.

---

''',
 'notes/part3_os49_cap_scope.md':'''## Current-status notice — 17 November 2026

This is the original **P3F.33** free-cap derivation. The higher integral homology left uncomputed at that stage was subsequently supplied by **P3F.34**. The correct current component-supported OS49 return values and complete fan formulas are proved in **P3K.65–66 and P3K.76–78**; the earlier all-fan numerical assertions are explicitly refuted in **P3K.74**. The fixed-source smooth order-one clutch comparison, including the full order-m root groupoid, is K78. The proof and its original claims below are preserved as the dated development record, with the earlier bytes archived.

---

'''
}
record={'utc':now.isoformat(),'purpose':'Explicit correction/current-status notices on retained older working notes; no frozen checkpoint is changed.','files':[]}
for rel,notice in updates.items():
    p=root/rel;old=p.read_bytes();dst=archive/p.name;shutil.copy2(p,dst)
    p.write_text(notice+old.decode())
    record['files'].append({'path':rel,'prior_archive':str(dst.relative_to(root)),
      'prior_sha256':hashlib.sha256(old).hexdigest(),'new_sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
(archive/'correction.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))

