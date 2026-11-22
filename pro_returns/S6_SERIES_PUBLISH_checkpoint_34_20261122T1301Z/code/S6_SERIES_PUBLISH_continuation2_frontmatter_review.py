"""Record an actual complete source reading; this awards no final-PDF credit."""
from pathlib import Path
import datetime as dt,hashlib,json,re
R=Path(__file__).resolve().parents[1]
p=R/'S6_SERIES_PUBLISH_II.tex';raw=p.read_bytes();s=raw.decode()
a=s.index('\\begin{document}');b=s.index('\\section{Index, Picard components and endpoint cohomology}',a)
front=s[a:b]
claims=[]
for letter in 'ABCDEFG':
 start=front.index('\\label{series:II:'+letter+'}')
 start=front.index('\\textit{Relation to literature.}',start)
 end=front.index('\\hyperlink{outline-II-'+letter+'}',start)
 claims.append({'main_theorem':letter,'locations':['1.2','1.4'],'literal_current_claim':front[start:end].strip(),'three_way_verification':'OPEN; split compound claims and bind final statements and final deposit fields during the provenance pass'})
record={
 'created_utc':dt.datetime.now(dt.timezone.utc).isoformat(),
 'source_sha256':hashlib.sha256(raw).hexdigest(),
 'frontmatter_region_sha256':hashlib.sha256(front.encode()).hexdigest(),
 'actual_reading':'Root actually read the entire source from begin{document} through the end of Common conventions, in contiguous bounded outputs: title, abstract, series paragraph/table, all seven complete main statements, all literature paragraphs, all further-result table rows, all seven outlines, Known and new, Methodology, organization/figure and conventions. This is a preliminary source reading, not a final global proof verification or rendered-PDF reading.',
 'publication_page_reading_credit':0,
 'defect_classes_closed':[],
 'source_changes':0,
 'provenance_claims':claims,
 'required_editorial_work':[
  'D01/D08: Main A refers to earlier auxiliary claims, G refers to the former fan-independent clause; actual/retained/supplied and surviving process words remain in main statements and mechanisms. Preserve every assertion and replace the production references by exact mathematical statements and primary locators.',
  'D02/D11: Main D repeats absent-hypothesis language; state its full unrestricted positive domain once, retaining every quantified conclusion.',
  'D10/D15: Further results is a long result/tag table covering most of the body. Replace it by the requested one-line mathematical list with resolving statement references. Machine-style full-statement and outline-return text remains after each main statement.',
  'D12/D15: Every Known and new entry repeats its literature paragraph almost verbatim. Give one concise status line per main theorem, with exact primary locators and a separate inventory of each provenance assertion.',
  'D15/D18: G still cites an attached-source edition. Use the exact opened version and its matching pages. E attributes the untwisted tuple only through Paper I; verify the original DGKX version and precise locator during the scheduled provenance check without reopening the closed Paper I source.',
  'D15: Methodology still states the counts932,34,102,659,259,2 and revision date21November. Recompute all six counts from the final event associations, preserve actual model effort disclosures and dates, and verify the extra September authorship claim from the supplied records.',
  'D24/D10: Organization says headers contain local uses and outline links, contrary to the required tag-only format. Rewrite after the body has been restructured, and regenerate the dependency figure from the actual supplying arguments.',
  'D14: Main C and its sign/equality dependencies span the large irreducible and unrestricted support sections. Determine an order from precise dependencies, retaining all required hypotheses, and split sections to readable lengths. The already completed B5/WP authority consolidation is a precedent, not a license to merge assertions without proof comparison.',
  'D20: Common conventions explicitly identifies peripheral coefficients r1,r2 with l1,l2, and main E reuses r1,r2 for residues. Give the exact conversion once and choose consistent names at the final notation pass. Do not alter the marked lattice basis or period normalization without its exact transport map.',
  'D18/D19/D10: Final resolving cross-paper references, equation numbers by section and visible permanent tags require the integrated typesetting pass. The present inherited numbers are historical locators.'
 ],
 'provenance_gate':'Only the separately recorded records-link claim has a current canonical II row. The full claim inventory, primary-source and online literature-status checks, final recount and deposit-field comparison remain open. This preliminary extraction creates no done claim or progress movement.'
}
out=R/'records/S6_SERIES_PUBLISH_II_frontmatter_source_review_continuation2.json'
assert not out.exists();out.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'path':str(out.relative_to(R)),'sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'main_literature_paragraphs':len(claims),'page_readings':0},indent=2))
