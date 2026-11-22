"""Prepare guarded A--C wording and the cited elliptic-surface application.

Only agent files are written.  The publication source is read for exact guards.
"""
from pathlib import Path
import datetime, hashlib, json, re

ROOT = Path('/workspace/scratch/653608133b22')
OUT = Path(__file__).parent
p = ROOT/'work/S6_SERIES_PUBLISH_I.tex'
s = p.read_text()
snapshot = json.loads((OUT/'S6_SERIES_PUBLISH_I_global_ABC_comparison_intake.json').read_text())
guards = []
def guard(ident, old, new, reason, scope):
    assert s.count(old)==1, (ident,s.count(old))
    guards.append({'id':ident,'old':old,'new':new,'expected_count':1,
                   'reason':reason,'scope':scope})

guard('IA-GLOBAL-01',
      'For torsion $P$ of order $n$ and $m\\equiv\\pm1\\pmod n$ this gives',
      'For torsion $P$ of order $n$ and $m\\ge2$ with\n$m\\equiv\\pm1\\pmod n$, this gives',
      'Repeat the already stated m>=2 hypothesis in the torsion specialization; C4.2 states it explicitly.',
      'series:I:A; inherited hypothesis made explicit, no mathematical change')
guard('IA-GLOBAL-02',
      'These are exact height identities; no transcendence conclusion\nat the stated non-torsion points is included.\n',
      '',
      'The exact identities already state the theorem; the unresolved arithmetic questions have their own final part.',
      'series:I:A; remove status prose from the theorem, retain every mathematical assertion')
guard('IA-GLOBAL-03',
      'from the square root point and the controlled local theta\nexpansion give $\\max N=\\sqrt2$.',
      'from the square elliptic point and the controlled local theta\nexpansion give $\\max N=\\sqrt2$.',
      'The local point is the square elliptic curve tau=i; the old phrase could suggest a choice of square root.',
      'outline A step4; wording only')
guard('IA-GLOBAL-04',
      'Its bounded complement is the strict\nsuperlevel set; these sets form nested discs.',
      'Its bounded complementary component is the strict\nsuperlevel set; these sets form nested discs.',
      'Name the bounded component of the complement of the Jordan curve.',
      'series:I:A; wording only')
guard('IA-GLOBAL-05',
      'In the real parabolic,\na fundamental set is given by the classical modular region for',
      'In the real vector stabilizer $P_d(\\mathbb R)$,\na fundamental set for $\\Gamma\\backslash P_d(\\mathbb R)$\nis given by the classical modular region for',
      'The proved fundamental set is for the vector stabilizer, as explicitly stated in I:monodromy-fundamental-set; the real line stabilizer also has a scaling coordinate.',
      'series:I:C; exact quotient scope')
guard('IA-GLOBAL-06',
      'These countable unions classify all quotient maps, including\nthose that mix the two displayed coordinates.',
      r'''For each nonzero form $E$ in this integral kernel with zero
Pfaffian, put
$K_{\mathbb R}=\ker(E:\Lambda_{\mathbb R}\to\Lambda_{\mathbb R}^*)$
and $K=K_{\mathbb R}\cap\Lambda$. The maps
\[
 (\Pi_cK_{\mathbb R})/\Pi_cK\ \hookrightarrow F_t
 \longrightarrow\mathbb C^2/(\Pi_cK_{\mathbb R}+\Pi_c\Lambda)
\]
give every connected elliptic kernel and its quotient, including
kernels that mix the two displayed coordinates.''',
      'State the actual morphisms proved in D1.6: the unions specify loci; the saturated null lattices specify connected kernels and their quotient maps.',
      'series:I:C; replace an imprecise summary by the existing exact kernel/quotient construction')

old11 = snapshot['blocks']['fam:src:B.1.1']['text']
old13 = snapshot['blocks']['fam:src:B.1.3']['text']
assert s.count(old11)==s.count(old13)==1
statement11 = old11[:old11.index(r'\end{proposition}')+len(r'\end{proposition}')]
statement11 = statement11.replace('[The period quotient and the lifted line bundle]',
                                  '[The period quotient and its marked elliptic point]')
statement11 = statement11.replace(
    r'\StatementRecord{fam:src:B.1.1}{proved}{01Q7}{\SeriesRef{fam:src:A.3.1}}',
    r'''\hypertarget{tag-01Q9}{}\label{fam:src:B.1.3}\label{fam:st:B.1.3}
\StatementRecord{fam:src:B.1.1}{proved}{01Q7}{\cref{I:weierstrass-comparison}; \cite[Remark~3.12, p.~19]{AC2026}}
\StatementRecord{fam:src:B.1.3}{proved}{01Q9}{\cref{I:weierstrass-comparison}; \cite[Remark~3.12, p.~19]{AC2026}}''')
statement11 = statement11.replace(
    'The section $P=[\\mu]$ is a generator of the Mordell--Weil group of the stated pointed Weierstrass surface.',
    r'''The section $P=[\mu]$ is a generator of the Mordell--Weil group
of the stated pointed Weierstrass surface, and
\[
 \wp_\tau(\mu)=0.
\]
Under the pointed map in the proof it is one of
$P_*=(0,\sqrt2t^2(t-1))$ and $-P_*$.''')
proof12 = old11[old11.index(r'\begin{proof}'):old11.index(r'\item We first verify')]
proof12 = proof12.replace(
    "therefore this isomorphism descends over $B^\\circ$.",
    "therefore this isomorphism descends over $B^\\circ$.\n"
    "It pulls $dx/(2y)$ back to $f_{\\rm sc}^{-1}d\\xi$.")
last = r'''\item Write $C=t^3(t-1)$ and $D=t^4(t-1)^2$.
In \cite[Remark~3.12, p.~19]{AC2026}, the surface
\[
 y_0^2=4x_0^3-3Cx_0-D
\]
has Mordell--Weil generator $P_0=(0,it^2(t-1))$, whose
normalized Abel--Jacobi coordinate is $-\mu$.
Its Weierstrass scale $r$ satisfies
\[
 r^4=3C/g_2(\tau),\qquad r^6=D/g_3(\tau),\qquad
 r^2=\frac{Dg_2(\tau)}{3Cg_3(\tau)}.
\]
Thus $x_0(P_0)=r^2\wp_\tau(-\mu)=0$.
Evenness of $\wp$ gives the asserted zero for the original
affine logarithm. Changing the sign of $r$ composes this
uniformization with $\xi\mapsto-\xi$, and leaves this zero
identity unchanged.
The exact pointed map of \cref{I:weierstrass-comparison},
\[
 (x_0,y_0)\longmapsto(-2x_0,i\sqrt2y_0),
\]
sends $P_0$ to $-P_*$ and $-P_0$ to $P_*$.
Both visible sections therefore generate the Mordell--Weil group
of the geometric equation. The preceding $f_{\rm sc}$ map sends
$[\mu]$ to one of these two sections, proving the generator claim.
The Shioda self-pairing is
$\langle P,P\rangle=2-4/3-1/2=1/6$
\cite[proof of Lemma~2.1, pp.~3--4]{Engel2026}; the two sign choices
have the same pairing. The chosen sign in our family is fixed by
the cusp calculation in \cref{fam:src:B.1.4}.

\item The nodal comparison needed for that sign is explicit.
Put $v=1/t$, $X=v^2x$, $Y=v^3y$; the geometric equation becomes
$Y^2=X^3-3(1-v)X+2(1-v)^2$.
At $v=0$, the chosen scale gives
\[
 X=1+\frac{12U}{(U-1)^2},\qquad
 Y=\frac{12\sqrt3\,U(U+1)}{(U-1)^3},\qquad
 U=e^{2\pi i\xi}.
\]
On the smooth locus away from $O$ its inverse is
$U=(Y/(X-1)+\sqrt3)/(Y/(X-1)-\sqrt3)$;
at $O$ a local parameter is $X/Y$.
The normally convergent multiplicative expansion of $\wp$
gives the corresponding holomorphic map for small $v$.
\end{enumerate}
\end{proof}'''
new11 = statement11+'\n\n'+proof12+last
guard('IA-ELLIPTIC-01',old11,new11,
      'One statement/proof now contains the quotient map, scale, known generator and zero identification. Exact source sign and all original labels/tags are retained; old logarithm reproof is archived.',
      'fam:src:B.1.1 and fam:src:B.1.3; source/application consolidation')
guard('IA-ELLIPTIC-02',old13,'',
      'The zero/generator statement and all labels/tags have moved into B1.1. Its full original blow-up/intersection proof is archived; cited AC and Engel results supply its known input.',
      'fam:src:B.1.3; one proof after merger')

preview=s
for row in guards:
    assert preview.count(row['old'])==1,row['id']
    preview=preview.replace(row['old'],row['new'],1)
old_labels=re.findall(r'\\label\{([^}]+)\}',s)
new_labels=re.findall(r'\\label\{([^}]+)\}',preview)
assert sorted(old_labels)==sorted(new_labels)
old_tags=re.findall(r'\\hypertarget\{(tag-[^}]+)\}',s)
new_tags=re.findall(r'\\hypertarget\{(tag-[^}]+)\}',preview)
assert sorted(old_tags)==sorted(new_tags)
data={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
      'source':str(p),'source_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
      'guards':guards,'labels_and_tags_preserved':True,
      'main_source_written':False}
(OUT/'S6_SERIES_PUBLISH_I_global_ABC_guards.json').write_text(json.dumps(data,indent=2)+'\n')
(OUT/'S6_SERIES_PUBLISH_I_global_ABC_preview.tex').write_text(preview)

original=ROOT/'source/S6_SERIES_GRIND_I.tex';o=original.read_text()
archives=[]
for label,old,new in [('fam:src:B.1.1',old11,new11),('fam:src:B.1.3',old13,'merged into fam:src:B.1.1')]:
    i=o.index(r'\label{'+label+'}');a=o.rfind(r'\begin{proposition}',0,i)
    b=o.index(r'\end{proof}',i)+len(r'\end{proof}')
    archives.append({'statement_id':label,'original_source':str(original),
                     'original_source_sha256':hashlib.sha256(original.read_bytes()).hexdigest(),
                     'original_line_start':o.count('\n',0,a)+1,
                     'original_line_end':o.count('\n',0,b)+1,
                     'original_full_statement_and_proof':o[a:b],
                     'premerge_current_locator':snapshot['blocks'][label]['line_start'],
                     'premerge_current_source_sha256':snapshot['source_sha256'],
                     'premerge_current_full_statement_and_proof':old,
                     'new_locator':'fam:src:B.1.1 (= fam:src:B.1.3), shared four-step proof',
                     'proposed_replacement':new})
(OUT/'S6_SERIES_PUBLISH_I_elliptic_duplicate_proofs.json').write_text(json.dumps(archives,indent=2)+'\n')
print(json.dumps({'guards':len(guards),'source_sha256':data['source_sha256'],
                  'labels_and_tags_preserved':True,'main_source_written':False},indent=2))
