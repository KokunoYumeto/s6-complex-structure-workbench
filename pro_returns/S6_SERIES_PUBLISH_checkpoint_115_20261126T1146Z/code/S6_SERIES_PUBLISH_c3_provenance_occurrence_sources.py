#!/usr/bin/env python3
"""Record bounded primary readings for UN6/P328 and the Kummer input to UN13."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'agents/continuation3_provenance/final_sources'
now = datetime.now(timezone.utc).isoformat()

def write(name, rows):
    with (OUT / name).open('w', newline='') as f:
        w = csv.DictWriter(f, list(rows[0]), delimiter='\t', lineterminator='\n')
        w.writeheader()
        w.writerows(rows)

write('S6_SERIES_PUBLISH_fujimoto_sources.tsv', [dict(
    source_key='Fujimoto1988Log',
    url='https://doi.org/10.1215/kjm/1250520560',
    version='Published journal facsimile, J.Math.Kyoto Univ.28(1),91-110,1988; accessed through https://scispace.com/pdf/logarithmic-transformations-on-elliptic-fiber-spaces-1uinrvp8jj.pdf',
    locus_read='Complete notation/convention definition pp.91-92; Theorem2.1 and proof, Corollaries2.2-2.3 and Remarks2.5-2.6 pp.94-96; complete Theorem2.8 statement/proof and Lemma2.9 p.96; complete Corollary2.10 statement/proof pp.96-97; complete Example3.1 construction pp.97-99 and Example3.4(1) p.99',
    sha256='', bytes='',
    own_paraphrase='The definition requires a proper surjective holomorphic map of complex manifolds, connected fibres and a smooth general elliptic fibre. Theorem2.8 asserts a cyclic quotient of the complement fundamental group and divisibility of the boundary self-intersection by the multiplicity. Corollary2.10 asserts divisibility of the degree for a smooth plane boundary in the constant-modulus case. Example3.4(1) applies the earlier logarithmic construction to a twisted product of elliptic curves; the torsion choice gives an abelian general fibre and a component of Kodaira dimension one.',
    exact_application='P328 has the actual map [a,b,c] to [a^m:b:c], fixed general fibre C*/q^Z, connected reduced boundary fibre C*/(q^m)^Z, pullback of the line equal to m times its reduced preimage, and affine complement C^2. It meets the printed analytic definition and the constant-modulus/smooth-complement premises. The cover used on p.96 is xi^m=s_E^m in O_X(E); its normalization map is the disjoint union of the global graphs x to (x,zeta s_E(x)). Each graph maps identically to X, so its Stein factor over the base is a disjoint copy of the base. For the UN6 credit, take zero twisting in Example3.4(1) and the same two elliptic factors; the source and UN6 have the same punctured product through their displayed complement trivializations.',
    read_extent='The specified primary mathematical text was opened and read through the web tool in the 20-page journal facsimile. The original complete UN6 statement/proof and the complete following counterexample/cover paragraph were read. The source screenshot requests returned text placeholders rather than image bytes, so no visual page reading is claimed. Direct Project Euclid retrieval served a security-check HTML page; direct mirror retrieval served an empty HTTP202 challenge. The tools exposed no PDF bytes, so the PDF byte count and SHA256 are intentionally left empty. No hash of a challenge page or of extracted text is substituted. Bibliographic journal/title/pages/DOI agree with the facsimile and primary Crossref record. No further bibliography edit is needed.',
    date_utc=now)])

pdf = ROOT.parents[1] / 'tmp/c3_provenance_primary/Huybrechts_K3Global_fresh.pdf'
b = pdf.read_bytes()
sha = hashlib.sha256(b).hexdigest()
assert len(b) == 3256284
assert sha == '59da72d5807fd05d08ce28ceaf30a030cfc7e52b92e27778d824ac86cb1dd287'
write('S6_SERIES_PUBLISH_kummer_sources.tsv', [dict(
    source_key='HuybrechtsK3Draft',
    url='https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf',
    version='449-page author draft, explicitly a pre-publication copy; copyright Daniel Huybrechts2015 on the second PDF page; publication metadata retained by bibliography155',
    locus_read='Complete Chapter1 Example1.3(iii), pp.8-9, including its whole proof/continuation on p.9; title/copyright/version page; pp.8-9 rendered and visually read',
    sha256=sha, bytes=len(b),
    own_paraphrase='For an arbitrary abelian surface over a field of characteristic different from two, the minimal resolution of the quotient by inversion is a K3 surface. It is also the quotient of the blowup at the sixteen two-torsion points by the lifted involution. The text gives the canonical-bundle comparison and the invariant coherent-cohomology argument.',
    exact_application='Take the same arbitrary abelian surface A fixed in UN13, over C, with its inversion a to -a. Restrict the actual threefold quotient (a,s) to (-a,-s) to s=0 or infinity. The retained charts (a,b,s)=(r,ru,rv), R=r^2 restrict at v=0 to the quotient of the point blowup of A at A[2]. The identity away from A[2] and those charts identify P with the source surface Bl_{A[2]}A modulo the lifted involution, over A/(+-1). No global product decomposition of A is used.',
    read_extent='Fresh HTTP200 download, complete cited example and proof read, and page images read. The full original UN13 statement and the complete quotient/Kummer proof steps1-5 were read for the exact application. The remaining complete UN13 proof is root\'s reading; no full-unit or independent check credit is claimed here. Bibliography155 already names this draft layout, so only the two body locators need pp.8-9.',
    date_utc=now)])

events = []
for sid, suffix, outcome, where in [
    ('cdp:st:C.2.UN.6;prop:II:multiple-elliptic-hopf-threefold', 'Fujimoto-UN6-P328',
     'Read the complete original UN6 owner/proof and its complete following Hopf-map counterexample, then the exact published definition, Theorem2.8 full proof, Corollary2.10 and Examples3.1/3.4(1). Checked the stated analytic hypotheses against the explicit Hopf quotient, both fibre parametrizations, the multiple-line pullback and the global graph normalization of the source cover. The source text is opened; raw PDF bytes/hash and visual reading are unavailable and are not claimed. No independent derivation or full receiving root-unit reading claimed.',
     'UN6 and P328; Fujimoto1988 published pp.91-99 at the specified complete loci'),
    ('cdp:st:C.2.UN.13', 'Huybrechts-Kummer-UN13',
     'Freshly downloaded the exact author draft and read complete Example1.3(iii) pp.8-9 including its proof and rendered page images. Applied it to the same arbitrary abelian surface A and identified the source blowup quotient with the actual central component through the retained local charts and the identity away from the two-torsion points. Original UN13 statement and quotient/Kummer steps1-5 read. No product specialization, independent check or full-unit closure claimed.',
     'UN13 classical Kummer input; Huybrechts author draft Chapter1 Example1.3(iii),pp.8-9'),
]:
    event_id = 'publish:c3:provenance:' + suffix
    events.append(dict(statement_id=sid, date=now[:10],
        who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; continuation3 provenance',
        type='used and rechecked in this run', outcome=outcome,
        event_id=event_id, phase='publication exact primary application',
        source_file='agents/continuation3_provenance/final_sources/S6_SERIES_PUBLISH_occurrence_sources_CHECK_EVENTS.tsv',
        source_row='', source_event_type='used and rechecked in this run',
        evidence_group=event_id, publish_input_file='', publish_input_row='',
        date_utc=now, where=where))
write('S6_SERIES_PUBLISH_occurrence_sources_CHECK_EVENTS.tsv', events)
print('Prepared Fujimoto exact-reading report with explicit raw-byte limitation and Kummer exact-source report; shared source unchanged.')
