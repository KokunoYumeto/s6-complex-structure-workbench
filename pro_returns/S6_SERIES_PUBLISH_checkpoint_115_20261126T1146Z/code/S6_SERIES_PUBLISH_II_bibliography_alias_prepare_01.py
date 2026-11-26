"""Prepare exact bibliography/citation guards; leave canonical source untouched."""
from pathlib import Path
import datetime,hashlib,json,re
R=Path(__file__).resolve().parents[1]
def bound(p):
 b=(R/p).read_bytes()
 return dict(path=p,bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
source=(R/'S6_SERIES_PUBLISH_II.tex').read_text()
assert hashlib.sha256(source.encode()).hexdigest()=='53b3c435bf45d126b9091236e4f563709b3945b5644f63db68680421cd971816'
ba=source.index(r'\begin{thebibliography}')
bb=source.index(r'\end{thebibliography}',ba)
matches=list(re.finditer(r'\\bibitem(?:\[[^\]]*\])?\{([^}]+)\}',source[ba:bb]))
entries={}
for i,m in enumerate(matches):
 a=ba+m.start();b=ba+(matches[i+1].start() if i+1<len(matches) else bb-ba)
 entries[m.group(1)]=source[a:b]
assert len(entries)==130
aliases={'AC2026':'AC26','AC26Root':'AC26','CDP20':'CDP2020',
         'CDP2020D':'CDP2020','Grauert60':'Grauert1960D',
         'ViaTwo26push':'Viaclovsky2026Two'}
canonical={
'AC26':r'''\bibitem[{Claude} and {L. Alp{\"o}ge}(2026)]{AC26}
{Claude} and {L. Alp{\"o}ge}.
\newblock The $(3,4,\infty)$ modular family of $2$-tori, completed at its three
special points, is a complex structure on $S^6$.
\newblock Manuscript, 108 pages, 2026.
\newblock \url{https://alpo.ge/s6.pdf}.

''',
'CDP2020':r'''\bibitem[Campana et~al.(2020)Campana, Demailly, and Peternell]{CDP2020}
Fr{\'e}d{\'e}ric Campana, Jean-Pierre Demailly, and Thomas Peternell.
\newblock The algebraic dimension of compact complex threefolds with vanishing
second Betti number.
\newblock \emph{Compositio Mathematica}, 156(4):679--696, 2020.
\newblock \doi{10.1112/S0010437X19007802}.

''',
'Grauert1960D':r'''\bibitem[Grauert(1960)]{Grauert1960D}
Hans Grauert.
\newblock Ein Theorem der analytischen Garbentheorie und die Modulr\"aume
komplexer Strukturen.
\newblock \emph{Publications Math\'ematiques de l'IH\'ES}, 5:5--64, 1960.
\newblock \doi{10.1007/BF02684746}.

''',
'Viaclovsky2026Two':r'''\bibitem[Viaclovsky(2026{\natexlab{a}})]{Viaclovsky2026Two}
Jeff Viaclovsky.
\newblock A two-parameter family of complex structures on $S^6$.
\newblock arXiv:2609.33785v1, 2026{\natexlab{a}}.
\newblock \url{https://arxiv.org/abs/2609.33785v1}.

'''}
locator_map={
 r'Lemma~4.6, p.~7 of the attached-source edition':r'Lemma~4.6, p.~685',
 'proof of Proposition~7.3,\np.~16 of the attached-source edition':'proof of Proposition~7.3,\np.~694',
 r'Theorem~2.1, arXiv v2, p.~1':r'Theorem~2.1, p.~679',
 r'Lemma~4.2, arXiv v2, p.~6':r'Lemma~4.2, p.~684'}
body=source[:ba]
pat=r'\\cite[a-zA-Z]*\*?(?:\[[^\]]*\]){0,2}\{([^}]+)\}'
citations=[]
for m in re.finditer(pat,body):
 keys=[x.strip() for x in m.group(1).split(',')]
 if not any(k in aliases for k in keys):continue
 mapped=[]
 for k in keys:
  k=aliases.get(k,k)
  if k not in mapped:mapped.append(k)
 new=m.group(0)[:m.start(1)-m.start()]+','.join(mapped)+m.group(0)[m.end(1)-m.start():]
 for oldloc,newloc in locator_map.items():
  new=new.replace(oldloc,newloc)
 labels=list(re.finditer(r'\\label\{([^}]+)\}',body[:m.start()]))
 citations.append(dict(old=m.group(0),new=new,
  old_source_line=body[:m.start()].count('\n')+1,
  nearby_preceding_label=labels[-1].group(1) if labels else 'preamble',
  type='D18',reason='Map the citation key to the identified work; preserve its locator except for the separately verified published-page relocations.'))
# Exact old/new pairs can repeat; multiplicity is bound explicitly.
grouped={}
for c in citations:
 key=c['old']
 if key not in grouped:grouped[key]=dict(old=c['old'],new=c['new'],type='D18',expected_occurrences=0,locations=[])
 assert grouped[key]['new']==c['new']
 grouped[key]['expected_occurrences']+=1
 grouped[key]['locations'].append({k:c[k] for k in ['old_source_line','nearby_preceding_label']})
guards=list(grouped.values())
for k,new in canonical.items():
 guards.append(dict(old=entries[k],new=new,type='D01,D18,D23',
  expected_occurrences=1,location='Bibliography '+k,
  reason='One entry for this exact work and edition; restore mathematical/proper-name capitalization and keep verification history in the evidence and master bibliography.'))
for old,new in aliases.items():
 guards.append(dict(old=entries[old],new='',type='D18',expected_occurrences=1,
  location='Bibliography '+old,
  reason='Consolidate this exact bibliographic alias under '+new+' after transporting every citation.'))
candidate=source
for g in guards:
 assert candidate.count(g['old'])==g['expected_occurrences'],g['old']
 candidate=candidate.replace(g['old'],g['new'])
for pat in [r'\\label\{([^}]+)\}',r'\\hypertarget\{([^}]+)\}']:
 assert re.findall(pat,source)==re.findall(pat,candidate)
assert len(re.findall(r'\\bibitem(?:\[[^\]]*\])?\{([^}]+)\}',candidate))==124
display_pattern=r'(?<!\\)\\\[(.*?)(?<!\\)\\\]'
assert re.findall(display_pattern,source,re.S)==re.findall(display_pattern,candidate,re.S)
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
primary=dict(created_utc=now,
 scope='Bibliographic identity and four published-page relocations; no new theorem or independent proof-check credit.',
 sources=[
  dict(url='https://www.numdam.org/item/PMIHES_1960__5__5_0/',
   web_ref='turn519998998view0',read='Complete displayed bibliographic metadata, title, author, journal, volume, pages, year, DOI and corrigendum link. No new reading of the 1960 theorem pages is claimed.'),
  dict(url='https://www.cambridge.org/core/journals/compositio-mathematica/article/algebraic-dimension-of-compact-complex-threefolds-with-vanishing-second-betti-number/CDF2D04CFB35CEE105E10B188D97D68A',
   web_ref='turn580573761search0',pdf_web_ref='turn618367331view0',
   pdf_url='https://www.cambridge.org/core/services/aop-cambridge-core/content/view/CDF2D04CFB35CEE105E10B188D97D68A/S0010437X19007802a.pdf/algebraic_dimension_of_compact_complex_threefolds_with_vanishing_second_betti_number.pdf',
   local_reading_source='../primary_continuation2_root_provenance/CDP2020_publisher.pdf',
   sha256='c4cb6408f97dec241d1d1e6f9cc30029f3d51272433717d0592a46ec501898b4',
   actual_rendered_pages_read=[679,684,685,694],
   exact_loci=['Theorem2.1 complete statement,679','Lemma4.2 complete statement and proof,684','Notation4.5 and Lemma4.6 full statement and printed proof citation,685','Proposition7.3 continuation and reducible genus-one inference,694'],
   reading_notes='Read all text on the four displayed pages. Page684 states the original unrestricted component count; the current manuscript uses its own monodromy-corrected argument. This bibliographic operation neither adopts that unrestricted assertion nor credits it as newly proved. Page685 contains the explicit conductor/resolution formulas. Page694 contains the precise nodal-cycle inference criticized by P4.14.',
   generated_but_not_viewed_in_this_pass=['CDP2020-locator-3.png','CDP2020-locator-9.png']),
  dict(url='https://arxiv.org/abs/2609.33785v1',web_ref='turn519998998view2',
   read='Version1 metadata,21 pages,author/title and sole displayed submission history. Earlier recorded full theorem-page readings retain their own scope.'),
  dict(url='https://alpo.ge/s6.pdf',web_ref='turn863870892view0',
   read='Current source title and108-page extent reopened. Existing exact original-version primary readings remain the authority for mathematical locators; no new full-proof reading is claimed.')
 ],
 access_failures=[
  'Direct DOI open for CDP2020 was inaccessible; the publisher article and its exact PDF were successfully opened through the DOI search.',
  'arXiv1904.11179v2 abstract/PDF returned DisabledError. The locator replacements use the actual published named statements and their observed pages; no byte identity of entire editions is asserted.'
 ],
 exact_locator_map=locator_map,
 identity_maps=[
  'AC2026 and AC26Root -> AC26: same specified108-page manuscript URL/title and previously recorded original source.',
  'CDP20 and CDP2020D -> CDP2020: same publisher DOI,title,authors,volume and page range. Explicit preprint/attached-page citations are relocated to the separately read named published results.',
  'Grauert60 -> Grauert1960D: same DOI10.1007/BF02684746 and publisher/archive metadata.',
  'ViaTwo26push -> Viaclovsky2026Two: same arXiv2609.33785 paper, pinned to the observed version1 used by the existing exact locators.'
 ],
 source_changed=False,events_added=0,final_pdf_page_credit=0)
pr='records/S6_SERIES_PUBLISH_II_bibliography_primary_01.json'
assert not (R/pr).exists()
(R/pr).write_text(json.dumps(primary,indent=2)+'\n')
proposal=dict(created_utc=now,basis=bound('S6_SERIES_PUBLISH_II.tex'),
 status='Prepared and reviewed; canonical application waits for the mathematical-order implementation to avoid conflicting block hashes.',
 aliases=aliases,citation_occurrences=len(citations),unique_citation_guards=len(grouped),
 bibliography_entries_before=130,bibliography_entries_after=124,
 guards=guards,primary_evidence=bound(pr),
 complete_removed_bibliography_entries={k:entries[k] for k in aliases},
 unchanged_mathematical_displays=True,unchanged_labels_and_hypertargets=True,
 master_bibliography='Its historical aliases and verification records remain available for the held papers and final five-paper integration.',
 canonical_mutations=0)
out='records/S6_SERIES_PUBLISH_II_bibliography_alias_proposal_01.json'
assert not (R/out).exists()
(R/out).write_text(json.dumps(proposal,indent=2)+'\n')
print(json.dumps(dict(proposal=bound(out),primary=bound(pr),
 citation_occurrences=len(citations),guards=len(guards),
 entries_before=130,entries_after=124),indent=2))
