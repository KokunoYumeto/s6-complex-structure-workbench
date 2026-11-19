#!/usr/bin/env python3
"""Install the frozen alternative A.RT.21 proof, retaining the exact old text."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
P=Path(__file__).resolve().parents[2]
start='For these two boundary classes one can further exclude a'
end='Since every image component is rational-normalized, write'
replacement=r'''For these two boundary classes one can further exclude a
one-component image with first Betti number one. Its normalization
is $\mathbf P^1$, and exactly one point $q$ identifies two distinct
normalization points $\alpha,\beta$. Other singular points are
unibranch and do not change this topological quotient. The universal
cover of the image is an infinite chain of normalized spheres $C_j$,
with $\beta_j$ identified with $\alpha_{j+1}$.

The actual map $h|_{D_{\rm red}}$ lifts to this cover because
$D_{\rm red}$ is simply connected. Each noncontracted rational
component factors through the normalization of the image and maps
surjectively onto it; its lift therefore covers one whole $C_j$.
Each contracted component lifts to a point. There are finitely many
components, so their connected lifted image is a finite chain
$C_m,\ldots,C_M$.

Choose a preimage in $D_{\rm red}$ of the left endpoint node and
let $t_-$ be its image under $\pi$ in the normalization $T$ of $S$.
The resolution fibre $\pi^{-1}(t_-)$ is connected and lies in
$D_{\rm red}=h^{-1}(\Gamma_{\rm red})$. Its lift is a single point
of the discrete fibre over $q$. Every local conductor branch of $T$
through $t_-$ has a strict transform meeting this resolution fibre.
It can receive only the branch directed into $C_m$: receiving the
other branch would force the lifted image to contain $C_{m-1}$.
At the right endpoint the same argument produces a point $t_+$
receiving only the opposite branch. The two points are distinct,
because their connected resolution fibres lift to different endpoint
nodes, including when $m=M$.

Distinct normalization points over $q$ correspond to distinct local
irreducible hypersurface branches of $S$ in the smooth threefold.
Their two distinct equations have an intersection curve: the ideal
they generate has height two. Every such curve is an actual
conductor-image branch received by both normalization points.
There are only the two image branches at $q$, whereas $t_-$ and
$t_+$ receive disjoint ones. This contradiction excludes the
one-component, first-Betti-number-one image.

'''
changes=[]
for name in ['papers/II/body.tex','papers/II/body_source.tex']:
 path=P/name;before=path.read_bytes();text=before.decode()
 at=text.index(start);stop=text.index(end,at);old=text[at:stop]
 if old==replacement:continue
 text=text[:at]+replacement+text[stop:];path.write_text(text)
 changes.append({'path':name,'before_sha256':hashlib.sha256(before).hexdigest(),
  'after_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'old_text':old,'new_text':replacement})
receipt=P/'analysis/continuation_VI_ledger/RAT1_forest_replacement_receipt.json'
if changes:
 payload={'timestamp_utc':datetime.now(timezone.utc).isoformat(),
  'frozen_derivation':'analysis/continuation_VI_ledger/RAT1_residual_before_read.md',
  'frozen_derivation_sha256':'e6d9041e95b79f08c4c4bc89e39e8303b0f2d242ee2097bbdd60f98f5572d09b',
  'scope':'Only the A.RT.21 forest argument is replaced by the complete alternative derived before target reading. Old argument is preserved without a claim that it was false. No whole A.5.16 gate is awarded.',
  'changes':changes}
 if receipt.exists():
  prior=json.loads(receipt.read_text());prior.setdefault('later_applications',[]).append(payload);payload=prior
 receipt.write_text(json.dumps(payload,indent=2)+'\n')
print(json.dumps({'changed_files':len(changes),'receipt':str(receipt)}))
