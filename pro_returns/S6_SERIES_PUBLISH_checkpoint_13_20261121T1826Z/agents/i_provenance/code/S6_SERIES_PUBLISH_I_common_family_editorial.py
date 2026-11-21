from pathlib import Path
import re, json, hashlib, datetime, difflib

ROOT = Path('/workspace/scratch/653608133b22')
OUT = ROOT/'work/agents/i_provenance'
SOURCE = ROOT/'work/S6_SERIES_PUBLISH_I.tex'
src = SOURCE.read_text()
sha = hashlib.sha256(src.encode()).hexdigest()
changes, records = [], []

def block(label):
    at = src.index('\\label{'+label+'}', src.index('\\clearpage\n\\section{The marked family'))
    starts = list(re.finditer(r'\\begin\{(?:proposition|theorem|corollary|lemma|remark|definition|cited)\}', src[:at]))
    start = starts[-1].start()
    end = src.index('\\end{proof}', at)+len('\\end{proof}')
    return src[start:end]

def replace(text, old, new, count=1):
    assert text.count(old)==count, (old[:130], text.count(old), count)
    return text.replace(old,new)

def save(label, old, new, why):
    assert src.count(old)==1, (label,src.count(old))
    assert old != new, label
    name=re.sub(r'[^A-Za-z0-9]+','_',label).strip('_')
    oldp=OUT/f'S6_SERIES_PUBLISH_I_common_{name}_old.tex'
    newp=OUT/f'S6_SERIES_PUBLISH_I_common_{name}_new.tex'
    oldp.write_text(old); newp.write_text(new)
    old_labels=re.findall(r'\\(?:label|hypertarget)\{([^}]+)\}',old)
    new_labels=re.findall(r'\\(?:label|hypertarget)\{([^}]+)\}',new)
    missing=[x for x in old_labels if x not in new_labels]
    assert not missing,(label,missing)
    cid='I-common-'+name
    changes.append(dict(id=cid,old=old,new=new,expected_count=1,reason=why))
    records.append(dict(statement_id=label,old_path=str(oldp),new_path=str(newp),old_sha256=hashlib.sha256(old.encode()).hexdigest(),new_sha256=hashlib.sha256(new.encode()).hexdigest(),reason=why,old_labels=old_labels,new_labels=new_labels))

titles={
 'fam:src:B.1.1':'The period quotient and the lifted line bundle',
 'fam:src:B.1.2':'The compactness radius',
 'fam:src:B.1.3':'The zero of the Weierstrass function',
 'fam:src:B.1.4':'The reference linearization',
 'fam:src:A.1.2':'Normalized root covers and the finite fibres',
 'fam:src:A.4.1':'Albanese curves and parameter recovery',
 'fam:src:B.2.1':'Classification with arbitrary affine and cusp data',
 'fam:src:B.2.2':'The two classes over a fixed linearization parameter',
 'fam:src:B.3.1':'Classification for higher multiplicities',
}

for label in ['fam:src:B.1.1','fam:src:B.1.2','fam:src:B.1.3','fam:src:B.1.4','fam:src:A.1.2','fam:src:A.4.1','fam:src:B.2.1','fam:src:B.2.2']:
    old=block(label);new=replace(old,'\\begin{proposition}','\\begin{proposition}['+titles[label]+']')
    if label=='fam:src:B.1.1':
        new=replace(new,"Engel's generator, in Definition 2.3 of the attached paper, is its inverse", "The generator in \\cite[Definition~2.3, p.~5]{Engel2026} is its inverse")
        new=replace(new,"\\item For clarity the elliptic surface in this dictionary is the displayed cubic, rather than only a curve with the same $j$-value. Let $f_{\\rm sc}$ be the branch satisfying", "\\item The pointed map to the elliptic surface is determined by the branch $f_{\\rm sc}$ satisfying")
    elif label=='fam:src:B.1.2':
        new=replace(new,"this boundary issue is treated in Part C", "the maximizing locus is determined in \\cref{ari:C.8.15}")
    elif label=='fam:src:B.1.3':
        new=replace(new,' This assertion does not use a numerical evaluation of $\\mu$ or of $\\beta$.','')
        new=replace(new,'These identities follow by substitution in the displayed polynomial, not by discarding its higher terms.','Substitution in the displayed polynomial proves these identities with all higher terms retained.')
        new=replace(new,' already proved $P_*=nP$ for an integer $n\\ne0$, without identifying the visible section.',' proves $P_*=nP$ for an integer $n\\ne0$.')
    elif label=='fam:src:B.1.4':
        new=replace(new,'proved without numerical input in \\ref{fam:src:B.1.3}','proved in \\ref{fam:src:B.1.3}')
        new=new.replace('\\cite[Lemma 2.1]{Engel2026}','\\cite[Lemma~2.1, pp.~3--4]{Engel2026}')
        new=new.replace('\\cite[Corollary 2.2]{Engel2026}','\\cite[Corollary~2.2, p.~4]{Engel2026}')
        new=replace(new,', which we have read together with its proof, identifies', ' identifies')
        new=replace(new,'; no scalar value is invariant under that declared choice.','.')
        new=replace(new,'With the cusp branch fixed in Part C and',r'With the cusp branch $e^{2\pi i\mu}\to-(5+2\sqrt6)$ and')
        new=replace(new,'With the cusp branch in Part C and',r'With this cusp branch and')
    elif label=='fam:src:A.1.2':
        new=replace(new,'finite etale covers',r"finite \'etale covers")
    elif label=='fam:src:A.4.1':
        new=replace(new,', independently of the centralizer calculation.','.')
        new=replace(new,'In particular the Albanese computation includes the kernel of the product isogeny and the affine quotient, rather than just its fixed eigenspace.','The two displayed lattices include both the product-isogeny kernels and the affine quotient translations.')
        new=replace(new,'The independently certified interval in \\texttt{cd\\_special\\_intervals.py} gives $-0.2<\\operatorname{Im}d_*<-0.1$; in particular it is nonzero.',r'''The definitions $\kappa_1^{\rm part}=\beta^{\rm part}(z_1)+2\mu_1$ and
$\kappa_2^{\rm part}=\beta^{\rm part}(z_2)+3\mu_2$, together with
\cref{ari:C.1.2}, give
\[
 \operatorname{Im}d_*=
 -\frac{3}{2\pi}\log48+\frac3\pi\log6
 =-\frac{3}{2\pi}\log\frac43<0.
\]''')
        new=replace(new,'This proves the generic necessity with its actual exceptional set;', 'This proves the necessity outside the specified exceptional set;')
    elif label=='fam:src:B.2.1':
        new=new.replace('\\cite[Section 6.4]{AC2026}','\\cite[Section~6.4, pp.~39--40]{AC2026}')
        new=replace(new,'Thus the norm condition is sufficient for a local isomorphism, not only for conjugacy on the central real torus.','Thus the norm condition supplies a biholomorphism on the complete root disc.')
        new=replace(new,'This proof supplies the necessary extension test; no assertion about arbitrary punctured translations is used.','Thus every extending translation has the stated integral winding and holomorphic unit factor.')
        new=replace(new,'\\item We retain the actual collar convention. The map', '\\item The map')
        new=replace(new,'This also proves that the extra collar data have been accounted for, rather than omitted from the statement.','The construction in the preceding steps absorbs the analytic part and the second winding of the collar.')
    elif label=='fam:src:B.2.2':
        a=new.index('\\item We spell out the integral comparison')
        b=new.index('They also agree with the complex periods:',a)
        new=new[:a]+r'''\item Put $P_{\rm E}=P_{\rm mark}$, the integral isomorphism of
\cref{inv:B1.0}, and retain Engel's $Cf_4=e_1+e_4$.
Besides the intertwining identities in that proposition, multiplication gives
$P_{\rm E}d=\delta_0$, $\psi P_{\rm E}=-\gamma$,
$P_{\rm E}\varepsilon=-e_4$ and
$P_{\rm E}\varepsilon'=\delta_0-Cf_4$.
'''+new[b:]
        new=replace(new,'\\item For the sign assertion, inverting the concrete clockwise affine generator changes its invariant translation $\\Pi_cv_j/m_j$ to $-\\Pi_cv_j/m_j$. Thus our dictionary is', '\\item The inverse-generator convention of \\cref{inv:B1.0} gives')
    save(label,old,new,'Numbered mathematical title; remove process wording and filenames while preserving all maps and proof steps. Reuse the canonical integral marking in B2.2; archive its redundant printed matrix and computational cross-check in the comparison record.')

label='fam:src:A.4.3';old=block(label)
proof=old.split('\\begin{proof}',1)[1].rsplit('\\end{proof}',1)[0].strip()
proof=replace(proof,'This is exactly the implication used in the cited Proposition 4.7, whose statement and proof we have read.','This is the period argument of \\cite[Proposition~4.7, pp.~14--15]{ViaclovskyLog2026}.')
proof=replace(proof,"\\item Yang's cited lemmas use", "\\item The comparison in \\cite[Lemmas~6.6--6.7 and~6.9, pp.~31--32; Remark~6.8, p.~32; Proposition~6.15, pp.~37--38]{Yang2026} uses")
proof=replace(proof,'The common proof operations transfer through these explicitly stated matrix substitutions; no conclusion about one family is inferred merely from the label of the other.','These matrix substitutions identify the commuting maps, finite norm equations and collar corrections with the ones just displayed.')
proof=replace(proof,'His nonzero absolute Kodaira--Spencer conclusion is obtained in the present setting by the explicit computation and intrinsic-pencil transfer above.','The nonzero absolute Kodaira--Spencer conclusion in \\cite[Theorem~6.18, p.~39]{Yang2026} is obtained for the present family by the explicit computation and intrinsic-pencil transfer in \\cref{fam:src:A.4.2}.')
head=old[:old.index('\n\nThe non-isotriviality argument')]
head=replace(head,'\\begin{proposition}','\\begin{remark}[Period variation and norm comparisons]')
new=head+'\n\n'+proof+'\n\\end{remark}'
save(label,old,new,'Convert the source-comparison proposition to a numbered mathematical remark. Preserve its full countability argument, z↦z² derivative example, exact first-column/norm substitutions, and references to the unified tangent result; remove the repeated introductory claims and source-reading narration.')

# Main A5.1 only; its deferred proof belongs to the parent.
label='fam:src:A.5.1';at=src.index('\\label{'+label+'}',src.index('\\clearpage\n\\section{The marked family'))
start=src.rfind('\\subsection{The assembled theorem}',0,at)
end=src.index('\\section{Discrete data and the geometric parameter}',at)
old=src[start:end]
new=replace(old,'\\subsection{The assembled theorem}','\\subsection{The standard isomorphism classes}')
new=replace(new,'\\begin{theorem}','\\begin{theorem}[Classification of the standard family]')
beg=new.index('The standard classification is ')
scope=new.index('\\paragraph{Scope and a precise changed-input test.}')
new=new[:beg]+new[scope:]
scope=new.index('\\paragraph{Scope and a precise changed-input test.}')
new=new[:scope]+r'''\begin{remark}[A rank-one nodal model]
\hypertarget{tag-IP09}{}\label{I:remark:rank-one-nodal-model}
The family of \cref{fam:src:A.5.1,fam:src:A.5.2} uses the original period
system with multiplicities $(3,4)$. Its arbitrary affine and cusp data are
classified in \cref{fam:section:B.2}, and its higher multiplicities in
\cref{fam:section:B.3}.
For the elliptic surface $y^2=x^3+tx+1$ of
\cite[Section~2, pp.~3--5; Proposition~3.1, pp.~6--7;
Proposition~6.1, pp.~17--18]{ViaclovskyTwo2026}, fix the nodal value
$p_1$ with $4p_1^3+27=0$. In that paper's equation~(3.1), put
$\gamma_0=\gamma(0)$, $\beta_0=\beta(0)$ and
$c_0=\lambda\delta(0)$, with $0<|c_0|<1$.
The normalization of this rank-one filling is
\[
 \begin{gathered}
 E'=\mathbb C^*/\langle c_0\rangle,\qquad
 R=\mathbb P_{E'}(\mathcal O_{E'}\oplus L),\\
 R=(\mathbb P^1\times\mathbb C^*)/
       \langle(z,v)\mapsto(\gamma_0z,c_0v)\rangle,
 \end{gathered}
\]
and its boundary sections are identified by $v\mapsto\beta_0v$.
The invariant nodal volume form in equation~(6.2) of that paper
trivializes the ambient canonical line near this fibre. The branch-normal
map therefore has quotient $\nu_*K_R$ by the local coefficient map in
\eqref{fam:eq:ab-normal-quotient}.
For the ruling $\pi:R\to E'$, one has
$\pi_*\mathcal O_R=\mathcal O_{E'}$ and
$R^1\pi_*\mathcal O_R=0$; Leray and Serre duality give
$h^\bullet(K_R)=(0,1,1)$.
The corresponding summand of the connecting homomorphism is
\[
 H^1(R,K_R)=\mathbb C\longrightarrow H^2(T_X(-\log D)),
\]
where $D$ is the union of that model's three reduced nodal fibres.
Its defining boundary-translation \v Cech cocycle uses the full
holomorphic units in equation~(3.1), their central values
$(\gamma_0,c_0,\beta_0)$ and the vertical frames. The integral
comparison equations use that model's four monodromy matrices and
their collar defects. These are the explicit local and global inputs
for this model; the displayed cohomology calculation evaluates the
source of the connecting map.
\end{remark}

'''
save(label,old,new,'Title the standard classification, remove two obsolete re-derivation navigation paragraphs, and number the rank-one comparison as IP09. Preserve its ruled-surface map, canonical quotient, cohomology, connecting-map source/target and full-unit/collar inputs. Supply the exact central-multiplier dictionary from the opened primary equation; make no claim that the connecting map has been evaluated. Leave the parent-owned deferred proof unchanged.')

label='fam:src:B.2.3';old=block(label)
new=replace(old,'\\begin{proposition}[counterexample, with corrected family]','\\begin{proposition}[The double cover of the linearization parameter]')
a=new.index('The assertion in \\cite[Remark 8.1]');b=new.index('\\end{proposition}',a)
new=new[:a]+r'''Fix the sphere logarithmic data in \cite[Remark~8.1, p.~22]{Engel2026}.
The resulting family has a proper holomorphic realization on every
simply connected admissible $u$-open set and globally over the punctured
$w$-disc of \cref{fam:src:A.3.1}, with $u=w^2$.
The order-two class of $d$ in $\Lambda^{A_2}/N_2\Lambda$ obstructs
descent of this family to the punctured $u$-disc.
'''+new[b:]
new=replace(new,'This verifies the obstruction independently of a choice of isomorphism lift.','This Laurent coefficient gives a second expression of the same descent obstruction.')
new=replace(new,'The untwisted middle quotient itself has the integer shear identification, so this refutation concerns the fixed sphere logarithmic data in the stated remark.','The integer shear identifies the untwisted middle quotients; the nonzero order-two class is carried by the finite root quotient with the fixed sphere logarithmic data.')
save(label,old,new,'Retain both exact obstruction proofs and the local/global family scope; state the double-cover obstruction positively and archive the historical counterexample wording. No mathematical conclusion or source attribution removed.')

# Consolidate the two higher-multiplicity proofs, preserving unique local maps.
b3old=block('fam:src:B.3.1');e12old=block('push:src:E.1.2')
def items(b):
    p=b.split('\\begin{proof}',1)[1].split('\\begin{enumerate}[label=\\arabic*.,leftmargin=*]',1)[1].rsplit('\\end{enumerate}',1)[0]
    return [s.strip() for s in p.split('\\item ')[1:]]
bi,ei=items(b3old),items(e12old);assert len(bi)==5 and len(ei)==5
bi[0]=replace(bi[0],"This is the full reduction in the read Proposition 4.7 of Viaclovsky's paper, written here with its exact maps.","This is the base-preservation argument of \\cite[Proposition~4.7, pp.~14--15]{ViaclovskyLog2026}, with the displayed maps.")
bi[0]=replace(bi[0],'We first recover the base for these sphere members without using the degree-two canonical pencil.','The base is intrinsic for these sphere members.')
bi[0]=replace(bi[0],'Kahler',r'K\"ahler')
bi[1]=replace(bi[1],'The centralizer and first-column comparison remain unchanged.',r'''On ordinary fibres the affine lift has simultaneous rational centralizer
$\mathbb Q I+\mathbb Q E$, as in \cref{fam:src:A.2.1}.
Comparison of the constant period columns gives fibre-linear part $aI$,
integer shift $n$ and lattice map $aS_n^{-1}$, where $S_n=I+nE$.
Functorial normalization of the root base change makes the lift commute
with the prescribed deck generator; summing its defect gives the norm
equation. The explicit base norms are
\[
 N_3v=3\gamma(v)\varepsilon+(2v_u+v_w+3v_\delta)d,\qquad
 N_4v=4\gamma(v)\varepsilon'+(2v_u+2v_w+4v_\delta)d,
\]
where $N_3=N_1$ and $N_4=N_2$ in the notation above.
At the cusp the character ratio of any extending map is $t_c^q$ times
a holomorphic unit, by \cref{fam:src:B.2.1}; its winding vanishes in
the quotient by the toric directions. The middle cocycle then forces
$p'=ap$.''')
bi[2]=replace(bi[2],'For completeness the integer $p$ records','The integer $p$ records')
local=ei[0][ei[0].index("Suppose $p'"):]
def rename_local(t):
    t=t.replace('{m}', '{m_1}').replace('{n}', '{m_2}')
    t=t.replace('modulo $m,n$','modulo $m_1,m_2$')
    t=t.replace('N_m','N_{m_1}').replace('N_n','N_{m_2}')
    t=t.replace('a(t_c)','u(t_c)').replace('a(0)','u(0)')
    t=t.replace(' A_j=\\Pi_cb_j+', ' \\mathcal A_j=\\Pi_cb_j+')
    return t
local=rename_local(local)
local=r'''For the local sufficiency maps put $\alpha=a$, $h=n$,
$S_h=I+hE$ and $d_j=S_hw'_j-\alpha w_j$.
'''+local
cusp=rename_local(ei[1])
sheaf=rename_local(ei[2])
sheaf=replace(sheaf,'We justify the global analytic correction.  Differences of allowed','Differences of allowed')
sheaf=replace(sheaf,'Thus the coarse difference sheaf is literally the same\nsheaf $\\mathcal V_B$ as for multiplicities $(3,4)$, not an assumed\nanalogue.','These invariant-coefficient maps identify the coarse difference sheaf\nwith $\\mathcal V_B$ for multiplicities $(3,4)$.')
bi[4]=bi[4][:bi[4].index(' The program\n')]+'.' if not bi[4][:bi[4].index(' The program\n')].endswith('.') else bi[4][:bi[4].index(' The program\n')]
newproof='\\begin{proof}\n\\begin{enumerate}[label=\\arabic*.,leftmargin=*]\n'+''.join('\\item '+x+'\n\n' for x in [bi[0],bi[1],bi[2],local,cusp,sheaf,bi[4]])+'\\end{enumerate}\n\\end{proof}'
b3new=b3old[:b3old.index('\\begin{proof}')]+newproof
b3new=replace(b3new,'\\begin{proposition}','\\begin{proposition}[Classification for higher multiplicities]')
save('fam:src:B.3.1',b3old,b3new,'Canonical higher-multiplicity proof. Move unique explicit defects, rational local vectors, cusp maps and invariant-coefficient/cohomology argument from pushE1.2; retain the original intrinsic-base, norm, primitive p and Chinese-remainder steps. Archive five-pair adjacent_exact diagnostic. The local proof explicitly sets alpha=a and h=n; source covering degrees m,n are written m1,m2. The displayed definition names the local translation mathcal A_j, and the cusp unit is u(t_c), avoiding collisions with the fixed matrix A_j and sign a. Their formulas are otherwise unchanged.')
e12new=e12old[:e12old.index('\\begin{proof}')]+r'''\begin{proof}
Apply \cref{fam:src:B.3.1} through the integral isomorphism
$P_V$ of \cref{push:src:E.1.1}. Its affine and cusp coordinates are
\[
 r_1=N_0,\quad s_1=-\rho_0,\qquad
 r_2=N_1,\quad s_2=-(\rho_1+N_1),\qquad p=-b.
\]
Thus $p'=\alpha p$ is $b'=\alpha b$, and the first norm congruence is
$hN'_0\equiv\rho'_0-\alpha\rho_0\pmod{k}$.
The second becomes
\[
 hN'_1\equiv\rho'_1-\alpha\rho_1+N'_1-\alpha N_1\pmod{2l}.
\]
The relation $b'=\alpha b$, reduced modulo $4l$, gives
$N'_1\equiv\alpha N_1\pmod{4l}$, since $\gcd(3k,4l)=1$.
It removes the last two terms and yields the stated congruence.
The base-preservation assertion, identification subgroup and number of
classes transfer through this same integral map. It preserves
$u=e^{-2\pi ic}$, so a positive $u$-circuit is still $c\mapsto c-1$
and induces the single cycle proved in \cref{fam:src:B.3.1}.
\end{proof}'''
e12new=replace(e12new,'[classification in Viaclovsky\'s coordinates]',"[Classification in Viaclovsky's coordinates]")
save('push:src:E.1.2',e12old,e12new,'Replace the second full classification proof by the exact invertible coordinate substitution from the canonical result. The explicit local constructions are moved intact, with declared variable renamings, to famB3.1. All statement assertions, labels and tags remain.')

label='push:src:E.1.1';old=block(label);new=replace(old,'[the integral dictionary]','[The integral dictionary]')
new=new.replace('\\cite[Section 2, equations (2.1), (2.2), (2.7), (2.11)--(2.12)]{ViaclovskyLog2026}', '\\cite[Section~2, equations~(2.1)--(2.2), p.~3, and (2.7), (2.11)--(2.12), p.~4]{ViaclovskyLog2026}')
new=replace(new,'The homomorphism from the marking of the question to this marking is','The homomorphism from the marking of \\cref{def:common-conventions} to this marking is')
new=replace(new,'although its chosen lift fixes the collar bookkeeping.','while its chosen lift fixes the integral collar defect.')
new=replace(new,'Replacing $v_i$ by an integral\nmultiple $m_i$ times a period does not change that torsion\npoint,',r'''Replacing $v_i$ by $v_i+m_i\lambda$, $\lambda\in\Lambda$,
leaves the class $[v_i/m_i]$ unchanged,''')
new=replace(new,'In Engel\'s marking the four columns of the change to Viaclovsky\'s\nbasis are',"Use $P_E=P_{\\rm mark}$ from \\cref{inv:B1.0}. In Engel's marking,\nthe four columns of the change to Viaclovsky's basis are")
new=replace(new,'including the otherwise easily missed $N_1$ in the\nsecond coefficient.','including the term $N_1$ in the second coefficient.')
new=replace(new,'These matrix identities are independently executed in\n\\texttt{code/e\\_push\\_exact.py}, with their output attached.','')
save(label,old,new,'Title and source-locator cleanup; keep P_V, Q_E, all invariant-vector identities, affine signs and p=-b. Define P_E through the earlier canonical marking and archive diagnostic program narration.')

label='push:src:E.1.3';old=block(label);new=replace(old,'[holomorphic dependence of the comparisons]','[Holomorphic dependence of the comparisons]')
new=replace(new,'In \\ref{push:src:E.1.2} the rational vectors $b_j$, integral defects $\\ell_j$,\nand toric exponents are independent of $c$.','The rational vectors $b_j$, integral defects $\\ell_j$ and toric\nexponents in the proof of \\cref{fam:src:B.3.1}, transported through\n\\cref{push:src:E.1.1}, are independent of $c$.')
new=replace(new,'The full automorphism\ncalculation re-derived in the credited appendix at \\ref{fam:src:B.4.1} identifies that group with $\\mathbb C^*$;', 'The automorphism calculation in \\cref{fam:src:B.4.1} identifies\nthat group with $\\mathbb C^*$;')
save(label,old,new,'Retain the full holomorphic-parameter sheaf argument, exact W=(-1)^s2w map and monodromy conjugacy proof; update the supplying proof after consolidation and remove re-derivation narration.')

# Number the three orphan spans without changing their mathematical coordinates.
old=r'''We distinguish Viaclovsky's indices $0,1$ from the indices $1,2$ of
the question.  Put $m=3k$, $n=4l$, and assume $\gcd(m,n)=1$.
The lattice coordinates in this subsection are integral homology
coordinates, and matrices act on columns.'''
new=r'''\begin{definition}[Higher multiplicities and source coordinates]
\hypertarget{tag-IP10}{}\label{I:def:higher-multiplicity-coordinates}
Put $m=3k$, $n=4l$ with $\gcd(m,n)=1$.
Viaclovsky's indices $(0,1)$ correspond to the finite indices $(1,2)$
of \cref{def:common-conventions}. Lattice coordinates are integral
homology coordinates, and matrices act on columns.
\end{definition}'''
save('I:def:higher-multiplicity-coordinates',old,new,'Number the pre-dictionary conventions as IP10, with the explicit index correspondence.')
a=src.index('For a general cusp collar $\\sigma$, write $c(\\sigma)$ for',src.index('\\label{push:src:E.1.1}',src.index('\\clearpage\n\\section{The marked family')))
b=src.index('\\begin{theorem}[classification in Viaclovsky',a)
old=src[a:b]
new='\\begin{definition}[The residual cusp defect]\n\\hypertarget{tag-IP11}{}\\label{I:def:residual-cusp-defect}\n'+old.strip().replace("In the question's notation",'In the marked coordinates')+'\n\\end{definition}\n\n'
save('I:def:residual-cusp-defect',old,new,'Number the complete residual-defect definition as IP11, preserving its clockwise defect formula, quotient lattice and p equation.')
old=r'''The preceding theorem answers Question 3 of
\cite[Section 1.1]{ViaclovskyLog2026}.  The original return asserted the
same arithmetic classification in \cref{fam:src:B.3.1}; the contribution here is
the explicit dictionary and the complete enlarged-root and collar
argument.'''
assert src.count(old)==1
changes.append(dict(id='I-common-source-comparison-record',old=old,new='',expected_count=1,reason='Move return-history and contribution narration to the provenance record. The mathematical result and exact coordinate dictionary remain in famB3.1 and pushE1.1--2.'))
records.append(dict(statement_id='push:src:E.1.2:postproof-attribution',old=old,new='',reason='Archived historical attribution, not a removed mathematical assertion.'))

for cid,old,new in [
 ('I-common-elliptic-section-title','\\subsection{A typed fibre dictionary}','\\subsection{The elliptic surface and the period quotient}'),
 ('I-common-higher-section-title','\\section{Classification and deformation questions}','\\section{Classification in elliptic-surface coordinates}')]:
    assert src.count(old)==1
    changes.append(dict(id=cid,old=old,new=new,expected_count=1,reason='Use a mathematical section title.'))

guard=dict(source=str(SOURCE),source_sha256=sha,created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),changes=changes,proof_reread_status='DRAFT: old complete proof blocks read; proposed blocks require final bounded comparison before events are emitted',label_preservation='All old label and hypertarget anchors preserved by assertion; new definitions/remark IP09--IP11',parent_owned_span='app:rederive:fam-src-A.5.1 is unchanged')
(OUT/'S6_SERIES_PUBLISH_I_common_family_guards.json').write_text(json.dumps(guard,indent=2,ensure_ascii=False)+'\n')
(OUT/'S6_SERIES_PUBLISH_I_common_family_comparison.json').write_text(json.dumps(dict(source_sha256=sha,changes=records),indent=2,ensure_ascii=False)+'\n')
diff=[]
for r in records:
    if 'old_path' in r:
        diff.extend(difflib.unified_diff(Path(r['old_path']).read_text().splitlines(),Path(r['new_path']).read_text().splitlines(),fromfile=r['statement_id']+' old',tofile=r['statement_id']+' proposed',lineterm=''))
(OUT/'S6_SERIES_PUBLISH_I_common_family_diff.txt').write_text('\n'.join(diff)+'\n')
print(json.dumps(dict(source_sha256=sha,guard_count=len(changes),record_count=len(records),changed_subjects=[r['statement_id'] for r in records]),indent=2))
