"""Resolve the three carrier scopes and write bare pre-exposure inputs."""
from pathlib import Path
from hashlib import sha256
import csv, io, json

ROOT=Path(__file__).resolve().parents[1]
FOLDER=ROOT/'agents/continuation6_iii_infra'
source=ROOT/'S6_SERIES_PUBLISH_III.tex'
raw=source.read_bytes()
assert sha256(raw).hexdigest()=='9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0'
lines=raw.decode().splitlines()
def locate(s):
    hits=[i for i,line in enumerate(lines) if line==s]
    assert len(hits)==1,(s,hits)
    return hits[0]
def digest(a,b):return sha256('\n'.join(lines[a:b+1]).encode()).hexdigest()

t=locate(r'\begin{corollary}[All higher smash powers]')
te=next(i for i in range(t,len(lines)) if lines[i]==r'\end{corollary}')
tp=next(i for i in range(te+1,len(lines)) if lines[i]==r'\begin{proof}')
tpe=next(i for i in range(tp+1,len(lines)) if lines[i]==r'\end{proof}')
x=locate(r'\paragraph{The one-copy invariant and its computed value}')
w=locate(r'\paragraph{Scope}')
end=locate(r'\subsection{The original cusp coefficient: an explicit framed nullbordism}')
xe=w-1
while not lines[xe].strip():xe-=1
we=end-1
while not lines[we].strip():we-=1
groups={
 '038T':{'candidate_tags':['038T'],'statement_lines':[t+1,te+1],
         'proof_spans':[{'start_line':tp+1,'end_line':tpe+1,'sha256':digest(tp,tpe)}],
         'proof_kind':'proof_environment'},
 '038X':{'candidate_tags':['038X'],'statement_lines':None,
         'proof_spans':[{'start_line':x+1,'end_line':xe+1,'sha256':digest(x,xe)}],
         'proof_kind':'argument_paragraph'},
 '038W':{'candidate_tags':['038W'],'statement_lines':None,
         'proof_spans':[{'start_line':w+1,'end_line':we+1,'sha256':digest(w,we)}],
         'proof_kind':'argument_paragraph'},
}
header='% Bare target claims and defining inputs only; original arguments remain closed.\n'
header+='% Root has read the three exact original scopes to resolve ownership and claims no fresh credit for them.\n'
header+='% Source SHA256 '+sha256(raw).hexdigest()+'.\n'
packets={
'038T':r'''
\paragraph{Target 038T: all higher smash powers}
For every continuous based map $g:S^6\to S^3$ and every integer $r\ge2$,
the ordered external smash $g^{\wedge r}:S^{6r}\to S^{3r}$ is based
null-homotopic. The ordered sphere identifications are the admitted
cube-concatenation maps. At $r=2$ use the admitted universal external
smash theorem 038V. Establish the higher cases with exact maps,
associativity identifications and all homotopy endpoints.
''',
'038X':r'''
\paragraph{Target 038X: the complete one-copy invariant}
This is a separate argument-bearing paragraph, not an alias of 038T.
Its complete claims, stripped of its original argument, are as follows.
The sixfold suspension $\pi_6(S^3)\to\pi_{12}(S^9)$ is injective and
has exactly the even subgroup of the latter cyclic group as image.
For a chosen generator $\nu_9$ there is a unique $a\in\mathbb Z/12$
with $[E^6g]=2a\nu_9$; this gives the exact coefficient correspondence.
For the native cusp map $g$, that coefficient and its one-copy class
are zero. With $0<r_0<\epsilon$ and a long-torus point $u_0$ in the
open cell, the full regular inverse image of $[r_0,c(u_0)]$ is the
subset $|t|=r_0$, $\overline\pi_f=u_0$. It is a smooth three-torus.
Its ordered derivative normal framing represents the stabilized
class under Pontryagin--Thom and thus determines $a$ exactly.
Any claims about what the unframed manifold, surjectivity or ordinary
homology determine require a precise proved map or example, not an
unsupported distinction.

Defining inputs: the quotient long basis is
$(\widehat\gamma,\widehat u)$, with kernel
$K_\Lambda=\mathbb Z\langle\widehat w,\widehat\delta\rangle$.
The monodromy fixes that kernel pointwise. The real period and native
map definitions, fixed basepoint and ordered framing are the same
as the existing 038S/03A6 definition packet. The original labels
038Z and038Y belong to this paragraph and must remain attached to
the coefficient equation and inverse-image equation respectively.

The primary citation specified for the suspension claim is Hatcher,
Spectral sequences, Theorem5.41(b), p573 and pp577--578,
\url{https://pi.math.cornell.edu/~hatcher/AT/ATch5.pdf}.
Its statement and precise suspension conventions require direct reading.
The admitted038V group bridge alone does not establish this starting
map's injectivity. No original038X argument is included here.
''',
'038W':r'''
\paragraph{Target 038W: exact scope of the sphere-valued null-homotopy}
This is the separate Scope paragraph following038X. It asserts that
the sphere-carrier null-homotopy is compatible with the established
point-set quotient properties, moving embedded four-spheres and
their intrinsic pointed Euclidean limits. It concerns the sphere-valued
postcomposition $\widehat q_3^{\wedge2}$ and states that this conclusion
alone does not give null-homotopy of $q_2^{\wedge2}$ into its earlier
conical target. Check this scope through the exact maps; a claimed
failure of implication requires its mathematical justification.

Here are the defining maps, already established in admitted035X/036J.
Let
\[
 \mathcal A=([0,\epsilon]\times S^1\times\overline T^2)/\sim,
\]
where the entire zero end is one point $v_0$, the entire epsilon end
is a different point $v_1$, and every other class is a singleton.
The basepoint is $v_0$. Its exact coordinate identification with the
unreduced suspension of $S^1\times\overline T^2$ rescales the first
coordinate by $1/\epsilon$, with inverse rescaling by $\epsilon$.
On the punctured cusp,
\[
 q_2(x)=[|t|,t/|t|,\overline\pi_f(x)],\quad
 q_2(W)=v_0,\quad q_2(X\setminus\operatorname{int}N_0)=v_1.
\]
Let $c:\overline T^2\to Z_2=\overline T^2/K^{(1)}$ be the
coordinate-skeleton collapse. The postcomposition is
\[
 \widehat p_2:\mathcal A\to\Sigma_{\mathrm{red},\epsilon}Z_2,
 \qquad[r,z,a]\mapsto[r,c(a)],\qquad
 \widehat q_3=\widehat p_2q_2.
\]
It sends both distinct poles to the reduced-suspension basepoint.
The exact sphere identifications, moving-slice maps, intrinsic metrics
and entire-ball isometries are in the admitted036J receiver. The
separate positive null-homotopy is in admitted02Q7 and038V.
No original038W argument is included here.
'''
}
for tag,body in packets.items():
    p=FOLDER/f'S6_SERIES_PUBLISH_III_{tag}_definition_inputs.tex'
    content=header+body.lstrip()
    if p.exists():
        assert p.read_text()==content
    else:
        p.write_text(content,newline='\n')
    groups[tag]['safe_input_path']=str(p.relative_to(ROOT))
    print(tag,groups[tag]['proof_kind'],groups[tag]['statement_lines'],groups[tag]['proof_spans'])
(FOLDER/'S6_SERIES_PUBLISH_III_carrier_resolved_scopes.json').write_text(json.dumps(groups,indent=2)+'\n',newline='\n')
progress=ROOT/'S6_SERIES_PUBLISH_required_progress_III.tsv'
with progress.open(newline='') as f:
    r=csv.DictReader(f,delimiter='\t');fields=r.fieldnames;rows=list(r)
for row in rows:
    if row['tag'] not in groups:continue
    assert row['status']=='open' and row['proof_status']=='embargoed'
    row.update(statement_packet=groups[row['tag']]['safe_input_path'],
       packet_status='individual_scope_resolved_fresh_derivation_required',
       statement_status='bare_claims_and_definitions_available',
       source_ownership_status='verified_exact_individual_scope',
       metadata_owner=row['label'],source_owner=row['label'],
       owner_group_tags=row['tag'],alias_clause_map_required='no',alias_clause_map='',
       label_locus='statement' if row['tag']=='038T' else 'argument_paragraph',
       assigned_checker='agents/continuation6_iii_carriers',unresolved_inputs='')
    note=' Root resolved the separate corollary/proof and two argument-bearing paragraphs; no aliasing or completed-check credit. Original argument remains embargoed to the fresh checker.'
    if note not in row['notes']:row['notes']+=note
s=io.StringIO(newline='');w=csv.DictWriter(s,fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
progress.write_text(s.getvalue(),newline='\n')
assert source.read_bytes()==raw
print('Three exact scopes resolved; all original arguments remain closed to the assigned checker; no check closed.')
print('Initial preparation stopped before writing the progress table because packet_path was not a column; corrected to statement_packet. No mathematical result or source text changed.')
