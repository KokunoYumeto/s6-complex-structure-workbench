from pathlib import Path
import hashlib,json,datetime
root=Path('/workspace/scratch/490d8ca4e928/work/S6_10_PAPERS')
p=root/'papers/II/opening.tex'
s=p.read_text()
start=s.index(r'\subsection*{12. Closedness along deformation discs}')
end=s.index(r'\subsection*{14. The base parameter',start)
old=s[start:end]
new=r'''\subsection*{12. Separation along analytic and continuous deformations}
\RungZero{The ordered coprime pair $(3k,4l)$ is constant in every
proper smooth holomorphic family over a connected reduced analytic
base containing a constructed member, and it distinguishes the
constructed members' deformation classes through arbitrary finite
chains.  Disc propagation and finite curve projections make the
fixed-pair locus open and closed; the actual Kuranishi retraction
gives the same separation in the $C^\infty$ space of integrable
complex structures and its indicated diffeomorphism quotients
(\ref{push:src:E.2.23}--\ref{push:src:E.2.24}).}
\RungOne
\begin{enumerate}[label=\arabic*.,leftmargin=*]
\item The fibration-retention theorem supplies the pencil near
each constructed member; its intrinsic anticanonical description
identifies the pencils on overlapping deformation charts.
\item The finite covers carry the labelled integral monodromies
and attachment classes.  Their holomorphic continuation preserves
the specified root charts and finite multiplicities.
\item The marked period map has the given root-curve form on the
known open set.  The analytic comparisons in
\ref{push:src:E.2.21} extend a full punctured-disc family, and
\ref{push:src:E.2.22} fills its successive discrete exceptional
sets in reverse order to propagate from any nonempty known open
subset of a disc.
\item The cusp comparison retains the nonzero logarithmic
coefficient and the full affine gluing class.  Together with the
finite charts, it identifies the continued members with the same
$(3k,4l)$ construction.
\item The fixed-pair locus is open by local miniversality.  At a
boundary point $b$, choose a finite local projection
$\rho:T\to\Delta^d$ of an irreducible branch with
$\rho^{-1}(0)=\{b\}$.  The inverse image of the line through
$0$ and $\rho(a)$, for a known point $a$, has an irreducible
curve containing both $a$ and $b$; pullback to its normalization
and the disc propagation just proved show that $b$ is known
(\ref{push:src:E.2.23}).
\item The locus is therefore closed, and connectedness makes it
the whole analytic base.  This preserves the pair through every
finite deformation chain; conversely the admissible half-plane
and its quotient by the actual period lattice $2kl\Z$ give a
connected family for each fixed pair
(\ref{push:src:E.2.23}).
\item At every smooth integrable structure $J_0$, the Kuranishi
local theorem supplies a connected neighbourhood $\mathcal U$
and a retraction $\Xi:\mathcal U\to K$, with each $J$
biholomorphic to $\Xi(J)$ through a diffeomorphism isotopic to
the identity.  Apply the analytic-base conclusion to the
connected reduction of $K$: if $\mathcal U$ meets the fixed-pair
locus, every point of $\mathcal U$ belongs to it.  Thus that locus
is open and closed, as are its images under the specified
saturated diffeomorphism quotients, and every continuous family
over a connected parameter space retains its pair
(\ref{push:src:E.2.24}).
\end{enumerate}

\subsection*{13. Four explicit corrections}
\RungZero{The Poincar\'e line bundle gives a torsion higher
direct image in the scope of the printed local-freeness claim;
a square-zero embedded point survives every divisor twist;
positive combs have $2m+1$ global vector fields; and an explicit
half-period section makes the proposed theta square vanish
while the actual period determinant is nonzero.  The four
constructions and their exact corrections are
\ref{cdp:st:E12}, \ref{cdp:st:E17}, \ref{inv:E2.4}, and
\ref{cdp:st:E18}, with their source scopes retained.}
\RungOne
\begin{enumerate}[label=\arabic*.,leftmargin=*]
\item For the normalized Poincar\'e line $P$ on $E\times E$,
the moving degree-one divisor gives
$Rp_*P=\C_0[-1]$, with length one at the origin.
Tensoring with $R\Gamma(\PP^1,\OO(-2))=\C[-1]$ gives the
direct-image counterexample $\C_0[-2]$.
\item On $\OO_Z=\OO_{\PP^1}\oplus\C_p$ with square-zero
second summand and a Cartier divisor $q\ne p$, the equality
$\OO_Z(-kq)=\OO_{\PP^1}(-kq)\oplus\C_p$ retains a nonzero
section for every $k$.
\item Krull intersection proves the corrected stable-space
formula: descending twists stabilize at the sections whose
support avoids the Cartier divisor.  Absence of embedded
components gives the stated eventual vanishing case.
\item The computed $h^0(T_{X_m})=2m+1$ is at least $25$ for
$m\ge12$.  Its comparison with the printed two-vector-field
bound gives the explicit counterexample and the exact
algebraic-dimension scope described in \ref{inv:E2.4}.
\item On a small disc about $\tau=i$, take $\mu=1/2$ and
\[
 v=\frac{i}{\pi}\log\frac{\vartheta_1(1/2,\tau)}{\eta(\tau)}+i,
 \qquad
 \Lambda_\tau=\Z(1,0)+\Z(0,1)+\Z(\tau,1/2)+\Z(3,6v).
\]
The logarithm is real at $i$; the theta products give
$\operatorname{Im}v>0$, so $\C^2/\Lambda_\tau$ is a proper
family of compact tori.  The quotient
$\vartheta_1(z-1/2,\tau)/\vartheta_1(z,\tau)$ has divisor
$[1/2]-[0]$ and multipliers $1,-1$, giving the actual elliptic
line bundle and its contracting linearization.  Adjoining
$(1/2,v)$ enlarges the lattice by index six; identity on
$\C^2$ induces the degree-six isogeny to the symmetric-period
family with $\Omega=\left(\begin{smallmatrix}\tau&1/2\\1/2&v\end{smallmatrix}\right)$
and preserves its Kodaira--Spencer rank
(\ref{cdp:st:E18}).
\item Put $h=\partial_\mu\log\vartheta_1(\mu,\tau)$.
The half-period shift and evenness of $\vartheta_2$ give
$h=\mu'=0$, whereas the heat equation gives
\[
 \det\Omega'(i)=-\frac{\wp(1/2;i)}{4\pi^2}
 =-\frac{\vartheta_3(0,i)^4+\vartheta_4(0,i)^4}{12}\ne0.
\]
In the displayed linearization the full identity is
\[
 \det\Omega'
 =-\left(\mu'-\frac{i}{2\pi}h\right)^2
       -\frac{\wp(\mu,\tau)}{4\pi^2}
 \qquad\text{(\ref{cdp:eq:E-theta-general}).}
\]
For the actual original period branch, the equation
$\wp(\mu,\tau)=0$ proves its square formula; an added
holomorphic linearization term contributes its derivative
(\ref{cdp:st:E18}).
\end{enumerate}

'''
assert s.count(old)==1
before=hashlib.sha256(p.read_bytes()).hexdigest()
p.write_text(s.replace(old,new))
pv=root/'build/sign_II/preview.tex'
t=pv.read_text(); assert t.count(old)==1
pvbefore=hashlib.sha256(pv.read_bytes()).hexdigest()
pv.write_text(t.replace(old,new))
receipt={'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'checker':'GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro)','scope':'Final plan-to-opening coverage repair; exact previously fully checked body arguments reopened for the receiving summary. No additional full-proof credit.','changes':{'II.L12':{'rung_zero_sentences':2,'rung_one_steps':7,'exact_refs':['push:src:E.2.21','push:src:E.2.22','push:src:E.2.23','push:src:E.2.24'],'mechanisms':['finite local projection with unique zero fibre','irreducible curve over line through known point and boundary point','normalization and generic-disc propagation','connected base and connected fixed-pair period quotient','actual connected Kuranishi retraction and isotopic diffeomorphism','saturated open-and-closed quotient images']},'II.L13':{'rung_zero_sentences':2,'rung_one_steps':6,'exact_refs':['cdp:st:E12','cdp:st:E17','inv:E2.4','cdp:st:E18','cdp:eq:E-theta-general'],'new_mechanisms':['full lattice and elliptic line/linearization','identity-induced degree-six isogeny','half-period zero square and nonzero theta determinant','retained Weierstrass correction and original branch wp(mu)=0']}},'files':[{'path':str(p.relative_to(root)),'before_sha256':before,'after_sha256':hashlib.sha256(p.read_bytes()).hexdigest()},{'path':str(pv.relative_to(root)),'before_sha256':pvbefore,'after_sha256':hashlib.sha256(pv.read_bytes()).hexdigest()}],'body_sha256':hashlib.sha256((root/'papers/II/body.tex').read_bytes()).hexdigest(),'numbered_environments_added':0,'preview_build':'pending following source integration'}
(root/'analysis/sign_final_opening_coverage_receipt.json').write_text(json.dumps(receipt,indent=2,ensure_ascii=False)+'\n')
print(json.dumps(receipt,ensure_ascii=False,indent=2))
