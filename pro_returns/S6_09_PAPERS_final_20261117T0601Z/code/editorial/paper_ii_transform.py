"""Explicit, recorded editorial normalization for Paper II.

This module changes labels, theorem wrappers and source-number references.
It never verifies a proof. Mathematical replacements are supplied separately
as fully checked proof blocks with their own provenance.
"""
from pathlib import Path
import re, json

ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/'deliverables'
I_AUX=(OUT/'S6_09_PAPERS_I.aux').read_text()
I_NUM=dict(re.findall(r'\\newlabel\{([^}]+)\}\{\{([^}]+)\}',I_AUX))
I_KIND=dict(re.findall(r'\\newlabel\{([^}]+)@cref\}\{\{\[([^\]]+)\]',I_AUX))

def iref(label,kind='result'):
    if label not in I_NUM:raise KeyError(('Paper I label',label))
    if kind=='result':kind=I_KIND.get(label,'result').capitalize()
    return 'Paper~I, '+kind+'~'+I_NUM[label]

def expand(s,run):
    def one(m):
        p=ROOT/'sources/returns'/run/m[1]
        if not p.suffix:p=p.with_suffix('.tex')
        return expand(p.read_text(),run)
    return re.sub(r'\\input\{([^}]+)\}',one,s)

def protect(s):
    saved=[]
    def one(m):saved.append(m[0]);return '@@TEXPROTECT'+str(len(saved)-1)+'@@'
    s=re.sub(r'\\(?:label|ref|eqref|cref|Cref|autoref|tag\*?|cite\w*|nocite|path|url|texttt)(?:\[[^\]]*\])*\{[^{}]*\}',one,s)
    return s,lambda x:re.sub(r'@@TEXPROTECT(\d+)@@',lambda m:saved[int(m[1])],x)

def namespace(s,ns):
    return re.sub(r'\\(label|ref|eqref|cref|Cref|autoref)\{([^}]+)\}',
      lambda m:'\\'+m[1]+'{'+','.join(ns+':'+x for x in m[2].split(','))+'}',s)

def normalize_equations(s,ns):
    tags=set(re.findall(r'\\tag\{([^{}]+)\}',s))
    # Keep the established source tags during the initial assembly. A single
    # equation-label dictionary makes every ordinary reference clickable and
    # prevents a mathematical tag from being confused with a result number.
    s=re.sub(r'\\tag\{([^{}]+)\}',lambda m:m[0]+'\\label{'+ns+':eq:'+m[1]+'}',s)
    s,restore=protect(s)
    for tag in sorted(tags,key=len,reverse=True):
        s=s.replace('('+tag+')','\\eqref{'+ns+':eq:'+tag+'}')
    return restore(s),tags

def cdp_wrapper(s):
    def opening(m):
        sid,status,title=m[1],m[2],m[3]
        kind='proposition'
        if 'Known' in status:title='Credited re-derivation: '+title
        if 'Refuted' in status:title='Counterexample: '+title
        if 'Open' in status:kind='problem'
        return '\\begin{'+kind+'}['+title+']\\label{cdp:st:'+sid+'}'
    s=re.sub(r'\\begin\{statement\}\{([^{}]+)\}\{([^{}]+)\}\{([^\n]+)\}',opening,s)
    # Every source statement here has exactly one opening/closing pair and no
    # nested source statement; save the destination environment in source order.
    envs=re.findall(r'\\begin\{(proposition|problem)\}\[[^\n]+\]\\label\{cdp:st:[^}]+\}',s)
    it=iter(envs)
    s=re.sub(r'\\end\{statement\}',lambda m:'\\end{'+next(it)+'}',s)
    s=re.sub(r'\\begin\{idstatement\}\{([^{}]+)\}\{([^{}]+)\}',
             lambda m:'\\begin{proposition}['+m[2]+']\\label{cdp:st:'+m[1]+'}',s)
    s=s.replace('\\end{idstatement}','\\end{proposition}')
    s=s.replace(r'\begin{proposition}[Proved]',r'\begin{proposition}')
    seen=set()
    def unique(m):
        if m[1] in seen:return ''
        seen.add(m[1]);return m[0]
    return re.sub(r'\\label\{(cdp:st:[^}]+)\}',unique,s)

def raw_refs(s,ids,ns='cdp:st:'):
    s,restore=protect(s)
    # Within the occurrence section, UNn is the author's unambiguous shorthand.
    if ns=='cdp:st:':
        s=re.sub(r'(?<![\w.])UN\s*(\d+)\b',lambda m:'\\ref{cdp:st:C.2.UN.'+m[1]+'}',s)
    pattern=r'(?<![\w.:])('+'|'.join(re.escape(x) for x in sorted(ids,key=len,reverse=True))+r')(?![\w:]|\.\d)'
    s=re.sub(pattern,lambda m:'\\ref{'+ns+m[1]+'}',s)
    return restore(s)

def replace_external_I(s):
    known={'cdp:st:D.1.14':('fam:src:F.1.1','Theorem'),
           'cdp:st:E9':('fam:src:A.5.2','Theorem')}
    for label,(target,kind) in known.items():
        s=re.sub(r'\\(?:ref|cref|Cref)\{'+re.escape(label)+r'\}',lambda m:iref(target,kind),s)
    # Source-owned references in PUSH and INV whose complete statements and
    # proofs belong in Paper I are resolved from the actual final aux file.
    available=set(re.findall(r'\\label\{([^}]+)\}',s))
    def multiple(m):
        keys=m[2].split(',')
        if len(keys)<2 or not any(k in I_NUM and k not in available for k in keys):return m[0]
        return ' and '.join(iref(k) if k in I_NUM and k not in available else '\\'+m[1]+'{'+k+'}' for k in keys)
    s=re.sub(r'\\(ref|eqref|cref|Cref)\{([^}]+)\}',multiple,s)
    for label in set(re.findall(r'\\(?:ref|eqref|cref|Cref)\{([^},]+)\}',s)):
        if label in I_NUM and label not in available:
            kind='equation' if ':eq:' in label else 'result'
            s=re.sub(r'\\(?:ref|eqref|cref|Cref)\{'+re.escape(label)+r'\}',lambda m:iref(label,kind),s)
    return s

def common_cleanup(s):
    # The opened source is the corrected 2019 arXiv text, not the 2018 edition.
    s=s.replace('LRS2018D','LRS2019')
    s=re.sub(r'^%[^\n]*\n','',s,flags=re.M)
    s=s.replace('\\Verified','').replace('\\AuthorSelfCheck','').replace('\\NeedsCheck','').replace('\\Refuted','')
    s=re.sub(r'\s*No priority is claimed\.', '',s)
    s=re.sub(r';?\s*no priority claim\s+is made for this example\.', '.',s)
    s=s.replace('not a completeness or priority assertion','a record with the stated search scope')
    s=re.sub(r';\s*no priority for the projective quotient classification\s+is claimed\.', '.',s)
    s=re.sub(r'No priority claim is\s+made for the shared elliptic ruled conclusion\.', '',s)
    s=re.sub(r'; it makes\s+no priority claim for the occurrence itself\.', '.',s)
    s=re.sub(r'We claim no priority for the construction or these\s+ambient Hodge numbers\.', '',s)
    s=s.replace('quotient and makes no priority claim.','quotient.')
    s=s.replace('We make no priority claim.','')
    s=re.sub(r';\s*we claim no priority\.', '.',s)
    s=re.sub(r'We give the argument above\s+and claim no priority\.', 'The complete argument is given above.',s)
    s=re.sub(r';\s*no priority is claimed\.', '.',s)
    s=s.replace('but no earlier complete','but no matching complete')
    s=s.replace('the construction in the supplied source','the construction')
    s=s.replace('under the hypotheses in Lead 1','under the hypotheses just stated')
    s=s.replace('the two vanishings in Lead 1',r'the vanishings $H^0(S,N^*\otimes A)=H^0(S,Q\otimes A)=0$')
    s=s.replace('prove Lead 4 with rational Betti-number', 'prove the stated index obstruction with rational Betti-number')
    s=s.replace('the Euler-number identity of Lead 5 is', 'the Euler-number identity is')
    s=s.replace("This is the proof of CDP98, Lemma~1.4 in the attached arXiv source;\nthe prompt's reference to Corollary~1.2 does not match that source's\nnumbering.", 'This is the proof of CDP98, Lemma~1.4 in the opened arXiv source.')
    s=s.replace('The restriction on roots of unity in Lead 2 is unnecessary:', 'The computation applies to roots of unity as well:')
    s=s.replace('the all-twist interpretation of Lead 8:', 'the assertion that the map is nonzero for every twist:')
    s=s.replace('the marked functions $\\tau,\\mu,\\beta_c$ of the prompt', 'the fixed marked functions $\\tau,\\mu,\\beta_c$')
    s=s.replace('the torus-fibred families listed in the prompt,', 'the following torus-fibred families,')
    s=s.replace(r'The extension assertion of \ref{cdp:st:E4}(ii) of the prompt, with an arbitrary'+'\n'+r'fixed curve $C$ in place of $\mathbb P^1$, is false even for a torus', r'The assertion that every small deformation of a fibration extends'+'\n'+r'over its original fixed positive-genus target curve $C$ is false even for a torus')
    s=s.replace('The configuration in the question is not the configuration of\n'+r'\cite{ViaTwo26push}.  The elliptic surface', 'The proposed configuration with three rank-one reduced singular fibres\n'+r'does not describe the construction of \cite{ViaTwo26push}. The elliptic surface')
    fractions={r'{u\over(1-u)^2}':r'\frac{u}{(1-u)^2}',r'{u^2\over(1-u)^3}':r'\frac{u^2}{(1-u)^3}',r'{Y/X-1\over Y/X+1}':r'\frac{Y/X-1}{Y/X+1}',r'{z\over w^{r_i}}':r'\frac{z}{w^{r_i}}',r'{\beta_i^{-r_i}\over\log|\beta_i|}':r'\frac{\beta_i^{-r_i}}{\log|\beta_i|}',r'{dz\wedge dw\over w^{r_i+1}}':r'\frac{dz\wedge dw}{w^{r_i+1}}',r'{\bar a_i\over a_i}':r'\frac{\bar a_i}{a_i}',r'{2\pi i\over a_i}':r'\frac{2\pi i}{a_i}',r'{\bar a_i b_i\over a_i}':r'\frac{\bar a_i b_i}{a_i}',r'{dz\over z}':r'\frac{dz}{z}',r'{dw\over w}':r'\frac{dw}{w}'}
    for old,new in fractions.items():s=s.replace(old,new)
    s=s.replace('The integral index in R7 is\nverified next;', 'The integral index is proved in '+iref('fam:src:F.1.1')+';')
    s=s.replace('We first check the precise input from R2--R3.', 'We check the root-curve and logarithmic tangent inputs of '+iref('fam:src:A.1.1')+' and '+iref('fam:src:A.5.2')+'.')
    s=s.replace('as in R5', 'as in '+iref('fam:src:B.2.1'))
    s=s.replace('maximum in R3 is attained', 'maximum in '+iref('fam:src:C.2.3')+' is attained')
    s=s.replace('the precise threshold of R3.', 'the precise threshold of '+iref('fam:src:C.2.3')+'.')
    s=s.replace(r'The graph method is that of \cite{LRS2019}, in the theorem labelled'+'\n'+r'\texttt{theorem main2 new} in the supplied Lehn--Rollenske--Schinko'+'\n'+r'source;', r'The graph method is that of \citet[Theorem~3.1, p.~9]{LRS2019};')
    s=s.replace('Their discriminant orders and the resolved fibre\ntypes are precisely the corresponding entries of\n'+r'\cite[Theorem~6.2 and Table~I]{Kodaira1963II}.', r'''The primitive monodromy matrices and their characters distinguish the
unstarred and starred types; see \citet[Section~2.3, pp.~5--6]{UlmerUrzua2021}
and \citet[Theorem~6.2 and Section~8(iv)]{Kodaira1963II}.
For the displayed minimal equations the discriminant orders are computed
directly as $12r/d$, and the corresponding Kodaira configurations have
the same Euler numbers.''')
    s=s.replace(r'\cite[Theorem~6.2, pp.~564--566, and Table~I, p.~604]{Kodaira1963II}', r'\cite[Theorem~6.2, pp.~564--566; Section~8(iv)(11), p.~585]{Kodaira1963II}, together with the explicit positive-loop matrices in \citet[Section~2.3, pp.~5--6]{UlmerUrzua2021},')
    s=s.replace(r'\cite[Theorem~6.2 and Table~I]{Kodaira1963II}', r'\cite[Theorem~6.2; Section~8(iv)(11), p.~585]{Kodaira1963II} and \citet[Section~2.3, pp.~5--6]{UlmerUrzua2021}')
    # Literal source typographical errors, separately documented by the audit.
    s=s.replace('\\text{if } n=0,','\\text{if } n=0,')
    s=s.replace("P'_epsilon",r"P'_{\epsilon}").replace('f_epsilon',r'f_{\epsilon}')
    s=s.replace('\text{is represented by}',r'\text{is represented by}')
    s=re.sub(r'(\\begin\{(equation\*?|align\*?|gather\*?|multline\*?)\})(.*?)(\\end\{\2\})',
      lambda m:m[1]+re.sub(r'\n\s*\n','\n',m[3])+m[4],s,flags=re.S)
    s=re.sub(r'\\\[(.*?)\\\]',lambda m:r'\['+re.sub(r'\n\s*\n','\n',m[1])+r'\]',s,flags=re.S)
    return s
