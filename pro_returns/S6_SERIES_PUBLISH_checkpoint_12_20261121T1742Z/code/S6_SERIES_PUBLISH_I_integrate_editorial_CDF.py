from pathlib import Path
import json, hashlib, datetime
from S6_SERIES_PUBLISH_editing import Editor

r=Path(__file__).resolve().parents[1]
ed=Editor('I')
paths=[
 r/'agents/i_provenance/S6_SERIES_PUBLISH_I_editorial_famF_guards.json',
 r/'agents/i_analytic/S6_SERIES_PUBLISH_I_editorial_batch_c_guards.json',
 r/'agents/i_analytic/S6_SERIES_PUBLISH_I_editorial_batch_d_guards.json',
 r/'agents/i_analytic/S6_SERIES_PUBLISH_I_night_P57_date_guard.json',
]
sources=[]
for p in paths:
 d=json.loads(p.read_text())
 changes=d.get('guards',d.get('changes'))
 for x in changes:
  new=x['new']
  if x['id']=='IA-P57-date':
   new=r'''The working-edition proof of the exact $2\mathbb Z$ equivalence
is dated 8 September 2026. Version~1, submitted on
23 September 2026, states that equivalence as its Theorem~1.4.'''
  ed.replace(x['old'],new,x.get('type','D09'),x['reason'],x['id'],
             count=x.get('expected_count',1))
 sources.append({'path':str(p.relative_to(r)),
                 'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
                 'guard_count':len(changes)})
old=r'''Let $C$ dominate the coefficient one-norms of $F,G$ and both
pairs $(A_j,B_j)$. For coprime $a,b$, the two identities bound
the common divisor of $F(a,b),G(a,b)$ by $|D|$ and give
'''
new=r'''Let $C$ dominate the coefficient one-norms of $F,G$ and the
sums $\|A_j\|_1+\|B_j\|_1$. For coprime $a,b$, put
$H=\max(|a|,|b|)$ and $d=\gcd(F(a,b),G(a,b))$.
The two identities give $d\mid D$. Using the identity whose
right side contains the coordinate of size $H$ also gives
$\max(|F(a,b)|,|G(a,b)|)\geq |D|H^4/C$.
After division by $d$, the projective size is at least $H^4/C$
and at most $CH^4$. Therefore
'''
ed.replace(old,new,'D25',
 'Spell out the exact Bezout lower bound and the cancellation d divides D in the restored canonical-height application; no new estimate or constant is introduced.',
 'ari:C.6.R4')
ed.save()
receipt={
 'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'sources':sources,
 'root_reading':'Every complete old/new guard actually displayed and read before integration; the five truncated D23-D27 guards were separately displayed and read.',
 'scope':'Exposed-proof editorial comparison only. Agent scoped reread/computation records remain separate; integration supplies no additional independent event.',
 'date_limit':'September8 is supported by the attached working-edition provenance, not independently authenticated as an early public posting. September23 is the authenticated arXiv v1 submission. The paper states a dated proof and submission without claiming an independently verified early posting.',
 'height_bound':'The homogenous Bezout identity yields raw size >= |D| H^4/C; gcd divides D, so the normalized lower bound is H^4/C. The four original norm constants are preserved.'
}
(r/'records/S6_SERIES_PUBLISH_I_editorial_CDF_integration.json').write_text(json.dumps(receipt,indent=2)+'\n')
