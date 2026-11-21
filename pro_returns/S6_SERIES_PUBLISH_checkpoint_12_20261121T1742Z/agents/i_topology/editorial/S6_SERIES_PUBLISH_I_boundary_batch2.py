from pathlib import Path
import re,json,hashlib,datetime
P=Path(__file__).resolve().parent;initial=(P/'S6_SERIES_PUBLISH_I_boundary_batch1_preview.tex').read_text();s=initial;patches=[];archive=[]
def patch(id,old,new,why,ids=[]):
 global s
 assert s.count(old)==1,(id,s.count(old),old[:90]);patches.append(dict(id=id,old=old,new=new,reason=why,statement_ids=ids));s=s.replace(old,new,1)
def block(lab):
 i=s.index('\\label{'+lab+'}');a=s.rfind('\\begin{',0,i);b=s.index('\\end{proof}',i)+len('\\end{proof}');return s[a:b]
def proof(bl):return bl[bl.index('\\begin{proof}'):]
# The common meridian calculation applies to the exact fixed partial model.
b430=block('push:src:B.4.30');archive.append({'statement_id':'push:src:B.4.30','original_block':b430})
head=b430[:b430.index('\\begin{proof}')]
head=head.replace('[the fixed partial filling cannot be completed]','[Noncompletion of the fixed partial filling]')
a=head.index('\nThis is a statement about');z=head.index('\\end{proposition}',a);head=head[:a]+'\n'+head[z:]
newproof=r'''\begin{proof}
\begin{enumerate}[label=\arabic*.,leftmargin=*]
\item Every finite coordinate-root cover is dominated by one with $q=Q^{12m}$ and $r=R^n$, where $m,n>0$; proper pullback reduces to this case. Suppose such a completion exists. Retain and normalize its reduced dominating component, resolve it, and principalize the inverse image of the two axes, as in the proof of Theorem~\ref{night:P2.7}. These proper modifications preserve the given family on the complement of the axes and the smooth open parts of the two prescribed axial models. The resulting proper map to the bidisc has connected fibres: its finite Stein factor is generically one sheet and the bidisc is normal.

\item We identify the axial markings with the standard specialization of Theorem~\ref{night:P2.3}, namely $(l_0,l_1,l_2)=(0,1,-1)$ and $a=b=1$. In the notation of Proposition~\ref{push:src:B.4.24}, one has $U=-12\kappa_0$. The two origins in Theorem~\ref{night:P2.3} equal the two origins there plus $6ve$, where $e=\Pi_c\widehat\delta=(0,1)^{\mathsf t}$. Translation by $6ve$ acts on the character $W$ as $W\mapsto r^{-6}W$. It shifts the twelve-chain index by six and extends, with its inverse, across the parameter axis; along the cusp axis $r\ne0$ it is multiplication by a holomorphic unit. Thus this is an explicit comparison of the prescribed axial models. It changes meridian labels only by multiples of $\widehat\delta$ and leaves their $\widehat\gamma$ coefficients unchanged.

\item In the commuting lifts of Theorem~\ref{night:P2.7}, an axis component has orders $(\alpha_i,\beta_i)$ and $\widehat\gamma$ meridian coefficient $\kappa_i$. The same group calculation gives
\[
 (m\alpha_i+n\beta_i)\kappa_j
 =(m\alpha_j+n\beta_j)\kappa_i
\]
for intersecting components. Every denominator $m\alpha_i+n\beta_i$ is positive, including for exceptional components over the origin. Hence the ratio $\kappa_i/(m\alpha_i+n\beta_i)$ is constant on the incidence graph of components meeting the corner.

\item The prescribed parameter-axis model has an extending ordinary origin. Its positive parameter loop has zero lattice label in that origin, so the strict parameter component has ratio zero. The prescribed cusp-axis origin has ratio $a=1$, by the exact covered origin formulas \eqref{eq:P2FQ}--\eqref{eq:P2FR} and the commuting lift $Q_o=T_{-m\widehat\gamma}Q$. Both strict components meet the corner by properness. The compact connected corner fibre makes the incidence graph connected, exactly as in the proof of Theorem~\ref{night:P2.7}. Its ratios would therefore be both zero and one. This contradiction proves noncompletion for every pair of positive root degrees and for all additional corner components.
\end{enumerate}
\end{proof}'''
patch('I-topology2-01',b430,head+newproof,'Reuse the fully proved commuting-meridian argument for the identical fixed axial models, with the explicit6v-delta comparison; archive the second log-trace proof.', ['push:src:B.4.30'])
# Extending-section loops are sums of the already killed global component meridians.
b432=block('push:src:B.4.32');archive.append({'statement_id':'push:src:B.4.32','original_block':b432});head=b432[:b432.index('\\begin{proof}')]
head=head.replace('[vanishing of the global affine loop defect]','[Vanishing of the normalized radial-loop defect]')
head=head.replace('This conclusion controls a loop class; it does not assert\nthat $t-do$ is bounded or extends holomorphically at $r=0$.','')
newproof=r'''\begin{proof}
\begin{enumerate}[label=\arabic*.,leftmargin=*]
\item Use the smooth marked model of Theorem~\ref{night:P2.4} and remove the finitely many base values which are images of vertical central components or critical values of the maps on the central branch strata. Every central component above the remaining ordinary base dominates the original $\mathbb P^1$. Its positive normal meridian has zero lattice class in $\Lambda/\mathbb Z\widehat\delta$ by Theorem~\ref{night:P2.6}.

\item The ordinary origin is exactly the one used there. Indeed, write $k=\log K/(2\pi i)$ with $K=t^4/(t-1)^3$ and $v=\log r/(2\pi i)$. The parameter descent of Theorem~\ref{night:P2.1} is $H=-k$, so subtracting the local origin $vHe$, with $e=\Pi_c\widehat\delta$ gives the ordinary gauge $\widetilde\zeta=\zeta+kv e$ of Proposition~\ref{push:src:B.4.19}. On an overlap, $k$ changes by an integer, and the resulting radial label is an integral multiple of $\widehat\delta$. The finite-root cancellation and the cusp comparison in that proposition have the same property. Thus the splitting used in Theorem~\ref{night:P2.6} computes precisely the radial-loop defect relative to the stated ordinary origins.

\item For completeness, the connecting map is the endpoint period of a continued additive lift. With $T_r=I-mE$, $E=\widehat\delta\otimes\gamma$ and $E^2=0$, changing the lift adds $(T_r-I)\Lambda\subset\mathbb Z\widehat\delta$, so its image $\nu_r$ in $V$ is well defined. Under $r=R^e$ its label changes by
\[
 \sum_{j=0}^{e-1}T_r^jv
 =ev-\frac{me(e-1)}2Ev
 \equiv ev\pmod{\mathbb Q\widehat\delta}.
\]
Consequently the normalized defect of a section $b$ on that root cover is $e^{-1}\nu_R(b-o(R^e))$.

\item Lift an extending section to a common proper resolution. For a fixed ordinary base point the lift extends over the parameter origin: normalize the dominating curve in its proper graph, which has degree one over the disc. At its limit choose a normal-crossing chart in which
\[
 r=\text{unit}\prod_{i=1}^k x_i^{a_i},\qquad a_i>0.
\]
On the section, $x_i(R)=R^{b_i}u_i(R)$ with $u_i$ a holomorphic unit and $b_i\ge0$. Thus $e=\sum_i a_i b_i$, and its positive $R$-loop is the sum of $b_i$ positive component meridians. The unit loops contract in the chart. In the quotient presentation of Theorem~\ref{night:P2.6}, the lattice label is the same sum of the component labels, each zero modulo $\widehat\delta$. Hence the normalized radial defect is zero. This argument applies to every extending section and every root, and is preserved under common proper refinements. In a varying ordinary base chart the labels are locally constant, so the vanishing also holds across the isolated points where a simultaneous section lift has indeterminacy.

\item The connecting homomorphism is additive. Split a finite multisection after a cyclic root at a generic ordinary point, add the zero normalized defects of its branches, and use the preceding root formula. Its trace of degree $d$ therefore satisfies $\nu_r(t-do)=0$ in $V$. These zero local classes patch under the actual lattice transport, independently of the section and all choices. Finally, by the bounded-character presentation of Proposition~\ref{push:src:B.4.27}, a bounded logarithmic difference along the strict parameter axis has characters in $\mathcal O^*\times\mathcal M_r^{\mathrm{gp}}$: its first character has zero winding and its second contributes only a multiple of $\widehat\delta$. Adding it to a multiplied trace preserves the zero class. This proves every stated assertion.
\end{enumerate}
\end{proof}'''
patch('I-topology2-02',b432,head+newproof,'Consolidate the global section-loop argument with P2.6 using the explicit local normal-circle decomposition and exact finite-root normalization.', ['push:src:B.4.32'])
# Update the final interpretative step of the invariant-form counterexample.
b429=block('push:src:B.4.29');old=r'''\item The example compares two markings of the same
proper family. It does not identify either
with the actual six-sphere cap. Nor does it
show that differences of two sections both
extending into a single cap fail to extend:
a common essential translation cancels in
such a difference. The difference-extension bridge
is proved in \ref{push:src:B.4.30}; \cref{push:src:B.4.31,push:src:B.4.32,night:P2.7} add the global
meridian and loop control needed for the actual family.
They do not contradict this counterexample. Exact chart,
monodromy, and translation identities are
checked in
\path{code/e_push_forms_translation.py}.'''
new=r'''\item Both markings belong to the same proper family. Their relative invariant forms and their absolute canonical form agree by the displayed pullbacks, while the two limits of the translated zero section are distinct. A common translation cancels in a difference of two sections.'''
patch('I-topology2-03',old,new,'Keep the proved counterexample and its explicit comparison; remove the superseded proof-mechanism pointer and program narration.', ['push:src:B.4.29'])
# Replace unnumbered historical comparison essays by their actual proved example.
a=s.index('\\paragraph{Why automatic analytic comparison is not used.}');b=s.index('\\begin{proposition}[a parabolic analytic model',a);old=s[a:b];archive.append({'statement_id':'unnumbered-analytic-comparison-essay','original_block':old})
new=r'''\begin{remark}[A punctured isomorphism with an essential singularity]
\hypertarget{tag-PT03}{}\label{I:essential-punctured-isomorphism}
\StatementRecord{I:essential-punctured-isomorphism}{proved}{PT03}{}
The automorphism
\[
 (s,[z_0:z_1])\longmapsto(s,[e^{1/s}z_0:z_1])
\]
of $\Delta^*\times\mathbb P^1$ has no meromorphic extension across zero, although the two product families extend properly over the disc. Its restriction to the constant section $[1:1]$ is $[e^{1/s}:1]$, which has an essential singularity. The proper graph of a meromorphic extension, pulled back to this section and normalized in its dominating component, would give a holomorphic extension from the disc, a contradiction.
\end{remark}

'''
patch('I-topology2-04',old,new,'Retain the concrete comparison counterexample as a numbered remark; move research-process and unused-scope discussion to records.', ['I:essential-punctured-isomorphism'])
a=s.index('\\paragraph{Limits of automatic analytic comparison}');b=s.index('\\begin{proposition}',a);old=s[a:b];archive.append({'statement_id':'unnumbered-action-compactification-essay','original_block':old})
new=r'''\begin{remark}[The distinguished orbit on an ordinary torus]
\hypertarget{tag-PT04}{}\label{I:noncompactifiable-distinguished-orbit}
\StatementRecord{I:noncompactifiable-distinguished-orbit}{proved}{PT04}{}
The distinguished nonconstant orbit map $\mathbb C^*\to T^2$ on an ordinary torus has no meromorphic extension to $\mathbb P^1$. A meromorphic map from a smooth curve to a compact complex manifold extends holomorphically at its isolated indeterminacies, by normalization of its proper graph. A holomorphic map $\mathbb P^1\to T^2$ lifts to $\mathbb C^2$ and is constant. This contradicts the nonconstant orbit map.
\end{remark}

'''
patch('I-topology2-05',old,new,'Keep the proved orbit-extension obstruction, removing the long list of unused comparison hypotheses.', ['I:noncompactifiable-distinguished-orbit'])
# Remove repeated closing scope/program steps after reading their complete proofs.
for lab,marker,ident in [('push:src:B.4.24','\\item Finally, the cited proper-model theorem is a','I-topology2-06'),('push:src:B.4.27','\\item No step supplies a log-group presentation of','I-topology2-07')]:
 bl=block(lab);a=bl.index(marker);b=bl.rfind('\\end{enumerate}');new=bl[:a]+bl[b:]
 patch(ident,bl,new,'Remove a closing scope/program recap after the full mathematical proof; retain all equations and actual sheaf maps.',[lab])
# Retain the exact adjunction formula as a numbered mathematical remark.
a=s.index('\\paragraph{The separate canonical-model reduction}');b=s.index('\\subsection{What invariant forms do not control}',a);old=s[a:b]
new=r"""\begin{remark}[Vertical divisors and component adjunction]
\hypertarget{tag-PT05}{}\label{I:vertical-divisor-adjunction}
\StatementRecord{I:vertical-divisor-adjunction}{proved}{PT05}{}
For a proper semistable surface family with smooth total space and reduced simple normal-crossing central divisor $\sum_i V_i$, let a nonzero meromorphic relative two-form have vertical divisor $\sum_i a_iV_i$. Put $C_{ij}=V_i\cap V_j$ and $C_i=\sum_{j\ne i}C_{ij}$. Then
\[
 K_{V_i}+C_i\sim\sum_{j\ne i}(a_j-a_i)C_{ij}.\tag{B.4.28.11}
\]
Indeed, adjunction gives $K_{V_i}=(K_{\mathcal X/\Delta}+V_i)|_{V_i}$, while the principal total fibre gives $\mathcal O_{\mathcal X}(V_i)|_{V_i}\sim-C_i$. Restricting the divisor of the form yields the displayed equality.
\end{remark}

"""
patch('I-topology2-08',old,new,'Keep the proved adjunction identity and its exact divisor map; remove the unproved reduction proposal and superseded proof summary.', ['I:vertical-divisor-adjunction'])
a=s.index('\\paragraph{Scope of the affine comparison}');b=s.index('\\subsection{The radial-loop class',a)
patch('I-topology2-09',s[a:b],'','Remove the duplicate closing discussion and program narration after the global angular-meridian proof.', ['push:src:B.4.31'])
# No removed internal proof equation may remain as an operative citation.
for lab in ['push:src:B.4.30','push:src:B.4.32']:
 hits=re.findall(r'\\ref\{'+re.escape(lab)+r'\}\.[0-9]+',s)
 assert not hits,(lab,hits)
pat=r'\\label\{([^}]+)\}|\\hypertarget\{(tag-[^}]+)\}'
def anchors(t):return sorted(a or b for a,b in re.findall(pat,t))
a0=anchors(initial);a1=anchors(s);lost=[x for x in a0 if x not in a1];dups=[x for x in set(a1) if x in a0 and a1.count(x)>a0.count(x)];assert not lost,lost;assert not dups,dups
(P/'S6_SERIES_PUBLISH_I_boundary_batch2_guarded.json').write_text(json.dumps({'input_sha256':hashlib.sha256(initial.encode()).hexdigest(),'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'patches':patches,'anchor_check':{'lost':lost,'duplicates':dups,'new':[x for x in a1 if x not in a0]}},indent=2))
(P/'S6_SERIES_PUBLISH_I_boundary_batch2_preview.tex').write_text(s)
(P/'S6_SERIES_PUBLISH_I_boundary_batch2_archived_proofs.json').write_text(json.dumps(archive,indent=2))
print(json.dumps({'patch_count':len(patches),'removed_chars':len(initial)-len(s),'new_anchors':[x for x in a1 if x not in a0]},indent=2))
