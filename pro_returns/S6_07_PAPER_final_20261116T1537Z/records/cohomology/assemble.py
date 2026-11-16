from pathlib import Path
import re, json

BASE=Path('/workspace/scratch/33c5206c0778')
OUT=BASE/'deliverables/records/cohomology'
RET=BASE/'inputs/sources/returns'
FILES={
 'A':RET/'S6_01_INVARIANTS/fragments/part_A.tex',
 'B':RET/'S6_01_INVARIANTS/fragments/part_B.tex',
 'C':RET/'S6_01_INVARIANTS/fragments/part_C.tex',
 'D':RET/'S6_01_INVARIANTS/fragments/part_D.tex',
 'F':RET/'S6_02_FAMILY/sections/AB.tex',
 'P':RET/'S6_02_PUSH/sections/E_push.tex',
 'CDP':RET/'S6_03_CDP/sections/part_C5.tex',
}
TEXT={k:p.read_text() for k,p in FILES.items()}
records=[]
chunks=[]

def extract_custom(k, sid, env='claim'):
    s=TEXT[k]
    m=re.search(r'\\begin\{'+env+r'\}\{'+re.escape(sid)+r'\}\{([^}]+)\}\{([^\n]*)\}\n',s)
    if not m: raise ValueError((k,sid))
    end=s.index('\\end{'+env+'}',m.end())
    raw=s[m.start():end+len('\\end{'+env+'}')]
    body=s[m.end():end].strip()
    p=s.index(r'\begin{proof}',end)
    q=s.index(r'\end{proof}',p)
    proof=s[p+len(r'\begin{proof}'):q].strip()
    return dict(k=k,id=sid,title=m[2],body=body,proof=proof,raw=raw,source_status=m[1])

def extract_standard(k,sid,env='theorem'):
    s=TEXT[k]
    m=re.search(r'\\begin\{'+env+r'\}\['+re.escape(sid)+r'[^\n]*\](?:\\label\{[^}]+\})?\n',s)
    if not m: raise ValueError((k,sid))
    end=s.index(r'\end{'+env+'}',m.end())
    raw=s[m.start():end+len(r'\end{'+env+'}')]
    p=s.index(r'\begin{proof}',end);q=s.index(r'\end{proof}',p)
    return dict(k=k,id=sid,title=sid,body=s[m.end():end].strip(),proof=s[p+len(r'\begin{proof}'):q].strip(),raw=raw,source_status='Proved')

INV={sid:extract_custom(sid[0],sid) for sid in ['A1.0','A1.1','A1.2','A1.3','A2.1','A2.2','A2.4','A3.1','A4.1','A4.2','B1.1','B1.2','B2.1','B2.2','B3.1','B3.2','B3.3','C1.1','C2.1','C3.3','C3.5','C3.7','D1.3']}
FAM=extract_standard('F','A.5.2')
PUSH=extract_standard('P','E.2.1')
CDP=extract_custom('CDP','C5b','statement')

def labels(s,pre):
    shared={'sec:cotangent-images','sec:hodge'}
    s=re.sub(r'\\label\{([^}]+)\}',lambda m:r'\label{'+pre+':'+m[1]+'}',s)
    s=re.sub(r'\\(eqref|ref)\{([^}]+)\}',lambda m:'\\'+m[1]+'{'+(m[2] if m[2] in shared else pre+':'+m[2])+'}',s)
    return s

def notation(s,run,determinant=False):
    protected={}
    def protect(m):
        token='ZZREFPROTECT'+str(len(protected))+'ZZ'
        protected[token]=m[0]
        return token
    s=re.sub(r'\\(?:label|eqref|ref)\{[^}]+\}',protect,s)
    # Citation keys are centralized by the editor.
    for a,b in {'AC2026':'AC26','Engel2026':'E26','DGKX26v1':'DGKXv1','ViaclovskyLog2026':'VL26','Stelzig2021':'Stelzig21','McHugh2017':'McHugh18','Angella2017':'Angella17'}.items():
        s=s.replace('{'+a+'}','{'+b+'}')
    s=s.replace(r'\citet',r'\cite').replace(r'\citep',r'\cite')
    macros={'Pone':r'\mathbb P^1','PP':r'\mathbb P','Pp':r'\mathbb P','OO':r'\mathcal O','C':r'\mathbb C','Z':r'\mathbb Z','Q':r'\mathbb Q','R':r'\mathbb R'}
    # Pairs of backslashes are row breaks, not the start of a macro: in
    # particular the source row break followed by a coefficient C is untouched.
    s=re.sub(r'(?<!\\)((?:\\\\)*)\\(Pone|PP|Pp|OO|C|Z|Q|R)(?![A-Za-z])',lambda m:m[1]+macros[m[2]],s)
    # Do not touch local module generators or parameter u. These substitutions
    # are only the displayed lattice-covector combinations used in the sources.
    for a,b in [
      ('\\gamma,u','\\gamma,u_{\\Lambda}'),
      ('\\gamma, u','\\gamma, u_{\\Lambda}'),
      ('\\tau u+w','\\tau u_{\\Lambda}+w_{\\Lambda}'),
      ('\\tau u + w','\\tau u_{\\Lambda} + w_{\\Lambda}'),
      ('\\mu u+\\delta','\\mu u_{\\Lambda}+\\delta'),
      ('\\mu u + \\delta','\\mu u_{\\Lambda} + \\delta'),
      ('u\\wedge w','u_{\\Lambda}\\wedge w_{\\Lambda}'),
      ('u\\wedge\\sigma','u_{\\Lambda}\\wedge\\sigma'),
      ('\\gamma\\wedge u\\wedge w','\\gamma\\wedge u_{\\Lambda}\\wedge w_{\\Lambda}'),
      ('\\gamma\\wedge u','\\gamma\\wedge u_{\\Lambda}'),
      ('\\langle\\gamma,u,w,\\delta','\\langle\\gamma,u_{\\Lambda},w_{\\Lambda},\\delta'),
      ('\\sigma_1\\otimes u','\\sigma_1\\otimes u_{\\Lambda}'),
      ('the $w,\\delta$','the $w_{\\Lambda},\\delta$'),
      ('\\psi_1=2u+w+3\\delta','\\psi_1=2u_{\\Lambda}+w_{\\Lambda}+3\\delta'),
      ('\\psi_2=u+w+2\\delta','\\psi_2=u_{\\Lambda}+w_{\\Lambda}+2\\delta'),
    ]: s=s.replace(a,b)
    # Avoid reapplying gamma wedge u to an already subscripted covector.
    s=s.replace('u_{\\Lambda}_{\\Lambda}','u_{\\Lambda}')
    if run=='inv':
        s=re.sub(r'\\mathcal E(?![A-Za-z])',lambda m:r'\mathcal E_{\rm cot}',s)
        s=re.sub(r'(?<![A-Za-z\\])G(?![A-Za-z_])',r'G_B',s)
        s=s.replace(r'\mathcal B',r'\mathfrak B')
        s=s.replace('E_X',r'\mathcal E_{\rm cot,X}').replace('E_Y',r'\mathcal E_{\rm cot,Y}')
        s=re.sub(r'(?<!\\mathcal )(?<![A-Za-z\\_])E(?![A-Za-z0-9_])',lambda m:r'\mathcal E_{\rm cot}',s)
        s=s.replace('Hodge diamond of Part A',r'Hodge diamond of Section~\ref{sec:hodge}')
        s=s.replace('Part A',r'Section~\ref{sec:cotangent-images}').replace("Part C's argument",r'The argument of inv:C1.1')
    if run in ('fam','push','cdp'):
        s=s.replace(r'\rho:',r'\varpi:').replace(r'\rho\bar',r'\varpi\bar').replace(r'\rho^',r'\varpi^').replace(r'\rho_*',r'\varpi_*')
        s=re.sub(r'\\mathcal E(?![A-Za-z])',lambda m:r'\mathcal E_{\rm tan}',s)
        s=re.sub(r'(?<![A-Za-z\\])G(?![A-Za-z_])',lambda m:r'G_{\mathfrak B}',s)
        if run=='cdp':
            s=re.sub(r'(?<!\\mathcal )(?<![A-Za-z\\_])E(?![A-Za-z0-9_])',lambda m:r'\mathcal E_{\rm tan}',s)
        else:
            s=re.sub(r'(?<!\\mathcal )(?<![A-Za-z\\.])E(?![A-Za-z0-9.])',lambda m:r'{P_6}' if m.start()>0 and s[m.start()-1]=='_' else r'P_6',s)
    # Every original ID remains in the text, prefixed by its run.
    if run=='inv':
        s=re.sub(r'(?<![:A-Za-z])([ABCD][1-4]\.[0-9]+)(?![0-9])',r'inv:\1',s)
    elif run=='fam':
        s=re.sub(r'(?<![:A-Za-z])([AB]\.[1-5]\.[0-9]+)(?![0-9])',r'fam:\1',s)
    if determinant:
        s=re.sub(r'(?<![A-Za-z\\])N(?![A-Za-z_])',lambda m:r'N_{\rm det}',s)
    for token,value in protected.items():s=s.replace(token,value)
    return labels(s,run)

def numbered_proof(s):
    # Number existing source paragraphs. Mathematical displays stay attached to
    # their prose paragraph; no inference is inserted by this layout operation.
    if len(s.split())<150:return s
    parts=s.split('\n\n'); out=[]; n=0
    for idx,part in enumerate(parts):
        t=part.lstrip()
        is_prose=idx==0 or bool(re.match(r'(?:[A-Z]|(?:inv|fam|push|cdp):|\\emph\{)',t))
        if is_prose:
            n+=1
            part=r'\par\smallskip\noindent\textbf{Step '+str(n)+r'.}\ '+part
        out.append(part)
    if n==0:out[0]=r'\noindent\textbf{Step 1.}\ '+out[0]
    return '\n\n'.join(out)

def source_file(src):
    return str(FILES[src['k']].relative_to(BASE/'inputs/sources'))

def add(src,run,status,uses,env='theorem',title=None,body=None,proof=None,mechanism=None,suffix='',changes=None,kind=None,proof_location=None,extra=None):
    sid=src['id']; pid=f'{run}:{sid}{suffix}'
    b=notation(src['body'] if body is None else body,run,run=='inv' and sid in ('A1.1','A1.2'))
    title=src['title'] if title is None else title
    opening='\\begin{'+env+'}['+pid+'; '+status+'; '+title+']\\label{'+pid+'}\n'
    rendered=opening+b+'\n\\end{'+env+'}'
    chunks.append(rendered+'\n\\uses{'+uses+'}\n')
    if proof is not False and status=='T':
        p=src['proof'] if proof is None else proof
        p=notation(p,run,run=='inv' and sid in ('A1.1','A1.2'))
        chunks.append('\\begin{proof}\n'+numbered_proof(p)+'\n\\end{proof}\n')
    if status=='A':
        assert mechanism
        chunks.append(mechanism+'\n\\par\\noindent\\emph{proof in the repository} (\\texttt{'+run.upper()+'}, '+sid+').\n')
    rec={
      'paper_label':pid,'statement_as_printed':rendered,'status':status,
      'source_run':{'inv':'S6_01_INVARIANTS','fam':'S6_02_FAMILY','push':'S6_02_PUSH','cdp':'S6_03_CDP'}[run],
      'source_id':sid,'source_file':source_file(src),'wording_vs_source':{'classification':'changed' if changes or suffix or status!=src['source_status'] else 'same content','details':(changes or [])+['Run-prefixed statement ID and T/K/A heading; common macro and bibliography-key normalization; source lattice covectors use u_Λ,w_Λ; coarse root map uses varpi; cotangent and tangent bundles receive distinct subscripts.']},
      'found_in_AC26':None,'found_in_E26':None,'found_in_DGKX_v1':None,'credited_to':[],
      'checks':[],'kind':kind or ('Announcement' if status=='A' else 'Known result re-derived' if status=='K' else 'Theorem'),
      'uses':uses,'summary':title,'proof_location':proof_location or ('repository: '+source_file(src) if status=='A' else 'main text' if status=='T' else 'Appendix B, tangent cohomology subsection'),
      'source_statement':src['raw'],'source_status':src['source_status'],
    }
    if extra:rec.update(extra)
    records.append(rec)
    return rec

def text_source(k,sid,title,body):
    return dict(k=k,id=sid,title=title,body=body,proof='',raw=body,source_status='text')

def tex(s):chunks.append(s+'\n')

tex(r'''\section{Cotangent cohomology and its consequences}\label{sec:cohomology}
\subsection{Direct images and the decisive period derivative}\label{sec:cotangent-images}
The calculations concern every admissible member of the fixed marked
$(3,4)$ period family.  The structure-sheaf direct images and the previously
known Hodge constraints are credited to \cite[Proposition 9.13 and Theorem 9.1]{AC26};
the root-curve version also occurs in \cite[Proposition 6.10]{DGKXv1}.
The source proof of the structure-sheaf calculation is retained below as a
new proof, in accordance with the prescribed T status of this subsection.
''')
setup=TEXT['A'][TEXT['A'].index('We use the marked'):TEXT['A'].index(r'\begin{claim}')].strip()
add(text_source('A','notation-cotangent','Cotangent notation',setup),'inv','text',r'The family and marking fixed in Section~\ref{sec:family}.',env='definition',proof=False,kind='Definition',proof_location='definition',changes=['The unnumbered source setup is displayed as a definition for explicit notation and traceability.'])

a10proof=INV['A1.0']['proof']
assert a10proof.count(r'\Delta(\tau)^{-1}')==1
a10proof=a10proof.replace(r'\Delta(\tau)^{-1}',r'\Delta_{\rm mod}(\tau)^{-1}')
add(INV['A1.0'],'inv','T',r'The cyclic and cusp charts; analytic base change \cite[III.4.10, III.4.12]{BS76}; analytic duality \cite[pp.~261, 264--266]{RRV71} and \cite[p.~91, Proposition~2]{RR70}.',proof=a10proof,kind='New proof',changes=['Content already known in AC26 Proposition 9.13 and DGKXv1 Proposition 6.10 is explicitly credited; the binding map retains this source re-derivation as T in the main text.'])
add(INV['A1.1'],'inv','T',r'The local cyclic and normal-crossing charts; inv:A1.0.',env='lemma')
add(INV['A1.2'],'inv','T',r'inv:A1.0, inv:A1.1; analytic duality \cite[pp.~261, 264--266]{RRV71}.',env='proposition')

branch=TEXT['A'][TEXT['A'].index('At the order-four point') if 'At the order-four point' in TEXT['A'][TEXT['A'].index(r'\subsection{A.2'):TEXT['A'].index(r'\begin{claim}{A2.1}')] else TEXT['A'].index(r'\subsection{A.2'):TEXT['A'].index(r'\begin{claim}{A2.1}')]
branch=TEXT['A'][TEXT['A'].index('\n',TEXT['A'].index(r'\subsection{A.2'))+1:TEXT['A'].index(r'\begin{claim}{A2.1}')].strip()
branch=branch.replace('Statement A2.3','fam:B.1.3')
add(text_source('A','notation-period-branch','The order-four branch',branch),'inv','text',r'The period functions and the first-run clockwise convention.',env='definition',proof=False,kind='Definition',proof_location='definition',changes=['The source branch convention is displayed as a definition.'])
ap21=INV['A2.1']['proof'].replace('The symbolic residuals\nof all three identities are zero in \\texttt{a\\_calculations.py}.','The producing run reports zero symbolic residuals for all three identities in \\texttt{a\\_calculations.py}.')
add(INV['A2.1'],'inv','T',r'inv:A1.0; the period transformations \cite[Definition 3.1 and Theorem 3.4(i)]{AC26}; the modular identities stated in the proof.',proof=ap21,changes=['Placed before inv:A1.3 so the decisive period calculation is available at the direct-image step. The symbolic-check sentence is attributed to its producing run.'])
ap=INV['A2.2']['proof'].replace('A2.3','fam:B.1.3')
ap=ap.replace('Here are the numerical methods actually run.','The producing run reports the following numerical methods and outputs.')
ap=ap.replace('The code, all output, and precision are supplied.','The source reports that the code, output, and precision accompanied that run.')
add(INV['A2.2'],'inv','T',r'inv:A2.1; the already identified elliptic section fam:B.1.3; the displayed Ramanujan identities.',proof=ap,changes=['The duplicate section-identification reference inv:A2.3 is replaced by the same earlier identification fam:B.1.3; numerical checks in the source are producing-run reports, not new verification.'])
add(INV['A2.4'],'inv','T',r'inv:A1.2, inv:A2.1, inv:A2.2; for the explicitly counterfactual final clause, the residue calculation in inv:A1.3.',changes=['Placed before inv:A1.3 to expose the rank input; the source counterfactual clause still depends on the later residue calculation, explicitly listed in Uses.'])
a13=INV['A1.3']['proof'].replace('proved below','proved above').replace('below','above')
add(INV['A1.3'],'inv','T',r'inv:A1.0--inv:A1.2, inv:A2.1, inv:A2.2, inv:A2.4; the normalized residue sequence; analytic relative duality \cite{RRV71}.',proof=a13,changes=['Moved after inv:A2.1, inv:A2.2 and inv:A2.4; source directional words “below” change to “above”.'])

tex(r'\subsection{The Hodge table}\label{sec:hodge}')
tex(r'The values of $h^{0,q}$, the vanishing of $h^{p,0}$ for $p>0$, and $h^{1,1}=h^{1,2}+1$ were already obtained in \cite[Theorem 9.1 and Remark 1.3]{AC26}. The evaluated middle value completes that table.')
add(INV['A3.1'],'inv','T',r'inv:A1.0, inv:A1.3; coherent Leray on $\mathbb P^1$ and Serre duality.',changes=['The known boundary Hodge numbers and middle relation are expressly credited to AC26; the complete table is unchanged.'])

tex(r'\subsection{The Fr\"olicher sequence}\label{sec:frolicher}')
tex(r'''The earlier conditional study of a complex structure on $S^6$ supplies
general Hodge and spectral-sequence constraints in
\cite[Proposition 3.1, Theorem 3.2 and Corollary 3.3]{Ugarte00}.
McHugh gives Bott--Chern and Aeppli formulas in terms of Dolbeault and
Fr\"olicher data \cite[Section 7.1, pp.~24--25]{McHugh18}; Angella records
the spectral-sequence and double-complex descriptions and the resulting
Bott--Chern relations \cite[Figures 1--2 and Section 4]{Angella17}.
The geometric input here is the evaluated Hodge table of inv:A3.1;
the proof of inv:C2.1 uses the structure theorem of \cite{Stelzig21}.''')
tex(r'Nondegeneration at $E_1$ and injectivity of the map from $H^{0,1}$ were already established in \cite[Corollary 9.22]{AC26}. The following source calculation determines all the first-differential ranks and degeneration at $E_2$.')
csetup=TEXT['C'][TEXT['C'].index('In this section'):TEXT['C'].index(r'\begin{claim}{C1.1}')].strip()
csetup=csetup.replace('by Part A','by inv:A3.1').replace('for this part','for this calculation')
add(text_source('C','notation-hodge-input','The formal Hodge parameter',csetup),'inv','text',r'inv:A1.0, inv:A1.3, inv:A3.1; sphere topology.',env='definition',proof=False,kind='Definition',proof_location='definition',changes=['The unnumbered source hypothesis table is displayed as a definition; the formal parameter h is retained with its full source scope.'])
add(INV['C1.1'],'inv','T',r'The Hodge table in inv:notation-hodge-input; convergence of the Fr\"olicher spectral sequence to de Rham cohomology.',changes=['AC26 Corollary 9.22 already gives E1 nondegeneration and injectivity of the first map; all ranks and E2 degeneration retain the source general-h formulation.'])

tex(r'\subsection{Bott--Chern and Aeppli cohomology}\label{sec:bc-aeppli}')
c21=INV['C2.1']['proof'].replace('The program \\texttt{code/c\\_double\\_complex.py} performs','The producing run reports that \\texttt{code/c\\_double\\_complex.py} performs')
add(INV['C2.1'],'inv','T',r'inv:C1.1; the bounded-double-complex decomposition \cite[Theorem 3 and Proposition 6(1)]{Stelzig21}.',proof=c21,changes=['The source code paragraph is explicitly attributed to the producing run; it is not a fresh program check. Definitions, formal-h tables, and numerical specialization are retained.'])
add(INV['C3.3'],'inv','A',r'inv:C1.1, inv:C2.1; repository inv:C1.2 and inv:C3.1; the graded Leibniz rule.',env='announcement',body=INV['C3.3']['body'].replace('N\\subset','N_{BC}\\subset').replace('\\oplus N','\\oplus N_{BC}').replace('N^2','N_{BC}^2').replace('disputed value','evaluated value'),mechanism=r'The repository argument represents the positive Bott--Chern classes by the arrow targets in the double-complex decomposition. It combines the curvature identity of repository inv:C3.1, the graded Leibniz rule, the first-differential ranks and integration in top degree to make the products vanish.',changes=['The binding map changes the producing run’s Proved status to A; no proof is printed. The square-zero ideal is named N_BC, distinct from the determinant line; “disputed” changes to “evaluated”. The source dependence on unread inv:C3.1 is explicit in Uses and the mechanism paragraph.'])

tex(r'\subsection{Higher multiplicities and finite covers}\label{sec:multiplicities-covers}')
tex(r'For the original multiplicities, the canonical bundle is credited to \cite[Proposition 9.11]{AC26}; the fundamental group and rational homology of the admissible finite-fundamental-group members are credited to \cite[Theorems 7.17 and 7.22]{AC26}. The statements below retain the source hypotheses for higher multiplicities and for the finite universal covers.')
add(INV['B1.1'],'inv','T',r'The fixed period and cusp charts; inv:A1.0--inv:A1.2; smooth proper base change \cite[III.4.12]{BS76}.',env='lemma',changes=['Included as the source comparison lemma needed for the binding canonical and cover statements.'])
b21body=INV['B2.1']['body'].split('Moreover')[0].strip()
b21proof=INV['B2.1']['proof'].replace('B1.2 computes the cohomology, with no use of that\ntopological conclusion.\n','')
add(INV['B2.1'],'inv','T',r'inv:B1.1; \cite[Theorem 1.1 and Proposition 2.3]{VL26}; relative duality \cite{RRV71}.',body=b21body,proof=b21proof,suffix='-canonical',changes=['The source statement is partitioned at “Moreover”: only its canonical-bundle clause is T; the Hodge clauses are printed separately as A with the identical hypotheses. The source sentence referring to the Hodge computation is transferred to the announcement mechanism.'])
add(INV['B1.2'],'inv','A',r'inv:B1.1; the repository residue calculation and relative duality.',env='announcement',mechanism=r'The repository compares the invariant extensions of the logarithmic cohomology bundles under the enlarged cyclic roots. The absolute residue maps then remove the same two finite skyscraper terms, and relative duality supplies the second cotangent row.',changes=['The binding map changes the producing run’s Proved status to A; its complete direct-image statement, one-component-cusp hypothesis, and consequence are retained without proof. The source reference to the Hodge diamond in Part A points to the printed Hodge-table subsection sec:hodge.'])
b21h=INV['B2.1']['body'][:INV['B2.1']['body'].index('Then')]+INV['B2.1']['body'][INV['B2.1']['body'].index('Moreover'):]
b21h=b21h.replace('Moreover','Then',1)
add(INV['B2.1'],'inv','A',r'inv:B1.2; \cite[Theorem 1.1 and Proposition 2.3]{VL26}.',env='announcement',body=b21h,suffix='-hodge',title='Hodge numbers for all coprime multiplicities',mechanism=r'The announced direct-image comparison gives the structure-sheaf and cotangent cohomology by Leray on the base. These are the Hodge clauses of the same source statement as the preceding canonical formula.',changes=['The source statement is partitioned at “Moreover” to implement the binding T/A distinction. The same admissibility, coprimality and nonzero construction-parameter hypotheses are repeated verbatim.'])

# Move an existing source paragraph earlier to remove B3.1 -> B3.3 proof dependence.
b33=INV['B3.3']['proof']
cstart=b33.index('We justify the comparison with $N$')
cend=b33.index('The constant-sheaf normalization',cstart)
contraction=b33[cstart:cend].strip().replace('We justify the comparison with $N$ without assuming a collapse\ntheorem from AC26.','Let $N$ be the small cusp tube. The following normal-crossing contraction is the one supplied in inv:B3.3.')
b31=INV['B3.1']['proof']
old='The explicit normal-crossing contraction\nof the tube onto $W$ given in B3.3 identifies their fundamental groups,\nso the same generator is in the image of $\\pi_1(W)$.'
new='The following source normal-crossing calculation contracts the tube onto $W$.\n\n'+contraction+'\n\nIt identifies their fundamental groups, so the same generator is in the image of $\\pi_1(W)$.'
assert old in b31
b31=b31.replace(old,new)
add(INV['B3.1'],'inv','T',r'The admissible affine and cusp fillings; inv:B1.1; the elementary covering and normalization calculations in the proof; \cite[III.4.12]{BS76}.',env='lemma',proof=b31,changes=['Included as the source support for inv:B3.2 and inv:B3.3. The existing normal-crossing contraction paragraph of inv:B3.3 is transferred verbatim here to make this use antecedent; its original occurrence is replaced by a cross-reference.'],extra={'proof_sources':[source_file(INV['B3.1'])+' B3.1',source_file(INV['B3.3'])+' B3.3, normal-crossing contraction paragraph']})
add(INV['B3.2'],'inv','T',r'inv:B3.1; inv:B1.2 (A, source dependency retained); inv:A1.3; derived relative duality \cite{RRV71}.',changes=['The antecedent hypotheses are inv:B3.1. The supplied proof invokes inv:B1.2, which the binding map makes an announcement; that dependency is retained and expressly recorded rather than silently repaired.'])
b33=b33[:cstart]+'The contraction of the cusp tube used here was established in the proof of B3.1 by the source normal-crossing vector-field calculation.\n\n'+b33[cend:]
# The original proof invokes B2.2. Print its already supplied valuation and
# monomial argument here at the only pair used by B3.3; no extra theorem is added.
val=INV['B2.2']['proof']
val=val[:val.index('Finally, $d=0$')].strip()
val=val.replace('B2.1 then gives','The canonical formula then gives').replace('using B2.1','using the canonical formula')
val=val.replace('This proves the displayed dimension formula using the canonical formula and\n$h^0(\\Pone,\\OO(e))=\\max\\{e+1,0\\}$.','The cohomology used in this valuation calculation is $h^0(\\Pone,\\OO(e))=\\max\\{e+1,0\\}$.')
val=re.sub(r'(?<![A-Za-z\\])([xy])(?![A-Za-z])',lambda m:'y' if m[1]=='x' else 'x',val)
val=val.replace(r'\mathcal L',r'\mathcal L_{\rm root}')
ring_context=r'For the invoked source argument, take $m_1=3$, $m_2=4$, $k=l=1$, $d=6$, and integers $r,s$ with $4r+3s=1$, and put $\mathcal L_{\rm root}=\mathcal O(rS_1+sS_2)$. In the following valuation calculation, $f$ denotes either $f:X\to B$ or $g:Y\to B$, and the $S_j$ denote its reduced finite fibres. The weighted root coordinates are $x$ of weight $3$ and $y$ of weight $4$.'
ring_context+='\n\n'+val+'\n\n'
needle='the ring statement with all multiplication maps.\n\n'
assert needle in b33
b33=b33.replace(needle,needle+ring_context,1)
b33=b33.replace('The integer matrices and all exterior-power\nidentities were checked exactly in','The producing run reports that the integer matrices and all exterior-power identities were checked exactly in')
add(INV['B3.3'],'inv','T',r'inv:B3.1, inv:B3.2; the source valuation and monomial argument of inv:B2.2, printed below for $(k,l)=(1,1)$; the marked lattice and affine data.',proof=b33,changes=['The source normal-crossing contraction paragraph has been moved to the proof of inv:B3.1; its later occurrence is a cross-reference. The source-invoked valuation and monomial argument of inv:B2.2 is printed inside this proof at (k,l)=(1,1), where it is used. The final d=0 exclusion for general pairs is outside this specialized proof and is not imported. Producing-run program claims are labelled as such.'],extra={'proof_sources':[source_file(INV['B3.3'])+' B3.3',source_file(INV['B2.2'])+' B2.2 proof, specialized to (k,l)=(1,1)']})

tex(r'\subsection{Metric consequences}\label{sec:metric-announcements}')
add(INV['C3.5'],'inv','A',r'The fibration and sphere topology; Stokes’ theorem.',env='announcement',mechanism=r'The source uses the nonzero semipositive exact form $f^*\omega_{FS}$ and the positive four-form supplied by a balanced or strongly Gauduchon metric. The remaining exclusions use $b_1=b_2=0$ and the same integral obstruction.',changes=['The binding map changes the producing run’s Proved status to A; no proof is printed.'])
add(INV['C3.7'],'inv','A',r'inv:A3.1; the global Dolbeault lift in repository inv:A3.2; inv:C2.1.',env='announcement',mechanism=r'The repository restricts the prospective metric class to a regular torus fibre. Its real Aeppli image lies in $\mathbb R\eta$, while the complex-oriented square of $\eta$ is $-12$; translation averaging would give a positive class with positive square.',changes=['The binding map changes the producing run’s Proved status to A; both the geometric hypothesis and the source’s more general sufficient condition are retained.'])

tex(r'''\subsection*{Correction concerning relative differentials}\label{sec:relative-correction}
The locators are \cite[Remark 1.3, printed p.~5; Remark 9.21, printed p.~81]{AC26}.
\emph{Paraphrase of the printed assertions:} the former attributes torsion
along the singular fibres to the relative differential sheaves without
separating their degrees; the latter includes the reduced cusp $W$ in the
torsion support of $\Omega^1_{X/B}$. This is a paraphrase, not a quotation:
the requirement not to reproduce the prose of \cite{AC26} prevents the
separately requested literal printed sentence from being supplied.
The correction is local and does not alter the preceding credits.
''')
add(INV['A4.1'],'inv','T',r'The presentations of ordinary relative Kähler differentials for $t=xy$, $t=xyz$, and $t=s^m$.',env='lemma',changes=['Included as the source local-module proof supporting the required neutral correction.'])
a42=INV['A4.2']['body']
a42p=INV['A4.2']['proof'].replace('Both disputed sentences were checked on rendered pages of the\noriginal PDF, so this is not a transcription correction.','The producing run reports that both disputed sentences were checked on rendered pages of the original PDF. The present source check uses the supplied transcription at the exact locators above.')
add(INV['A4.2'],'inv','T',r'inv:A4.1; \cite[Remarks 1.3 and 9.21]{AC26}.',env='remark',proof=a42p,kind='Correction',changes=['The producing-run “Refuted” heading becomes the binding T correction. AC26 is identified by exact locators and a labelled paraphrase; its prose is not reproduced. The literal-quotation requirement remains explicitly unsatisfied.'])

tex(r'''\section{Tangent cohomology and local deformations}\label{sec:tangent}
\subsection{The standard family: the known Kuranishi line}\label{sec:tangent-known}
The following statement is credited to \cite[Theorem 1.3 and Theorem 6.12]{DGKXv1}.
The first source theorem gives the Kuranishi and miniversality conclusions;
the tangent-cohomology theorem gives the displayed dimensions.
The supplied re-derivation is in Appendix~\ref{app:tangent-rederivation}.
''')
add(FAM,'fam','K',r'The compact family fam:A.5.1 and its nonzero Kodaira--Spencer class fam:A.4.2; \cite[Theorems 1.3 and 6.12]{DGKXv1}.',env='cited',title='Tangent cohomology and the Kuranishi line',proof=False,changes=['Corrected from the producing run’s Proved heading to K under REVIEW_S6_02_FAMILY §5; credited to DGKXv1 Theorem 1.3 and its tangent-cohomology theorem. The re-derivation is placed in Appendix B.'],extra={'credited_to':['DGKXv1 Theorem 1.3','DGKXv1 Theorem 6.12, source label p2:thm:tangent-cohomology']})

tex(r'\subsection{Every integral Picard twist}\label{sec:tangent-twists}')
cdpsetup=TEXT['CDP'][TEXT['CDP'].index('In this subsection'):TEXT['CDP'].index(r'\begin{statement}{C5b}')].strip()
add(text_source('CDP','notation-integral-twists','The integral Picard normalization',cdpsetup),'cdp','text',r'The standard clockwise affine data and exponential sequence; the root factorization.',env='definition',proof=False,kind='Definition',proof_location='definition',changes=['The source subsection setup is displayed as a definition. The source coarse map rho becomes varpi, preserving rho for the elliptic fixed value.'])
cdpbody=CDP['body'].replace('r_1(n)','r_3(n)').replace('r_2(n)','r_4(n)')
cdpproof=CDP['proof'].replace('We first check the precise input from R2--R3.','We give the root-chart and cusp calculations used in this proof.')
cdpproof=cdpproof.replace('needed from the earlier returns','used here')
start=cdpproof.index('Statement C5a gives the quotient')
end=cdpproof.index('We have\n',start)
ds=INV['D1.3']['proof'];p=ds.index('To verify the quotient');q=ds.index('We obtain the complete root direct images',p)
detail=ds[p:q]
detail=detail.replace('(D.10)','the normal-coefficient sequence').replace('(D.9)','the displayed logarithmic direct images').replace('$P$','$\\mathrm dP_6$').replace('K_P','K_{\\mathrm dP_6}').replace('\\Omega_P^1','\\Omega_{\\mathrm dP_6}^1').replace('\\OO_P','\\OO_{\\mathrm dP_6}')
normal=r'''The branch-normal sequence is
\[
0\longrightarrow\mathcal T\longrightarrow T_X
\longrightarrow\nu_*K_{\mathrm dP_6}\longrightarrow0.
\]
'''+detail+r'''
Every $\nu^*M_n$ is trivial because $H^2(X,\mathbb Z)=0$ and
$\operatorname{Pic}^0(\mathrm dP_6)=0$. Thus the same quotient
calculation applies after each integral twist. The elementary extension
of $\mathcal O(-6)$ by $\mathbb C_{p_0}$ is $\mathcal O(6)$,
since $\mathcal O(p_0)=\mathcal O(12)$ on the root curve.
'''
cdpproof=cdpproof[:start]+normal+cdpproof[end:]
add(CDP,'cdp','T',r'The root and normalization calculations below; inv:D1.3 for the source-expanded branch-normal and conormal computation; analytic base change \cite[III.4.10, III.4.12]{BS76} and relative duality \cite{RRV71}.',title='Integral twists and the normalization-map exception',body=cdpbody,proof=cdpproof,changes=['Residues r1,r2 are renamed r3,r4 to agree with the first-run root notation. The source C5a/Part A cross-reference is expanded by the already supplied proof paragraphs of INV D1.3, with no new mathematical claim. Every integral twist and the normalization-map exception are retained.'],extra={'proof_sources':[source_file(CDP)+' C5b',source_file(INV['D1.3'])+' D1.3, normal-coefficient and fibre-conormal paragraphs'],'secondary_sources':['returns/S6_01_INVARIANTS/fragments/part_D.tex D4.1']})

tex(r'''\subsection{Coprime higher multiplicities}\label{sec:tangent-higher}
The tangent vector occurs in two producing runs, \texttt{PUSH} E.2.1
and \texttt{CDP} E11: \emph{two runs, no second reader}.
The statement below retains the full hypotheses and conclusions of
\texttt{PUSH} E.2.1; the comparison with \texttt{CDP} is limited to
their common higher-multiplicity tangent-cohomology conclusion.
''')
pushbody=PUSH['body'].replace('admissible logarithmic data of E.1','admissible logarithmic data of push:E.1 (in particular, $\\gcd(3k,4l)=1$)')
push_citation_before='The base-change and relative-duality argument E.3.1 applies on\nthese charts.'
push_citation_after=r'The base-change and relative-duality argument applies on these charts, using \cite[III.4.12]{BS76} and \cite[pp.~264--266]{RRV71}.'
assert push_citation_before in PUSH['proof']
pushproof=PUSH['proof'].replace(push_citation_before,push_citation_after)
pushproof=pushproof.replace('The program \\texttt{e\\_push\\_exact.py} independently checks','The producing run reports that \\texttt{e\\_push\\_exact.py} independently checks')
add(PUSH,'push','T',r'The admissible higher-multiplicity data push:E.1; the displayed root-chart and residue computations; \cite[III.4.12]{BS76} and \cite{RRV71}. Two runs, no second reader.',title='Tangent cohomology and local miniversality for coprime multiplicities',body=pushbody,proof=pushproof,changes=['The implicit coprimality in source E.1 is explicitly repeated; the phrase “two runs, no second reader” is displayed. The reported finite exact computation remains a producing-run report.','The proof sentence referring to E.3.1 is replaced by a grammatical sentence with opened analytic references BS76 III.4.12 and RRV71 pp. 264–266. The exact before/after sentence is recorded in proof_wording_changes; mathematical content is unchanged.'],extra={'secondary_sources':['returns/S6_03_CDP/sections/part_E.tex E11'],'secondary_source_role':'CDP E11 is a cross-run comparison of the common tangent-cohomology conclusion only; the printed statement and proof are PUSH E.2.1, not a merged theorem.','proof_wording_changes':[{'source_before':push_citation_before,'printed_after':push_citation_after,'reason':'Replace the unavailable internal citation by the opened standard sources and remove the grammar artifact found on master page 56.','mathematics_changed':False}],'checks':[{'type':'source_status','scope':'Common higher-multiplicity tangent-cohomology conclusion; comparison source returns/S6_03_CDP/sections/part_E.tex E11','verdict':'two runs, no second reader','source':'status/RESPONSE_INTAKE.md'}]})

tex(r'\subsection{The algebraic-dimension corollary}\label{sec:algebraic-dimension-nearby}')
cor=text_source('F','A.5.2-corollary','Algebraic dimension near the standard family',r'Every sufficiently small deformation of $X_c$ has algebraic dimension $1$.')
cor['raw']='Consequence: every small deformation of X_c has algebraic\n  dimension 1 and carries the pencil |-2K|.'
cor['proof']=r'By fam:A.5.2, every sufficiently small deformation is induced by the compact period family. Each member has algebraic dimension one by \cite[Theorem 9.1(i)]{AC26}. This proves the stated local corollary.'
rec=add(cor,'fam','T',r'fam:A.5.2; \cite[Theorem 9.1(i)]{AC26}.',env='corollary',kind='Corollary',changes=['The binding row 6d is printed only as the algebraic-dimension consequence of A.5.2. Exact source wording is in REVIEW_S6_02_FAMILY F4 and RESPONSE_INTAKE §1.3; the additional pencil clause is omitted, narrowing rather than strengthening the source. No broader stability statement is claimed.'])
rec['source_file']='status/REVIEW_S6_02_FAMILY.md'
rec['source_id']='F4 consequence of A.5.2; binding row 6d'
rec['source_archive']='S6_07_PAPER_context.zip'

(OUT/'sections.tex').write_text('\n'.join(chunks))

# Appendix B contains the source re-derivation, with the review's citation fix.
fp=FAM['proof']
intro_end=fp.index(r'\emph{The base and its line bundles.}')
fp=r'''This is the supplied re-derivation of the known statement
\cite[Theorems 1.3 and 6.12]{DGKXv1}; the body retains its K status.
The analytic base-change and duality applications below are supported by
the opened standard sources \cite[III.4.10, III.4.12]{BS76},
\cite[pp.~261, 264--266]{RRV71}, and \cite[p.~91, Proposition 2]{RR70}.

'''+fp[intro_end:]
old='This is precisely the pointwise base-change and\ntop-degree duality application spelled out in the cited Lemmas 6.8--6.9.'
new='The base-change application is \\cite[III.4.10 and III.4.12]{BS76}; the relative trace is supplied by \\cite[pp.~261, 264--266]{RRV71}, with the Gorenstein dualizing line as in \\cite[p.~91, Proposition 2]{RR70}. These replace the producing run\'s incorrect DGKX lemma citations.'
assert old in fp
fp=fp.replace(old,new)
# Only the identified cusp-coordinate occurrences in FAM A.5.2 are renamed;
# q in R^q and in cohomological degrees is untouched, as are the root discs.
appendix_cusp_renamings=[
    (r'\Delta(\tau)',r'\Delta_{\rm mod}(\tau)',2),
    (r'$q=z_0z_1z_2$',r'$t_c=z_0z_1z_2$',2),
    (r'\mathbb C\{q\}',r'\mathbb C\{t_c\}',1),
    (r'u(q)q^{B_0\lambda}',r'u(t_c)t_c^{B_0\lambda}',2),
    (r'=q\,u(q)',r'=t_c\,u(t_c)',1),
    (r'q\partial_q',r't_c\partial_{t_c}',1),
    (r'\wedge dq',r'\wedge dt_c',1),
    (r'$dq$',r'$dt_c$',1),
]
for old_notation,new_notation,expected_count in appendix_cusp_renamings:
    assert fp.count(old_notation)==expected_count,(old_notation,fp.count(old_notation))
    fp=fp.replace(old_notation,new_notation)
fp=notation(fp,'fam')
(OUT/'appendix_b_tangent.tex').write_text(r'''\subsection{Tangent cohomology and the Kuranishi line}\label{app:tangent-rederivation}
\uses{fam:A.1.2, fam:A.3.1, fam:A.4.2; the cyclic and cusp charts; \cite[III.4.10, III.4.12]{BS76}; \cite[pp.~261, 264--266]{RRV71}; \cite[p.~91, Proposition 2]{RR70}.}
\begin{proof}[Re-derivation of the known result \ref{fam:A.5.2}]
'''+numbered_proof(fp)+'\n\\end{proof}\n')

(OUT/'records.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'statements':len(records),'sections_chars':len((OUT/'sections.tex').read_text()),'appendix_chars':len((OUT/'appendix_b_tangent.tex').read_text())}))
