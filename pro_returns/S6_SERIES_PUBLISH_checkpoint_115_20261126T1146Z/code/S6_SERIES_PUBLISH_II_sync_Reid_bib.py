from pathlib import Path
import datetime as dt,hashlib,json
R=Path(__file__).resolve().parents[1]
p=R/'S6_SERIES_PUBLISH_references.bib';old=p.read_bytes()
entry=r'''
@incollection{Reid1997Chapters,
  author = {Reid, Miles},
  title = {Chapters on algebraic surfaces},
  booktitle = {Complex algebraic geometry (Park City, UT, 1993)},
  series = {IAS/Park City Mathematics Series},
  volume = {3},
  pages = {3--159},
  publisher = {American Mathematical Society},
  address = {Providence, RI},
  year = {1997},
  doi = {10.1090/pcms/003/02},
  url = {https://mreid.warwick.ac.uk/surf/Reid_Park_City_chapters.pdf},
  verification = {verified at listed scope},
  source_note = {Author-hosted published scan, SHA256 a0e1145b0fa8633cdf5f7cbc61daa87f2523435da147dc5457521087ed228f1c. Checker continuation2_B actually read Proposition4.14 and proof, pp102--103, the lemma and full proof in Section4.17 p105, and continuation through p108. DOI and publisher fields verified through Crossref. The printed lemma has an affine algebraic base; PaperII supplies the explicit analytic relative-evaluation argument on Stein representatives. Exact page-image and retrieval receipt: agents/continuation2_B/01B8/S6_SERIES_PUBLISH_II_B2_B8_primary_receipt.json.}
}
'''
assert b'{Reid1997Chapters,' not in old
new=old+entry.encode();p.write_bytes(new)
sha=lambda b:hashlib.sha256(b).hexdigest()
rp=R/'records/S6_SERIES_PUBLISH_II_Reid_bib_sync_20261122.json';assert not rp.exists()
rp.write_text(json.dumps(dict(created_utc=dt.datetime.now(dt.timezone.utc).isoformat(),path=p.name,before_sha256=sha(old),after_sha256=sha(new),exact_append=entry,reason='Synchronize the separately delivered bibliography with the exact D18 entry already admitted in batch59; no source proof or ledger mutation.',paper_source_changed=False,events_added=0,required_rows_closed=0),indent=2)+'\n')
print(json.dumps(dict(path=p.name,sha256=sha(new),receipt=str(rp.relative_to(R)))))
