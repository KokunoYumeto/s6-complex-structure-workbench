#!/usr/bin/env python3
"""Create a distinct D19 derivative with exact current-source guards.

The sealed B tools and packets are immutable. Only path configuration, the
fresh enumerated row counts, and the obsolete line-number citation guard are
changed here. Citation identity is strengthened to exact reviewed contexts.
"""
from pathlib import Path
import datetime as dt, difflib, hashlib, json
R=Path(__file__).resolve().parents[1]
B=R/'agents/continuation2_B/D19'
OUT=R/'records/S6_SERIES_PUBLISH_II_D19_rebase_01'
OLDPRE='S6_SERIES_PUBLISH_II_B2_D19_'
NEWPRE='S6_SERIES_PUBLISH_II_D19_rebase_01_'
sha=lambda b:hashlib.sha256(b).hexdigest()
assert sha((R/'S6_SERIES_PUBLISH_II.tex').read_bytes())=='58a481e28e6c881b1da96cc3dcac9189c8c1fbd1f62f2568c722de0345d9fa5b'
OUT.mkdir(exist_ok=True)
old=(B/(OLDPRE+'propose.py')).read_text();new=old
edits=[]
def change(before,after,count=1):
    global new
    assert new.count(before)==count,(before,new.count(before),count)
    new=new.replace(before,after)
    edits.append(dict(old=before,new=after,occurrences=count))
change('ROOT=Path(__file__).resolve().parents[3]\nOUT=Path(__file__).resolve().parent\nPRE="S6_SERIES_PUBLISH_II_B2_D19_"',
       'ROOT=Path(__file__).resolve().parents[1]\nBDIR=ROOT/"agents/continuation2_B/D19"\nOLDPRE="S6_SERIES_PUBLISH_II_B2_D19_"\nOUT=ROOT/"records/S6_SERIES_PUBLISH_II_D19_rebase_01"\nPRE="S6_SERIES_PUBLISH_II_D19_rebase_01_"')
change('OUT/(PRE+"reference_scan.py")','BDIR/(OLDPRE+"reference_scan.py")')
change('OUT/(PRE+"CIR_scope_guard.json")','BDIR/(OLDPRE+"CIR_scope_guard.json")')
change('    data,blocks=scan.inventory(s)\n',
       '    assert digest(s)=="58a481e28e6c881b1da96cc3dcac9189c8c1fbd1f62f2568c722de0345d9fa5b"\n'
       '    data,blocks=scan.inventory(s)\n'
       '    assert len(data["numbered_equations"])==1832\n'
       '    assert len(data["displays"])==3057\n'
       '    assert sum(bool(x["old_tag"]) for x in data["numbered_equations"])==1779\n'
       '    baseline_single=[x for x in json.loads((BDIR/(OLDPRE+"v1_literal_reference_transport.json")).read_text()) if x.get("treatment")=="single-letter text reference replaced by eqref"]\n'
       '    assert len(baseline_single)==9\n')
change('            assert 23200<x["line"]<23600,"A new single-letter text citation needs review"',
       '            assert any((x["old_tag"],x["context"])==(v["old_tag"],v["context"]) for v in baseline_single),"A changed single-letter citation context needs review"')
change('    assert len(single_text)==9',
       '    assert [(x["old_tag"],x["context"]) for x in single_text]==[(x["old_tag"],x["context"]) for x in baseline_single]\n    assert len(single_text)==9')
change('==len(after["numbered_equations"])==1830','==len(after["numbered_equations"])==1832')
change('numbered_equations=1830,old_manual_tags=1779','numbered_equations=1832,old_manual_tags=1779')
dest=R/'code/S6_SERIES_PUBLISH_II_D19_rebase_01_propose.py'
assert not dest.exists();dest.write_text(new)
(OUT/'proposer_derivative.diff').write_text(''.join(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile=str(B/(OLDPRE+'propose.py')),tofile=str(dest))))
(OUT/'proposer_derivative_changes.json').write_text(json.dumps(dict(created_utc=dt.datetime.now(dt.timezone.utc).isoformat(),original_sha256=sha(old.encode()),new_sha256=sha(new.encode()),changes=edits,canonical_mutations=0,old_files_modified=False),indent=2)+'\n')

# Derive the temporary TeX verifier without modifying its verification logic.
old=(B/(OLDPRE+'tex_verify.py')).read_text();new=old;edits=[]
change('ROOT=Path(__file__).resolve().parents[3]\nOUT=Path(__file__).resolve().parent\nTMP=ROOT.parent/"temporary_B_D19"\nPRE="S6_SERIES_PUBLISH_II_B2_D19_"',
       'ROOT=Path(__file__).resolve().parents[1]\nBDIR=ROOT/"agents/continuation2_B/D19"\nOLDPRE="S6_SERIES_PUBLISH_II_B2_D19_"\nOUT=ROOT/"records/S6_SERIES_PUBLISH_II_D19_rebase_01"\nTMP=ROOT.parent/"temporary_root_D19_rebase_01"\nPRE="S6_SERIES_PUBLISH_II_D19_rebase_01_"')
change('OUT/(PRE+"scan.py")','BDIR/(OLDPRE+"scan.py")')
dest=R/'code/S6_SERIES_PUBLISH_II_D19_rebase_01_tex_verify.py'
assert not dest.exists();dest.write_text(new)
(OUT/'tex_verifier_derivative.diff').write_text(''.join(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile=str(B/(OLDPRE+'tex_verify.py')),tofile=str(dest))))
(OUT/'tex_verifier_derivative_changes.json').write_text(json.dumps(dict(created_utc=dt.datetime.now(dt.timezone.utc).isoformat(),original_sha256=sha(old.encode()),new_sha256=sha(new.encode()),changes=edits,canonical_mutations=0,old_files_modified=False),indent=2)+'\n')
print(json.dumps(dict(proposer='code/S6_SERIES_PUBLISH_II_D19_rebase_01_propose.py',verifier=str(dest.relative_to(R)),expected_numbered_equations=1832,expected_displays=3057,expected_manual_tags=1779,single_letter_guard='All nine exact old-tag/context pairs match the sealed actually-read contexts; appearance order preserved.'),indent=2))
