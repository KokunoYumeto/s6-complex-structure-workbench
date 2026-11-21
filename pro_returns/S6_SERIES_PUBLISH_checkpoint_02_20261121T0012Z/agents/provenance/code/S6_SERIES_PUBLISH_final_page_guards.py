from pathlib import Path
import re,json,hashlib
root=Path('/workspace/scratch/653608133b22')
p=root/'work/S6_SERIES_PUBLISH_V.tex';s=p.read_text();original=s
changes=[]
def add(cid,label,page,old,new,defects=('D02',),reason='State the existing mathematical content directly; every displayed formula and proof operation is retained.'):
 global s
 start=s.index('\\label{'+label+'}')
 end=s.index('\\end{proof}',start)+len('\\end{proof}')
 scope=s[start:end]
 pat=r'\s+'.join(re.escape(w) for w in old.split())
 matches=list(re.finditer(pat,scope))
 assert len(matches)==1,(cid,label,len(matches),old)
 m=matches[0];actual=scope[m.start():m.end()]
 assert s.count(actual)==1,(cid,'global uniqueness',s.count(actual))
 changes.append({'id':cid,'page':page,'label':label,'defects':list(defects),'old':actual,'new':new,'reason':reason,'mathematical_check_event':False})
 s=s[:start+m.start()]+new+s[start+m.end():]
def globaladd(cid,page,old,new,defects,reason):
 global s
 assert s.count(old)==1,(cid,s.count(old))
 changes.append({'id':cid,'page':page,'label':None,'defects':list(defects),'old':old,'new':new,'reason':reason,'mathematical_check_event':False});s=s.replace(old,new,1)
add('p097_cutoff','maps:src:F.2.30',97,'No finite cutoff is imposed or needed.','')
add('p097_tuple_scope','maps:src:F.2.31',97,'No irreducibility, determinant-one, or three-connectivity hypothesis is imposed.','',reason='The immediately preceding hypotheses already range over every integral rank-six tuple satisfying the finite-order and primitive maximal-cusp conditions. No new restriction is introduced.')
add('p098_integral_sum','maps:src:F.2.31',98,'This is an integral sum, without saturation.',r'Every element of $L$ is a finite integral sum of elements of the subgroups $gU$.',reason='Preserve the exact subgroup L, explicitly as finite integral sums; no saturation or rational-span replacement is made.')
add('p098_cusp_relations','maps:src:F.2.31',98,'so it adds exactly these relations, with no extra meridian relation left unspecified.','so its filling imposes exactly these relations.')
add('p099_convention','maps:src:F.2.31',99,'Changing the transport convention causes no group ambiguity:','The opposite transport convention is related by the following explicit isomorphism:')
add('p099_hidden_relation','maps:src:F.2.31',99,r'This proves \eqref{maps:eq:F.G6}, including the absence of any further hidden fibre relation.',r'This proves \eqref{maps:eq:F.G6}.')
add('p100_smaller_cases','maps:src:F.2.31',100,'Thus no smaller case has been omitted within the hypotheses of this theorem.','')
add('p100_cusp_column','maps:src:F.2.31',100,'No cusp column was lost:','The inclusion')
add('p102_vertical_dependence','maps:src:F.2.32',102,r'This proves \eqref{maps:eq:F.LT2}, including the absence of any dependence on the vertical part of $v$.',r'This proves \eqref{maps:eq:F.LT2}; the presentation depends on $v$ only through $r=\ell(v)$.')
add('p102_torus_cohomology','maps:src:F.2.32',102,'There is no cohomology torsion in this torus cap.','The integral cohomology of this torus cap is free.')
add('p105_added_description','maps:src:F.2.33',105,r'Every higher perturbation followed by the horizontal homotopy lowers cyclic degree, so this added description changes neither the termination proof nor the $2^r$ generator bound.',r'Every higher perturbation followed by the horizontal homotopy lowers cyclic degree, proving termination with the $2^r$ generator bound.',('D01','D08'))
add('p106_gluing_constants','maps:src:F.2.34',106,r'The finite face identifications give \eqref{maps:eq:F.CK2}, so there are no further gluing constants in this fixed marked cap.',r'The finite face identifications give \eqref{maps:eq:F.CK2}.')
add('p106_AO_citation','maps:src:F.2.34',106,r'Achinger--Ogus, Theorem~4.1.1, identifies its topological germ with the mapping cylinder of this logarithmic collapse \cite[Theorem 4.1.1 and Lemmas 4.1.2--4.1.3, pp.~480--482]{ffAchingerOgus20}.',r'The logarithmic comparison theorem \cite[Theorem 4.1.1 and Lemmas 4.1.2--4.1.3, pp.~480--482]{ffAchingerOgus20} identifies its topological germ with the mapping cylinder of this logarithmic collapse.',('D18',))
add('p107_cusp_marking','maps:src:F.2.34',107,'It does not replace the cusp marking by another integral basis.','')
add('p107_cancellation_counts','maps:src:F.2.34',107,r'After respectively 2063, 4988 and 7087 such cancellations for the cap, boundary and collapse cone, Smith reduction gives \eqref{maps:eq:F.CK1}.',r'After cancelling unit pairs for the cap, boundary and collapse cone, Smith reduction gives \eqref{maps:eq:F.CK1}.',('D09',),'Operation counts 2063/4988/7087 remain in this exact before/after record and the original computational records. All chain ranks, differentials, reductions and invariant factors remain in the proof.')
add('p107_filtration','maps:src:F.2.34',107,'This computes the integral groups without a filtration extension problem.','This computes the integral groups.')
add('p108_outstanding','maps:src:F.2.35',108,r'We supply both global boundary maps which were left outstanding after \ref{maps:src:F.2.34}.',r'We construct both boundary maps for the global gluing.',('D01','D08'))
add('p109_resolution','maps:src:F.2.35',109,'In particular this one-edge model avoids an unnecessary periodic resolution of the seven-dimensional boundary.','')
add('p110_filtration','maps:src:F.2.35',110,'Consequently its cone computes integral homology directly; there is no remaining filtration extension to choose.','Consequently its cone computes integral homology.')
add('p110_cutoff','maps:src:F.2.35',110,'Word reductions and affine orbit enumerations are finite, with no imposed size cutoff.','Word reductions and affine orbit enumerations terminate.')
add('p111_unit_count','rem:V:orientation-reversing-gluing',111,r'Applying $7345$ integral unit cancellations to its gluing cone gives free ranks','Integral unit cancellation and Smith reduction of its gluing cone give free ranks',('D09',),'The operation count 7345 remains in this exact before/after record. Every homology rank, torsion group, Betti vector and Euler number remains in the remark.')
add('p111_entry_bounds','maps:src:F.2.36',111,'The algorithm does not impose a bound on their entries, on the affine multiplicities, or on the integral conjugator.','')
add('p111_primitive_scope','maps:src:F.2.36',111,r'with $N^2=0$ and $\operatorname{rank}N=3$; the primitive-image assumption is unnecessary for this statement.',r'with $N^2=0$ and $\operatorname{rank}N=3$.',reason='The general input class is already stated by the exact square-zero and rank conditions; omitting the defensive tail adds no hypothesis.')
add('p111_lucky_search','maps:src:F.2.36',111,'This is a terminating exact test, including the negative case, and not a search for a lucky invertible intertwiner.','This gives a terminating exact test for rational isomorphism.')
add('p112_BHJ_locator','maps:src:F.2.36',112,r'This proves hypothesis (H) of \cite[Algorithm 8.3, p.~21]{rootBHJ22} for every tuple under consideration.',r'This proves hypothesis (H) of \cite[hypothesis (H), p.~2; Algorithm~8.3, p.~21]{rootBHJ22} for every tuple under consideration.',('D18',),'Both primary locators were opened by the topology agent and are recorded in its source verification; distinguish the hypothesis page from the algorithm page.')
add('p113_conjugator','maps:src:F.2.37',113,r'The displayed candidate bound makes no assumption about entries of $P_T$; the terminating witness construction is the stated input from \cref{maps:src:F.2.36}.',r'The candidate bound depends on $H(T)$; \cref{maps:src:F.2.36} constructs the integral witness $P_T$.')
add('p114_entry_bounds','maps:src:F.2.38',114,'for every such input, without any bound on its entries.','for every such integral input.')
add('p115_factors','maps:src:F.2.38',115,r'There is no additional identification between the two factors, since an intertwiner of a trivial and a sign lattice is zero over $\mathbb Z$.',r'An intertwiner of a trivial and a sign lattice is zero over $\mathbb Z$, which proves independence of the two factors.')
add('p116_height','maps:src:F.2.39',116,'There is no fixed global height cutoff; the finite stopping bound','The finite stopping bound')
add('p116_affine_scope','maps:src:F.2.39',116,'The algorithms have no cutoff on affine orders, twist entries or lattice indices.','',reason='The preceding sentence already covers every choice of free affine orders, integer numerators, integral clutch vector and primitive cusp marking. No input is excluded.')
add('p117_chain_range','maps:src:F.2.39',117,r'maps of \ref{maps:src:F.2.33}--35 give',r'maps of \cref{maps:src:F.2.33,maps:src:F.2.34,maps:src:F.2.35} give',('D04','D06','D23'),'Replace the stale printed range 14.3–35 by the three actual finite-cap, cusp and global-gluing theorem numbers.')
add('p117_classification_range','maps:src:F.2.39',117,r'Finally \ref{maps:src:F.2.7}--30 prove both directions of the classification.',r'The results from \cref{maps:src:F.2.7} through \cref{maps:src:F.2.30} prove both directions of the classification.',('D04','D06','D23'),'The actual old source range is F.2.7–F.2.30; preserve both exact endpoints and render their current numbers/kinds.')
add('p121_kind','maps:src:F.3.11',121,r'Its integral version is Theorem \ref{maps:src:F.2.1}.',r'Its integral version is \cref{maps:src:F.2.1}.',('D23',),'F.2.1 is a Proposition (currently2.2), so use its automatic kind and number.')
add('p153_chain_values','maps:src:E.2.16',153,'These are values on chains, not assertions that all the displayed cells are cycles in the cover.',r'The tables give the chain map; its induced map on lifted peripheral homology is \eqref{maps:eq:E.C4}.')
add('p153_chain_comparison','maps:src:E.2.16',153,r'We first give the local chain comparison; the homology maps alone do not determine \eqref{maps:eq:E.C1}.',r'We give the local chain comparison underlying \eqref{maps:eq:E.C1}.')
add('p155_translation_prism','maps:src:E.2.16',155,'The linear three-torus return fixes its origin; hence there is no additional translation prism in this comparison.','The linear three-torus return fixes its origin.')
add('p156_independent_coefficient','maps:src:E.2.16',156,r'This also checks the ordinary coefficient independently: after taking $K$ coinvariants,', r'Taking $K$ coinvariants gives',('D07','D08'))
add('p157_norm_relation','maps:src:E.2.17',157,r'The degree-two norm $N_a$ in \eqref{maps:eq:E.P7} is written with the same expression as in \eqref{maps:eq:E.P3}, but here $a^3=h_1$, not $1$.',r'The degree-two norm $N_a$ in \eqref{maps:eq:E.P7} is the polynomial $1+a+a^2$ of \eqref{maps:eq:E.P3}, evaluated in $R$ with $a^3=h_1$.')
add('p159_central_quotient','maps:src:E.2.17',159,r'Thus the whole $14$-generator summand is a module over $S$, without imposing an additional quotient.',r'Thus the whole $14$-generator summand is a module over $S$.')
add('p159_readable','maps:src:E.2.17',159,r'For a readable final reduction, the $14$ generators separate into two seven-generator blocks.',r'The $14$ generators separate into two seven-generator blocks.',('D08',))
add('p160_recovery','maps:src:E.2.17',160,r'This is an independent recovery of \ref{maps:src:E.2.11}.',r'Taking coinvariants therefore gives the groups in \cref{maps:src:E.2.11}.',('D07','D08'))
add('p161_boundary_scope','maps:src:E.2.18',161,r'$E_0$, even without requiring the equivalence to preserve the boundary.',r'$E_0$.',reason='The statement already quantifies over every underlying homotopy equivalence, with no boundary condition. The full arbitrary-free-summand obstruction proof remains unchanged.')
add('p161_free_summands','maps:src:E.2.18',161,r'connected closed nine-manifold $Y_0$, despite the twenty-four free $\mathbb Z\Pi$ summands in \eqref{maps:eq:E.P6}.',r'connected closed nine-manifold $Y_0$.',reason='The 24 free summands remain stated and proved in E.2.17 and explicitly used in E.2.18 proof11–13; omit only the defensive reprise.')
add('p164_original','maps:src:E.2.19',164,'For the original marked cusp, let','For the marked cusp, let',('D08',))
add('p165_triple_clutching','maps:src:E.2.19',165,r'ordinary triple charts $q=z_0z_1z_2$, with no additional clutching loop at either triple point.',r'ordinary triple charts $q=z_0z_1z_2$ with trivial clutching around each triple point.')
add('p167_lattice_descent','maps:src:E.2.20',167,r'A lattice change of $\phi$ changes the base angle by $m_j\kappa_j$, and $B_j^{m_j}=I$, so it introduces no further ambiguity.',r'A lattice change of $\phi$ changes the base angle by $m_j\kappa_j$; the equality $B_j^{m_j}=I$ makes the map descend under this change.')
add('p170_planar_drawing','maps:src:E.2.21',170,'To fix their maps without a planar drawing, use the oriented ribbon','To fix their maps, use the oriented ribbon')
add('p170_affine_term','maps:src:E.2.21',170,'There is no affine term.','These gluing maps are linear.')
add('p172_q_trivialization','maps:src:E.2.21',172,'In particular no twisting of the $q$ disk is introduced on the six sector seams.',r'The $q$ coordinate therefore gives a common normal trivialization across the six sector seams.')
add('p173_top_handle','maps:src:E.2.21',173,'In particular a top handle keeps its entire attaching map, so no homotopy-sphere ambiguity arises.','Every top handle is attached by its prescribed full map.')
old=r'\begin{theorem}[A complete three-point logarithmic family]'
globaladd('p100_orphan_heading',100,old,'\\Needspace{5\\baselineskip}\n'+old,['D23'],'Keep the theorem heading with the opening statement; actual candidate p.100 had the heading alone.')
for cid,page,title in [('p152_orphan_section',152,'The homotopy module and the quadratic cusp attachment'),('p163_orphan_section',163,'Smooth plumbings and framed handles')]:
 old='\\section{'+title+'}'
 globaladd(cid,page,old,'\\Needspace{9\\baselineskip}\n'+old,['D14','D23'],'Keep the section heading and first statement with substantive opening text; actual candidate had both headings alone at the page bottom.')
# Every mathematical target and equation label remains. The only extra reference is existing E.C4.
for command in ['label','hypertarget']:
 assert set(re.findall(r'\\'+command+r'\{([^}]+)\}',original))==set(re.findall(r'\\'+command+r'\{([^}]+)\}',s)),command
q=root/'work/agents/provenance/S6_SERIES_PUBLISH_V_final_reading_editorial_guards.json'
q.write_text(json.dumps({'source':str(p),'source_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'candidate_pdf_sha256':'8b2d18bb43fedda842510e01967074589e0439c491fa3bb53928ab1d7eeedc2d','changes':changes,'status':'Guarded editorial/reference/layout proposals; main source unchanged. Every assigned candidate page was visually read.','mathematical_check_events_added':0},ensure_ascii=False,indent=2)+'\n')
print('guards',len(changes),'source_sha',hashlib.sha256(p.read_bytes()).hexdigest(),'path',q)
