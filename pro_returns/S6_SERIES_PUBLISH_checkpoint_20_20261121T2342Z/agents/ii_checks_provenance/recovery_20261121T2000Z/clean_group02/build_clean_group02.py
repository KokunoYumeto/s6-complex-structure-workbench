from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,csv,re
ROOT=Path(__file__).resolve().parents[4];HERE=Path(__file__).resolve().parent
DER=HERE.parent/'clean_derivations';SOURCE=ROOT/'S6_SERIES_PUBLISH_II.tex'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def ref(p):return {'path':str(p.relative_to(ROOT)),'sha256':sha(p)}
now=datetime.now(timezone.utc).isoformat();source=SOURCE.read_text();targets=[]
scopes={
'01C9':'Full agreement with the independently frozen residue, normalized double-cover, conductor sign-line and exact branch-resolution arguments. The prerelease alternating branch matrices and universal Euler equations were checked. No global splitting of the conductor double cover is used.',
'01CA':'Full agreement with the frozen uniform-multiplicity Euler deduction and the exact graph normalization s=zeta*v*product(x_i). This is the same finite etale map as w^m=u, s=w*product(z_i) in the printed proof, with w=zeta*v; degrees and triple-point counts are transported by that map.',
'01FR':'Full agreement with the frozen coefficient-to-branch-normal map, determinant-line isomorphism, finite direct image and Serre-duality image calculation. The exact primary DGKX v1 Lemma6.11 on p81 and its full proof were read after release; its canonical map specializes exactly to this one. Its credit is preserved.',
'01GJ':'The frozen diagonal restriction sequence computes the exact length-one map O_A(-0) to O_A before target exposure. The new preproof two-term complex and P1 Laurent-Cech certificate agree with the printed derived shifts and fibre dimensions. The additional printed general base-change sequence was checked after release by taking direct images of multiplication by the base parameter; no extra independent event is proposed for that added paragraph.',
'01GO':'The frozen support/Krull/associated-prime proof and explicit square-zero embedded-point construction agree with the full printed proof. The additional all-integer cohomology values are checked after release using the exact P1 Cech intervals: global exponents 0 through -k, and degree-one exponents -k<n<0, together with the one-dimensional point summand. The final full-fibre application is supplied by the exact graph quotient ring from the frozen derivation and safely supplied E2 setup. The graph is not asserted smooth.',
'02WK':'The independently frozen proper-analytic normal-crossing trace argument agrees with the complete printed proof. The proposed text makes the homology/cohomology dual map explicit and clarifies that the Nth power, rather than the original monodromy, is the unipotent operator. The fresh universal 4x4 exterior-minor program checks that exact dual trace identity. Primary A Campo1975 Sections1-3 were actually read before freeze. No prior A/C reconstruction was used.'}
for tag in ['01C9','01CA','01FR','01GJ','01GO','02WK']:
 fp=json.loads((DER/f'S6_SERIES_PUBLISH_II_{tag}_freeze_pointer.json').read_text());rp=json.loads((DER/f'S6_SERIES_PUBLISH_II_{tag}_release_pointer.json').read_text())
 fpath=ROOT/fp['receipt'];assert sha(fpath)==fp['sha256'];freeze=json.loads(fpath.read_text())
 original=(ROOT/rp['full_block']).read_text();assert source.count(original)==1,(tag,source.count(original))
 proposed=original;guards=[]
 def ch(suffix,typ,old,new,reason):
  global proposed
  assert proposed.count(old)==1,(tag,suffix,proposed.count(old))
  proposed=proposed.replace(old,new,1)
  guards.append({'change_id':'II-REC-C02-'+tag+'-'+suffix,'defect_type':typ,'old':old,'new':new,'expected_occurrences_in_owning_block':1,'reason':reason})
 enum=r'\begin{enumerate}[label={$\langle1\rangle$\arabic*.},leftmargin=*]'
 if tag=='01FR':
  ch('ENUMOPEN','D04,D23',enum+'\n'+r'\item '+'\n','','Remove the one-item iteration wrapper.')
  ch('ENUMCLOSE','D04,D23','\n'+r'\end{enumerate}','','Remove the corresponding terminator.')
 else:ch('ENUM','D04,D23',enum,r'\begin{enumerate}[label=\arabic*.,leftmargin=*]','Use ordinary step numbering.')
 if tag=='01C9':
  ch('RESIDUE','D08',', proving the comparison. Since both line bundles','. Since both line bundles','Retain the exact determinant/unit transition comparison and remove its closing announcement.')
  ch('ETALE','D08',' This proves étaleness at the missing points as well.','','The preceding local-isomorphism calculation already proves the extension across triple points.')
  ch('COVER','D11','may be connected; no splitting is assumed.','may be connected.','Retain the positive connected-cover possibility.')
  ch('MARKS','D08',', proving their summed formula.','.','Retain the exact three-marks-per-triple-point count.')
  ch('FINALLY','D08',r'\item Finally $\widehat D$',r'\item $\widehat D$','Remove the process transition before the actual Euler calculation.')
  ch('COHERENTCLOSE','D08','\n'+r'which proves the last equality in \eqref{cdp:eq:C.NC.4}.','','Retain the displayed coherent Euler equation and the proved three-marks relation; remove only the recap reference to the owning result.')
  ch('COHERENTPUNCT','D23',r'0=\sum_i\chi(T_i,\OO_{T_i})-\frac12\sum_\alpha e(C_\alpha)+\tau,',r'0=\sum_i\chi(T_i,\OO_{T_i})-\frac12\sum_\alpha e(C_\alpha)+\tau.','Close the complete displayed sentence after removal of its recap clause; every term and sign is preserved.')
  ch('EULERCLOSE','D08',r' This proves the first identity in \eqref{cdp:eq:C.NC.5}.','','Retain the exact node-identification Euler decrement; the second identity still retains its formula reference.')
 elif tag=='01CA':
  ch('LOCATOR','D06','By (C.NC.5),',r'By \eqref{cdp:eq:C.NC.5},','Resolve the literal formula number to its existing exact label.')
  ch('CLOSE1','D08,D11',r'This proves \eqref{cdp:eq:C.NC.8} directly, with no base-change assumption.'+'\n','', 'The preceding two displayed equalities already establish the announced Euler formula.')
  ch('OPEN2','D08','To verify the additional comparison, locally write','Locally write','Keep the exact unit and root equations without the verification announcement.')
  ch('CLOSE2','D11',' The two displayed comparisons remain valid without any connectedness assertion about that cover.','','Retain the preceding explicit additivity over connected components.')
  ch('STATEMENTSCOPE','D11','Its possibly disconnected components do not affect the comparisons\n','The induced cover of reduced fibres satisfies\n','State the two exact full-cover comparisons positively; the proof retains additivity over components.')
 elif tag=='01FR':
  ch('PREFACE','D08',' We retain the short argument for its general ambient line-bundle twist and the exact image of its cohomology map.','','Retain the precise DGKX attribution and remove the process announcement.')
  ch('STEP','D23',r'\noindent\textbf{Step 1.} ','','Remove the duplicate step marker.')
  ch('SCOPE','D11',r'; no such vanishing has been suppressed in \eqref{cdp:eq:C.4}.','.','Retain the actual sufficient H3-vanishing criterion and the exact image formula.')
 elif tag=='01GJ':
  ch('TITLE','D16','Counterexample: The universal local-freeness assertion of CDP98, Lemma 1.5','A length-one torsion direct image','Give the result a mathematical heading; the primary attribution is supplied in the statement.')
  ch('CITATION','D06,D18','cohomology is zero in every degree; for $t=0$ it is $(0,1,1)$.','cohomology is zero in every degree; for $t=0$ it is $(0,1,1)$.\nThe torsion in $R^2g_*V$ contradicts the local-freeness assertion of\n'+r'\citet[Lemma~1.5, pp.~79--80]{CDP98}.','Bind the exact published assertion and the sheaf that violates it.')
  ch('CLOSE','D08',' This proves the direct-image,\nlength, and global-cohomology assertions.','','The exact derived complex and its shifts already establish those values.')
  ch('KUENNETH','D23','Fibre Kunneth gives',r'Fibre K\"unneth gives','Correct the mathematical name.')
  ch('REPLACEMENT','D01','actual replacement exact sequence','base-change exact sequence','Name the actual mathematical map, retaining the entire sequence.')
  ch('COMPUTEOPEN','D08','To compute the direct image with its length,\nput','Put','Retain the full degree-one auxiliary bundle and its exact map without a computation announcement.')
 elif tag=='01GO':
  ch('TITLE','D16','Counterexample: The embedded-component omission in the divisor-twisting lemma','Divisor twisting and embedded associated points','Name the stable-support theorem and its embedded-point obstruction.')
  ch('OPEN','D01,D08','CDP98, Proposition~1.1, in its printed generality of arbitrary\nnonreduced compact spaces, is false. The exact replacement is as\nfollows. For','For','Begin with the exact theorem; the fully proved counterexample retains its precise primary citation.')
  ch('CITATION','D06,D18','survives for every $k\\geq1$, refuting the printed proposition.','survives for every $k\\geq1$, contrary to\n'+r'\citet[Proposition~1.1, p.~78]{CDP98}.','Resolve the unnamed printed proposition to the actually read journal result.')
  ch('OPEN2','D01','For the replacement, the descending spaces','The descending spaces','Retain the descending finite-dimensional spaces without revision language.')
  ch('CLOSE','D08','This proves the exact stable-space formula. When','When','Both inclusions already prove the stable-support identity.')
  ch('VANISHCLOSE','D08',', proving the vanishing.','.','The support/intersection implication is the complete mathematical conclusion.')
  ch('GRAPHSTATEMENT','D06,D22',r'This last case applies to every full Cartier fibre used in \CompendiumRef{II}{cdp:st:E2}.',
   'For the graph of a nonconstant meromorphic map from a smooth connected threefold\n'+r'$Y$ to $\mathbb P^1$, every full fibre is isomorphic to a Cartier divisor in $Y$'+'\nand is Cohen--Macaulay with no embedded associated components.',
   'Replace the absent current E2 interface by the exact independently derived graph-fibre assertion, including multiplicities.')
  ch('GRAPHPROOF','D06,D22','\n'+r'\end{enumerate}',
   '\n'+r'\item Locally write the meromorphic map as $[a:b]$, where $a,b$ have'+'\nno common prime factor. Its graph $Z$ has equation\n'+r'$av-bu=0$ in $Y\times\mathbb P^1$. At $c=[u_c:v_c]$, the maps'+'\n'+r'\['+'\n'+r' \{av_c-bu_c=0\}\longrightarrow Z_c,\qquad y\longmapsto(y,c),'+'\n'+r'\]'+'\nand the restriction of the projection to $Y$ are inverse holomorphic\nmaps of analytic spaces: both local rings are\n'+r'$\mathcal O_Y/(av_c-bu_c)$.'+' The local equation is a nonzero\nelement of the regular local ring of $Y$, hence a nonzerodivisor.\nThe quotient is Cohen--Macaulay and Gorenstein and has no embedded\nassociated components. This identifies the full analytic fibre,\nincluding its nilpotents and multiplicities.\n\n'+r'\end{enumerate}',
   'Supply the actual inverse graph/fibre maps and regular-local quotient from the prerelease derivation; no smoothness assertion about the graph is used.')
 elif tag=='02WK':
  ch('TITLE','D16','[P4.13]','[Monodromy and the smooth locus of an irreducible fibre]','Replace the coded heading, retaining the permanent labels and tag.')
  ch('SCOPE','D11','This assertion requires no Betti-number hypothesis on a compactification.\n','','The complete proper local degeneration hypotheses already specify the scope.')
  ch('OPEN','D08','We resolve the pair by a proper holomorphic modification','Choose a proper holomorphic resolution of the pair','Retain the exact modification and its isomorphism loci without a proof announcement.')
  ch('TRACEOPEN','D08','We spell out the trace comparison. At a point','At a point','Remove the standalone announcement before the complete local calculation.')
  ch('TRACEACTION','D25','Alternating traces in the nearby-cycle spectral sequence, with a\nfinite stratification of the compact central divisor, therefore give\n'+r'\['+'\n'+r' L(A^d;H^*(T^4;\C))',
   r'Let $F$ be the nearby torus and $T$ its induced cohomology monodromy. Alternating traces in the nearby-cycle spectral sequence, with a'+'\nfinite stratification of the compact central divisor, give\n'+r'\['+'\n'+r' L(T^d;H^*(F;\C))',
   'Distinguish the homology operator A from its induced cohomology operator T; their exact evaluation-dual map is proved in the final step.')
  ch('CITATION','D06,D18',"This is the global form of A'Campo 1975, Theorem 1; his proper\nanalytic construction in Section 2 and spectral-sequence proof in\nSection 3 give precisely this comparison. The explicit local\ncalculation verifies the hypotheses without a Kähler assumption.",
   r'This is the proper analytic trace formula of \citet[Theorem~1, p.~235; \S\S2--3, pp.~237--245]{ACampo1975}, obtained from the displayed local traces and the nearby-cycle spectral sequence.',
   'Bind the actual primary theorem, proper-analytic construction and trace proof that were read before freeze.')
  ch('POWER','D25','A common multiple $N$\nof the $n_j$ makes monodromy act trivially on all local\nnearby-cohomology sheaves, hence on the $E_2$ page. Its action\non the filtered abutment is consequently unipotent.',
   'For a common multiple $N$\nof the $n_j$, the $N$th power of monodromy acts trivially on all local\nnearby-cohomology sheaves, hence on the $E_2$ page. This $N$th power\nacts unipotently on the filtered abutment.',
   'Specify the precise power which is unipotent; the original monodromy need only be quasi-unipotent.')
  ch('DUAL','D25','Since torus cohomology is\nthe exterior algebra on $H_1$, its Lefschetz number is\n$\\det(I-A^m)$.',
   r'Under the evaluation pairing $H^1(F;\C)=H_1(F;\C)^\vee$, the induced cohomology action is $A^T$, since $(T\alpha)(c)=\alpha(Ac)$. The cohomology of the nearby torus $F$ is the exterior algebra on $H^1(F;\C)$, so its Lefschetz number is'+'\n'+r'$\det(I-(A^m)^T)=\det(I-A^m)$.',
   'Correct the cohomology/homology identification by the exact evaluation dual map and determinant transpose equality, as independently derived before release.')
  ch('ASREQUIRED','D08',', as required.','.','Retain both the nonnegativity and the exact 2^4 bound.')
  ch('QUASIOPEN','D08','These same charts prove quasi-unipotence. For a common multiple','For a common multiple','Retain the complete finite-power/filtration proof without its opening announcement.')
 oc=HERE/f'S6_SERIES_PUBLISH_II_{tag}_original.tex';pc=HERE/f'S6_SERIES_PUBLISH_II_{tag}_proposed.tex';oc.write_text(original);pc.write_text(proposed)
 dp=ROOT/freeze['frozen_derivation_path'];assert sha(dp)==freeze['derivation_sha256']
 targets.append({'tag':tag,'statement_owner':freeze['statement_owner'],'checker':'i_provenance_recovery','freeze_receipt':ref(fpath),'frozen_derivation':ref(dp),'release_receipt':{'path':rp['receipt'],'sha256':rp['sha256']},'original_full_block':ref(oc),'proposed_full_block':ref(pc),'guards':guards,'comparison':scopes[tag],'actual_complete_original_proof_read':True,'actual_complete_proposed_proof_read':False,'source_application_pending':True,'events_added':0})
ledger=ROOT/'CHECK_EVENTS.tsv';owners=[x['statement_owner'] for x in targets]
with ledger.open() as f:rows=[{'line':i,'row':r} for i,r in enumerate(csv.DictReader(f,delimiter='\t'),2) if r['statement_id'] in owners]
lp=HERE/'S6_SERIES_PUBLISH_II_clean_group02_prior_associations.json';lp.write_text(json.dumps({'created_utc':now,'ledger':ref(ledger),'rows':rows,'scope':'Only these six exact owners, inspected after freeze and release; no unreleased target records read.','events_added':0},indent=2)+'\n')
primary=HERE.parent/'primary_inputs';primary_receipts=[ref(primary/'CDP98_journal_receipt.json'),ref(primary/'ACampo1975_receipt.json')]
bundle={'schema_version':1,'paper':'II','checker':'i_provenance_recovery','created_utc':now,'canonical_source_at_review':ref(SOURCE),'targets':targets,'prior_associations':ref(lp),'primary_receipts':primary_receipts,'safe_E17_graph_input':ref(HERE.parent/'S6_SERIES_PUBLISH_II_E17_graph_ambient_inputs.tex'),'root_program_lookup':'Root actually read the pinned 20-line C_euler.py and reports it contains A×P1/genus-two/point-blowup and finite N toroidal v/e/f calculations, with no C9/CA conductor or normalized root-cover routine. Root also inspected E_checks.py and reports routines E5/E8/E10/E11/E13/E14, with no E12 or E17 routine. These are exact-file bounded lookup reports, not a repository-wide absence claim. Shared E_checks.py has not been opened by this checker.','computations':[ref(ROOT/'agents/ii_checks_provenance/computations/S6_SERIES_PUBLISH_II_01C9_preproof_branch_complex.py'),ref(ROOT/'agents/ii_checks_provenance/computations/S6_SERIES_PUBLISH_II_01C9_preproof_branch_complex.output.json'),ref(DER/'S6_SERIES_PUBLISH_II_01GJ_preproof_complex.py'),ref(DER/'S6_SERIES_PUBLISH_II_01GJ_preproof_complex.output.json'),ref(DER/'S6_SERIES_PUBLISH_II_02WK_preproof_exterior.py'),ref(DER/'S6_SERIES_PUBLISH_II_02WK_preproof_exterior.output.json')],'status':'Complete final proposed pair rereading pending.','canonical_mutations':0,'events_added':0}
p=HERE/'S6_SERIES_PUBLISH_II_clean_group02_proposals.json';p.write_text(json.dumps(bundle,indent=2,ensure_ascii=False)+'\n');print(json.dumps({'proposal':ref(p),'guards':sum(len(t['guards']) for t in targets)},indent=2))
