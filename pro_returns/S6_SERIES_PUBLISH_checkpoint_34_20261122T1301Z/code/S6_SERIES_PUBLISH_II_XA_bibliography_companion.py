from pathlib import Path
import datetime as dt,hashlib,json

R=Path(__file__).resolve().parents[1]
def sha(b):return hashlib.sha256(b).hexdigest()
def bind(s):
    b=(R/s).read_bytes()
    return dict(path=s,sha256=sha(b),bytes=len(b))

p=R/'S6_SERIES_PUBLISH_references.bib'
before=p.read_bytes()
assert sha(before)=='f1ac2c94a0c742eee7b40891e4cce1f5c0ccc604c7a58a301d72eae5dda27949'
assert b'{FavreThesis2002,' not in before and b'{DlousskyOeljeklaus1999,' not in before
addition=r'''

@phdthesis{FavreThesis2002,
  author = {Favre, Charles},
  title = {Dynamique des applications rationnelles},
  year = {2000},
  note = {Author-hosted version dated 22 July 2002},
  url = {https://www.cmls.polytechnique.fr/perso/favre.charles/these.pdf}
}

@article{DlousskyOeljeklaus1999,
  author = {Dloussky, Georges and Oeljeklaus, Karl},
  title = {Vector fields and foliations on compact surfaces of class {$\mathrm{VII}_0$}},
  journal = {Annales de l'Institut Fourier},
  volume = {49},
  number = {5},
  pages = {1503--1545},
  year = {1999},
  doi = {10.5802/aif.1728},
  url = {https://www.numdam.org/item/10.5802/aif.1728.pdf}
}
'''.encode()
after=before+addition
out=R/'records/S6_SERIES_PUBLISH_II_XA_bibliography_companion.json'
assert not out.exists()
record=dict(created_utc=dt.datetime.now(dt.timezone.utc).isoformat(),scope='Bibliography companion for the two exact entries admitted into Paper II in batch70; no paper source is modified.',source=bind('S6_SERIES_PUBLISH_II.tex'),admission=bind('records/S6_SERIES_PUBLISH_II_clean_checks_70/manifest.json'),admitted_entries=bind('agents/continuation2_A/S6_SERIES_PUBLISH_II_A2_XA_v1_20261122/S6_SERIES_PUBLISH_II_A2_XA_bibliography_entries.tex'),file=p.name,before_sha256=sha(before),after_sha256=sha(after),append_text=addition.decode(),exact_prior_bytes_preserved=True,keys_added=['FavreThesis2002','DlousskyOeljeklaus1999'],new_mathematical_events=0,new_defect_rows=0,closed_provenance_claims=0)
p.write_bytes(after)
assert p.read_bytes().startswith(before)
out.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(dict(bibliography_sha256=sha(after),receipt=bind(str(out.relative_to(R)))),indent=2))
