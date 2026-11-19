"""Consolidate the received mathematical outlines for Papers III and V.

Every numbered outline step retains or receives an explicit expansion target.
The construction is source-based; the global scope review remains separately
recorded and is not inferred from this text transformation.
"""
from pathlib import Path
import re,json
from tex_tools import macros,argument
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'frontmatter';OUT.mkdir(exist_ok=True)

def blocks(paper):
    text=(ROOT/f'parts/{paper}.source_front.linked.tex').read_text()
    matches=list(macros(text,'RungZero',1));out=[]
    for index,(a,b,args) in enumerate(matches):
        end=matches[index+1][0] if index+1<len(matches) else len(text)
        tail=text[b:end]
        begin=tail.index('\\begin{enumerate}')
        start=begin+len('\\begin{enumerate}')
        if tail[start:start+1]=='[':_,start=argument(tail,start,'[',']')
        finish=tail.index('\\end{enumerate}',start)
        content=tail[start:finish]
        items=[x.strip() for x in re.split(r'\\item\b',content)[1:]]
        out.append({'result':args[0],'steps':items})
    return out

def refs(text):
    result=[]
    for m in re.finditer(r'\\(?:[cC]?ref|SeriesRef)\{([^}]+)\}',text):
        result.extend(x.strip() for x in m.group(1).split(','))
    return list(dict.fromkeys(result))

def write(paper,main,scope):
    text='\\subsection{The main theorems}\n\\label{series:'+paper+':main-theorems}\n\n'+scope+'\n\n'
    index={'paper':paper,'main_theorems':[],'rung_grouping':{}}
    for n,row in enumerate(main):
        letter=chr(65+n);label=f'series:{paper}:{letter}'
        target_labels=list(dict.fromkeys(row['body_labels']))
        text+=f'\\hypertarget{{main-{paper}-{letter}}}{{}}\n\\paragraph{{Theorem {letter} ({row["title"]}).}}\n\\label{{{label}}}\n'
        text+=row['statement']+'\n\n\\textit{Mechanism.} '+row['mechanism']+'\n'
        text+='\\textit{Relation to literature.} '+row['literature']+'\n'
        text+=f'\\hyperlink{{outline-{paper}-{letter}}}{{Proof in outline}}; full statements: '+', '.join('\\SeriesRef{'+lab+'}' for lab in target_labels)+'.\n\n'
        entry={'letter':letter,'title':row['title'],'label':label,'main_anchor':f'main-{paper}-{letter}',
            'outline_anchor':f'outline-{paper}-{letter}','body_labels':target_labels,'steps':[]}
        for k,(claim,targets) in enumerate(row['steps'],1):
            entry['steps'].append({'number':k,'anchor':f'step-{paper}-{letter}-{k}','body_targets':targets,'claim_tex':claim})
        assert 3<=len(entry['steps'])<=7,(paper,letter,len(entry['steps']))
        index['main_theorems'].append(entry)
        for old in row.get('old_blocks',[]):index['rung_grouping'][old]=letter
    text+='\\subsection{The proofs in outline}\n'
    for entry in index['main_theorems']:
        letter=entry['letter'];text+=f'\\hypertarget{{outline-{paper}-{letter}}}{{}}\n\\subsubsection*{{Theorem {letter}: {entry["title"]}}}\n\\begin{{enumerate}}[label=\\arabic*.,leftmargin=*]\n'
        for step in entry['steps']:
            text+='\\item\\hypertarget{'+step['anchor']+'}{} '+step['claim_tex']+'\n'
            text+='\\textit{Expansion:} '+', '.join('\\SeriesRef{'+lab+'}' for lab in step['body_targets'])+'.\n'
        text+='\\end{enumerate}\n\n'
    (OUT/f'frontmatter_{paper}.tex').write_text(text)
    (OUT/f'frontmatter_{paper}_map.json').write_text(json.dumps(index,indent=2,ensure_ascii=False))

def main():
    iii=blocks('III');v=blocks('V')
    assert len(iii)==10 and len(v)==5
    def seq(block,targets):
        assert len(block['steps'])==len(targets),(len(block['steps']),targets)
        return list(zip(block['steps'],targets))
    main3=[]
    main3.append({'title':'The prescribed quotient and relative extensions','statement':iii[0]['result'],
        'mechanism':'The target solid torus fixes the relative extension, and an interior-ball pinch realizes every unrestricted exterior-agreement class.',
        'literature':r'The relative pinch and $\pi_6(S^3)=\Z/12$ are known inputs; the explicit receiving form and its counterexample are proved in \cref{maps:src:A.2.2}.',
        'body_labels':['maps:src:A.2.2'],'steps':seq(iii[0],[['mapsI:src:A.1.1'],['mapsI:src:A.2.1'],['maps:src:A.2.2'],['maps:src:A.2.2']]),'old_blocks':['III.1']})
    main3.append({'title':'The quotient and algebraic-reduction homotopy classes','statement':iii[1]['result']+'\n\n'+iii[2]['result'],
        'mechanism':'The actual normal-frame comparison identifies the Lie-framed regular fibre, and the exact degree-twelve factorization kills its unstable class.',
        'literature':r'The real Adams invariant and suspension inputs are known: \cite[Theorem~4.14, p.~423]{mapsAPS2} and \cite[Theorem~4.1, Corollaries~4.2--4.3]{mapsToda52}. The full statements identify their applications to the retained maps.',
        'body_labels':['maps:src:B.1.1','maps:src:B.1.2','maps:src:B.2.1'],
        'steps':seq(iii[1],[['maps:src:B.1.1'],['maps:src:B.1.1'],['maps:src:B.1.2'],['maps:src:B.1.2']])+seq(iii[2],[['maps:src:B.2.1'],['maps:src:B.2.1'],['maps:src:B.2.1']]),'old_blocks':['III.2','III.3']})
    csteps=seq(iii[3],[['maps:src:B.3.1'],['maps:src:B.3.1'],['maps:src:B.3.1'],['maps:src:B.3.2','maps:src:B.3.3']])
    csteps += [(' '.join(iii[4]['steps'][:2]),['maps:src:B.5.1']),(' '.join(iii[4]['steps'][2:4]),['maps:src:B.5.1']),(iii[4]['steps'][4],['maps:src:B.5.2'])]
    main3.append({'title':'The retained-angle cusp map and finite cell model','statement':iii[3]['result']+'\n\n'+iii[4]['result'],
        'mechanism':'Explicit chart-frame homotopies preserve the Lie framing, and the same marked collar maps give integral cell attachments.',
        'literature':r'The framed-torus invariant is a known topological input, cited at its exact locator in \cref{maps:src:B.3.1}. The product-collar input is \cite[Theorem~6.1, p.~77]{mapsWaldhausen68}; the marked constructions are the receiving applications.',
        'body_labels':['maps:src:B.3.1','maps:src:B.5.1','maps:src:B.5.2'],'steps':csteps,'old_blocks':['III.4','III.5']})
    main3.append({'title':'The relative Kummer cover and its global completion','statement':iii[5]['result'],
        'mechanism':'Adjacent unimodular fan cones force scalar primitive ray indices, while the retained finite monodromy carries the prescribed lattice outside that scalar system.',
        'literature':r'The covering-space and normal-monomial inputs are credited at the exact locators in \cref{maps:src:C.1.1,maps:src:C.1.3,maps:src:C.1.5}; the statement retains the prescribed entire cusp component and its actual lattice maps.',
        'body_labels':['maps:src:C.1.1','maps:src:C.1.2','maps:src:C.1.3','maps:src:C.1.4','maps:src:C.1.5'],
        'steps':seq(iii[5],[[f'maps:src:C.1.{k}'] for k in [1,2,3,4,5]]),'old_blocks':['III.6']})
    main3.append({'title':'The cyclic universal covers','statement':iii[6]['result'],
        'mechanism':'The cyclic cusp matrix and its finite-coefficient cubic evaluations specify the complete published smooth invariant of the constructed cover.',
        'literature':r'The starting quotient family is credited to \cite[Theorems~7.17 and 7.22, pp.~57 and 60]{AC26}. The body cites Zhubr\textquotesingle s classification at its exact locator and computes the full receiving invariant, including its torsion data.',
        'body_labels':['maps:src:D.1.1','maps:src:D.1.4','maps:src:D.1.6','maps:src:D.1.9','maps:src:D.1.11'],
        'steps':seq(iii[6],[['maps:src:D.1.1'],['maps:src:D.1.4'],['maps:src:D.1.6'],['maps:src:D.1.9'],['maps:src:D.1.11'],['maps:src:D.1.4']]),'old_blocks':['III.7']})
    main3.append({'title':'The marked elliptic profiles and their integral outputs','statement':iii[7]['result'],
        'mechanism':'The primitive specialization and normal-circle-torus maps determine the integral cokernels before the full characteristic evaluations identify their smooth outputs.',
        'literature':r'The broader section-line construction and its realization question are credited to \cite[Remark~8.5]{E26}. The exact input table and the refined OS49 groups occur in the full statements below; the published classification theorems are cited there in the precise forms used.',
        'body_labels':['maps:src:D.2.28','maps:src:D.2.44','maps:src:D.2.45','maps:src:D.2.46','maps:src:D.2.47','maps:src:D.2.48','night:P3F.34'],
        'steps':seq(iii[7],[['maps:src:D.2.28'],['maps:src:D.2.28'],['maps:src:D.2.28'],['maps:src:D.2.44','maps:src:D.2.45'],['maps:src:D.2.47'],['maps:src:D.2.48'],['night:P3F.33','night:P3F.34']]),'old_blocks':['III.8']})
    main3.append({'title':'The conifold transition','statement':iii[8]['result'],
        'mechanism':'The actual annular gluing gives the node equation and the primitive boundary maps of its surgery, determining the smooth side with its complex orientation.',
        'literature':r'The smooth classification and $\Theta_6=0$ are known inputs, cited in \cref{maps:src:D.3.2}; the full statements give the holomorphic construction and its marked surgery maps.',
        'body_labels':['maps:src:D.3.1','maps:src:D.3.2','maps:src:D.3.3'],
        'steps':seq(iii[8],[['maps:src:D.3.1'],['maps:src:D.3.1'],['maps:src:D.3.2'],['maps:src:D.3.2'],['maps:src:D.3.3','maps:src:D.3.4']]),'old_blocks':['III.9']})
    scope3=r'''We fix the marked $(3,4,\infty)$ family of Paper~I, its positive
normal-circle orientation, ordered integral lattice, finite affine twists,
and prescribed cusp fan. The first four theorems use the standard
sphere twist data $|p|=1$. The map $e:X\to S^3$ is the repaired quotient
with its target and collar data in \SeriesRef{mapsI:src:A.2.1};
$f:X\to\PP^1$ is its holomorphic algebraic reduction. Every further
elliptic profile carries the source section, vanishing linearization,
lattice and affine cap data specified in its statement. The explicit
transport dictionary is \ref{sec:III:conventions}.'''
    write('III',main3,scope3)
    titles=['The resolved transverse elliptic fibre product','The integral rank-six construction','The genus-two period construction','The oriented diffeomorphism type','The exact family and its two ends','The integral input classification']
    sourceblocks=[iii[9]]+v
    targets=[['maps:src:E.1.2','maps:src:E.2.1'],['maps:src:F.2.5','maps:src:F.2.6','night:P1.13'],['night:P1.4','night:P1.5','maps:src:F.3.5','maps:src:F.3.6'],['maps:src:F.3.7','maps:src:F.4.1'],['night:P1.18','night:P1A.1','night:P1A.2','night:P1A.3','night:P1A.4','night:P1A.5'],['maps:src:F.2.39','maps:src:F.3.11']]
    step_targets=[[['maps:src:E.1.2'],['maps:src:E.1.2'],['maps:src:E.2.1'],['maps:src:E.2.1'],['maps:src:E.2.1']],
                  [['maps:src:F.2.5','night:P1.1'],['maps:src:F.2.5','night:P1.10'],['maps:src:F.2.6','night:P1.11'],['mapsaudit:order-four-torsion-transgression'],['maps:src:F.2.6','night:P1.12'],['night:P1.13']],
                  [['night:P1.4'],['night:P1.2'],['night:P1.5','maps:src:F.3.5'],['maps:src:F.3.5','night:P1.7'],['maps:src:F.3.6','night:P1.8']],
                  [['maps:src:F.3.7','night:P1.9'],['night:P1.13'],['maps:src:F.4.1'],['maps:src:F.4.1'],['maps:src:F.4.1'],['maps:src:F.4.1']]]
    mechanisms=[r'The explicit period comparison and a small crepant Kuhn resolution preserve the root canonical calculation and the integral characteristic pairings.',
                r'The actual order-four boundary map kills the remaining torsion with coefficient one, and the integral Leray filtration gives the middle lattice.',
                r'The wedge image of the genus-two Hodge line has rank three, and its split lift becomes transverse after the normalized imaginary shift.',
                r'The middle-lattice isometry transports both Euler and Pontryagin clutching data, after which the cited absorption theorem removes the homotopy sphere.',
                r'The normalized Frobenius period minimum fixes the exact domain, and the marked period and cap maps determine the family invariants and isomorphisms.',
                r'Finite-order module restrictions and integral cusp transvections reduce the marked inputs to the stated finite list and its explicit analytic realizations.']
    literature=[r'The threefold input is credited to \cite[Theorems~7.17 and 7.22, pp.~57 and 60]{AC26}; the body computes the resolved fibre product and its invariants under the displayed period morphism.',
                r'The integral specialization method uses the original construction in \cite[\S7.7]{AC26}; the receiving rank-six chain maps and their torsion coefficients are displayed in full.',
                r'The exterior-square and good-reduction inputs are cited at their exact locators in the full statements; the specified pencil, integral projection and split lift are retained as explicit constructions.',
                r'Wall\textquotesingle s extended-form classification and Kramer--Stolz\textquotesingle s Theorem~A are known results cited at their exact locators in \cref{maps:src:F.4.1}. The receiving theorem supplies the integrable fourfold and its actual normal data.',
                r'The analytic and source-specific inputs, the exact normalization, and their source comparisons are recorded with \cref{night:P1.18,night:P1A.1,night:P1A.2,night:P1A.3,night:P1A.4,night:P1A.5}.',
                r'The integral and Oka inputs are credited at their exact locators in \cref{maps:src:F.2.39,maps:src:F.3.11}; the statement applies them to every retained marked input.']
    main5=[]
    for n,block in enumerate(sourceblocks):
        if n<4:steps=seq(block,step_targets[n])
        else:
            steps=[]
            for claim in block['steps']:
                labs=refs(claim)
                steps.append((claim,labs or targets[n]))
        statement=block['result']
        if n==4:
            statement=r'''Put
\[
 c_*=-h_{b,\min}=\frac{96}{625\pi}\operatorname{Re}(XH_\infty)_{03},
 \qquad \mathcal U=\{\xi\in\C:\Im\xi>c_*\},
\]
where $X$ is the normalized integral intertwiner of
\cref{night:P1.15} and $H_\infty$ is its regular infinity-root
fundamental-solution limit, normalized at $\lambda=1$ as in
\cref{night:P1.18}. Thus
$c_*=1.0945402503114027801162682630549457037\ldots$.
The point-normalized parameter is transported by the full complex
translation $\xi_b=\xi_{\rm original}-a_{\rm split}$ of that statement.
'''+statement+r'''
On the effective root curve put
$L=\OO((4/5)[\infty]-(3/4)[0])$. Then
\[
 R^qh_*\OO=\bigwedge^q(\OO\oplus L^{-1}\oplus L^{-2}),
 \qquad K_M=h^*L^{-6}.
\]
With $p$ indexing rows and $q$ indexing columns, the Hodge table is
\[
\begin{array}{c|ccccc}
h^{p,q}&0&1&2&3&4\\\hline
0&1&1&0&0&0\\
1&0&2&1&0&0\\
2&0&1&6&1&0\\
3&0&0&1&2&0\\
4&0&0&0&1&1
\end{array}
\]
The tangent tuple is $h^q(T_M)=(1,1,1,2,0)$ and its Kuranishi germ
is smooth of dimension one. A full parameter disc across the
transversality boundary has the proper-filling obstruction of
\cref{night:P1A.5}. A proper smooth family on a punctured disc
whose fibres belong to $\mathcal U$ has the smooth filling after
the explicit degree-two torsor cover of \cref{night:P1A.6}.
'''
            targets[n]=targets[n]+['night:P1.17','night:P1A.6']
        main5.append({'title':titles[n],'statement':statement,'mechanism':mechanisms[n],
            'literature':literature[n],'body_labels':targets[n],'steps':steps,
            'old_blocks':['III.10' if n==0 else f'V.{n}']})
    scope5=r'''The resolved fibre product uses the fixed standard
$(3,4,\infty)$ threefold data and the transverse elliptic factor in
\cref{maps:src:E.1.2}. The rank-six construction uses the displayed
integral monodromies of orders five and four, the primitive maximal
cusp and its marked Kuhn fan in \cref{maps:src:F.2.5}. We retain the
complex orientation and column homology vectors. The family parameter
$\xi$ uses the algebraic splitting $\sigma_b$ of
\cref{night:P1.18}; a change of splitting is transported by the full
complex constant stated there. The shifted products in the first part
also include the complex fivefolds explicitly constructed in
\cref{maps:src:E.2.6,maps:src:E.2.14}.'''
    write('V',main5,scope5)
    print(json.dumps({'III_theorems':len(main3),'V_theorems':len(main5),'III_steps':sum(len(r['steps']) for r in main3),'V_steps':sum(len(r['steps']) for r in main5)}))

if __name__=='__main__':main()
