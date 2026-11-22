"""02YD exact source-edit proposals; no canonical changes."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json

R=Path('agents/ii_checks_A/recovery_20261121T195642Z');O=R/'group12_YD';O.mkdir(exist_ok=True)
p=Path('agents/ii_infra/released_proofs/02YD/ebc0b2dadfc25c76/S6_SERIES_PUBLISH_full_owning_block.tex')
original=p.read_text();text=original
sha=lambda s:hashlib.sha256(s.encode()).hexdigest()
oldpath=O/'S6_SERIES_PUBLISH_II_02YD_full_original.tex';newpath=O/'S6_SERIES_PUBLISH_II_02YD_full_proposed.tex';oldpath.write_text(original)
guards=[]
def edit(old,new,defects,reason,transport):
 global text
 assert text.count(old)==1,(old,text.count(old))
 before=text;at=before.index(old);text=before[:at]+new+before[at+len(old):]
 guards.append({'tag':'02YD','guard_id':f'A_REC_02YD_{len(guards)+1:03}','literal_old':old,'literal_new':new,'defect_types':defects,'reason':reason,'mathematical_transport':transport,'offset_before':at,'intermediate_before_sha256':sha(before),'intermediate_after_sha256':sha(text),'full_original_path':str(oldpath),'full_proposed_path':str(newpath)})

edit('[P4R.2]','[Euler number for a bijective normalization]',['D04','D16'],'Use a mathematical title.','Statement, tag and both labels retain their exact identities.')
edit('of fundamental groups and equality of Euler numbers. P4R.1\nmakes', 'of fundamental groups and equality of Euler numbers.\n\\SeriesRef{night:P4R.1} makes',['D04'],'Use the retained series label.','The same independently checked fundamental-group result is invoked.')
edit('P4.12 applies to this same $T$ and proves $\\kappa(T)=-\\infty$.\nThe opened classification theorem used there leaves rational,\nruled, and class-VII minimal models, followed by point blowups.',
     '\\SeriesRef{night:P4.12} applies to this same $T$ and proves\n$\\kappa(T)=-\\infty$. Write $q:T\\to T_0$ for the contraction\nto a minimal model, with $k$ point blowups. The classification\ngives rational, ruled, and class-VII possibilities for $T_0$.\nIn the K\\\"ahler case, $p_g(T_0)=0$ permits an integral\nK\\\"ahler class; the embedding given by\n\\cite[Main Theorem, pp.~314--315]{Kodaira1954} identifies $T_0$\nwith a projective surface, to which\n\\cite[Theorem~VI.17 and Corollary~VI.18, pp.~111--112]{Beauville1978}\napplies. In the non-K\\\"ahler case use\n\\cite[Theorem~5.1, p.~27]{OVV2020}. Its elliptic alternative\nhas $e=K^2=0$ by Theorem~4.2 there; together with $p_g=0$,\nNoether\'s formula gives $h^1(\\OO)=1$, and Theorem~2.5 gives\n$b_1=1$. It therefore also satisfies the class-VII conditions\n$b_1=1$ and $\\kappa=-\\infty$.',
     ['D04','D08','D18'],'Replace the indirect source/process phrase by the opened primary classification loci.','The exact Kodaira section embedding carries the Kähler minimal model to Beauville; OVV elliptic overlap is verified by e=K²=χ=0, p_g=0 and b1=1, retaining precisely the original three alternatives.')
edit('van Kampen applies to the common punctured four-ball with\nsimply connected boundary $S^3$. A ruled surface over a\ngenus-$g$ curve has the same fundamental group as that curve,\nby the homotopy sequence of its $\\mathbb P^1$-bundle.',
     'van Kampen compares a four-ball with the disk bundle\nof $\\OO_{\\mathbb P^1}(-1)$, both attached along the same\nsimply connected boundary $S^3$. For a ruled minimal model\n$p:T_0\\to C$ over a genus-$g$ curve, the homotopy sequence\nof its $\\mathbb P^1$-bundle gives the isomorphism $p_*$\non fundamental groups. The resulting isomorphism from\n$\\pi_1(S)$ to $\\pi_1(C)$ is $p_*q_*(\\nu_*)^{-1}$.',
     ['D20','D22'],'State the local replacement and composite group map.','The blowdown ([u:v],a)↦(au,av) induces q_*; ν is the given homeomorphism and p is the actual P1-bundle.')
edit('\\item A rational surface has positive Euler number. A ruled surface\nover an elliptic curve, blown up $k$ times, has Euler number\n$k$. A class-VII surface has Euler number $b_2\\ge0$, and\neach blowup increases it by one. These formulas give',
     '\\item A point blowup replaces a point by $\\mathbb P^1$ and\nincreases Euler characteristic by one. The cell counts of\n$\\mathbb P^2$ and a $\\mathbb P^1$-bundle over a genus-$g$\ncurve give $3$ and $4-4g$, respectively. For class VII,\nPoincar\\\'e duality and $b_1(T_0)=1$ give $e(T_0)=b_2(T_0)$.\nThus\n\\[\n e(T)=\\begin{cases}\n 3+k,&T_0=\\mathbb P^2,\\\\\n 4-4g+k,&T_0\\text{ ruled over a genus-}g\\text{ curve},\\\\\n b_2(T_0)+k,&T_0\\text{ of class VII}.\n \\end{cases}\n\\]\nSince $g\\le1$, these formulas give',
     ['D20','D22'],'Display the original Euler calculations with one minimal-model convention.','Cell-degree convolution gives3 and4−4g; q adds one for each blowup; classVII Betti ranks(1,1,b2,1,1) giveb2. These are exactly the original formulas.')
edit('and nonnormal; P4.12 gives an effective conductor curve on\n$T$. The precise class-VII classification and absence of\ncurves on Inoue surfaces verified in P4.8 therefore force\n$T$ to be Hopf.',
     r"""and nonnormal; \SeriesRef{cdp:st:A.5.3} gives its effective
conductor divisor on $T$. By \cite[Theorem~1, p.~1]{BBK2019},
there is a finite \'etale cover $a:T'\to T$ whose domain is
Hopf or Inoue. The inverse image of the conductor contains
a curve, excluding the Inoue alternative by
\cite[Propositions~2(i) and~3(i), pp.~274--275 and~277,
and the paragraph after (21), p.~279]{Inoue1974}.
The composition of $a$ with the Hopf universal cover
$\C^2\setminus\{0\}\to T'$ is a universal cover of $T$;
hence $T$ itself is Hopf.""",
     ['D04','D08','D18','D22'],'Give the exact finite-cover classification and original no-curves locators.','a^-1(conductor) is a nonempty curve; the Hopf cover from punctured C² to T′, composed with a, is the universal cover of T. No NC hypothesis from P4.8 is imported.')

edit('Its elliptic alternative\nhas $e=K^2=0$ by Theorem~4.2 there; together with $p_g=0$,\nNoether\'s formula gives $h^1(\\OO)=1$, and Theorem~2.5 gives\n$b_1=1$. It therefore also satisfies the class-VII conditions\n$b_1=1$ and $\\kappa=-\\infty$.',
     r"""For its elliptic alternative, Theorem~4.2, Remark~4.4 and
Proposition~4.5 there (pp.~17--22) give elliptic reduced fibres,
the cyclic translation model at multiple fibres, and a
holomorphic elliptic action. For the fibration
$\pi:T_0\to C_0$, its nowhere-zero vertical vector field gives
$Q=T_{T_0}/\OO$, and the differential induces
$Q\simeq\pi^*T_{C_0}(-R_\pi)$, where $R_\pi$ is the
multiple-fibre ramification divisor. Thus
$K_{T_0}=\pi^*K_{C_0}(R_\pi)$ and $K_{T_0}^2=0$;
the elliptic fibres also give $e(T_0)=0$. Together with
$p_g=0$, Noether's formula gives $h^1(\OO)=1$.
Theorem~2.5 there (pp.~7--9) then gives $b_1=1$.
This alternative also satisfies the class-VII conditions
$b_1=1$ and $\kappa=-\infty$.""",
     ['D18','D22'],'Give the exact action and differential producing the elliptic numerical invariants.','The already opened Proposition4.5 supplies the global elliptic action; its vertical vector field and the actual differential ofπ give Q and the canonical line bundle. Vertical divisors have zero pairwise intersection. Corollary4.3 is not the action locator.')

edit('Equality in the ruled case is exactly\n$k=0$.',
     'Equality in the ruled case is exactly\n$g=1$ and $k=0$.',
     ['D20','D22'],'Specify the genus in the displayed general ruled formula.','The original rational case has positive Euler number, and its elliptic ruled case has Euler number k; the same zero case is now stated beside the formula4−4g+k.')

newpath.write_text(text)
source=Path('S6_SERIES_PUBLISH_II.tex').read_text();a=source.index('\\section*{Programs}');b=source.index('\\end{longtable}',a)+len('\\end{longtable}');oldtable=source[a:b]
row=r'''Euler identities from curve and sphere cells, point blowups and class-VII Betti ranks (\cref{night:P4R.2}) & \href{https://raw.githubusercontent.com/KokunoYumeto/s6-complex-structure-workbench/\SsixRepositoryCommit/code/S6_SERIES_PUBLISH_II_A_02YD_euler_cells.py}{\nolinkurl{S6_SERIES_PUBLISH_II_A_02YD_euler_cells.py}} \\[3pt]
'''
manifest={'created_utc':datetime.now(timezone.utc).isoformat(),'checker':'ii_check_a','canonical_writes':0,'guards':guards,'blocks':[{'tag':'02YD','original_path':str(oldpath),'proposed_path':str(newpath),'original_sha256':sha(original),'proposed_sha256':sha(text),'statement_unchanged':True,'proof_repairs':[],'scope_repairs':[]}],'bibliography_guards':[],'program_table_guard':{'literal_old':oldtable,'literal_new':oldtable.replace('\\end{longtable}',row+'\\end{longtable}'),'source_path':'S6_SERIES_PUBLISH_II.tex','source_sha256':sha(source),'source_character_offset':a,'defect_types':['D09'],'reason':'Associate the new Euler computation with its owning statement.','mathematical_transport':'The degree counts and blowup replacement compute exactly the displayed Euler formulas.'},'note':'Root owns canonical integration. Three mathematical proof items are retained; the run enumeration wrapper remains for the global numbering pass.'}
mp=O/'S6_SERIES_PUBLISH_II_A_YD_editorial_proposals.json';mp.write_text(json.dumps(manifest,indent=2)+'\n')
f=original
for g in guards:
 assert sha(f)==g['intermediate_before_sha256'];assert f.count(g['literal_old'])==1;f=f.replace(g['literal_old'],g['literal_new'],1);assert sha(f)==g['intermediate_after_sha256']
assert f==text
for g in reversed(guards):
 at=g['offset_before'];assert f[at:at+len(g['literal_new'])]==g['literal_new'];f=f[:at]+g['literal_old']+f[at+len(g['literal_new']):]
assert f==original
v={'created_utc':datetime.now(timezone.utc).isoformat(),'owner_guard_count':len(guards),'forward_exact':True,'inverse_exact':True,'current_original_matches':source.count(original),'original_sha256':sha(original),'proposed_sha256':sha(text),'canonical_writes':0};(O/'S6_SERIES_PUBLISH_II_A_YD_guard_validation.json').write_text(json.dumps(v,indent=2)+'\n');print(json.dumps(v,indent=2))
