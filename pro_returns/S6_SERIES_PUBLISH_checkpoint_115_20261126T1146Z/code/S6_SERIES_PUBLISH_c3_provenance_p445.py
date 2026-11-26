#!/usr/bin/env python3
"""Prepare the bounded, fully read P280/P4.45 proposal; never edit main."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import re

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'agents/continuation3_provenance/p445'
MAIN=ROOT/'S6_SERIES_PUBLISH_II.tex'
PROPOSED=OUT/'S6_SERIES_PUBLISH_p445_proposed.tex'
source=MAIN.read_text()
new=PROPOSED.read_text()
anchor=source.index(r'\label{night:P4.45}')
start=source.rfind(r'\begin{proposition}',0,anchor)
end=source.index(r'\end{proof}',anchor)+len(r'\end{proof}')
old=source[start:end]
assert 'In an actual torus degeneration' in old
assert source.count(old)==1
assert '\r' not in new

def write_tsv(name, rows):
    with (OUT/name).open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t',lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows)

def digest(text):
    return hashlib.sha256(text.encode()).hexdigest()

write_tsv('S6_SERIES_PUBLISH_p445_guards.tsv',[dict(
    change_id='II-C3-P445-GUARD-001',statement_id='night:P4.45',
    source_file='S6_SERIES_PUBLISH_II.tex',old_sha256=digest(old),new_sha256=digest(new),
    old_text=old,new_text=new,proposed_file=str(PROPOSED.relative_to(ROOT)))])

lemma_end=new.index(r'\end{proof}')+len(r'\end{proof}')
lemma=new[:lemma_end]
prop=new[lemma_end:].strip()
new_proof=prop[prop.index(r'\begin{proof}'):]
old_proof=old[old.index(r'\begin{proof}'):]
old_statement=old[old.index('\n\n')+2:old.index(r'\end{proposition}')]
new_statement=prop[prop.index('\n\n')+2:prop.index(r'\end{proposition}')]
assert old_statement.replace('an actual torus','a torus')==new_statement

def segment(text,begin,finish):
    a=text.index(begin)
    b=text.index(finish,a)+len(finish)
    return text[a:b]

defects=[]
def add(types, owner, before, after, reason):
    assert before in old
    assert after in new
    defects.append(dict(change_id=f'II-C3-P445-{len(defects)+1:03d}',type=types,
        statement_id=owner,old_location='P4.45 complete proof in the unchanged base owner',
        old_page='final concordance pending',new_location='P280 immediately before P4.45; exact receiving owner',
        new_page='integrated build pending',old_text=before,new_text=after,reason=reason,
        review_status='Complete old proof and receiving P280/P4.45 read; exposed comparison; final owner-level checks passed; no independent or PDF-page credit'))

add('D08','night:P4.45',old_statement,new_statement,
    'Remove the process adjective. All mathematical clauses and the full domain remain identical.')
add('D14;D20;D25','lem:II:ordinary-triple-factor-lifts',
    segment(old,r'\item Write the full reduced critical-curve ideal as',r'Then $f=F(u,x,y,h)$.'),lemma,
    'Put the precise normalization and factor-lift owner before its application. The old reduced-generator lift did not identify lifts of each analytic component with its full multiplicity. The determinant presentation, exact normalization maps and local factor blocks now prove that identification, including reducible C and the zero central cubic.')
add('D22;D25','night:P4.45',
    segment(old,'Arbitrarily small constant changes','We also choose its leading coefficient nonzero.'),
    segment(new,'The coefficient\nperturbations preserve','In both cases the choices are arbitrarily small.'),
    'Perturb the proved analytic factor lifts, with every original positive power. The weighted logarithmic derivative has a quadratic numerator; its discriminant is nonzero by the explicit real-root argument, proving dense available parameters and a simple nonzero full critical value.')
add('D20;D25','night:P4.45',
    segment(old,r'\item After substituting $u=Hv$',r'\qquad \beta(0)\ne0.'+'\n'+r'\]'),
    segment(new,r'\item Keep $\tau=\epsilon$ fixed',r'\label{eq:II:triple-critical-value-coordinate}'+'\n'+r'\end{equation}'),
    'The critical-centre equation differentiates the complete weighted product and its unit. Its exponent is N=sum_j m_j n_j. The coefficient functions remain evaluated at w=Hv, so no homogeneous-function assertion is imposed on variable coefficients.')
add('D12;D25','night:P4.45',
    segment(old,'Choose a small morsification',r'\qquad f_s=F(u,x,y,H_s(x,y)).'+'\n'+r'\]'),
    segment(new,r'Set $\widehat h=',r'At $s=0$ this is $H_0=h$.'),
    'Apply the already-proved finite-gradient construction of A.5.17 to the same reduced plane function, and define the full family using the two exact inverse identities. No second gradient or Morse proof is introduced.')
add('D25','night:P4.45',
    segment(old,'On its $u$-critical branch',r'critical point with nonzero critical value.'),
    segment(new,r'\item The $w$-critical centre is',r'\label{eq:II:triple-full-Hessian}'+'\n'+r'\end{equation}'),
    'The full gradient, transverse Hessian entry, Schur complement and determinant are computed at the same point and nonzero value q0. This proves the Morse point with unequal original component multiplicities.')
add('D04;D25','night:P4.45',
    segment(old,r'\item All deformations above','This proves the assertion.'),
    segment(new,r'\item We check boundary transport','assertion permits these inner and outer balls.'),
    'Replace the bare P4.28 analogy by the exact P295 hypothesis check. Three branch equations are straightened by (a,b,z) to (a alpha,b beta,z); the full weighted unit is removed with an explicit inverse. The first coefficient deformation uses the outer ball; the critical-centre construction uses an inner ball after coefficients are fixed.')
add('D25','night:P4.45',
    segment(old,'The Morse\nvanishing sphere embeds','This proves the assertion.'),
    segment(new,'The local Morse sphere',r'contrary to its transported square $-2$.'),
    'Compose the inner local transport, inclusion at a value regular for the outer ball, outer target transport and inverse coefficient-parameter transport. Each map applies to the full function and preserves the compact sphere square in the initial torus fibre.')
write_tsv('S6_SERIES_PUBLISH_p445_defects.tsv',defects)

# Full labels/targets and display structure are checked in memory, without main writes.
for pattern in (r'\\label\{([^}]+)\}',r'\\hypertarget\{([^}]+)\}'):
    for item in re.findall(pattern,old):
        assert re.findall(pattern,new).count(item)==re.findall(pattern,old).count(item),item
st=[]
for op,env in re.findall(r'\\(begin|end)\{([^}]+)\}',new):
    if op=='begin': st.append(env)
    else: assert st.pop()==env,env
assert not st
for env in ('equation','align','gather','multline'):
    for body in re.findall(r'\\begin\{'+env+r'\*?\}(.*?)\\end\{'+env+r'\*?\}',new,re.S):
        assert not re.search(r'\n[ \t]*\n',body),env
all_labels=set(re.findall(r'\\label\{([^}]+)\}',source+new))
refs=[]
for keys in re.findall(r'\\(?:cref|Cref|ref|eqref|SeriesRef)\*?\{([^}]+)\}',new):
    refs.extend(keys.split(','))
assert all(k in all_labels for k in refs),[k for k in refs if k not in all_labels]
for key in ('push:src:E.5.2','push:src:E.5.3'):
    assert key not in old and key not in new
assert r'\tag{' not in new
assert not re.search(r'\b(actual|requested|candidate|certificate|diagnostic|survivor)\b',new)

now=datetime.now(timezone.utc).isoformat()
who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; inherited effort not separately exposed; continuation3 provenance'
events=[]
def event(owner,kind,outcome,suffix):
    events.append(dict(statement_id=owner,date=now[:10],who=who,type=kind,outcome=outcome,
        event_id=f'publish:c3:p445:{suffix}',phase='publication proof and consumer comparison',
        source_file='agents/continuation3_provenance/p445/S6_SERIES_PUBLISH_p445_CHECK_EVENTS.tsv',
        source_row='',source_event_type=kind,evidence_group=f'publish:c3:p445:{suffix}',
        publish_input_file='',publish_input_row='',date_utc=now,
        where='Complete bounded owner, exact predecessor and required consumer/application maps'))
event('lem:II:ordinary-triple-factor-lifts','used and rechecked in this run',
    'Read the complete current P4.45 predecessor and complete P280 receiving proof. Check P^3 saturation through the CI graded pieces; choose the explicit smooth coordinate w=u+lambda h and regular denominator; compute the determinant matrix and its fractional normalization module. Its associated primes prove injectivity, simple-root maps identify normalization off the origin, and the two depth-two modules agree by local cohomology. The zero binary cubic has local square-zero normalization fibre and one analytic component. Otherwise the coefficient implicit-function map gives the exact monic blocks; B_j[w^-1]=S[w^-1]/(phi_j), normal locality and regular w prove irreducibility. The monic H term proves the same order on every critical branch. Every original component unit is incorporated to its given power in U. Foundations supplied the exposed cubic-algebra derivation and read this owner; this event is used-and-rechecked, not independent. No rendered-page credit.','factor-lifts-read')
event('night:P4.45','used and rechecked in this run',
    'Read the complete old and final receiving proof, the complete P295 and A.5.17 input proofs, P298 in context, and the complete P4.46 consumer. Preserve every statement clause, removing only the word actual. The receiving family is U times the product of each proved factor lift to its original positive power. Generic weighted roots give a simple off-support critical point. Exact triple-branch coordinate maps and the shared degree-N unit root provide all P295 boundary data. Coefficients deform on an outer ball; the beta/Lambda inverse and plane morsification use a subsequent inner ball. The complete critical value is hhat_s^N; the transverse Hessian and Schur determinant are nonzero at the same selected point. The nested maps carry its sphere into the initial full torus fibre. P4.46 applies at each of its ordinary planar nodes with all local branches D4; its other conormal arguments are outside this guard. Exposed comparison, with no independent or final-page claim.','full-function-read')
event('lem:II:ordinary-triple-factor-lifts','computation or formal certificate',
    'Executed code/S6_SERIES_PUBLISH_c3_provenance_p445_algebra.py. Exact SymPy polynomial arithmetic verifies det(M)=f, all three column relations and the three normalization multiplication identities modulo at^3+bt^2+ct+d. This verifies the printed algebra only; the finite-module, depth and analytic-normalization arguments are covered by the exposed proof read.','cubic-algebra-computation')
event('night:P4.45','computation or formal certificate',
    'The same executed algebra program verifies the weighted logarithmic-derivative numerator at each of its three roots, its discriminant at roots -1,0,1 as (mu1-mu3)^2+4 mu2(mu1+mu2+mu3), and the symbolic 3x3 Schur-complement determinant L N^2 q0^(2N-2) det(Q). This is exact arithmetic for the displayed identities, not an analytic boundary-transport or independent proof claim.','weighted-Hessian-computation')
write_tsv('S6_SERIES_PUBLISH_p445_CHECK_EVENTS.tsv',events)

status=[]
for owner in ('lem:II:ordinary-triple-factor-lifts','night:P4.45'):
    for n in range(1,26):
        kind=f'D{n:02d}'
        state='checked in bounded owner'
        note='Complete owner read; exact changed instances logged; no remaining owner-level instance found.'
        if n in (10,16):
            state='inherited done, preserved'
            note='Permanent tags, labels and current renderer retained; both mathematical titles present.'
        if n in (14,15,23,24):
            state='local check complete; integrated gate deferred'
            note={14:'P280 precedes its only consumer. Complete subsection/global structure is owned by root.',
                  15:'No front-matter edit. Root owns the final three-way provenance and first-part pass.',
                  23:'Source has balanced environments and no blank display paragraph. Root owns pdfLaTeX and page reading.',
                  24:'P4.45 statement scope is unchanged. Root owns final front/body consistency.'}[n]
        if n==25:
            note='The original full multiplicity gap is resolved by exact factor lifts and the full-function critical value and transport maps; complete old/receiving read.'
        status.append(dict(owner=owner,unit='Further uniform transverse sectors; bounded P280/P4.45 only',
            defect_type=kind,status=state,note=note,
            subsection_closure='No full-subsection closure or movement credit: P4.44/P4.46 remain with root.'))
write_tsv('S6_SERIES_PUBLISH_p445_unit_status.tsv',status)

comparison=r'''# P280 / P4.45: complete original and receiving comparison

## Outcome and boundary

The bounded guard replaces only the complete old P4.45 owner. It adds P280 immediately before that proposition. All original P4.45 labels and permanent targets remain. Its printed assertion changes only “an actual torus degeneration” to “a torus degeneration”; every mathematical clause is identical. Neither protected E.5.2/E.5.3 statement is touched. There are no edits to P254, P256, P4.44 or P4.46.

Both complete proofs were read. P295, A.5.17 and P298 were read in full as inputs; P4.44 was read as adjacent context and P4.46 was read in full as the sole mathematical consumer. These are exposed reads. Foundations supplied the explicit normalization algebra and reviewed the receiving algebra; no independent event is claimed.

## Exact old-to-receiving mathematics

| Original component | Receiving owner / exact map | Preserved conclusion |
|---|---|---|
| Entire critical curve `(u,h)`, reduced singular `h`; generic transverse multiplicity three | P280 proves saturation of `P^3` through its complete-intersection graded pieces | The same reduced equation has a cubic expression in the two ideal generators. |
| A lift of the reduced equation obtained by replacing `h` with `H` | P280 uses `w=u+lambda h`, inverse `u=w-lambda h`; its determinant presentation gives the actual normalization | Every original analytic factor receives its own polynomial lift with the same generic order on every branch of the critical curve. |
| No distinction between one analytic factor and several factors at the central point | The exact normalization fibre has basis `1,omega,nu`. If the four cubic coefficients vanish, its augmentation ideal squares to zero, so the normalization is local and the support is irreducible | The common-power case follows from the ring itself. |
| Reduced cubic coefficient perturbation | In the nonzero case, `Q=prod Q_j`, `B_j=S[T]/(wT-h,Q_j)` and `B_j[w^-1]=S[w^-1]/(phi_j)` identify each original irreducible factor. `Phi_j=w^n_j Q_j(H/w)` specializes exactly to `phi_j` | All original multiplicities `m_j` and their unit `U` remain in the full family. Unequal multiplicities and reducible critical curves are included. |
| A simple critical root of an unweighted cubic | The full central weighted polynomial has logarithmic derivative `sum mu_i/(v-a_i)`. Its quadratic numerator has nonzero discriminant on a dense open set; the real-root argument exhibits one such configuration for every positive weight list | Arbitrarily small permitted coefficient choices give a simple critical point off every factor, with nonzero full critical value. |
| `F_u/H^2=0` and reduced critical value `H^3 beta` | `Psi_v=0`, `w=H V(x,y,H)` and `N=sum m_j n_j` give the full value `H^N beta` | The full unit and all coefficient derivatives are included. Variable coefficient functions are evaluated at `w=Hv`; no false homogeneity of the full analytic function is used. |
| Cube-root inverse and reduced plane morsification | `Lambda=H beta^(1/N)`, its two inverse identities and `H_s=R(x,y,hhat_s)` | The same reduced singular plane germ is morsified, and the full critical value is exactly `hhat_s^N`. The finite-gradient and Morse-sphere constructions apply through A.5.17. |
| Three-variable reduced Hessian | `(G_s)_ww=H_s^(N-2) Psi_vv`, Schur complement `N q0^(N-1) Q` | Determinant `(G_s)_ww N^2 q0^(2N-2) det Q` is nonzero at the same nonzero full critical value. |
| Bare P4.28 boundary analogy | Three branch equations `(a,b,a alpha+b beta)` map to `(X,Y,X+Y)` via `(X,Y)=(a alpha,b beta)`. The shared degree-N unit root has the displayed implicit inverse | The exact fixed transverse polynomial and a boundary-transverse product direction satisfy P295 for the full weighted function. |
| One fixed-boundary claim for successive coefficient and plane changes | Coefficients deform on the first ball K. After fixing them, the beta inverse is defined on a smaller ball K'. Inner transport, regular-value inclusion, outer target transport and inverse coefficient transport are composed | The Morse sphere maps into the initial full torus fibre with its square preserved. No extension of the local beta inverse to the first outer boundary is assumed. |

## Consumer and ownership checks

The exhaustive label/tag/printed-name lookup has one outward mathematical consumer, P4.46. Its last step has two ordinary planar nodes of the entire reduced critical curve and transverse D4 along every branch. At either node, the ideal has the form `(u,h)` with `h` a reduced planar node, so P4.45 applies directly. P4.46's conormal/Euler proof is owned and being updated by root through P254/P256; no guard here overlaps that work. The other occurrences are the local dictionary, the further-result entry and the Programs row. Their claim scopes are unchanged.

P280's normalization algebra is its single owner. P256 owns the separate primary conductor/symbolic-square equality. This proposal does not repeat that conductor proof. P445 applies A.5.17's existing finite-gradient and Morse-sphere constructions rather than adding another such proof.

## Checks and limits

One whole-owner guard matches the current source. Old label and permanent-target multiplicities are preserved. The receiving reference keys resolve; display environments have no blank paragraphs; the environment stack balances; there are no inherited manual equation tags. The exact P4.45 statement comparison removes only its process adjective. The two protected E.5.2/E.5.3 blocks are outside the guard.

The delivered editorial algebra program was executed. It verifies the determinant, generator relations, multiplication table, weighted critical quadratic and Schur determinant by exact symbolic arithmetic. Its scope is those identities. The module-theoretic, analytic and topological steps are supported by the exposed complete proof comparison, not by that program.

The eight defect rows record exact old/new text, four check events record two complete exposed reads and two bounded computations, and the owner-level 25-class status table does not claim a full-subsection closure. Root owns the integrated build, current page reading, final provenance/counts and global structure.
'''
(OUT/'S6_SERIES_PUBLISH_p445_comparison.md').write_text(comparison)
print(f'Prepared one guard, {len(defects)} exact defect rows, {len(events)} check events and {len(status)} owner-class outcomes; main unchanged.')
