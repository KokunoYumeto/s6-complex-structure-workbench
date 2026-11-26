from pathlib import Path
import datetime as dt, hashlib, json

R=Path(__file__).resolve().parents[1]
def binding(path):
    p=Path(path)
    q=p if p.is_absolute() else R/p
    return dict(path=str(p),sha256=hashlib.sha256(q.read_bytes()).hexdigest(),bytes=q.stat().st_size)

out=R/'agents/continuation2_root/S6_SERIES_PUBLISH_II_root_RAT6_freeze.json'
assert not out.exists()
receipt=dict(
    frozen_utc=dt.datetime.now(dt.timezone.utc).isoformat(),
    owner='cdp:st:C.2.RAT.6',tag='01CI',required_check_owner=False,
    derivation=binding('agents/continuation2_root/S6_SERIES_PUBLISH_II_root_RAT6_derivation.md'),
    complete_target_source=binding('../S6_GRIND_5_research_runs_tex/returns/S6_03_CDP/sections/part_C2_rational_triple.tex'),
    proof_exposure='The statement at source lines97-110 was read; the proof beginning at111 has not yet been opened. Historical inventory summary exposure is explicitly disclosed in the derivation. No fully blind credit.',
    supporting_computation=[binding(x) for x in ['code/S6_SERIES_PUBLISH_II_root_BW_koszul_spectrum.py','agents/continuation2_root/01BW/S6_SERIES_PUBLISH_II_root_BW_koszul_spectrum.json']],
    primary_retrieval=binding('agents/continuation2_root/S6_SERIES_PUBLISH_II_root_RAT6_primary_retrieval.json'),
    purpose='Freeze full statement-led supporting derivation before opening its original proof. Existing known-result disposition stays outside the197 required checks. No closure or event is assigned here.')
out.write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(binding(out),indent=2))
print(json.dumps(receipt,indent=2))
