"""Append scoped source openings without changing or deleting prior records."""
from pathlib import Path
import hashlib, json

R = Path('/workspace/scratch/037cd144174c')
O = R / 'deliverables/work/maps_audit'
BASE = 'sources/external/maps_audit/'
reader = {'reader': 'GPT-6 Astra (OpenAI, ChatGPT Pro mode)',
          'effort': 'Pro', 'date': '2026-11-17'}

def artifact(name, kind):
    p = R / BASE / name
    return {'source': str(p.relative_to(R)), 'sha256': hashlib.sha256(p.read_bytes()).hexdigest(),
            'artifact_type': kind}

records = [
 {'key':'Beardon1983', 'url':'https://ru.djvu.online/file/s9XGIhPaw1MHy',
  'edition_opened':'1986 Russian translation, section 10.6; English corrected second printing, section 7.38 only',
  'opened_locators':['Definition 10.6.1, pp.247–248 (translation)', 'Definition 10.6.3 and Theorem 10.6.4, forward implication and proof, pp.249–250 (translation)', 'English section 7.38, Theorem 7.38.2 and subsequent parabolic criterion, pp.179–181'],
  'verification_scope':'The actual triangle has angles pi/3, pi/4, 0. Reflection products give its elliptic rotations and parabolic cusp; the orientation-preserving subgroup has index two. The forward signature construction supplies the unique parabolic conjugacy class. The manuscript proves simultaneous reversal by explicit products and reduced words.',
  'limits':'English section 10.6 NOT opened; no assertion of its page-level verification. The converse of Theorem 10.6.4 is not used. Translation page numbers are not English page numbers.',
  'applications':['WORK:lem:triangle-generator-orientations'],
  'artifacts':[artifact('wb_foundation_final_open.json','web-rendered primary translation excerpt'), artifact('wb_beardon_and_fulton_open.json','web-rendered English primary-text excerpts')],
  'status':'verified in the specified translation and English section 7.38 scopes'},
 {'key':'Serre1973', 'url':'https://www.math.purdue.edu/~jlipman/MA598/Serre-Course%20in%20Arithmetic.pdf',
  'edition_opened':'1973 Springer English edition, original scanned pages',
  'opened_locators':['Chapter VII, Theorems 1–2, pp.78–79', 'Theorem 3, p.85', 'Theorem 4 and Proposition 5, pp.88–89', 'Proposition 8 and normalized Fourier expansions, pp.92–93'],
  'verification_scope':'The modular quotient has stabilizer orders 3 and 2, j has values 0 and 1728 there, is unramified elsewhere, and identifies the quotient with the affine line. The printed Fourier expansions give j(q)=q^(-1)(1+O(q)). These match local degrees 3 and 4 of the source map, so both deleted meridians act trivially on the lift.',
  'limits':'The nondegenerate period construction and its analytic estimates are separate manuscript proofs, not consequences attributed to Serre.',
  'applications':['WORK:prop:period-input-audit'],
  'artifacts':[artifact('serre1973.pdf','original book scan')],
  'status':'verified in the specified scope'},
 {'key':'Brown1982', 'url':'https://ru.djvu.online/file/QtlfpGD38sXAT',
  'edition_opened':'1982 Springer English edition, web-rendered original text',
  'opened_locators':['Chapter I section 5, bar boundary (5.2), pp.18–19', 'Chapter VII section 5, cohomology and cup products, pp.170–171', 'Chapter VII section 6, Theorem 6.3 and cohomology version, pp.171–172'],
  'verification_scope':'The group extension has normal subgroup Lambda, cyclic quotient C_m, and trivial integral coefficients. The contractible universal cover identifies space and group cohomology; conjugation gives the displayed exterior-power action. Brown supplies the multiplicative Hochschild–Serre sequence. The specific transgression is independently computed from the section factor set in the accompanying supplement.',
  'limits':'The downloaded HTML is a CAPTCHA and is not a source artifact. The preserved web-rendered original excerpts are the evidence. The explicit extension transgression is not claimed to be printed in these Brown pages.',
  'applications':['WORK:prop:finite-indices'],
  'artifacts':[artifact('wb_brown_final_scope.json','web-rendered original book excerpt'),artifact('wb_source_group_and_orbits.json','web-rendered original bar-resolution excerpt')],
  'status':'verified in the specified scope'},
 {'key':'Cartan1954Quotient', 'url':'https://www.numdam.org/item/SHC_1953-1954__6__A12_0.pdf',
  'edition_opened':'Original 1953–1954 seminar, Exposé 12',
  'opened_locators':['Section 1, conditions (I)–(II), pp.1–2', 'Theorem 1, p.2'],
  'verification_scope':'Finite group action on the Hausdorff complex manifold satisfies orbit separation, finite stabilizers and the stated local separation condition. Cartan supplies the analytic quotient and invariant structure sheaf. In the finite fillings the action is free, and the manuscript separately proves smoothness using disjoint translated charts.',
  'limits':'Smoothness is not inferred for an arbitrary nonfree finite quotient.',
  'applications':['WORK:ffcert:prop:quotient-charts'],
  'artifacts':[artifact('cartan1954_quotient.pdf','original seminar scan')],
  'status':'verified in the specified scope'},
 {'key':'Fulton1993', 'url':'https://www.scribd.com/document/768783720/Introduction-to-Toric-Varieties-Fulton',
  'edition_opened':'Reproduction of 1993 book, including 1996 errata page',
  'opened_locators':['Section 1.2, separation lemma and Proposition 3, pp.13–14', 'Section 1.3, affine toric charts and face localization, pp.15–19', 'Section 1.4, fan gluing and closed-diagonal lemma, pp.20–22'],
  'verification_scope':'Rational strongly convex cones and their common faces give the affine semigroup charts and open gluing used in the manuscript. The source assumes finite fans by default. The countable fan and proper cusp quotient require the manuscript’s additional explicit arguments.',
  'limits':'Chapter 3 has not been opened. Replace its broad citation for orbit correspondence by Cox–Little–Schenck Theorem 3.2.6. Divisor/line-bundle applications elsewhere are outside this verification scope.',
  'applications':['WORK:thm:candidate-cusp-geometry'],
  'artifacts':[artifact('wb_foundation_final_open.json','web-rendered original book excerpt'),artifact('wb_foundation_final_find.json','web-rendered original book excerpt')],
  'status':'verified in the specified Chapter 1 scope'},
 {'key':'CoxLittleSchenck2011', 'url':'https://pi.math.cornell.edu/~tsh/cornell-only/cox-little-schenck-toric.pdf',
  'edition_opened':'Authors’ 2010 prepublication text; final bibliographic edition 2011',
  'opened_locators':['Lemma 1.2.13, pp.28–29', 'Definition 3.1.2, Proposition 3.1.3 and Theorem 3.1.5, pp.106–108', 'Theorem 3.2.6 and Proposition 3.2.7, pp.119–121', 'Proposition 12.1.9 and Theorem 12.1.10, pp.565–567'],
  'verification_scope':'Pairwise cone separation, affine gluing, and orbit correspondence match each finite collection of manuscript charts. The source’s fan definition is finite; the infinite-fan extension is independently proved. The fundamental-group result is checked for corroboration, while the candidate now prints its own ray-disc and transversality proof.',
  'limits':'Opened edition is the authors’ 2010 text, not a downloaded 2011 final-edition scan. Binary downloads returned HTTP 403; preserved rendered excerpts are the source evidence. No unexamined divisor theorem is certified.',
  'applications':['WORK:thm:candidate-cusp-geometry','WORK:prop:geometric-pi1'],
  'artifacts':[artifact('wb_sources_cls_open.json','web-rendered author prepublication excerpt'),artifact('wb_source_group_and_orbits.json','web-rendered author prepublication excerpt'),artifact('wb_source_last_open.json','web-rendered author prepublication excerpt')],
  'status':'verified in the specified author-prepublication scope'}
]
for x in records:
    x.update(reader)
    x['source'] = [a['source'] for a in x['artifacts']]
    x['sha256'] = x['artifacts'][0]['sha256']
    x['sha256_scope'] = x['artifacts'][0]['artifact_type']
(O/'wb_foundation_source_checks.json').write_text(json.dumps(records,indent=2,ensure_ascii=False)+'\n')
p=O/'references_verified.json'; existing=json.loads(p.read_text())
for x in records:
    old=next((y for y in existing if y.get('key')==x['key']),None)
    if old is None: existing.append(x)
    elif old != x:
        x['previous_record']=old
        existing[existing.index(old)]=x
p.write_text(json.dumps(existing,indent=2,ensure_ascii=False)+'\n')
print('Persisted six scoped entries; reference ledger entries:',len(existing))
