from pathlib import Path
import json,hashlib,datetime,re
ROOT=Path.cwd(); D=ROOT/'agents/ii_checks_provenance/recovery_20261121T2000Z/clean_group13'
def bind(p):
 p=ROOT/p if not p.is_absolute() else p
 return {'path':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
def dump(name,obj):
 p=D/name;assert not p.exists(),p;p.write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n');return bind(p)
source=ROOT/'S6_SERIES_PUBLISH_II.tex';src=source.read_text(); targets=[]
for tag,owner in [('01CB','cdp:st:C.2.NC.4'),('01CC','cdp:st:C.2.NC.5')]:
 original=D/f'S6_SERIES_PUBLISH_II_{tag}_original.tex';text=original.read_text();assert src.count(text)==1
 guards=[]
 def add(typ,old,new,reason,n=1):
  global text
  assert text.count(old)==n,(tag,old,text.count(old),n)
  guards.append({'change_id':f'II-REC-C13-{tag}-{len(guards)+1:02}','defect_type':typ,'old':old,'new':new,'expected_occurrences_in_owning_block':n,'reason':reason})
  text=text.replace(old,new)
 add('D04,D23',r'\begin{enumerate}[label={$\langle1\rangle$\arabic*.},leftmargin=*]',r'\begin{enumerate}[label=\arabic*.,leftmargin=*]','Use ordinary proof-step numbering, preserving every step and all statement/equation tags.')
 if tag=='01CB':
  add('D06,D18',r'\cite[Theorem~2.2]{Peters2021}',r'\cite[Theorem~2.2, p.~843]{Peters2021}','Bind both occurrences to the exact opened journal classification table.',2)
  add('D06,D18',r'\cite[Theorem~3.2]{BMS2012}',r'\cite[Theorem~3.2, p.~16]{BMS2012}','Bind both occurrences to the exact 27 October 2011 author edition already identified in the bibliography.',2)
  add('D04,D06','(C.NC.6)',r'\eqref{cdp:eq:C.NC.6}','Replace the literal equation number by its exact existing current label.')
  add('D06,D18','A Kähler $T_i$ is consequently rational or a blown-up ruled surface.',r'By \cite[Theorem~2.2, p.~843]{Peters2021}, a Kähler $T_i$ is consequently rational or a blown-up ruled surface.','Credit the classification at its first mathematical use, with unchanged alternatives.')
  add('D08',' This derives all numerical classification facts used here from the cited statements.','','Remove the closing account of what the proof has accomplished; every classification input and numerical deduction remains.')
  add('D02',' This proof places no restriction on intersections between two local branches belonging to the same $S_i$.','','Remove the defensive scope sentence. The actual restriction j≠i, distinct global component S_j, and empty-intersection conclusion remain exactly in the preceding argument; self-intersection branches are not excluded.')
  add('D04,D06','(C.NC.4)',r'\eqref{cdp:eq:C.NC.4}','Use the exact current coherent-Euler equation label.',2)
  add('D13','The weighted Euler formula now reads',r'The nearby Euler function is $m_i$ along the smooth part of $S_i$. At a double crossing the local map is $x^{m_i}y^{m_j}$; its transverse nearby fibre is a disjoint union of annuli and has Euler number zero. Euler integration gives $e(Y_t)=\sum_i m_i e(T_i\setminus D_i)$. Since $e(D_i)=0$, this is','Supply the local single-branch degree and double-branch annulus maps underlying the printed weighted formula, including self-double branches and unequal multiplicities. The displayed weighted equation is unchanged.')
  add('D04,D06','(C.NC.5)',r'\eqref{cdp:eq:C.NC.5}','Use the exact current topological-Euler equation label.')
  add('D08','This proves the final assertion and also proves that any triple point lies on an irreducible support with rational normalization.','Thus any triple point lies on an irreducible support with rational normalization.','Retain the mathematical conclusion and remove the closing proof-status announcement.')
 else:
  add('D02','The scheme-theoretic fibre may be a multiple of $S$; this conclusion does not assert that its multiplicity is one.','The scheme-theoretic fibre may be a multiple of $S$.','Retain the positive multiplicity scope and remove its redundant defensive restatement; the proof still explicitly treats mS.')
  add('D06,D13','A smooth support has Euler number zero directly from (C.NC.1).','A smooth support is connected and irreducible, so the same uniform-multiplicity formula gives Euler number zero.','Replace the unresolved literal locator by the exact application of the already cited uniform-multiple proposition; smooth support has τ=0.')
  add('D02,D08',r'\ref{cdp:st:C.3.5} proves the required zero Euler number for every smooth fibre under the CDP hypotheses, so that application uses no assumption that the general fibre is a torus.',r'Under the CDP hypotheses, \ref{cdp:st:C.3.5} gives Euler number zero for every smooth fibre.','State the exact positive CDP input and retain its full smooth-fibre scope.')
  add('D13',r'its rational first Chern class is zero, and the injectivity and torsion-freeness used in \ref{cdp:st:C.2.NC.4} apply.',r'its rational first Chern class is zero, and the exponential sequence identifies $\Pic(T)$ with the torsion-free group $H^2(T,\Z)$ by the first Chern class, as in \ref{cdp:st:C.2.NC.4}.','Write the actual Picard-to-integral-cohomology map that turns rational Chern-class vanishing into triviality.')
  add('D13',r'The injection of torsion-free differentials into normalization differentials gives',r'The differential pullback has kernel $\operatorname{Tor}(\Omega_S^1)$ and induces $\widetilde\Omega_S^1\hookrightarrow\eta_*\Omega_T^1$. Tensoring by $A$ and applying the projection formula gives','Specify the exact quotient and normalization map used for the vanishing of sections.')
  add('D13',r'The canonical normal-crossings kernel isomorphism \ref{cdp:st:A.1.2} therefore gives',r'Put $K=\ker(\Omega_Y^1|_S\to\widetilde\Omega_S^1)$. The exact sequence in \ref{cdp:st:A.1.1} and the isomorphism $K\simeq\eta_*\eta^*N^*$ of \ref{cdp:st:A.1.2}, followed by the projection formula, give','Display the kernel and exact sequence transporting the normalization group to the ambient cotangent group.')
  add('D02,D05,D08','This proves the second equality. It establishes the universal normalization target requested in B.3 for the full normal-crossings class, including unequal multiplicities. It leaves the unrestricted nonordinary-fibre assertion to be decided separately.','','Remove the proof recap, requested-target language and separate-work announcement. Both groups, the entire NC domain and arbitrary multiplicities remain explicit in statement and proof.')
 proposed=D/f'S6_SERIES_PUBLISH_II_{tag}_proposed_v1.tex';assert not proposed.exists();proposed.write_text(text)
 # All labels, tags, hypertargets and original display blocks stay byte-identical.
 token=lambda x:re.findall(r'\\(?:label|tag|hypertarget)\{[^}]*\}',x)
 assert token(original.read_text())==token(text)
 display=lambda x:re.findall(r'\\\[(.*?)\\\]',x,re.S)
 assert display(original.read_text())==display(text)
 targets.append({'tag':tag,'statement_owner':owner,'original_full_block':bind(original),'proposed_full_block':bind(proposed),'guards':guards,'all_original_display_math_unchanged':True,'all_labels_tags_and_hypertargets_unchanged':True,'statement_scope_and_values_unchanged':True,'inline_math_scope':'Additional explicit maps and local weighted-Euler calculation; deletion of one duplicated S_i in the bounded defensive sentence; no original hypothesis/value/quantifier is changed.'})
# One exact bibliography pair; no unsupported DOI-absence assertion.
m=re.search(r'\\bibitem(?:\[[^\]]*\])?\{Peters2021\}',src);assert m
end=m.end()+re.search(r'\\bibitem|\\end\{thebibliography\}',src[m.end():]).start();old=src[m.start():end]
needle='\\newblock \\emph{Verified}.\n';assert old.count(needle)==1
new=old.replace(needle,'')
for name,text in [('original',old),('proposed',new)]:
 p=D/f'S6_SERIES_PUBLISH_II_Peters2021_{name}_entry.tex';assert not p.exists();p.write_text(text)
bib={'key':'Peters2021','change_id':'II-REC-C13-bib-Peters2021-01','defect_type':'D18','old':old,'new':new,'reason':'Remove the internal verification-status marker; primary journal title/author/volume/year/pages and exact PDF URL remain unchanged.','original_entry':bind(D/'S6_SERIES_PUBLISH_II_Peters2021_original_entry.tex'),'proposed_entry':bind(D/'S6_SERIES_PUBLISH_II_Peters2021_proposed_entry.tex')}
receipt={'schema_version':1,'paper':'II','checker':'i_provenance','created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source_at_preparation':bind(source),'targets':targets,'bibliography_guards':[bib],'canonical_mutations':False,'events_added':0,'final_manual_pair_reading_pending':True}
print(json.dumps(dump('S6_SERIES_PUBLISH_II_clean_group13_preparation_v1.json',receipt),indent=2))
