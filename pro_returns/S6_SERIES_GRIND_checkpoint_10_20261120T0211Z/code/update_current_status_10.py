"""Guarded report refresh for the two accepted checkpoint10 proofs."""
from pathlib import Path
import datetime,hashlib,json
R=Path(__file__).resolve().parents[1]
p=R/'code/current_status07.py'
receipt=R/'analysis/status_generator_update_10.json'
assert not receipt.exists()
old=p.read_text();t=old;changes=[]
def replace(a,b):
    global t
    assert t.count(a)==1,(a[:100],t.count(a))
    t=t.replace(a,b)
    changes.append({'old':a,'new':b})
replace('The entire seven-theorem/35-step PaperII outline comparison has been completed at its stated current scope.',
        'The earlier complete seven-theorem/35-step PaperII outline comparison retains its stated scope. The new accepted comb result supplies a seventh step in main F, giving36 outline steps; the full new F statement and its exact body/outline maps have a separate receiving record.')
replace('For the open comb problem, the new explicit wedge map gives K_m = rho_*(coker(delta0)^* tensor detG), with the dual-extension sign and invariant pushforward proved. This is an exact relation of the existing maps, not a solved period section or a strict reduction of the remaining splitting gate.',
        'For the comb problem, the explicit wedge map gives K_m = rho_*(coker(delta0)^* tensor detG), with the dual-extension sign and invariant pushforward proved. The newly accepted E2.5 then proves a nonempty open family of actual admissible twelve-tooth embedded smoothings with K_12=O(-8) direct-sum O(-9)^2, e_12=0, h0=0, h1=23 and Hodge values(49,48). Its full seven-step proof, exact main-F statement, seventh outline step and three marked-plane scope are integrated. The original section, the regular mixed node, the finite-root graph division, actual conic two-jets, normalization collapse and both family-cohomology vanishings are compared by their literal maps. The53-check root program and25-check receiving program retain their exact exposure scopes. A complete independent derivation was frozen before target proof/code reading; prior admitted inputs and route cues remain disclosed. Viaclovsky Lemma5.1, Proposition5.3, section9.2 and question10(2) give the opened source credit. E2.3 remains open for the remaining tooth counts and special members. Whole-row confidence, source and current-page decisions remain controlled by the canonical assessment.')
start=t.index('For PaperII, root has also frozen a complete proposed twelve-tooth flat-kernel construction.')
end=t.index('\n\n### PaperIV',start)
replace(t[start:end],'The accepted PaperII comb construction is recorded in its own paper section above; its exact mathematical status changed only after the full independent comparison and root acceptance receipt.')
replace('P1.8 and P1.17 retain their remaining whole-row gates. P1.19 is now explicitly open for the geometric comparison described below.',
        'P1.8 and P1.17 retain their remaining whole-row gates. A new isolated-input P1.8 derivation is in progress before target-proof exposure; no unfinished derivation is assigned completion credit. P1.19 has a newly accepted complete geometric comparison, as recorded below; its additional before-reading confidence gate remains expressly pending.')
start=t.index('A later post-reading P1.19 supplement constructs exact floor-chain composition,')
end=t.index('\n\n## Every mathematically open inventory placement',start)
replace(t[start:end],'''The complete new P1.19 geometric repair was frozen at01:37:26UTC and received in full by root and corrections. It constructs an actual free integral rational-polyhedral model, the all-degree triangle/product homotopies and degree-five floor replacement, the four literal finite-cap cell maps with their based positive meridians, the coefficient-two order-four cap homotopy and the resulting cone chain equivalence. The inverse-word prism and the explicit integral seven-chain fix the prescribed cusp tori. The common fibre is carried exactly to its coordinate cycles, preserving all four saved integral F_k fillers. The rank-nine boundary image and odd secondary term then follow from the printed local relative-duality argument, without assuming the global homology or global duality conclusion. The154-check geometric program,113-check top adapter and50-check receiving program retain their actual authorship and exposure scopes. Root corrected an ambiguous rank-nine antecedent by naming the exact map H4(B0) to H4(C).

The earlier failed cellular-approximation argument and withdrawn whole-row closure remain in the immutable history. The new complete proof closes their mathematical gap and restores P1.19 to proved in the body, with its permanent label and all eight original formula tags retained. The new all-degree repair was constructed after earlier proof exposure, so no whole-before-reading claim is manufactured. Current complete-proof visual/reference checks and the exact added-step before-reading confidence reconciliation remain separate recorded obligations. The independently established actual fourfold homology in P1.12 retains its own proof and credit.''')
start=t.index("The complete current report records P1.19's newly identified integral geometric-comparison gap")
end=t.index('\n\nCurrent canonical completion:',start)
replace(t[start:end],'''The complete current report records the accepted P1.19 integral geometric comparison and restored complete theorem, including its actual all-degree finite-cap/common-fibre/cusp maps and precisely pending added-step before-reading confidence gate. The accepted PaperII twelve-tooth open-family proposition gives K_12=O(-8) direct-sum O(-9)^2, e_12=0 and Hodge values(49,48); its complete proof, exact main F and seventh outline step are integrated, while broader E2.3 remains open. Root53 and receiving25 comb assertions, and the154/113/50 P1.19 assertions, retain their exact proof-reading chronology. The complete new weighted OS45 source-line, embedded odd sphere and integral Borel/framing proof gives P_ref=0 at the precise D2.53 scope; broader D2.4 remains open. K111/K112 retain their expressly bounded whole-row exposure gates. A fresh isolated-input P1.8 derivation is in progress. Mathematical acceptance and current full-page inspection are separately recorded.''')
needle="              'audit_corrections/III_OS45_local_geometry_receiving_08.md']:"
replace(needle,"              'audit_corrections/III_OS45_local_geometry_receiving_08.md',\n              'analysis/comb_open_family_acceptance_10.json','analysis/comb_open_family_integration_10.json',\n              'analysis/P119_geometric_integration_10.json','audit_corrections/P119_geometric_09/FULL_RECEIVING_REVIEW.md',\n              'audit_root/arithmetic_09/primary_sources/opening_02_full_visual.json']:")
# The primary-source receipt can reside one level above the assets directory.
candidate=R/'audit_root/arithmetic_09/primary_sources/opening_02_full_visual.json'
if not candidate.exists():
    found=list((R/'audit_root/arithmetic_09').rglob('opening_02_full_visual.json'))
    assert len(found)==1
    t=t.replace('audit_root/arithmetic_09/primary_sources/opening_02_full_visual.json',str(found[0].relative_to(R)))
compile(t,str(p),'exec')
p.write_text(t)
receipt.write_text(json.dumps({'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'before_sha256':hashlib.sha256(old.encode()).hexdigest(),'after_sha256':hashlib.sha256(t.encode()).hexdigest(),'changes':changes},indent=2)+'\n')
print(json.dumps({'guards':len(changes),'receipt':str(receipt.relative_to(R))}))
