"""Generate the common convention, symbol and source-label concordance.

The formulas are copied from the independently checked notation text. Label
resolution is mechanical and is reported separately from proof verification.
"""
from pathlib import Path
import csv,json,re,collections

ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'deliverables';SRC=ROOT/'sources'
rows=list(csv.DictReader((OUT/'S6_09_PAPERS_inventory.csv').open()))
papers={p:(OUT/f'S6_09_PAPERS_{p}.tex').read_text() for p in ['I','II','III'] if (OUT/f'S6_09_PAPERS_{p}.tex').exists()}
labels={p:set(re.findall(r'\\label\{([^}]+)\}',s)) for p,s in papers.items()}
numbers={}
for paper in papers:
    aux=OUT/f'S6_09_PAPERS_{paper}.aux'
    if aux.exists():
        for lab,num in re.findall(r'\\newlabel\{([^}]+)\}\{\{([^{}]*)\}',aux.read_text()):
            if not lab.endswith('@cref'):numbers[(paper,lab)]=num
def loc(lab,paper=None):
    found=[p for p in papers if lab in labels[p] and (not paper or p==paper)]
    if not found:return 'Placement pending: `'+lab+'`'
    return '; '.join('Paper '+p+', '+(numbers.get((p,lab)) or 'label `'+lab+'`') for p in found)
def prose_tex(s):
    s=re.sub(r'\\(?:sub)*section\{([^{}]*)\}',lambda m:'## '+m[1]+'\n',s)
    s=re.sub(r'\\paragraph\{([^{}]*)\}',lambda m:'### '+m[1]+'\n',s)
    s=re.sub(r'\\(?:Cref|cref|ref|eqref)\{([^}]+)\}',lambda m:'; '.join(loc(x) for x in m[1].split(',')),s)
    s=re.sub(r'\\label\{[^}]+\}','',s)
    s=s.replace('\\[','$$').replace('\\]','$$').replace('\\(','$').replace('\\)','$')
    s=s.replace('\\noindent','').replace('\\smallskip','').replace('\\medskip','')
    return s
text='''# S6_09_PAPERS — common notation and complete result concordance

The binding convention is the FAMILY convention reproduced and proved in Paper I. A positive base meridian and an analytic root-deck generator are different objects: the former is counterclockwise, the latter is clockwise. The endpoint identification of the lifted positive loop gives the displayed homology monodromy. A bare change of integral basis does not reverse a meridian.

## Core dictionary

| Symbol or source notation | Common meaning and normalization |
|---|---|
| B, t; p1, p2, p0 | Projective base with marked values 0, 1, infinity, respectively. |
| S1, S2, W | Reduced multiple fibres and reduced cusp; the full scheme fibres are 3S1, 4S2 and W. |
| Lambda | Integral fibre homology with ordered basis (gamma-hat, u-hat, w-hat, delta-hat). |
| (gamma,u,w,delta) | Dual cohomology basis; its w is a covector, not the family parameter. |
| Pi_c | Two by four period matrix with rows (6mu,tau,1,0) and (beta_part+c,mu,0,1). |
| beta_part | Particular period normalized by (beta_part+tau)(p0)=0. |
| w | Family parameter exp(−pi i c), with 0<abs(w)<216. |
| u_Engel | Engel's parameter for the transported inverse reference lift at c=0; u_Engel=w². |
| v | Multiplicative second fibre coordinate exp(2pi i zeta2). |
| q | Modular nome exp(2pi i tau) when used in a theta formula; a cusp monomial in the stated toric chart otherwise. Every such local use is defined in the proof. |
| P_mark | FAMILY-to-Engel integral marking matrix; columns are the FAMILY basis in Engel's common basis. |
| Q in the invariant source | Reversed-meridian marking P_mark S, with S displayed below. |
| D_c; Delta in the invariant fibre formulas | The real determinant Im(beta_c)−6(Im(mu))²/Im(tau). It is not the elliptic discriminant. |
| Delta in arithmetic | Weierstrass or modular discriminant with the displayed scaling; no identification with D_c. |
| eta_F | Integral fibre two-class u wedge w + 6 gamma wedge delta. It is distinct from Dedekind eta and Weierstrass quasi-periods. |
| g_gamma, mathfrak g | Primitive global class with exp(12 g_gamma)=f*O(−p); exp is z↦exp(2pi i z). |
| G0 | The unrescaled global representative with class 12 mathfrak g. |
| R on the root curve | R1 R2^(−1), with R1=R^4, R2=R^3 and rho*O_B(1)=R^12. |
| O_mathcalB(n) versus O_B(n) | Root power R^n versus ordinary coarse degree n; their degrees and characters are different. |
| k_chi | Cayley local coordinate in the critical-point calculations; z=k_chi². |
| N(P), L | The normalized theta norm and its logarithm; no missing Gaussian, discriminant or height factor is suppressed. |
| m_P | Positive Betti measure db wedge da; the opposite order has the wrong sign. |
| h-hat | Canonical height with the explicit factor-of-two convention in the arithmetic section. |

The detailed formulas below fix every nontrivial sign, row order, special-point scaling, root-line degree and arithmetic normalization used by the invariant and period arguments. Repeated generic local letters are bound by their displayed local definitions, not identified across different charts.

'''
text+=prose_tex((OUT/'work/invariants_arithmetic/notation_dictionary.tex').read_text())
text+='''
## Source namespaces and historical question labels

FAM, PUSH, INV, CDP, MAPS and ARI denote the six run identifiers. A source question called “Lead n” is identified within its own run's prompt; it never denotes an additional theorem. Its complete mathematical assertion is restated at the correction or calculation that treats it. R-items and K-items inherited from prompts are replaced in the papers by the actual definitions or numbered results that supply them. The source-to-print transforms and exact aliases are retained with the editorial code.

| Source family | Printed label namespace |
|---|---|
| FAMILY | fam:src: for numbered results, fam: for retained original labels |
| PUSH | push:src: for numbered results, retained push: local labels |
| INVARIANTS | inv: |
| ARITHMETIC Part C | ari: |
| CDP | cdp:, with explicitly shared Paper I statements mapped below |
| MAPS in Paper I | mapsI: |
| Working edition | wb:, or the explicit inv:/mapsI: aliases below |

## Every result row

Each row below is an exact inventory identifier. Multiple source results can have the same printed statement while retaining distinct proofs. A shared label is therefore an explicit consolidation, not an omitted result.

| Source run | Source result | Paper | Printed label | Printed number |
|---|---|---|---|---|
'''
for r in rows:
    lab=r['printed_label'];paper=r['paper']
    text+='| '+r['source_run']+' | `'+r['source_id']+'` | '+paper+' | `'+lab+'` | '+(numbers.get((paper,lab)) or ('Not yet typeset' if lab else 'Placement pending'))+' |\n'
text+='\n## Exact consolidation and equation aliases\n\n'
for rel in ['work/invariants_arithmetic/statement_aliases.json',
            'work/invariants_arithmetic/working_statement_aliases.json',
            'work/invariants_arithmetic/working_equation_tag_aliases.json',
            'work/maps_audit/paperI_topology_aliases.json']:
    p=OUT/rel
    if not p.exists():continue
    obj=json.loads(p.read_text())
    if isinstance(obj,list):pairs=[(x['source_label'],x['shared_printed_label']) for x in obj]
    else:pairs=[(k,v.get('label',str(v)) if isinstance(v,dict) else v) for k,v in obj.items()]
    text+='### '+p.stem+'\n\n| Original label or tag | Printed label | Place |\n|---|---|---|\n'
    for old,new in pairs:text+='| `'+old+'` | `'+new+'` | '+loc(new)+' |\n'
text+='\n## Every label in the assembled papers\n\nThe list includes proof, equation and section labels as well as result labels. The numeric column is read from the actual LuaLaTeX auxiliary file, not inferred from source order.\n\n| Paper | Label | Printed number |\n|---|---|---|\n'
for paper,ls in labels.items():
    for lab in sorted(ls):text+='| '+paper+' | `'+lab+'` | '+(numbers.get((paper,lab)) or 'Unnumbered or awaiting final auxiliary pass')+' |\n'
(OUT/'S6_09_PAPERS_notation_sheet.md').write_text(text)
(OUT/'records/notation_concordance.json').write_text(json.dumps({'inventory_rows':len(rows),'paper_labels':{p:len(v) for p,v in labels.items()},'unplaced_results':[(r['source_run'],r['source_id']) for r in rows if not r['printed_label']]},indent=2)+'\n')
print('Notation sheet:',len(text),'characters;',len(rows),'result rows')
