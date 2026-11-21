"""Small remaining analytic consolidations; guarded edits only."""
from pathlib import Path
import json,hashlib,datetime,re
B=Path(__file__).parent
source=Path('/workspace/scratch/653608133b22/work/S6_SERIES_PUBLISH_I.tex')
original=source.read_text();s=original;guards=[];removed=[]
def patch(old,new,reason,ids=()):
 global s
 assert s.count(old)==1,(reason,s.count(old),old[:100])
 guards.append(dict(id=f'IA-H-{len(guards)+1:02}',old=old,new=new,
  expected_count=1,reason=reason,statement_ids=list(ids)))
 s=s.replace(old,new,1)
def archive(name,text,why):
 removed.append(dict(name=name,reason=why,original=text,sha256=hashlib.sha256(text.encode()).hexdigest()))

a=s.index(r'\begin{proposition}[the real locus]')
b=s.index(r'\end{proof}',a)+len(r'\end{proof}')
old=s[a:b]
archive('ari_C22_full_reflection_proof',old,
 'Full reflection proof consolidated with the retained seven-step fam B4.2 proof; unique affine correcting vectors retained in a numbered remark.')
new=r'''\begin{corollary}[The real locus]
\hypertarget{tag-000M}{}\label{ari:C.2.2}
\StatementRecord{ari:C.2.2}{proved}{000M}{\SeriesRef{fam:src:B.4.2}}
An antiholomorphic equivalence $X_c\to X_{c'}$ exists exactly when
$c'-(1-\bar c)\in2\mathbb Z$. Consequently $X_c$ admits an
antiholomorphic involution exactly when $q_2\in\mathbb R\setminus\{0\}$.
\end{corollary}
\begin{proof}
The equivalence criterion and the involution are
\cref{fam:src:B.4.2}. Its real locus is $w=-\bar w$.
Under the exact coordinate change $q_2=iw/216$, this is
$q_2=\bar q_2$; the parameter domain excludes zero.
\end{proof}

\begin{remark}[Affine corrections for the real comparison]
\hypertarget{tag-IA20}{}\label{I:real-affine-corrections}
The normalization in \cref{fam:src:B.4.2} has linear fibre map
$-I_2$, parameter shift $1$, and lattice map $-I+E$, where
$d=(0,0,0,1)^t$ and $E=d(1,0,0,0)$.
For the canonical vectors $v_1=\varepsilon$, $v_2=-\varepsilon'$
and the reflected vectors
$v'_1=-\varepsilon+d$, $v'_2=\varepsilon'-3d$, its integral
correcting cocycles and rational translations can be taken as
\[
 \ell_1=(0,0,-2,0)^t,\quad \ell_2=(0,2,0,0)^t,
 \qquad
 r_1=(0,-2/3,-2/3,0)^t,\quad r_2=(0,1,1,0)^t.
\]
Direct substitution in the matrices of \cref{fam:src:B.2.1} gives
\[
 N_1\ell_1=-2d,\qquad N_2\ell_2=4d,\qquad
 (I-A_j)r_j=\frac{v_j-(-I+E)v'_j}{m_j}+\ell_j.
\]
The cusp cocycle is
\[
 \ell_0=-A_0(\ell_1+A_1\ell_2)=(0,0,4,-2)^t.
\]
These are the explicit corrections for the root-disc and cusp
extensions in \cref{fam:src:B.2.1,fam:src:B.4.2}.
\end{remark}'''
patch(old,new,'Use the full retained reflection theorem once and preserve all unique normalization constants.',('ari:C.2.2',))

a=s.index(r'\par This finite comparison proves equality of the entire modular forms.')
b=s.index('For $k=2,N=s^2$',a)
old=s[a:b]
archive('IA08_original_R5_valence_product_argument',old,
 'Complete elementary characteristic-zero valence proof retained as a check record; short primary Sturm application has explicit characteristic-zero bridge.')
new=r'''\par The difference of the two weight-two forms has integral
Fourier coefficients. Apply Sturm's congruence theorem
\cite[Theorem~9.18, p.~171]{CgzStein2007} to this difference
modulo each rational prime. Agreement through
$\lfloor kI/12\rfloor$, where
\[
 I=[\mathrm{SL}_2(\mathbb Z):\Gamma_0(N)]
   =N\prod_{p\mid N}(1+1/p),
\]
forces every coefficient to vanish modulo every prime;
the index is also stated in
\cite[Corollary~9.20, p.~174]{CgzStein2007}.
An integer divisible by every prime is zero, so the forms
are equal over $\mathbb C$.
'''
patch(old,new,'Replace the repeated known valence proof by the exact congruence theorem and its explicit characteristic-zero application.',('ari:C.6.R5',))

# The titles below do not change any mathematical statement or proof.
titles={
 'the phases and the two periods':'Phases and the two periods',
 'the full division identity':'The full division identity',
 'algebraicity and explicit fields for every order':'Algebraicity and fields of division values',
 'the five values and all orders through eight':'Five norm values and torsion through order eight',
 'the two first-derivative identities':'The two first-derivative identities',
 'fourth order at the maximum':'The fourth-order expansion at the maximum',
 'three uniform bounds on the elliptic norm':'Three uniform bounds on the elliptic norm',
 'an explicit local maximum on a larger disc':'The maximum on an explicit local disc',
 'the comparison of the two local discs':'Comparison of the two local discs',
 'the first three normalized duplication steps':'The first three normalized duplication steps',
 'no smooth CM-torsion parameter':'The CM torsion fibres',
 'the global formula':'The global height formula',
 'exact finite local-height calculation':'Finite local heights',
 'the CM models and their height identities':'The CM models and their height identities',
 'the maximum as a height inequality':'The maximum as a height inequality',
 'rigorous high-precision height enclosures':'Explicit height enclosures',
 'the Mahler-measure identities':'The Mahler-measure identities',
 'the two complex beta integrals':'The two complex beta integrals',
 'the signed Gaussian identity':'The signed Gaussian identity',
}
for oldtitle,newtitle in titles.items():
 matches=list(re.finditer(r'\\begin\{(?:proposition|cited)\}\['+re.escape(oldtitle)+r'\]',s))
 assert len(matches)==1,(oldtitle,len(matches))
 old=matches[0].group();new=old.replace('['+oldtitle+']','['+newtitle+']')
 patch(old,new,'Give the statement a concise mathematical title; no mathematical change.')

old=r'''The covering equations and local tests use exact arithmetic in
$\mathbb Q(\sqrt3)$; every surviving class is represented by a point,
and every excluded class has a local obstruction at the stated primes.
'''
patch(old,'','Remove the immediately repeated description of the same surviving classes and local obstructions.',('ari:C.6.T2',))

meta=dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
 base=str(source),base_sha256=hashlib.sha256(original.encode()).hexdigest(),
 policy='Guarded proposals only; root TeX not modified. All mathematical changes are scoped exposed-proof rereads.',guards=guards)
(B/'S6_SERIES_PUBLISH_I_editorial_batch_h_guards.json').write_text(json.dumps(meta,indent=2)+'\n')
(B/'S6_SERIES_PUBLISH_I_editorial_batch_h_preview.tex').write_text(s)
(B/'S6_SERIES_PUBLISH_I_editorial_batch_h_removed.json').write_text(json.dumps(removed,indent=2)+'\n')
oldlabels=set(re.findall(r'\\label\{([^}]+)\}',original));newlabels=set(re.findall(r'\\label\{([^}]+)\}',s))
assert oldlabels<=newlabels,oldlabels-newlabels
oldtags=set(re.findall(r'\\hypertarget\{tag-([^}]+)\}',original));newtags=set(re.findall(r'\\hypertarget\{tag-([^}]+)\}',s))
assert oldtags<=newtags,oldtags-newtags
assert s.count('tag-IA20')==1
print(json.dumps({'guards':len(guards),'new_labels':sorted(newlabels-oldlabels),'new_tags':sorted(newtags-oldtags),'root_modified':False}))
