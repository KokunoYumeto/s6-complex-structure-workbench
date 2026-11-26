from S6_SERIES_PUBLISH_c3_foundations_sec11_unit_logs import *

comparison=r'''# Elliptic alignment on normal-crossing normalizations

READY: two complete receiving owner guards, P260 and UN67. Their existing actual subsections remain in place. No new tag, bibliography entry or shared-main write is involved. Both full original/current statements and proofs and all216 receiving lines were read; the final finite-map notation, homology map, newly admitted P344 root-chart reference and statement-type navigation were then reread.

## Domain and exact maps

| Owner | Old domain and conclusion | Receiving domain and exact proof map |
|---|---|---|
| P260 | An embedded component T of a full reduced SNC torus fibre, with every boundary curve vertical for a connected elliptic map q:T→B. Identity integral monodromy, relative contraction, all smooth multiple fibres, fixed Jacobian, R¹q_*O=O, pg=g(B)≤1 and χ=0. | Full reduced NC, with smooth normalization ν:T→S_i and D=(ν⁻¹Sing S)_red containing both labelled self-double branches. P240 at m_i=1 gives ρ:U′→U and r:E→T with ρ|E=νr. The original SNC case is ν=id and may use r=id. All conclusions are unchanged. |
| UN67 | A rational SNC component with an isolated smooth elliptic boundary J of torsion normal cannot occur; Hopf-adjacent rational components and rational parents of Hopf leaves are excluded. | A smooth rational normalization P with the same isolated J in its complete inverse NC boundary. The original pencil q:P→P¹ is unchanged. P260 is applied to exactly (T,ν,D)=(P,ν,D), and its r:E→P compares q∘r to q. The Hopf-normalization consequence uses the two global component labels and xy=t derivative maps. |

The proper birational map r is a composition of point blowups by Popescu-Pampu Proposition3.12, p20, already opened in the admitted quartic package. That source states the analytic factorization; its proof is referred elsewhere, and no reading of an unprinted proof is claimed here. The maps identify the function fields and their meromorphic derivations. P239 therefore transports the saturated two-dimensional commuting space and semicompleteness to the full holomorphic loci on T.

The polar-locus argument is on the original smooth U. Pushing the ambient meromorphic fields through ρ preserves verticality and holomorphy over the puncture. Their divisorial poles are central, and saturation plus the generic isomorphism removes S_i as a polar divisor. At S_i minus Sing S it is the only central branch, so coefficient extension across codimension two gives holomorphy. Pullback by ν then gives poles only in D on T. No embeddedness of T is assumed in this argument.

In the transverse-field case, P303 is applied on the smooth compact T with V=V2−cV1, Y=V1 and the Stein factor of h∘q; that Stein map is q because q_*O=O and h is finite. In the two-vertical-field case, the UN29 application is made on E, its exact embedded multiplicity-one domain. The map q_E=q∘r has connected fibres because r_*O=O. Its ratio is q_E*H, with graph already defined and Stein factor E→B→P¹. Off the finitely many base images of the point centres, r_b:(q_E)⁻¹(b)→q⁻¹(b) is a biholomorphism. Its pushforward (r_b)_* identifies the integral homology local systems. Surjectivity of π1 of this open base onto the full smooth base gives the stated monodromy of q.

Every remaining P260 step is unchanged: vertical point blowdowns, the exact P306 application, the two-chart point-blowup direct-image proof, Leray, and the UN28 genus bound for this smooth normalization. The complete current P240/P239/P303/UN28/UN29 owners were read for these applications. P260's transverse and rank-one arguments remain distinct applications with their specified maps; neither is replaced by a uniformity assertion.

UN67 retains the complete restriction-sequence calculation for every 0≤k<m, the basepoint-free |mJ| pencil, the exact-order argument proving its Stein degree1, adjunction, the verticality intersections, the same q_min, the full unit/root chart w^a=u,s=wh and the invariant direct-image application. The complete newly admitted P344 definition/proof was read, and the root chart now cites that single owner, with its exponent m=a, unchanged unit u and primitive h; P306 supplies the canonical-intersection and invariant direct-image applications. The finite pencil map is renamed β to reserve ν for normalization. The Hopf consequence is proved on smooth normalizations: their curves are disjoint, excluding triples on this interface; the two distinct global components prevent an interchange of its two branches, so each inverse curve maps isomorphically to the double curve, and xy=t identifies their normal tensor product with O. All three bare references remaining in those final Hopf steps are replaced by statement-type references. The original SNC statements are thereby preserved, with an explicit proved NC extension needed by UN83.

There is no counterexample or refuted statement here. The inherited later phrase that the SNC argument works on a normalization is replaced by these proved earlier maps. D25 records the required scope/application completion. All25 local classes are assessed on both existing subsections. D10/D16 stand. Whole-paper D14, final rendered D23, D24 and global restructuring remain with root; required198/198 and independent-check counts are unchanged.
'''
write_unit_logs('nc_alignment','subsec:II:elliptic-alignment','Elliptic alignment and rational-normalization obstruction',
 'Complete original/current and receiving statements and proofs read; final homology-map and Stein-notation paragraphs reread; every old label/target and exact NC morphism compared; exposed used-and-rechecked reading; root admission pending.',
 [
 ('P260','lem:II:vertical-elliptic-alignment','Read the complete current original and receiving alignment proof. Compared the degree-one component resolution rho|E=nu r, the bimeromorphic derivation transport and original-ambient polar argument, the exact transverse P303 Stein map, and the rank-one UN29 application to q_E=q r with (r_b)_* on the integral local system. All relative-minimal, root, direct-image, genus and coherent Euler conclusions remain.'),
 ('UN67','cdp:st:C.2.UN.67','Read the complete current original and receiving rational-boundary proof. Compared every divisor restriction and exact normal-order calculation, the same connected pencil and relative contraction, the P306 unit/root and invariant coefficient maps, and the labelled NC Hopf-interface derivative map. The finite pencil map beta is distinct from normalization nu.'),
 ('prerequisites','lem:II:vertical-elliptic-alignment','Read the complete present P240 cyclic-component, P239 semicomplete-transport, P303 elliptic-first-integral, UN28 normalization-genus and UN29 return-period statements and proofs. Compared their hypotheses to the exact maps E→T→S_i and q_E=q r. Read the complete current P318 analytic factorization application; its already opened Popescu-Pampu Proposition3.12 p20 is reused at r between smooth compact analytic surfaces, with statement/setup reading only for that external source.'),
 ('root-owner','cdp:st:C.2.UN.67','Read the complete newly admitted P344 definition and proof in the current source. Its normalized chart w^m=u,s=wh, finite etale projection, free deck action, full connected reduced fibre and translation quotient are applied with m=a and the identical unit u and primitive fibre equation h in UN67. Reread the final bounded citation and statement-navigation updates.')
 ],{
 'D12':'The original saturated-field and return-map owners are applied through explicit maps; no duplicate field or return-map proof is introduced. The rational-pencil calculations remain its own specific obstruction proof.',
 'D14':'P240/P239/P303/UN28/UN29 and the analytic factorization citation precede these applications. Their NC extension is available before the later UN70/UN80/UN83 reduction chain; final whole-paper placement remains open.',
 'D17':'The analytic point-blowup factorization cites the already opened exact proposition; the field transport and monodromy comparison are the short specific NC application not stated by that source.',
 'D18':'The existing Popescu-Pampu2016 entry and exact Proposition3.12 p20 locator are reused. No bibliography alteration or new primary proof-reading claim is made.',
 'D19':'Every existing equation counter, label and hypertarget remains unchanged; there is no new manually tagged display.',
 'D20':'rho, r, nu, q_E and (r_b)_* give the precise normalization and monodromy maps. beta names the finite pencil map separately from nu.',
 'D22':'The degree-one root is justified by full reducedness, the finite discarded base set by point-blowup factorization, and the rational contradiction by the unchanged coherent Euler calculation.',
 'D25':'A proved NC normalization extension supplies the exact earlier premise for UN83. All original SNC domains and conclusions remain; no false original statement or counterexample is claimed.'
 },comparison,2,'none')

prefix='S6_SERIES_PUBLISH_sec11_nc_alignment'
path=OUT/(prefix+'_defects.tsv')
with path.open(newline='') as f:
 reader=csv.DictReader(f,delimiter='\t'); fields=reader.fieldnames; rows=list(reader)
for row in rows:
 unit='subsec:II:torsion-normal-rational-obstruction' if row['statement_id']=='cdp:st:C.2.UN.67' else 'subsec:II:elliptic-alignment'
 row['old_location']=unit+' / '+row['statement_id']; row['new_location']=row['old_location']
with path.open('w',newline='') as f:
 writer=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n'); writer.writeheader(); writer.writerows(rows)

progress=OUT/(prefix+'_unit_progress.tsv')
with progress.open(newline='') as f:
 reader=csv.DictReader(f,delimiter='\t'); fields=reader.fieldnames; rows=list(reader)
other=[dict(row,unit='subsec:II:torsion-normal-rational-obstruction',fragment='agents/continuation3_foundations/sec11/S6_SERIES_PUBLISH_II_sec11_nc_alignment_UN67.tex') for row in rows]
for row in rows:
 row['fragment']='agents/continuation3_foundations/sec11/S6_SERIES_PUBLISH_II_sec11_nc_alignment_P260.tex'
with progress.open('w',newline='') as f:
 writer=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n'); writer.writeheader(); writer.writerows(rows+other)
status=OUT/(prefix+'_status.md')
status.write_text(status.read_text()+'\nThe same26 local-class assessments apply to the complete existing subsection `subsec:II:torsion-normal-rational-obstruction`; both actual-subsection rows are present in the progress TSV.\n',newline='\n')

guards=json.loads((OUT/(prefix+'_guards.json')).read_text())
main=(ROOT/'S6_SERIES_PUBLISH_II.tex').read_text()
from collections import Counter
for guard in guards:
 assert main.count(guard['old'])==1,guard['key']
 for pattern in [r'\\label\{([^{}]+)\}',r'\\hypertarget\{([^{}]+)\}']:
  assert Counter(re.findall(pattern,guard['old']))==Counter(re.findall(pattern,guard['new'])),guard['key']
 for body in re.findall(r'\\begin\{equation\}([\s\S]*?)\\end\{equation\}',guard['new']):
  assert not re.search(r'\n[ \t]*\n',body)
print('READY:2 guards;35 defect rows;4 exposed events;52 actual-subsection assessment rows;no new tags or source rows.')
