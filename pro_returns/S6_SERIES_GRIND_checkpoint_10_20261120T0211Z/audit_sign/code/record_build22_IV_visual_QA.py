import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
data = json.loads((HERE / 'build22_IV_QA_pending.json').read_text())
observations = {
17: 'Pages 145–146: repaired F22/F23 characteristic equations, fractions and proof numbers are readable; Theorem 3.24 heading and uses links fit.',
18: 'Pages 147–148: long code paths wrap; mapping-torus and glued-sphere formulas and Eells–Kuiper fractions fit; Theorems 3.25/3.26 headings and cross-paper links are clear.',
19: 'Pages 1305,1312: K111 Theorem 10.10 actual source/scalar/fan hypotheses, pair (71,-4), native (-1,72) and return 12 are readable; new proof introduction and SI2.42–48 cell list/matrices fit.',
20: 'Pages 1314,1323: full point/O module formulas and localized-exterior/lower graph-scope paragraph are visible; RB33/34 pairings and new NS input heading fit.',
21: 'Pages 1324–1325: protected lower facets, new 54121/31-chart scope, reciprocal NS maps and full point/O factors are readable.',
22: 'Pages 1326,1329: 31-chart derivative NS23/23a, full units and 29-blowdown statement fit; NC header and NC1–3 are clear.',
23: 'Pages 1332–1333: NC17–20 matrices, own-cap equality, bundle bordism and 29-blowup replacement are readable; MN reference heading is clear.',
24: 'Pages 1334–1335: actual own reference, MN15/16 matrices, retained NS17 locator and IL twelve-surface scope are readable. IL beginning retains the publication-format prefix Working proof, 18 November 2026.',
25: 'Pages 1340,1353: IL41 Euler expression, minimal (1,-2) pair, RFB reference (-72,0), new ASI2 counts and long Miller identity fit. RFB introduction retains Working proof, 18 November 2026.',
26: 'Pages 1358–1359: compact/lower/moving totals, ASI2.41, sum (1,4), Jin interval arrow and whole RFB pair are readable. Build22 still contains the RFB.17 diagonal-lift locator; the separately delivered guard changes it to RFB.16.',
27: 'Pages 1362–1363: F41/F46/K96 fixed-scalar path, inverse ODE, physical class 12 and native pair are readable; new proof20 A–B begins clearly with cells, periods, semigroup map and counts.',
28: 'Pages 1364–1365: endpoint period maps, source bands, infinity substitution, original exterior identities, proper-graph scope and point/O torus module maps are fully visible; no formula is cut off at the margins.',
29: 'Pages 1366–1367: physical/second cocharacter table, compact-owner localization formulas, three endpoint matrices, compact sum and moving cap intersection products are readable and within margins.',
30: 'Pages 1368–1369: the corrected 2-by-2 I matrix, lower pair, original outer/fixed-source comparison, sums and signs fit. All code paths in proof20 G wrap within the text area; closing square, return link and K112 heading fit.',
31: 'Pages 1370,1395: K112 native, vertical and all-fan statements and VM2.1–3 fit; later completed-reduction numbered steps and cross-links are readable. VM2 prose retains the historically qualified wording still unevaluated constant S0 although the preceding theorem supplies S0=2.',
32: 'Pages 1396,1434: relocated open problem 12.1 clearly separates original unreconstructed arrays from proved Theorem10.10; preserved alternative begins below the scope statement. Bibliography is readable and uncut; duplicate Engel and Haefliger entries are visible.',
33: 'Page1438: final bibliography entries, long Shioda URL and Verified line fit without clipping; page footer is clear.'
}
for item in data['sheets']:
    number = int(Path(item['path']).stem.rsplit('_', 1)[1])
    actual = hashlib.sha256(Path(item['inspected_copy']).read_bytes()).hexdigest()
    assert actual == item['sha256'], (number, actual, item['sha256'])
    item.update(actually_viewed=True, method='functions tools.view_image with explicit image output',
                layout_result='No clipping, missing glyphs, equation-label collisions or margin overflow observed.',
                observation=observations[number])
data.update(
    recorded_utc=datetime.now(timezone.utc).isoformat(),
    reviewer='GPT-6 Astra (OpenAI), ChatGPT Pro mode, S6_SERIES_GRIND/sign_theorem_audit; same model family as receiving reviewers',
    build='22', paper='IV', pdf_pages=1438,
    scope='All assigned sheets changed_IV_17 through changed_IV_33 were actually viewed; 33 distinct PDF pages. No claim is made for other pages or a later PDF build.',
    total_sheets=17, total_pages=33,
    exposure_receipt='An earlier multi-image call for sheets28–31 was truncated and was not counted. Each of those four sheets was subsequently reopened individually and inspected.',
    overall_layout_result='PASS at the exact inspected page/hash scope.',
    publication_format_observations=[
      {'pages':[1335,1340], 'issue':'Retained Working proof, 18 November 2026. prefixes in active IL/RFB text.'},
      {'pages':[1363,1364,1366,1367,1368,1369], 'issue':'New proof20 uses A–G inner headings; root should compare this with its numeric proof-step formatting requirement.'},
      {'pages':[1370], 'issue':'The relative VM2 paragraph still says still unevaluated constant S0; the preceding theorem now supplies the value2.'},
      {'pages':[1359], 'issue':'RFB.17 to RFB.16 locator repair is already supplied separately and was not yet present in build22.'},
      {'pages':[1434], 'issue':'Duplicate bibliographic entries for Engel and Haefliger are visibly present; bibliographic alias reconciliation is outside this visual pass.'}
    ],
    mathematical_scope='This is a visual verification receipt, not a new mathematical re-proof. Mathematical closure and exact receiving computations remain in the separately named K111 records.',
    shared_sources_modified=False
)
(HERE / 'build22_IV_visual_QA.json').write_text(json.dumps(data, indent=2, ensure_ascii=False)+'\n')
print(json.dumps({'file':str(HERE / 'build22_IV_visual_QA.json'),'sheets':17,'pages':33,'sha256':hashlib.sha256((HERE / 'build22_IV_visual_QA.json').read_bytes()).hexdigest()}))
