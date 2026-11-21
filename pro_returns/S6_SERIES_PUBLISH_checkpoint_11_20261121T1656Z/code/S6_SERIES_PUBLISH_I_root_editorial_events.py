from pathlib import Path
import csv,json,hashlib,datetime
r=Path(__file__).resolve().parents[1]
out=r/'records/S6_SERIES_PUBLISH_I_root_editorial_CHECK_EVENTS.tsv'
assert not out.exists(), 'Do not overwrite a saved event file.'
date=datetime.datetime.now(datetime.timezone.utc).date().isoformat()
who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; reasoning effort inherited, no separate numerical setting exposed; S6_SERIES_PUBLISH root'
groups=[
 ('marking',['inv:B1.0'],'code/S6_SERIES_PUBLISH_I_conventions.py',
  'Compared the original marking result and its replacement. The explicit P_mark,S,Q maps intertwine both supplied monodromy matrices; their determinants and affine-vector signs were checked exactly. Repeated theta and parameter arguments are cited at their complete proofs. This is editorial rechecking, with no blind-derivation claim.'),
 ('determinant',['I:period-determinant'],'records/S6_SERIES_PUBLISH_I_root_comparison_01.json',
  'Compared the consolidated period-determinant/exterior-form statement with the previously printed identities and the exact exterior-algebra output. The determinant is yD, the marked eta-square coefficient is12 (complex orientation -12), and eta wedge Gamma wedge d-zeta2 has coefficient1. No new independent experiment is inferred from the new label.'),
 ('modular',['inv:A2.3','inv:A2.2'],'records/S6_SERIES_PUBLISH_I_modular_consolidation_comparison.json',
  'Read the original and consolidated modular proofs against one another. The section-group proof is cited once; the exact mu=1-z0 branch map, order-two contact, finite specializations and certified scalar bounds remain. The removed alternate proof is in the edit record. The earlier preread/compute events retain their separate narrower scopes.'),
 ('classification',['fam:src:A.2.1','wb:pshift:lem:centralizer','fam:src:A.5.1'],'records/S6_SERIES_PUBLISH_I_classification_consolidation_comparison.json',
  'Compared the body and complete classification-appendix arguments before consolidation. The exact centralizer, middle-family sign, finite cyclic-norm obstruction, global additive correction and intrinsic pencil are retained at their single proofs. Alias associations share this one comparison group.'),
 ('family_deformation',['fam:src:A.3.1','fam:src:A.4.2','wb:thm:retained-period-deformation'],'records/S6_SERIES_PUBLISH_I_period_deformation_comparison.json',
  'Compared both complete family/deformation proofs and the fuller sixteen-step WB proof. The unique F/submersion scope, all18 PD formula markers, uniform cusp constants and compact representatives, marked real-linear map, inverse, graph/KS sign, relative canonical map and dual-number critical-value calculation are preserved. Covariance is transported by M_g=A_g^{-1}. This is one editorial comparison, not three independent proofs.'),
 ('canonical',['fam:src:A.1.1','wb:thm:canonical-ring-recovery'],'records/S6_SERIES_PUBLISH_I_canonical_ring_comparison.json',
  'Compared the complete canonical/divisor/ring proof with the earlier body statement. Preserved the evaluation divisor, meromorphic subsheaf equality, graded generator map, basis and coordinate changes. The affine/cusp translation scope is carried by the explicit wedge cancellation; the intrinsic-base conclusion follows from the preserved pencil and fibre invariants.'),
 ('automorphisms',['fam:src:B.4.1','night:P5.5'],'records/S6_SERIES_PUBLISH_I_automorphism_comparison.json',
  'Read and compared both complete automorphism proofs. The broader admissible-twist scope, finite-root obstruction, local compactified translation sheaf, full integral lattice calculation and all components remain in one credited proof. The alternate coefficient lattices are related by the exact recorded unimodular map.'),
 ('common_root',['inv:D1.1','inv:D1.2','push:src:E.3.1','fam:st:A.5.2'],'records/S6_SERIES_PUBLISH_I_common_root_comparison.json',
  'Compared the full original Picard, vertical-bundle, cusp/base-change and first tangent appendix proofs with the existing Koszul/KS/Kuranishi route. The single early proof now contains the explicit coarse degree, root quotient map, complete branch resolution/cup pairing, exponential vertical-field map, ordinary-kernel divisibility, discriminant line, trace and nonvanishing cocycle extension. The alternate first tangent proof is archived; the full remaining direct-image and deformation proofs are retained. This row certifies this consolidation scope, not the later unfinished tangent restructuring.'),
 ('metric',['inv:C3.6'],'records/S6_SERIES_PUBLISH_I_metric_application_comparison.json',
  'Read the complete supplied application proof and independent comparison before restoring its operative argument. K_X^2=f^*O(-1), Chern–Ricci=2pi c1BC, the prescribed pi f^*FS form and preservation of the Gauduchon-square Aeppli class agree. The classical theorems are cited; the positive pairing supplies the nonzero class. No independent PDE proof is claimed.')
]
rows=[]
for group,ids,source,scope in groups:
 assert (r/source).exists(),source
 eg='eg:publish-I-root-editorial-'+group
 for label in ids:
  suffix=hashlib.sha256((group+'|'+label).encode()).hexdigest()[:16]
  rows.append(dict(statement_id=label,date=date,who=who,type='used and rechecked in this run',outcome=scope,
    event_id='ce:publish-I-root-editorial-'+suffix,phase='S6_SERIES_PUBLISH_I',source_file='work/'+source,
    source_row=str(len(rows)+1),source_event_type='used and rechecked in this run',evidence_group=eg))
for label in ['fam:src:B.4.1','night:P5.5']:
 suffix=hashlib.sha256(('aut-coordinate-map|'+label).encode()).hexdigest()[:16]
 rows.append(dict(statement_id=label,date=date,who=who,type='computation or formal certificate',
   outcome='PASS for the exact comparison of the two integral cocycle coordinate systems: K*T=Q, Q*L=-C, det(T)=1, det(L)=-1. This new post-reading SymPy multiplication checks the specified integral transport only; it is not a whole-result independent proof or a preread computation. Both associations share one actual calculation.',
   event_id='ce:publish-I-aut-transport-'+suffix,phase='S6_SERIES_PUBLISH_I',
   source_file='work/records/S6_SERIES_PUBLISH_I_aut_lattice_transport.json',source_row=str(len(rows)+1),
   source_event_type='computation or formal certificate',evidence_group='eg:publish-I-aut-coordinate-map'))
with out.open('w') as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t');w.writeheader();w.writerows(rows)
print(json.dumps({'rows':len(rows),'evidence_groups':len({x['evidence_group'] for x in rows}),'file':str(out)}))
