#!/usr/bin/env python3
"""Preserve the reviewed bibliography proposal and issue its final DOI style.

Only the four newly added DOI fields change from a URL command to the already
established DOI macro. This program writes proposed guards, never paper source.
"""
from pathlib import Path
import copy
import datetime as dt
import hashlib
import json
import re

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'agents/continuation_infra'


def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    reviewed=OUT/'S6_SERIES_PUBLISH_I_candidate16_infra_D18_publication_guards.json'
    assert sha(reviewed)=='dca099fa6674ff9c0b8f14ad9736718e578ea9e6a353786a823758f323bcb651'
    previous=json.loads(reviewed.read_text())
    final=copy.deepcopy(previous)
    total=0
    for old,g in zip(previous,final):
        g['after'],count=re.subn(r'\\url\{https://doi\.org/([^}]+)\}',lambda m:r'\doi{'+m[1]+'}',g['after'])
        total+=count
        g['revision']=3
        g['supersedes_guard_file']=str(reviewed.relative_to(ROOT))
        g['superseded_guard_files']=[
          'agents/continuation_infra/S6_SERIES_PUBLISH_I_candidate16_infra_D18_guards.json',
          str(reviewed.relative_to(ROOT))]
        g['reviewed_prior_after_sha256']=hashlib.sha256(old['after'].encode()).hexdigest()
        g['final_doi_macro_replacements']=count
        g['original_entry']=f"agents/continuation_infra/{g['id']}_original_bibliography_entry.tex"
        original=ROOT/g['original_entry']
        assert original.read_text()==g['before']
        g['original_entry_sha256']=sha(original)
        final_entry=OUT/(g['id']+'_publication_final_bibliography_entry.tex')
        assert not final_entry.exists();final_entry.write_text(g['after'])
        g['proposed_entry']=str(final_entry.relative_to(ROOT));g['proposed_entry_sha256']=sha(final_entry)
    assert total==4
    source=ROOT/'S6_SERIES_PUBLISH_I.tex'
    source_sha=sha(source)
    assert source_sha==previous[0]['source_sha256']
    before=source.read_text();after=before
    for g in final:
        assert after.count(g['before'])==1
        after=after.replace(g['before'],g['after'],1)
    assert before.split(r'\begin{thebibliography}',1)[0]==after.split(r'\begin{thebibliography}',1)[0]
    target=OUT/'S6_SERIES_PUBLISH_I_candidate16_infra_D18_publication_guards_final.json'
    receipt=OUT/'S6_SERIES_PUBLISH_I_candidate16_bibliography_publication_final_receipt.json'
    assert not target.exists() and not receipt.exists()
    target.write_text(json.dumps(final,indent=2)+'\n')
    record=dict(recorded_utc=dt.datetime.now(dt.timezone.utc).isoformat(),paper='I',candidate=16,
                source_sha256=source_sha,previous_reviewed_guard_file=str(reviewed.relative_to(ROOT)),
                previous_reviewed_guard_sha256=sha(reviewed),final_guard_file=str(target.relative_to(ROOT)),
                final_guard_sha256=sha(target),guard_count=7,new_doi_fields_using_existing_macro=4,
                cited_edition_notes_and_citation_keys_unchanged_from_reviewed_set=True,
                original_source_before_bibliography_byte_identical=True,
                proposed_source_sha256=hashlib.sha256(after.encode()).hexdigest(),
                canonical_source_unchanged=sha(source)==source_sha,mathematical_events_added=0,
                supersedes=[str(reviewed.relative_to(ROOT)),
                            'agents/continuation_infra/S6_SERIES_PUBLISH_I_candidate16_infra_D18_guards.json'],
                scope='Final style refinement of the reviewed full-entry proposal: four DOI macro substitutions only. Apply this seven-guard set once; prior proposal sets remain preserved.')
    receipt.write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps(dict(final_guard_file=str(target),final_guard_sha256=sha(target),
                          receipt=str(receipt),receipt_sha256=sha(receipt),source_unchanged=sha(source)==source_sha),indent=2))


if __name__=='__main__':main()
