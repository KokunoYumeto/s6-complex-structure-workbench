from pathlib import Path
import datetime, hashlib, json, re
R=Path(__file__).resolve().parents[1]
def bind(p):
 b=(R/p).read_bytes()
 return dict(path=p,sha256=hashlib.sha256(b).hexdigest(),bytes=len(b))
s=(R/'S6_SERIES_PUBLISH_II.tex').read_text()
expected={
 'cdp:st:C.2.UN.1':'90c79029d02aaea9a3343f45846c57f3812423859180349b784cc1c6b536a016',
 'cdp:st:C.2.UN.2':'aeb29fc7ee341354317ed058532a82ae2656c057b1156422bff080167dada7a2',
 'cdp:st:C.2.UN.4':'2f3fe5d4868736d0ad159bc7d506454d96f22c53147d743621349c43e5689ffe',
 'cdp:st:C.2.UN.14':'5f552c995c7d54660c5e15d18e23f18a3664ef066df31a56b2bfd67aa363a7e8',
 'cdp:st:C2b':'cffaaf498424fe9d43d0bac1e636c6833f2af8e2e349b52d4098812a88dd8c2c'}
blocks=[]
for label,wanted in expected.items():
 p=s.index('\\label{'+label+'}')
 a=list(re.finditer(r'\\begin\{(proposition|lemma|theorem|corollary)\}',s[:p]))[-1]
 b=s.index('\\end{proof}',p)+len('\\end{proof}')
 text=s[a.start():b]
 digest=hashlib.sha256(text.encode()).hexdigest()
 assert digest==wanted
 blocks.append(dict(owner=label,sha256=digest,bytes=len(text.encode()),
                    proof_items=text.count('\\item'),
                    original_full_block_read=True,changed=False))
oa=s.index('\\hypertarget{outline-II-D}{}')
ob=s.index('\\hypertarget{outline-II-E}{}',oa)
outline=s[oa:ob]
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
cert=json.loads((R/'code/S6_SERIES_PUBLISH_II_global_D_root_certificate_01.json').read_text())
assert cert['passed']==118 and all(x['passed'] for x in cert['checks'])
record=dict(created_utc=now,
 checker='GPT-6 Astra (OpenAI), ChatGPT Pro mode, root; reasoning effort not separately exposed',
 scope='Current global theoremD, with final-source binding and final publication review still pending.',
 chronology='MainD statement read in the preceding segment; this segment read five statement-only environments and wrote the reconstruction before deliberately opening the body proofs. Historical root exposure cannot be excluded, so no new independent required-check credit is claimed. Full body blocks and all five D outline steps were subsequently read; C2b was read as the explicit supporting construction.',
 source_at_statement_intake='d082e8cc1d290deca9e8c1855010e6789dd93c9b6fea01c5233984ee0f4120c8',
 current_source=bind('S6_SERIES_PUBLISH_II.tex'),
 blocks=blocks,
 outline=dict(sha256=hashlib.sha256(outline.encode()).hexdigest(),bytes=len(outline.encode()),steps=5,fully_read=True),
 comparison=[
  'UN1 item1: the compact full tube, smooth boundary, orientation, analytic retraction and mapping-torus interpretation have exactly the scope reconstructed. The source supplies controlled-gradient and triangulated regular-neighbourhood descriptions. The final known-result citation audit remains open; no new primary-source reading is claimed here.',
  'UN1 item2: the source adds the three boundary Betti numbers via b_i(M)=b_i(U)-s_i+b_(5-i)(U)-s_(i+1), giving sum b_i(U)-s0-s3-2s1-2s2. The root instead used the upper half of the pair long exact sequence. Both give the same parity because s0=0,b6=0 and the middle alternating form has even rank. The written root difference is exactly2b3-2b4+2b5-r.',
  'UN1 item3: Wang gives1,1+a1,a1+a2. The printed generalized-minus-one eigenspace is even-dimensional by reciprocal eigenvalue pairing and determinant1; it is nondegenerate. On its orthogonal complement G+I is invertible, and(G-I)(G+I)^(-1) is skew-adjoint, giving even rank. This proves the stated parity including nonsemisimple monodromy. The root Wall-form proof uses h((I-A)x,v)=B(x,v), H transpose=-H A_U inverse and identity action onV/U, and remains solely in this check record.',
  'UN2 items1–3: the horizontal surface C2 times P1 meets the exceptional surface in the base-normal section, disjoint from the preceding component. Its normal direction maps isomorphically to the base tangent, giving the exact splitting at every successive centre. The charts t=u tau prove reduced multiplicities and the absence of triple points. Distinct point centres on the old abelian component give plane leaves. The root used the same transverse divisor intersections and blowdown maps.',
  'UN2 items4–5: each genus-two curve adds-2 and each point adds2; k>=max(1,-n),m=k+n realizes2n. The polynomial(1+t)^4(1+t²)+k t²(1+4t+t²)+m(t²+t⁴) reproduces every integral Betti rank, the Euler number2(m-k), and the special C2b tuples. Torsion-freeness follows from the integral direct-sum maps. The structure-sheaf pullback isomorphism follows from the stated direct images of a smooth blowup and yields(1,2,1,0).',
  'UN4 items1–4: the actual complement isomorphism and exceptional projective bundle give deltae=(r-1)eZ with compact-support additivity. The root reconstruction includes arbitrary singularities and multiplicities. The local unit root gives t=x^m; the point chart gives t=(ru)^m. Fermat quartic smoothness, adjunction g3, four simple transverse line intersections, and the curve blowup charts v=rw or r=vw give t=(ru)^m or(uvw)^m. The strict plane stays a plane because its curve centre is Cartier; the old component is blown up at the four intersection points. The original displays and multiplicities are correct.',
  'UN4 items5–8: the integral blowup map is pullback plus the exceptional Gysin images of hyperplane powers. Excision, the projective-bundle basis and j^*j_*=-xi give the source isomorphism, including on a tube with boundary. The root records its explicit inverse via degree-one trace and the hyperplane coefficients. The negative move adds(2,6,2) in degrees2,3,4; the zero move adds(3,6,3). Connectedness follows from the connected blowup fibres and proper Stein factorization. Finite iteration gives the exact prescribed Euler value and arbitrarily many components at zero; all old divisorial valuations persist.',
  'UN14 items1–5: the closure and resolution of the graph of each strict-transform map gives the bimeromorphisms of normalization resolutions. Composition of dominant maps C times P1 through either inverse proves preservation of uniruledness. The explicit rational plane map and meromorphic rank-two-bundle frame make every new component uniruled. The marking is transported through the actual complement isomorphism. These maps prove both set inclusions and preserve repetitions and multiplicities. Disjoint base supports permit simultaneous prescription; the compact critical image is finite. No additional equivalence or scope restriction is used.',
  'C2b complete prerequisite: w²=z^6-1 has six simple branch points and two unramified infinity points, giving genus2. Abel–Jacobi injectivity uses the degree-one function contradiction. At finite branch points dz/w is nonzero; at infinity s=1/z,v=w/z³ gives dz/w=-s ds/v and z dz/w=-ds/v, proving the canonical evaluation has no common zero. The embedding and normal line K_C then give the printed projective bundle. The component Euler values and all three Betti tuples agree with the independent polynomial computation. The old code-path prose remains an editorial D09 instance; this comparative pass does not silently delete it.',
  'The five D outline steps each point to exactly the body result proved: tube parity; Wang and Cayley parity; +/-2 vertical modifications and cofinal zero models; strict-transform multiset and multiplicity; projective genus-two/point construction. The main statement includes all these conclusions with the same ambient domain. No discrepancy in a statement or proof step was found.'
 ],
 certificate=bind('code/S6_SERIES_PUBLISH_II_global_D_root_certificate_01.json'),
 certificate_program=bind('code/S6_SERIES_PUBLISH_II_global_D_root_certificate_01.py'),
 reconstruction=bind('records/S6_SERIES_PUBLISH_II_global_D_root_derivation_01.md'),
 certificate_failure=bind('records/S6_SERIES_PUBLISH_II_global_D_certificate_failure_01.json'),
 computation_detail='118 successful exact checks including33 exterior-square matrices, symbolic pair/Wang identities, all displayed Betti polynomials, curve squarefreeness and local chart substitutions. The finite matrix/grid cases support the written general proofs. The first execution compared SymPy expanded and factored expressions structurally and failed; comparing their expanded difference resolved that certificate error without changing mathematics. The failure is retained.',
 source_changes=0,mathematical_errors_found=[],canonical_events_added=0,
 required_check_rows_closed=0,final_pdf_page_reading_credit=0,
 final_source_binding_pending=True,known_result_and_literature_status_audit_pending=True)
out=R/'records/S6_SERIES_PUBLISH_II_global_D_root_comparison_01.json'
assert not out.exists()
out.write_text(json.dumps(record,indent=2)+'\n')
note=f"""

### {now}: Paper II global-D comparative reconstruction

The local parity and prescribed-Euler main theorem was reconstructed from its
statement and compared with all of UN.1, UN.2, UN.4 and UN.14, the explicit
genus-two construction C2b, and all five proof-outline steps. All original
inferences and formulas agree. The alternative Wall-form argument is kept in
the checking record; the source keeps its generalized-eigenspace/Cayley proof.
The actual tube, blowup, cohomology, normalization-resolution and marking maps
were checked without narrowing the total-space hypotheses. A new exact program
passes 118 checks; its initial structural-equality error and repair are recorded.
No manuscript or canonical check-event row changed. Historical root exposure
precludes a new independence claim. Final-source binding, known-result citation
review and final PDF reading remain open.
Record: records/S6_SERIES_PUBLISH_II_global_D_root_comparison_01.json.
"""
for name in ['S6_SERIES_PUBLISH_report.md','PROGRESS_LEDGER.md']:
 with (R/name).open('a') as f:f.write(note)
print(json.dumps(bind(str(out.relative_to(R))),indent=2))
