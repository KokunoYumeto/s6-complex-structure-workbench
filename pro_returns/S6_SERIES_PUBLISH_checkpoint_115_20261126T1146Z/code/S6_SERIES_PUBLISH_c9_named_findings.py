#!/usr/bin/env python3
"""Prepare exact Paper III finding edits; never write the canonical source."""
from pathlib import Path
import csv
import re

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'agents/continuation9_findings'
OUT.mkdir(parents=True, exist_ok=True)
SOURCE = ROOT / 'S6_SERIES_PUBLISH_III.tex'
source = SOURCE.read_text()
edits = []

def add(finding, suffix, types, statement, old, new, reason, page='cp100 reading copy; see finding'):
    assert old != new
    count = source.count(old)
    assert count == 1, (finding, suffix, count, old[:100])
    edits.append(dict(change_id=f'CLAUDE-III-{finding}-{suffix}', type=types,
        statement_id=statement, old_location=f'cp100 source; {statement}', old_page=page,
        new_location=statement, new_page='pending final build', old_text=old,
        new_text=new, reason=reason,
        review_status='Exact replacement prepared and reread; canonical application and rendered review pending.'))

add('P1','ABSTRACT','D15;D22','abstract',
    'We also determine weighted smooth types and the homology of every free\nOS49 affine cap, including its additional three-primary torsion. A\nweighted OS45 member has zero refined Pontryagin class, as follows',
    'We also determine weighted smooth types and the homology of every free\naffine cap over the elliptic surface with fibres $IV^*,II,I_2$,\nincluding its additional three-primary torsion. A weighted member over\nthe surface with fibres $I_8,4I_1$ has zero refined Pontryagin class, as follows',
    'The two surface descriptions are exactly those in the explicit OS49 construction (02S2) and weighted OS45 datum. The abstract now supplies their geometric fibre configurations. No model or invariant changes.', '1')
add('P1','F45','D22','series:III:F',
    r'\item For the OS45 data of Definition~\ref{maps:def:weighted-os45-data},',
    '\\item For the OS45 data of Definition~\\ref{maps:def:weighted-os45-data},\n'
    'where OS45 denotes entry~45 of\n'
    '\\cite[Main Theorem table, p.~85]{manOguisoShioda91}\n'
    '(root lattice $A_7$, Mordell--Weil lattice $\\langle1/8\\rangle$),',
    'Opened Oguiso--Shioda 1991 p.85: entry 45 has root lattice A7 and torsion-free rank-one Mordell--Weil lattice with generator height 1/8. The description fixes the meaning at first main-text use.', '9')
add('P1','F49','D22','series:III:F',
    '\\item For the OS49 affine cap with $m=3k$, $k>0$ and\n',
    '\\item For the affine cap of entry~49 of the same table\n'
    '(OS49, with root lattice $E_6\\oplus A_1$ and Mordell--Weil\n'
    'lattice $\\langle1/6\\rangle$), let $m=3k$, $k>0$ and\n',
    'Opened Oguiso--Shioda 1991 p.85: entry 49 is E6+A1 with rank-one height 1/6. The same affine parameters are retained.', '9')
add('P1','NOTATION','D13;D22','mapsIII:def:finite-filling-inputs',
    'Use the marked Mordell--Weil generator $G$ and the following\nconfigurations and integers $n$:',
    'Throughout the elliptic-profile tables, OS$j$ denotes entry $j$ of\n'
    '\\cite[Main Theorem table, p.~85]{manOguisoShioda91},\n'
    'with its listed root lattice and Mordell--Weil lattice. For the\n'
    'torsion-free rank-one entries used here, $G$ is a marked generator\n'
    'and $n=1/\\langle G,G\\rangle$. The configurations and these\n'
    'integers are:',
    'The eight printed values 2,8,4,14,6,12,20,30 are the reciprocal generator heights of entries 43,45,46,47,49,50,55,56, read from the primary table. The notation is fixed in the numbered input definition.', '114')

# P2: explicit cleveref names are independent of the package capitalization option.
add('P2','DEFAULT-THEOREM','D23','preamble',
    r'\usepackage[nameinlink,noabbrev]{cleveref}',
    r'\usepackage[nameinlink,noabbrev,capitalise]{cleveref}',
    'The capitalise option also covers the default theorem environment, which has no explicit crefname in this preamble. Explicit custom singular/plural names are capitalized separately; all reference targets remain unchanged.')
for match in re.finditer(r'\\crefname\{([^}]+)\}\{([^}]+)\}\{([^}]+)\}', source):
    kind, single, plural = match.groups()
    new = r'\crefname'+'{'+kind+'}{'+single[:1].upper()+single[1:]+'}{'+plural[:1].upper()+plural[1:]+'}'
    if new != match.group(0):
        add('P2',kind.upper(),'D23','preamble',match.group(0),new,
            'Capitalize the explicit cleveref singular and plural names, retaining the theorem-counter mapping and every label. This controls all corresponding automatic references.')

add('P3','PART','D14;D23','part:open-problems',
    r'\part{Open problems}',
    '\\part*{Open problems}\n\\phantomsection\n\\addcontentsline{toc}{part}{Open problems}',
    'The final part remains in the contents and PDF navigation with its unchanged title, without a part numeral that can be read as the paper identifier.')
add('P5','ZHUBR','D18','series:III:E',
    '\\cite[Theorem~3, p.~795; \\S4.1, p.~809]{manZhubr75}.\n\n\\hypertarget{main-III-F}{}',
    '\\cite[Theorems~3 and~5, pp.~795--796; \\S4.1, p.~809]{manZhubr75}.\n\n\\hypertarget{main-III-F}{}',
    'The complete proof of 02K9 uses Theorem 5 for injectivity of (P,h), then Theorem 3 and Section 4.1 for marked smooth recognition. This matches the existing Known and new locator exactly.', '8')
add('P6','CONJUNCTION','D23','series:III:F',
    r' \gcd(k,n,d)=1,\qquad 3\nmid n\ \text{or}\ 3\mid k.',
    r' \gcd(k,n,d)=1\quad\text{and}\quad(3\nmid n\ \text{or}\ 3\mid k).',
    'The original comma encodes conjunction with the following alternative, as the n=0 case and the cited free-cap theorem specify. Parentheses display exactly that Boolean formula.', '9')
add('P7','MODEL','D07;D15','methodology',
    'and publication work during 20--25 November 2026. Its numerical\nreasoning-effort setting was not separately exposed. GPT-6 Astra Pro\n(OpenAI), in ChatGPT Pro mode, continued the publication work on\n25 November 2026, also without a separately exposed numerical\neffort setting.',
    'and publication work during 20--26 November 2026.',
    'One setup is named once as GPT-6 Astra (OpenAI), ChatGPT Pro mode, following prompt section 4.1; 26 November includes this continuation. Historical signed event rows retain their original attribution.', '14')
add('P7','CLAUDE-DATES','D15','methodology',
    'Paper~II on 24 November. It also checked the publication material\nreceived during 23--25 November, including arithmetic and\nsource-scope questions.',
    'Paper~II on 24 November, and began its reading of Paper~III on\n'
    '25 November. It also checked the publication material received\n'
    'during 23--25 November, including arithmetic and source-scope\n'
    'questions; its Paper~III reading and computations continued on\n'
    '26 November.',
    'The attached reading log starts on 25 November and records continued reading and computations on 26 November; the existing model/effort attribution remains in the preceding sentence.', '14')
add('P8','TWISTS','D13;D22','mapsIII:def:marked-family',
    'The multiple fibres have $f^*p_j=m_jS_j$, and\n$W=f^{-1}(p_0)$ is the reduced cusp. The standard twists are\n\\[\n v_1=(1,2,-4,0)^t,\\qquad v_2=(-1,-3,3,0)^t.\n\\]\nFor general twists we write $p=12\\ell_0-4\\ell_1-3\\ell_2$.',
    'The multiple fibres have $f^*p_j=m_jS_j$, and\n'
    '$W=f^{-1}(p_0)$ is the reduced cusp. Write\n'
    '\\[\n \\varepsilon_1=(1,2,-4,0)^t,\\qquad\n'
    ' \\varepsilon_2=(1,3,-3,0)^t,\\qquad\n'
    ' v_j=\\ell_j\\varepsilon_j+k_j\\widehat\\delta\\quad(j=1,2),\n\\]\n'
    'where $\\ell_j,k_j\\in\\mathbb Z$. In the real period marking,\n'
    'the finite root generator acts by\n'
    '$(s,x)\\mapsto(e^{-2\\pi i/m_j}s,A_jx+v_j/m_j)$.\n'
    'The integer $\\ell_0$ is the cusp clutching winding: after the\n'
    'vanishing fibre cycles are killed, the remaining fibre generator\n'
    '$z$ and clockwise peripherals $x,y$ satisfy\n'
    '$x^3=z^{\\ell_1}$, $y^4=z^{\\ell_2}$ and $xy=z^{\\ell_0}$.\n'
    'Put $p=12\\ell_0-4\\ell_1-3\\ell_2$. The standard twists have\n'
    '$(\\ell_1,\\ell_2,k_1,k_2)=(1,-1,0,0)$, hence\n'
    '$v_1=\\varepsilon_1$ and $v_2=-\\varepsilon_2$.',
    'The definition now introduces every integral twist parameter before use. Its finite action is exactly the action in the complete 02KD proof; the cusp winding and peripheral powers are those derived in 02K7. The coordinate identification is the displayed ordered homology basis. The standard second vector equals -epsilon2 entry by entry.', '16')
add('P9','VERSION','D18','bibliography:HatcherSpectralSequences',
    '\\bibitem[Hatcher(n.d.)]{HatcherSpectralSequences}\nAllen Hatcher.\n\\newblock Spectral sequences.\n\\newblock Additional Chapter~5 of \\emph{Algebraic Topology}, preliminary version.\n\\newblock \\url{https://pi.math.cornell.edu/~hatcher/AT/ATch5.pdf}.',
    '\\bibitem[Hatcher(2022)]{HatcherSpectralSequences}\nAllen Hatcher.\n'
    '\\newblock Spectral sequences.\n'
    '\\newblock Preliminary additional Chapter~5 of \\emph{Algebraic Topology},\n'
    'PDF version of 29 April 2022, 117 pages.\n'
    '\\newblock \\url{https://pi.math.cornell.edu/~hatcher/AT/ATch5.pdf}.\n'
    '\\newblock Page references use this version, consulted 26 November 2026.',
    'Downloaded the author-hosted 117-page PDF, SHA256 d65a738385f4d060cc4d11862a5826f4d2f65d2e9a92c903b2ed2ae2ecedd46e. Its PDF CreationDate is 29 April 2022; this is explicitly a PDF-version date, not a claim about original composition. Theorem 5.41(b) is on printed p.573 and states the cited pi6(S3)=Z/12.')
add('P10','LIFTING','D18','maps:src:A.2.2',
    r'\cite[Proposition~4.1 and its proof, p.~342]{Hatcher2002}.',
    r'\cite[Proposition~1.33, p.~61]{Hatcher2002}.',
    'Opened Hatcher Algebraic Topology p.61, Proposition 1.33. The source S6 is connected, locally path connected and simply connected, so its fundamental-group image is zero and lies in the covering subgroup. The based lift to R follows. The old Proposition 4.1 proof also invokes this criterion; the new locator is direct.', '20')

add('P11','B32','D08','maps:src:B.3.2',
    '$L=\\ell\'$. These are literal identifications of the maps just\nconstructed, with their inverse notation changes. The neighbourhood',
    '$L=\\ell\'$. The neighbourhood',
    'The complete assignment N=N0, r=|q|, alpha=bar-pi, h=pi-prime, L=ell-prime remains immediately before this sentence. Only the repeated assertion that variable names invert is removed.')
add('P11','CUSP','D08','mapsIII:def:retained-angle-cusp-data',
    'the base parameter and the constant upper suspension value. The\nidentity on this intrinsic cusp, with itself as inverse, therefore\nidentifies every local map used below for all these members.\n\nWrite $t=q$ and $q=t$ for the two inverse names of the cusp\nparameter, and $h_{\\rm per}=h$ for the period function in that\ndefinition, with inverse $h=h_{\\rm per}$. The radial convention\nhas $B_0=J$ in the same ordered bases. In the real period\ndecomposition below, $u=u_{\\rm long}$ and $k=v$ from that\ndefinition, with inverse assignments $u_{\\rm long}=u$ and $v=k$.',
    'the base parameter and the constant upper suspension value. Every\n'
    'local map below therefore agrees on their common intrinsic cusp.\n\n'
    'Write $t=q$ for the cusp parameter and $h_{\\rm per}=h$ for\n'
    'the period function in that definition. The radial convention\n'
    'has $B_0=J$ in the same ordered bases. In the real period\n'
    'decomposition below, write $u=u_{\\rm long}$ and $k=v$.',
    'All coordinate assignments and the actual cusp translation with inverse T_{-sigma} remain. The common intrinsic domain and maps are stated directly; no nonidentity map is removed.')
add('P11','HOPF','D08','mapsIII:lem:lie-torus-spin-invariant',
    'The coordinate identification is the identity on $\\mathbb C^2$,\nwith inverse itself, and the circle parameter map is $\\theta=a$,\nwith inverse $a=\\theta$. Thus its proved translation-framed\ncircle represents this same $\\eta$.',
    'These are the same complex coordinates, with circle parameter\n'
    '$\\theta=a$, so the translation-framed circle represents $\\eta$.',
    'The preceding explicit Hopf map, fibre and two derivative normal vectors are unchanged. The equality of ordered coordinates and theta=a retains the exact identification.')
add('P11','H-SMOOTHING','D08','maps:src:B.3.1',
    'The source and target maps are the identical ones defined above,\nwith inverse notation changes $H=f$, $M=N$ and $y_0=y$.\nWrite $H_b=f_b$ for the first endpoint in that lemma, with inverse\n$f_b=H_b$. In its notation take the protected tube $T=U_1$;',
    'Write $H_b=f_b$ for the first endpoint in that lemma and\n'
    'take the protected tube $T=U_1$;',
    'The explicit application f=H, N=M, x0=xbase, y=y0, n=4 remains directly above. The first endpoint and protected tube retain their assignments; no smoothing map or inverse construction changes.')
add('P11','THREE-SMOOTHING','D08','maps:src:B.4.1',
    'The inverse naming map is $H=f$; the regular value $y$ is the\nsame chosen open-cell value, and the target coordinates are the',
    'The regular value $y$ is the chosen open-cell value, and the\ntarget coordinates are the',
    'The application already states f=H:X to S4. Only its redundant reverse naming is removed; the actual target chart is retained.')
add('P11','THREE-FRAME','D08','maps:src:B.4.1',
    'contraction of this same comparison matrix; the inverse coordinate\nidentification is $(a,b)\\mapsto(a,b)$.',
    'contraction of this comparison matrix.',
    'The preceding identification explicitly uses the same ordered angular coordinates and the stated constant frame change. The two nontrivial K_v factors and their contraction remain.')
add('P11','THREE-DECK','D08','maps:src:B.4.1',
    '$\\alpha=h+[L_{\\rm ext}]$. These are the same operations as the cited construction\nwith the identity on its real native deck coordinates; the inverse\ncoordinate map is the identity.',
    '$\\alpha=h+[L_{\\rm ext}]$. These are the operations of the cited\nconstruction in the same real native deck coordinates.',
    'The explicit cutoff formulas for h and L_ext and their identity alpha=h+[L_ext] remain; native deck coordinates are unchanged.')
add('P11','FILLING-NAMES','D08','mapsIII:def:three-filling-datum',
    'where the inverse naming map sends each unhatted basis vector\nto its displayed hatted vector. Thus\n$v_1=g+2u-4w$, $v_2=-g-3u+3w$, and the cusp translation drift is zero.',
    'Thus $v_1=g+2u-4w$, $v_2=-g-3u+3w$, and the cusp\ntranslation drift is zero.',
    'The ordered equality (g,u,w,d)=(gamma-hat,u-hat,w-hat,delta-hat) remains in the display. This retains the precise basis assignment.')
add('P11','BAND-NAMES','D08','mapsIII:def:finite-band-coverings',
    'The inverse naming map sends $(g,u_h,w_h,d)$ to its displayed\nhatted basis. Write $(\\gamma,u,w,\\delta)$ for the dual basis\nof $V=H^1(F;\\mathbb Z)$; thus $u=u^*$, $w=w^*$ and\n$\\delta=\\delta^*$ in the cell-presentation proof, with the\ninverse assignments $u^*=u$, $w^*=w$, $\\delta^*=\\delta$.',
    'Write $(\\gamma,u,w,\\delta)$ for the dual basis of\n'
    '$V=H^1(F;\\mathbb Z)$; thus $u=u^*$, $w=w^*$ and\n'
    '$\\delta=\\delta^*$ in the cell-presentation proof.',
    'The ordered homology-basis equality remains above; the ordered dual and its aliases remain here. No lattice change is deleted.')
add('P11','BAND-MAPS','D08','mapsaudit:finite-degree-three',
    'matrices and translations. Under the identity of the ordered\nmarked lattices, with inverse the same identity, its bases\n$(\\rho_1,w_h)$ and $(\\rho_2,w_h)$ give the degree-one maps',
    'matrices and translations. In the same ordered marked lattices,\n'
    'its bases $(\\rho_1,w_h)$ and $(\\rho_2,w_h)$ give the degree-one maps',
    'Both displayed Q matrices, their integral basis data and the preceding identification with the exact affine quotient remain unchanged.')
add('P11','UNDERLYING','D08','mapsIII:def:canonical-cyclic-model',
    'structure. The oriented smooth manifold $M_d$ is the underlying\nmanifold of $Z_d$: the identification is the identity on points,\nwith each complex chart read as a real chart, and its inverse is\nthe same identity.',
    'structure. Let $M_d$ be the underlying smooth manifold of $Z_d$,\nwith its complex orientation.',
    'The exact operation is forgetting the complex structure in each chart while retaining the same points, transitions and complex orientation. The definition and its scope d prime to six are preserved.')

add('P12','THEOREM-END','D04;D13','maps:src:B.3.1',
    '\\(\\eta^2\\), so injectivity gives the exact equality\n\\cref{maps:src:B.3.1}.  Finally, a based null-homotopy of \\(q_2\\)\nwould postcompose with \\(p_3\\) to a based null-homotopy of \\(H\\),\ncontradicting \\cref{maps:src:B.3.1}.',
    '\\(\\eta^2\\), so injectivity gives \\eqref{maps:eq:B.3.1}.',
    'The proof concludes its own labelled display by the already established injectivity; the separate q2 non-nullhomotopy argument moves to the following corollary where q2 is in the statement.', '50')
add('P12','COROLLARY','D13','wb:h24:ret:q2-detected-quotient',
    'This is the nonzero element of the target group of order two,\nso \\(\\varepsilon\\) is surjective.',
    'This is the nonzero element of the target group of order two,\n'
    'so \\(\\varepsilon\\) is surjective. A based null-homotopy of\n'
    '\\(q_2\\) would postcompose with \\(p_3\\) to a based null-homotopy\n'
    'of \\(H\\), contradicting \\eqref{maps:eq:B.3.1}.',
    'The moved implication is exactly postcomposition p3 of the hypothetical based homotopy. It preserves the original proof step and now directly supports the corollary conclusion alpha nonzero.', '50')

# Both wrong-kind references are in one completely read theorem/proof.
block_start=source.index(r'\begin{theorem}[Homology and framed fibre of the attaching model]')
block_end=source.index(r'\subsection{Integral degree-three maps of the finite band}',block_start)
block=source[block_start:block_end]
needle=r'Theorem~\ref{maps:src:B.1.1}'
assert block.count(needle)==2
for n,m in enumerate(re.finditer(re.escape(needle),block),1):
    a=block.rfind('\n',0,m.start())+1;b=block.find('\n',m.end())
    old=block[a:b]
    add('P13',str(n),'D23','maps:src:B.5.2',old,
        old.replace(needle,r'\cref{maps:src:B.1.1}'),
        'The permanent label maps:src:B.1.1 belongs to a Lemma. Automatic reference reads its registered environment and preserves the exact referenced statement.', '62; 66')

block_start=source.index(r'\begin{theorem}[An OS49 family with three-prime torsion]') if r'\begin{theorem}[An OS49 family with three-prime torsion]' in source else source.rfind(r'\begin{theorem}',0,source.index(r'\label{maps:src:D.2.11}'))
# Locate the exact theorem owning the 02KL permanent tag.
tag=source.index(r'\hypertarget{tag-02KL}')
block_start=source.rfind(r'\begin{theorem}',0,tag)
block_end=source.index(r'\end{proof}',tag)+len(r'\end{proof}')
block=source[block_start:block_end]
for n,m in enumerate(re.finditer(re.escape(r'M_{IV}'),block),1):
    a=block.rfind('\n',0,m.start())+1;b=block.find('\n',m.end())
    old=block[a:b]
    if any(x['old_text']==old for x in edits):continue
    add('P16',str(n),'D20;D23','maps:src:D.2.11',old,old.replace(r'M_{IV}',r'M_{IV^*}'),
        'The matrix and every entry are unchanged. Its subscript now records the IV-star fibre specified by the ordered tuple (II,IV-star,I2) and the given order-three monodromy.', '144')

add('P16','TYPE-C-REFERENCE','D20;D23','os49:rem:type-c-marking',
    r''' (M_{II},M_{IV})\longmapsto
 (M_{IV},M_{IV}^{-1}M_{II}M_{IV}).''',
    r''' (M_{II},M_{IV^*})\longmapsto
 (M_{IV^*},M_{IV^*}^{-1}M_{II}M_{IV^*}).''',
    'This ordered-pair Hurwitz comparison explicitly cites the (II,IV-star,I2) marking of 02KL. The same unchanged IV-star matrix now has the same subscript at this dependent use. The displayed Hurwitz map and lattice conjugacies remain unchanged.')

add('P17','F','D20','series:III:F',
    '$m_1n_0+m_0n_1=\\pm1$, give one oriented smooth type $M_d$ for',
    '$m_1n_0+m_0n_1=\\pm1$, give one oriented smooth type $M_d^{\\rm w}$ for',
    'The weighted family receives a distinct symbol for all positive d; the cyclic-cover model keeps M_d on its original coprime domain.')
add('P17','F-ID','D20','series:III:F',
    '$-12$ and $0$. For $d$ prime to six this is the type of\nTheorem~\\ref{series:III:E}, under the marking of\n\\cref{maps:src:D.2.48}.',
    '$-12$ and $0$. For $d$ prime to six,\n'
    '$M_d^{\\rm w}\\cong M_d$ with the complex orientations and\n'
    'the marking proved in \\cref{maps:src:D.2.48}, where $M_d$ is\n'
    'the cyclic-cover model of Theorem~\\ref{series:III:E}.',
    '02LP compares the complete marked (P,mu) invariants and gives F*=psi_cyclic psi_weighted^{-1}; that proved oriented map identifies the two notations exactly on the common coprime domain.')
add('P17','OUTLINE','D20','step-III-F-6',
    '$M_d$ for every $d>0$ (\\cref{maps:src:D.2.48}).',
    '$M_d^{\\rm w}$ for every $d>0$ (\\cref{maps:src:D.2.48}).',
    'The outline uses the same new weighted-family symbol as its full statement.')
start=source.index(r'\begin{definition}[Weighted Engel data]')
end=source.index(r'\subsection',source.index(r'\end{proof}',start))
weighted=source[start:end]
for n,m in enumerate(re.finditer(r'\$M_[d1]\$',weighted),1):
    a=weighted.rfind('\n',0,m.start())+1;b=weighted.find('\n',m.end())
    old=weighted[a:b]
    if any(x['old_text']==old for x in edits):continue
    new=old.replace('$M_d$',r'$M_d^{\rm w}$').replace('$M_1$',r'$M_1^{\rm w}$')
    add('P17','WEIGHTED'+str(n),'D20','maps:src:D.2.48',old,new,
        'Only the symbol of the weighted representative is changed. The full marked-invariant argument, chosen construction and all parameter scopes are preserved.')
add('P17','WEIGHTED-ONE','D20','maps:src:D.2.48',
    'One has $M_1=S^6$, and for $d$ prime to six this is the\ntype in \\ref{maps:src:D.1.11}, under the marking proved below.',
    'One has $M_1^{\\rm w}=S^6$ and, for $d$ prime to six,\n'
    '$M_d^{\\rm w}\\cong M_d$ with the complex orientations and the\n'
    'marking proved below; here $M_d$ is the model of\n'
    '\\cref{maps:src:D.1.11}.',
    'This is the exact existing coprime recognition, with the two representatives now named separately. The proof gives the induced H2 isomorphism and its inverse.')
add('P17','WEIGHTED-ONE-PROOF','D20','maps:src:D.2.48',
    r'the orientation-preserving identification $M_1=S^6$.',
    r'the orientation-preserving identification $M_1^{\rm w}=S^6$.',
    'The d=1 representative in this proof is the weighted construction; its marked recognition and explicit stable tangent map are unchanged.')

fields=['change_id','type','statement_id','old_location','old_page','new_location','new_page','old_text','new_text','reason','review_status']
with (OUT/'S6_SERIES_PUBLISH_c9_named_findings_defects.tsv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(edits)

# This exact sequential application is a readback check in memory only.
candidate=source
for e in edits:
    assert candidate.count(e['old_text'])==1,(e['change_id'],'overlap or stale text')
    candidate=candidate.replace(e['old_text'],e['new_text'],1)
assert re.findall(r'\\label\{[^}]+\}',source)==re.findall(r'\\label\{[^}]+\}',candidate)
assert re.findall(r'\\hypertarget\{[^}]+\}',source)==re.findall(r'\\hypertarget\{[^}]+\}',candidate)
print(f'Prepared {len(edits)} exact edits; canonical TeX unchanged; labels and targets preserved in order.')
print('Findings represented:', ', '.join(sorted({e['change_id'].split('-')[2] for e in edits},key=lambda x:int(x[1:]))))
print('P14 and P15 remain under substantive review; P4 is reserved for the five-together step.')
