"""Apply the current prompt's commit and continuation dates to Paper II."""
from S6_SERIES_PUBLISH_c4_edit import *

before = SOURCE.read_text()
changes = [
    ("II-C4-RECORDS-COMMIT", "D18", "preamble; methodology",
     r"\newcommand{\SsixRepositoryCommit}{bc08b5278bcad2beb70b6862c5722f1b9f636db6}",
     r"\newcommand{\SsixRepositoryCommit}{a02f2eacf5a8c3db7cf8cdfcdba50c0002ee91c7}",
     "The controlling continuation prompt section 0.3 prescribes the commit shared with the deposited Papers I and V; the previous Paper II identifier is superseded. The records-page URL remains the single repository address."),
    ("II-C4-METHODOLOGY-DATES", "D07", "methodology",
     "revision and further checks of 20--22 November 2026.",
     "revision and further checks of 20--23 November 2026.",
     "Include this fourth continuation on 23 November. This changes the documented dates of revision and asserts no additional proof-check count or completion."),
]
after = before
rows = []
for ident, kind, location, old, new, reason in changes:
    assert after.count(old) == 1, ident
    after = after.replace(old, new, 1)
    rows.append(dict(change_id=ident, type=kind, statement_id="II:methodology",
        old_location=location, old_page="checkpoint 44 working PDF", new_location=location,
        new_page="final build pending", old_text=old, new_text=new, reason=reason,
        review_status="Compared with the attached continuation prompt sections 0.3 and 4.1 and the complete current methodology. Check totals and deposit fields await the text-final recomputation."))
assert identifiers(before) == identifiers(after)
assert re.findall(r"[0-9a-f]{40}", after) == ["a02f2eacf5a8c3db7cf8cdfcdba50c0002ee91c7"]
SOURCE.write_text(after, newline="\n")
print("Appended", append_rows(ROOT / "S6_SERIES_PUBLISH_defects_II.tsv", rows, "change_id"), "editorial defect rows.")
