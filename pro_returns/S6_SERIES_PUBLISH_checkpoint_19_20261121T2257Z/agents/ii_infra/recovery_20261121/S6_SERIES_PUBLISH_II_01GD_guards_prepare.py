from pathlib import Path
import json,hashlib,re,datetime,difflib
ROOT=Path(__file__).resolve().parents[3];D=Path(__file__).parent
source=ROOT/'S6_SERIES_PUBLISH_II.tex';s=source.read_text()
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def bind(p):return {'path':str(p.relative_to(ROOT)),'sha256':sha(p),'bytes':p.stat().st_size}
def save(p,t):assert not p.exists();p.write_text(t)
folder=D/'GD_guard_blocks';folder.mkdir(exist_ok=False)
rp=ROOT/'agents/ii_infra/released_proofs/01GD/3452ece0b3fe38b9/S6_SERIES_PUBLISH_full_owning_block.tex'
before=rp.read_text();assert s.count(before)==1
after=before;edits=[]
def edit(old,new,typ,reason,witness=None):
 global after
 assert after.count(old)==1,(old,after.count(old))
 a=after.index(old);after=after[:a]+new+after[a+len(old):]
 x={'before':old,'after':new,'type':typ,'reason':reason,'sequential_before_offset':a}
 if witness:x['exact_mathematical_witness']=witness
 edits.append(x)

edit('[Proved extension of the marked torus period]','[Extension of the marked torus period]','D08/D16','Remove the proof-status adjective from the title.')
edit('This assertion does not assert an extension of the\nAlbanese map from the given proper model $U$.','', 'D11','The unchanged statement asserts only the marked-period and relative-group extensions; delete the neighbouring-map disclaimer.','The two exact conclusions remain in the preceding three sentences. No morphism from U to the extending family is added.')
edit(r'\begin{enumerate}[label={$\langle1\rangle$\arabic*.},leftmargin=*]',r'\begin{enumerate}[leftmargin=*]','D04','Remove the printed iteration marker while retaining the five logical proof items.')
old='\\item An embedded resolution of the central fibre changes neither\nthe smooth fibres nor their marking, so we may use the relative\nlogarithmic complex of \\ref{cdp:st:D.2.3} with arbitrary multiplicities.'
new='''\\item The punctured family is connected by local triviality and connectedness
of its fibres, so it lies in one open and closed component $U^0$ of $U$.
The inclusion $U^0\\hookrightarrow U$ is an isomorphism over $\\Delta^*$.
Apply analytic embedded resolution to the compact reduced central divisor
in $U^0$ \\cite[\\S0.2(2), preprint p.~3; Theorem~1.6 and Remarks~1.7,
preprint pp.~5--6]{BierstoneMilman1997}. This gives a proper composite
of blowups $\\pi:\\widetilde U\\to U^0$ with smooth centres over that
divisor, with $\\widetilde U$ smooth and the reduced central support
of $h\\circ\\pi$ normal crossing. For $t\\ne0$,
$\\pi_t:\\widetilde U_t\\to U_t$ is a biholomorphism;
its pullback identifies holomorphic forms, the integral marking and
cup products. Transporting through these pullbacks, use the relative
logarithmic complex in the proof of Proposition~\\ref{cdp:st:D.2.3}
on this model, with its full central multiplicities.'''
edit(old,new,'D06/D25','Give the exact resolution morphism and primary analytic locator behind the model transport, including the dominating-component scope.','The prerelease GD derivation §1 proves the inclusion and fibre maps; the version-bound primary receipt verifies compact embedded-divisor resolution and centres over the central support.')
edit('as in \\ref{cdp:st:D.2.3}.','as in that proof.','D08','The same proof is named immediately before the unchanged construction of its logarithmic bundle and generator.','The first explicit Proposition reference is retained; this adjacent duplicate reference is replaced by its unambiguous antecedent.')
old='''\\item The second case of that proof, including the exact maps
(D.18)--(D.19), did not use any geometric-genus assumption.
It shows that $\\Omega$ cannot vanish on the whole reduced
central support: otherwise its divided cohomology class would
have bounded periods while its positive $L^2$ volume diverges.
Thus $\\Omega|_T$ is nonzero on some normalized component $T$.
The first case of that proof shows, without a geometric-genus
assumption, that every conductor residue of every component
restriction is zero, because a nonzero residue would give the
same divergent positive volume. The nonzero restriction
$\\Omega|_T$ is therefore a holomorphic two-form on $T$.'''
new='''\\item The coefficient-ideal argument in
\\eqref{cdp:eq:D.18}--\\eqref{cdp:eq:D.19} shows that $\\Omega$
cannot vanish on the whole reduced central support: otherwise
its divided cohomology class would have bounded periods while
its positive $L^2$ volume diverges. Thus $\\Omega|_T$ is nonzero
on some normalized component $T$. The annular volume estimate
in the same proof makes every conductor residue of every
component restriction zero: a nonzero residue would give a
divergent positive volume while its cup-product expression
stays bounded. The nonzero restriction $\\Omega|_T$ is therefore
a holomorphic two-form on $T$.'''
edit(old,new,'D02/D06/D08','Bind the two actual input maps by their labels and state the coefficient-ideal and residue arguments directly.','The entire GA proof was independently checked before the GD freeze. Its ideal argument and annular estimate use identity monodromy at these exact steps; geometric genus is used only in the separate GA contradiction, not in the retained arguments used here.')
edit('The flat cohomology class $v(t)=[\\Omega_t]$ is holomorphic\nacross zero.','The cohomology class $v(t)=[\\Omega_t]$, expressed in the flat\nframe, is holomorphic across zero.','D25','The section has holomorphic period coordinates in a flat frame; it is not asserted to be horizontal.','The prerelease construction maps the varying top form into the flat bundle. The connection is flat, but no equation ∇v=0 is required or proved; the full argument uses holomorphic coordinates.')
edit('therefore lies in $\\mathcal T_2$, as claimed.','therefore lies in $\\mathcal T_2$.','D08','Remove the outcome marker after the actual transversality deduction.')
edit('\\item For completeness the extending group family is explicit.\nLet','\\item Let','D08','Start directly with the group-family construction.')
old='''The direct-sum relation with the conjugate makes this a full
real lattice in every fibre, uniformly on compact subsets of
the disc. Hence'''
new='''A real cycle annihilating $\\mathcal W_t$ also annihilates
$\\overline{\\mathcal W_t}$, hence all of $V$; it is therefore zero.
Equality of real dimensions makes the real-linear evaluation
map an isomorphism, so the image is a full lattice in every fibre,
uniformly on compact subsets of the disc. Translation by this
lattice is free and properly discontinuous. For a fixed integral
basis, the closed parallelotopes generated by its images cover
each quotient fibre; over a compact subset of the base their
union is compact. Consequently'''
edit(old,new,'D25','Give the injectivity, real-linear dimension argument and proper quotient map behind the compact torus family.','The prerelease GD derivation §5 gives the evaluation map ι_t(γ)(ω)=<ω,γ>, its real-linear inverse by transversality/dimension, the uniform lower singular-value bound, and the compact fundamental-parallelotope map.')
old='''This is the asserted exact isomorphism of relative group
families. Extending a map from the original model $U$ to
$\\mathcal A$ requires a further argument; it does not follow
merely from this period construction.'''
edit(old,'','D08/D11','Remove the duplicate isomorphism recap and neighbouring-map disclaimer.','The retained preceding sentences give the fibrewise Albanese identification and its holomorphic variation, while the complete construction proves a smooth proper group family. The theorem asserts no extension of a map from U.')
tag=r'\tag{D.20}';k=after.index(tag);a=after.rfind('\\[',0,k);b=after.index('\\]',k)+2;old=after[a:b]
new=old.replace('\\[','\\begin{equation}',1).replace(tag,'',1);new=new[:-2]+'\\end{equation}'
edit(old,new,'D04','Use the current paper equation counter while retaining the full lower-bound formula, label and hypertarget.')
rebuild=after
for x in reversed(edits):
 a=x['sequential_before_offset'];assert rebuild[a:a+len(x['after'])]==x['after'];rebuild=rebuild[:a]+x['before']+rebuild[a+len(x['after']):]
assert rebuild==before
anchors=lambda t:re.findall(r'\\(?:label|hypertarget)\{[^}]+\}',t)
assert anchors(before)==anchors(after)
def displays(t):
 return [re.sub(r'\\tag\{D\.20\}','',m.group(1)if m.group(1)is not None else m.group(2))for m in re.finditer(r'\\\[(.*?)\\\]|\\begin\{equation\}(.*?)\\end\{equation\}',t,re.S)]
assert displays(before)==displays(after)
refs=lambda t:re.findall(r'\\(?:ref|eqref|cref|Cref|SeriesRef|CompendiumRef|cite)(?:\[[^\]]*\])?\{[^}]+\}(?:\{[^}]+\})?',t)
inline=lambda t:re.findall(r'(?<!\\)\$(?!\$)(.*?)(?<!\\)\$',t,re.S)
inline_changes=[];ib,ia=inline(before),inline(after)
for op,a,b,c,d in difflib.SequenceMatcher(None,ib,ia,autojunk=False).get_opcodes():
 if op!='equal':inline_changes.append({'operation':op,'before':ib[a:b],'after':ia[c:d]})
assert before.count('\\item ')==after.count('\\item ')==5
bf=folder/'S6_SERIES_PUBLISH_II_01GD_original_full_block.tex';af=folder/'S6_SERIES_PUBLISH_II_01GD_proposed_full_block.tex';save(bf,before);save(af,after)
items=list(re.finditer(r'\\bibitem(?:\[[^\]]*\])?\{([^}]+)\}',s));i=next(i for i,x in enumerate(items)if x.group(1)=='BierstoneMilman1997');bb=s[items[i].start():items[i+1].start()]
old='\\newblock URL \\url{https://arxiv.org/pdf/alg-geom/9508005}.\n\\newblock \\emph{Verified}.'
new='\\newblock URL \\url{https://arxiv.org/pdf/alg-geom/9508005v2}.\n\\newblock Cited preprint edition: arXiv:alg-geom/9508005v2,\n16 August 1995; preprint page locators refer to this edition.'
assert bb.count(old)==1;ba=bb.replace(old,new)
bbf=folder/'S6_SERIES_PUBLISH_II_BierstoneMilman1997_original_entry.tex';baf=folder/'S6_SERIES_PUBLISH_II_BierstoneMilman1997_proposed_entry.tex';save(bbf,bb);save(baf,ba)
evidence=D/'GD_primary_inputs/S6_SERIES_PUBLISH_II_01GD_primary_input_receipt.json'
g1={'id':'II-infra-recovery-01GD-publication','statement_id':'cdp:st:D.2.6','tag':'01GD','source_sha256':sha(source),'before':before,'after':after,'type':'D02/D04/D06/D08/D11/D16/D25','reason':'Preserve the proved extension while specifying the exact resolution and lattice morphisms, distinguishing a holomorphic section from a horizontal section, and replacing historical numbering and presentation residue.','literal_edits':edits,'original_full_block':str(bf.relative_to(ROOT)),'original_full_block_sha256':sha(bf),'proposed_full_block':str(af.relative_to(ROOT)),'proposed_full_block_sha256':sha(af),'preservation':{'exact_forward_inverse':True,'all_display_math_identical_after_only_D20_number_tag_removed':True,'all_labels_and_hypertargets_identical':True,'five_proof_items_preserved':True,'references_before':refs(before),'references_after':refs(after),'reference_changes':'One adjacent duplicate cdp:st:D.2.3 reference is replaced by its explicit proof antecedent. The only additions are the version-bound primary embedded-resolution citation and eqref links for the existing literal D.18–D.19 pair.','inline_changes':inline_changes,'mathematical_map_witnesses':'All added inline data specify the dominating-component inclusion, resolution and fibre isomorphisms, or evaluation/transversality maps proved in the prerelease derivation. The deleted U/A mentions occur only in discarded disclaimer/recap tails; theorem hypotheses and the complete group construction remain.','bundle_section_precision':'v(t) is the holomorphic top-form class expressed in a horizontal frame; no horizontality of v itself is asserted.','complete_hypotheses_and_conclusions_retained':True},'mathematical_scope_changed':False,'primary_evidence':bind(evidence)}
g2={'id':'II-infra-recovery-01GD-BM-edition','statement_id':'bib:BierstoneMilman1997','key':'BierstoneMilman1997','source_sha256':sha(source),'before':bb,'after':ba,'type':'D08/D18','reason':'Pin the primary arXiv edition actually read and distinguish its page locators from the retained published journal metadata.','literal_edits':[{'before':old,'after':new,'type':'D08/D18','reason':'The official arXiv version history and actual PDF bind v2 to 16 August 1995; remove the workflow verification marker.'}],'original_entry':str(bbf.relative_to(ROOT)),'original_entry_sha256':sha(bbf),'proposed_entry':str(baf.relative_to(ROOT)),'proposed_entry_sha256':sha(baf),'publication_evidence':bind(evidence),'preservation':{'key_authors_title_journal_volume_pages_year_doi_unchanged':True,'primary_publisher_url':'https://link.springer.com/article/10.1007/s002220050141','primary_publisher_ref':'turn320991488view0','primary_publisher_note':'Publisher metadata confirms title, volume, pages, year and DOI. Its displayed author metadata omits Milman; the actual two-author paper and official arXiv record confirm both retained authors.','cited_edition':'Only preprint page locators are assigned to v2; published journal pagination remains 207–302 (1997).'},'mathematical_scope_changed':False}
g={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source_sha256':sha(source),'guards':[g1,g2],'guard_count':2,'literal_edit_count':len(edits)+1,'status':'Prepared only; complete final-pair reading is recorded separately.','events_added':0,'canonical_files_modified':False}
gp=D/'S6_SERIES_PUBLISH_II_01GD_guards.json';save(gp,json.dumps(g,indent=2)+'\n');print(json.dumps(bind(gp)));print('literal_edits',g['literal_edit_count']);print('inline_changes',json.dumps(inline_changes));print('all_preservation_assertions_passed')
