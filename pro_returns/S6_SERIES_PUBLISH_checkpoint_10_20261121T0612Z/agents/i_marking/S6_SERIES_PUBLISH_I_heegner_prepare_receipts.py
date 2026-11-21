#!/usr/bin/env python3
"""Build read-only primary-locator receipts and exact proposed guards.

This script writes only agent records.  It neither changes publication sources
nor performs or credits a mathematical proof/computation check.
"""
from pathlib import Path
import datetime
import hashlib
import json
import re

WORK = Path('/workspace/scratch/653608133b22/work')
OUT = WORK / 'agents/i_marking'
LIT = OUT / 'literature'
PREFIX = 'S6_SERIES_PUBLISH_I_heegner'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def dump(name, value):
    path = OUT / (PREFIX + name)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')
    return path


def page(key, pdf_page, printed_page, purpose):
    p = LIT / f'S6_SERIES_PUBLISH_I_{key}_p{pdf_page:03}.png'
    return dict(pdf_page_1based=pdf_page, printed_page=printed_page,
                image=str(p), image_sha256=sha(p), purpose=purpose,
                actual_image_view=True)


now = datetime.datetime.now(datetime.timezone.utc).isoformat()
snapshot = json.loads((OUT / (PREFIX + '_receiving_snapshot.json')).read_text())
source_path = Path(snapshot['source'])
if not source_path.is_absolute():
    source_path = WORK / source_path
source = source_path.read_text()
assert sha(source_path) == snapshot['source_sha256'] == '7479a42f0c18cb2853e483ba3b0b222087e800a6a720ca5f2a21313ff6706cc6'
retrieval = json.loads((OUT / (PREFIX + '_primary_retrieval.json')).read_text())
retrieval_by_key = {r['key']:r for r in retrieval['sources']}
gross_retrieval_path = LIT/'S6_SERIES_PUBLISH_I_Gross1991_primary.retrieval.json'
retrieval_by_key['Gross1991'] = json.loads(gross_retrieval_path.read_text())

specs = [
    dict(key='CrCremonaSiksek2006', file_key='CremonaSiksek2006',
         receiving=['ari:C.6.R1'],
         edition='Linked author version, 12 unnumbered PDF pages; published chapter metadata remains ANTS VII, LNCS4076 (2006),275–286. No numerical conversion to published pages is asserted.',
         locator='Theorem1, PDF page8; minimal-model setup PDF page1; good-reduction subgroup PDF page2; height convention equations(3)–(4), PDF page3.',
         pages=[page('CremonaSiksek2006',1,None,'Title and minimal Weierstrass model'),page('CremonaSiksek2006',2,None,'Definition of E_gr(Q) and component multiplier'),page('CremonaSiksek2006',3,None,'Local and canonical height definitions'),page('CremonaSiksek2006',8,None,'Theorem1 complete displayed statement')],
         scope='The source criterion gives a positive canonical-height lower bound for nontorsion points in E_gr(Q), using B_n(mu) and the intersection of inverse-image intervals. The receiving proof explicitly uses a minimal model and the real and finite good-reduction subgroup. The source height is defined by equations(3)–(4), starting with log max(1,|x|).',
         limits='No saturation output, interval computation, height conversion, generator primitiveness, or numerical bound is recomputed in this locator pass.'),
    dict(key='CrDarmon2009', file_key='Darmon2009',
         receiving=['I:CM-coefficient-series','ari:C.6.R2','ari:C.6.R5'],
         edition='Author lecture notes dated31July2009 on the displayed title page;16pages, printed pagination1–16.',
         locator='Section3, Assumption3.1 and the canonical Hecke-character/theta-series displays, pp.4–5.',
         pages=[page('Darmon2009',1,1,'Title and date'),page('Darmon2009',4,4,'Section3 setup and start of Assumption3.1'),page('Darmon2009',5,5,'End of Assumption3.1 and Hecke character/theta series')],
         scope='The displayed construction concerns maximal-order CM, class number one, two units, odd discriminant, and a rational curve of conductor D^2. It specifies the type(1,0) Hecke character on principal ideals and the associated normalized weight-two theta series. These are the source inputs cited for the receiving coefficient construction.',
         limits='The receiving coefficient comparison, twists, integer enumeration, and numerical L-series certificates remain local arguments; their calculations are not rechecked here.'),
    dict(key='CrRubin1999', file_key='Rubin1999',
         receiving=['ari:C.6.R2'],
         edition='Linked68-page lecture-note version, using its printed pages15 and47; no transfer to the published collection pagination167–234.',
         locator='Proposition5.3 and its proof p.15; maximal-order convention p.16; class-number-one setup p.27; E/K and Hecke-character setup p.37; Theorem10.1 p.47.',
         pages=[page('Rubin1999',1,None,'Title and introductory theorem'),page('Rubin1999',15,15,'CM definition, Proposition5.3 and full proof'),page('Rubin1999',16,16,'Maximal-order convention'),page('Rubin1999',27,27,'Class-number-one convention'),page('Rubin1999',37,37,'E/K and Hecke-character conventions'),page('Rubin1999',47,47,'Theorem10.1')],
         scope='Theorem10.1 states the Coates–Wiles central-Hecke-value implication giving finite E(K). Proposition5.3 constructs an F-isogeny E→E′ by quotienting by the Galois-stable conductor-ideal subgroup; its proof identifies End_F(E′) with O_K. The surrounding source conventions include F containing the CM field, maximal order after Proposition5.3, and class number one in the subsequent exposition.',
         limits='The printed Proposition5.3 statement shows End_F(E) where its proof explicitly gives End_F(E′); the receipt records the actual construction. No new proof of Coates–Wiles, isogeny invariance, or the receiving central vanishing is credited.'),
    dict(key='CrGrossZagier1986', file_key='GrossZagier1985preprint',
         receiving=['ari:C.6.R3'],
         edition='Official MPIM submitted preprint MPI/SFB85-30 (1985), identified by title page and repository record. Two printed pages per scan page. The bibliography also identifies the1986 Inventiones publication; cited page numbers below are preprint pages.',
         locator='ChapterI, Theorem7.3, printedp.12 (PDFpage8,right); definitions of the real period/global height onp.11; ChapterV,Section2, printedp.129 (PDFpage67,left). Setuppp.125–126 (PDFpage65).',
         pages=[page('GrossZagier1985preprint',1,None,'Title and MPI/SFB85-30 identifier'),page('GrossZagier1985preprint',7,'9–10','Height conventions and modularity setup'),page('GrossZagier1985preprint',8,'11–12','Period/height definitions and TheoremI.7.3'),page('GrossZagier1985preprint',65,'125–126','Waldspurger choice and modular parametrization setup'),page('GrossZagier1985preprint',67,'129–130','Proof return to Q by trace and period-product formula')],
         scope='TheoremI.7.3 supplies a rational point and nonzero rational factor relating the central derivative, a rational differential real period, and a canonical height for a modular E/Q with central value zero. The final proof onp.129 chooses the auxiliary quadratic twist with nonzero central value, forms P=P_K+conjugate(P_K), and uses the displayed period-product identity.',
         limits='The receiving rational differential scaling and full-real-period conversion are local steps. Their arithmetic and the finite list of curves are not rechecked in this citation pass.'),
    dict(key='CrGross1991', file_key='Gross1991',
         receiving=['ari:C.6.R3'],
         edition='Identified scan of the published chapter from wstein.org; chapter title and authorship visible, p.236 printed on the theorem page. Cambridge publisher metadata confirms the1991 chapter pp.235–256 and DOI10.1017/CBO9780511526053.009. The publisher web title uses "for"; the scan title and existing bibliography use "on".',
         locator='Section1 setup p.235 (PDFpage1,right; starting page supported by publisher metadata); Theorem1.3 p.236 (PDFpage2,left); later proof-sketch restriction p.237 (PDFpage2,right).',
         pages=[page('Gross1991',1,'235 (chapter start; numeral not displayed)','Chapter title, modular parametrization and Heegner setup'),page('Gross1991',2,'236–237','Theorem1.3 and subsequent proof-sketch scope')],
         scope='Theorem1.3 gives rank1 and finite Sha(E/K) from the infinite-order Heegner point y_K. Section1 assumes a modular E/Q, split primes dividing N, auxiliary imaginary quadratic discriminant −D with D≠3,4, and defines y_K by trace. The non-CM restriction occurs in Section2’s illustrative proof after the theorem, as visible onp.237.',
         limits='The receipt inventories D≠3,4 explicitly. It does not select an auxiliary field or reprove its availability, the Gross–Zagier input, Kolyvagin’s theorem, or the receiving restriction–inflation argument.'),
    dict(key='CrJetchev2008', file_key='Jetchev2008',
         receiving=['ari:C.6.R3'],
         edition='arXiv:0707.0032v1,30June2007,20pages. The explicitv1 download is byte-identical to the original bare-URL retrieval. Journal publication metadata remains JNT128(2008),3394–3410; citedp.2 is the arXiv version.',
         locator='Theorem1.1, p.2 of arXivv1.',
         pages=[page('Jetchev2008',1,1,'Title, authors, arXivv1/date side stamp'),page('Jetchev2008',2,2,'Theorem1.1')],
         scope='Theorem1.1 states equality of analytic and Mordell–Weil ranks for elliptic curves over Q of analytic rank at most one. The receiving paragraph labels this citation as the rank conclusion and cites Gross separately for finite Sha.',
         limits='No finite-Sha conclusion is attributed to the displayed Theorem1.1, and no receiving rank or Heegner-point computation is rerun.'),
    dict(key='CrBDP2012', file_key='BDP2012',
         receiving=['I:ordinary-CM-scope'],
         edition='Publisher-paginated PDF hosted by Darmon; displayed journal title, volume260,no.2,year2012,DOI10.2140/pjm.2012.260.261. The article begins on PDFpage2, printedp.261.',
         locator='Theorem1,p.262 (PDFpage3); CM and split-good-prime setuppp.261–262.',
         pages=[page('BDP2012',2,261,'Published article metadata and CM setup'),page('BDP2012',3,262,'Prime setup, Theorem1 and all displayed quantities')],
         scope='For a maximal-order CM curve A/Q, a split prime prime to its conductor, and a simple central zero, Theorem1 supplies a nontorsion rational point and the Katz-value/formal-logarithm identity modulo K×, with the stated p-adic period and differential. The receiving statement preserves that algebraic-factor scope.',
         limits='No comparison of real and p-adic periods or proof of the receiving curve-by-curve applicability is made here.'),
    dict(key='CrCastella2025', file_key='Castella2025',
         receiving=['I:ordinary-CM-scope'],
         edition='Linked author manuscript dated14February2025,37pages. Its title page names Francesco Castella. The bibliography’s published PLMS record is retained; locatorp.2 refers to this author version.',
         locator='TheoremA and Remark1.1,p.2 of the14February2025 author version.',
         pages=[page('Castella2025',1,1,'Title, author spelling and manuscript date'),page('Castella2025',2,2,'TheoremA with all displayed hypotheses and Remark1.1')],
         scope='The displayed hypotheses include maximal-order CM, an abelian torsion extension over K, a simple zero of the specified Hecke L-function, p prime to6h_K and split in K, conductor prime to p, and the exact-different condition '+r'\mathfrak d_K\parallel N_{F/K}(\mathfrak f_\psi)'+' in the source notation. The theorem gives rank equality and the stated p-primary Sha/leading-term valuation formula.',
         limits='The source’s notation is retained in the receipt. No new transfer to nonmaximal orders, isogeny argument, conductor computation, or applicability at the excluded inert prime is credited.')
]

for row in specs:
    p = LIT / f"S6_SERIES_PUBLISH_I_{row['file_key']}_primary.pdf"
    row['primary_pdf'] = str(p)
    row['primary_pdf_sha256'] = sha(p)
    download = retrieval_by_key[row['file_key']]
    assert row['primary_pdf_sha256'] == download['sha256']
    row['primary_url'] = download['url']
    row['retrieval_hash_matches'] = True
    row['observation_recorded_utc'] = now
    row['mathematical_check_events_added'] = 0
    row['status'] = 'primary statement located and actual page image read; edition and cited scope recorded'

md_receipt_path = WORK/'agents/i_provenance/literature/S6_SERIES_PUBLISH_I_Drinfeld1973_locator_receipt.json'
md_bib_path = WORK/'agents/i_provenance/S6_SERIES_PUBLISH_I_Drinfeld1973_bibliography_input.json'
md = json.loads(md_receipt_path.read_text())
md_bib = json.loads(md_bib_path.read_text())
assert sha(md['path']) == md['sha256']
for p in md['actual_page_views']:
    assert sha(p['image']) == p['image_sha256']
specs.append(dict(key='Drinfeld1973', receiving=['ari:C.6.R5'],
                 primary_pdf=md['path'],primary_pdf_sha256=md['sha256'],
                 primary_url=md['url'],metadata_url=md['metadata_source'],retrieval_hash_matches=True,
                 edition='Original Russian edition, Funktsional. Anal. i Prilozhen.7(2)(1973),83–84. The English translation155–156 and its DOI are metadata only; those English pages were not viewed.',
                 locator='Section1, unnumbered theorem, originalp.83 (PDFpage1).',
                 pages=md['actual_page_views'],
                 scope='The theorem concerns a congruence subgroup of PSL2(Z) and the degree-zero divisor class of two cusps. For the receiving modular parametrization phi:X_0(N)→E, the induced homomorphism phi_*:Pic^0(X_0(N))→E sends [0]−[infinity] to phi(0)−phi(infinity). The homomorphism commutes with multiplication by each integer, carrying the source finite-order class to the receiving torsion point.',
                 limits='The source supplies cusp-difference torsion. The subsequent elliptic-logarithm identity and denominator arithmetic remain the receiving argument. No English-page reading or new mathematical-check event is claimed.',
                 delegated_receipt=str(md_receipt_path),delegated_receipt_sha256=sha(md_receipt_path),
                 delegated_checker='/root/provenance_inventory',
                 own_followup='This agent opened and read both retained primary images, including the Section1 theorem, after receiving the delegated receipt; verified the exact PDF/image hashes and opened the official Mathnet metadata.',
                 observation_recorded_utc=now,mathematical_check_events_added=0,
                 status='primary statement located and actual page image read; edition and cited scope recorded'))

receipt_path = dump('_primary_locator_receipt.json',dict(
    created_utc=now,source=str(source_path),source_sha256=snapshot['source_sha256'],
    receiving_context_file=str(OUT/(PREFIX+'_receiving_context.txt')),
    receiving_context_sha256=snapshot['context_sha256'],
    receiving_context_lines=[snapshot['context_start_line'],snapshot['context_end_line']],
    exposure='Complete frozen receiving propositions/lemmas/remarks and proofs from lines26784–27657 read before source comparison. No fresh-context proof derivation is claimed. Historical shared-bibliography notes were read after the present theorem-page image reads, solely to preserve their fields in the proposed bibliography guards.',
    actual_image_view_completion_window_utc='2026-11-21T05:03–05:08Z; individual retained images are hash-bound below. The recorded time is the receipt assembly time, not a fabricated per-image timestamp.',
    sources=specs,
    retrieval_receipts=[str(OUT/(PREFIX+'_primary_retrieval.json')),str(gross_retrieval_path),str(OUT/(PREFIX+'_metadata_retrieval.json'))],
    coverage=dict(requested=9,primary_statement_page_images_read=9,blocked=0),
    purpose='Exact-primary citation locator, edition identification and source-scope inventory only.',
    mathematical_check_events_added=0,computational_check_events_added=0,
    main_tex_modified=False,defect_tsv_modified=False,
    receipt_limits=['No primary theorem is re-proved.','No receiving numerical certificate is rerun.','No historical source-note claim is transferred to this pass.','The Gross auxiliary-discriminant prerequisite is explicitly inventoried; this locator pass does not select that field.']
))

changes=[]

def guard(id, old, new, reason):
    count=source.count(old)
    assert count>0,(id,old)
    changes.append(dict(id=id,old=old,new=new,count=count,
                        old_sha256=hashlib.sha256(old.encode()).hexdigest(),reason=reason))

guard('I-heegner-CremonaSiksek-T1-page',r'\citet[Theorem 1]{CrCremonaSiksek2006}',
      r'\citet[Theorem~1, PDF p.~8]{CrCremonaSiksek2006}',
      'The displayed author-version Theorem1 is on unnumbered PDFpage8; both header and operative proof citation receive the exact locator.')
guard('I-heegner-Darmon-section-pages',r'\citet[Section 3]{CrDarmon2009}',
      r'\citet[\S3, pp.~4--5]{CrDarmon2009}',
      'The remaining broad Section3 citations receive the pages already used in the receiving coefficient lemma and R5 header; actual images show Assumption3.1 and theta-series construction.')
guard('I-heegner-Rubin-T10-page',r'\citet[Theorem 10.1]{CrRubin1999}',
      r'\citet[Theorem~10.1, p.~47]{CrRubin1999}',
      'Actual linked-note Theorem10.1 page; the bibliography guard identifies this pagination.')
guard('I-heegner-Rubin-P53-page',
      'Proposition~5.3 of the same source supplies, for a nonmaximal CM order, an isogenous',
      r'\citet[Proposition~5.3, p.~15]{CrRubin1999} supplies, for a nonmaximal CM order, an isogenous',
      'Add a direct page-specific source to the conductor-ideal quotient statement; its receiving mathematical content is unchanged.')
guard('I-heegner-GrossZagier-I73-page',r'\citep{CrGrossZagier1986}',
      r'\citep[Chapter~I, Theorem~7.3, preprint p.~12]{CrGrossZagier1986}',
      'The exact displayed result is on MPI85-30 printedp12, PDFspread8; the page is explicitly identified as preprint pagination.')
guard('I-heegner-GrossZagier-V2-page',
      'imaginary quadratic field $K$ in the proof of Gross--Zagier I.7.3\nhas split Heegner primes',
      'imaginary quadratic field $K$ in the proof of Gross--Zagier I.7.3\n'+r'\citep[Chapter~V, \S2, preprint p.~129]{CrGrossZagier1986} has split Heegner primes',
      'The actual proof return to Q and auxiliary-twist nonvanishing step is on preprintp129; no auxiliary-field assertion is added.')
guard('I-heegner-Gross-T13-page',r'\citet[Theorem 1.3]{CrGross1991}',
      r'\citet[Theorem~1.3, pp.~235--236]{CrGross1991}',
      'Theorem1.3 is on publishedp236; p235 contains its Heegner and discriminant setup.')
guard('I-heegner-Jetchev-T11-page',r'\citet[Theorem 1.1]{CrJetchev2008}',
      r'\citet[Theorem~1.1, p.~2 of arXiv v1]{CrJetchev2008}',
      'Actual version1 page2 supplies the stated rank conclusion; the source is pinned in the bibliography.')
guard('I-heegner-BDP-T1-page',r'\citet[Theorem 1]{CrBDP2012}',
      r'\citet[Theorem~1, p.~262]{CrBDP2012}',
      'Published theorem page262 is visually confirmed in the DOI-bearing journal PDF.')
guard('I-heegner-Castella-TA-page',r'\citet[Theorem~A]{CrCastella2025}',
      r'\citet[Theorem~A, p.~2 of the author version]{CrCastella2025}',
      'The linked14February2025 author-version theorem page is visually confirmed; its edition is identified in the bibliography.')
guard('I-heegner-Drinfeld-operative-citation',
      'Manin--Drinfeld says that the image of\nthe rational cuspidal divisor $[0]-[\u005cinfty]$ is torsion.',
      'Manin--Drinfeld '+r'\citep[Section~1, unnumbered theorem, p.~83 of the Russian original]{Drinfeld1973}'+' says that the image of\nthe rational cuspidal divisor $[0]-[\u005cinfty]$ is torsion.',
      'The primary Russian theorem actually read onp83 supplies cusp-difference torsion; new bibliography entry identifies both original and translation metadata.')

notes={
 'CrCremonaSiksek2006':r'\newblock The linked author version has unnumbered pages; its locators use PDF page numbers.',
 'CrDarmon2009':r'\newblock Author lecture notes dated 31 July 2009; the cited pagination is that of this version.',
 'CrRubin1999':r'\newblock Page references use the linked lecture-note version, paginated 1--68.',
 'CrGrossZagier1986':r'\newblock The linked text is the MPI/SFB 85-30 preprint (1985); citations marked as preprint pages use its pagination.',
 'CrGross1991':r'\newblock Chapter scan: \url{https://wstein.org/papers/bib/gross-kolyvagins_work_on_modular_elliptic_curves.pdf}.',
 'CrJetchev2008':r'\newblock The cited version is arXiv:0707.0032v1, 30 June 2007; page references use that version.',
 'CrCastella2025':r'\newblock Page references use the linked author version dated 14 February 2025.'
}
for key,note in notes.items():
    old=snapshot['bibliography_entries'][key]
    new=old.rstrip()+'\n\n'+note+'\n\n'
    if key=='CrJetchev2008':new=new.replace('https://arxiv.org/pdf/0707.0032}', 'https://arxiv.org/pdf/0707.0032v1}')
    if key=='CrCastella2025':new=new.replace('Francesc Castella.','Francesco Castella.')
    guard('I-heegner-bib-'+key,old,new,'Identify the exact primary version read and the pagination used; Castella author spelling and Jetchev version URL are corrected where applicable.')

md_anchor=r'\bibitem[Darmon(2009)]{CrDarmon2009}'
guard('I-heegner-bib-Drinfeld1973-insert',md_anchor,md_bib['inline_bibitem']+'\n'+md_anchor,
      'Add the actual original Russian primary source and separately identify its English translation. Root may move the complete new entry to its preferred alphabetical location.')

# Every old fragment is required against the frozen source; replacements are
# deliberately disjoint except for the Drinfeld insertion anchor.  Validate the
# proposed sequence in memory only and do not write a replacement main source.
working=source
for c in changes:
    n=working.count(c['old'])
    assert n==c['count'],(c['id'],'sequential count',n,c['count'])
    working=working.replace(c['old'],c['new'])
guard_path=dump('_citation_guards.json',dict(source=str(source_path),source_sha256=sha(source_path),
                   receipt=str(receipt_path),changes=changes,
                   mathematical_check_events_added=0,applied_to_main_source=False))

bib_path=WORK/'S6_SERIES_PUBLISH_references.bib'
bib=bib_path.read_text()
bib_changes=[]
for row in specs[:-1]:
    key=row['key']
    m=re.search(r'(?ms)^@\w+\{'+re.escape(key)+r',.*?(?=^@|\Z)',bib)
    assert m,key
    old=m.group(0)
    core=old.rstrip()
    assert core.endswith('}')
    body=core[:-1].rstrip()
    new=body+',\n'
    new+='  current_run_source = {'+row['edition']+'},\n'
    new+='  current_run_locators = {'+row['locator']+'},\n'
    new+='  current_run_receipt = {S6_SERIES_PUBLISH_I_heegner_primary_locator_receipt.json; actual statement-page images read on21November2026; zero mathematical check events}\n}\n\n'
    if key=='CrCastella2025':new=new.replace('Castella, Francesc}', 'Castella, Francesco}')
    if key=='CrJetchev2008':new=new.replace('url = {https://arxiv.org/pdf/0707.0032}', 'url = {https://arxiv.org/pdf/0707.0032v1}')
    if key=='CrGross1991':new=new.replace('  retrieval_url = {https://wstein.org/papers/bib/gross-kolyvagins_work_on_modular_elliptic_curves.pdf},','  url = {https://wstein.org/papers/bib/gross-kolyvagins_work_on_modular_elliptic_curves.pdf},')
    bib_changes.append(dict(id='I-heegner-shared-bib-'+key,old=old,new=new,count=1,
                            reason='Preserve historical source-note fields and append exact current-run edition/locator scope.'))
assert '@article{Drinfeld1973,' not in bib
anchor='@misc{CrDarmon2009,'
assert bib.count(anchor)==1
bib_changes.append(dict(id='I-heegner-shared-bib-Drinfeld1973',old=anchor,
                        new=md_bib['shared_bib_entry']+'\n'+anchor,count=1,
                        reason='Insert the new primary original/translation bibliographic record; leave existing entries intact.'))
bib_working=bib
for c in bib_changes:
    assert bib_working.count(c['old'])==c['count'],c['id']
    bib_working=bib_working.replace(c['old'],c['new'])
shared_path=dump('_shared_bib_guards.json',dict(bib=str(bib_path),bib_sha256=sha(bib_path),
                     created_utc=now,receipt=str(receipt_path),changes=bib_changes,
                     mathematical_check_events_added=0,applied_to_shared_bibliography=False))

validation=dict(created_utc=now,frozen_source_sha256=sha(source_path),
                bibliography_input_sha256=sha(bib_path),
                source_guard_count=len(changes),source_replacement_occurrences=sum(c['count'] for c in changes),
                shared_bib_guard_count=len(bib_changes),
                all_old_fragments_matched_expected_count=True,
                all_sequential_in_memory_guard_applications_pass=True,
                sources_with_actual_statement_page_views=len(specs),
                primary_pdf_hashes={x['key']:x['primary_pdf_sha256'] for x in specs},
                no_main_source_or_bib_or_defect_file_written=True,
                source_guard_sha256=sha(guard_path),shared_guard_sha256=sha(shared_path),
                receipt_sha256=sha(receipt_path),mathematical_check_events_added=0)
validation_path=dump('_guard_validation.json',validation)

report=OUT/(PREFIX+'_locator_report.md')
report.write_text('''# Heights and Heegner primary locators

Nine requested sources have an exact primary statement locator and an actual page-image read. This pass adds no mathematical proof-check or computation events. The complete receiving context is frozen to candidate11 source `7479a42f0c18cb2853e483ba3b0b222087e800a6a720ca5f2a21313ff6706cc6`, lines26784–27657.

| Source | Exact displayed locator | Edition used |
|---|---|---|
| Cremona–Siksek | Theorem1, PDFp8; subgroup PDFp2; height equations PDFp3 | Unnumbered linked author version |
| Darmon | Section3, Assumption3.1 and theta displays, pp4–5 |31July2009 author notes |
| Rubin | Proposition5.3,p15; Theorem10.1,p47 | Linked68-page lecture notes |
| Gross–Zagier | I.7.3,p12; final proof V.2,p129 | MPI/SFB85-30 preprint; two-up scan |
| Gross | Theorem1.3,p236; setup p235 | Published1991 chapter scan |
| Jetchev–Lauter–Stein | Theorem1.1,p2 | arXiv0707.0032v1,30June2007 |
| Bertolini–Darmon–Prasanna | Theorem1,p262; setup pp261–262 | Published2012 PJM PDF |
| Castella | TheoremA and Remark1.1,p2 |14February2025 author version |
| Drinfeld | Section1, unnumbered theorem,p83 | Original Russian1973 edition |

The operative source/bibliography changes are in `_citation_guards.json`; shared bibliography changes are in `_shared_bib_guards.json`. Both files give exact old/new strings and expected counts. Validation applies all changes in memory only. Main TeX, shared bibliography and defect TSV are untouched.

The edition notes prevent transfers of lecture-note/preprint/arXiv pagination to journal or collection pages. The Castella author spelling is corrected from Francesc to Francesco, as printed on the primary title page. The Gross chapter scan is now an actually read retrieval, with its title and visible theorem-page number compared to the publisher record. A Drinfeld entry is added, with English translation metadata identified separately from the Russian pages read.

Scope limits remain explicit. Gross’s section1 includes D≠3,4 for the auxiliary quadratic discriminant, inventoried in the receipt; this pass does not choose that field. Jetchev Theorem1.1 is used for the rank conclusion, with finite Sha sourced to Gross. The Castella exact-different condition is recorded in the primary notation. The Drinfeld source is transported by the explicit induced Jacobian homomorphism [a]−[b]↦phi(a)−phi(b). Row-specific heights, saturation, ranks, L-series bounds, conductor computations and isogeny transfers are not rerun.

The primary receipt records every PDF and image hash, receiving IDs, actual exposures and source-scope limits. The Manin–Drinfeld search was delegated to provenance; this agent subsequently opened the retained primary images and checked their hashes and the official metadata. Historical shared-bibliography verification notes were preserved rather than credited to this pass.
''')

print(json.dumps(dict(receipt=str(receipt_path),receipt_sha256=sha(receipt_path),
                      guards=str(guard_path),guard_sha256=sha(guard_path),
                      shared_guards=str(shared_path),shared_guard_sha256=sha(shared_path),
                      validation=str(validation_path),validation_sha256=sha(validation_path),
                      report=str(report),source_guard_count=len(changes),
                      source_replacement_occurrences=sum(c['count'] for c in changes),
                      shared_guard_count=len(bib_changes),coverage=9),indent=2))
