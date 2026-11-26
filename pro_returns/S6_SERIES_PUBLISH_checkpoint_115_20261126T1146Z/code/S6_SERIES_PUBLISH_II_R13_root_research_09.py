from pathlib import Path
import datetime as dt, hashlib, json

R=Path(__file__).resolve().parents[1]
sha=lambda b:hashlib.sha256(b).hexdigest()
P=R/'agents/continuation2_C/S6_SERIES_PUBLISH_II_C2_R13_publication_P205'
idx=P/'S6_SERIES_PUBLISH_II_C2_P205_publication_index_final_v1.json'
assert sha(idx.read_bytes())=='cf297742df692b417f37c2e4a4246da74ae48f157c8d91c5a665da3dd4412424'
d=json.loads(idx.read_text());verified=[]
for row in d['files']:
    p=R/row['path'];b=p.read_bytes()
    assert len(b)==row['bytes'] and sha(b)==row['sha256'],row['path']
    verified.append(row)
def binding(p):
    b=p.read_bytes();return dict(path=p.relative_to(R).as_posix(),bytes=len(b),sha256=sha(b))
proposal=P/'S6_SERIES_PUBLISH_II_C2_P205_proposal_final_v1.tex'
assert sha(proposal.read_bytes())=='6b6d81b18ee5ca89a582b5d6e80164186930a6216ae60dfd55165064f9ba07b4'
items=[
 'Read all integral matrices Ai,Ci and the actual conjugacy AiCi=CiAloc, with the homology basis and meridian convention.',
 'Read the entire real-parameter representation, its rank-one square-zero logarithms, lattice D_epsilon P Z4 and exact conjugacy.',
 'Read the Klein-four base cover, marked lifts, full jointly holomorphic canonical extension, corrected Grauert application, evaluation isomorphism and character projectors. These agree with the primary pages actually read in research07.',
 'Read all twistor rows and row transformations, the cubic equivariant map, logarithmic determinant expansion, fixed-disc uniform positivity and the real evaluation map defining the proper group family.',
 'Read the exact local lattice normalization, continued-versus-endpoint marking comparison, parity, negative sign of Im(tau), and odd coordinate absorption of gamma.',
 'Read every chain-chart transition and period action, the invariant norm, uniform proper-discontinuity bound, two-chart compact representative construction and actual nearby lattice.',
 'Read every formula for g and g squared, freeness on regular and central loci, full multiplicity two, the component-to-support finite map, its induced normalization, the sign line and the two degree-two conductor maps.',
 'Read both affine descent formulas and the exact translation Phi, its monodromy, equivariance and inverse.',
 'Read the central I2 specialization chain, invariant cohomology representatives, transfer square and deformation preserving the tube, chosen fibre, boundary and marking. No dimension-only replacement of restriction maps is used.',
 'Read the integral conductor amalgam, nearby homology inclusion, index-two integral restriction image and explicit zero-section boundary loop. The loop value is transported by the same marked-pair deformation.',
 'Read the literal open cover with annular overlaps, the exact gluing maps and inverses, Hausdorffness, properness, compactness and connectedness.',
 'Read all alpha pullbacks, local loop values, Mayer--Vietoris matching equations, vanishing of H1 and the primitive integral transgression in its explicitly stated sign convention.',
 'Read the sheaf stalk identifications, H1 of j-star V computation, the printed exterior-square minor, all degree-two Leray terms, Euler additivity and Poincare duality giving b3=2.'
]
scope=R/'agents/continuation2_C/S6_SERIES_PUBLISH_II_C2_R13_scope_final_v1'
scope_files=[p for p in scope.iterdir() if p.suffix in ['.json','.md','.tex']]
record=dict(created_utc=dt.datetime.now(dt.timezone.utc).isoformat(),purpose='Root complete publication-proof review of P205 before insertion; continuation of research08.',
    proposal=binding(proposal),index=binding(idx),all_index_file_bindings_verified=verified,
    complete_publication_TeX_actually_read=True,reading_method='Three consecutive untruncated chunks covering characters0:8500,8500:17000,17000:end. The earlier pre-compaction truncated working-draft return receives no credit.',
    proof_item_reviews=[dict(item=i+1,review=x) for i,x in enumerate(items)],
    conclusion='All asserted maps and calculations in the complete publication proof agree with the previously fully read final construction and A pretarget derivation. No mathematical defect found in this publication read-through.',
    other_files_actually_read=[binding(P/n) for n in ['S6_SERIES_PUBLISH_II_C2_P205_publication_review_final_v1.md','S6_SERIES_PUBLISH_II_C2_P205_printed_data_check.py','S6_SERIES_PUBLISH_II_C2_P205_printed_data_check.out','S6_SERIES_PUBLISH_II_C2_P205_syntax_receipt_v2.json','S6_SERIES_PUBLISH_II_C2_P205_programs_row_proposal_final_v1.json']],
    computation_scope='Root read the complete exact-data program and complete successful output. Its equations supplement the actual analytic proof; no independent re-computation claim is added.',
    build_scope='Root read the complete two-pass build receipt; the full raw150235-byte compiler outputs are hash-verified only. No integrated-build or visual-page credit.',
    C_scope_files=sorted([binding(p) for p in scope_files],key=lambda x:x['path']),
    scope_reading_update='After research08 was frozen, root read the full16019-byte scope statement extract and full12192-byte scope JSON, in addition to the previously fully read10512-byte report. Root has not newly read every complete downstream consumer proof; C has.',
    additional_reading='Root read the complete original P4.26/tag02WY statement and all9 proof items to locate the nonnegative-Euler sum bound needed by corrected02XE. The proof cites P4R.7/P4R.9 for ruled resolutions and P4R.8 for Hopf models. C is checking transitive circularity before the final correction is admitted.',
    source_at_review=binding(R/'S6_SERIES_PUBLISH_II.tex'),ledger_at_review=binding(R/'CHECK_EVENTS.tsv'),
    source_mutations=0,events_added=0,required_rows_closed=0,global_defect_classes_closed=0,final_pdf_page_credit=0,
    independence='Postreading publication-proof review. Root had read originals and construction research; no pristine derivation or targeted pretarget check is claimed. A whole pretarget derivation and its collaborative provenance remain at their frozen receipt.',
    pending='A corrected R13/P440/P206 final packet, C mathematical review, exact consumer changes, registry updates and honest event admission.')
out=R/'records/S6_SERIES_PUBLISH_II_R13_root_research_09.json';assert not out.exists()
out.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(dict(record=binding(out),verified_files=len(verified),proof_items_actually_read=13,events_added=0,source_mutations=0),indent=2))
