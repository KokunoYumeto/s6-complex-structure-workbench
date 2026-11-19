"""Record completed manual checks, correct a replay attribution, retain the exact proof revision."""
from pathlib import Path
import csv,hashlib,importlib.util,json,sys
P=Path(__file__).resolve().parents[2];R=P.parents[1]
sys.path.insert(0,str(P/'code'))
from inventory_reconcile import commands,argument
idx=json.loads((P/'analysis/inventory_source_index.json').read_text())
f=P/'records/root_events.tsv';rows=list(csv.DictReader(f.open(),delimiter='\t'));superseded=[]
for r in rows:
 if r['statement_id']=='push:src:E.4.1' and r['type']=='computation or formal certificate' and 'replay_interval_leaves.output.json' in r['outcome']:
  superseded.append(dict(r));r['type']='scope correction'
  r['outcome']='The earlier attribution of code/I/replay_interval_leaves.output.json and replay_family/f_interval_verify.stdout to this independent Arb theorem is withdrawn. Those executions used the earlier mpmath implementation and remain recorded under fam:src:C.2.3. The fresh unchanged Arb execution is separately recorded below.'
 if r['statement_id']=='push:src:E.4.1' and 'Matched rational/binary input enclosures' in r['outcome']:
  superseded.append(dict(r));r['type']='exact software-source reading; execution attribution corrected'
  r['outcome']='Read Johansson2016 Section2 pp2–4 and complete Section3 pp4–6, and official python-flint0.9.0 constructor/lower/upper/man_exp/str semantics. These source-reading scopes are retained. The earlier reference to an already replayed Arb certificate was premature: that earlier execution used mpmath. The actual Arb implementation match and execution are recorded in the subsequent events.'
checker='GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro, S6_10_PAPERS'
new=[
('fam:st:A.5.2','used and rechecked in this run','Verified exact label identity with fam:src:A.5.2: all six co-located labels occupy the same statement at source characters44182–45155 in S6_09_PAPERS_I.tex, SHA2565089ddf726828eea0c2d6a1542e7777ae4cc9694a0e06338db13875c56773534. The complete receiving Koszul, direct-image, Kodaira–Spencer and Kuranishi proof already reviewed under fam:src:A.5.2 therefore supplies this identical statement. This is an identity propagation, with no additional independent proof credit.'),
('push:src:E.4.1','targeted proof check','Read and rederived the full six-step proof and both complete original programs. Checked rational-to-Arb enclosures, exact dyadic Newton choices, the complex sup-norm contraction, finite pole-free Fourier enclosures, both moment tails, theta and logarithmic eta tails, upper-endpoint acceptance and the exact rational sweep. Wrote the explicit half-period theta identity and period/evenness transformations proving that the one-root norm enclosure controls both zeros. The successful contraction forces the selected preconditioner to be nonzero. The proof review is separate from the executable certificates.'),
('push:src:E.4.1','computation or formal certificate','PASS: executed the original unchanged e4_arb_certificate.py with python-flint0.9.0,192bits,all19701boxes,four workers. All19701 strict root contractions and norm bounds succeeded,0failures. The largest upper endpoint is enclosed by1.999877571767410524070536478244687423578792301873142913 plus or minus9.26e-56,below1.999877571767410525; worst index17866. The input SHA256 is87b7c2dc672e98cab926c092ebdc757373a6817bb651c3472235a42956b5c9ab. Only rational endpoints from the earlier certificate are imported. Full outputs and identical source hashes are in code/I/replay_arb and analysis/I_arb_replay_manifest.json.'),
('push:src:E.4.1','computation or formal certificate','PASS: executed the original unchanged e4_cover_and_local.py. The exact Fraction sweep checks19911leaves,438vertical edges,area23/40,disjoint interiors and complete coverage;36local rectangles lie in the prescribed disc and174excluded rectangles lie below the unit circle. The separately implemented256bit Arb local-constant inequalities also all passed. Execution of those constants grants no additional whole-proof review of the older local argument.')]
for label,typ,outcome in new:
 e={'statement_id':label,'date':'2026-11-18','who':checker,'type':typ,'outcome':outcome}
 if e not in rows:rows.append(e)
with f.open('w',newline='') as o:
 w=csv.DictWriter(o,fieldnames=['statement_id','date','who','type','outcome'],delimiter='\t');w.writeheader();w.writerows(rows)
# Read the actual current receiving block; the revision excludes generated records.
path=P/'papers/I/10_interval_certificate.tex';s=path.read_text();a=s.index('\\begin{theorem}[independent certification');b=s.index('\\begin{theorem}[quantitative local maximum]',a);raw=s[a:b]
for m in sorted(commands(raw,'StatementRecord'),key=lambda q:q['start'],reverse=True):
 end=m['end']
 for _ in range(3):
  while raw[end].isspace():end+=1
  _,end=argument(raw,end)
 raw=raw[:m['start']]+raw[end:]
raw=raw.replace('\\path{code/e4_arb_certificate.py}','\\path{code/I/replay_arb/S6_02_PUSH/code/e4_arb_certificate.py}')
raw=raw.replace('\\path{code/e4_cover_and_local.py}','\\path{code/I/replay_arb/S6_02_PUSH/code/e4_cover_and_local.py}')
old='''The two zeros of $\\wp$ are negatives modulo the period lattice, counted
with multiplicity. The theta transformation laws show that
$\\mathcal N$ is invariant under these operations; hence one root
enclosure controls both zeros. No continuity or success of Newton
iteration is used in that conclusion.'''
repl=r'''The finite Fourier enclosures exclude the poles on $Z$, and the strict
Lipschitz inequality forces $A\ne0$. The two zeros of $\wp$ are
negatives modulo the period lattice, counted with multiplicity. The
exact half-period transformation, obtained by replacing the summation
index in the theta series, is
\[
 \vartheta_3\bigl(z-(1-\tau)/2,\tau\bigr)
   =i e^{-\pi i\tau/4-\pi i z}\vartheta_1(z,\tau).
\]
Writing $v=\Im z$ and $y=\Im\tau$, its modulus and Gaussian factor
cancel to give
\[
 \mathcal N(z,\tau)=
 \left|\frac{\vartheta_1(z,\tau)}{\eta_D(\tau)}\right|
 e^{-\pi v^2/y}.
\]
Now $\vartheta_1(-z)=-\vartheta_1(z)$,
$\vartheta_1(z+1)=-\vartheta_1(z)$ and
$\vartheta_1(z+\tau)=-e^{-\pi i\tau-2\pi i z}\vartheta_1(z)$.
In the last transformation the modulus contributes
$e^{\pi y+2\pi v}$, while the Gaussian contributes its reciprocal.
Thus the displayed norm is even and lattice-periodic, proving directly
that the one-root enclosure controls both zeros. No continuity or
success of Newton iteration is used in that conclusion.'''
if old in raw:raw=raw.replace(old,repl)
else:assert repl in raw
rev=P/'papers/I/revisions/push_src_E.4.1.tex';rev.write_text(raw)
spec=importlib.util.spec_from_file_location('bodyI',P/'code/I/build_body.py');h=importlib.util.module_from_spec(spec);spec.loader.exec_module(h)
row=next(r for r in h.ROWS if r['source_run']=='S6_02_PUSH' and r['source_id']=='E.4.1');loc=idx['S6_02_PUSH:E.4.1']
path.write_text(s[:a]+h.record_block(raw,loc,row)+s[b:])
# Add the precise identity scope to the existing canonical family record only.
fam=P/'papers/I/02_moduli.tex';t=fam.read_text();aliastext=h.escape(new[0][2])
if aliastext not in t:
 m=next(m for m in commands(t,'StatementRecord') if m['value']=='fam:st:A.5.2');at=m['end']
 while t[at].isspace():at+=1
 _,at=argument(t,at)
 while t[at].isspace():at+=1
 _,end=argument(t,at)
 t=t[:end-1]+' '+aliastext+t[end-1:];fam.write_text(t)
source=R/loc['file'];sourceblock=source.read_text()[loc['start']:loc['end']]
record={'superseded_event_entries':superseded,'new_events':new,'source_block':{'file':loc['file'],'start':loc['start'],'end':loc['end'],'sha256':hashlib.sha256(sourceblock.encode()).hexdigest()},'proof_revision':str(rev.relative_to(P)),'proof_revision_sha256':hashlib.sha256(raw.encode()).hexdigest(),'arb_summary':json.loads((P/'code/I/replay_arb/S6_02_PUSH/code/e4_arb_certificate_summary.json').read_text()),'cover_and_constants':json.loads((P/'code/I/replay_arb/S6_02_PUSH/code/e4_cover_and_local.json').read_text()),'identity_alias_credit':'No additional independent proof event.'}
(P/'analysis/I_e4_and_alias_scope_correction.json').write_text(json.dumps(record,indent=2))
print('Corrected',len(superseded),'overbroad entries; recorded',len(new),'precise scopes. Root total',len(rows))
