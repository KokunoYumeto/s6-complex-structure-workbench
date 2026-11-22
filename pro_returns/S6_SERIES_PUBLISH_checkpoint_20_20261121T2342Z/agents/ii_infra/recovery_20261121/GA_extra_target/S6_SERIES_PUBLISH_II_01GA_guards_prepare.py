from pathlib import Path
import json,hashlib,re,datetime,difflib

ROOT=Path(__file__).resolve().parents[4]
D=Path(__file__).parent
assert (ROOT/'S6_SERIES_PUBLISH_II.tex').exists()
source=ROOT/'S6_SERIES_PUBLISH_II.tex'
s=source.read_text()
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def bind(p):return {'path':str(p.relative_to(ROOT)),'sha256':sha(p),'bytes':p.stat().st_size}
def save(p,t):assert not p.exists();p.write_text(t)
released=D/'released/23733aed2d9af3d1/S6_SERIES_PUBLISH_II_01GA_released_full_block.tex'
before=released.read_text();assert s.count(before)==1
after=before;edits=[]
def edit(old,new,typ,reason):
 global after
 assert after.count(old)==1,(old,after.count(old))
 off=after.index(old);after=after[:off]+new+after[off+len(old):]
 edits.append({'before':old,'after':new,'type':typ,'reason':reason,'sequential_before_offset':off})

edit('[Proved logarithmic period obstruction]','[Logarithmic period obstruction]','D08/D16','Remove the proof-status adjective from the mathematical title.')
edit('No K\\"ahler assumption\non $U$ or $D$ is made, and the positive integers $m_i$ are arbitrary.','The conclusion holds for every choice of positive integers $m_i$.','D02','The hypotheses already specify the full complex analytic scope. State the multiplicity scope positively and retain every allowed total space and central divisor.')
edit(r'\begin{enumerate}[label={$\langle1\rangle$\arabic*.},leftmargin=*]',r'\begin{enumerate}[leftmargin=*]','D04','Remove the proof-iteration prefix while preserving all twelve numbered arguments.')
edit('\\item We first identify exactly the analytic comparison used in the\nargument. Put','\\item Put','D08','Begin with the defined relative logarithmic complex.')
edit('They precede the additional Hodge-theoretic assumptions of the\nlater sections. ','','D02/D11','The exact cited analytic hypotheses remain immediately before this discarded contrast.')
edit('its actual Gauss--Manin connection','its Gauss--Manin connection','D08','Use the mathematical name of the connection.')
old='The local calculation used below is the same monomial Koszul\ncalculation as \\cite[Proposition~1.13, pp.~233--234, and proof of Proposition~2.20, pp.~238--239]{Steenbrink1976}; we give it explicitly for the\nsubcomplex needed here. No local invariant-cycle surjectivity\nor polarization is invoked.'
new='The local calculation on the coefficient ideal uses the monomial\nKoszul complex of \\cite[Proposition~1.13, pp.~233--234, and proof of Proposition~2.20, pp.~238--239]{Steenbrink1976}.'
edit(old,new,'D02/D08','Preserve the exact primary locator and the coefficient-ideal construction; remove the announcement and the defensive scope tail.')
edit('The determinant of the locally free relative logarithmic complex is','The second exterior power of the relative logarithmic cotangent bundle is','D25','The displayed bundle is the top exterior power of the rank-two quotient cotangent bundle. A determinant of the entire complex would have alternating tensor powers; the exact quotient sequence, not that determinant, gives the displayed formula.')
edit('\\item It remains to treat the case where $\\Omega$ vanishes on every\nbranch of $D$. Put','\\item Suppose that $\\Omega$ vanishes on every\nbranch of $D$. Put','D08','State the second mathematical case directly.')
edit('absolute/relative logarithmic exact sequence remains an exact\nsequence of complexes after tensoring by $\\mathscr J/(t)$:','absolute/relative logarithmic exact sequence remains exact\nwhen its coefficients are restricted to $\\mathscr J/(t)$:','D25','Name the induced coefficient subquotient, whose differential was verified to preserve the two ideals, rather than suggesting an O-linear tensor differential.')
edit('\\item We compute the eigenvalues of $\\rho_{\\mathscr B}$ without\nassuming reduced multiplicities. At a point of $r$ branches,','\\item At a point of $r$ branches,','D02/D08','The displayed monomial calculation already handles all multiplicities; remove its announcement and repeated disclaimer.')
edit('periods again gives a contradiction. This proves nontriviality\nof the $H^2$ monodromy in the remaining case.','periods again gives a contradiction.','D08','The explicit contradiction completes this case. The removed H² mention repeats the assumption and the unchanged proposition conclusion.')
edit('\\item Finally the natural\ncup-product isomorphism','\\item The natural\ncup-product isomorphism','D08','State the final natural morphism directly.')
edit('is monodromy-equivariant, proving the final assertion.','is monodromy-equivariant. Identity on first cohomology would\ntherefore imply identity on second cohomology.','D08','Replace the outcome recap by its precise implication through the displayed exterior-square isomorphism.')
for number in ['18','19']:
 tag=r'\tag{D.'+number+'}'
 k=after.index(tag);a=after.rfind('\\[',0,k);b=after.index('\\]',k)+2
 old=after[a:b];assert old.count('\\[')==1 and old.count('\\]')==1
 new=old.replace('\\[','\\begin{equation}',1).replace(tag,'',1)
 new=new[:-2]+'\\end{equation}'
 edit(old,new,'D04','Use the paper equation counter while retaining the entire display, label, hypertarget and all label-based references.')

reconstructed=after
for x in reversed(edits):
 off=x['sequential_before_offset'];assert reconstructed[off:off+len(x['after'])]==x['after']
 reconstructed=reconstructed[:off]+x['before']+reconstructed[off+len(x['after']):]
assert reconstructed==before
def displays(t):
 out=[]
 for m in re.finditer(r'\\\[(.*?)\\\]|\\begin\{equation\}(.*?)\\end\{equation\}',t,re.S):
  out.append(re.sub(r'\\tag\{D\.(?:18|19)\}','',m.group(1)if m.group(1)is not None else m.group(2)))
 return out
assert displays(before)==displays(after)
anchors=lambda t:re.findall(r'\\(?:label|hypertarget)\{[^}]+\}',t)
refs=lambda t:re.findall(r'\\(?:ref|eqref|cref|Cref|SeriesRef|CompendiumRef|cite)(?:\[[^\]]*\])?\{[^}]+\}(?:\{[^}]+\})?',t)
assert anchors(before)==anchors(after) and refs(before)==refs(after)
inline=lambda t:re.findall(r'(?<!\\)\$(?!\$)(.*?)(?<!\\)\$',t,re.S)
ib,ia=inline(before),inline(after);changes=[]
for op,a,b,c,d in difflib.SequenceMatcher(None,ib,ia,autojunk=False).get_opcodes():
 if op!='equal':changes.append({'operation':op,'before':ib[a:b],'after':ia[c:d]})
assert all(x['operation']=='delete' for x in changes)
removed=[y for x in changes for y in x['before']]
assert removed==['U','D',r'\langle1\rangle',r'\rho_{\mathscr B}',r'H^2'],removed
assert before.count('\\item ')==after.count('\\item ')==12
bf=D/'S6_SERIES_PUBLISH_II_01GA_original_full_block.tex';af=D/'S6_SERIES_PUBLISH_II_01GA_proposed_full_block.tex';save(bf,before);save(af,after)

items=list(re.finditer(r'\\bibitem(?:\[[^\]]*\])?\{([^}]+)\}',s))
i=next(i for i,x in enumerate(items)if x.group(1)=='Steenbrink1976');a=items[i].start();b=items[i+1].start()
bb=s[a:b];ba=bb.replace('Limits of hodge structures.','Limits of Hodge structures.')
tail='\\newblock URL\n  \\url{https://www.academia.edu/47027671/Limits_of_Hodge_structures}.\n\\newblock \\emph{Verified}.\n'
assert ba.count(tail)==1;ba=ba.replace(tail,'')
bibbefore=D/'S6_SERIES_PUBLISH_II_Steenbrink1976_original_entry.tex';bibafter=D/'S6_SERIES_PUBLISH_II_Steenbrink1976_proposed_entry.tex';save(bibbefore,bb);save(bibafter,ba)
publication=D/'S6_SERIES_PUBLISH_II_Steenbrink_publisher_receipt.json';assert publication.exists()
g1={'id':'II-infra-extra-01GA-publication','statement_id':'cdp:st:D.2.3','tag':'01GA','source_sha256':sha(source),'before':before,'after':after,'type':'D02/D04/D08/D11/D16/D25','reason':'Publish the fully compared logarithmic period proof with exact analytic scope, mathematical bundle terminology and current equation numbering.','literal_edits':edits,'original_full_block':str(bf.relative_to(ROOT)),'original_full_block_sha256':sha(bf),'proposed_full_block':str(af.relative_to(ROOT)),'proposed_full_block_sha256':sha(af),'preservation':{'exact_forward_inverse':True,'all_display_math_identical_after_only_historical_number_tags':True,'all_references_and_citations_identical_in_order':True,'all_labels_and_hypertargets_identical_in_order':True,'all_twelve_mathematical_steps_retained':True,'inline_removals':changes,'inline_removal_witnesses':{'U and D':'The unchanged initial hypotheses define h:U→Δ and the full central divisor with reduced support D. All complex analytic total spaces and all positive multiplicities remain allowed.','iteration_marker':'Only the printed proof-iteration prefix is removed.','rho_B':'Its definition, full local eigenvalue calculation, equivariant spectral sequence and zero-map conclusion remain unchanged. This one occurrence was in an announcement sentence.','H2':'The unchanged proposition conclusion and second proof item name H². The retained final norm contradiction proves that exact claim.'},'D25_bundle_map':'The exact sequence 0→h*Ω¹_Δ(log0)→Ω¹_U(logD)→K¹→0 gives det(K¹)=ω_U(D)⊗h*ω_Δ(0)^−1. The exterior-square identification K²=Λ²K¹ gives the displayed formula. The original phrase determinant of the entire complex would instead use alternating determinants.','D25_coefficient_map':'Both logarithmic differentials preserve J and (t); the locally split θ-sequence restricts to J/(t), giving the exact displayed subquotient sequence. No O-linear de Rham differential is asserted.'},'mathematical_scope_changed':False,'additional_dependency_only':True,'required_197_index_modified':False}
g2={'id':'II-infra-extra-01GA-Steenbrink-bibliography','statement_id':'bib:Steenbrink1976','key':'Steenbrink1976','source_sha256':sha(source),'before':bb,'after':ba,'type':'D08/D18/D23','reason':'Restore Hodge capitalization and retain the verified publisher DOI while removing the third-party copy URL and workflow verification marker.','literal_edits':[{'before':'Limits of hodge structures.','after':'Limits of Hodge structures.','type':'D18/D23','reason':'Match the primary title.'},{'before':tail,'after':'','type':'D08/D18','reason':'The retained DOI resolves to the primary publisher metadata; full journal page locators are confirmed by actual archive scans.'}],'original_entry':str(bibbefore.relative_to(ROOT)),'original_entry_sha256':sha(bibbefore),'proposed_entry':str(bibafter.relative_to(ROOT)),'proposed_entry_sha256':sha(bibafter),'publication_evidence':bind(publication),'preservation':{'citation_key_unchanged':True,'author_journal_volume_year_pages_and_doi_unchanged':True,'cited_edition':'Published 1976 journal edition; exact printed pages viewed in the Göttingen archive scans.'},'mathematical_scope_changed':False}
g={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source_sha256':sha(source),'guards':[g1,g2],'guard_count':2,'literal_edit_count':len(edits)+2,'status':'Prepared only. Full final before/after blocks require actual comparison attestation in a separate receipt.','events_added':0,'canonical_files_modified':False}
gp=D/'S6_SERIES_PUBLISH_II_01GA_guards.json';save(gp,json.dumps(g,indent=2)+'\n')
print(json.dumps(bind(gp)));print('literal_edits',g['literal_edit_count']);print('inline_changes',json.dumps(changes));print('all_preservation_assertions_passed')
