from pathlib import Path
import hashlib,json,re,datetime,difflib
R=Path(__file__).resolve().parents[3];D=Path(__file__).parent
source=R/'S6_SERIES_PUBLISH_II.tex';s=source.read_text()
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def bind(p):return {'path':str(p.relative_to(R)),'sha256':sha(p),'bytes':p.stat().st_size}
def save(p,t):
    assert not p.exists(),p
    p.write_text(t)
folder=D/'F5_guard_blocks';folder.mkdir(exist_ok=False)
released=R/'agents/ii_infra/released_proofs/01F5/8f59f1260cf17d1b/S6_SERIES_PUBLISH_full_owning_block.tex'
before=released.read_text();assert s.count(before)==1
start=s.index(before);end=start+len(before)

# Token inventory exposes only exact labels/commands and source positions.
tokens=[]
for m in re.finditer(r'(?<![A-Za-z0-9.])C\.PK\.[1-8](?![0-9.])',s):
    pre=s[max(0,m.start()-90):m.start()]
    if re.search(r'\\tag\{$',pre):kind='historical_display_tag'
    elif re.search(r'\\label\{cdp:eq:$',pre):kind='stable_label'
    elif re.search(r'\\(?:ref|eqref|SeriesRef|SRef|SBack|hyperref|hyperlink)[^\n]*\{?cdp:eq:$',pre):kind='stable_label_reference_or_macro'
    elif re.search(r'(?:SRef@|SBack@)cdp:eq:$',pre):kind='identifier_macro'
    elif pre.endswith('cdp:eq:'):kind='stable_identifier_argument'
    else:kind='bare_historical_token'
    tokens.append({'token':m.group(),'start_character':m.start(),'line':s.count('\n',0,m.start())+1,
                  'within_target_owner':start<=m.start()<end,'kind':kind})
outside=[x for x in tokens if not x['within_target_owner'] and x['kind']=='bare_historical_token']
assert not outside,outside
audit={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source':bind(source),
       'target_owner':'cdp:st:C.3.10','scope':'All exact C.PK.1 through C.PK.8 tokens, excluding longer-number/prefix collisions.',
       'tokens':tokens,'outside_owner_bare_tokens':outside,'stable_anchors_retained':True,'events_added':0}
auditpath=D/'S6_SERIES_PUBLISH_II_01F5_exact_number_token_audit.json'
save(auditpath,json.dumps(audit,indent=2)+'\n')

after=before;edits=[]
def edit(old,new,typ,reason,witness=None):
    global after
    assert after.count(old)==1,(old,after.count(old))
    pos=after.index(old);after=after[:pos]+new+after[pos+len(old):]
    row={'before':old,'after':new,'type':typ,'reason':reason,'sequential_before_offset':pos}
    if witness:row['exact_mathematical_witness']=witness
    edits.append(row)
edit('[Proved exclusion of primary Kodaira general fibres]','[Exclusion of primary Kodaira general fibres]',
     'D08/D16','Remove the proof-status adjective from the title.')
edit('A compact complex threefold with','A smooth compact complex threefold with',
     'D25','State the actual smooth total-space domain required by the printed proof and independently derived argument. The potentially singular reading is not asserted.',
     'Complete cited D1.9 requires a manifold; full D1.12 HRR, smooth-centre resolution and the differential-form comparison use smoothness. Every actual receiver is bound to its explicitly smooth domain in the separate source/receiver receipts.')
edit(r'\begin{enumerate}[label={$\langle1\rangle$\arabic*.},leftmargin=*]',
     r'\begin{enumerate}[leftmargin=*]','D04','Remove the historical iteration prefix, preserving all twelve proof items.')
edit('Use the intrinsic quotient and its orientation from (C.SK.2):',
     r'Use the intrinsic quotient and its orientation from \eqref{cdp:eq:C.SK.2}:',
     'D06','Replace the first literal legacy equation locator by the exact existing quotient label.')
edit('Picard quotient in (C.SK.2), hence is a constant integer $k$.',
     r'Picard quotient in \eqref{cdp:eq:C.SK.2}, hence is a constant integer $k$.',
     'D06','Replace the second literal legacy locator by the same exact quotient label.')
edit('It remains to obtain the same contradiction when $k=0$.\n\n\\item In that case',
     '\\item For $k=0$,','D08','Move the exact zero-case condition to the start of its proof item, removing the announcement without changing the condition.')
edit('Here is the actual\nlocal product comparison we use. Borcea\'s',
     'Borcea\'s','D08','Begin directly with the complete marked family used for the local product.')
edit('This proves the needed\nholomorphic local triviality from the specified complete\nfamily.\n','',
     'D08','Remove the repeated outcome immediately after the constant pullback is proved to be a product.')
edit('\\item We compute its entire action on $H^2(P;\\C)$, including\nvertical shears. Write',
     '\\item Write','D08','Begin directly with the group presentation and retain the complete shear computation.',
     'Only the announcement occurrence H^2(P;C) is removed. The statement of the actual identity action and all four basis classes remain in items6–7.')
edit('\\item For clarity, their induced cohomology action can be read\noff without discarding any of those elements. In the real',
     '\\item In the real','D02/D08','Remove the assurance/announcement; every central shear and its exact cohomology image remain.')
edit('\\item We next construct a global section of $\\mathscr G$ by an\nactual morphism of complexes. Resolve',
     '\\item Resolve','D08','Begin directly with the resolution and retain the entire chain map, direct image and global-section construction.',
     'Only the announcement occurrence mathscr G is removed. G is defined in item2 and appears unchanged in C.PK.5–8 and the section construction.')
edit('This section is nowhere zero on $B$; zeros at points\nof $\\Sigma$ cause no problem.',
     'This section is nowhere zero on $B$.','D02','Remove the neighbouring reassurance; the proof only uses nonvanishing on the smooth base.',
     'Sigma is still the specified critical-value set. The global holomorphic section and the H1(P1,O)=0 lifting argument remain exact and require no nonvanishing claim on Sigma.')
edit('This proves constancy of the quotient differential,\nincluding its normalization; it is not a boundedness\nassertion about an unspecified function on $B$.\n','',
     'D02/D08','Remove the conclusion recap and defensive contrast after the complete comparison and C.PK.8.',
     'Only the duplicate smooth-base B mention is removed. The preceding actual global maps, overlap agreement and displayed constant kappa^{-1} retain the precise conclusion.')
edit('contradicting $a(Y)=1$. This completes the proof.',
     'contradicting $a(Y)=1$.','D08','Retain the final contradiction without its completion marker.')
for n in range(1,9):
    tag=rf'\tag{{C.PK.{n}}}';k=after.index(tag);a=after.rfind(r'\[',0,k);b=after.index(r'\]',k)+2
    old=after[a:b];new=old.replace(r'\[',r'\begin{equation}',1).replace(tag,'',1)
    new=new[:-2]+r'\end{equation}'
    edit(old,new,'D04',f'Use the current equation counter for C.PK.{n}, keeping the entire formula, stable label and tag anchor.')

reconstructed=after
for e in reversed(edits):
    p=e['sequential_before_offset'];assert reconstructed[p:p+len(e['after'])]==e['after']
    reconstructed=reconstructed[:p]+e['before']+reconstructed[p+len(e['after']):]
assert reconstructed==before
anchors=lambda t:re.findall(r'\\(?:label|hypertarget)\{[^}]+\}',t)
refs=lambda t:re.findall(r'\\(?:ref|eqref|cref|Cref|SeriesRef|CompendiumRef|cite)(?:\[[^\]]*\])?\{[^}]+\}(?:\{[^}]+\})?',t)
inline=lambda t:re.findall(r'(?<!\\)\$(?!\$)(.*?)(?<!\\)\$',t,re.S)
def displays(t):
    return [re.sub(r'\\tag\{C\.PK\.[1-8]\}','',m.group(1) if m.group(1) is not None else m.group(2))
            for m in re.finditer(r'\\\[(.*?)\\\]|\\begin\{equation\}(.*?)\\end\{equation\}',t,re.S)]
assert anchors(before)==anchors(after)
added_ref=r'\eqref{cdp:eq:C.SK.2}'
assert after.count(added_ref)==2 and before.count(added_ref)==0
assert refs(before)==[x for x in refs(after) if x!=added_ref]
assert displays(before)==displays(after)
assert before.count(r'\item ')==after.count(r'\item ')==12
ib,ia=inline(before),inline(after)
changes=[{'operation':op,'before':ib[a:b],'after':ia[c:d]}
         for op,a,b,c,d in difflib.SequenceMatcher(None,ib,ia,autojunk=False).get_opcodes() if op!='equal']
removed=[v for x in changes for v in x['before']]
assert all(x['operation']=='delete' for x in changes),changes
assert removed==[r'\langle1\rangle',r'H^2(P;\C)',r'\mathscr G',r'\Sigma','B'],removed
bf=folder/'S6_SERIES_PUBLISH_II_01F5_original_full_block.tex'
af=folder/'S6_SERIES_PUBLISH_II_01F5_proposed_full_block.tex'
save(bf,before);save(af,after)
guards=[{'id':'II-infra-recovery-01F5-publication','statement_id':'cdp:st:C.3.10','tag':'01F5',
         'source_sha256':sha(source),'before':before,'after':after,'type':'D02/D04/D06/D08/D16/D25',
         'reason':'Make the actual smooth domain explicit and remove presentation residues while retaining all twelve mathematical steps and the printed logarithmic route.',
         'literal_edits':edits,'original_full_block':str(bf.relative_to(R)),'original_full_block_sha256':sha(bf),
         'proposed_full_block':str(af.relative_to(R)),'proposed_full_block_sha256':sha(af),
         'scope_repair':{'old':'compact complex threefold under the analytic-space convention',
                         'new':'smooth compact complex threefold','broader_singular_claim_verified':False,
                         'receiver_audit':bind(R/'records/S6_SERIES_PUBLISH_II_F5_root_safe_inputs_and_front_scope.json'),
                         'body_receiver_statements':bind(D/'S6_SERIES_PUBLISH_II_01F5_safe_dependencies_receivers.json')},
         'preservation':{'exact_forward_inverse':True,'all_display_formulas_identical_after_only_eight_legacy_tags_removed':True,
                         'all_stable_labels_and_hypertargets_identical_in_order':True,'all_twelve_proof_items_retained':True,
                         'reference_exception':{'added':[added_ref,added_ref],'replaced_literals':['(C.SK.2)','(C.SK.2)'],
                                                'target_label':'cdp:eq:C.SK.2','target_display_sha256':'7910bcc6081a49741c60710ef3b2fe37193de1d07f884af9c720702ba6c283ec'},
                         'all_other_reference_and_citation_tokens_identical_in_order':True,'inline_changes':changes,
                         'inline_removal_witnesses':{r'\langle1\rangle':'iteration prefix only',
                           r'H^2(P;\C)':'announcement only; complete identity action remains',
                           r'\mathscr G':'announcement only; exact sheaf, map and section remain',
                           r'\Sigma':'reassurance only; critical set and every map retain their original scopes',
                           'B':'recap only; actual overlap and constant-quotient derivation remain'},
                         'printed_logarithmic_route_retained':True},
         'primary_evidence':bind(D/'S6_SERIES_PUBLISH_II_01F5_prereading_input_receipt.json'),
         'number_token_audit':bind(auditpath)}]

items=list(re.finditer(r'\\bibitem(?:\[[^\]]*\])?\{([^}]+)\}',s))
def bib(key):
    i=next(i for i,x in enumerate(items) if x.group(1)==key)
    e=items[i+1].start() if i+1<len(items) else s.index(r'\end{thebibliography}',items[i].end())
    return s[items[i].start():e]
def bibguard(key,replacements,evidence,reason,typ='D08/D18'):
    old=bib(key);new=old;literal=[]
    for a,b,t,why in replacements:
        assert new.count(a)==1,(key,a);new=new.replace(a,b,1)
        literal.append({'before':a,'after':b,'type':t,'reason':why})
    bp=folder/f'S6_SERIES_PUBLISH_II_{key}_original_entry.tex'
    ap=folder/f'S6_SERIES_PUBLISH_II_{key}_proposed_entry.tex'
    save(bp,old);save(ap,new)
    assert inline(old)==inline(new)
    guards.append({'id':f'II-infra-recovery-01F5-bib-{key}','statement_id':f'bib:{key}','key':key,
                   'source_sha256':sha(source),'before':old,'after':new,'type':typ,'reason':reason,
                   'literal_edits':literal,'original_entry':str(bp.relative_to(R)),'original_entry_sha256':sha(bp),
                   'proposed_entry':str(ap.relative_to(R)),'proposed_entry_sha256':sha(ap),
                   'publication_evidence':evidence,'preservation':{'citation_key_and_author_year_label_preserved':True,
                    'body_citation_tokens_unchanged':True,'inline_math_identical':True}})
bibguard('Borcea1984',[(r'\newblock \emph{Verified}.','','D08/D18','Remove the workflow marker from the verified bibliographic entry.')],
         {'primary_pdf':bind(D/'F5_F7_GD_primary_inputs/S6_SERIES_PUBLISH_II_Borcea1984_primary.pdf'),
          'primary_record_url':'https://www.numdam.org/item/CM_1984__52_3_373_0/','web_ref':'turn367258764view0',
          'bounded_doi_observation':'The opened Numdam article record and its BibTeX/RIS contain no DOI field. No universal absence claim is made.'},
         'Keep the exact primary publication data and PDF link, removing only the workflow marker.')
old=r'\newblock URL \url{https://arxiv.org/pdf/math/0001077}.'+'\n'+r'\newblock \emph{Verified}.'
new=r'''\newblock \doi{10.1007/978-3-642-56202-0_14}.
\newblock Cited preprint edition: arXiv:math/0001077v2, 28 October 2001;
preprint page and statement locators refer to this edition.
\newblock URL \url{https://arxiv.org/pdf/math/0001077v2}.'''
bibguard('SS2002',[
    ('Irreducible degenerations of primary kodaira surfaces.','Irreducible degenerations of primary {Kodaira} surfaces.','D18/D23','Preserve the primary title with the proper-name capitalization.'),
    (old,new,'D08/D18','Add the verified chapter DOI and bind the byte-matched supplied preprint edition, retaining its page/statement scope.')],
    {'exact_source_version_receipt':bind(D/'F5_F7_GD_primary_inputs/S6_SERIES_PUBLISH_II_SS2002_v2_exact_source_binding.json'),
     'publisher_url':'https://link.springer.com/chapter/10.1007/978-3-642-56202-0_14','publisher_ref':'turn367258764view1',
     'official_arxiv_url':'https://arxiv.org/abs/math/0001077v2','official_arxiv_ref':'turn700198841view0'},
    'Keep the published chapter metadata and distinguish the exact cited preprint edition; restore the title proper name.','D08/D18/D23')
out={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source_sha256':sha(source),
     'guards':guards,'guard_count':len(guards),'literal_edit_count':sum(len(g['literal_edits']) for g in guards),
     'status':'Prepared only; complete final-pair rereading follows and is recorded separately.',
     'events_added':0,'canonical_files_modified':False}
p=D/'S6_SERIES_PUBLISH_II_01F5_guards.json';save(p,json.dumps(out,indent=2)+'\n')
print(json.dumps(bind(p)));print('literal_edits',out['literal_edit_count']);print('inline_changes',json.dumps(changes))
print('outside_owner_bare_tokens',len(outside));print('all_preservation_assertions_passed')
