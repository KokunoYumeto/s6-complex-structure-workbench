"""Write the completed outcome table, final audits, and full dated journal."""
from pathlib import Path
from datetime import datetime, timezone
import collections
import csv
import hashlib
import json
import re
import shutil
import fitz

root = Path(__file__).resolve().parents[1]
stamp = datetime.now(timezone.utc).isoformat()
report = root/'S6_03_CDP_report.md'
old_report = report.read_text()
prior = root/'records/versions/report_before_completion_20261116.md'
assert not prior.exists()
shutil.copy2(report, prior)

rows = list(csv.DictReader((root/'S6_03_CDP_results.csv').open()))
ids = [row['id'] for row in rows]
ordered = '\n'.join(p.read_text() for p in (root/'build/ordered').glob('*.tex'))
numbered = re.findall(r'\\begin\{(?:statement|idstatement)\}\{([^}]+)\}', ordered)
assert len(ids) == len(set(ids)) == len(numbered) == 239
assert set(ids) == set(numbered)
assert all(row['status'].startswith(('Proved','Refuted','Known')) for row in rows)
tag_counts = collections.Counter(re.findall(r'\\tag\{([^}]+)\}', ordered))
assert not [tag for tag,count in tag_counts.items() if count > 1]
pdf_path = root/'S6_03_CDP_paper.pdf'
pdf = fitz.open(pdf_path)
pdf_hash = hashlib.sha256(pdf_path.read_bytes()).hexdigest()
qa = json.loads((root/'build/visual_qa/manifest.json').read_text())
inspection = json.loads((root/'records/root_final_visual_inspection.json').read_text())
assert qa['pdf_pages'] == len(pdf)
assert inspection['pdf_sha256'] == pdf_hash
assert set(inspection['pages']) <= set(qa['rendered_pages'])
build_log = (root/'build/root_build_0129.out').read_text()
for needed in ['pass 1: exit 0','pass 2: exit 0','pass 3: exit 0','pass 4: exit 0',
               'TeX errors: 0','Overfull boxes: 0','Unresolved reference warnings: 0',
               'Missing glyph warnings: 0']:
    assert needed in build_log

prefixes = {
 'A.1':'(a) Proved. ', 'A.2':'(a) Proved, with exact countermodels to the invalid shortcuts. ',
 'A.3':'(b) The support-only inference is refuted; (a) the complete full-fibre replacement is proved. ',
 'A.4':'(a) Proposition7.3 is proved; (b) its stated genus inference is refuted. ',
 'A.5':'(a) Proved in the required geometric and singularity scopes. ',
 'B.1':'(b) Complete counterexample and computed replacement. ',
 'B.2':'(b) Complete compact counterexample. ', 'B.3':'(a) Proved. ',
 'C.1':'(a) Proved. ', 'C.3':'(a) Complete surviving-type classification and occurrence. ',
 'C.4':'(b) The unconditional assertion is refuted; (a) the exact geometric replacement is proved. ',
 'C.5':'(b) The proposed all-twist surjection is refuted; (a) all groups and actual map ranks are computed. ',
 'D.1':'(b) The printed monodromy-free statements are refuted; (a) the corrected forms are proved. ',
 'D.2':'(a) Existence and the exact zero theorem are proved. ',
 'E.1':'(a) Proved and applied to every named family. ',
 'E.2':'(a) The nonholomorphic-reduction theorem is proved; (b) the overgeneral auxiliary assertion is refuted. ',
 'E.3':'(a) Proved for every requested family and its small deformations. ',
 'E.4':'(b) The overgeneral fixed-target and theta claims are refuted; (a) the required P1 stability and exact family calculations are proved. '
}
table = ['| Item | Numbered statements | Outcome |','|---|---|---|']
for line in old_report.splitlines():
    if not re.match(r'^\| [A-E]\.\d+ \|',line):
        continue
    _, item, statements, outcome, _ = [part.strip() for part in line.split('|')]
    if item == 'C.2':
        statements = ('C2a–C2d; C.2.NC.1–5; C.2.VII.1–4; C.2.INT.1–3; '
                      'C.2.RAT.1–9; C.2.IRR.1; C.2.D4.1–3; C.2.CR.1–6; '
                      'C.2.MH.1–4; C.2.G.1; C.2.UN.1–86; A.5.18–21')
        outcome = ('(b) Unrestricted nonnegativity is refuted by complete compact examples; '
                   '(a) the exact Euler range is 2Z, the rank-two values and all irreducible zero cases '
                   'are computed, and UN85–86 give exhaustive finite geometric generation of every '
                   'reducible zero-Euler support, including arbitrary original singularities and full '
                   'multiplicities. The construction starts from classified torus, marked cycle, '
                   'periodic toric, or elliptic-network cores and retains the actual analytic atlas, '
                   'inverse modifications, finite action, toric coarsening and smooth contractions. '
                   'The independent converse constructs each output. Zero is exactly the proved '
                   'signed Euler balance. Under all integral CDP hypotheses every fibre Euler number '
                   'is nonnegative, c3 is 0 or2, and equality has the complete geometric description. '
                   'The compact construction and the intrinsic normal-root/H−tau branch comparison '
                   'are proved. This resolves the final unrestricted clause.')
    else:
        outcome = prefixes[item] + outcome
    table.append(f'| {item} | {statements} | {outcome} |')
assert len(table) == 21

front = f'''COMPLETE

{chr(10).join(table)}

# S6_03_CDP completed research report

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode),15–16November2026.
The run began at approximately12:36UTC on15November. This completed
report was recorded at {stamp}. No priority is claimed. All19 Parts
and all9 Leads are answered by the239 numbered statements. A complete
counterexample is accompanied by its computed or proved replacement.

## The final unrestricted zero-Euler classification

Statements C.2.UN.85–86 close the last outstanding clause. They provide
a finite geometric construction with both directions proved. Every
smooth-total torus degeneration, with any original singular support and
any full multiplicities, is recovered from one of four actual core
types: a smooth two-torus; a canonical-flat marked elliptic-ruled/Hopf
cycle; a positive periodic toric log core; or the exact rooted-tree or
unicyclic elliptic-quasi-bundle/Hopf supports of UN61–62.

The construction data contain the actual core neighbourhood, its finite
analytic atlas, every inverse sigma map and restored overlap, a finite
cyclic action regular after the inverse record, the labelled normalized
toric coarsening, invariant smooth quotient coordinates, and the ordinary
smooth point/curve contraction maps. These data are supplied independently
in the converse. The resulting maps directly prove properness, flatness,
connected fibres, smooth total space and torus general fibres. The
necessity proof produces this data from every original family.

The canonical-flat and positive-Hopf branches are chosen intrinsically.
For each original normalized component, use its actual finite normal-root
cover. Let tau be the integrability threshold of the canonical density
divided by the fibre-function power, and H the maximum original canonical
ratio over the covers with Hopf minimal model. On every divisible
semistable root the highest Hopf order is exactly N(H-tau). The exact
local root map, the Jacobian comparison and the exclusion of exceptional
Hopf covers prove independence from resolution and root exponent.

For the output support S and core support S*, the proved formula is

    e(S) = e(S*) - Delta_sigma - R_N - Delta_pi.

Here Delta_sigma is the signed normal-cone defect of the actual forward
modification record; Delta_pi is twice the number of ordinary point
centres plus the sum of2-2g over its curve centres; and

    R_N = sum_I (N^(|I|-1) gcd(m_i:i in I)^2 / product(m_i:i in I) - 1)
                    * e_c(D_I^open).

The exact zero class consists of these construction records with
Delta_sigma+R_N+Delta_pi=e(S*). The core value is zero in the torus,
cycle and elliptic-network cases, and2[N0:Gamma0] for the positive toric
core. Thus the classification gives actual spaces and comparison maps
in addition to an Euler test. It retains all analytic data needed to
reverse the specified operations. Uniqueness of a reduction record and
identification of arbitrary smoothing germs from central log parameters
are not asserted or used.

The compact proof chooses a global meromorphic base function with a
prescribed first jet at the selected value and nonzero prescribed values
at every other critical value. Serre duality and the exact restriction
sequence give that choice. Every additional branch value lies over a
smooth fibre; the normalized base change is smooth elsewhere. The local
unit map is displayed explicitly. Consequently the same finite
construction and its converse apply to compact total threefolds over
compact curves.

## How the last reduction terminates

UN84 stops the actual Kulikov selection at the highest positive Hopf
order. Its proof uses the current-maximal ruledness identified in the
primary1981 proof; the removed component can have lower order, so the
termination vector includes every positive order. UN77 and82 then make
a surviving maximal Hopf an embedded minimal leaf with torsion-normal
elliptic interface.

UN80 proves that every exceptional prime of the specified aligned
elliptic surface map is an actual boundary. Its constant-period ambient
field cannot lift regularly at a point-exceptional prime, by the exact
two-coordinate valuation calculation. UN81 therefore handles every last
point defect by actual two-ruling, ruled-removal or plane-progress maps.
UN83 extends the interface comparison to every canonical coefficient,
using actual finite etale covers, Stein pencils, finite trace and the
retained possibly nonsplit ruled extension.

UN85 records these actual surface maps while traversing the connected
support. Its finite potential is the full positive-order component-count
vector, then the number of unrecognized components, then the total
recorded point defect. A direct move lowers the last entry; recording a
new actual interface lowers the preceding entry; a completed removal
lowers the first changed component count and permits a finite restart
of the other data. The chosen maximal Hopf neighbourhood is preserved.
The explicit NC image-curve argument uses coprime adjacent shifted
canonical coefficients, including coefficient-zero full-fibre curves.
It handles all one-,two- and three-source triple patterns and the
same-global-component defect drop of two.

At the endpoint all boundaries are isolated smooth elliptic curves and
all components are embedded and minimal. The actual normal-root maps
identify the quasi-bundle Jacobians. A geometric-genus-one component
surjects onto the support fundamental group, while the graph quotient
kills that image, forcing a tree. The remaining case is the exact
unicyclic class. The complete torsors, finite characters, translations
and gluing maps are retained.

## Leads and their precise outcomes

| Lead | Answering statements | Outcome |
|---|---|---|
|1|A.1.1–2; A.2.1–6|The canonical conormal filtration and inverse-Jacobian comparison are proved, with exact NC and non-NC maps.|
|2|B1–B3|The nodal inference is refuted; every gluing scalar and the compact replacement are computed.|
|3|A.4.1–9; A.5.1–21|The actual normality, torsion-free vanishing and normalization-pullback issues are resolved with their exact scopes.|
|4|C.1.1–3; C5a–C5c|The index and generic endpoint vanishings are proved, and all-twist nonvanishing is computed.|
|5|C2a; C.2.G.1; C.2.UN.1–86|Euler localization, the unrestricted counterexamples, the complete zero class and the CDP sign/equality theorem are proved.|
|6|D.1.1–15; D.2.1–8|The coinvariant count and all corrected monodromy-dependent statements are proved, with compact counterexamples and a trivial-monodromy example.|
|7|E1; E7|Verticality and meromorphic descent are proved and applied to every requested family.|
|8|C5a–C5c|The normal quotient is computed; the proposed universal surjection has explicit exceptional twists, while the actual groups and map ranks are determined.|
|9|E4–E8; E10; E16; E18|All-orders stability over P1 and the requested family rank calculations are proved; the overgeneral fixed-target and theta statements have complete counterexamples.|

## Source comparison and corrections

The supplied original manuscripts, their AI transcriptions, the
workbench, course, survey, S6_01 and S6_02 returns and the prior review
were treated as claims to check. The exact sources and used steps are
recorded in the proofs and in A_notes,D_notes,E_notes and the source-
specific root audits. The dated journal below retains the complete
development and corrections, including intermediate attempts that were
later superseded by the stated maps.

The CDP ambient-cotangent inference is replaced by the typed conormal,
torsion and connecting maps; the missing normalization contribution and
the extra cusp quotient are computed. Nonreduced fibres are treated by
their complete lifting filtrations. Proposition7.3 is proved in its
stated scope, while its printed genus inference is refuted. The
monodromy-free H1 count is replaced by the exact coinvariant sequence;
the coherent restriction, direct-image splitting and generic
non-torsion statements are repaired in their actual generality.

The workbench's asserted strongest replacement is superseded by the
proved geometric criterion of C4f and the complete fibre sign/equality
theorem. The compact local counterexample has all its cohomology
computed and its exact failure of global CDP hypotheses recorded.
The integral-versus-rational homology distinction in the Wang example
is proved through the universal coefficient sequence. The actual
signed AC/Engel lattice and affine-twist dictionary is retained.

For the standard family, the all-Picard tangent computation and its
normalization map are exact. At the twist n=-1 the tangent tuple is
(0,0,1,0) and the normalization map has rank zero, giving the explicit
exception to the proposed all-twist surjection. The general H2
nonvanishing is nevertheless proved. The S6_01 jump and stalk claims,
the S6_02 steps used, the nonholomorphic-reduction proof, the named
Kuranishi families and the exact Kodaira--Spencer rank loci are checked
in their numbered statements. The universal theta square requires the
additional Weierstrass term; the original marked-section formula is
proved in its exact scope.

The DGKX claims are attributed to version1, and version2's omission is
recorded without an explanation being inferred. The primary
Kulikov1977/1981 definitions, selection, overlap restoration, finite
component game and corrections were read and compared with the exact
maps used here. Recent and attached primary literature, its references,
and targeted searches are logged in the individual records. Every
bibliographic entry carries its verification status. No priority is
claimed for the independently derived extensions.

## Final independent executions and audits

UN79–84 have complete root and agent written-source audits, with their
independent outputs in build/root_UN79_code_rerun.out through
build/root_UN84_code_rerun.out. UN85 and86 each have complete root,A,E,D
written-source audits and independent executions by the reviewing
agents. The final root UN85 run passes129925 shifted-edge checks,
248040 removal/reset comparisons and60 complete records with39441
steps. The final UN86 run passes24486 canonical quotient comparisons,
166782 intrinsic/root-scaling cases,61930 invariant-monoid comparisons,
258 root-stratum calculations and6336 zero-balance reconstructions.
Their written inductions and actual analytic maps establish the
theorems; the finite exact programs verify the stated identities.

One rejected auxiliary bound n<=b-1 is preserved with its exact node
counterexample; the proof uses n<=b+1. UN79's explicit compact horizontal
(-1,-2) germ is retained and reconciled with UN80 through the specified
surface morphism. Every superseded source, failed layout passage and
earlier report remains recoverable. The equation namespaces C.SK and
C.G were repaired to C.SKD and C.VC where needed, with full pre-repair
sources retained. The catalogue now has one unique row for each of the
239 compiled statements, with exact ID-set equality verified by this
script and no duplicate equation tags.

## Final typesetting and actual visual inspection

The final build is build/root_build_0129.out. All four stages returned
zero. Its log has0 TeX errors,0 overfull boxes,0 overflows above2pt,
0 unresolved references and0 missing glyphs. Earlier failures and their
original passages are retained; the last previously detected display
overflow,32.09746pt in C.WF.13, was repaired by splitting the same
definitions over two lines and then rebuilt cleanly.

The final PDF has {len(pdf)} pages and239 numbered statements. Its
SHA256 is {pdf_hash}. The current visual manifest records
{len(qa['rendered_pages'])} actually rendered pages. Root actually
inspected final pages {','.join(map(str,inspection['pages']))}; the
record includes this exact PDF hash. These are fresh images of the
final PDF. The prior489-page image tree was preserved before rendering,
and stale images were removed from the current directory only after
their preserved copies had been byte-checked.

## Thirteen-hour review and final checkpoint

Decision: completed. The work since the twelfth-hour review closed the
remaining main question through the fully audited UN79–86 chain, with
UN85–86 proving the unrestricted finite construction and its converse.
All requested mathematical items now have the outcomes in the opening
table. The scheduled01:36UTC checkpoint13 is the complete final package;
no intervening ZIP has been created.

The package retains the full current deliverable, code, outputs, notes,
audits, logs and every historical byte version. Its included programs
restore the exact previous checkpoint archives. Duplicate generated
build paths share verified identical payloads, and the complete current
tree is reconstructed by history/restore_current_tree.py. That restorer
was tested on all2021 files of checkpoint12, with every output hash
checked; alias, mode, timestamp, corruption and overwrite checks passed.
The immediately preceding archive is reconstructed and its exact byte
hash checked during the final save. No earlier checkpoint is changed.

## Dated working journal and resolution of its intermediate status

The following journal is preserved verbatim from the prior report's
research-record body. Its references to work still remaining describe
the recorded intermediate states. The complete current outcomes are
the table above and Statements C.2.UN.85–86, whose actual maps resolve
that final unrestricted clause. The entire prior report, including its
original opening table and status, is separately retained at
records/versions/report_before_completion_20261116.md.

'''
journal = old_report.split('# S6_03_CDP research record\n',1)[1]
report.write_text(front+journal)
summary = {'recorded_utc':stamp,'status':'COMPLETE','statements':len(ids),
           'pdf_pages':len(pdf),'pdf_sha256':pdf_hash,
           'rendered_pages':len(qa['rendered_pages']),
           'actually_inspected_pages':inspection['pages'],
           'equation_tags':len(tag_counts),'duplicate_equation_tags':0,
           'build_log':'build/root_build_0129.out'}
(root/'records/root_completion_manifest.json').write_text(json.dumps(summary,indent=2)+'\n')
(root/'records/root_review13.md').write_text(
    f'# Thirteen-hour review — {stamp}\n\nDecision: COMPLETE.\n\n'
    'UN85--86 close the unrestricted geometric generation and exact zero-Euler class. '
    'Every requested Part and Lead has a proved or refuted outcome with its replacement. '
    'The full report contains the exact scope, source audits and executed checks.\n\n'
    +json.dumps(summary,indent=2)+'\n\nOne final checkpoint13 is due01:36UTC; '
    'no ZIP was created by this review script.\n')
with (root/'records/progress_reviews.md').open('a') as stream:
    stream.write('\n\n'+(root/'records/root_review13.md').read_text())
print(json.dumps(summary,indent=2))
print('Complete report, full prior journal and final review written; no ZIP created.')
