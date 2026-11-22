"""Prepare exact 02Y2 proposals in the checker directory; no canonical writes."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

REC = Path('agents/ii_checks_A/recovery_20261121T195642Z')
OUT = REC / 'group11_Y2'
OUT.mkdir(exist_ok=True)
released = Path('agents/ii_infra/released_proofs/02Y2/7cbacc27defe4a41/S6_SERIES_PUBLISH_full_owning_block.tex')
original = released.read_text()
proposed = original
sha = lambda x: hashlib.sha256(x.encode()).hexdigest()
oldpath = OUT / 'S6_SERIES_PUBLISH_II_02Y2_full_original.tex'
newpath = OUT / 'S6_SERIES_PUBLISH_II_02Y2_full_proposed.tex'
oldpath.write_text(original)
guards = []


def change(old, new, defects, reason, transport):
    global proposed
    assert proposed.count(old) == 1, (old, proposed.count(old))
    before = proposed
    at = before.index(old)
    proposed = before[:at] + new + before[at+len(old):]
    guards.append({'tag': '02Y2', 'guard_id': f'A_REC_02Y2_{len(guards)+1:03}',
                   'defect_types': defects, 'literal_old': old, 'literal_new': new,
                   'reason': reason, 'mathematical_transport': transport,
                   'offset_before': at, 'intermediate_before_sha256': sha(before),
                   'intermediate_after_sha256': sha(proposed),
                   'full_original_path': str(oldpath), 'full_proposed_path': str(newpath)})


change('[P4R.1]', '[Fundamental group of an irreducible fibre]', ['D04', 'D16'],
       'Give the proposition a mathematical title.', 'The statement, owner, tag and both labels retain their identities.')
change('\\begin{enumerate}[label={$\\langle1\\rangle$\\arabic*.},leftmargin=*]\n\\item \nWe give the neighbourhood and group comparison explicitly.\n',
       'Write the degeneration as $f:X\\to\\Delta$.\n', ['D04', 'D08', 'D14'],
       'Remove the isolated one-item run wrapper and state the map being used.',
       'The proper holomorphic degeneration in the statement is denoted f:X→Δ; its original single proof item remains the proof.')
change('The compatible triangulation of Lojasiewicz, Theorem~2,\n\\noindent\\textbf{Step 1. Triangulation of semi-analytic sets}, p.~464 \\cite{Lojasiewicz1964}, applies to\n',
       'The compatible triangulation of {\\L}ojasiewicz\n\\cite[Theorem~2, p.~464]{Lojasiewicz1964} applies to\n', ['D18', 'D23'],
       'Remove the article title incorrectly formatted as a proof step and restore the author accent.',
       'The same Theorem2 and printed page464 in the opened1964 primary edition are cited.')
change('After barycentric\nsubdivision $S$ is a full subcomplex. In an open star of this\nsubcomplex, erase the barycentric coordinates at vertices\noutside $S$ and normalize the remaining coordinates to sum\nto one. Linear interpolation gives a strong deformation\nretraction $r:V\\to S$. The star can be chosen inside a\nrelatively compact neighbourhood of $S$.',
       'Let $\\tau:|K|\\to X$ be the resulting homeomorphism and\n$L\\subset K$ the subcomplex with $|L|=\\tau^{-1}(S)$.\nAfter barycentric subdivision, $L$ is a full subcomplex.\nFor barycentric coordinates $\\lambda_v$, put\n$q=\\sum_{v\\in L}\\lambda_v$. On the open star $q>0$, the map\n\\[\n r_K\\Bigl(\\sum_v\\lambda_v v\\Bigr)\n   =\\sum_{v\\in L}\\frac{\\lambda_v}{q}v\n\\]\nerases the other coordinates and divides the remaining ones\nby their sum. For $0\\le s\\le1$, the interpolation\n$H_s(x)=(1-s)x+s r_K(x)$ stays in the same star, since\n$q(H_s(x))=(1-s)q(x)+s>0$, and fixes $L$.\nTransport by $\\tau$ gives a strong deformation\nretraction $r:V\\to S$. Compactness of $S$ and successive\nsubdivision make $V$ lie inside a relatively compact\nneighbourhood of $S$.', ['D20', 'D22'],
       'Write the coordinate map and its transport instead of leaving the renormalization implicit.',
       'Exactly the original erase-and-rescale map: r=τ∘r_K∘τ^-1, H transported byτ. Frozen derivation§2 proves fullness, continuity, homotopy and cofinality.')
change('This retraction comparison also follows from the statement\nimmediately after Definition~1 of Fernandez de Bobadilla--Kollar,\n\\noindent\\textbf{Step 2. Homotopically trivial deformations}, p.~85 \\cite{BobadillaKollar2012}; the preceding\nconstruction supplies the particular comparison needed here.',
       'The neighbourhood-retraction statement immediately after\nDefinition~1 of Fern\\\'andez de Bobadilla--Koll\\\'ar\n\\cite[p.~85]{BobadillaKollar2012} applies to the same proper\nmap $f:X\\to\\Delta$.', ['D08', 'D18', 'D23'],
       'Give the ordinary source citation and its exact receiving map.',
       'The opened publisher p85 states the fibre-neighborhood retraction for proper morphisms of complex spaces; specialize y=0 and f:X→Δ.')
change('The extension splits because its quotient is infinite cyclic.',
       'Choose $t$ mapping to $1$ in the infinite cyclic quotient.\nEvery element is uniquely $\\lambda t^n$, with $\\lambda\\in\\Lambda$;\nconjugation by $t$ gives the displayed semidirect product.', ['D22'],
       'State the splitting map and the group operation it induces.',
       'n↦t^n is a section; g↦(gt^-n,n), n=winding(g), is its inverse decomposition. This is the same split extension.')
change('The smooth locus of the\nirreducible $S$ is connected, so those meridians are conjugate,\nwith their positive orientation fixed by a complex transverse\ncoordinate.',
       'The smooth locus of the\nirreducible $S$ is connected. Along a path in that locus, a\ntrivialization of its complex normal line gives an annulus of\npositive meridians in $U^*$, proving their conjugacy. The complex\nnormal coordinate fixes their positive orientation.', ['D22'],
       'Display the annulus giving conjugacy and fix its orientation.',
       'The path interval trivializes the complex normal line; its small circle bundle is the annulus carrying one positive meridian to the other. The complete kernel argument is retained and checked.')
change('At a smooth point of $S$, the defining map is a unit times\n$z^m$. A positive meridian therefore maps to $m$ under\n$\\pi_1(U^*)\\to\\mathbb Z$.',
       'At a smooth point of $S$, write $f=vz^m$ with $v$ a\nholomorphic unit. On a small coordinate neighbourhood,\n$z\'=z\\exp((\\log v)/m)$ is a holomorphic normal coordinate\nand $f=(z\')^m$. For small $a>0$, the positive circle\n$z\'=a\\exp(2\\pi i\\theta)$, $0\\le\\theta\\le1$, maps to\n$a^m\\exp(2\\pi im\\theta)$, so its image under\n$\\pi_1(U^*)\\to\\mathbb Z$ is $m$.', ['D20', 'D22'],
       'Give the exact unit-removing coordinate and the oriented circle map.',
       'The coordinate derivative is v(point)^(1/m)≠0, and f=(z′)^m exactly. The same full multiplicity m and positive meridian are used.')
change('This proves the assertion for the actual support,\nwithout replacing it by its normalization.',
       'This proves the assertion for $\\pi_1(S)$.', ['D02', 'D08', 'D11'],
       'End with the proved group conclusion.',
       'The maps i:S→U and r:U→S already identify the receiving space. No mathematical assertion or hypothesis changes.')
change('\n\\end{enumerate}\n\\end{proof}', '\n\\end{proof}', ['D04', 'D14'],
       'Close the proof after removing its single-item wrapper.', 'Only the presentation wrapper is removed.')

newpath.write_text(proposed)
canonical = Path('S6_SERIES_PUBLISH_II.tex')
source = canonical.read_text()
bstart=source.index('\\begin{thebibliography}')
bend=source.index('\\end{thebibliography}',bstart)
bibliography=source[bstart:bend]
bibguards=[]
for key in ['BobadillaKollar2012','Lojasiewicz1964']:
    blocks=re.split(r'(?=\\bibitem)',bibliography)
    old=next(b for b in blocks if re.search(r'\\bibitem(?:\[[^\n]*\])?\{'+key+r'\}',b))
    new=old.replace('\\newblock \\emph{Verified}.\n','')
    if key=='BobadillaKollar2012':
        new=new.replace('Fernandez~de Bobadilla and Kollar(2012)',"Fern\\'andez~de Bobadilla and Koll\\'ar(2012)")
        new=new.replace('Javier Fernandez~de Bobadilla and Janos Kollar.',"Javier Fern\\'andez~de Bobadilla and J\\'anos Koll\\'ar.")
    else:
        new=new.replace('Scienze}, 18\\penalty0 (4):','Scienze}, ser.~3, 18\\penalty0 (4):')
        new=new.replace('https://www.numdam.org/article/ASNSP_1964_3_18_4_449_0.pdf','https://www.numdam.org/item/ASNSP_1964_3_18_4_449_0.pdf')
    assert new!=old and source.count(old)==1
    bibguards.append({'key':key,'literal_old':old,'literal_new':new,'defect_types':['D08','D18','D23'],
        'reason':'Remove the process marker and use the opened primary edition with exact author/journal metadata.',
        'mathematical_transport':'Stable bibliography key and cited theorem/page retained; exact original publisher/archive PDF bound in the primary reading records.',
        'source_path':str(canonical),'source_sha256':sha(source),'source_character_offset':source.index(old)})

table_start=source.index('\\section*{Programs}')
table_end=source.index('\\end{longtable}',table_start)
table_old=source[table_start:table_end+len('\\end{longtable}')]
row=r'''Barycentric retraction identities and the symbolic meridian winding map (\cref{night:P4R.1}) & \href{https://raw.githubusercontent.com/KokunoYumeto/s6-complex-structure-workbench/\SsixRepositoryCommit/code/S6_SERIES_PUBLISH_II_A_02Y2_neighborhood_certificate.py}{\nolinkurl{S6_SERIES_PUBLISH_II_A_02Y2_neighborhood_certificate.py}} \\[3pt]
'''
table_new=table_old.replace('\\end{longtable}',row+'\\end{longtable}')

manifest={'created_utc':datetime.now(timezone.utc).isoformat(),'checker':'ii_check_a','canonical_writes':0,
    'guards':guards,'blocks':[{'tag':'02Y2','original_path':str(oldpath),'proposed_path':str(newpath),
       'original_sha256':sha(original),'proposed_sha256':sha(proposed),'statement_unchanged':True,
       'scope_repairs':[],'proof_repairs':[],'exact_map_explications':['τ∘r_K∘τ^-1','n↦t^n','normal-circle annulus','z′=z exp(log(v)/m)']}],
    'bibliography_guards':bibguards,'program_table_guard':{'literal_old':table_old,'literal_new':table_new,'source_path':str(canonical),'source_sha256':sha(source),'source_character_offset':table_start,'defect_types':['D09'],'reason':'Associate the new universal algebra certificate with its owning proposition.','mathematical_transport':'Only the displayed retraction and meridian maps are computed; the topology is proved in the text and check record.'},
    'note':'All literal edits require root review. Root owns canonical integration and the common final repository commit.'}
path=OUT/'S6_SERIES_PUBLISH_II_A_Y2_editorial_proposals.json'
path.write_text(json.dumps(manifest,indent=2)+'\n')

forward=original
for g in guards:
    assert sha(forward)==g['intermediate_before_sha256']
    assert forward.count(g['literal_old'])==1
    forward=forward.replace(g['literal_old'],g['literal_new'],1)
    assert sha(forward)==g['intermediate_after_sha256']
assert forward==proposed
back=proposed
for g in reversed(guards):
    at=g['offset_before'];assert back[at:at+len(g['literal_new'])]==g['literal_new']
    back=back[:at]+g['literal_old']+back[at+len(g['literal_new']):]
assert back==original
validation={'created_utc':datetime.now(timezone.utc).isoformat(),'owner_guard_count':len(guards),'forward_exact':True,'inverse_exact':True,'source_original_match_count':source.count(original),'original_sha256':sha(original),'proposed_sha256':sha(proposed),'no_canonical_writes':True}
(OUT/'S6_SERIES_PUBLISH_II_A_Y2_guard_validation.json').write_text(json.dumps(validation,indent=2)+'\n')
print(json.dumps({'manifest':str(path),'validation':validation},indent=2))
