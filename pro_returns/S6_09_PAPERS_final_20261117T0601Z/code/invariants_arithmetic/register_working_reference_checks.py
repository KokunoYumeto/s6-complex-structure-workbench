"""Record the original-source checks actually performed for the WB appendices."""
from pathlib import Path
import csv, hashlib, json, re

OUT=Path('deliverables/work/invariants_arithmetic')
EXT=Path('sources/audit_cache/inv_ari/working_literature')
META={'checker':'GPT-6 Astra (OpenAI, ChatGPT Pro mode)', 'effort':'Pro', 'date':'2026-11-17'}
rows=[]
def add(key,title,url,locator,use,hyp,filename=None,refs=None,aliases=None):
    p=EXT/filename if filename else None
    rows.append(dict(META, citation_key=key,title=title,url=url,
       status='verified_for_stated_use',verified=True,opened_locator=locator,
       actual_use=use,hypotheses_and_normalization_check=hyp,
       local_source=str(p) if p else None,
       source_sha256=hashlib.sha256(p.read_bytes()).hexdigest() if p else None,
       web_refs=refs or [], aliases=aliases or [],citation_contexts=[],
       extent='Original operative statement and surrounding hypotheses opened; no claim that the full external article was independently reproved.'))

add('AtiyahSinger1963','The index of elliptic operators on compact manifolds',
 'https://scispace.com/pdf/the-index-of-elliptic-operators-on-compact-manifolds-3n33719pz0.pdf',
 'Original journal scan, §3.2 and Theorem 3, published p.427 (PDF p.6); preceding definition of the index, pp.422–425.',
 'Hirzebruch–Riemann–Roch for the holomorphic cotangent bundle in the parameterized Hodge calculation.',
 'The theorem explicitly allows every compact complex manifold and every holomorphic vector bundle. Hermitian metrics define the elliptic Dolbeault operator; no Kähler or projectivity hypothesis occurs. Its Todd class is that of the complex tangent bundle. The appendix independently expands ch(Omega^1) and Td, using c1=c2=0 and integral c3=2.',
 refs=['turn168view1','turn169view0'])
add('Frolicher1955','Relations between the cohomology groups of Dolbeault and topological invariants',
 'https://www.pnas.org/doi/pdf/10.1073/pnas.41.9.641',
 'Original publisher PDF, pp.641–644 in full; Lemmas 1–2 and Theorem 3 on p.643.',
 'E1 equals Dolbeault cohomology and E-infinity is the associated graded complex de Rham cohomology.',
 'The bounded filtration is by holomorphic degree of smooth forms on a complex manifold. The identification and finite stabilization do not require Kählerness. Compactness supplies the finite dimensions used here. The candidate-specific vanishing of higher differentials and exactness of the middle rows are proved in the appendix, not taken from this source.',
 refs=['turn168view0'])
add('Serre1955Duality','Un théorème de dualité',
 'https://www.college-de-france.fr/media/jean-pierre-serre/UPL35645220559164287_Un_theoreme_de_dualite.pdf',
 '§13, Theorem 4, published p.22; §15, cup product and integration, p.23.',
 'Dolbeault–Serre duality for the smooth compact threefold and its cup-product pairing.',
 'The theorem pairs H^q(Omega^p(V)) with H^(n-q)(Omega^(n-p)(V dual)) for a holomorphic vector bundle on a compact complex n-fold. No Kähler assumption is required. Here n=3 and V is trivial. Singular and nonreduced fibres instead use RR70; this smooth theorem is not extended to them.',
 'Serre1955Duality.pdf',refs=['turn149view1'])
add('Grothendieck1957','Sur la classification des fibrés holomorphes sur la sphère de Riemann',
 'https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/AG/AG-25.pdf',
 'Theorem 2.1, published p.126 (PDF p.7), with the preceding holomorphic bundle convention.',
 'Splitting of the locally free direct images on the base P1.',
 'The base is the Riemann sphere and the object is a holomorphic vector bundle. The theorem splits it into line bundles with degrees unique up to permutation. The appendix computes extension groups and degrees directly; it never infers projectivity of the total threefold from this classification.',
 'Grothendieck1957.pdf',refs=['turn150search7'])
add('Deligne1970','Équations différentielles à points singuliers réguliers',
 'https://publications.ias.edu/sites/default/files/Number9.pdf',
 'Chapter II, §3.2 Proposition 3.2 and Lemma 3.2.1, pp.72–73; §3.3.1–3.3.2, pp.73–75; §3.4–3.7, pp.75–78, especially residue isomorphism 3.5.3 and Proposition 3.6.',
 'Locally free logarithmic differentials, the relative monomial conormal sequence, and residues on the normalized strata of a self-crossing divisor.',
 'The analytic version explicitly allows a smooth total space and smooth one-dimensional base with local equation t=product z_i^e_i, positive e_i, and a normal-crossing boundary containing the central fibre. It gives the split local relative logarithmic sequence used here. Normalized strata and their orientation sheaves handle global self-crossing; the degree-one target is the structure sheaf of the normalization, not the unnormalized divisor.',
 'Deligne1970.pdf')
add('KatzOda1968','On the differentiation of de Rham cohomology classes with respect to parameters',
 'https://www.its.caltech.edu/~matilde/GaussManinKatzOda.pdf',
 '§2, equations (5)–(10), published pp.202–204; §3, the Čech connecting description, pp.205–209.',
 'Credit for the smooth Gauss–Manin connecting construction and its exterior-product Leibniz rule.',
 'Katz–Oda assume a smooth algebraic morphism of smooth schemes. The appendix explicitly limits this citation to that formalism. Its logarithmic analytic special-fibre statement is separately derived from Deligne’s local split sequence and the Čech difference of splittings; it does not apply the algebraic theorem to singular analytic fibres.',
 'KatzOda1968.pdf',refs=['turn153view1'])
add('Schweitzer2007','Autour de la cohomologie de Bott–Chern',
 'https://arxiv.org/pdf/0709.3528',
 '§1.a, definitions and algebra; §2.c, Lemma 2.5 and the harmonic duality, pp.9–10; §8.a, pp.25–26, line-bundle transition, curvature and Chern normalization.',
 'Bott–Chern/Aeppli definitions and pairing, Hodge-star duality, and c1_BC(L)=[i F/(2 pi)].',
 'Duality requires a compact complex manifold and a Hermitian metric, without Kählerness. The conjugate-linear star convention has target bidegree (n-p,n-q); the dimension identity agrees with the complex-linear convention after conjugation. The source distinguishes the ordinary Chern class i Theta/(2 pi) from its 2 pi i multiple; the appendix uses the ordinary class consistently.',
 'Schweitzer2007.pdf')
add('Ugarte2000','Hodge numbers of a hypothetical complex structure on the six sphere',
 'https://zaguan.unizar.es/record/165697/files/texto_completo.pdf?version=1',
 'Lemma 2.1 and Proposition 3.1, pp.175–176; Theorem 3.2 and full proof, pp.176–177; Corollary 3.3 and Remark 3.4, p.177.',
 'Historical credit for constraints on Hodge numbers of a complex six-sphere, including second-page symmetry and inequalities.',
 'Theorem 3.2 concerns an arbitrary complex structure on the topological six-sphere, not every compact complex threefold. It gives E3=E-infinity, E2 symmetries and h2^(0,1)=h^(1,2)-h^(1,1)+1. The stronger E2 degeneration here uses independently proved holomorphic-form vanishing and the candidate’s direct images; it is not attributed to Ugarte.',
 'Ugarte2000.pdf')
add('Serre1973','A course in arithmetic',
 'https://www.math.purdue.edu/~jlipman/MA598/Serre-Course%20in%20Arithmetic.pdf',
 'Chapter VII, §3.1 Theorem 3, p.85; §3.2 Theorem 4 and proof, p.88; §3.3 equation (22) and Proposition 5, p.89; visually inspected PDF pp.94–100, printed pp.84–90.',
 'The modular invariant has ramification order two at tau=i, used to compute the scalar Kodaira–Spencer zero.',
 'The valence formula and Theorem 4 proof give a simple zero of G3 at i and no zero of Delta on the upper half-plane. Since j=1728 g2^3/Delta and Delta=g2^3-27g3^2, j-1728=1728*27*g3^2/Delta has exactly a double zero at i. This is a derivation from the opened statements, with Serre’s G3 of weight six identified with the usual E6 up to a nonzero scalar.',
 'Serre1973.pdf',refs=['turn169view2'])
add('StacksProject','The Stacks Project',
 'https://stacks.math.columbia.edu/',
 'Tag 0C6K, Remark 31.15.11; Tag 0B3A, Lemma 20.5.1 and proof; Tag 01XT, Lemma 30.8.1 and its Čech proof.',
 'Cartier modification sequences, Ext^1(O,F)=H^1(F), and the line-bundle cohomology calculation on projective space.',
 'The Ext statement is for ringed spaces. The Cartier exact sequences require a regular section; the elementary modifications here are on the smooth base. Tag 01XT is stated algebraically. The analytic P1 calculation in the appendix is also the same Laurent–Čech computation; no algebraic proper-base-change theorem is asserted for the analytic family.',
 refs=['turn152view0','turn152view1','turn152view2'])
add('AngellaTomassini2013','On the partial-partial-bar lemma and Bott–Chern cohomology',
 'https://arxiv.org/pdf/1402.1954',
 'Author version of Inventiones 192 (2013), pp.71–81; combined Theorems A–B in the introduction (PDF p.2) and §1, pp.2–3.',
 'Credit for the general non-Kählerness inequality and the dimension formulation; the numerical defect table here is calculated directly.',
 'Compact complex manifolds are the sole geometric hypothesis. The inequality is sum over p+q=k of (hBC+hA) at least 2bk; equality for every k characterizes the partial-partial-bar lemma. No equality case is assumed for this threefold. The citation was in the source duplicate statement and should remain credited when its statement is merged.',
 'AngellaTomassini2013.pdf',refs=['turn169view1'])
add('BS76','Algebraic methods in the global theory of complex spaces',
 'https://djvu.online/file/2hQiOnz8WuoQk',
 'Chapter III, §3 Theorem 3.4 and proof pp.116–120; Corollaries 3.5, 3.7 and 3.10 pp.120–122; §4 Theorem 4.12(i)–(iii) and proof pp.134–135.',
 'Analytic cohomology and base change, cohomological flatness, local freeness, and semicontinuity for full scheme fibres.',
 'Properness, coherence and flatness of the coefficient sheaf are required. The constant-dimension converse in Theorem 4.12(ii) additionally requires a reduced base, satisfied by P1 and the discs here. The fibres themselves may be nonreduced. Corollary 3.10 identifies local freeness of all higher images with cohomological flatness in the bounded range.',
 refs=['turn157view1','turn159view0','turn159view1','turn160view0','turn160view1'],aliases=['BanicaStanasila1976','BS76push'])
add('Cartan1954Quotient','Quotient d’une variété analytique par un groupe discret d’automorphismes',
 'https://www.numdam.org/item/SHC_1953-1954__6__A12_0/',
 'Exposé 12, §1, conditions (I)–(II), pp.1–2, and Theorem 1, p.2; original PDF first three pages including cover read locally.',
 'Analytic quotient structure in the finite free quotient charts.',
 'The action has a Hausdorff quotient, finite stabilizers, and neighborhoods meeting only stabilizer translates. A finite group acting on the Hausdorff manifold here satisfies these conditions. The theorem gives a normal analytic space; smoothness of the free quotient is separately proved by disjoint local charts.',
 aliases=['Cartan1954'])
rows[-1]['local_source']='sources/external/maps_audit/cartan1954_quotient.pdf'
rows[-1]['source_sha256']=hashlib.sha256(Path(rows[-1]['local_source']).read_bytes()).hexdigest()

# These original scans were checked by the parallel CDP writing-run reader.
# Preserve that provenance instead of claiming a second original-source read.
cdp=json.loads(Path('deliverables/work/cdp_audit/references_verified.json').read_text())
for key in ['Grauert1960','RR70','RRV71']:
    a=next(x for x in cdp if x.get('key')==key)
    r=dict(META,citation_key=key,title=a['title'],url=a['url'],
      status='verified_for_stated_use',verified=True,
      opened_locator='; '.join(a['opened_locators']),
      actual_use={'Grauert1960':'Proper direct-image coherence in the working structure-sheaf proof; base change uses the separately opened BS76 statements.',
                 'RR70':'Serre duality on the compact possibly nonreduced Gorenstein Cartier fibres.',
                 'RRV71':'Relative analytic duality for the proper flat Gorenstein surface family over the smooth curve.'}[key],
      hypotheses_and_normalization_check=a['verification_scope'],
      local_source=a.get('local_pdf'),source_sha256=a.get('sha256'),
      web_refs=a.get('web_refs',[]),aliases=a.get('aliases',[]),citation_contexts=[],
      original_check_provenance={'agent':'/root/cdp_audit','record':'work/cdp_audit/references_verified.json','citation_key':key,'recorded_checker':a['own_check']},
      extent='Original-source reading is the recorded parallel writing-run check; this reader separately matched the WB application to those precise hypotheses.')
    if key=='RRV71':r['original_page_files']=a['original_page_files']
    rows.append(r)

files=list(OUT.glob('working_*proofs.tex'))
for r in rows:
    keys=[r['citation_key']]+r.get('aliases',[])
    for p in files:
        s=p.read_text()
        for m in re.finditer(r'\\cite\w*\*?(?:\[[^\]]*\])*\{([^}]+)\}',s):
            if any(k in m.group(1).split(',') for k in keys):
                r['citation_contexts'].append({'file':str(p),'line':s[:m.start()].count('\n')+1,
                  'context':s[max(0,m.start()-180):min(len(s),m.end()+220)]})
    if r['citation_key']=='AngellaTomassini2013':
        r['citation_contexts'].append({'file':'sources/overleaf_working_edition/supporting_materials/workbench/hodge_frolicher.tex',
          'context':'Original duplicate Bott–Chern table statement: non-Kählerness degrees credited to Theorem A. Statement merged; provenance retained.'})

(OUT/'working_references_verified.json').write_text(json.dumps(rows,indent=2,ensure_ascii=False)+'\n')
ledger=json.loads((OUT/'references_verified.json').read_text())
bykey={r['citation_key']:r for r in ledger}
bykey.update({r['citation_key']:r for r in rows})
(OUT/'references_verified.json').write_text(json.dumps(list(bykey.values()),indent=2,ensure_ascii=False)+'\n')

# Enrich, without changing proof outcome or reviewer records, each WB row with
# its actual external citation dependencies and check-record destinations.
inventory=json.loads((OUT/'working_edition_inventory.json').read_text())
alias={a:r['citation_key'] for r in bykey.values() for a in r.get('aliases',[])}
for row in inventory:
    p=Path('deliverables')/row['extracted_file']
    text=p.read_text()
    keys=[]
    for m in re.finditer(r'\\cite\w*\*?(?:\[[^\]]*\])*\{([^}]+)\}',text):
        keys.extend(alias.get(k.strip(),k.strip()) for k in m.group(1).split(','))
    # McHugh is a bibliography-year alias resolved in the checked candidate.
    keys=['McHugh2018' if k=='McHugh2019' else k for k in keys]
    row['reference_dependencies']=sorted(set(row.get('reference_dependencies',[])+keys))
    row['reference_check_records']=[{'citation_key':k,'record':'work/invariants_arithmetic/references_verified.json',
       'status':bykey[k]['status']} for k in row['reference_dependencies'] if k in bykey]
(OUT/'working_edition_inventory.json').write_text(json.dumps(inventory,indent=2,ensure_ascii=False)+'\n')
with (OUT/'working_edition_inventory.csv').open('w',newline='') as f:
    fields=list(inventory[0]);w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
    for r in inventory:w.writerow({k:json.dumps(v,ensure_ascii=False) if isinstance(v,(dict,list)) else v for k,v in r.items()})
print(json.dumps({'new_working_checks':len(rows),'total_references':len(bykey),
  'verified':sum(r.get('verified',False) for r in bykey.values()),
  'unverified':[k for k,r in bykey.items() if not r.get('verified',False)]},indent=2))
