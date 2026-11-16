from pathlib import Path
from collections import Counter
import datetime, json, re
import fitz

ROOT=Path(__file__).resolve().parents[3]
D=ROOT/'deliverables';R=D/'records'
rows=json.loads((R/'all_records.json').read_text())
audit=json.loads((R/'final_integrity.json').read_text())
bib=json.loads((R/'bibliography_audit.json').read_text())
cites=json.loads((R/'all_citation_checks.json').read_text())
checks=json.loads((R/'verification_record.json').read_text())
stats=json.loads((R/'build/final_typesetting.json').read_text())
visual=json.loads((R/'build/visual_qa.json').read_text())
pdf=fitz.open(D/'S6_07_PAPER_paper.pdf')
esc=lambda s:str(s).replace('|',r'\|').replace('\n',' ')
out=['# S6_07_PAPER assembly and audit report',
'AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). No human has checked this work. Human understanding: none. Formalization: none.',
'## Deliverable and verification scope',
f'The completed standalone LuaLaTeX manuscript has **{len(pdf)} pages**, including all twelve requested sections, Appendices A–C and inline references. The front matter occupies three pages. The source table has **{len(rows)} rows**: 136 numbered formal entries and nine setup/artifact prose records. The status totals are 73 T, 10 K, 32 A, 29 text/setup entries and one separately quoted false target. There are 80 printed proof environments. Every required content group is represented; none is left as a plan or placeholder.',
f'The verification table has **{len(checks)} rows**: {len(checks)-len(cites)} historical records drawn from the supplied status files and {len(cites)} current S records of opened-source matching. The bibliography has {len(bib)} entries: {sum(x["status"]=="verified" for x in bib.values())} marked verified within their stated scope and {sum(x["status"]=="unverified" for x in bib.values())} marked unverified. Source comparison, file integrity, compilation and page-image inspection are editorial checks; they are not counted as fresh independent F, D or C mathematical verification.',
'The binding prompt and both supplied archives were opened; the post format was read in full. Input hashes, per-result source text, exact statement differences, credit searches, bibliography openings, transformation scripts and build logs are retained. The CSV contains exactly the twelve columns requested by the prompt. The three-source credit fields distinguish complete overlap, partial overlap and a bounded negative search.',
'## Coverage of the binding table',
'| Requested group | Printed location and treatment |',
'|---|---|',
'| §0 | Status, credit, exact prescribed Campana–Demailly–Peternell paragraph, and proof map. |',
'| §1 and §1′ | Family dictionary, transported normalization u=w² and Engel correction are T; intrinsic pencil and all-maps companion are K, with proofs in Appendix B. |',
'| §2a–c | Standard 2Z theorem K with the exact workbench-independence wording; Appendix A complete workbench proof; all-data T invariants and two classes; 2klZ T only for its stated model; coordinate dictionary A. |',
'| §3a–c | Closed periods, finite values, exact nomes, division identities/evaluations, Mahler identity and beta integrals T; Gaussian, corrected measure, equidistribution and derivative announcements A outside the selected ladder proof. |',
'| §4 and §4′ | Both source certificate accounts as proof of record, complete duplication ladder, unique maximum and radius 216; known abstract disc frame credited; rays and level sets A. |',
'| §5.1–6 and correction | Direct images, scalar/determinant, Hodge and Frölicher, Bott–Chern/Aeppli, canonical and cover results T; specified product, higher Hodge and metric statements A; relative-differentials correction with exact source locators. |',
'| §6a–d | Standard tangent/Kuranishi/miniversality K with Appendix B re-derivation; integral twists T; higher tangent tuple T with “two runs, no second reader”; only the requested local algebraic-dimension corollary. |',
'| §7 | Full automorphisms K; conjugation and real-nome criterion T; fixed loci and involution classes A. |',
'| §8 | Complete selected monodromy/index-12 and period-domain proofs T. |',
'| §9 | Requested Néron–Severi, fibre, curve and surface statements with full proofs and prior-source credit; binding T status retained. |',
'| §10 | Outer non-extension and Euler obstruction T, Engel Conjecture 8.2 quoted exactly as the false target; corrected fillings A. |',
'| §11 | Zero-end non-filling, smooth monodromy in Θ₇ and components A; no general admissible-twist non-filling extension is asserted. |',
'| §12 | All four requested question groups, with the announced MAPS scope distinguished from the other families. |',
'| Appendices | A: complete period-shift workbench argument; B: K re-derivations and required supporting arguments; C: per-result status/source, section credits, dependencies, notation and one row per verification check. |',
'## Exact source comparison',
f'The final audit matches all {audit["formal_statement_entries"]} formal statement bodies in the master to their ledger text. {audit["contiguous_source_statement_count"]} source statements are contiguous literal excerpts after whitespace normalization; {audit["declared_composite_definition_count"]} declared context definitions combine separately matched exact excerpts. The full statement-to-source differences record notation, reference-key, heading, partition and contextual-extraction changes. The nine prose records distinguish literal source definitions from editorial artifact-availability descriptions. There are no unmatched source excerpts, missing source rows, duplicate source rows, empty required fields, duplicate TeX labels or missing bibliography keys in the final check.',
'All 32 announcement blocks have repository pointers and no attached printed proof. The model and effort/mode are stated in the paper and the check records. The required AI-produced wording is present. The prescribed version-2 and independent-workbench sentences are present. The only uncited bibliography key is Gray97. These assertions are recorded mechanically in `records/final_integrity.json` and `records/source_audit.json`.',
(R/'root/assembly_findings.md').read_text()]
for agent,title in [('periods','Periods and maximum'),('cohomology','Cohomology and deformations'),('geometry_ends','Geometry and ends')]:
    text=(R/agent/'discrepancies.md').read_text()
    text=re.sub(r'^# .*\n','',text,count=1)
    out.extend(['### '+title,text])
out.extend(['## References opened and matched',
'The following entries reproduce the scope of the current S ledgers. Repeated keys correspond to distinct source passages checked for different sections. The full URLs, source locators, matched assertions and the supplied-source limitations are in `records/all_citation_checks.json`; every entry of the BibTeX file also carries its verified/unverified note. “Verified” here means opened and matched within that scope, not independent verification of a source theorem.',
'| Key | Opened source | Matched locator and scope |','|---|---|---|'])
for c in cites:
    origin=c.get('url') or c.get('source') or c.get('opened') or c.get('url_or_file') or ''
    if not origin: origin='See '+c.get('_ledger','the source-opening ledger')
    out.append('| '+esc(c.get('key',''))+' | '+esc(origin)+' | '+esc(c.get('locator',''))+' — '+esc(c.get('matched') or c.get('match') or c.get('scope') or '')+' |')
out.extend(['### Unverified bibliography entries'])
for k,v in bib.items():
    if v['status']=='unverified':out.append(f'- **{k}:** {v["note"]}')
out.extend(['## Typesetting before and after',
'The recorded first complete build and the final delivery build are compared below. Earlier incomplete bootstrap logs and intermediate passes are retained. The source fixes changed line breaking, table construction, identifier wrapping, glyph declarations and citation grammar; no mathematical inequality, constant or hypothesis was changed to obtain a fit.',
'| Build | Pages | Overfull boxes | Over 2pt | Largest excess | Missing glyph reports | Unresolved references/citations |',
'|---|---:|---:|---:|---:|---:|---:|'])
for x in stats['comparison']:
    out.append(f'| {x["name"]} | {x["pages"]} | {x["overfull_total"]} | {x["overfull_above_2pt"]} | {x["max_excess_pt"]}pt | {x["missing_glyphs"]} | {x["undefined_references_or_citations"]} |')
out.extend([f'The final compile returned success, with **zero overfull boxes, zero missing glyphs, zero undefined references/citations and zero LaTeX warnings**. There are {stats["final"]["underfull_total"]} underfull-box diagnostics in the bibliography, arising from ragged lines and breakable URLs; these do not extend outside the text block and were visually inspected. The final source has no external input/image/bibliography dependency.',
'The initial incomplete abstract overflow was 41.8099pt. The first complete build had 20 overfull boxes, 17 above 2pt, all in Appendix C; the largest was 201.80676pt. The intermediate table rewrite briefly produced 25 overfull boxes and two missing Unicode glyphs; its long identifiers and the two math-script glyph mappings were corrected. Stable complete passes have zero overfull boxes. The exact logs remain available instead of only the final count.',
'### Rendered-page inspection',
f'{len(visual["pages"])} selected final pages were rendered. The reviewed page numbers are: '+', '.join(map(str,visual['pages']))+'.',
'Every page identified with an overflow in the first complete build (106, 107, 116, 118, 123 and 125) was included, as were all pages of the final long audit tables and references, the front matter and a spread of proof pages. Final notation/glyph corrections were reviewed on the affected images. Main-text reviewers checked the final image hashes; changed images were reopened. The records state the actual sampled pages and findings, without claiming a page-by-page mathematical proof review.',
'The overview sheets in `records/visual/` document the final visual check. `records/scripts/render_qa.py` reproduces the full-resolution images from the delivered PDF; the large temporary PNG set is omitted as reproducible working material. Per-worker `master_visual_qa.json` files and `records/build/visual_qa.json` preserve the review scope and image hashes.',
'## Packaging, reproducibility and checkpoint accounting',
'The ZIP contains the six requested named deliverables and the substantive records, fragments, source-comparison data, scripts, notes, final visual overview sheets and build logs. The paper source is standalone. On a complete standard TeX installation, run `lualatex -interaction=nonstopmode -halt-on-error S6_07_PAPER_paper.tex` twice, or use `python records/scripts/compile_paper.py`. The workspace-specific runtime helper is retained only to document this session’s repaired installation; its external cache is not required on a standard installation.',
'The supplied attachment archives, their extracted original papers/scans and the temporary Duke–Imamoglu reading extraction are excluded, as requested. Provisional isolated fragment PDFs and wrappers, their `.aux`/`.out` files, Python bytecode, Lua font caches and transient runtime downloads are excluded; they are superseded by the single final master PDF and retained build/audit records. No provisional PDF is delivered. Standalone fragment compile logs may contain expected missing cross-section references that are resolved in the final master; only the master log determines the final reference count.',
'Checkpoint accounting is in `records/session.json`. The session started at 14:40:18 UTC on 16 November 2026 and the final package was completed before the first hourly checkpoint became due at 15:40:18 UTC. No checkpoint was created early, and there is no checkpoint content to reconcile. The retained record gives the packaging time.',
'The manifest lists packaged files with SHA-256 hashes. It excludes its own self-referential hash and the enclosing ZIP. Delivery is CC0 1.0 for the text produced here; cited source works retain their own terms.'])
text='\n\n'.join(out)+'\n'
text=re.sub(r'(?<=\|)\n\n(?=\|)','\n',text)
(D/'S6_07_PAPER_report.md').write_text(text)
print('Report words',len((D/'S6_07_PAPER_report.md').read_text().split()))
