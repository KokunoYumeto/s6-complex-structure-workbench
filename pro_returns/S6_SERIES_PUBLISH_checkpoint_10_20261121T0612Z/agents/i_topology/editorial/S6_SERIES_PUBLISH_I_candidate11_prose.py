from pathlib import Path
import json,hashlib,datetime,csv
R=Path('/workspace/scratch/653608133b22');D=R/'work/agents/i_topology';E=D/'editorial';S=E/'S6_SERIES_PUBLISH_I_candidate11_source_snapshot.tex';O=R/'source/S6_SERIES_GRIND_I.tex';before=S.read_text();s=before;orig=O.read_text();patches=[]
sha=lambda t:hashlib.sha256(t.encode()).hexdigest()
def edit(old,new,ids,why,proof=False):
 global s
 if isinstance(ids,str):ids=[ids]
 assert s.count(old)==1,(old,s.count(old));patches.append(dict(id=f'I-topology-c11-prose-{len(patches)+1:02d}',old=old,new=new,statement_ids=ids,reason=why,proof_change=proof));s=s.replace(old,new)
def block(t,lab):
 p=t.index('\\label{'+lab+'}');a=t.rfind('\\begin{',0,p);e=t.index('\\end{proof}',p)+len('\\end{proof}');return t[a:e]

edit('Gysin maps just constructed glue the surviving\nclasses with unit coefficient, so this local\ncancellation cannot hide an extension or an\nintegral index.','Gysin maps just constructed glue the surviving\nclasses with unit coefficient.','push:src:A.4.9','Delete the repeated defensive interpretation; the explicit integral Gysin maps and unit coefficients remain.')
edit('claimed topology. Every step is on the specified plain-cusp\ncharts, so the conclusion has exactly the scope in the statement.','claimed topology.','push:src:B.2.2','The plain-cusp hypotheses remain in the statement and all chart maps remain in the proof.')
edit('[the marked genus-three component cover]','[The marked genus-three component cover]','push:src:B.3.2','Capitalize the statement title.')
edit('A cyclic cusp-root construction using a\nfractional translation by the two cusp\nperiods cannot repair \\ref{push:src:B.3.1} while retaining\nthe reduced Mumford fibre for $r\\ne0$.\nMore precisely, let $q=s^d$, $u=r^n$,','Let $q=s^d$, $u=r^n$,','push:src:B.3.3','Replace proposal language by the exact existing universal statement; all deck and multiplicity hypotheses/conclusions remain.')
edit('$(\\mathbb Z/d)^2$. The proposed deck\ngenerator translates','$(\\mathbb Z/d)^2$. The deck\ngenerator translates','push:src:B.3.3','Remove the process epithet; same deck generator.')
edit('Thus the proposed repair that takes the\nnormalization over $C$ to be ruled over\nthis split elliptic surface, with adjacent\nconductor map $t_Q\\circ\\sigma$, is\nimpossible.','For a normalization over $C$ ruled over this split elliptic\nsurface, the twelfth iterate of an adjacent conductor map\n$t_Q\\circ\\sigma$ is therefore $t_{12kP}$ for some $k\\in\\mathbb Z$.','push:src:B.3.4','State the exact receiving trace calculation already proved; the preceding exclusion of t6P remains.')
edit('proves the claimed obstruction, with\nthe scope stated in the theorem.','proves the claimed obstruction.','push:src:B.3.4','Remove duplicate scope prose; the trace formula remains.')
edit('[analytic unramified torsors do not evade the Hodge obstruction]','[Hodge theory of analytic unramified torsors]','push:src:B.3.8','Short neutral title retaining the specified analytic torsor class.')
edit('Jacobian surface $\\mathscr E\\to C$ of \\ref{push:src:B.3.4}. Algebraicity\nor finite order of this analytic torsor class is not assumed.','Jacobian surface $\\mathscr E\\to C$ of \\ref{push:src:B.3.4}.','push:src:B.3.8','The quantified hypothesis already allows every compact smooth locally trivial analytic torsor; no algebraicity or finite-order condition is added.')
edit('Consequently the necessary non-$\\partial\\bar\\partial$\nnormalization component in \\ref{push:src:B.4.5} cannot be obtained simply\nby replacing the projective torsor of \\ref{push:src:B.3.6} by a nonalgebraic\nlocally trivial analytic torsor, followed by a ruled bundle\nand bimeromorphic modifications. This excludes that specified\nrepair; it does not assert that every possible cusp\nnormalization has this form.','Consequently none of these projective bundles or smooth compact\nbimeromorphic models can be the non-$\\partial\\bar\\partial$\nnormalization component required in \\ref{push:src:B.4.5}.','push:src:B.3.8','State the same exact incompatibility between the proved ddbar conclusion and the required component; retain the precise quantified class.')
edit('is K\\"ahler without an algebraicity hypothesis.','is K\\"ahler.','push:src:B.3.8','Buchdahl applies to the already stated compact analytic surface with b1=6; remove redundant disclaimer.')
edit('\\item There is an even shorter argument excluding a meromorphic\nextension of the punctured product comparison.  A sufficiently','\\item The fundamental groups also exclude a meromorphic\nextension of the punctured product comparison. A sufficiently','push:src:B.4.7','Introduce the retained complete fundamental-group argument directly.')
edit('[A normal-line obstruction on every semistable good-reduction interface]','[Normal-line obstruction at good reduction]','push:src:B.4.8','Shorten the printed title so its tag fits; all statement hypotheses remain.')
edit('This is an integral calculation; no limiting logarithm\nor asymptotic estimate is involved.\n','', 'push:src:B.4.8','Keep the explicit integral Chern-class calculation and remove the defensive comparison.')
edit('This elementary plumbing argument is all that is needed\nhere; no algebraic stable-reduction or comparison theorem\nfor arbitrary analytic total spaces is being assumed.\n','', 'push:src:B.4.8','Keep the complete plumbing proof, remove only its process disclaimer.')
edit('[Ordinary logarithmic torus cocycles and the remaining descent classes]','[Ordinary torus cocycles and descent classes]','push:src:B.4.9','Shorten title; all logarithmic and analytic exponential sequences remain.')
edit('[An explicit parabolic family and its nonextending exceptional correction]','[Parabolic families and exceptional divisors]','push:src:B.4.10','Short neutral title; no hypotheses or conclusions change.')
edit('Notice that no special smallness condition on the Picard parameter\n$\\kappa$ is required.','For each finite bound on $|\\kappa|$, these inequalities give such a radius $R$.','push:src:B.4.10','Restate the preceding uniform inequality positively, retaining arbitrary bounded holomorphic kappa.')
edit('divisor would still have a proper horizontal part of\ndegree $n$ would be finite over the disc and define a continuous','divisor would still have a proper horizontal part of\ndegree $n$, finite over the disc, defining a continuous','push:src:B.4.10','Repair the duplicated finite-clause grammar; the horizontal divisor, degree and symmetric-power map are unchanged.')
edit('Atiyah-extension map just computed, not a dimension count alone.','Atiyah-extension map just computed.','push:src:B.4.11','Retain the explicit map; remove the contrast.')
edit('automorphisms; it does not differentiate the coarse $j$-invariant.','automorphisms.','push:src:B.4.11','The preceding exact tau-period cocycle already gives the Kodaira–Spencer map, including extra-automorphism points.')
edit('There is no hypothesis about the kind of exceptional curve\nin this criterion.  A regular morphism of analytic','A regular morphism of analytic','push:src:B.4.11','The cited criterion is stated with its actual hypotheses immediately before this sentence.')
edit('deformation base lifts to the global base, without replacing\nthe prescribed local deformation by a different smoothing\ncomponent.','deformation base lifts to the global base.','push:src:B.4.11','The specified analytic disc and its exact lift remain; remove repeated scope language.')
edit('and blowing up its vertex; no finite base change is needed.','and blowing up its vertex over the original parameter disc.','push:src:B.4.12','Positive formulation of the same unchanged base and construction.')
edit('this follows from the Kunneth formula for','this follows from the K\\"unneth formula for','push:src:B.4.12','Correct mathematical-name typography.')
edit('In degree eight the quadric component is distinguished from the\nother smoothing component; no replacement of it by that other\ncomponent is made here.\n','', 'push:src:B.4.12','The exact displayed cone and its Q-minus-E fibre identify the smoothing; remove the unused comparison.')
edit('\\item For the more general assertion no blowdown is needed.\nIf an automorphism preserves $E$,','\\item For the more general assertion, an automorphism preserving $E$','push:src:B.4.13','Introduce the derivative map directly; retain the same line-bundle pullback and torsion calculation.')
# The previous replacement changes the grammar around its retained verb.
edit('an automorphism preserving $E$ its derivative in the normal\ndirection gives','an automorphism preserving $E$ induces through its derivative in the normal\ndirection an isomorphism','push:src:B.4.13','Grammatical completion with the exact normal derivative map.')
edit('\\citet[Theorem~(4.6), p.~566]{AtiyahSinger1968IIIE}; it requires\na compact complex manifold, not a K\\"ahler manifold.','\\citet[Theorem~(4.6), p.~566]{AtiyahSinger1968IIIE}, which applies\nto compact complex manifolds.','push:src:B.4.14','State the applicable hypothesis positively; all equivariant weights and character calculation remain.')
edit('comparison with its Jacobian. No extension of this\nsection across $r=0$ is asserted.','comparison with its Jacobian.','push:src:B.4.15','The exact domain U=Delta_z times punctured Delta_r is already printed; no map is extended.')
edit('origin. The cocharacter $\\mathbf u$ is needed only on\nthis disc and is not extended around the special base\npoints. Since the local rings of the total space are','origin. The cocharacter $\\mathbf u$ is defined on this disc.\nSince the local rings of the total space are','push:src:B.4.15','Retain the specified disc and cocharacter domain positively.')
edit('incompatible global assembly are unchanged. This proves\nthe precise local assertion and its stated limitation.','incompatible global assembly are unchanged.','push:src:B.4.15','The exact rotations and their component-label action remain; delete repeated conclusion prose.')
edit('of \\ref{push:src:B.4.7}; no extension of a meromorphic comparison is required.','of \\ref{push:src:B.4.7}.','push:src:B.4.17','The explicit Cartier cocycle construction remains; remove disclaimer.')
edit('representative $-ke$. This use of a period changes\nthe representative, not the quotient map.','representative $-ke$, since addition of those periods\npreserves the quotient map.','push:src:B.4.19','Positive exact period-quotient identification, with scalar sign unchanged.')
edit('isomorphism of the punctured families. It is not\nasserted to extend at $r=0$.','isomorphism of the punctured families.','push:src:B.4.19','The stated punctured domain remains explicit.')
edit('translates the elliptic base by $6P$. In particular\na shift of twelve need not be the identity on a\ncentral ruled component; no such identity is used.','translates the elliptic base by $6P$.','push:src:B.4.19','Keep the exact twelfth closing translation rather than repeated defensive wording.')
edit('\\item The component cover can also be read without\nguessing a global normalization. If $i_i$ is the','\\item The component cover is determined by the local indices.\nIf $i_i$ is the','push:src:B.4.19','Introduce the retained index/cocycle formula directly.')
edit('\\item We need more than the line isomorphism \\eqref{pub:I:eq:B-4-21-7}.\nThe point-blow-up charts give the following exact local','\\item The point-blow-up charts give the following exact local','push:src:B.4.21','The preceding normal-line isomorphism remains; introduce the additional exact chart maps directly.')
edit('In particular there is no additional exceptional divisor\nmeeting $D$ hidden in this product comparison.\n','', 'push:src:B.4.21','The full explicit product charts and all exceptional branches remain.')
edit('The remaining issue is the global closing, which the Kato\nformula determines exactly.  In its blowdown coordinate $x$','The Kato formula determines the global closing. In its blowdown coordinate $x$','push:src:B.4.21','Directly introduce the retained exact closing calculation.')
edit('are additional local completion charts; their attachment\nto a complementary global Kato piece has not been established.','are additional local completion charts.','push:src:B.4.22','Remove an unproved-construction report; retain only the proved local charts, with no global attachment claim.')
edit('There is also a deformation obstruction which does not\nassume a particular plumbing. Suppose a smooth complex','For the deformation obstruction, suppose a smooth complex','push:src:B.4.23','Start from the exact existing quantified fourfold/base-map hypotheses.')
edit('$r\\ne0$ surface fibres. The conclusion uses the specified complementary Kato component,\nits conductor-disjoint curve and the displayed holomorphic base map.','$r\\ne0$ surface fibres.','push:src:B.4.23','The three exact hypotheses remain stated immediately before the conclusion.')
edit('context. No classification of all central curves is used.','context.','push:src:B.4.23','Keep the complete marked-intersection argument; remove disclaimer.')
edit('model. This use of their proper-model theorem does\nnot require polarization.','model.','push:src:B.4.24','The exact nondegenerate log-torus hypotheses and cited proper-model theorem remain.')
edit('[A one-eigenvalue Hopf boundary has no proper analytic completion]','[Noncompletion of a one-eigenvalue Hopf boundary]','push:src:B.4.25','Shorten title to keep its tag on the statement heading.')
edit('contraction. The conclusion applies to the indicated Hopf family with its two\nspecified multipliers.','contraction.','push:src:B.4.25','The two specified multipliers and their orders remain in the statement.')
edit('bivector automorphy, with no choice of Picard convention.','the displayed bivector automorphy.','push:src:B.4.25','Retain the exact coefficient equation; remove disclaimer.')
old=r'''\item The local extensions agree on overlaps because
they agree on the ordinary locus. To see uniqueness
without a compactification assumption, lift locally
to log characters; agreement there is an equality
up to a locally constant $Y$-period, and that
meromorphic equality extends across the axis.
We have therefore obtained sections
$h_q$ of $\mathcal A$ on $B_q$ and $h_r$ on
$B_r$. The change between the two origins for
each point is $F$, so on $U$
\begin{equation}
 h_q-h_r=dF
\label{pub:I:eq:B-4-26-3}
\end{equation}
up to the harmless overall choice of subtraction
convention. The ghost proof of \ref{push:src:B.4.24} forbids
\eqref{pub:I:eq:B-4-26-3}: its $r$-loop $Y$-component is
$d\gamma\ne0$. Thus no such finite multisection
can exist.'''
new=r'''\item The local extensions agree on overlaps because
they agree on the ordinary locus. Lift locally to log characters:
agreement there is an equality up to a locally constant $Y$-period,
and that meromorphic equality extends across the axis.
We have therefore obtained sections $h_q$ of $\mathcal A$ on
$B_q$ and $h_r$ on $B_r$.
To fix the sign, write $z_r=\zeta-\sigma$ for the cusp group
coordinate. The comparison map of \ref{push:src:B.4.18} gives the
rotating coordinate $z_q=\zeta-\sigma+F=z_r+F$.
Summing over the $d$ points, with multiplicity, therefore gives
\begin{equation}
 h_q-h_r=dF
\label{pub:I:eq:B-4-26-3}
\end{equation}
on $U$. The ghost proof of \ref{push:src:B.4.24} forbids
\eqref{pub:I:eq:B-4-26-3}: its $r$-loop $Y$-component is
$d\gamma\ne0$. Thus no such finite multisection can exist.'''
edit(old,new,'push:src:B.4.26','Replace the unspecified subtraction convention by the exact receiving coordinate map z_q=z_r+F and trace; displayed sign and nonzero ghost class are unchanged.',True)
edit('secondary Hopf surfaces; no primary marking is required.','secondary Hopf surfaces.','push:src:B.4.28','Retain the stated secondary-Hopf scope; remove repeated marking disclaimer.')
edit('To see this without an invariant-cycle theorem, remove','To prove this, remove','push:src:B.4.28','Retain the full explicit compact-core and annular-monodromy argument.')
edit('excludes every hyperbolic Inoue component. The\nargument uses the nearby torus, not a free-product\ndescription of the central fundamental group.','excludes every hyperbolic Inoue component.','push:src:B.4.28','Retain the complete nearby form-period contradiction and remove the unneeded alternative-method comparison.')
edit('There is no hidden edge-reflection monodromy. Subdivision','Subdivision','push:src:B.4.28','The preceding explicit unramified-cover extension and splitting remain; remove the epithet.')
edit('They concern the linear cohomology variation,\nnot the translated origin.\n','', 'push:src:B.4.29','The exact cohomology and connection pullbacks already state the proved content.')
edit('\\item There is even an unchanged absolute form','\\item The absolute form','push:src:B.4.29','Introduce the retained nonvanishing canonical form directly; adjust next clause below.')
edit('\\label{pub:I:eq:B-4-29-2}\n\\end{equation}\nIt descends under both Tate period actions,','\\label{pub:I:eq:B-4-29-2}\n\\end{equation}\ndescends under both Tate period actions,','push:src:B.4.29','Complete the same canonical-form sentence after removing the filler lead-in.')
edit('\\item \\emph{What a total differential would have to add.}','\\item \\emph{The horizontal term of an absolute differential.}','push:src:B.4.29','Replace speculative/process heading by the exact displayed differential term.')
edit('distinct central limits. A condition imposing\na regular extending affine connection or\nspecified absolute lifts could detect such\ngrowth, but it is additional data; properness\nand the invariant forms above do not supply it.','distinct central limits.','push:src:B.4.29','Remove speculative additional-condition prose; retain the exact essential-singularity example, two sequences, and all proved pullback identities.')
edit('Theorem~\\ref{push:src:B.4.30} proves its noncompletion, and','Proposition~\\ref{push:src:B.4.30} proves its noncompletion, and','push:src:B.4.19','Correct the referenced printed statement kind, Proposition22.54.')
edit('$q$. Theorem~\\ref{push:src:B.4.30} excludes completions of this fixed','$q$. Proposition~\\ref{push:src:B.4.30} excludes completions of this fixed','push:src:B.4.26','Correct the referenced printed statement kind, Proposition22.54.')
edit('\\citet[Theorem 1.1 and Proposition 2.3]{ViaclovskyLog2026},','\\citet[Theorem~1.1, p.~1, and Proposition~2.3, pp.~5--6]{ViaclovskyLog2026},','inv:B2.1','Reuse provenance actual-page receipt02 for Theorem1.1p1 andProposition2.3pp5–6; no new page-reading claim by this agent.')
now=datetime.datetime.now(datetime.timezone.utc).isoformat();g=dict(created_utc=now,input_sha256=sha(before),scope='Candidate11 actual-page findings. Minimal positive prose, title and statement-kind edits; one explicit coordinate/trace clarification. All labels/tags/equations preserved. Main source remains parent-owned.',patches=patches)
(E/'S6_SERIES_PUBLISH_I_candidate11_prose_guards.json').write_text(json.dumps(g,indent=2)+'\n')
ids=sorted({x for p in patches for x in p['statement_ids']});archive=[]
for lab in ids:
 try:ob=block(orig,lab)
 except ValueError:ob='Original label absent; see earlier consolidation record.'
 archive.append(dict(statement_id=lab,original_attached_block=ob,candidate11_complete_block=block(before,lab),proposed_complete_block=block(s,lab)))
(E/'S6_SERIES_PUBLISH_I_candidate11_prose_full_blocks.json').write_text(json.dumps(dict(created_utc=now,source_sha256=sha(before),original_sha256=sha(orig),blocks=archive),indent=2)+'\n')
(E/'S6_SERIES_PUBLISH_I_candidate11_prose_preview.tex').write_text(s)
print(json.dumps({'guards':len(patches),'affected_statements':len(ids),'proof_map_changes':sum(p['proof_change'] for p in patches),'ids':ids},indent=2))
