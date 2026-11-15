## Checkpoint retention record

No checkpointed file or passage is discarded. Unchanged files remain at their original paths; every changed version is retained byte for byte below. The current source supersedes its historical counterpart. A prior Open statement may therefore remain in an archived version even when the current numbered statement has been resolved. The original ZIPs are never modified.

| Checkpoint | Previous file | Retained full version | Current replacement |
|---|---|---|---|
| S6_02_PUSH_checkpoint_01.zip | S6_02_PUSH_paper.aux | retained/checkpoint_01/S6_02_PUSH_paper.aux | S6_02_PUSH_paper.aux |
| S6_02_PUSH_checkpoint_01.zip | S6_02_PUSH_paper.log | retained/checkpoint_01/S6_02_PUSH_paper.log | S6_02_PUSH_paper.log |
| S6_02_PUSH_checkpoint_01.zip | S6_02_PUSH_paper.out | retained/checkpoint_01/S6_02_PUSH_paper.out | S6_02_PUSH_paper.out |
| S6_02_PUSH_checkpoint_01.zip | S6_02_PUSH_paper.tex | retained/checkpoint_01/S6_02_PUSH_paper.tex | S6_02_PUSH_paper.tex |
| S6_02_PUSH_checkpoint_01.zip | S6_02_PUSH_paper.toc | retained/checkpoint_01/S6_02_PUSH_paper.toc | S6_02_PUSH_paper.toc |
| S6_02_PUSH_checkpoint_01.zip | S6_02_PUSH_references.bib | retained/checkpoint_01/S6_02_PUSH_references.bib | S6_02_PUSH_references.bib |
| S6_02_PUSH_checkpoint_01.zip | S6_02_PUSH_report.md | retained/checkpoint_01/S6_02_PUSH_report.md | S6_02_PUSH_report.md |
| S6_02_PUSH_checkpoint_01.zip | S6_02_PUSH_results.csv | retained/checkpoint_01/S6_02_PUSH_results.csv | S6_02_PUSH_results.csv |
| S6_02_PUSH_checkpoint_01.zip | code/ab_push_catalogue.out | retained/checkpoint_01/code/ab_push_catalogue.out | code/ab_push_catalogue.out |
| S6_02_PUSH_checkpoint_01.zip | code/ab_push_catalogue.py | retained/checkpoint_01/code/ab_push_catalogue.py | code/ab_push_catalogue.py |
| S6_02_PUSH_checkpoint_01.zip | code/assemble_records.out | retained/checkpoint_01/code/assemble_records.out | code/assemble_records.out |
| S6_02_PUSH_checkpoint_01.zip | code/assemble_records.py | retained/checkpoint_01/code/assemble_records.py | code/assemble_records.py |
| S6_02_PUSH_checkpoint_01.zip | code/assembly_summary.json | retained/checkpoint_01/code/assembly_summary.json | code/assembly_summary.json |
| S6_02_PUSH_checkpoint_01.zip | code/build_paper.py | retained/checkpoint_01/code/build_paper.py | code/build_paper.py |
| S6_02_PUSH_checkpoint_01.zip | code/d_push_equianharmonic.out | retained/checkpoint_01/code/d_push_equianharmonic.out | code/d_push_equianharmonic.out |
| S6_02_PUSH_checkpoint_01.zip | code/d_push_equianharmonic.py | retained/checkpoint_01/code/d_push_equianharmonic.py | code/d_push_equianharmonic.py |
| S6_02_PUSH_checkpoint_01.zip | code/d_push_registry.out | retained/checkpoint_01/code/d_push_registry.out | code/d_push_registry.out |
| S6_02_PUSH_checkpoint_01.zip | code/d_push_registry.py | retained/checkpoint_01/code/d_push_registry.py | code/d_push_registry.py |
| S6_02_PUSH_checkpoint_01.zip | code/package_checkpoint_01.out | retained/checkpoint_01/code/package_checkpoint_01.out | code/package_checkpoint_01.out |
| S6_02_PUSH_checkpoint_01.zip | code/refresh_report.out | retained/checkpoint_01/code/refresh_report.out | code/refresh_report.out |
| S6_02_PUSH_checkpoint_01.zip | code/refresh_report.py | retained/checkpoint_01/code/refresh_report.py | code/refresh_report.py |
| S6_02_PUSH_checkpoint_01.zip | evidence/ab_push_search_log.md | retained/checkpoint_01/evidence/ab_push_search_log.md | evidence/ab_push_search_log.md |
| S6_02_PUSH_checkpoint_01.zip | sections/AB_push.tex | retained/checkpoint_01/sections/AB_push.tex | sections/AB_push.tex |
| S6_02_PUSH_checkpoint_01.zip | sections/AB_push_references.bib | retained/checkpoint_01/sections/AB_push_references.bib | sections/AB_push_references.bib |
| S6_02_PUSH_checkpoint_01.zip | sections/AB_push_report.md | retained/checkpoint_01/sections/AB_push_report.md | sections/AB_push_report.md |
| S6_02_PUSH_checkpoint_01.zip | sections/AB_push_results.csv | retained/checkpoint_01/sections/AB_push_results.csv | sections/AB_push_results.csv |
| S6_02_PUSH_checkpoint_01.zip | sections/C_push.tex | retained/checkpoint_01/sections/C_push.tex | sections/C_push.tex |
| S6_02_PUSH_checkpoint_01.zip | sections/C_push_report.md | retained/checkpoint_01/sections/C_push_report.md | sections/C_push_report.md |
| S6_02_PUSH_checkpoint_01.zip | sections/D_push.tex | retained/checkpoint_01/sections/D_push.tex | sections/D_push.tex |
| S6_02_PUSH_checkpoint_01.zip | sections/D_push_references.bib | retained/checkpoint_01/sections/D_push_references.bib | sections/D_push_references.bib |
| S6_02_PUSH_checkpoint_01.zip | sections/D_push_report.md | retained/checkpoint_01/sections/D_push_report.md | sections/D_push_report.md |
| S6_02_PUSH_checkpoint_01.zip | sections/D_push_results.csv | retained/checkpoint_01/sections/D_push_results.csv | sections/D_push_results.csv |
| S6_02_PUSH_checkpoint_01.zip | sections/D_referee_AB_C.md | retained/checkpoint_01/sections/D_referee_AB_C.md | sections/D_referee_AB_C.md |
| S6_02_PUSH_checkpoint_01.zip | sections/D_referee_references.bib | retained/checkpoint_01/sections/D_referee_references.bib | sections/D_referee_references.bib |
| S6_02_PUSH_checkpoint_01.zip | sections/E_push_report.md | retained/checkpoint_01/sections/E_push_report.md | sections/E_push_report.md |
| S6_02_PUSH_checkpoint_01.zip | sections/conventions_push.tex | retained/checkpoint_01/sections/conventions_push.tex | sections/conventions_push.tex |

Exact byte counts and SHA256 digests are in code/retention_record.json.
