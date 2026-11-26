from pathlib import Path
import datetime as dt, hashlib, json

R=Path(__file__).resolve().parents[1]
index='agents/continuation2_C/S6_SERIES_PUBLISH_II_C2_R13_global_variation_02/S6_SERIES_PUBLISH_II_C2_R13_integral_matrix_index_v1.json'
def bind(p):
    b=(R/p).read_bytes()
    return dict(path=p,bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
assert bind(index)['sha256']=='9dbc4d05024c70158f0633039c68507c4b509c67adbfb341eb951b82af7058a3'
x=json.loads((R/index).read_text())
for f in x['files']: assert bind(f['path'])==f
out='records/S6_SERIES_PUBLISH_II_R13_root_research_04.json'
record=dict(created_utc=dt.datetime.now(dt.timezone.utc).isoformat(),
    checker='GPT-6 Astra (OpenAI), ChatGPT Pro mode, root continuation2; reasoning effort not separately exposed',
    actual_reading='Root read the full 9939-byte component/R2/matrix note, entire2489-byte program, full3363-byte actual output, complete1674-byte receipt and index. Root also reread the exact R13 statement-only packet. No R13 target proof was opened in this research step; the target still has no complete independent derivation. Root did not open the primary p85 passage for this packet; the agent receipt records its exact primary reading and scope.',
    mathematical_review=[
        'On a small closed tube U with central retraction and boundary Z, Poincare-Lefschetz duality gives H1(U,Z)=0 and H2(U,Z)=Q^[components]. The relative Thom basis maps to the restrictions of global Cartier-divisor first Chern classes, which vanish because H2(Y;Q)=0. Hence the exact pair sequence is0 to H1U to H1Z to Q^n to0. In the Wang sequence the base-circle class maps under the boundary map to the multiplicity vector, by the local angular winding z maps to z^mi. Quotienting the Wang lift by that vector gives the actual cokernel map V^T/H1S isomorphic to Q^n/Q(m_i). This proves dimension n-1 and, with the earlier global sequence, r=1+sum(n_b-1).',
        'For each Fq=Rq f_*Q, extension by zero and restriction to omitted-point stalks give0 to j!(exterior^q V) to Fq to a skyscraper sheaf to0. Its degree2 cohomology identifies with Hc2 of the local system, dual to the invariant space of the dual representation. For degree1 retain r-prime separately from r. The Euler identity is sum codim local invariants=8-r-r-prime. The actual wedge pairing exterior2 V tensor exterior2 V to the oriented exterior4 V proves the needed self-duality of exterior2, without imposing a polarization or self-duality on V.',
        'The Leray d2:H0F2 to H2F1 is injective because H2Y=0. Poincare duality H4Y=0 forces d2:H0F3 to H2F2 surjective. These constrain the actual direct-image sheaves; they do not produce global sections from local positive classes.',
        'The local lattice retains its half-period coupling. Returning the continued basis a,b,c,d+c by the deck linear part(z,w) maps to(z,-w) yields a-c,b,-c,-d-c and exactly the displayed local monodromy. The three integral matrices have determinant1 and product identity; the supplied determinant1 matrices satisfy Ai Ci=Ci Aloc. The rational comparison uses the specified half-sum basis P and Ai=P^-1 diag(1,Bi)P. The program evaluates exterior minors and invariant kernels exactly, obtaining global dimensions1,1,0,1,1, dual dimensions equal for this representation, local dimensions1,2,2,2,1, and H1 of each j-star exterior local system zero.',
        'The primitive invariant cohomology vector(1,1,1,2) evaluates2 on the common fixed homology vector(0,0,0,1). The stated formal transgressions are dimensionally compatible with b1=b2=0 and b3=2. An actual holomorphic period family, analytic extensions at the three singular values, affine torsor/gluing class and nonzero transgression must still be constructed. Root explicitly requested those steps and exact binding to every standing Part4.2 hypothesis. The matrix calculation supplies no compact example, theorem refutation or smaller completed R13 gate.'
    ],
    evidence=[bind(index),*x['files']],
    outcome='Exact necessary maps and integral representation reviewed; analytic/global realization remains unfinished.',
    canonical_source_changes=0,events_added=0,required_checks_completed=0,
    mathematical_gate_reduction_claimed=False,publication_page_reading_credit=0)
assert not (R/out).exists()
(R/out).write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(bind(out)))
