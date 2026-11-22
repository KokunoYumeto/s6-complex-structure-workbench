from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import json

R=Path(__file__).resolve().parents[1]
def bind(p):
    return dict(path=p,sha256=sha256((R/p).read_bytes()).hexdigest())
record=dict(
    created_utc=datetime.now(timezone.utc).isoformat(),
    owner='cdp:st:C.2.D4.2',tag='01BX',status='full original comparison completed; final packet pending',
    freeze=bind('agents/ii_infra/derivation_freezes/01BX/20261122T061218665587Z/S6_SERIES_PUBLISH_derivation_freeze_receipt.json'),
    release=bind('agents/ii_infra/released_proofs/01BX/b168cbeb6186b92e/S6_SERIES_PUBLISH_release_receipt.json'),
    derivation=bind('agents/continuation2_root/01BX/S6_SERIES_PUBLISH_II_root_01BX_derivation.md'),
    original=bind('agents/ii_infra/released_proofs/01BX/b168cbeb6186b92e/S6_SERIES_PUBLISH_full_owning_block.tex'),
    program=bind('code/S6_SERIES_PUBLISH_II_root_BX_prerelease.py'),
    output=bind('agents/continuation2_root/01BX/S6_SERIES_PUBLISH_II_root_BX_prerelease.json'),
    actual_reading='The entire seven-section derivation and full program/output were read before freeze. All397 lines of the original owning block were read after release in two complete bounded outputs, including all thirteen proof items and every display.',
    comparison=[
        'The independent line-subundle degree ell gives pa(R2)=3+ell-v and R1.R2=2-ell-v, hence v<=2. In the balanced original notation ell=-1-d; when a>=0 and v>0 the forced linear factor gives ell=a. These are the exact maps to the original degree bounds.',
        'The frozen argument handles v=0 even with disconnected branch, using its actual Euler/Gysin calculation. The original proves the sharper exact boundary relation count epsilon=c-r by pi^*B_i=3*strict_i plus exceptional terms. This strengthens the frozen rank bounds without changing the cyclic cover.',
        'The reduced cases v0,v1 and two simple zeros all have positive compact pairing and b1<=3, exactly as frozen. Original DD.12,13,15 are stronger numerical bounds and will receive their own postrelease exact arithmetic comparison.',
        'The double-zero normalized character algebra is identical to the frozen O+L^-1+L^-2(F) with explicit generators1,w,w^2/s. The original resolves every contact k by k base blowups; the frozen proof handles the needed k1,2 by diagonal mu3 quotient maps and one base blowup in the tangency case. For k1 the base blowup normalizes to the O(-3) resolution. For k2 the first base blowup has three inverse-image P1 leaves, and resolving the remaining quotient is exactly the second base blowup. Thus the exact proper maps and character transformations agree.',
        'For the original arbitrary-contact argument, the identities for both character sheaves with O(E) and sigma_*O(E)=O,R1sigma_*O(E)=0 give vanishing higher direct image by projection formula, finite faithful pushforward and Leray. A final disjoint branch cover is smooth. Formal functions and surjectivity of H1 on exceptional thickenings give H1(O_exceptional)=0, hence rational components and a tree. The full original rationality proof is sound and will be retained.',
        'The original double-zero epsilon1 gives b1U1 and exact pairing rank2nu for nu2 or3; this strengthens the frozen positive lower bound2nu-1. The same actual cover-to-q1 map and compact-core embedding yield the contradiction. The final elliptic consequence matches the supplied A5.19 statement exactly.'
    ],
    discrepancies_found=[],
    next_actions=['Postrelease exact computation of the original stronger formulas','Resolve internal reference locators, including the missing RAT6 authority','Prepare minimal guards retaining all thirteen mathematical steps and all displays','Read the complete proposed proof before admission'],
    prefreeze_working_correction='A mistaken draft sentence asserting connectedness for v0 was removed before freeze, and the arithmetic code was changed to use only b>=0. The complete corrected derivation/output were reread before freeze. No target proof had been opened. A first freeze preflight then requested the exact owner identifier; adding that identifier was followed by the successful immutable freeze.',
    events_added=0,required_rows_closed=0,publication_page_reading_credit=0)
p='records/S6_SERIES_PUBLISH_II_root_BX_pending_review_20261122.json'
assert not (R/p).exists()
(R/p).write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(bind(p),indent=2))
