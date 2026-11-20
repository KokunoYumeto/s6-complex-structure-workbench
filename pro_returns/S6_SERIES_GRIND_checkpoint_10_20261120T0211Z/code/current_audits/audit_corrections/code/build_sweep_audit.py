from pathlib import Path
import csv, json, hashlib, datetime, re

root=Path(__file__).resolve().parents[3]
src=root/'S6_SERIES_GRIND_source'
out=root/'S6_SERIES_GRIND_work'/'audit_corrections'
base=src/'S6_GRIND_1_papers_cp15'
papers={r:(base/f'S6_10_PAPERS_{r}.tex').read_text() for r in ['I','II','III','IV','V','VI']}
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
who='GPT-6 Astra (OpenAI), ChatGPT Pro mode, reasoning effort inherited from root (not separately exposed), S6_SERIES_GRIND/corrections_audit'
events=[]
def event(label,kind,outcome):
 d={'statement_id':label,'date':'2026-11-19','who':who,'type':kind,'outcome':outcome,'phase':'S6_SERIES_GRIND'}
 d['event_id']='s6sg:'+hashlib.sha256(json.dumps(d,sort_keys=True).encode()).hexdigest()[:20]
 events.append(d)

rows=[
 (1,'carried','maps:src:D.2.11;night:P3F.34','The printed D.2.11 explicitly assumes gcd(n,3k)=1. With g=gcd(3k,n,3d), divisibility g|gcd(3k,n) proves g=1 in that scope. The cap (m,n,d)=(9,3,1) has k=3 and gcd(n,3k)=3, outside that scope. The unrestricted free-cap formula extends the printed theorem.','No theorem repair; preserve the hypothesis in the inventory summary.'),
 (2,'local_scope_patch_required','night:P3K.7;night:P3K.8;night:P3F.17','C.3.24/C.3.27/C.4.1 and B.6.2/B.6.21/B.6.24/B.6.25 explicitly retain the reference fan. K7/K8 rely on their section for this datum; F17 page data retains the P3F.10 boundary marking in its proof. E.1.3 transports the fixed data by W=(-1)^s2 w, so the same positive loop is carried by a holomorphic rotation.','Add the reference fan and actual collar/boundary marking to K7/K8/F17 statements; keep E.1.3 as the stated fixed-data comparison.'),
 (3,'carried','maps:src:B.6.17;maps:src:B.6.20;night:P3K.9;night:P3K.11','All four statements now print both line conventions or their exact transport. The nonzero-vector map D(v)(v)=1 satisfies D(cv)=c^{-1}D(v). On the fixed oriented quotient x_M=-x_U and y_M=-y_U, hence (k_M,l_M)=-(k_U,l_U).','No sign replacement; retain the actual duality morphism and framing.'),
 (4,'carried_structurally','series:sweep:4','There are exactly 33 iv:correction:* receiving labels in IV and 33 corresponding inventory labels. These separate the historical false compound claims from retained/corrected conclusions. The prompt count 34 is a one-row overcount; its total 39 high-risk rows is correct using 33.','Audit each actual correction proof separately; compilation and label presence give no mathematical credit.'),
 (5,'carried','ari:C.5.1','The printed statement quantifies simultaneous CM and torsion and explicitly records completed-fibre orders 3 and 2. It does not claim the torsion locus is confined to those two fibres.','Keep the simultaneous condition in all one-line summaries. Source-theorem verification remains its separate existing gate.'),
 (6,'inherited_hypothesis_made_local','cdp:st:C.2.INT.3','C.2.INT.3 imports C.2.INT.2, whose exact hypotheses include smooth compact complex dimension three, H^2(Y;Q)=0, proper connected-fibre map and general complex two-torus.','Expand that hypothesis in C.2.INT.3 itself to make the scope visible without following a link.'),
 (7,'carried','maps:src:D.2.24;maps:src:D.2.27;maps:src:D.2.28','The three statements explicitly cite the natural section-line and local filling sector of D.2.22. D.2.22 names M=O(P-O), permitted additive/multiplicative fillings, and an optional larger O(P-O+V) construction separately. The star exclusions retain the natural sector.','No repair to these scopes. Preserve the sector in frontmatter and summary tables.'),
 (8,'carried','cdp:st:E15;inv:E2.2;inv:E2.3','E15 specifies constructed positive combs, including m>=12, and its proof defines G=R^1 f_*O via the quotient of the full de Rham extension and explains finite-root and cusp comparison. E2.3 now leaves only K_m splitting and h^0(K_m) open and credits the established Kuranishi germ to E15.','No status promotion for the remaining comb splitting. At m=12 the printed Kuranishi dimension is 97.'),
 (9,'carried','night:P2.2','The exact finite-difference formula has radial gamma coefficient an. P2.1 fixes a=-p, so substitution gives -pn. P2.2 prints this value and the fixed conventions.','No further sign edit.'),
 (10,'carried','night:P1.5;night:P1.8;maps:src:F.3.6','F.3.6 prints a rank-three subbundle. P1.5 explicitly supplies the full rank-four de Rham bundle as the domain of ell_0 wedge -, and P1.8 uses that corrected bundle.','Retain the linear-algebra correction. For nonzero ell_0 in a four-dimensional space V, kernel(ell_0 wedge -)=span(ell_0), so the image has dimension three.'),
 (11,'carried','maps:src:E.1.1;maps:src:E.1.2;maps:src:E.1.3;maps:src:E.1.4','E.1.1 states the precise normalization failure; E.1.2 identifies Z as a small crepant resolution of a Weierstrass model over X, bimeromorphic to the literal product, and E.1.3/E.1.4 compute the resolved cusp and Euler number six.','Keep the resolved construction and its actual morphisms; moving this block to V must retain its distinction of local models by the displayed birational maps.'),
 (12,'notation_update_required','series:sweep:12','The inherited notation sheet retains a stale three-paper 1184-row section and local symbol meanings. This audit finds the physical line transport explicit in B.6.17/B.6.20 and K68, but has not certified every symbol occurrence.','Root should replace stale series counts and add local-to-series identity adapters: admissibility constant M_adm, elliptic source line L_E=O(P-O), fourfold M_c, physical line M with U=M^{-1}, and separate exterior-square/rank-three bundle notation.'),
 (13,'carried_with_source_coverage_gap','push:src:A.3.2;push:src:C.3.12;inv:E2.4;fam:src:B.2.3;inv:A4.2;ari:A.5.7','The five S6 correction statements are present. AC26 original PDF Remarks 1.3 p5, 9.21 p81 and 9.26 p83 were opened as extracted original-PDF text. E26 source Additional remarks was opened. The ARI A.5.7 side-lane correction is absent from the inherited inventory, along with all 27 current A rows.','Add explicit source-coverage records for the 27 A rows; source-backed editorial exclusion is available from sweep13 side-lane designation, but final disposition belongs to root. Do not silently treat source presence as inventory integration.'),
 (14,'carried_at_checked_dependencies','maps:src:B.6.23;maps:src:D.2.17;maps:src:D.2.21;maps:src:E.2.6;maps:src:E.2.14;ari:C.2.2;ari:C.6.R3;push:src:E.2.23;push:src:E.3.1','The three typo cases use the dotted canonical labels. E.2.6 and E.2.14 now use actual receiving equation/theorem labels. ARI C.2.2 uses fam:B.4.2. Demailly and Grauert/Banica-Stanasila are bibliography citations. C.6.R3 cites Gross-Zagier with its other named inputs.','Regenerate cross-paper links during assembly. Presence and resolution of dependencies are an apparatus check, not proof re-derivation.'),
 (15,'cp36_carried_missing_three_tracked','series:sweep:15','The supplied night register has 299 rows at cp36, and cp15 paper text carries K113-K119. Missing P1.6/P1.14/P5.7 are explicitly identified; their preservation and integration instructions accompany this report.','Use cp36 as source identity; import the two reported classification checks and insert the credited P5.7 comparison.'),
 (16,'scoped_exclusion','series:sweep:16','No Q03 rows occur in the inherited S6 inventory and no dedicated Q03 deliverable is present in the attached tree. Sweep16 directs a separate tag space for its scheduling manuscript.','Record the editorial scope choice from sweep16. This asserts no absence of mathematical relations between the subjects and gives no proof check to the scheduling results.'),
]
with (out/'sweep_16_audit.tsv').open('w',newline='') as f:
 w=csv.writer(f,delimiter='\t');w.writerow(['item','state','labels','finding','action']);w.writerows(rows)
for n,state,labels,finding,action in rows:
 for lab in labels.split(';'):
  kind='targeted proof check' if n in [1,3,9,10] else 'used and rechecked in this run'
  event(lab,kind,f'Sweep correction {n}: {finding} Action: {action} Scope: the stated correction only; this event does not certify the entire receiving proof.')

patches=[]
def replace(paper,label,old,new,reason):
 assert papers[paper].count(old)==1,(label,papers[paper].count(old))
 patches.append({'paper':paper,'label':label,'old':old,'new':new,'reason':reason})
replace('IV','night:P3K.7',
'The real trace gives a spin bordism carrying the Euler line from the actual covered conifold return to a normal sphere bundle.',
'For the reference cusp fan of \\cite{AC26}, with the lattice basis, boundary marking, and collar maps of \\cref{night:P3F.10}, the real trace gives a spin bordism carrying the Euler line from the actual covered conifold return to a normal sphere bundle.',
'Sweep2: make the reference-fan scope local to the statement.')
replace('IV','night:P3K.8',
'The same actual return index vanishes by a second calculation: vertical sphere quantization, an explicit marked cap switch, and acyclicity of the elliptic Picard line.',
'For the reference cusp fan, lattice basis, boundary marking, and collar maps of \\cref{night:P3K.7}, the actual return index vanishes by a second calculation: vertical sphere quantization, an explicit marked cap switch, and acyclicity of the elliptic Picard line.',
'Sweep2: make the reference-fan scope local to the statement.')
replace('IV','night:P3F.17',
'For coprime multiplicities $(3k,4l)$ the regular-binding page has degree $12kl$, Euler characteristic $12kl$, signature $-8kl$, section-line square $-2kl$ and relative Pontryagin pairing $-24kl$.',
'For coprime multiplicities $(3k,4l)$, retain the reference cusp fan and the regular-binding boundary marking of \\cref{night:P3F.10}. The resulting page has degree $12kl$, Euler characteristic $12kl$, signature $-8kl$, section-line square $-2kl$ and relative Pontryagin pairing $-24kl$.',
'Sweep2: expose the actual page and boundary scope used in the proof.')
replace('IV','iv:correction:P3K.22',
'At the retained effective smooth-site\ncaps the first homology contribution\n\\((\\mathbb Z/m_i)^2\\) forces every such \\(m_i=1\\) in a sphere\nmember, with total signed order-one norm \\(\\pm1\\).',
'At the retained effective smooth-site caps, the injective\ndegree-two homology term \\(\\bigoplus_i(\\mathbb Z/m_i)^2\\)\nin \\(H_2(Y;\\mathbb Z)\\), given by the actual Mayer--Vietoris\nsequence (P3K.22.1) in \\cref{night:P3K.22}, forces every\n\\(m_i=1\\) in a sphere member, with total signed order-one\nnorm \\(\\pm1\\).',
'The retained source exact sequence (P3K.22.1) places this injective term in H_2(Y;Z), not H_1(Y;Z). Preserve the actual rim-cycle map and its degree.')
replace('VI','cdp:st:C.2.INT.3',
'Let $f:Y\\to B$ satisfy the hypotheses of \\ref{cdp:st:C.2.INT.2},\nand let $S$ be a connected reducible fibre support.',
'Let $f:Y\\to B$ be a proper connected-fibre map from a smooth\ncompact complex threefold with $H^2(Y;\\mathbb Q)=0$ and general\nfibre a complex two-torus, as in \\ref{cdp:st:C.2.INT.2}.\nLet $S$ be a connected reducible fibre support.',
'Sweep6: state the existing H^2=0 hypothesis at the point of use.')
(out/'proposed_patches.json').write_text(json.dumps(patches,indent=2)+'\n')

# Every latest A register row absent from cp15 is listed, with its source
# status retained. Recommending editorial scope is not a mathematical claim.
with (base/'S6_10_PAPERS_inventory.csv').open() as f:inv=list(csv.DictReader(f))
existing={(r['source_run'],r['source_id']) for r in inv}
a_base=src/'S6_GRIND_5_research_runs_tex'/'returns'/'S6_05_ARITHMETIC'
arows=[]
for p in sorted(a_base.glob('results_A*.csv')):
 with p.open() as f:
  for r in csv.DictReader(f):
   if ('S6_05_ARITHMETIC',r['id']) in existing:continue
   arows.append({'source_run':'S6_05_ARITHMETIC','source_id':r['id'],'statement':r['statement'],
    'source_status':r['status'],'source_register':str(p.relative_to(src)),
    'source_proof':r['where_proved'],'disposition':'pending root editorial disposition',
    'recommendation':'Account explicitly as omitted from this five-paper editorial selection; retain the original source proof in the attached base. Sweep13 explicitly calls A.5.7 a side lane; the current ARI report groups A.1-A.5 under The count and C.1-C.8 under family arithmetic. This recommendation asserts no absence of mathematical relations.',
    'scope_evidence':'sweep1_s6/CORRECTIONS.md item13; S6_05_ARITHMETIC_report.md item table and The count section; sections/A.tex definition of F(s,t,z)=s^2-3t^2-18z^2.'})
with (out/'missing_ari_A_rows.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(arows[0]));w.writeheader();w.writerows(arows)

event('night:P3K.68','computation or formal certificate','Fresh independent_orientation_checks.py derives quaternion Hopf derivatives, Cox/projective determinant signs, exterior-form collar transgression, and global x -> -x characteristic transport without importing earlier code. All exact checks pass. This confirms the displayed arithmetic and orientation maps; it gives no substitute for primary-source verification of Jin coordinates.')
event('night:P3F.22','computation or formal certificate','Fresh independent_orientation_checks.py expands exp(z/2) A-hat in degree eight, eliminates p2 via the signature polynomial, computes the inverse intersection pairing for [[0,1],[1,k]], and obtains mu(lambda(f))=(4k-l)/672. At (k,l)=(8,8) this is +1/28, agreeing with the imported second-model derivation. Geometric realization, gluing direction and the given Jin coordinates are retained inputs.')
event('maps:src:F.4.1','independent re-proof','Classification implication independently written in fourfold_classification_prereading.md before reading the target proof. Given P1.12/P1.13, the diagonal cohomology isometry preserves q and p1 and hence the full normal clutching pair; Wall extended-form classification gives the oriented almost diffeomorphism, and Kramer-Stolz Theorem A absorbs the sphere in a positive HP2 summand. Source statements opened: Kramer-Stolz p178 and Conway-Crowley-Powell-Sixt Definition3.6/Theorem3.7. Construction and characteristic inputs are not independently re-proved by this event.')
with (out/'CHECK_EVENTS.tsv').open('w',newline='') as f:
 w=csv.DictWriter(f,delimiter='\t',fieldnames=['statement_id','date','who','type','outcome','event_id','phase']);w.writeheader();w.writerows(events)
print(json.dumps({'sweep_items':len(rows),'patches':len(patches),'missing_ari_A_rows':len(arows),'events':len(events),'timestamp':now},indent=2))
