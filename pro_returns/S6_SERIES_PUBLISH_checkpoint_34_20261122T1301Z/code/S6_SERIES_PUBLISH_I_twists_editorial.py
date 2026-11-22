from pathlib import Path
import json,hashlib,datetime
from S6_SERIES_PUBLISH_editing import Editor,block
r=Path(__file__).resolve().parents[1];ed=Editor('I');reviewed={}
def within(label,old,new,why,kind='D08'):
 whole=block(ed.text,label);assert whole.count(old)==1,(label,old[:100])
 reviewed.setdefault(label,{'old':whole})
 ed.replace(whole,whole.replace(old,new),kind,why,label)

old=r'''We use the marked threefold, with its arbitrary admissible
constant $c$.  Coefficients of coherent cohomology are complex.  In this
section $\omega_f=K_X\otimes f^*K_B^{-1}$,
$\mathcal L=\Omega_B^1(\log\Sigma)=\OO_B(1)$,
$\mathcal A=\Omega_X^1(\log D)$, and
$\mathcal E=\mathcal A/f^*\mathcal L$.  We write $\gamma,u$ also for
their images in $R^1f_*\OO_X$; this convention concerns cohomology
classes and does not identify them with differential-form representatives.'''
new=r'''\begin{definition}[Logarithmic cotangent notation]
\hypertarget{tag-PI17}{}\label{I:def:coarse-log-cotangent}
For an admissible marked member, set
\[
 \omega_f=K_X\otimes f^*K_B^{-1},\qquad
 \mathcal L=\Omega_B^1(\log\Sigma)=\OO_B(1),\qquad
 \mathcal A=\Omega_X^1(\log D),\qquad
 \mathcal E=\mathcal A/f^*\mathcal L.
\]
All coherent cohomology groups have complex coefficients.
The symbols $\gamma,u$ in $R^1f_*\OO_X$ denote the images of
the marked integral classes under the constant-to-coherent
cohomology map. Representatives in the Dolbeault resolution are
specified separately by their displayed forms.
\end{definition}'''
ed.replace(old,new,'D15','Number the exact cotangent sheaves and constant-to-coherent notation map.','I:def:coarse-log-cotangent')
within('inv:D4.1',r'''The code evaluates
these formulas for $-240\le n\le240$ using two independent integer
cohomology counts; their alternating sums are all one. That last
check is supplementary to the sheaf proof.''','',
 'Move the finite verification range and check report to records; the projection/Leray proof remains.','D09')
within('inv:D4.2',r'''so this calculates the
actual coherent cohomology $H^q(W,M_z|_W)$, not just a topological
analogy.''',r'''so this normalization resolution computes
$H^q(W,M_z|_W)$ through the displayed cellular complex.''',
 'Describe the exact normalization-to-cellular chain comparison.')
within('inv:D4.2',r'''This proves (D.14), including its annihilator and not only its residue
dimension.''',r'''The reduced support gives annihilator $(q)$ and proves (D.14).''',
 'State the annihilator calculation directly.')
within('inv:D4.3','The exceptional nonintegral twists cannot be omitted','The exceptional nonintegral twists','Use a mathematical title.')
within('inv:D4.3','The period\nidentification in Part A','The period\nidentification in \\cref{I:weierstrass-comparison}','Resolve the period-model reference.','D03')
whole=block(ed.text,'inv:D4.3');a=whole.index('The exact chord-and-tangent duplication');b=whole.index('\\end{enumerate}',a)
within('inv:D4.3',whole[a:b],r'''The integers $p,q$ are the marked elliptic-logarithm coordinates of
this order-four point; the displayed period relation determines the
corresponding resonance lattice.
''','Archive the diagnostic rational values and program output; retain the exact duplication and nonzero-discriminant argument.','D09')
within('inv:D4.4',r'''Thus averaging is a quasi-isomorphism, not merely a fibrewise
dimension comparison.''',r'''These homotopies exhibit averaging as a quasi-isomorphism.''',
 'State the established chain equivalence positively.')
within('inv:D4.4',r'''The chain-level comparison can be written without an unspecified
holomorphic gauge.''',r'''The chain-level comparison uses the following frames.''',
 'Introduce the explicit frames directly.')
within('inv:D4.4',r'''The conventional factor $2\pi i$ in the Dolbeault representative of
the exponential class multiplies both components of $a$ by the
same nonzero constant; absorbing it in the frame has no effect on
any module below.''',r'''Let $\lambda=2\pi i$. The Dolbeault exponential convention gives
the differential with Picard vector $\lambda a$ and tangent term
$\kappa$. Its explicit chain isomorphism to (D.19) is, in degree $j$,
\[
 F^j|_{V\otimes\bigwedge^jG}=\lambda^{-j}\operatorname{id},
 \qquad
 F^j|_{L\otimes\bigwedge^jG}=\lambda^{-j-1}\operatorname{id}.
\]
Direct substitution gives $F^{j+1}d_{\lambda a,\kappa}
=d_{a,\kappa}F^j$ on both summands. The inverse multiplies them
by $\lambda^j$ and $\lambda^{j+1}$, respectively. These constant
maps also commute with the finite cyclic action.''',
 'Give the exact chain isomorphism for the existing 2pi-i normalization, including the tangent-extension term.','D22')
within('inv:D4.4',r'''This identifies the chain map and its tangent extension;
no unspecified map between fibre cohomology groups is being used.''',r'''Together these formulas identify the chain map and its tangent extension.''',
 'Keep the exact chain map without a defensive clause.')
within('inv:D4.4','The determinant of $\\kappa$ is nonzero there by\nPart A.',
 'The determinant of $\\kappa$ is nonzero there by\n\\cref{inv:A2.1}.','Resolve the determinant input.','D03')
within('inv:D4.4','The exact period determinant identity in Part A gives',
 'The period determinant identity in \\cref{inv:A2.1} gives','Resolve the exact derivative identity.','D03')
within('inv:D4.4',r'''Thus neither the order of the Picard section nor the determinant
order alone is used to select a Smith form. The joint coefficient
has been evaluated exactly.''',r'''This nonzero joint coefficient determines the two transverse
orders in the following Smith presentation.''','State the role of the exact coefficient positively.')
within('inv:D4.4','We specify the character convention to avoid a sign ambiguity.',
 'We use the following character convention.','State the convention directly.')
whole=block(ed.text,'inv:D4.4');a=whole.index('The two independent\nexact checks in');b=whole.index('\\end{enumerate}',a)
within('inv:D4.4',whole[a:b],'','Move the Smith/jet corroboration report to records; every local module and character calculation is retained.','D09')
within('inv:D4.5',r'''To clarify the word generic, the''',r'''The''','Introduce the universal holomorphic family directly.')
within('inv:D4.5',r'''Some indexed resonances, namely the two invisible
order-four congruences, produce no jump; (D.25) distinguishes them.''',r'''The jump set is the union of the four thresholds
$h^0\ge1$, $h^1\ge1$, $h^2\ge2$ and $h^3\ge1$, hence is locally
discrete. The order-four congruences $n\equiv0,3\pmod4$
have zero contribution in (D.25).''','Identify the exact finite union of analytic thresholds and the zero weights.')
within('inv:D4.5',r'''This is an explicit countable description of the jump loci in the
Picard coordinate, rather than a generic assertion. It can also be
indexed algebraically on the elliptic surface.''',r'''The jump loci can also be indexed algebraically on the elliptic surface.''',
 'Introduce the exact algebraic indexing directly.')
within('inv:D4.5',r'''The script
\texttt{d\_division\_polynomials.py} evaluates the polynomials
exactly for $2\le N\le12$; for example the first nonconstant
regular factors are $5t-32$, $89t^2+4736t-4096$ and
$11t^2-6016t+8192$. These computations specify an executable
enumeration of the resonance loci without inventing decimal values
for the unspecified parameter $c$.''',r'''The division-polynomial recursion gives the first nonconstant
regular factors $5t-32$, $89t^2+4736t-4096$ and
$11t^2-6016t+8192$. The displayed lattice formula sends every
such root to its resonance values in the fixed Picard coordinate.''',
 'Retain the exact polynomial inputs and resonance map; move implementation and production wording to records.','D09')
within('inv:D4.5','As an independent index check,','For the index,','State the mathematical computation without check narration.')
within('inv:D4.5',r'''The index is used here to
verify the completed sheaf calculation, not to select its lengths.''','',
 'Remove a closing verification recap.')
within('push:src:E.2.2','local separation and canonical dimension','Local separation and Kodaira dimension','Use the standard name and title capitalization.')
within('push:src:E.2.3','separation in irreducible analytic families','Separation in irreducible analytic families','Capitalize the title.')
within('push:src:E.2.3',r'''This proof uses relative cohomology only; it makes
no general invariance assertion for Kodaira dimension.''','',
 'Remove a scope disclaimer after the full exact proof.','D02')

# Relative log-cotangent symbols retain their precise quotient definitions.
for label in ['inv:B1.1','inv:B3.1']:
 old=block(ed.text,label);new=old
 if label=='inv:B1.1':
  new=new.replace("E'=\\Omega",r"\mathcal E'=\Omega").replace("f_*E\\simeq",r"f_*\mathcal E\simeq").replace("f'_*E'",r"f'_*\mathcal E'").replace("defining $E'$",r"defining $\mathcal E'$")
 else:
  new=new.replace('E_X',r'\mathcal E_X').replace('E_Y',r'\mathcal E_Y')
  new=new.replace('The pullback maps induce isomorphisms',r'''For $\mathcal E_X$ of Definition~\ref{I:def:coarse-log-cotangent}
and the identical quotient $\mathcal E_Y$ on $Y$, pullback induces isomorphisms''')
 reviewed.setdefault(label,{'old':old});ed.replace(old,new,'D06','Use the declared relative logarithmic cotangent quotient notation, keeping the same pullback maps.',label)
within('inv:B1.1',r'''hence this equality
is an equality of the extensions inside the common punctured-disc
bundle, not only an equality of their ranks or degrees.''',r'''hence the map $s^{ea}v\mapsto z^av$, with $z=s^e$,
identifies the extensions inside the common punctured-disc bundle.''',
 'State the exact invariant-lattice comparison map.')
within('inv:B1.1','in Part A and the eigenframe calculation above',
 'in \\cref{inv:A1.0,inv:A1.1} and the eigenframe calculation above','Resolve the local-freeness inputs.','D03')
within('inv:B1.2','the Hodge diamond of Part A','the Hodge diamond of \\cref{inv:A3.1}','Resolve the Hodge-table reference.','D03')
within('inv:B1.2','In Part A the cokernel of $\\kappa_0$ is',
 'By \\cref{inv:A2.1,inv:A2.4}, the cokernel of $\\kappa_0$ is','Resolve the connecting-map inputs.','D03')
within('inv:B1.2','the residue diagram of Part A','the residue diagram of \\cref{inv:A1.3}','Resolve the residue diagram.','D03')
within('inv:B1.2',r'''so no separate invariance assumption about absolute forms is needed.''',r'''as the degree-zero entries and their duals show.''','State the direct-image reason positively.')
within('inv:B2.1',r'''Thus these Hodge numbers do not distinguish the multiplicity families.''',r'''The relative comparison maps in Proposition~\ref{inv:B1.1}
identify the cohomological calculation for all these multiplicities.''',
 'Name the exact cohomological comparison underlying the common numbers.')
within('inv:B2.1',r'''\ref{inv:B1.2} computes the cohomology, with no use of that
topological conclusion.''',r'''Proposition~\ref{inv:B1.2} computes the cohomology by the relative
cotangent comparison.''','State the supplying argument positively.')

a=ed.text.index('For completeness the requested small pairs');b=ed.text.index('\\subsection{Finite fundamental groups',a)
old=ed.text[a:b];table=old[old.index('\\['):old.index('\\]')+2]
new=r'''\begin{remark}[Six multiplicity pairs]
\hypertarget{tag-PI18}{}\label{I:small-multiplicity-pairs}
The formulas of \cref{inv:B2.1,inv:B2.2} give the following values,
where $r_1,r_2$ are the canonical-divisor coefficients and
$P_n^-=h^0(-nK_X)$:
'''+table+r'''
Each entry follows by substitution in the displayed floor formula,
or by counting monomials of weights $(m_2,m_1)$.
\end{remark}

'''
ed.replace(old,new,'D15','Number the exact small-pair table and remove the request/program history.','I:small-multiplicity-pairs')
within('inv:B3.1',r'''finite etale holomorphic''',r'''finite \'etale holomorphic''','Restore the accent.','D23')
within('inv:B3.1',r'''Consequently the dual complex is an actual
degree-$n$ covering of the original real two-torus, rather than merely
a cell complex with the same cell counts.''',r'''The lifted incidence maps therefore make the dual complex a
degree-$n$ covering of the original real two-torus.''','State the actual lifted-cell covering map.')
within('inv:B3.2','The splittings involving $T_n$ are not canonical.',
 r'''Writing $V$ for the locally free quotient, the splittings form an
affine space under $\operatorname{Hom}(V,T_n)$, by the exact
sequence in the proof.''','Specify the exact space of splittings instead of an unqualified noncanonicity statement.')
within('inv:B3.3',r'''We compute its rational topology here
from the actual attachment maps; the integral homology assertion
of AC26 is not used as an input.''',r'''Its rational topology is computed by the following attachment maps.''',
 'Introduce the exact attaching calculation directly.')
within('inv:B3.3',r'''We justify the comparison with $N$ without assuming a collapse
theorem from AC26.''',r'''The comparison with $N$ is given by this explicit deformation
retraction.''','State the explicit supplied map.')
within('inv:B3.3',r'''They therefore bound in $N$ with the literal toric meridian;
no choice of an unrecorded collar lift is being made.''',r'''They therefore bound in $N$ with the specified toric meridian.''',
 'State the fixed boundary map positively.')
within('inv:B3.3',r'''The integer matrices and all exterior-power
identities were checked exactly in \texttt{code/b\_topology.py},
with output \texttt{outputs/b\_topology.txt}.''','',
 'Move the diagnostic program report to records; retain all matrices, attachments and rank proofs.','D09')
within('inv:B3.3',r'''Part C's argument using this rational topology and the same Hodge
table now gives''',r'''Proposition~\ref{inv:C1.1}, applied to this rational topology and
the same Hodge table, gives''','Resolve the Frolicher argument.','D03')

for label,data in reviewed.items():data['new']=block(ed.text,label)
ed.save()
(r/'records/S6_SERIES_PUBLISH_I_twists_editorial_comparison.json').write_text(json.dumps({
 'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'proofs':reviewed,
 'scope':'Root read every full affected old proof, then compared all changes and retained calculations. The added constant normalization is the explicit degreewise chain isomorphism of the already displayed complex. This is editorial use/recheck, not a new preread independent proof.',
 'new_numbered_content':['Coarse logarithmic cotangent notation','Six unchanged multiplicity-pair values']
},indent=2)+'\n')
