from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json
import re

ROOT = Path('/workspace/scratch/9fcd229a9ed4/base/S6_SERIES_PUBLISH_checkpoint_35')
OUT = ROOT / 'agents/continuation3_provenance/firstpart_locators'
OUT.mkdir(parents=True, exist_ok=True)
REL = OUT.relative_to(ROOT).as_posix()
main = (ROOT / 'S6_SERIES_PUBLISH_II.tex').read_text()
stamp = datetime.now(timezone.utc).isoformat()
guards = []
defects = []

def tsv(name, rows):
    with (OUT / name).open('w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]), delimiter='\t', lineterminator='\n')
        w.writeheader()
        w.writerows(rows)

def add(cid, old, new, kinds, statement, reason):
    assert old != new
    assert main.count(old) == 1, (cid, main.count(old))
    guards.append(dict(change_id=cid, old_text=old, new_text=new))
    defects.append(dict(change_id=cid, type=kinds, statement_id=statement,
        old_location='Current Paper II; exact guarded span at line '+str(main[:main.index(old)].count('\n')+1),
        old_page='Final concordance pending', new_location=statement,
        new_page='Integrated PDF pending', old_text=old, new_text=new, reason=reason,
        review_status='Complete bounded old/receiving comparison; source-ready for root admission. Exposed used-and-rechecked work; no containing-unit or final-PDF closure.'))

add('II-C3-FIRSTPART-001',
    r'A & New normalization criterion extending \cite[\S10.4, pp.~87--90]{AC26};',
    r'A & New normalization criterion extending \cite[\S10.4, pp.~89--90]{AC26};',
    'D18', 'Known and new: A',
    'The freshly opened complete section 10.4 occupies printed pages 89–90. Pages 87–88 contain preceding results, already named separately in section 1.2.')
add('II-C3-FIRSTPART-002',
    r'\cite[\S1.1(1), p.~2]{Viaclovsky2026Log}, with twelve-tooth Hodge values;',
    r'\cite[\S1.1(1), p.~2]{Viaclovsky2026Log}, with Hodge values on the stated open twelve-tooth locus;',
    'D15;D18', 'Known and new: F',
    'Preserve Theorem F’s exact nonempty open family of admissible twelve-tooth smoothings. The comb deformation and ordered-pair answers retain their full printed scopes.')

start = main.index(r'\begin{definition}[Marked periods, fibres and orientations]')
end = main.index(r'\end{definition}', start) + len(r'\end{definition}')
old = main[start:end]
new = old.replace(r'\StatementRecord{def:II:marked-conventions}{proved}{P202}{}',
    r'\StatementRecord{def:II:marked-conventions}{proved}{P202}{\SeriesRef{fam:src:C.1.1}, \SeriesRef{I:def:finite-coordinates}, \SeriesRef{fam:src:A.5.1}, \SeriesRef{fam:src:B.2.1}}')
needle = 'Base meridians are counterclockwise.'
marked = r'''Let $\pi:\mathfrak H\to B\setminus\{p_0\}$ be the marked
$(3,4,\infty)$ orbifold uniformization, with marked deck generators
$g_1,g_2$ of orders three and four. Let $z_j\in\mathfrak H$
be the fixed point of $g_j$ above $p_j$. Thus
$\pi(z_j)=p_j$, $g_jz_j=z_j$,
$\rho=\tau(z_1)=e^{\pi i/3}$ and $\tau(z_2)=i$.
The marked values are
$\mu(z_1)=(2-\rho)/3$ and $\mu(z_2)=(1-i)/2$
(\SeriesRef{fam:src:C.1.1}). The local roots are
$r^3=t\circ\pi$ at $z_1$ and $s^4=(t-1)\circ\pi$ at $z_2$.
We take $r>0$ on $0<t<1$, where $\tau$ follows the unit-circle
arc from $\rho$ to $i$. At $z_2$ we use the branch with
$\operatorname{Im}\mu_s(0)>0$ and
\[
 \tau=i+\frac{i}{\pi\sqrt{E_4(i)}}s^2+O(s^4),
\]
where $E_4$ is the normalized Eisenstein series of weight four;
on the marked arc $t>1$ one has $\tau=iy$, $y>1$
(\SeriesRef{I:def:finite-coordinates}).
'''
new = new.replace(needle, marked + needle)
new = new.replace('and the marked periods\n',
    'and the marked periods, writing $\\beta_c=\\beta^{\\rm part}+c$,\n')
new = new.replace('For a finite affine datum we write',
    'For an admissible finite affine datum, with $3\\nmid l_1$ and\n$2\\nmid l_2$, we write')
oldp = r'''For general finite affine twists we use
$p=12l_0-4l_1-3l_2$ and $\pi_1(X)=\Z/|p|$.
The complete marked transport and construction are those of Paper I.'''
newp = r'''Let $\gamma:\Lambda\to\Z$ be the first coordinate and
$\Lambda_{\rm tor}=\Z\langle\widehat w,\widehat\delta\rangle$.
For the cusp collar section $\sigma$, define
$l_0=\gamma(c(\sigma))$, where
$c(\sigma)=[\lambda_\sigma]\in\Lambda/\Lambda_{\rm tor}$ is determined
by a holomorphic lift $\widetilde\sigma$ on the cusp cover:
\[
 t^{-1}=e^{2\pi i s_0},\qquad
 \widetilde\sigma(s_0+1)-\widetilde\sigma(s_0)
     =\Pi_c(s_0+1)\lambda_\sigma.
\]
Changing the lift adds $(I-M_0^{-1})\lambda$ to $\lambda_\sigma$;
this lies in $\Lambda_{\rm tor}$, on which $\gamma$ vanishes.
This is the winding convention of
\cite[Definition~6.6 and Proposition~6.7, pp.~39--40]{AC26}.
Since $\gamma(v_j)=l_j$, the peripheral presentation in
\cite[Theorem~7.17, p.~57]{AC26}, using the clockwise analytic
generators, gives
\[
 p=12l_0-4l_1-3l_2,\qquad \pi_1(X)\simeq\Z/|p|\Z.
\]
Those peripheral generators lift the inverses of our
counterclockwise base meridians. The standard fixed data are
those of \SeriesRef{fam:src:A.5.1}; the arbitrary affine vectors
and full cusp collar section are those of
\SeriesRef{fam:src:B.2.1}.'''
assert oldp in new
new = new.replace(oldp,newp)
(OUT/'S6_SERIES_PUBLISH_common_conventions_original.tex').write_text(old)
(OUT/'S6_SERIES_PUBLISH_common_conventions_proposed.tex').write_text(new)
add('II-C3-FIRSTPART-003',old,new,'D18;D20;D22', 'def:II:marked-conventions',
    'Define both fixed lifts, their branch coordinates and exact period values from permitted completed-I statement records. Define the previously unnamed cusp winding by the identical AC lattice cocycle; give the exact fundamental-group source and distinguish the inverse peripheral generators without changing the stated counterclockwise base orientation. Replace broad construction credit by its precise standard/arbitrary-data statement owners.')

add('II-C3-FIRSTPART-004',
    'For $z\\notin\\Z$, use the marked period functions\n$\\tau,\\mu,\\beta_c$ and let $\\mathcal R_z$ be the regular base\npoints where integers $(n,p,q,r)$ satisfy',
    r'''For $z\notin\Z$, let $z_1,z_2$ be the marked fixed lifts of
$p_1=0,p_2=1$ on the $(3,4,\infty)$ uniformizing half-plane, with
$\tau(z_1)=e^{\pi i/3}$ and $\tau(z_2)=i$ and with the cubic and
quartic root coordinates of \cref{def:II:marked-conventions}.
Use the marked period functions $\tau,\mu,\beta_c$ and let
$\mathcal R_z$ be the regular base points where integers
$(n,p,q,r)$ satisfy''',
    'D20;D22','series:II:E',
    'Make the two marked lifts local to the headline statement, while retaining every resonance equation, lattice, length, rank and cohomology conclusion. The explicit root coordinates are defined once in the common conventions.')
add('II-C3-FIRSTPART-005',
    r'Use the fixed marked functions $\tau,\mu,\beta_c$ and put $\rho=\tau(z_1)$. For $z\notin\Z$, let $\mathcal R_z$ be the set of regular base points at which integers $(n,p,q,r)$ satisfy',
    r'''Use the fixed marked functions $\tau,\mu,\beta_c$ and the
marked lifts $z_1,z_2$ of \cref{def:II:marked-conventions}; put
$\rho=\tau(z_1)=e^{\pi i/3}$. For $z\notin\Z$, let $\mathcal R_z$
be the set of regular base points at which integers $(n,p,q,r)$ satisfy''',
    'D20;D22','cdp:st:C5c',
    'Tie the resonance statement to the same fixed lifts and branches. The full original C5c statement and proof were read; no resonance module, invariant character, support argument or surjectivity conclusion changes.')
add('II-C3-FIRSTPART-006',
    r'The fixed values $\mu(z_1)=(2-\rho)/3$ and $\mu(z_2)=(1-i)/2$ give the two displayed lattices by solving the first equation.',
    r'The fixed values $\mu(z_1)=(2-\rho)/3$ and $\mu(z_2)=(1-i)/2$ of \SeriesRef{fam:src:C.1.1} give the two displayed lattices by solving the first equation.',
    'D18','cdp:st:C5c',
    'Supply the precise current I.3.2 owner for the fixed values, using attached statement metadata only. The equations themselves also follow by evaluating the opened AC equivariance identities at the two fixed points.')

entries = [
    ('fam:src:C.1.1','01QH','3.2','25'),
    ('fam:src:A.5.1','01Q6','7.8','51'),
    ('fam:src:B.2.1','01QB','8.1','52'),
]
for k,(label,tag,num,page) in enumerate(entries,7):
    prefix = r'\expandafter\def\csname SRef@'+label+r'\endcsname'
    line = next(x for x in main.splitlines() if x.startswith(prefix))
    updated = prefix+r'{\href{S6_SERIES_PUBLISH_I.pdf\#nameddest=tag-'+tag+'}{I.'+num+' (p.~'+page+')} }'
    if k == 7:
        assert r'\csname SRef@I:def:finite-coordinates\endcsname' not in main
        updated += '\n'+r'\expandafter\def\csname SRef@I:def:finite-coordinates\endcsname{\href{S6_SERIES_PUBLISH_I.pdf\#nameddest=tag-PI07}{I.12.8 (p.~82)} }'
    add(f'II-C3-FIRSTPART-{k:03d}',line,updated,'D06;D18',label,
        'Use the completed-I statement metadata and current permanent target, number and page. This is a bounded reader-target repair, not a cross-paper census refresh; no Paper I manuscript or PDF was opened.')

add('II-C3-FIRSTPART-010',
    r'\item At the order-three point put $t=s^3$,',
    r'''\item At the order-three point write $s$ for the fixed cubic
root of \cref{def:II:marked-conventions}, and put $t=s^3$,''',
    'D20;D22','cdp:st:C5c',
    'Identify the existing local variable of the complete order-three calculation with the specified marked cubic root. Every coefficient, character and local module calculation remains unchanged.')

add('II-C3-FIRSTPART-011',
    r'''For the symmetric period matrix
$\Omega=\left(\begin{smallmatrix}\tau&\mu\\\mu&\beta/6\end{smallmatrix}\right)$,
with Jacobi theta periods $1,\tau$ and''',
    r'''For the symmetric period matrix
$\Omega=\left(\begin{smallmatrix}\tau&\mu\\\mu&\beta/6\end{smallmatrix}\right)$,
set $\beta=\beta_c=\beta^{\rm part}+c$. With Jacobi theta periods
$1,\tau$ and''',
    'D20;D22','series:II:E',
    'Define beta locally for this fixed X_c by the same raw period entry. The complete E8 proof identifies the symmetric periods by the identity on C² and the index-six lattice inclusion, whose added generator is (mu,beta_c/6). The general theta identity and E18’s separate half-period application are unchanged.')

candidate=main
for row in guards:
    assert candidate.count(row['old_text'])==1,row['change_id']
    candidate=candidate.replace(row['old_text'],row['new_text'])
assert len(re.findall(r'\\label\{series:II:E\}',candidate))==1
for name,label in [('Theorem_E','series:II:E'),('Theorem_F','series:II:F'),('C5c','cdp:st:C5c')]:
    pos=main.index(r'\label{'+label+'}')
    start=main.rfind(r'\begin{',0,pos)
    if name=='C5c':
        end=main.index(r'\end{proof}',pos)+len(r'\end{proof}')
    else:
        end=main.index(r'\end{maintheorem}',pos)+len(r'\end{maintheorem}')
    old=main[start:end]
    new=old
    for row in guards:
        if row['old_text'] in new: new=new.replace(row['old_text'],row['new_text'])
    (OUT/f'S6_SERIES_PUBLISH_{name}_original.tex').write_text(old)
    (OUT/f'S6_SERIES_PUBLISH_{name}_proposed.tex').write_text(new)

tsv('S6_SERIES_PUBLISH_firstpart_guards.tsv',guards)
tsv('S6_SERIES_PUBLISH_firstpart_defects.tsv',defects)
metadata=ROOT/'records/S6_SERIES_PUBLISH_I_current_statements.json'
packet=ROOT/'records/S6_SERIES_PUBLISH_II_FT_completed_I_statement_inputs_01.tex'
inventory=ROOT.parent/'S6_SERIES_GRIND_inventory.csv'
source_specs=[
    dict(source_key='AC26',url='https://alpo.ge/s6.pdf',
        version='108-page author PDF, retrieved 22 November 2026; exact file identified by SHA256',
        locus_read='Setup on the second opening page; Definition 6.6 and Proposition 6.7 with complete printed proof, pp.39–40; section 7.5 meridian definitions and equation (7.10), pp.54–55; complete Theorem 7.17 and printed proof, p.57; complete section 10.4, pp.89–90',
        sha256='283bba102dd1d5dc346af81b28145bdaaea6654398d5032e76e97bafb9a858f2',bytes=1113315,
        own_paraphrase='The setup fixes the two orbifold lifts and their period values. The cusp section has a lattice-valued monodromy class modulo the toric sublattice; its first coordinate is the discrete gluing coefficient. The named fundamental-group theorem computes the cyclic group with determinant 12l0−4l1−3l2. Section10.4 identifies the failure of restriction from the ambient cotangent sheaf to the normalized cusp fibre.',
        exact_application='The lattice basis, invariant vectors, marked elliptic lifts and cusp collar are identified term by term with common convention P202. The source gamma is the first-coordinate functional, source v_j are the displayed v_j, source c(sigma) is the same analytic cocycle, and source l_j=l_j. The source clockwise peripheral generators lift inverses of the paper’s counterclockwise base loops; no affine coefficient is silently negated. Theorem7.17 supplies precisely the printed group formula. A’s section locator is corrected to pages89–90.',
        read_extent='Fresh online opening and full reading of each named statement/setup and the complete proofs of Proposition6.7 and Theorem7.17. Theorem7.17 and its full printed proof were also rendered and visually read on printed p.57. Section10.4 was fully read. Only the indicated parts of section7.5 were reread here; no new complete reading of Lemma7.16 or the whole article is claimed.',date_utc=stamp),
    dict(source_key='Completed-I statement metadata',url='',version='Attached current statement metadata and previously extracted statement-only packet; Paper I source/PDF closed',
        locus_read='I.3.2/tag01QH; I.7.8/tag01Q6; I.8.1/tag01QB; I.12.8/tagPI07. Complete finite-coordinate statement and exact selected source_statement fields in attached inventory.',
        sha256=hashlib.sha256(metadata.read_bytes()).hexdigest(),bytes=metadata.stat().st_size,
        own_paraphrase='The current records identify the normalized theta-period special values, the standard fixed-data classification, the arbitrary affine/cusp classification and the cubic/quartic branch convention. The arbitrary-data statement defines l0 as the first coordinate of the cusp cocycle and uses the same polynomial p.',
        exact_application='Current reader destinations are I.3.2 p25, I.7.8 p51, I.8.1 p52 and I.12.8 p82. P202 and C5c use the same normalized periods; the local branch maps are r³=t∘pi and s⁴=(t−1)∘pi, with the recorded arc and derivative signs. The classification statements supply the exact fixed data, not a newly asserted fundamental-group theorem.',
        read_extent='Read selected current metadata rows, the complete permitted statement-only packet and the three exact source_statement fields selected by Paper I plus exact label. No Paper I manuscript/PDF or proof was opened. Packet SHA256='+hashlib.sha256(packet.read_bytes()).hexdigest()+'; inventory SHA256='+hashlib.sha256(inventory.read_bytes()).hexdigest()+'. No check of the closed Paper I proofs is credited.',date_utc=stamp),
]
tsv('S6_SERIES_PUBLISH_firstpart_sources.tsv',source_specs)
events=[]
for i,(sid,outcome,where) in enumerate([
    ('Known and new A–G','Read all seven current brief rows against the already completed source-by-source literature claim records and the current complete Theorems E and F. Preserve the narrowed B wording and all fixed-data qualifications; correct only A pagination and F open-locus wording. This is a bounded reconciliation, not a new proof of novelty or another full literature search.','All seven current status rows; complete current E and F'),
    ('P202 / E / E8 / C5c','Read complete current P202, complete E8 statement/proof and complete current C5c statement/proof, then compare every proposed change. Identify fixed lifts and roots, beta=beta_c in the headline through E8’s explicit index-six lattice inclusion, gamma and the cusp cocycle, inverse peripheral generators and the exact determinant presentation. Every resonance equation, module, character, length, rank and conclusion is unchanged.','Complete old/receiving conventions and E; complete current E8; complete old/receiving C5c'),
    ('AC26 source loci','Freshly open the primary source and read the named setup and source loci, including full Proposition6.7/Theorem7.17 proofs and visual page57; record exact scope and reading limits.','AC26 named loci in source table'),
    ('Paper I metadata locators','Read only permitted attached statement metadata and statement-only packet. Verify four exact current destinations and preserve their permanent targets. No Paper I source/PDF or proof is opened.','Metadata records and finite-coordinate statement-only packet'),
],1):
    eid=f'publish:c3:firstpart:bounded:{i:02d}'
    events.append(dict(statement_id=sid,date='2026-11-22',who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; inherited effort not separately exposed; continuation3 provenance',
        type='used and rechecked in this run',outcome=outcome+' Exposed work; no independent or final-PDF credit.',event_id=eid,
        phase='bounded source and notation comparison',source_file=REL+'/S6_SERIES_PUBLISH_firstpart_CHECK_EVENTS.tsv',source_row='',
        source_event_type='used and rechecked in this run',evidence_group=eid,publish_input_file='',publish_input_row='',date_utc=stamp,where=where))
tsv('S6_SERIES_PUBLISH_firstpart_CHECK_EVENTS.tsv',events)
print(json.dumps({'guards':len(guards),'defects':len(defects),'source_rows':len(source_specs),'events':len(events),'shared_main_written':False}))
