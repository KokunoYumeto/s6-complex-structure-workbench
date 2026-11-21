from pathlib import Path
import json, hashlib, re, datetime, difflib

ROOT = Path(__file__).resolve().parents[3]
D = Path(__file__).parent
source = ROOT / 'S6_SERIES_PUBLISH_II.tex'
s = source.read_text()

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def bind(p): return {'path': str(p.relative_to(ROOT)), 'sha256': sha(p), 'bytes': p.stat().st_size}
def save(p, t):
    assert not p.exists(), p
    p.write_text(t)

folder = D / 'F7_guard_blocks'
folder.mkdir(exist_ok=False)
released = ROOT / 'agents/ii_infra/released_proofs/01F7/42eebc7bba55472f/S6_SERIES_PUBLISH_full_owning_block.tex'
before = released.read_text()
assert s.count(before) == 1
after = before
edits = []

def edit(old, new, typ, reason, witness=None):
    global after
    assert after.count(old) == 1, (old, after.count(old))
    a = after.index(old)
    after = after[:a] + new + after[a+len(old):]
    e = {'before': old, 'after': new, 'type': typ, 'reason': reason,
         'sequential_before_offset': a}
    if witness: e['exact_mathematical_witness'] = witness
    edits.append(e)

edit('[Proved exclusion of Inoue general fibres]', '[Exclusion of Inoue general fibres]',
     'D08/D16', 'Remove the proof-status adjective from the mathematical title.')
edit(r'\begin{enumerate}[label={$\langle1\rangle$\arabic*.},leftmargin=*]',
     r'\begin{enumerate}[leftmargin=*]', 'D04',
     'Remove the historical iteration prefix while preserving the eight logical proof items.')
edit('\\item We first establish the precise family construction needed for the\nassertion about $H^1$. Write',
     '\\item Write', 'D08', 'Begin directly with the family and its notation.',
     'The only removed mathematical token is the announcement occurrence H^1. The exact H^1(Y;R) conclusion remains in the unchanged statement and in the retained final extension display C.IN.6.')
edit('\\item We prove that these forms agree on overlaps, including base\ndirections. Over',
     '\\item Over', 'D08', 'Begin directly with the overlap and the actual lifted transition. The subsequent whole-family differential identity retains base-direction compatibility.')
edit('\\item We now check every meridian of the divisor\n', '\\item Put\n',
     'D08', 'Introduce the divisor and transverse disc directly.')
edit('This follows by trivializing the pulled-back constant transition\ncocycle on the simply connected covering space; it requires no\nextension of a family trivialization across $D$.',
     'This follows by trivializing the pulled-back constant transition\ncocycle on the simply connected covering space.',
     'D02/D11', 'Retain the complete cocycle construction and remove its neighbouring extension disclaimer.',
     'The map W is constructed on the punctured-disc universal cover from the stated constant cocycle. The reduced divisor D and every transverse-disc hypothesis remain. No family trivialization across D is introduced.')
edit('\\item For clarity, the exact topological extension is as follows.\nThe map',
     '\\item The map', 'D08', 'Start directly with the homology map and retain the full meridian-kernel argument.')
edit('This proves the asserted extension and the obstruction $b_1(Y)>0$.',
     'Consequently $b_1(Y)>0$.', 'D08', 'Keep the actual Betti-number deduction and remove the duplicate outcome recap.')
edit('\\item We finish by explaining why a very general Inoue fibre in \\ref{cdp:st:C.3.1}\nplaces the entire smooth locus in this situation. Ehresmann\'s',
     '\\item Suppose a very general smooth fibre under the hypotheses of\n\\ref{cdp:st:C.3.1} is an Inoue surface. Ehresmann\'s',
     'D08', 'State the contradiction hypothesis directly before the retained diffeomorphism and group arguments.')
edit('contradicts $b_1(Y)=0$ and completes the exclusion.',
     'contradicts $b_1(Y)=0$.', 'D08', 'Retain the final contradiction without a completion marker.')

for n in range(1, 7):
    tag = rf'\tag{{C.IN.{n}}}'
    k = after.index(tag)
    a = after.rfind(r'\[', 0, k)
    b = after.index(r'\]', k) + 2
    old = after[a:b]
    new = old.replace(r'\[', r'\begin{equation}', 1).replace(tag, '', 1)
    new = new[:-2] + r'\end{equation}'
    edit(old, new, 'D04', f'Use the current paper equation counter for C.IN.{n}, preserving the exact formula, label and hypertarget.')

reconstructed = after
for e in reversed(edits):
    a = e['sequential_before_offset']
    assert reconstructed[a:a+len(e['after'])] == e['after']
    reconstructed = reconstructed[:a] + e['before'] + reconstructed[a+len(e['after']):]
assert reconstructed == before

anchors = lambda t: re.findall(r'\\(?:label|hypertarget)\{[^}]+\}', t)
refs = lambda t: re.findall(r'\\(?:ref|eqref|cref|Cref|SeriesRef|CompendiumRef|cite)(?:\[[^\]]*\])?\{[^}]+\}(?:\{[^}]+\})?', t)
inline = lambda t: re.findall(r'(?<!\\)\$(?!\$)(.*?)(?<!\\)\$', t, re.S)
def displays(t):
    return [re.sub(r'\\tag\{C\.IN\.[1-6]\}', '', m.group(1) if m.group(1) is not None else m.group(2))
            for m in re.finditer(r'\\\[(.*?)\\\]|\\begin\{equation\}(.*?)\\end\{equation\}', t, re.S)]
assert anchors(before) == anchors(after)
assert refs(before) == refs(after)
assert displays(before) == displays(after)
assert before.count(r'\item ') == after.count(r'\item ') == 8
ib, ia = inline(before), inline(after)
changes = [{'operation': op, 'before': ib[a:b], 'after': ia[c:d]}
           for op,a,b,c,d in difflib.SequenceMatcher(None, ib, ia, autojunk=False).get_opcodes() if op != 'equal']
assert all(x['operation'] == 'delete' for x in changes)
removed = [v for x in changes for v in x['before']]
assert removed == [r'\langle1\rangle', 'H^1', 'D'], removed

bf = folder / 'S6_SERIES_PUBLISH_II_01F7_original_full_block.tex'
af = folder / 'S6_SERIES_PUBLISH_II_01F7_proposed_full_block.tex'
save(bf, before); save(af, after)
input_receipt = D / 'S6_SERIES_PUBLISH_II_01F7_primary_inputs_receipt_v2.json'
version_receipt = D / 'F7_primary_inputs/S6_SERIES_PUBLISH_II_KT_v4_source_binding_receipt.json'
assert json.loads(version_receipt.read_text())['exact_byte_matches'] == ['ClassificationInoue-article-new.tex']
guards = [{
    'id': 'II-infra-recovery-01F7-publication', 'statement_id': 'cdp:st:C.3.12', 'tag': '01F7',
    'source_sha256': sha(source), 'before': before, 'after': after,
    'type': 'D02/D04/D08/D11/D16',
    'reason': 'Retain the complete proved family/meridian obstruction while removing iteration labels, announcements, a redundant extension disclaimer and proof-status wording.',
    'literal_edits': edits,
    'original_full_block': str(bf.relative_to(ROOT)), 'original_full_block_sha256': sha(bf),
    'proposed_full_block': str(af.relative_to(ROOT)), 'proposed_full_block_sha256': sha(af),
    'preservation': {
        'exact_forward_inverse': True,
        'complete_statement_math_and_hypotheses_unchanged': True,
        'all_display_math_identical_after_only_six_CIN_number_tags_removed': True,
        'all_labels_hypertargets_references_citations_identical_in_order': True,
        'eight_proof_items_preserved': True, 'inline_changes': changes,
        'named_inline_removal_witnesses': {
            r'\langle1\rangle': 'Historical iteration label only; eight proof items remain.',
            'H^1': 'Announcement token only; unchanged statement and C.IN.6 give the complete H^1(Y;R) assertion.',
            'D': 'Neighbouring-extension disclaimer only; D=Y\\Ycirc, its transverse disc and full meridian argument remain.'
        },
        'finite_etale_quotient_argument_retained': True,
        'mathematical_statement_scope_changed': False
    }, 'primary_evidence': bind(input_receipt)
}]

items = list(re.finditer(r'\\bibitem(?:\[[^\]]*\])?\{([^}]+)\}', s))
def bib(key):
    i = next(i for i,m in enumerate(items) if m.group(1) == key)
    end = items[i+1].start() if i+1 < len(items) else s.index(r'\end{thebibliography}', items[i].end())
    return s[items[i].start():end]

def bib_guard(key, replacements, reason, evidence):
    old = bib(key); new = old; literal=[]
    for a,b,typ,why in replacements:
        assert new.count(a) == 1, (key,a)
        new = new.replace(a,b,1)
        literal.append({'before':a,'after':b,'type':typ,'reason':why})
    bp=folder/f'S6_SERIES_PUBLISH_II_{key}_original_entry.tex'
    ap=folder/f'S6_SERIES_PUBLISH_II_{key}_proposed_entry.tex'
    save(bp,old);save(ap,new)
    guards.append({'id':f'II-infra-recovery-01F7-bib-{key}','statement_id':f'bib:{key}','key':key,
      'source_sha256':sha(source),'before':old,'after':new,'type':'D08/D18','reason':reason,
      'literal_edits':literal,'original_entry':str(bp.relative_to(ROOT)),'original_entry_sha256':sha(bp),
      'proposed_entry':str(ap.relative_to(ROOT)),'proposed_entry_sha256':sha(ap),
      'publication_evidence':evidence,'preservation':{'citation_key_preserved':True,'body_citation_tokens_unchanged':True,'inline_math_identical':inline(old)==inline(new)},
      'mathematical_scope_changed':False})

bib_guard('Inoue1974',[(r'\newblock URL \url{https://doi.org/10.1007/BF01425563}.'+'\n'+r'\newblock \emph{Verified}.','', 'D08/D18','Retain the existing DOI macro, removing its duplicate URL and the workflow marker.')],
          'Retain the verified original publication metadata and DOI in the bibliography style.',
          {'primary_article':bind(D/'F7_primary_inputs/S6_SERIES_PUBLISH_II_Inoue1974_primary_article.pdf'),
           'identity_receipt':bind(D/'F7_primary_inputs/S6_SERIES_PUBLISH_II_Inoue1974_article_identity_receipt.json'),
           'publisher_url':'https://link.springer.com/article/10.1007/BF01425563','publisher_ref':'turn163422574view2'})

old=r'\newblock URL \url{https://arxiv.org/pdf/2406.15158}.'+'\n'+r'\newblock \emph{Verified}.'
new=r'''\newblock Published in \emph{Journal of Mathematical Sciences, The University
of Tokyo}, 33(3):283--357, 2026.
\newblock Cited preprint edition: arXiv:2406.15158v4, 13 July 2026;
preprint page and statement locators refer to this edition.
\newblock URL \url{https://arxiv.org/pdf/2406.15158v4}.'''
bib_guard('KhaledTeleman2026',[(old,new,'D08/D18','Bind the exact attached-source edition and retain its explicit cited-preprint scope alongside the verified publication metadata.')],
          'The downloaded v4 source matches the supplied TeX byte for byte; the publisher PDF supplies journal metadata. Preserve the preprint key and edition locators.',
          {'version_binding':bind(version_receipt),'published_pdf':bind(D/'F7_primary_inputs/S6_SERIES_PUBLISH_II_KhaledTeleman_Tokyo2026_primary.pdf'),
           'primary_urls':['https://arxiv.org/abs/2406.15158v4','https://arxiv.org/src/2406.15158v4','https://www.ms.u-tokyo.ac.jp/journal/33-3-1.pdf'],
           'bounded_doi_observation':'No DOI is displayed in the retrieved publisher PDF; no universal nonexistence assertion is made.',
           'actual_preprint_pdf_pages':45,'publisher_pdf_pages':75})
bib_guard('KhaledTeleman2026Journal',[
          ('On the classification of inoue surfaces.','On the classification of {Inoue} surfaces.','D18','Restore the proper-name capitalization from the publisher title.'),
          (r'\newblock \emph{Verified}.','', 'D08/D18','Remove the workflow marker while retaining the complete published-edition record and URL.')],
          'Keep the separately cited published edition and correct its title transcription.',
          {'publisher_pdf':bind(D/'F7_primary_inputs/S6_SERIES_PUBLISH_II_KhaledTeleman_Tokyo2026_primary.pdf'),'publisher_url':'https://www.ms.u-tokyo.ac.jp/journal/33-3-1.pdf','publisher_ref':'turn865022165view1'})
bib_guard('BMS2012',[
          ('3-manifold groups, k\\\"ahler groups and complex surfaces.','3-manifold groups, {K\\\"ahler} groups and complex surfaces.','D18','Restore the proper-name capitalization while preserving the published title wording.'),
          (r'\newblock \emph{Verified}.',r'''\newblock Cited author preprint: 27 October 2011; preprint page and statement
locators refer to the linked author edition.''','D08/D18','State the actual date of the linked author PDF and separate its locators from the retained 2012 journal record.')],
          'Preserve all published metadata and DOI while binding the actual author PDF used for the cited structure statements.',
          {'author_pdf':bind(D/'F5_F7_GD_primary_inputs/S6_SERIES_PUBLISH_II_BMS2012_primary.pdf'),
           'registry':bind(D/'F7_primary_inputs/S6_SERIES_PUBLISH_II_BMS2012_registry.json'),
           'primary_urls':['https://mathweb.tifr.res.in/~mahan/kahler3fld.pdf','https://api.crossref.org/works/10.1142/S0219199712500381']})

out = {'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source_sha256':sha(source),
       'guards':guards,'guard_count':len(guards),'literal_edit_count':sum(len(g['literal_edits']) for g in guards),
       'status':'Prepared only; actual complete final-pair reading is recorded separately.',
       'events_added':0,'canonical_files_modified':False}
p=D/'S6_SERIES_PUBLISH_II_01F7_guards.json';save(p,json.dumps(out,indent=2)+'\n')
print(json.dumps(bind(p)));print('literal_edits',out['literal_edit_count']);print('inline_changes',json.dumps(changes))
print('all_preservation_assertions_passed')
