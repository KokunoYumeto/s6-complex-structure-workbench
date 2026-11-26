from S6_SERIES_PUBLISH_c3_edit import *

s = SOURCE.read_text()
def block(label, kind='proposition'):
    i = s.index('\\label{' + label + '}', s.index('\\begin{document}'))
    a = s.rfind('\\begin{' + kind + '}', 0, i)
    b = s.index('\\end{proof}', i) + len('\\end{proof}')
    return s[a:b]

smooth = block('night:P4.24')
resolved = block('night:P4R.8')
equality = block('night:P4.27')
general = block('night:P4.36')
last = block('lem:II:last-blowup-minimal-resolution', 'lemma')
assert 'tag-P250' not in s
set_unit_status('subsec:II:smooth-hopf-normalizations', 'D12', 'open',
    'The general proper-resolution Chern proof of P4.36 proves the full smooth, Euler-bound and equality conclusions on the identical normalization data. Consolidation and complete receiving read required.',
    'code/S6_SERIES_PUBLISH_c3_hopf_complete_owner.py')

foliation_proof = smooth[smooth.index('\\item The primary normal form'):smooth.index('\\item Put $B=\\nu^*T_Y$')]
foliation_proof = foliation_proof.replace('Every strict transform\nof a conductor component', 'Every strict transform\nof a compact curve of $T_0$')
foliation = r'''\begin{lemma}[Hopf foliations under point blowups]\hypertarget{tag-P250}{}\label{lem:II:hopf-foliation-blowups}
\StatementRecord{lem:II:hopf-foliation-blowups}{proved}{P250}{\cref{lem:II:hopf-curves}}
Let $T_0$ be a primary Hopf surface, and let $T\to T_0$ be a sequence of $k$ point blowups. There is a nonsingular holomorphic foliation on $T_0$ tangent to every compact curve. Its saturated pullback has tangent line bundle $L\subset T_T$, tangent to every strict transform of a compact curve and every exceptional curve, with exactly $k$ simple saddle zeros. There is an integral divisor $V$ supported on the exceptional locus such that, numerically,
\[
 c_1(L)=-K_T+V,\qquad K_T^2=-k,\qquad K_TV-V^2=0.
\]
At a blowup $\mu$ with exceptional curve $E$,
\[
 K'=\mu^*K+E,\qquad V'=\mu^*V+\varepsilon E,
 \qquad \varepsilon=0\text{ at a regular point},\quad
 \varepsilon=1\text{ at a saddle}.
\]
\end{lemma}
\begin{proof}
\begin{enumerate}[label=\arabic*.,leftmargin=*]
''' + foliation_proof + r'''\end{enumerate}
\end{proof}

'''

head = r'''\begin{proposition}[Hopf normalizations]\hypertarget{tag-02X9}{}\label{night:P4.36}\label{stmt:P4.36}
\StatementRecord{night:P4.36}{proved}{02X9}{\cref{lem:II:hopf-curves,lem:II:single-conductor-branch,lem:II:hopf-foliation-blowups,lem:II:last-blowup-minimal-resolution,lem:II:exceptional-intersection,night:P4R.6}}
\hypertarget{tag-02WW}{}\label{night:P4.24}\label{stmt:P4.24}
\StatementRecord{night:P4.24}{proved}{02WW}{}
\hypertarget{tag-02YH}{}\label{night:P4R.5}\label{stmt:P4R.5}
\StatementRecord{night:P4R.5}{proved}{02YH}{}
\hypertarget{tag-02YK}{}\label{night:P4R.8}\label{stmt:P4R.8}
\StatementRecord{night:P4R.8}{proved}{02YK}{}
\hypertarget{tag-02WZ}{}\label{night:P4.27}\label{stmt:P4.27}
\StatementRecord{night:P4.27}{proved}{02WZ}{}
Let $f:Y\to B$ be a proper surjective holomorphic map with connected fibres from a connected smooth compact complex threefold with $b_1(Y)=b_2(Y)=0$ to a smooth compact curve, with smooth general fibre a complex two-torus. Let $mS$ be a fibre with irreducible, reduced, singular support. Write $\nu:N\to S$ for its normalization and $\sigma:T\to N$ for the minimal resolution. Suppose that $T$ has a Hopf minimal model $T_0$. Then $\sigma$ and the minimal-model contraction $T\to T_0$ are isomorphisms: $N$ is a smooth minimal Hopf surface. The reduced conductor on $N$ and its reduced image $C=\operatorname{Sing}(S)_{\rm red}$ are disjoint unions of smooth elliptic curves. Each map between their components is a finite unramified covering, and
\[
 e(S_{\rm reg})=e(C)=e(S)=0.
\]
The number $k$ of point blowups from $T_0$ to $T$ and the number $v$ of rational components of the pole divisor in \cref{night:P4R.6} are zero. Thus $e(S_{\rm reg})=k-v$ and $e(S)=k-v+e(C)$ as well.
\end{proposition}
'''
proof = general[general.index('\\begin{proof}'):]
a = proof.index('\\item The primary Hopf normal form')
b = proof.index('\\item Put $B=\\rho^*TY$')
proof = proof[:a] + r'''\item Apply \cref{lem:II:hopf-foliation-blowups} to this primary Hopf surface and this sequence of point blowups. Its line bundle $L\subset T_T$ is tangent to the strict conductor and every exceptional curve. The effective integral divisor of \cref{night:P4R.6} has $K_T+D$ torsion. Apply \cref{lem:II:canonical-boundary-blowup} at each step to $D$ and its pushforward: a centre of multiplicity $\mu_x$ has exceptional coefficient $\mu_x-1$, so every centre lies on the invariant support. Write $\varepsilon=0$ at a regular point and $\varepsilon=1$ at a saddle. The lemma gives
\[
 c_1(L)=-K_T+V,\qquad V'=\mu^*V+\varepsilon E,
 \qquad K_T^2=-k,\qquad K_TV-V^2=0.
\]
Topologically trivial line-bundle factors from $T_0$ do not change these intersection calculations.

''' + proof[b:]
a = proof.index('\\item Return to the original, possibly secondary Hopf')
b = proof.index('\\end{enumerate}', a)
proof = proof[:a] + r'''\item Return to the original, possibly secondary Hopf surface. Every exceptional curve of $\pi:T\to T_0$ has an exceptional lift in the finite unramified cover, and the preceding argument contracts that lift to a point of $N$. Thus every $\pi$-exceptional curve is $\sigma$-exceptional. Apply \cref{lem:II:last-blowup-minimal-resolution} with its two maps equal to $\sigma:T\to N$ and $\pi:T\to T_0$, respectively. It gives $k=0$. Every compact curve on $T=T_0$ has square zero by \cref{lem:II:hopf-curves}. A nonempty exceptional configuration for $\sigma$ would have a negative definite intersection matrix by \cref{lem:II:exceptional-intersection}, applied to this resolution. Hence $\sigma$ is also an isomorphism, and $N=T=T_0$ is smooth minimal Hopf.

\item On the primary cover after $k=0$, the map $\rho:T\to Y$ is finite. The foliation line $L$ is a subbundle of $T_T$. Every divisorial zero of $d\rho|_L$ would lie on a compact curve tangent to $L$. The finite restriction to that curve is nonconstant and has nonzero derivative at its generic point. Thus $Z=0$. We already proved $z_0=0$, so $Q=Q^{**}$ is locally free. The exact sequence $0\to L\to B\to Q\to0$ splits locally; the map $d\rho|_L$ is therefore nowhere zero. Every conductor component on the primary Hopf cover is smooth elliptic and tangent to $L$, so its restriction to $Y$ is immersive everywhere. The finite unramified covering transfers this conclusion to the original normalization.

The reduced conductor on $N$ consists of disjoint smooth elliptic curves by \cref{lem:II:hopf-curves}. Apply \cref{lem:II:single-conductor-branch} to the finite normalization $\nu:N\to S\subset Y$: the inverse image of $C$ has one smooth branch at each of its points. The lemma identifies every pair of image branches. Each image branch is smooth by the preceding differential calculation, so $C$ is a disjoint union of smooth curves and every conductor map is finite unramified. Riemann--Hurwitz makes each image component elliptic. Since normalization is an isomorphism away from these curves,
\[
 e(S_{\rm reg})=e(N)-e((\nu^{-1}C)_{\rm red})=0,
 \qquad e(C)=0,\qquad e(S)=0.
\]
There are no rational conductor components by \cref{lem:II:hopf-curves}, giving $v=0$ and the asserted identities.

''' + proof[b:]
# Retain equation labels, replacing the three production-number tags by section numbering.
for tag, label in [('P4.36.1','eq:hopf-normalization-chern'),('P4.36.2','eq:hopf-normalization-increment'),('P4.36.3','eq:hopf-normalization-equality')]:
    marker = '\\tag{' + tag + '}'
    p = proof.index(marker)
    a = proof.rfind('\\[', 0, p)
    b = proof.index('\\]', p) + 2
    old = proof[a:b]
    new = old.replace('\\[', '\\begin{equation}', 1).replace('\\]', '\\end{equation}', 1).replace(marker, '')
    proof = proof[:a] + new + proof[b:]

receiving = foliation + last + '\n\n' + head + proof
newsource = s.replace(smooth, receiving, 1)
for heading, fragment in [
    ('\\subsection{Equality in the Hopf-resolution case}\n\n', equality),
    ('\\subsection{Eliminating all positive-Euler Hopf resolutions}\n\n', general)]:
    assert newsource.count(heading + fragment) == 1
    newsource = newsource.replace(heading + fragment, '', 1)
assert newsource.count(resolved) == 1
newsource = newsource.replace(resolved, '', 1)
# Remove only the late copy of the lemma; the earlier receiving copy remains.
late = newsource.index('\\subsection{Class VII canonical boundaries}')
assert newsource[late:].count(last) == 1
newsource = newsource[:late] + newsource[late:].replace(last, '', 1)
newsource = newsource.replace('\\subsection{Smooth Hopf normalizations}', '\\subsection{Hopf normalizations}', 1)
newsource = newsource.replace('\\subsection{Resolved ruled and Hopf normalizations}', '\\subsection{Resolved ruled normalizations}', 1)
removed_items = []
for lab in ['night:P4.24','night:P4R.8','night:P4.27']:
    pattern = r'^\\item \\SeriesRef\{' + re.escape(lab) + r'\}[^\n]*\n'
    matches = re.findall(pattern, newsource, re.M)
    assert len(matches) == 1, (lab, len(matches))
    removed_items.extend(matches)
    newsource = re.sub(pattern, '', newsource, count=1, flags=re.M)
pattern = r'^\\item \\SeriesRef\{night:P4\.36\}[^\n]*'
old_item = re.findall(pattern,newsource,re.M)
assert len(old_item) == 1
new_item = r'\item \SeriesRef{night:P4.36}\quad Smooth minimal Hopf normalization, unramified elliptic conductor and zero Euler number.'
newsource = re.sub(pattern, lambda _: new_item, newsource, count=1, flags=re.M)
preserve_identifiers(s, newsource)
for before,after in zip(identifiers(s),identifiers(newsource)):
    for name,count in before.items():
        assert after[name] == count, (name,count,after[name])
SOURCE.write_text(newsource, newline='\n')

edits = [
 ('OWNER',['D12','D14'],'night:P4R.5; night:P4.24; night:P4R.8; night:P4.27; night:P4.36', smooth+'\n\n'+resolved+'\n\n'+equality+'\n\n'+general,receiving,
  'The proper-map theorem applies on the identical data (f,Y,B,mS,nu:N→S,sigma:T→N,pi:T→T0). It gives sigma=pi=id, hence k=v=0, the earlier Euler inequalities and identities, both true sides of the old equality equivalence, and the full unramified conductor conclusion. The smooth case is its exact specialization N=T,sigma=id. Preserve all five permanent identities on one complete statement, the entire general Chern calculation, and the smooth proof’s final differential/conductor argument. The superseded complete graph and finite-map proofs are retained verbatim in this defects row.'),
 ('FOLIATION',['D12','D14'],'lem:II:hopf-foliation-blowups',foliation_proof,foliation,
  'Extract the complete primary-Hopf vector-field and blowup-chart calculation before its general application. The proof uses only the primary Hopf surface and point-blowup sequence; replacing conductor component by compact curve states that exact proved scope. All fields, weights, zero lengths, divisor recurrences and numerical identities remain.'),
 ('LAST-BLOWUP',['D12','D14'],'lem:II:last-blowup-minimal-resolution',last,last,
  'Move this complete unchanged lemma before the Hopf application. The exact map substitution is lemma pi=sigma:T→N and lemma sigma=pi:T→T0; every latter exceptional curve was proved contracted by the former.'),
 ('EQUATIONS',['D19'],'night:P4.36',general,head+proof,
  'Replace the three manual production equation tags P4.36.1–3 by ordinary section-numbered equation environments; every existing equation label and all mathematical expressions remain.'),
 ('NAVIGATION',['D12','D24'],'night:P4.36',''.join(removed_items)+old_item[0],new_item,
  'The five preserved statement identities name the same proved theorem. The further-results list contains its content once, and the resolved-normalization subsection now contains only the ruled results.')]
rows=[]
for key,types,stmt,old,new,reason in edits:
    for i,kind in enumerate(types,1):
        rows.append(dict(change_id=f'II-C3-HOPF-COMPLETE-{key}-{i:02}',type=kind,statement_id=stmt,
          old_location='Smooth and resolved Hopf normalization units',old_page='working source; final concordance pending',
          new_location='Hopf normalizations',new_page='integrated build pending',old_text=old,new_text=new,
          reason=reason,review_status='Complete old proofs read by root; complete receiving comparison follows. No independent proof credit.'))
print('Defect rows',append_rows(ROOT/'S6_SERIES_PUBLISH_defects_II.tsv',rows,'change_id'))
add_event('night:P4R.5; night:P4.24; night:P4R.8; night:P4.27; night:P4.36; lem:II:hopf-foliation-blowups; lem:II:last-blowup-minimal-resolution',
 'II-C3-HOPF-COMPLETE-TRANSFER','used and rechecked in this run',
 'Complete old smooth, proper-resolution, equality and general statements/proofs read against their exact domains. Consolidation preserves the complete general Chern argument and equation labels, extracts the full prior foliation construction as P250, moves unchanged P291 before use, and supplies the finite-map differential argument after the proper proof makes both contractions trivial. All old labels and tag targets retain exact multiplicity. Complete receiving read follows; no final unit/page gate or independent credit claimed.',
 'S6_SERIES_PUBLISH_II.tex: Hopf normalizations',source='code/S6_SERIES_PUBLISH_c3_hopf_complete_owner.py')

path=ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv'
fields, progress=read_tsv(path)
oldunits={'subsec:II:smooth-hopf-normalizations','night:P4.27','night:P4.36'}
selected=[x for x in progress if x['paper']=='II' and x['unit_id'] in oldunits]
assert len(selected)==78
progress=[x for x in progress if not(x['paper']=='II' and x['unit_id'] in oldunits)]
for criterion in ['D'+str(i).zfill(2) for i in range(1,26)]+['structure']:
    candidates=[x for x in selected if (x['defect_type'] or x['row_kind'])==criterion]
    assert len(candidates)==3
    status='done' if all(x['status']=='done' for x in candidates) else 'open'
    progress.append(dict(paper='II',unit_id='subsec:II:smooth-hopf-normalizations',unit_title='Hopf normalizations',
      row_kind='structure' if criterion=='structure' else 'defect',defect_type='' if criterion=='structure' else criterion,
      status=status,date_utc=now(),evidence='code/S6_SERIES_PUBLISH_c3_hopf_complete_owner.py',
      detail='Three current units consolidated on their exact common normalization data. The former R8 block was part of the still-open R7 unit. Migration supplies no movement credit; complete receiving read remains pending.'))
for row in progress:
    if row['paper']=='II' and row['unit_id']=='night:P4R.7':
        row['unit_title']='Resolved ruled normalizations'
write_tsv(path,fields,progress)
print('One complete Hopf theorem; all permanent labels and targets preserved; receiving read pending.')
