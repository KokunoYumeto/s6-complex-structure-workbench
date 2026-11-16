# Complete hourly checkpoint 13

Frozen at 2026-11-16T01:36:14.391405+00:00. The current paper, PDF, report, CSV, bibliography,
source, code, records and current research support are directly readable
under S6_03_CDP/ and research_support/. Exactly 567 duplicate
generated build paths share their byte-identical payload with another
retained path. All paths, bytes, sizes, hashes and file modes of the full
current tree are recorded in history/current_snapshot.json. Reconstruct
that exact full current tree into a new directory with:

    python3 history/restore_current_tree.py /absolute/path/new_current_tree

Every distinct historical file version from the preceding compact package
is retained under its exact content hash. No authored file, proof passage,
code, output, note, log, or earlier packaging record has been omitted.
Unchanged bytes are shared only within the archive representation.

history/current_snapshot.json records the frozen current tree. The legacy
history/snapshots.json and history/restore_snapshot.py reconstruct any
original checkpoint1 through9 byte for byte. The exact compact checkpoint
packages9 through12 are described in history/compact_snapshots.json:

    python3 history/restore_compact_package.py 12 /absolute/path/prior.zip

The restore programs refuse to replace files and verify the exact original
ZIP byte hash. The immediately preceding compact package was reconstructed
in an anonymous temporary file and its byte hash verified during this save.
All older recipes retain their previously verified bytes and ZIP metadata.
No earlier checkpoint was overwritten, renamed or deleted.
