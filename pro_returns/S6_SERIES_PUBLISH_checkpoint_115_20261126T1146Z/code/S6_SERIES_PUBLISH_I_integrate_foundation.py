from pathlib import Path
import json,hashlib,datetime
from S6_SERIES_PUBLISH_editing import Editor

r=Path(__file__).resolve().parents[1]
p=r/'agents/i_topology/S6_SERIES_PUBLISH_I_E31_foundation_guarded_patches.json'
d=json.loads(p.read_text()); ed=Editor('I')
old=d['patches'][0]['old']
new=d['patches'][0]['new']
new=new.replace('For every root lift $\\bar f:X\\to\\mathfrak B_{k,l}=\\mathbb P(3k,4l)$\nof the retained coprime-multiplicity construction,',
    'Let $k,l$ be positive integers with $\\gcd(3k,4l)=1$.\nFor the root lift $\\bar f:X\\to\\mathfrak B_{k,l}=\\mathbb P(3k,4l)$\nof the construction in \\cref{fam:src:B.3.1},')
new=new.replace('is the original smooth proper torus family','is the smooth proper torus family')
new=new.replace('At the cusp the unchanged local charts','At the cusp the local charts')
new=new.replace('The original constant-dimension formulation is','The constant-dimension formulation also appears in')
new=new.replace('with the original stabilizer representations','with their stabilizer representations')
new=new.replace('{RR70}','{RR70push}')
heading=r'\subsection{Analytic foundations and the version 1}\hypertarget{tag-02ZG}{}\label{push:section:E.3}'
ed.replace(heading+'\n'+old,'','D14',
    'Move the complete root-atlas base-change and trace proof before its first direct-image use, preserving its section and statement identities.',
    'push:src:E.3.1')
anchor=r'\subsection{Local logarithmic bundles and a duality calculation}'
ed.replace(anchor,
    r'\subsection{Root-atlas cohomology and logarithmic bundles}\hypertarget{tag-02ZG}{}\label{push:section:E.3}'+'\n\n'+new,
    'D06','Restore the operative local-model proof with the precise Grauert, Banica–Stanasila and analytic trace citations. State the positive coprime multiplicity hypothesis explicitly.',
    'push:src:E.3.1:placement')
bib=d['patches'][1]['new']
import re
bib=re.sub(r'\. Verified source for the precisely cited statement or methodological fact:.*?2026\.', '.', bib)
bib=bib.replace('{RR70}','{RR70push}')
ed.replace(d['patches'][1]['old'],bib,'D18',
    'Add the two precise analytic-duality primary works. RR70push is the shared-bibliography identity of the same 1970 article; verification history stays outside the paper.',
    'bibliography:analytic-duality')
ed.save()

bp=r/'S6_SERIES_PUBLISH_references.bib';s=bp.read_text();before=s
assert '@article{RRV71,' not in s
s+='''
@article{RRV71,
  author = {Ramis, Jean-Pierre and Ruget, Gabriel and Verdier, Jean-Louis},
  title = {Dualit{\\'e} relative en g{\\'e}om{\\'e}trie analytique complexe},
  journal = {Inventiones Mathematicae},
  volume = {13},
  pages = {261--283},
  year = {1971},
  doi = {10.1007/BF01406078},
  verification = {verified at listed scope},
  source_note = {Current run: original full-article OCR transcription opened at introduction equation (1), page 261; Section 1, pages 264--265; Proposition 2.1, page 266. Publisher PDF download failed; no fresh scan-view or PDF-hash claim. See agents/i_topology/literature/S6_SERIES_PUBLISH_current_primary_locators.json.}
}
'''
bp.write_text(s)
(r/'records/S6_SERIES_PUBLISH_I_foundation_integration.json').write_text(json.dumps({
    'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'guard_source':str(p.relative_to(r)),
    'root_reading':'Full old/new guard and complete first-four/E21-D12 comparisons read before integration.',
    'dependency_repair':'Local atlas, flatness, constant (1,2,1) cohomology and trace precede all direct-image calculations; no global splitting is used in this proof.',
    'source_scope_receipt':'agents/i_topology/literature/S6_SERIES_PUBLISH_current_primary_locators.json',
    'same_work_key_map':{'RR70':'RR70push'},
    'bibliography_before_sha256':hashlib.sha256(before.encode()).hexdigest(),
    'bibliography_after_sha256':hashlib.sha256(s.encode()).hexdigest()
},indent=2)+'\n')
