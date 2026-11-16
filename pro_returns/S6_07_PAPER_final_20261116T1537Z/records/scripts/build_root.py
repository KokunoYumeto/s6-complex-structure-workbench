from pathlib import Path
import re, json, hashlib

ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/'deliverables/records/root'
FAM=ROOT/'inputs/sources/returns/S6_02_FAMILY/sections/AB.tex'
PUSH=ROOT/'inputs/sources/returns/S6_02_PUSH/sections/E_push.tex'
WB=ROOT/'inputs/context/workbench/period_shift_classification.tex'
DG=ROOT/'inputs/context/papers/arXiv_2610.00250v1_Du_Guo_Kusakabe_Xie.tex'
records=[]

def get_block(path, sid):
    s=path.read_text()
    m=re.search(r'\\begin\{(proposition|theorem|lemma|corollary)\}\['+re.escape(sid)+r'(?:;| \().*?\]',s)
    if not m: raise ValueError((path,sid))
    end=s.index('\\end{'+m[1]+'}',m.end())
    body=s[m.end():end]
    body=re.sub(r'^\s*\\label\{[^}]+\}\s*','',body)
    q=s.find('\\begin{proof}',end)
    nextst=s.find('\\begin{proposition}',end+1)
    proof=''
    if q>=0 and (nextst<0 or q<nextst):
        qe=s.index('\\end{proof}',q)+len('\\end{proof}')
        proof=s[q:qe]
    return m[1],body.strip(),proof

def notation(s, sid=None):
    s=s.replace('st:','fam:').replace('DGKX26v1','DGKXv1').replace('DGKX26v2','DGKXv2')
    s=s.replace('P_{\\rm E}','P_{\\rm mark}').replace('P_{\\rm mark}','P_{\\rm mark}')
    s=s.replace('D_{\\rm part}','D_{\\partt}')
    s=re.sub(r'\\dh(?![A-Za-z])',lambda m:r'\dhat',s)
    # Covectors only, not the hatted integral vectors or the parameter w.
    for a,b in [('2u+w+3\\delta','2u_{\\Lambda}+w_{\\Lambda}+3\\delta'),('u+w+2\\delta','u_{\\Lambda}+w_{\\Lambda}+2\\delta')]: s=s.replace(a,b)
    # Each following substitution is limited to its source statement/proof.
    # No label, file name or general parameter is rewritten by these rules.
    def symbol(text, old, new):
        return re.sub(r'(?<![A-Za-z\\])'+re.escape(old)+r'(?![A-Za-z_])',lambda m:new,text)
    if sid in ['A.1.1','A.4.1','B.1.4']:
        s=symbol(s,'q',r'q_\tau')
    if sid=='A.1.1':
        s=re.sub(r'\\Delta(?![A-Za-z_])',lambda m:r'\Delta_{\rm mod}',s)
        s=symbol(s,'h',r'h_6')
        s=symbol(s,'u',r's_{\rm can}')
        s=symbol(s,'v',r't_{\rm can}')
    if sid=='A.3.1':
        s=s.replace(r'$(u,0)$',r'$(h_{\rm loc},0)$')
    if sid=='A.4.2':
        s=s.replace(r'\partial_{w_2}',r'\partial_{\zeta^{\rm new}_2}')
        s=symbol(s,'w',r'\zeta^{\rm new}')
        s=symbol(s,'P',r'P_{\rm KS}')
    if sid in ['B.1.1','B.1.2','B.1.4']:
        s=symbol(s,'W','v')
    if sid=='B.1.1' and 'At the cusp put $v=1/t$' in s:
        a=s.index('At the cusp put $v=1/t$');b=s.index('Its two affine laws have integral defects:',a)
        s=s[:a]+symbol(s[a:b],'v',r'r_{\rm cusp}')+s[b:]
    if sid=='B.1.3':
        s=s.replace('uX',r'v_t X').replace('uY',r'v_t Y')
        s=symbol(s,'u',r'v_t')
        s=symbol(s,'v',r'r_{\rm cusp}')
        s=s.replace(r'\wedge dv/',r'\wedge d r_{\rm cusp}/')
    if sid=='B.2.1':
        s=s.replace('u(t_c)',r'v_{\rm unit}(t_c)').replace('u(0)',r'v_{\rm unit}(0)')
    s=s.replace('Part C',r'Section~\ref{sec:periods}')
    return s

def steps(proof):
    if not proof:return ''
    s=proof.removeprefix('\\begin{proof}').removesuffix('\\end{proof}').strip()
    pars=re.split(r'\n\s*\n',s)
    pieces=[];n=0
    for par in pars:
        if re.match(r'[A-Za-z]',par.strip()):
            n+=1;par='\\par\\smallskip\\noindent\\textbf{Step '+str(n)+'.} '+par
        pieces.append(par)
    return '\\begin{proof}\n'+'\n\n'.join(pieces)+'\n\\end{proof}'

knownac={
'A.1.1':'found: Main Theorem item (4); Theorem 9.1 and §9.4 canonical bundle. The graded canonical ring and all-affine-data scope are not asserted there in this form.',
'A.1.2':'found: §5 finite cyclic quotient construction and bielliptic fibres; searched normalized base change, product covers, degrees 9 and 8 for precise re-derivation.',
'A.2.1':'not found: searched centralizer, period shifts, 2Z; Remark 6.4 leaves parameter equivalence open.',
'A.3.1':'not found: searched parameter family, period shifts, 2Z and coherence; Remark 6.4 leaves parameter equivalence open.',
'A.4.1':'not found: searched Albanese, kappa, j_1, j_2, generic Albanese; §5 gives bielliptic fibres, not these parameter functions.',
'A.4.2':'not found: searched Kodaira, Spencer, deformation, derivative; Remark 6.4 only notes dependence of the fibres.',
'A.5.1':'not found: Remark 6.4 explicitly leaves parameter equivalence open; searched 2Z and classification.',
'B.1.1':'found in part: Remark 3.12 gives the elliptic surface and Abel–Jacobi interpretation of the generator; §3 gives the period matrix. The line-bundle quotient dictionary was not found (searched linearization, P-O, exponentiation).',
'B.1.2':'not found: searched linearization, parameter domain, u, exp(-2pi M); §3 contains the admissibility inequality in the period parameter.',
'B.1.3':'found in substance: Remark 3.12 gives -mu as Abel–Jacobi coordinate of the x=0 Mordell–Weil generator in its scaled Weierstrass model. The explicit zero identity and intersection re-derivation are written in FAM notation.',
'B.1.4':'not found: searched linearization, transported lift, u=w^2, scalar ratio; related elliptic-logarithm reading in Remark 3.12 credited.',
'B.2.1':'found in part: §6.4 and §7 define p=12ell_0-4ell_1-3ell_2 and its topological role; not found complete biholomorphism invariant (searched k_2, c+k_2, parity, isomorphism).',
'B.2.2':'not found: searched two classes, square roots, u, parameter circuit; §6.4 supplies the construction and admissible twists.',
'B.2.3':'not found: searched Engel, punctured u-disc, double cover, descent; correction concerns E26 Remark 8.1.',
'B.3.1':'not found: searched 3k, 4l, 2kl, higher multiplicities; §5 treats multiplicities 3 and 4.'}
knowne={
'A.1.1':'not found: searched canonical, bi-anticanonical, pencil, factorization; E26 §8 gives algebraic dimension 1 and uniqueness of the fibration as discussion.',
'A.1.2':'found in part: Corollaries 3.3 and 3.9 and §6 finite-fibre descriptions; exact normalization/lattice formulation not found.',
'A.2.1':'not found: searched centralizer, period shifts, 2Z, classification.',
'A.3.1':'not found: Remark 8.1 asserts the u-family, corrected by FAM B.2.3; no coherent even-shift maps found.',
'A.4.1':'found in part: Remark 8.1 notes varying elliptic curves in the bielliptic fibres; exact Albanese periods/nomes and generic two-invariant statement not found.',
'A.4.2':'not found: searched Kodaira, Spencer, derivative, Kuranishi; Remark 8.1 discusses variation.',
'A.5.1':'not found: searched classification, 2Z, period shifts; Remark 8.1 discusses variation without exact identifications.',
'B.1.1':'found in part: §2, Lemma 2.1, Definition 2.3 and §2 quotient; E26 fixes M=O(P-O), MW=ZP and inverse translation. The explicit comparison to Pi_c is FAM.',
'B.1.2':'found weaker: Proposition 2.4 gives sufficiently small u for a fixed reference; exact radius not found (searched radius, maximum, D_part).',
'B.1.3':'found in part: §2 and Lemma 2.1 give the generator and height 1/6, citing Oguiso–Shioda and Shioda. Identification with the AC26 logarithm is not stated.',
'B.1.4':'found in part: Corollary 2.2 gives the linearization up to scale and its fibre divisor. No absolute scale is fixed; searched u=w^2 and transported period lift.',
'B.2.1':'found in part: §3 logarithmic translation data and §6–7 topology; complete invariant in (c,k_2,p) not found.',
'B.2.2':'not found: searched two classes, square roots, double cover and parameter circuit; §3 supplies log transforms.',
'B.2.3':'found target: Remark 8.1, first paragraph, asserts a proper holomorphic submersion over the original punctured u-disc for X(u,a_0,a_1).',
'B.3.1':'not found: searched 3k, 4l, 2kl and higher multiplicities; source construction has 3,4.'}
knowndg={
'A.1.1':'found for standard data: Theorem 7.1 (p2:thm:intrinsic-fibration), K^-2 and intrinsic pencil; companion thm:all-maps-factor. Extra all-affine-data scope of FAM is not asserted by Theorem 7.1.',
'A.1.2':'found in part: §7 normalized finite covers and p2:lem:finite-normalization; exact degree-9/8 product-cover presentation not located (searched finite cover, product, bielliptic).',
'A.2.1':'found: §7 simultaneous centralizer, finite norm obstruction and Theorem 1.4 (p2:thm:exact-period).',
'A.3.1':'found: §7 even-shift construction, Appendix C coherent action, p2:cor:bare-period. Proof comparison concerns mechanism, not novelty of theorem.',
'A.4.1':'not found: searched Albanese, kappa, j_1, j_2 and generic cross-check; source has intrinsic pencil and exact-period criterion.',
'A.4.2':'found: Theorem 1.3 (p2:thm:kuranishi-aut) and §6 Kodaira–Spencer generator; FAM gives the displayed representative.',
'A.5.1':'found: Theorem 1.4 (p2:thm:exact-period), Theorem 7.1, p2:cor:bare-period and Theorem 1.3.',
'B.1.1':'not found: searched Engel, Mordell, P-O, linearization and Abel–Jacobi; construction period data are cited from AC26.',
'B.1.2':'found in part: p2:cor:bare-period gives abstract punctured disc, radius exp(-pi M_0) unevaluated; no Engel u-radius found.',
'B.1.3':'not found: searched wp, Mordell, Abel–Jacobi, x=0 section; no identification with the visible elliptic section.',
'B.1.4':'not found: searched Engel, linearization, transported period, lambda_0, u=w^2.',
'B.2.1':'not found for all data: §7 fixes standard twist vectors; searched c+k_2, all admissible, p invariant. Standard-data 2Z classification is Theorem 1.4.',
'B.2.2':'not found as all-data/Engel claim: searched Engel, two classes, square root, u. Standard parity theorem is Theorem 1.4.',
'B.2.3':'not found: searched Engel, Remark 8.1, u-family descent; source does not discuss Engel.',
'B.3.1':'not found: searched 3k, 4l, 2kl and higher multiplicities; §7 fixes standard 3,4 data.'}

def add(sid,status,where,uses,kind='Theorem',credit='S6_07_PAPER; construction credited to AC26 and E26',path=FAM,run='FAM',with_proof=True,env=None):
    et,body,pf=get_block(path,sid)
    printed=notation(body,sid)
    label=f'{run.lower()}:{sid}'
    if run=='FAM': ac,ee,dg=knownac[sid],knowne[sid],knowndg[sid]
    else:
        ac='not found: searched 3k, 4l, Viaclovsky, 2kl; §5 supplies the base 3,4 construction.'
        ee='found input: §3 logarithmic transforms and §5 monodromy marking; exact P_V and higher-data dictionary not found (searched 3k, 4l, 2kl).'
        dg='not found: searched Viaclovsky, 3k, 4l, 2kl; standard twists only in §7.'
    records.append(dict(paper_label=label,statement_as_printed=printed,status=status,source_run=run,source_id=sid,source_file=str(path).split('/inputs/')[-1].removeprefix('sources/').removeprefix('context/'),wording_vs_source='same content; source body retained word for word apart from the recorded notation and reference-key substitutions; status heading follows the binding table',found_in_AC26=ac,found_in_E26=ee,found_in_DGKX_v1=dg,credited_to=credit,checks='Statement body extracted from source, compared token by token after declared notation substitutions; three-source search recorded in records/root/credit_searches.json. Mathematical review only as in supplied status files.',kind=kind,uses=uses,summary=printed.split('\n')[0],proof_location=where,source_statement=body,source_sha256=hashlib.sha256(path.read_bytes()).hexdigest()))
    eenv=env or ('cited' if status=='K' else 'announcement' if status=='A' else et)
    title=f'{run} {sid}; {status}'
    text=f'\\begin{{{eenv}}}[{title}]\\label{{{label}}}\n{printed}\n\\end{{{eenv}}}\n\\uses{{{uses}}}\n'
    if with_proof and pf:text+=steps(notation(pf,sid))+'\n'
    return text,steps(notation(pf,sid))

sec1=r'''\section{The family and its geometric parameter}\label{sec:family}
\subsection{Conventions}
'''
conv=(ROOT/'inputs/sources/returns/S6_02_FAMILY/sections/conventions.tex').read_text()
conv=conv[conv.index('\n')+1:conv.index('\nEach statement below')]
conv=notation(conv).replace('proved in B.1 and B.2','proved below')
sec1+='\\begin{definition}[FAM conventions]\\label{def:conventions}\n'+conv+'\n\\end{definition}\n\\uses{The period construction of \\cite[Sections 2--6]{AC26}; \\cite[Sections 2--5]{E26}.}\n'
records.append(dict(paper_label='def:conventions',statement_as_printed=conv,status='text',source_run='FAM',source_id='conventions',source_file='returns/S6_02_FAMILY/sections/conventions.tex',wording_vs_source='changed: final metatext removed, heading replaced by typed definition; P_mark and all mathematical conventions retained; reference to B.1 and B.2 becomes below',found_in_AC26='found: §§2–6 construction, period laws and orientation conventions; theta/Engel dictionary is from FAM.',found_in_E26='found: §§2–5 construction and positive-root conventions; normalization u=w² is the FAM transported reference.',found_in_DGKX_v1='found in part: §2 fixed standard construction/marking and §7 period parameter; no Engel dictionary.',credited_to='AC26 and E26 for construction; FAM for explicit dictionary',checks='Opened all three supplied sources at recorded locators; notation taken from FAM conventions',kind='Definition',uses='AC26 §§2–6; E26 §§2–5',summary='Base, lattice, periods, clockwise deck generators and transported reference.',proof_location='§1',source_statement=(ROOT/'inputs/sources/returns/S6_02_FAMILY/sections/conventions.tex').read_text()))
initial=FAM.read_text().split('\\subsection{A.1.')[0].split('\n',1)[1]
sec1+=notation(initial)+'\n'
sec1+=r'''The construction, the smooth manifold $S^6$, its algebraic reduction, its canonical bundle and the connected automorphism group are due to \cite[Main Theorem; Sections 3--9]{AC26}. The rational elliptic surface, its line bundle and inverse-translation quotient are those of \cite[Section 2]{E26}. The equality $u=w^2$ uses the transported reference in Definition~\ref{def:conventions}; Engel's parameter has no absolute scale.

\subsection{The intrinsic pencil (known)}
The following result is printed with status K as prescribed. The intrinsic-pencil and base-preservation assertions for the standard data are \cite[Theorem 7.1]{DGKXv1}; the canonical bundle is \cite[Main Theorem (4); Theorem 9.1]{AC26}. The all-affine-data scope and direct-image formulation are retained from FAM A.1.1; the scope of the cited theorem is distinguished in the source table.
'''
x,p=add('A.1.1','K','Appendix B','Definition~\\ref{def:conventions}; \\cite[Theorem 7.1]{DGKXv1}; \\cite[Theorem 9.1]{AC26}.',kind='New proof',credit='AC26 for K_X; DGKXv1 for standard-data intrinsic pencil; FAM for retained extra scope',with_proof=False)
sec1+=x
dgtext=DG.read_text()
m=re.search(r'\\begin\{theorem\}\\label\{thm:all-maps-factor\}(.*?)\\end\{theorem\}',dgtext,re.S)
orig=m[1].strip()
body=orig.replace('a\\in\\cA','c\\in\\mathcal P').replace('X_a','X_c').replace('f_a','f_c').replace('\\Pone','\\mathbb P^1')
sec1+='\\begin{cited}[DGKX Theorem 7.2; K]\\label{dgkx:all-maps-factor}\n'+body+'\n\\end{cited}\n\\uses{\\cite[Theorem 7.2, \\texttt{thm:all-maps-factor}]{DGKXv1}.}\n'
records.append(dict(paper_label='dgkx:all-maps-factor',statement_as_printed=body,status='K',source_run='DGKXv1',source_id='Theorem 7.2; thm:all-maps-factor',source_file='papers/arXiv_2610.00250v1_Du_Guo_Kusakabe_Xie.tex',wording_vs_source='changed: a→c, cA→mathcal P and Pone→mathbb P¹ only; hypotheses and conclusion unchanged',found_in_AC26='not found as this universal map-factorization statement: searched factors, holomorphic map, algebraic reduction; §9 proves a(X)=1.',found_in_E26='not found as universal factorization; Remark 8.1 discusses uniqueness of algebraic reduction.',found_in_DGKX_v1='found: theorem thm:all-maps-factor immediately after Theorem 7.1.',credited_to='Du, Guo, Kusakabe and Xie, arXiv:2610.00250v1',checks='S: supplied v1 statement and proof opened; exact source-to-print variable substitutions recorded.',kind='New proof',uses='H²(S⁶;Z)=0; proper image theorem',summary='Every holomorphic map to P¹ factors uniquely through f.',proof_location='Appendix B (source re-derivation)',source_statement=orig))
sec1+='\n\\subsection{The elliptic surface and its reference lift}\n'
for sid in ['B.1.1','B.1.2','B.1.3','B.1.4']:
    cred='FAM comparison; AC26 Remark 3.12 and E26 §2 geometric inputs; Oguiso–Shioda and Shioda for the Mordell–Weil lattice and height'
    kind='New proof' if sid=='B.1.3' else 'Theorem'
    x,_=add(sid,'T','§1',r'Definition~\ref{def:conventions}; FAM A.3.1 and preceding dictionary identities; \cite[Remark 3.12]{AC26}; \cite[Lemma 2.1; Corollary 2.2; Definition 2.3]{E26}.',kind=kind,credit=cred)
    if sid=='B.1.3': sec1+=r'The geometric identification in this proposition is already implicit in \cite[Remark 3.12]{AC26}. Its intersection calculation re-derives the height computation of \cite[Main Theorem, entry 49; (3.2)]{OS91} and \cite[Theorem 8.6; (8.16)]{Shi90} in the given charts.'+'\n'
    sec1+=x
sec1+=r'''\subsection{Correction to Engel's Remark 8.1}
\noindent\textbf{Printed sentence.} In \cite[Remark 8.1]{E26}: ``We may thus build a proper, holomorphic submersion $\mathcal Y^*\to\Delta^*$ whose fiber over $u$ is $X(u,a_0,a_1)$''. The fault is the global descent for fixed sphere logarithmic data; the local construction is retained. No contact with the source's author is recorded. The finite order-two obstruction below identifies the precise qualification.
'''
x,_=add('B.2.3','T','§1','FAM A.2.1, A.3.1, A.4.1 and B.2.1; \\cite[Remark 8.1]{E26}.',kind='Correction',credit='FAM correction of E26 Remark 8.1')
sec1+=x

sec2=r'''\section{Discrete data and parameter identifications}\label{sec:discrete}
\subsection{The standard data (known)}
The $2\mathbb Z$ equivalence is Theorem 1.4 of Du, Guo, Kusakabe and Xie, arXiv:2610.00250, version 1 \cite[Theorem 1.4]{DGKXv1}. Version 2 does not contain it. The same statement was obtained independently in the workbench from which this paper grew, and Appendix A prints that proof in the present notation.
'''
x,_=add('A.5.1','K','Appendices A and B','FAM A.1.1, A.2.1, A.3.1 and A.4.2; \\cite[Theorems 1.3, 1.4 and 7.1; punctured-disc corollary]{DGKXv1}.',kind='New proof',credit='Du, Guo, Kusakabe and Xie, arXiv:2610.00250v1',with_proof=False)
sec2+=x+'\n\\subsection{All affine vectors and cusp sections}\n'
for sid in ['B.2.1','B.2.2']:
    x,_=add(sid,'T','§2','Definition~\\ref{def:conventions}; FAM A.1.1--A.3.1 and the preceding discrete-data calculation; \\cite[Section 6.4]{AC26}; \\cite[Sections 3 and 5]{E26}.')
    sec2+=x
sec2+='\n\\subsection{Coprime higher multiplicities}\n'
x,_=add('B.3.1','T','§2','FAM A.1.2, A.2.1, B.2.1; \\cite[Proposition 4.7]{VL26}.')
sec2+=r'The theorem concerns the stated model and marking. The identification with the coordinates of \cite[Section 2]{VL26} is separately announced below; this distinction retains the gap noted by the supplied review.'+'\n'+x
for sid in ['E.1.1','E.1.2']:
    x,_=add(sid,'A','Repository: S6_02_PUSH '+sid,'FAM B.3.1; PUSH E.1.1--E.1.2; \\cite[Section 2]{VL26}.',path=PUSH,run='PUSH',with_proof=False,credit='PUSH coordinate dictionary; Viaclovsky for the source models')
    x=x.replace('ViaLog26push','VL26').replace('P_E','P_{\\rm mark}')
    records[-1]['statement_as_printed']=x.split('}\n',1)[1].split('\\end{announcement}')[0].strip() if False else records[-1]['statement_as_printed'].replace('ViaLog26push','VL26').replace('P_E','P_{\\rm mark}')
    records[-1]['wording_vs_source']='changed: status Proved→A required by binding table; notation/reference substitutions only, statement content unchanged; proof omitted as required for announcement'
    sec2+=x+r'\noindent\textit{Mechanism.} The integral change of basis transports the positive-root translations; repeated norm images give the displayed congruences. Proof in the repository, S6\_02\_PUSH, '+sid+r' \cite[run S6\_02\_PUSH, '+sid+r']{Repo}.'+'\n'

appb=r'''\subsection{Intrinsic fibration and even shifts}\label{app:known-periods}
The results cited as K in Sections 1 and 2 are known with the credit given there. The claim made for the text below concerns its re-derivation from the retained period charts.
\subsubsection{Re-derivation of FAM A.1.1}
'''+steps(notation(get_block(FAM,'A.1.1')[2],'A.1.1'))+'\n'
for sid in ['A.1.2','A.2.1','A.3.1','A.4.1','A.4.2']:
    status='T' if sid in ['A.1.2','A.4.1'] else 'K'
    credit='FAM supporting calculation; E26 finite models' if sid in ['A.1.2','A.4.1'] else 'DGKXv1; FAM explicit re-derivation'
    x,_=add(sid,status,'Appendix B',r'Definition~\ref{def:conventions}; FAM A.1.1 and preceding appendix calculations.',kind='New proof' if status=='K' else 'Theorem',credit=credit)
    appb+=x
appb+='\\subsubsection{Re-derivation of FAM A.5.1}\n'+steps(notation(get_block(FAM,'A.5.1')[2],'A.5.1'))+'\n'
# The universal map assertion is supplied by DGKX, rather than silently attributed to FAM A.1.1.
pst=dgtext.index('\\begin{proof}',m.end());pend=dgtext.index('\\end{proof}',pst)+len('\\end{proof}')
dp=dgtext[pst:pend].replace('a\\in\\cA','c\\in\\mathcal P').replace('X_a','X_c').replace('f_a','f_c').replace('\\Pone','\\mathbb P^1').replace('\\Z','\\mathbb Z').replace('\\cO','\\mathcal O')
dp=dp.replace('Fix $a$','Fix $c$')
appb+=r'''\subsubsection{The universal map statement}
The following source proof is that of \cite[Theorem 7.2]{DGKXv1}, with its parameter renamed; it is reproduced with that credit rather than attributed to the workbench.
'''+steps(dp)+'\n'

w=WB.read_text()
w=re.sub(r'^%.*\n','',w,flags=re.M)
w=notation(w).replace('\\mathscr V','\\mathcal V').replace('\\mathcal L','\\mathcal L_{\\rm per}')
w=w.replace('ffcert:thm:normalization','fam:A.1.2').replace('prop:period-input-audit','fam:A.3.1').replace('thm:canonical-ring-recovery','fam:A.1.1')
w=w.replace('\\subsection{Exact global identifications of the retained period parameter}','\\subsection{Exact global identifications of the retained period parameter}')
w=w.replace('w_j','\\ell^{\\log}_j')
# Scope-specific root variable; period/discrete-data symbols keep the first run's meaning.
wa=w.index('The actual ramified base change');wb=w.index('In particular one may not replace the generator',wa)
w=w[:wa]+re.sub(r'(?<![A-Za-z\\])u(?![A-Za-z_])',lambda m:r's_{\rm new}',w[wa:wb])+w[wb:]
w=w.replace('comparing the $u$ and $w$','comparing the $u_{\\Lambda}$ and $w_{\\Lambda}$')
wa=w.index('Given an equivariant first component');wb=w.index('Thus projection is surjective there.',wa)
w=w[:wa]+re.sub(r'(?<![A-Za-z\\])u(?![A-Za-z_])',lambda m:r'h_{\rm loc}',w[wa:wb])+w[wb:]
for mm in list(re.finditer(r'\\begin\{(theorem|lemma)\}\[([^\]]+)\]\s*\\label\{([^}]+)\}(.*?)\\end\{\1\}',w,re.S))[::-1]:
    env,title,label,body=mm.groups()
    raw=re.search(r'\\begin\{'+env+r'\}\[[^\]]+\]\s*\\label\{'+re.escape(label)+r'\}(.*?)\\end\{'+env+r'\}',WB.read_text(),re.S)[1].strip()
    body=body.strip()
    records.append(dict(paper_label=label,statement_as_printed=body,status='K',source_run='WORKBENCH',source_id=label,source_file='workbench/period_shift_classification.tex',wording_vs_source='same content: statement retained; source proof has only declared notation/label conversions, numbered-step typography and K credit heading',found_in_AC26='not found: Remark 6.4 leaves exact parameter equivalence open; same search as FAM A.5.1.',found_in_E26='not found: searched exact equivalence, 2Z, parity and parameter shifts.',found_in_DGKX_v1='found: Theorem 1.4 and §7 centralizer/finite norm calculation.',credited_to='DGKXv1 for theorem; workbench for the independently obtained proof, with no date comparison',checks='Verbatim source statement preserved after notation mapping; entire supplied workbench fragment read; external source labels mapped to supplied FAM counterparts.',kind='New proof',uses='Retained period construction; canonical pencil; finite normalization; explicit centralizer and gluing',summary='Retained-family equivalence and its centralizer/finite-filling obstruction.',proof_location='Appendix A',source_statement=raw))
    repl='\\begin{cited}[WORKBENCH; K: '+title+']\\label{'+label+'}\n'+body+'\n\\end{cited}\n\\uses{The period data (PS1)--(PS4); the numbered steps below and the retained construction.}\n'
    w=w[:mm.start()]+repl+w[mm.end():]
w=re.sub(r'\\begin\{proof\}.*?\\end\{proof\}',lambda m:steps(m[0]),w,flags=re.S)
appA=r'''The proof in this appendix is the supplied workbench fragment, produced by GPT-5.6 Sol (Codex, reasoning effort ultra) and GPT-6 Astra (Codex, reasoning effort ultra). Its mathematical content is retained. Reference labels for the canonical pencil, finite normalization and period sheaf are mapped to their supplied FAM counterparts; the concordance records these conversions.
'''+w

(OUT/'sections.tex').write_text(sec1+'\n'+sec2)
(OUT/'appendix_a.tex').write_text(appA)
(OUT/'appendix_b_periods.tex').write_text(appb)
(OUT/'records.json').write_text(json.dumps(records,indent=2,ensure_ascii=False))
(OUT/'notation.md').write_text('''# Root notation and labels

FAM conventions are unchanged: rho=exp(pi i/3); clockwise root deck generators, positive base meridians, Pi_c and w=exp(-pi i c). P_E is renamed P_mark in statements and proofs. Dual covectors u,w appearing in linear combinations and their coefficient comparisons are u_Lambda,w_Lambda; hatted homology vectors retain their names. The shorthand macro for hatted delta is dhat, avoiding the standard T1 command dh. The modular nome is q_tau and the modular discriminant is Delta_mod, agreeing with the periods section; finite discs Delta_j, vector q_n and the auxiliary division-model discriminant keep their distinct meanings.

Scoped renamings avoid collisions with the global parameters u=w^2 and w. In FAM A.1.1 the square root of E_6 is h_6, and the two canonical-ring sections u,v are s_can,t_can (the abstract polynomial generators U,V are unchanged). In FAM A.3.1 the preliminary first-coordinate lift is h_loc. In FAM A.4.2 the moving torus coordinate w is zeta^new and its projector P is P_KS. In FAM B.1.1, B.1.2 and B.1.4 the line-bundle fibre coordinate W is v, exactly as in the first-run conventions; it is distinct from the cusp fibre W. The reciprocal cusp coordinate v=1/t is r_cusp, including the differential in B.1.3. The B.1.3 blow-up parameter u=t-1 is v_t, agreeing with the duplication section. The holomorphic torus-valued unit u(t_c) of B.2.1 is v_unit(t_c). These edits change symbols only, never hypotheses or algebraic identities.

Workbench mathscr V → mathcal V; its homogeneous line mathcal L → mathcal L_per; its local logarithms w_j → ell_j^log; its finite base-change variable u → s_new; its local equivariant first-component function u(z) → h_loc(z). The covector coefficient comparison uses u_Lambda,w_Lambda consistently. Both u replacements are confined to the source paragraphs defining those local variables; the global Engel parameter is unchanged. No sign is changed. Its missing labels ffcert:thm:normalization, prop:period-input-audit and thm:canonical-ring-recovery are mapped respectively to FAM A.1.2, A.3.1 and A.1.1, whose displayed calculations have been matched.

Every retained FAM st:ID label becomes fam:ID. The workbench pshift labels are retained. The companion universal map-factorization statement comes from DGKXv1 thm:all-maps-factor; it is not part of the supplied FAM A.1.1 statement. DGKX a → c and cA → mathcal P. PUSH E.1.1 and E.1.2 are printed as announcements as mandated, with their statement bodies retained.
''')
print('Root records',len(records),'TeX characters',sum(len(t) for t in [sec1,sec2,appb,appA]))
