#!/usr/bin/env python3
"""Record only full candidate18 PNGs actually viewed by this reader."""
import datetime,hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];AREA=ROOT/'agents/continuation_infra'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
findings={
186:'Read the complete page: affine/intersection calculations, infinity expansions, Shioda height-pairing matrix, rank calculation and torsion step. Displays, exact literature locators and numbered proof steps are legible; no new actionable register finding.',
188:'Read the complete page: end of the lattice proof and Proposition22.10 on torsor transgression, with its statement and Galois-cohomology/local restriction proof opening. Small tag, statement title, displayed sequence and source locators fit clearly; no new actionable finding.',
192:'Read the complete page: Section22.4, Remark22.13 and Theorem22.14 with the full displayed fundamental-group argument. The connector formulas, deformation-retraction steps and conclusion are readable; no new actionable finding.',
198:'Read the complete page: degree-restriction matrix, elliptic-bundle cocycle, Chern vector, scalar Hopf quotient and normal-line product. The revised proof language remains tied to the explicit construction; all formulas and proof numbering fit cleanly.',
199:'Read the complete page: integral homology, coherent cohomology, scalar-Hopf comparison, punctured-product obstruction and product conclusion. The cited Abasheva–Déev v1 locator is explicit; no new actionable register finding.',
207:'Read the complete page: infinite-product gauges, Hopf developing map, normal-line transform and the beginning of the divisor nonextension argument. Equations and explanatory steps are legible; no new actionable finding.',
208:'Read the complete page: end of the nonextension and normal-line matching argument, then Proposition22.28 and its proof opening. The dated-edition scope and references are explicit; the low-page displayed section-ring formula fits cleanly.',
209:'Read the complete page: continuation of Proposition22.28 through the cone, logarithmic forms, Atiyah extension and formal-neighbourhood cohomology. Displayed exact sequences and source locators are readable; no new actionable finding.',
210:'Read the complete page: Leray/global-local maps, Čech lifting proof and analytic semiversal deformation reference. Čech accent and exact Dloussky–Teleman preprint locator render correctly; no new actionable finding.',
211:'Read the complete page: end of the smoothing proof and Proposition22.29 with its normal-line formulas, explicit noncompactness reason and proof opening. The retained scope witness for the removed later repetition is present; no new actionable finding.',
294:'Read the complete page: Remark25.7, Section26, Definition26.1 and Proposition26.2 with sigma/third-kind period formulas. Numbered displays, branch conventions and proof steps fit the page; no new actionable finding.',
295:'Read the complete page: completion of Proposition26.2 and Proposition26.3 on the compact subgroup, including its real-axis formula and proof. The exact Bertolin v2 locator and equation numbers are readable; no new actionable finding.',
321:'Read this additional complete page to inspect the build warning. The last paragraph of proofstep5 shows visibly stretched spacing in the lines beginning “The second equality identifies...” and “The bundles...”, matching the two underfull messages at source31583–31593. The full PNG is byte-identical to candidate17 but is newly inspected here; a paragraph-break-only D23 proposal remains pending. All equations remain legible.',
322:'Read the complete page: proofsteps6–9, dual logarithmic sequence, tangent class and local miniversality. The source endpoint of the preceding underfull paragraph maps here, but the two reported underfull lines themselves are on321. No comparable layout defect or new actionable finding appears on322.',
324:'Read the complete page: final direct-image formulas, exact normal quotient, AppendixC heading and DefinitionC.1. The source changes retain the displayed exact sequences and direct images; headings and formulas fit cleanly.',
326:'Read the complete page: end of the conductor calculation and TheoremC.4 on the full automorphism group. The incidence matrix, theorem title/small tag and displayed exact sequence are legible; no new actionable finding.',
327:'Read the complete page: completion of the automorphism proof, integral matrix calculation and TheoremC.5 with its period-class proof opening. The group/action notation and referenced equations are clear; no new actionable finding.',
329:'Read the complete page: the final part on results not yet established and the relative-period question. The exact open-question scope, displayed examples and Bertolin v2 page locators remain explicit; no new actionable finding.',
333:'Read the complete bibliography page: Abasheva–Déev through Bănică–Stănășilă. The new Abate journal/DOI and cited2010 manuscript note, pinned preprint URLs, Agboola DOI and Angella v2 note render legibly; entry boundaries and line wraps fit.',
334:'Read the complete bibliography page: Belabas through Bourdon–Clark–Stankewicz. Bertolin DOI/v2 note, both Bierstone–Milman authors, the Bost collection/publisher and the Bourdon v3 note render correctly; no clipping or new actionable finding.',
335:'Read the complete bibliography page: Buchdahl through Cornulier. Cartan seminar/exposé metadata and Francesc Castella’s corrected given name render correctly; Claude/Alpöge, Chen v2 and Conrad source designations remain intact. No new actionable finding.',
}
def main():
    manifest=ROOT/'render/I_candidate18/manifest.json';m=json.loads(manifest.read_text());images={r['page']:r for r in m['rendered_pages']}
    pdf=ROOT/'build/I_candidate18/S6_SERIES_PUBLISH_I.pdf';pdfhash=sha(pdf)
    pages=[]
    for page,finding in sorted(findings.items()):
        p=ROOT/'render/I_candidate18'/f'page_{page:03d}.png';h=sha(p);assert h==images[page]['image_sha256']
        pages.append({'page':page,'finding':finding,'image_sha256':h,'pdf_sha256':pdfhash,'actual_full_page_image_read':True,'pending_guards':'D23 local paragraph-break layout proposal pending' if page==321 else ''})
    record={'paper':'I','candidate':18,'reader':'GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; continuation infrastructure agent','recorded_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source_sha256':'3542f2632cad8f1eb78f0f30f8a64ca91998f3bd1d97010ca76d89297c4bffe7','pdf_sha256':pdfhash,'render_manifest_sha256':sha(manifest),'pages':pages,'status':'immutable partial reading record;20 of31 assigned pages plus extra321 actually viewed','assigned_pages':[186,188,192,198,199,207,208,209,210,211,294,295,322,324,326,327,329,*range(333,347)],'extra_pages_actually_read':[321],'register_types_considered':[f'D{i:02d}' for i in range(1,26)],'mathematical_events_added':0,'certified':False,'scope':'Every listed complete PNG was displayed and actually read. This record gives page-reading evidence only; it adds no mathematical rechecking event or certification.'}
    p=AREA/'S6_SERIES_PUBLISH_I_final_candidate18_reading_infra_partial_01.json';assert not p.exists();p.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
    md=AREA/'S6_SERIES_PUBLISH_I_final_candidate18_reading_infra_partial_01.md';assert not md.exists();md.write_text('# Candidate18 infrastructure reading: immutable partial01\n\n'+record['scope']+'\n\n'+''.join(f'## Page {r["page"]}\n\n{r["finding"]}\n\nPNG SHA-256: `{r["image_sha256"]}`.\n\n' for r in pages))
    print(json.dumps({'record':str(p.relative_to(ROOT)),'sha256':sha(p),'actual_pages':len(pages),'assigned_pages_read':20,'extra_pages':1,'mathematical_events_added':0}))
if __name__=='__main__':main()
