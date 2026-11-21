from pathlib import Path
import re,json,hashlib,datetime
base=Path('/workspace/scratch/653608133b22/work/agents/i_topology'); e=base/'editorial'
main=Path('/workspace/scratch/653608133b22/work/S6_SERIES_PUBLISH_I.tex')
original=main.read_text();s=original;patches=[]
def patch(old,new,reason,ids,math=False):
 global s
 n=s.count(old)
 if n!=1:
  pattern=re.escape(old); pattern=re.sub(r'(?:\\\s)+',r'\\s+',pattern)
  matches=list(re.finditer(pattern,s))
  if len(matches)==1:old=matches[0].group()
  else:raise ValueError((n,len(matches),old[:180]))
 assert s.count(old)==1
 patches.append(dict(id=f'I-topology8-{len(patches)+1:03}',old=old,new=new,reason=reason,statement_ids=ids,proof_change=math))
 s=s.replace(old,new,1)
def block(label):
 i=s.index('\\label{'+label+'}')
 b=s.rfind('\\begin{',0,i)
 en=s.index('\\end{proof}',i)+len('\\end{proof}')
 return s[b:en]
def prose(old,new,ids):patch(old,new,'State the same defined object, map, hypothesis or proved conclusion positively; no mathematical identification changes.',ids)
# Preserve the first B4.2 derivation in the check file; retain the gradient proof that later applications use.
b42=block('push:src:B.4.2')
a=b42.index('\\item Equip');b=b42.index('\\item We give an independent elementary')
alternative=b42[a:b]
(e/'S6_SERIES_PUBLISH_I_B42_alternative_specialization_proof.tex').write_text(alternative)
old=alternative+r'''\item We give an independent elementary
surjectivity argument. Put'''
new=r'''\item The surjectivity assertion also follows from
\cite[Theorem~5.1, p.~2226]{NO10}. We use the explicit neighbourhood
retraction needed in \cref{push:src:A.4.7,push:src:B.4.7}. Put'''
patch(old,new,'Keep the complete gradient retraction used by A4.7 and B4.7; move the separate logarithmic covering-space proof to the check file.', ['push:src:B.4.2'],True)
patch(r'''generates $\pi_1(W)=\pi_1(D)$.

\item For the last assertion''',r'''generates $\pi_1(W)=\pi_1(D)$. Restricting the retraction
$W\to D$ to $Y_t$ gives the asserted continuous specialization
and its surjection on fundamental groups.

\item For the last assertion''','Make explicit the specialization map supplied by the retained complete proof.',['push:src:B.4.2'],True)
# A4.5 is only a restatement of A4.7-A4.9. Move a short numbered summary after those proofs.
a45=block('push:src:A.4.5')
(e/'S6_SERIES_PUBLISH_I_A45_duplicate_topology_summary.tex').write_text(a45)
meta=re.search(r'\\StatementRecord[^\n]*',a45).group()
remark=r'''\begin{remark}[Topology determined by the fan data]\hypertarget{tag-02ZV}{}\label{push:src:A.4.5}\label{push:A45}
'''+meta+r'''
For an output of Theorem~\ref{push:src:A.2.4},
Theorem~\ref{push:src:A.4.7} computes the Euler number, fundamental
group and nearby Euler function, and Theorem~\ref{push:src:A.4.8}
gives all integral homology groups and the marked monodromy.
Proposition~\ref{push:src:A.4.9} identifies the integral maps in the
normalization calculation through its direct-image splitting and
unit exceptional-fibre diagonals. All these calculations use the
same marked cone data.
\end{remark}'''
patch(a45,'','Replace the duplicate two-step restatement by a numbered summary remark after the three results it cites; preserve all anchors in the insertion guard.',['push:src:A.4.5'],True)
needle='\\section{Local limits and the global component obstruction}\\hypertarget{tag-02Z4}{}\\label{push:section:B}'
patch(needle,remark+'\n\n'+needle,'Place the concise topology summary after A4.7-A4.9, preserving its labels and tag.',['push:src:A.4.5'],True)
# Precise local references and titles.
prose(r'\subsection{Period transport and the actual parameter descent}',r'\subsection{Period transport and parameter descent}',['night:P2.1'])
prose('simple closed curve. The strict global maximum in \\cref{fam:src:C.1.1}, \\cref{fam:src:C.2.3}, including the\nindependent certificate in Part E.4, gives a uniform gap on the','simple closed curve. The strict global maximum in\nTheorem~\\ref{fam:src:C.2.3} gives a uniform gap on the',['push:src:D.4.1'])
prose('having finitely many cones modulo the periods. Here $n=1$\ngives Part A, and $n=2,12$ give the two cases of B.2.','having finitely many cones modulo the periods. The minimal subdivisions\nfor $n=1,2,12$ are described in Proposition~\\ref{push:src:A.2.1}\nand Theorem~\\ref{push:src:B.2.1}.',['push:src:A.2.4'])
prose('[the pointwise nearby Euler function]','[The pointwise nearby Euler function]',['push:src:A.4.3'])
prose('[limitation of Clemens--Schmid]','[Non-K\\"ahler models and the monodromy weight filtration]',['push:src:A.4.4'])
prose(r'\subsection{4 supplement. A Hodge obstruction to the central strata}',r'\subsection{A Hodge obstruction to the central strata}',['push:src:B.4.3'])
prose(r'Proposition~\ref{push:src:B.4.2} gives a surjection',r'Theorem~\ref{push:src:B.4.2} gives a surjection',['push:src:B.4.3'])
prose('[No log-torsor repair by point blowups]','[Logarithmic torsors under point blowups]',['push:src:B.4.27'])
# Exposed comparison of complete arguments; remove production/defensive clauses.
prose('\\item For completeness its graph is analytic and proper without an\nappeal to an unproved extension of a punctured graph. In a local','\\item Its graph is analytic and proper by the following local\nconstruction. In a local',['night:P2.4'])
prose('This equality is an equality of maps over the punctured disc,\nnot just a fibrewise biholomorphism statement.','Thus the two maps agree over the punctured disc.',['night:P2.4'])
prose('After a local finite root in the base, each horizontal component inherits this zero class from its global preimage; we do not assume that the local component itself is global.','After a local finite root in the base, each horizontal component inherits this zero class from its global preimage.',['night:P2.6'])
prose('\\item A proposed filling pulls back properly','\\item A proper filling pulls back properly',['night:P2.7'])
prose('gives the implication back to every proposed cover.','gives the implication back to every finite parameter cover.',['night:P2.9'])
prose('already excludes the proposed holomorphic proper extension.','already excludes a holomorphic proper extension.',['push:src:D.3.2'])
prose('is an identification of normalizations, not just a birational map.','identifies the normalizations.',['fam:src:E.1.3'])
prose('at $0,1$; smoothness of $S$, rather than smoothness of those fibres,\nis what the argument uses.','at $0,1$, since the argument uses smoothness of $S$.',['push:src:A.1.2'])
prose('exactly its orbit relation. It is therefore a biholomorphism,\nnot just a meromorphic comparison.','exactly its orbit relation. It is therefore a biholomorphism.',['push:src:A.1.2'])
prose('\\item We retain the actual product presentations, which also specify the\ncomparison with the surfaces in the stated problem. Let','\\item The following product presentations specify the comparison\nwith the marked central surfaces. Let',['fam:src:E.2.1'])
prose('with the given signs, rather than abstract surface isogenies.','with the stated signs.',['fam:src:E.2.1'])
prose('passes all three tests. Thus the procedure is a finite,\nexhaustive search at every height, rather than a restriction\nto regular triangulations or to new rays in a chosen orbit.\nThere is no projectivity condition in the tests.','passes all three tests. Thus the search at each height is finite,\nand the procedure is exhaustive.',['push:src:A.2.4'])
prose('\\item The finite-orbit condition is necessary for a proper quotient\nof such a refinement, not an additional restriction on the\nrequested proper models.','\\item Properness of the quotient forces the finite-orbit condition.',['push:src:A.2.4'])
prose('an actual proper modification of the base-changed compact\nnodal family, not a gluing inferred from a vanishing theorem.','a proper modification of the base-changed compact nodal family.',['push:src:A.2.4'])
prose('This also specifies all gluing maps, rather than only their\ncombinatorial incidence: they are the original period maps','The gluing maps are the original period maps',['push:src:A.2.4'])
prose('punctured family. No meromorphic extension of an arbitrary\npunctured isomorphism is needed here.','punctured family.',['push:src:A.2.4'])
prose('For every finite fan certificate $\\Sigma$','For every finite fan datum $\\Sigma$',['push:src:A.2.5'])
prose('This algorithm allows blow-downs; no toric\nstrong-factorization assertion is used.','The algorithm uses both blow-ups and blow-downs.',['push:src:A.2.5'])
prose('the reduced normal-crossings notion of d-semistability\nis not asserted for it.','the stated d-semistability conclusion applies to the reduced case.',['push:src:A.2.5'])
prose('describes centres and order, not merely a claim that\nsome birational map exists.','specifies the centres and their order.',['push:src:A.2.5'])
prose('There is no assertion that all these distinct\ncomponents are modifications of a single copy of $R$.\n','',['push:src:A.2.5'])
prose('This statement needs no projectivity or K\\"ahler hypothesis.\n','',['push:src:A.3.1'])
prose('Remark 5.9 of \\cite{FG10}; those scheme statements alone would\nnot justify omitting the analytic comparison above.','Remark 5.9 of \\cite{FG10}.',['push:src:A.3.1'])
prose('curve and zero off it; its integral is zero. This is an actual\nproper-flat smoothing of $Q$, but is not Engel\'s family.','curve and zero off it; its integral is zero. Thus this proper flat\nsmoothing has Euler number zero, whereas the fibres of Engel\'s\nfamily have Euler number two by Theorem~\\ref{push:src:A.3.2}.',['I:Euler-zero-pinching-smoothing'])
prose('The assertion that the two natural\nfillings exhaust smooth-total-space reduced-normal-crossings\nfillings is false, even when joint flatness over\n$B\\times\\Delta$ is imposed. There are infinitely many such\nfillings of the same punctured untwisted family. The\ntwo-model classification in \\ref{push:src:A.2.1} is a classification of the\nspecified minimal toroidal refinements, not of all fillings.','There are infinitely many fillings of the same punctured untwisted\nfamily with smooth total space, reduced normal-crossings central\ndivisor and joint flatness over $B\\times\\Delta$. The two-model\nclassification in Proposition~\\ref{push:src:A.2.1} concerns the minimal\ntoroidal refinements.',['push:src:A.3.3'])
prose('\\item We give centres that preserve joint flatness, rather than\nblowing up a point over a point of the two-dimensional base.','\\item The following centres preserve joint flatness.',['push:src:A.3.3'])
prose('isomorphism as fillings. The local substitutions and the\nsection-doubling calculation are exact computations, recorded\nwith the other local checks.','isomorphism as fillings.',['push:src:A.3.3'])
prose('Its integral is one. In particular the assertion that the\npointwise value on the smooth part of $S_\\infty$ is zero\nis false; its integrated contribution is zero.','Its integral is one. The smooth part of $S_\\infty$ has\nEuler number zero, so its integrated contribution is zero.',['push:src:A.4.3'])
prose('The classical K\\"ahler or projective Clemens--Schmid\ncomparison cannot be applied to these untwisted models.\nTheir smooth fibres have $b_1=1$ and are not K\\"ahler.','The smooth fibres of these untwisted models have $b_1=1$ and\nadmit no K\\"ahler metric.',['push:src:A.4.4'])
prose('weights $2,3,4$. This is a filtration of the computed\nmonodromy representation; we do not identify it with\na polarized limiting mixed Hodge structure.','weights $2,3,4$.',['push:src:A.4.4'])
prose('Its graded dimensions are the asserted ones. These\ntopological computations replace, rather than assume,\nthe inapplicable K\\"ahler comparison.','Its graded dimensions are the asserted ones.',['push:src:A.4.4'])
prose('The higher integral homology of every arbitrary output is\nnot asserted by this theorem.','The full integral homology is given by Theorem~\\ref{push:src:A.4.8}.',['push:src:A.4.7'])
prose('This is also a direct integral calculation of all the\nmaps needed below; it uses no degeneration theorem.','This computes all integral maps needed below.',['push:src:A.4.8'])
prose('are allowed in this preparatory step. Thus we do not\nassume that strictification preserves the punctured\n$r$-family.','are included in this preparatory step and in the comparison of\nthe punctured $r$-families.',['push:src:A.4.8'])
prose('\\item There is no invocation here of a general relative\nanalytic weak-factorization theorem. The complexes in\nquestion are finite. The cited combinatorial\nfactorization applies to them; the analytic','\\item The complexes are finite, so the cited combinatorial\nfactorization applies. The analytic',['push:src:A.4.8'])
prose('\\item Every original output, unlike temporary intermediate\nfactorizations, agrees with the marked family','\\item Every output agrees with the marked family',['push:src:A.4.8'])
prose('finite algorithm, not just the Euler characteristic.','finite algorithm.',['push:src:A.4.9'])
prose('\\item We construct the sheaf maps rather than infer a\nsplitting from fibre ranks. Let','\\item To construct the sheaf maps, let',['push:src:A.4.9'])
prose('This calculation concerns the stratified map of\ncentral spaces. It does not first calculate the\ncohomology of either ambient total neighbourhood.','This calculation concerns the stratified map of central spaces.',['push:src:A.4.9'])
prose('\\item Here is its explicit relation to the requested\nnormalization mapping cylinders. Resolve','\\item To compare this splitting with the normalization mapping\ncylinders, resolve',['push:src:A.4.9'])
prose('complex on those branches. No division by $s!$ is\nused; one uses alternating integral cochains, or','complex on those branches. Use alternating integral cochains, or',['push:src:A.4.9'])
prose('\\item We verify the horizontal-block assertion rather than\napply the pairwise criterion directly to its two\nconductor branches. By','\\item The horizontal-block comparison follows from the cohomology\nof its base curve. By',['push:src:B.4.6'])
prose('on the proposed interface.  It does not assert an obstruction\nfor arbitrary singular, non-flat, or higher-dimensional\ninterface networks.','on the interface.',['push:src:B.4.8'])
prose('This explains why the candidate axis has good reduction.\nNo claim is made that an arbitrary filling is obliged\nto contain this particular axis or normal factor.','This proves good reduction for this axis.',['push:src:B.4.8'])
prose('\\item We finally compute the actual affine class rather\nthan infer it from these linear monodromies.  Retain','\\item We compute the affine class using',['push:src:B.4.9'])
prose('Thus this construction does\nnot contradict \\ref{push:src:B.4.8}: the marked divisor used to change the normal\nline fails to extend.','The marked divisor used to change the normal line therefore\nfails the extension condition in Proposition~\\ref{push:src:B.4.8}.',['push:src:B.4.10'])
prose('calculation identifies an actual tubular line neighbourhood, not\nonly its first infinitesimal normal bundle.','calculation identifies a tubular line neighbourhood.',['push:src:B.4.10'])
prose('modifications if the proposed period permutes the collection','modifications if the period permutes the collection',['push:src:B.4.13'])
prose('a proposed deck\nmap has biholomorphisms','a deck map has biholomorphisms',['push:src:B.4.13'])
prose('\\item We check the actual cusp rather than assume that torsion fails.','\\item The infinite-order translation at the cusp is computed as follows.',['push:src:B.4.13'])
prose('by the actual $\\mu(z)$. We make neither a product assumption\nnor a torsion assumption on that line bundle. The formula','by $\\mu(z)$. The formula',['push:src:B.4.15'])
prose('\\item Here the action extends to the entire twelve-cycle model,\nnot just to its smooth fibres. Each unfolded normalization','\\item The action extends to the entire twelve-cycle model.\nEach unfolded normalization',['push:src:B.4.15'])
prose('using the actual semiabelian marking of B.1.','using the semiabelian marking of Proposition~\\ref{push:src:B.1.1}.',['push:src:B.4.15'])
prose('here, without assuming that the smooth two-tori are\nprincipal elliptic bundles. The invariant ideals show','here. The invariant ideals show',['push:src:B.4.15'])
prose('For self-crossings one uses the ordered local-branch\ndual complex, so no identification of distinct local\nbranches is silently discarded.','For self-crossings the ordered local-branch dual complex records\nevery local branch and its global identifications.',['push:src:B.4.16'])
prose('and the corrected punctured cusp of','and the punctured cusp of',['push:src:B.4.19'])
prose('with their retained markings.','with their given markings.',['push:src:B.4.19'])
prose('exactly as in \\ref{push:src:B.3.2}. No claim about the missing\ncusp point of the central divisor is implicit here.','exactly as in \\ref{push:src:B.3.2}.',['push:src:B.4.19'])
prose('\\emph{The corrected cusp overlap, including $r=0$.}','\\emph{The cusp overlap, including $r=0$.}',['push:src:B.4.19'])
prose('The actual-to-rotating\ncomparison of the corrected positive-deck model','The cusp-to-rotating comparison of the positive-deck model',['push:src:B.4.19'])
prose('central Kato surface still has degree $-1$, rather than $-12$.','central Kato surface has degree $-1$.',['push:src:B.4.21'])
prose('The construction has regularized the actual meromorphic\nfunction, rather than just its normal restriction.','Thus the modification makes the meromorphic function $H$\nholomorphic on this neighbourhood.',['push:src:B.4.21'])
prose('in characters, rather than infer it from the normal line.','in the following characters.',['push:src:B.4.21'])
prose('same local cyclic-cover count used earlier for\neach of the two actual cusp triple points; it\nis not a new global Euler count.','local cyclic-cover count at each cusp triple point.',['push:src:B.4.22'])
prose('\\item The equation arises from the actual repaired\nneighbourhood of','\\item The equation arises from the modified neighbourhood of',['push:src:B.4.22'])
prose('old node chart and $H=h/q$ is holomorphic in the\nrepaired collar.','node chart before modification, and $H=h/q$ is holomorphic\nin the modified collar.',['push:src:B.4.22'])
prose('Putting $g=f+r$ gives $X_n$. Thus the retained\n$q$ factor has been derived from the actual\nmeromorphic function regularized by the\nmodification, rather than inferred solely from\nan abstract normal-line isomorphism.\nMore precisely, the actual repaired collar, where $H$ is small,','Putting $g=f+r$ gives $X_n$, including its factor $q$.\nThe modified collar, where $H$ is small,',['push:src:B.4.22'])
prose('The intersection section in the repaired family is therefore','The intersection section in the modified family is therefore',['push:src:B.4.23'])
prose('function is a non-zero-divisor. No vertical component\nwas retained which could invalidate that assertion.','function is a non-zero-divisor on this dominating component.',['push:src:B.4.25'])
prose('the actual log-torsor obstruction \\ref{push:src:B.4.24}, without\nassuming that the unknown cap is itself a log torsor.','the log-torsor obstruction of Proposition~\\ref{push:src:B.4.24}.',['push:src:B.4.26'])
prose('finite extension is unique. No assumption that the\nwhole finite cover is a coordinate-root cover is\nbeing made.','finite extension is unique.',['push:src:B.4.26'])
prose('on the circle bundle also for a nontrivial normal line;\na product normal bundle is not assumed.','on the circle bundle of the normal line.',['push:src:B.4.28'])
prose('a proper smooth semistable cap. This statement\ndoes not refute a separate extension theorem\nfor the difference of two sections which both\nextend holomorphically into the same cap.','a proper smooth semistable cap.',['push:src:B.4.29'])
prose('unipotent degeneration at issue, rather than\na constant elliptic factor.','unipotent degeneration stated above.',['push:src:B.4.29'])
prose('\\item This also excludes a meromorphic total\nextension, rather than only a holomorphic\none. If such an extension existed, let','\\item This also excludes a meromorphic total extension.\nIf such an extension existed, let',['push:src:B.4.29'])
prose('the smooth local rings. We do not infer that its central\nmultiplicities remain one.','the smooth local rings; all central multiplicities are kept in the\nlocal monomial equations.',['push:src:B.4.31'])
prose('No assertion of reducedness after graph resolution and no\nsemistable-reduction theorem is needed for this step.','The argument uses the monomial equations with their displayed\npositive multiplicities.',['push:src:B.4.31'])
prose('generators. This proves a finite orbit in the actual lattice,\nnot merely a finite orbit of abstract stratum labels.','generators. This proves a finite orbit in the marked lattice.',['push:src:B.4.31'])
prose('gives a principal-bundle extension failure in codimension two and leaves general relative compactification open in that example.','gives a principal-bundle extension failure in codimension two.',['I:elliptic-bundle-primary-comparisons'])
prose('No K\\"ahler hypothesis is needed.\n','',['push:src:B.4.2'])
prose('Consequently a stratum of cone dimension $d$ is an actual\n$(\\mathbb C^*)^{4-d}$, with no additional torus quotient.','Consequently a stratum of cone dimension $d$ is\n$(\\mathbb C^*)^{4-d}$.',['push:src:A.4.7'])
prose('together with an actual\nperiod-frame identification.','together with a\nperiod-frame identification.',['push:src:B.4.19'])
prose('gives an\nactual projective bundle','gives a\nprojective bundle',['push:src:B.4.15'])
prose('factor identify this interface and its line with\nthe actual ones.','factor identify this interface and its line with\nthe cusp interface and its normal line.',['push:src:B.4.20'])

prose('cover.  Subtraction of the actual two origins fixes both deck','cover. Subtraction of the two origins fixes both deck',['series:I:F'])
prose("\\item\\hypertarget{step-I-F-2}{} Resolve a proposed filling's", "\\item\\hypertarget{step-I-F-2}{} Resolve a proper filling's", ['series:I:F'])
prose('actual cross-cocycles vanish.  The three unipotent annihilator','cross-cocycles vanish. The three unipotent annihilator',['series:I:F'])

# Remove the workflow epithet only within the assigned visible mathematical spans.
# Every remaining noun, variable, defining formula and map is unchanged.
spans=[]
for begin,end in [('\\hypertarget{main-I-F}{}','\\hypertarget{main-I-G}{}'),('\\hypertarget{main-I-G}{}','\\end{maintheorem}'),('\\subsection{Period transport and parameter descent}','\\section{Local limits and the global component obstruction}'),('\\begin{theorem}[Fundamental-group obstruction]','\\end{proof}')]:
 i=s.index(begin);j=s.index(end,i+len(begin))
 if begin.startswith('\\hypertarget{main-I-G}') or begin.startswith('\\begin{theorem}[Fundamental'):j+=len(end)
 spans.append((i,j))
i=s.index('\\label{push:src:B.4.3}');i=s.rfind('\\begin{theorem}',0,i)
j=s.index('\\label{push:src:B.4.32}');j=s.index('\\end{proof}',j)+len('\\end{proof}')
spans.append((i,j))
changes=[]
for a,b in spans:
 for m in re.finditer(r'(?m)^.*\bactual(?:ly)?\b.*$',s[a:b]):
  line=m.group()
  if line.lstrip().startswith(('\\Uses','\\StatementRecord','%')):continue
  new=line.replace('actual-to-rotating','cusp-to-rotating')
  new=re.sub(r'\ban actual\s+(?=[aeio][A-Za-z])','an ',new)
  new=re.sub(r'\ban actual\s+','a ',new)
  new=re.sub(r'\bactual(?:ly)?(?:[ \t]+|$)','',new)
  new=new.replace('Actual ','')
  if new!=line:changes.append((a+m.start(),line,new))
for _,old,new in sorted(changes,reverse=True):
 # Minimal line guards, enlarged by one preceding line only if necessary.
 if s.count(old)!=1:
  i=s.find(old);prev=s.rfind('\n',0,max(0,i-1))+1
  old=s[prev:i]+old;new=s[prev:i]+new
  if s.count(old)!=1:raise ValueError(('ambiguous actual line',old))
 pos=s.index(old)
 owners=list(re.finditer(r'\\begin\{(?:maintheorem|theorem|lemma|proposition|corollary|definition|remark)\}',s[:pos]))
 owner_start=owners[-1].start() if owners else 0
 lab=re.search(r'\\label\{([^}]+)\}',s[owner_start:pos])
 owner=lab.group(1) if lab else 'assigned-section-prose'
 patch(old,new,'Remove the workflow epithet actual/actually. The same explicitly defined mathematical object, marking and map is referred to before and after.',[owner],False)
# Anchor preservation is checked on the complete sequence, including the moved remark.
for pattern,name in [(r'\\label\{([^}]+)\}','labels'),(r'\\hypertarget\{([^}]+)\}','hypertargets')]:
 assert sorted(re.findall(pattern,original))==sorted(re.findall(pattern,s)),name
out=dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),input_sha256=hashlib.sha256(original.encode()).hexdigest(),patches=patches,scope='Final residual inspection of assigned F/G, period transport, boundary, untwisted-limit and B4 material. Exposed source comparison only; no independent proof or computation credit.')
(e/'S6_SERIES_PUBLISH_I_residual_batch8_guarded.json').write_text(json.dumps(out,indent=2)+'\n')
(e/'S6_SERIES_PUBLISH_I_residual_batch8_before.tex').write_text(original)
(e/'S6_SERIES_PUBLISH_I_residual_batch8_preview.tex').write_text(s)
print(json.dumps({'guards':len(patches),'actual_epithet_guards':len(changes),'proof_change_guards':sum(p['proof_change'] for p in patches),'input_sha256':out['input_sha256'],'preview_sha256':hashlib.sha256(s.encode()).hexdigest(),'net_characters':len(s)-len(original)},indent=2))
