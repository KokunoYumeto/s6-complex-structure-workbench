#!/usr/bin/env python3
"""Prepare exact conductor-source application guards; never write shared source."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'agents/continuation3_provenance/de_jong'
OUT.mkdir(parents=True, exist_ok=True)
main = (ROOT / 'S6_SERIES_PUBLISH_II.tex').read_text()
now = datetime.now(timezone.utc).isoformat()
changes = []

def change(owner, old, new, kind, reason):
    assert main.count(old) == 1, (owner, main.count(old), old[:80])
    changes.append(dict(change_id=f'II-C3-DJVS-{len(changes)+1:03d}',
        type=kind, statement_id=owner, old_location=f'{owner}: conductor application',
        old_page='final concordance pending', new_location=f'{owner}: same proof step',
        new_page='integrated build pending', old_text=old, new_text=new,
        reason=reason, review_status='Complete current proof read; receiving comparison pending'))

change('night:P4.41', r'''\item We use the ring condition of the conductor:
\begin{equation}
 \operatorname{Hom}_{\mathcal O_S}(I,I)=
 \operatorname{Hom}_{\mathcal O_S}(I,\mathcal O_S).
\label{eq:II:manual:4.41b}
\end{equation}
The right side is the normalization algebra by finite duality,
and $I$ is an ideal of that algebra. For the determinant
presentation of a Cohen--Macaulay codimension-two conductor
inside a Gorenstein hypersurface, this condition is equivalent
to membership of the adjugate entries in $I$. This is precisely
de Jong--van Straten, Theorem~1.12, printed p.~532
\cite{DeJongVanStraten1990Normalization}. Its hypotheses hold
here: the ambient space is regular, the reduced support is a
hypersurface, and its conductor quotient is Cohen--Macaulay.
We give all the matrices used below.''', r'''\item Put $\mathcal P=\mathbb C\{x,y,z\}$, let $f$ be the
reduced local equation of the support, and set
$R=\mathcal P/(f)$ and $\mathfrak c=I/(f)\subset R$.
The multiplier identification in \cref{lem:II:conductor-duality}
gives $\operatorname{Hom}_R(\mathfrak c,R)=\overline R$.
Since $\mathfrak c$ is also an ideal of $\overline R$, its
ring condition is
\begin{equation}
 \operatorname{Hom}_R(\mathfrak c,\mathfrak c)=
 \operatorname{Hom}_R(\mathfrak c,R).
\label{eq:II:manual:4.41b}
\end{equation}
Apply \cite[Lemma~1.9, Corollary~1.11 and Theorem~1.12,
pp.~531--532; Remark~1.13, p.~533]{DeJongVanStraten1990Normalization}
with base $\operatorname{Spec}\mathbb C$, ambient ring $\mathcal P$,
hypersurface equation $f$, ambient ideal $I$, and hypersurface
ideal $\mathfrak c$. The quotient $\mathcal P/I=R/\mathfrak c$
is Cohen--Macaulay of codimension two by
\cref{lem:II:conductor-duality}. A Hilbert--Burch matrix for $I$,
with a coefficient column for $f$ appended, gives a square
presentation matrix $M$ with $\det M=f$, after the corresponding
choice of signs. The cited criterion says that every entry of
$\operatorname{adj}(M)\bmod f$ belongs to $\mathfrak c$.
The quotient map $\mathcal P\to R$ has preimage
$\mathfrak c$ equal to $I$, so this is exactly membership of
every ambient adjugate entry in $I$. We use the matrices below.''',
    'D25', 'The ambient ideal I is not itself an R-module. State the quotient c=I/(f), use the previously proved multiplier identification, and give the exact source-specialization and inverse-image maps. The former ring equality is preserved with its correct domain; the same ambient adjugate condition follows.')

change('night:P4.47', r'''\item The conductor ring condition \eqref{eq:II:manual:4.41b}
applies to this regular ambient ring, reduced hypersurface and
Cohen--Macaulay conductor quotient. Its two-by-two adjugate calculation
\cite[Theorem~1.12, p.~532]{DeJongVanStraten1990Normalization}
gives $f\in I^2$. Write $f=A g^2+Bgh+Ch^2$.''', r'''\item Apply the conductor ring condition \eqref{eq:II:manual:4.41b}
to $\mathfrak c=I/(f)\subset R$, with the ambient ideal $I=(g,h)$
just proved. Write $f=\lambda g+\mu h$. The determinant and adjugate are
\[
 M=\begin{pmatrix}h&\lambda\\-g&\mu\end{pmatrix},\qquad
 \det M=f,\qquad
 \operatorname{adj}(M)=\begin{pmatrix}\mu&-\lambda\\g&h\end{pmatrix}.
\]
Theorem~1.12, p.~532 of \cite{DeJongVanStraten1990Normalization},
with the same regular ambient ring and Cohen--Macaulay quotient,
therefore gives $\lambda,\mu\in I$. Thus $f\in I^2$.
Write $f=A g^2+Bgh+Ch^2$.''',
    'D18', 'Supply the exact ambient-to-hypersurface ideal map and the two-generator determinant substitution at the cited theorem. This is the existing adjugate application with every matrix entry and sign specified.')

change('night:P4.49', r'''Appending $(a,b,c)$ to its Hilbert--Burch matrix gives
determinant $axk+bxh+ch^2$. The adjugate form of \eqref{eq:II:manual:4.41b}
\cite[Theorem~1.12, p.~532]{DeJongVanStraten1990Normalization}
applies to this same conductor: its quotient is Cohen--Macaulay
and the reduced hypersurface lies in the regular ambient ring. The colon ideals''',
    r'''Appending $(a,b,c)$ to its Hilbert--Burch matrix gives
determinant $axk+bxh+ch^2$. Put $\mathfrak c=I/(f)\subset R$.
Apply the adjugate form of \eqref{eq:II:manual:4.41b}
and \cite[Theorem~1.12, p.~532]{DeJongVanStraten1990Normalization}
through the quotient $\mathbb C\{x,y,z\}\to R$: its ambient
conductor ideal is this $I$, its hypersurface ideal is $\mathfrak c$,
and its Cohen--Macaulay quotient is $R/\mathfrak c$.
Thus each adjugate entry belongs to $I$. The colon ideals''',
    'D18', 'Identify both source ideals and the same quotient map in the three-generator application. No radicality of the conductor image is used; the Hilbert--Burch presentation and subsequent colon calculations retain their full scope.')

change('night:P4.49', r'''$d=-\kappa yh$. The conductor identifies
$\operatorname{Hom}(I,\mathcal O_S)$ with the
normalization, generated by $1,n_1,n_2$, where the
adjugate fractions are''', r'''$d=-\kappa yh$. The multiplier identification
$\operatorname{Hom}_R(\mathfrak c,R)=\overline R$, with
$\mathfrak c=I/(f)$ for this conductor ideal, gives the
normalization generated by $1,n_1,n_2$, where the
adjugate fractions are''',
    'D25', 'Use the hypersurface conductor c=I/(f) in the Hom domain for the second ideal form. The existing adjugate fractions and multiplication relations are unchanged.')

def write_tsv(name, rows):
    with (OUT / name).open('w', newline='') as stream:
        writer=csv.DictWriter(stream,fieldnames=list(rows[0]),delimiter='\t',lineterminator='\n')
        writer.writeheader();writer.writerows(rows)

def owner(s,label):
    p=s.index(r'\label{'+label+'}')
    a=s.rfind(r'\begin{',0,p)
    b=s.index(r'\end{proof}',p)+len(r'\end{proof}')
    return s[a:b]

receiving=main
for row in changes:
    receiving=receiving.replace(row['old_text'],row['new_text'],1)
labels=['night:P4.41','night:P4.47','night:P4.49']
for label in labels:
    old=owner(main,label);new=owner(receiving,label)
    end=old.index(r'\begin{proof}')
    assert old[:end]==new[:new.index(r'\begin{proof}')]
    assert re.findall(r'\\label\{([^}]+)\}',old)==re.findall(r'\\label\{([^}]+)\}',new)
    assert re.findall(r'\\hypertarget\{([^}]+)\}',old)==re.findall(r'\\hypertarget\{([^}]+)\}',new)
    (OUT / ('S6_SERIES_PUBLISH_djvs_'+label.split(':')[1].replace('.','_')+'_proposed.tex')).write_text(new+'\n')

guards=[]
for row in changes:
    guards.append(dict(change_id=row['change_id'],statement_id=row['statement_id'],
        source_file='S6_SERIES_PUBLISH_II.tex',
        old_sha256=hashlib.sha256(row['old_text'].encode()).hexdigest(),
        new_sha256=hashlib.sha256(row['new_text'].encode()).hexdigest(),
        old_text=row['old_text'],new_text=row['new_text'],
        proposed_file='agents/continuation3_provenance/de_jong/S6_SERIES_PUBLISH_djvs_'+row['statement_id'].split(':')[1].replace('.','_')+'_proposed.tex'))
write_tsv('S6_SERIES_PUBLISH_djvs_guards.tsv',guards)
write_tsv('S6_SERIES_PUBLISH_djvs_defects.tsv',changes)

pdf=ROOT.parents[1]/'tmp/c3_provenance_primary/DeJongVanStraten1990.pdf'
raw=pdf.read_bytes()
write_tsv('S6_SERIES_PUBLISH_djvs_sources.tsv',[
 dict(source_key='DeJongVanStraten1990Normalization',
      url='https://download.uni-mainz.de/mathematik/Algebraische%20Geometrie/DvS-Publikationen/Deformations%20of%20the%20normalization%20of%20hypersurfaces%20-%201990.pdf',
      version='Original journal facsimile hosted by the author; Math. Ann. 288 (1990), 527–547',
      sha256=hashlib.sha256(raw).hexdigest(),bytes=len(raw),
      locus_read='Conventions and §1 pp.528–533 through Remark1.13 and proof of Theorem1.2; complete Definition1.5, Lemma1.6 printed map, Propositions1.7–1.8 proofs, Lemma1.9, Proposition1.10, Corollary1.11 and Theorem1.12 proofs. Appendix conventions and A1–A11 pp.543–546 including all printed proofs. Page images 528,530–533,544 read.',
      own_paraphrase='The base may be a point and the ambient ring a regular local analytic ring. For a codimension-two Cohen–Macaulay ideal containing the hypersurface equation, a Hilbert–Burch presentation extends by its coefficient column. The ring condition for the quotient ideal is equivalent to membership of the adjugate entries in that ideal, and to vanishing of evaluation on the ambient normal module. The proof identifies evaluation with the adjugate via the periodic resolution. The separate reduced-conductor assumption in Theorem1.2 enters its additional identification with admissibility on p.533.',
      exact_application='Use base C, P=C{x,y,z}, F=f, ambient I_P=I and hypersurface c=I/(f). P222 gives the Cohen–Macaulay quotient and multiplier duality for the finite normalization. The quotient preimage of c is I, so the source criterion is exactly the ambient adjugate membership used by P441, P447 and both P449 ideal forms.',
      limits='No independent derivation, whole-article reading, or access to the unprinted exercise in Lemma1.6 is claimed. The normalization-identification input is the already proved P222; Theorem1.12 supplies the adjugate criterion.',date_utc=now),
 dict(source_key='DeJongVanStraten1990Normalization:metadata',
      url='https://link.springer.com/article/10.1007/BF01444547',
      version='Publisher article page reopened 22 November 2026',sha256='',bytes='',
      locus_read='Title, authors, journal/volume/pages, publication and received dates, DOI and recommended citation',
      own_paraphrase='Publisher metadata confirms title, authors, volume288, pp.527–547, December1990 issue date and DOI10.1007/BF01444547.',
      exact_application='The existing bibliography is correct and uses the author-hosted journal facsimile. Its page532 locator is correct. No bibliography replacement or new numbered bibliography correction is needed.',
      limits='Metadata page only; mathematical reading used the author-hosted primary facsimile.',date_utc=now)
])
if '--finalize' in sys.argv:
    all_labels=set(re.findall(r'\\label\{([^}]+)\}',main))
    for label in labels:
        new=owner(receiving,label)
        for keys in re.findall(r'\\(?:c|C)?ref\*?\{([^}]+)\}|\\eqref\{([^}]+)\}',new):
            assert all(k in all_labels for k in (keys[0] or keys[1]).split(','))
        stack=[]
        for op,env in re.findall(r'\\(begin|end)\{([^}]+)\}',new):
            if op=='begin':stack.append(env)
            else:assert stack.pop()==env
        assert not stack and '\r' not in new
        for body in re.findall(r'\\\[(.*?)\\\]',new,re.S):
            assert not re.search(r'\n[ \t]*\n',body)
    for row in changes:
        row['review_status']='Complete original and receiving P441/P447/P449 proofs read and compared, plus complete P222 input proof. All statements, labels and targets unchanged; exposed source/application comparison, no independent credit. Current guards match; integrated rendering remains root-owned.'
    write_tsv('S6_SERIES_PUBLISH_djvs_defects.tsv',changes)
    events=[]
    for label,detail in [
        ('night:P4.41','Reopened the exact primary Theorem1.12 statement and complete printed proof p532, its matrix-factorization setup and the analytic/local-ring conventions. Read the complete current and receiving P441 proofs and complete P222 input. Replace the ambient ideal in Hom by c=I/(f), identify its dual with the same normalization by the existing multiplier map, and specialize the source to base C and P=C{x,y,z}. The inverse-image equality q^(-1)(c)=I gives exactly the original ambient adjugate membership. The reduced conductor-image assumption used for admissibility in Theorem1.2 is not used in this ring-to-adjugate proof. All Hessian, factor, boundary-transport and equality-case arguments are preserved.'),
        ('night:P4.47','Read complete current and receiving proofs. With the already proved ambient ideal I=(g,h), use c=I/(f) in the same hypersurface ring. The explicit matrix [[h,lambda],[-g,mu]] has determinant lambda*g+mu*h and adjugate [[mu,-lambda],[g,h]], so the cited criterion yields precisely f in I^2. The original square completion, local normalization, full-power identification, critical-point calculation and torus transport are unchanged. No new computation or independent proof credit is claimed.'),
        ('night:P4.49','Read complete current and receiving proofs, including both conductor-ideal forms. Identify the source ideal in R as c=I/(f) and correct the later Hom domain to that same quotient. The two existing Hilbert–Burch matrices, adjugate fractions, colon identities, normalization multiplication tables, rational-normal-cubic map and full-power deformation constructions are unchanged. The source criterion uses the CM ambient quotient through the explicit quotient map; the original full statements remain byte-identical.')]:
        eid='publish:c3:djvs:'+label.split(':')[1]
        events.append(dict(statement_id=label,date=now[:10],
            who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; inherited effort not separately exposed; continuation3 provenance',
            type='used and rechecked in this run',outcome=detail,event_id=eid,
            phase='publication source and proof comparison',
            source_file='agents/continuation3_provenance/de_jong/S6_SERIES_PUBLISH_djvs_CHECK_EVENTS.tsv',
            source_row='',source_event_type='used and rechecked in this run',evidence_group=eid,
            publish_input_file='',publish_input_row='',date_utc=now,
            where='Complete old and receiving owner plus exact primary-source application'))
    write_tsv('S6_SERIES_PUBLISH_djvs_CHECK_EVENTS.tsv',events)
    write_tsv('S6_SERIES_PUBLISH_djvs_status.tsv',[
        dict(statement_id=label,defect_type='D18',status='exact source application resolved; admission pending',
             note='Primary theorem, complete printed proof, analytic/local-ring setting and source-to-receiving ideal maps checked. Existing bibliography and p532 locator correct. No whole-unit class closure or rendered-page credit.')
        for label in labels])
    (OUT/'S6_SERIES_PUBLISH_djvs_comparison.md').write_text(r'''# Exact de Jong–van Straten conductor application

## Outcome

The original bibliography entry and Theorem 1.12, printed p. 532 locator are correct. Four bounded guards supply the exact quotient-ideal maps at P4.41, P4.47 and P4.49. Every printed proposition statement, permanent target and label remains byte-identical. The complete original and receiving proofs of all three owners were read, as was the complete earlier P222 conductor-duality proof. This is exposed work and carries no independent derivation credit.

## Primary source and scope

The author-hosted journal facsimile was downloaded again and opened online at the complete cited theorem and proof. The analytic-germ convention is on p. 528. The construction on pp. 531–532 starts with an ambient regular local ring, a hypersurface equation and a codimension-two Cohen–Macaulay quotient. The exact correspondence between the ring condition and the adjugate entries is Theorem 1.12. Remark 1.13, p. 533 gives its maximal-minor formulation. The printed proof obtains the pairing from the dual periodic resolution. The additional comparison with admissibility in Theorem 1.2 uses a reduced conductor-image ideal at its separate p. 533 step; that step is not an input to any of the three applications here.

The complete reading extent is recorded in the source table: §1 pp. 528–533 at the listed statements and arguments, the appendix conventions and A1–A11 pp. 543–546. Lemma 1.6 leaves its proof as an exercise and prints its multiplier map; the record claims that printed map only. No full-article or unprinted-proof reading is claimed. The publisher page separately confirms the title, authors, journal, volume, pages, DOI and 1990 issue date. No bibliography change is needed.

## Maps and preservation

| Owner | Original application | Exact receiving map | Preserved proof content |
|---|---|---|---|
| P4.41 | The ambient ideal I was written directly inside Hom over the hypersurface ring. | Set P=C{x,y,z}, R=P/(f), c=I/(f). P222 identifies Hom_R(c,R) with the finite normalization by multiplication. Because c is also its ideal, Hom_R(c,c)=Hom_R(c,R). Apply the primary criterion to the appended Hilbert–Burch matrix. Since q^(-1)(c)=I for q:P→R, every adjugate membership over R is exactly the asserted ambient membership. | Both q cases, exact conductor ideals, Hessian orders, complete factor-preserving deformations, boundary maps and smooth-normalization equality case remain unchanged. The pre-existing later phrase “same R” now refers to an explicitly defined ring. |
| P4.47 | The two-generator ring condition gave f∈I². | For I=(g,h), write f=λg+μh and use M=[[h,λ],[-g,μ]]. The adjugate is [[μ,−λ],[g,h]], so the source criterion gives λ,μ∈I through the same quotient map. | The exact square completion, its normalization and irreducibility case, the full-power root, conic parametrization, critical values/Hessians and torus sphere transport are unchanged. |
| P4.49 | Two three-generator ideals used the adjugate condition and normalization multipliers. | Specify c=I/(f) for each ambient conductor ideal. In the second ideal form the Hom domain is c, and the original fractions n1 and n2 are still the multiplier generators. | Both Hilbert–Burch matrices, every colon identity, both equation forms, all multiplication relations, the rational-normal-cubic linear map, and both full-power deformation/transport constructions are unchanged. |

All three statements and all original equation labels remain unchanged. The added two-by-two display is the exact application matrix; it supplies no new general theorem or separate owner. Source guards match the current source, reference keys resolve, environments balance, and no blank paragraph occurs inside an added display. The protected E.5.2/E.5.3 blocks are outside all guards.

## Records

The package contains four exact old/new defect rows, three used-and-rechecked events, two source/metadata rows, bounded D18 outcomes and the three complete receiving owner fragments. The primary PDF and extracted text remain outside the checkpoint; the records contain only addresses, version, hash, loci and our own paraphrases. Root owns admission and integrated page reading. No whole-subsection or whole-paper closure is claimed.
''')
    print('READY: four bounded guards; four exact rows; three exposed reading events; two source rows; complete receiving proofs checked. No bibliography change.')
else:
    print('Prepared four bounded conductor guards, exact rows and three complete receiving proofs; statements and targets unchanged. Receiving read pending.')
