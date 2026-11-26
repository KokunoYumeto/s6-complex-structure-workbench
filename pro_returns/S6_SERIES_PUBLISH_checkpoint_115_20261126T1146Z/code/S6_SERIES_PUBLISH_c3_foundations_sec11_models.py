from S6_SERIES_PUBLISH_c3_foundations_sec11_helpers import *
from collections import Counter

main=(ROOT/'S6_SERIES_PUBLISH_II.tex').read_text()
p=Package('models','subsec:II:torsion-interface-models')
inputs={n:(OUT/f'S6_SERIES_PUBLISH_II_sec11_models_UN{n}_input.tex').read_text().rstrip() for n in [66,67,70,80,83]}
for n,body in inputs.items():
 assert block(main,f'cdp:st:C.2.UN.{n}')==body,(n,'Current owner differs from fully read input.')

parts={name:(OUT/f'S6_SERIES_PUBLISH_II_sec11_models_{name}.tex').read_text() for name in ['P354','UN80','UN70_UN83']}
parts['UN70_UN83']=parts['UN70_UN83'].replace('Neron--Severi',r"N\'eron--Severi")
(OUT/'S6_SERIES_PUBLISH_II_sec11_models_UN70_UN83.tex').write_text(parts['UN70_UN83'],newline='\n')

# Record each inherited manual display and printed run-reference conversion.
# These old intermediate copies are not receiving manuscript fragments.
for n in [70,80,83]:
 p.clean(inputs[n],f'cdp:st:C.2.UN.{n}')
 for i,m in enumerate(re.finditer(r'\\ref\{(cdp:[^{}]+)\}',inputs[n]),1):
  key=m.group(1)
  p.record('D04',f'cdp:st:C.2.UN.{n}',m.group(0),
           (r'\eqref{' if ':eq:' in key else r'\cref{')+key+'}',
           f'Use statement-type or equation navigation at the receiving owner or its exact application; the common proof has the explicit morphism recorded in the comparison. Occurrence {i}.')
 for i,m in enumerate(re.finditer(r'\brequired\b',inputs[n]),1):
  p.record('D05,D08',f'cdp:st:C.2.UN.{n}',m.group(0),'',
           f'The receiving proof states the resulting geometric map directly. Occurrence {i}.')

start66=inputs[66].index(r'\item Consider a component $T$ meeting a known elliptic')
end66=inputs[66].index(r'\item Start with the maximum Hopf',start66)
old66part=inputs[66][start66:end66]
new66part=r'''\item Consider a component $T$ meeting an elliptic boundary $C$ with torsion normal. Apply \cref{cdp:st:C.2.UN.83} to the same full reduced SNC family with identity normalization, $J=C$, and its unchanged boundary. The curve is isolated because there are no triple points. That proposition excludes rational $T$ and supplies its three marked surface models.

Every point map in this application is the identity. A minimal $T$ has no $(-1)$-curve. For an allowed projective-line bundle over a positive-genus base, every rational curve is a ruling fibre and has square zero; the rational bundles were just excluded. Thus there is no first curve to contract. The three models consequently describe the given component and its marked curves themselves.

The one-section ruled description would make $T$ an eligible terminal pair for \cref{cdp:st:C.2.UN.64}, already removed in forming $S_0$. A nonlinear Hopf description is its torsion-normal leaf. In every other case the elliptic map \eqref{cdp:eq:C.TI.1} is defined on this same $T$, has every boundary vertical, and has the full identity-monodromy, fixed-Jacobian and smooth-multiple conclusions \eqref{cdp:eq:C.MR.8}.

For a ruled component this is the quotient \eqref{cdp:eq:C.MR.11}: its first cover is $T'=T\times_E C$, its section normal is the same $L$ in \eqref{cdp:eq:C.MR.10}, and its product cover kills that $L$. For nonnegative Kodaira dimension the degree-one component cover identifies its minimal model with $T$, and \eqref{cdp:eq:C.MR.12}--\eqref{cdp:eq:C.MR.14} give the marked quotient through the same principal torsor and Chern-class pullback. These are the ruled and nonruled maps constructed in \cref{cdp:st:C.2.UN.83}; their normal-order identifications carry each boundary to its full fibre support.

'''
new66=inputs[66][:start66]+new66part+inputs[66][end66:]
assert new66.split(r'\end{proposition}',1)[0]==inputs[66].split(r'\end{proposition}',1)[0]
(OUT/'S6_SERIES_PUBLISH_II_sec11_models_UN66_receiving.tex').write_text(new66+'\n',newline='\n')
p.record('D12,D14,D20','cdp:st:C.2.UN.66',old66part,new66part,
 'Transfer the complete shared ruled/nonnegative marked-alignment calculation to the single earlier UN83/UN70 owner, with C.MR.9 at P354 and C.MR.10--14 at the common classification. Apply it to the identical minimal-or-bundle component T and isolated C; its point map is the identity. The complete UN66 statement is byte-identical, and the remainder of its proof is unchanged.')

def statement(body):
 return body[:body.index(r'\end{proposition}')+len(r'\end{proposition}')]

p.record('D12,D14,D20,D25','cdp:st:C.2.UN.70',statement(inputs[70]),statement(parts['UN70_UN83']),
 'UN70 is the nonnegative-coefficient clause of the single NC normalization classification. Its entire embedded-SNC domain, elliptic map, normal multiplicity, inverse point maps, rational-boundary and Hopf-parent conclusions remain explicitly stated; its tag and label become aliases at that owner. No statement is refuted or narrowed.')
p.record('D12,D14,D20,D25','cdp:st:C.2.UN.83',statement(inputs[83]),statement(parts['UN70_UN83']),
 'Preserve all three original NC models, both inverse self-double branches, every coefficient, normal line, extension, exceptional-prime support and neighbour-order conclusion. The common proof now has the earlier explicit NC field premise and no reliance on a later UN70/UN80 proof.')
p.record('D12,D14,D20,D25','cdp:st:C.2.UN.80',statement(inputs[80]),statement(parts['UN80']),
 'State the precise elliptic-map data formerly inherited from UN70. Every original UN70 datum satisfies them, and the proved NC elliptic branch does also. The full constant-combination, nowhere-zero extension, fixed period lattice and every exceptional-prime polar conclusion remain.')

maps=[
 ('cdp:st:C.2.UN.70',r'\par\medskip\noindent\textbf{Ruled minimal model:',r'\item At least one other',parts['P354'],'Ruling, isogeny, all lifted sections, weighted full-fibre identity, section-preserving contraction and equivariant quotient are proved once at P354.'),
 ('cdp:st:C.2.UN.83',r'\par\medskip\noindent\textbf{A section:',r'\item Suppose that one exists.',parts['P354'],'Replace the second section-preserving point-map proof by P354 on the exact degree-one specialization. Its C.TI.13 target moves to the full preserved normal-line map.'),
 ('cdp:st:C.2.UN.80',r'\item \par\medskip\noindent\textbf{The actual field space',r'\item Remove finitely many',parts['UN80'].split(r'\begin{enumerate}',1)[0],'Apply the fully read current P260 NC normalization field and polar-locus owner through r:E→P; retain the exact C.EP.3 conclusion without another saturation proof.'),
]
for owner,a,b,target,reason in maps:
 old=inputs[int(owner.rsplit('.',1)[1])]
 a0=old.index(a);b0=old.index(b,a0)
 p.record('D12,D17,D20',owner,old[a0:b0],target,reason)

for n,filename in [(80,'code/A_translation_exceptions.py'),(83,'code/A_torsion_interfaces.py')]:
 body=inputs[n]
 loc=body.index(filename)
 a=body.rfind(r'\item',0,loc);b=body.index(r'\end{enumerate}',loc)
 p.record('D07,D09,D21',f'cdp:st:C.2.UN.{n}',body[a:b],'',
          'The complete mathematical period, root, valuation, graph and normal-order proofs remain at their receiving owners. Program-execution and certificate bookkeeping is omitted from the manuscript; no new computation or independent-check credit is claimed.')

def oldspan(n,start,end):
 body=inputs[n];a=body.index(start);b=body.index(end,a)+len(end);return body[a:b]
scope=[
 (70,oldspan(70,'No contraction of any','ambient threefold is asserted.'),'The inverse point blowups of fibres of $q_Z$, with their centres, positions and normal maps, recover $T$ and its marked curves.'),
 (80,oldspan(80,'This assertion\nconcerns','changed.'),'Every prime exceptional for $\\pi$ is a polar divisor of its meromorphic lift $W_P$.'),
 (83,oldspan(83,'No sign is\nimposed','canonical divisor.'),'Write the induced meromorphic canonical section as'),
 (83,oldspan(83,'No replacement of an','logarithmic model is used.'),'Every model preserves the marked normal line and all boundary branches.')
]
for n,old,new in scope:
 p.record('D02,D11',f'cdp:st:C.2.UN.{n}',old,new,'State the exact domain and preserved maps positively at the single receiving statement. The mathematical scope is retained by the explicit normalization, point morphism and canonical coefficients.')

p.record('D12,D20,D22','cdp:st:C.2.UN.83',
 oldspan(83,r'\item First let \(d\ge2\).',r'\par\medskip\noindent\textbf{A section: the contraction retaining its actual normal line.}'),
 parts['UN70_UN83'][parts['UN70_UN83'].index(r'\item\textbf{The multisection pencil'):parts['UN70_UN83'].index(r'\item\textbf{The one-section ruled')],
 'The original Picard map and |mJ1| pencil are retained and identified with the product quotient by its exact coordinate z^m and subgroup G_L. Its connected elliptic fibres and group descent follow through this explicit map, replacing the second independent construction proof.')
p.record('D12,D17,D20','cdp:st:C.2.UN.83',
 oldspan(83,r'\item If \(H\) is nonlinear,',r'\par\medskip\noindent\textbf{The actual ruling and its elliptic multisection.}'),
 parts['UN70_UN83'][parts['UN70_UN83'].index('For a nonlinear $H$'):parts['UN70_UN83'].index(r'\item\textbf{Ruled models')],
 'Apply the complete current P352 single-Hopf-curve owner with a=-a_J and the same pushed section, including its unramified primary and finite secondary maps. All discrepancy and neighbour-order conclusions remain here.')
p.record('D12,D17,D20','cdp:st:C.2.UN.66',
 old66part[old66part.index(r'\item  Let $q_0:T\to B_0$'):old66part.index(r'\item  In Kodaira dimension zero')],
 parts['UN70_UN83'][parts['UN70_UN83'].index('For this latter map'):parts['UN70_UN83'].index('The Jacobian of each point blowup')],
 'Use the general canonical quasibundle clause already proved at P351. Its full line formula, raised to N and the Cartier equality q*(b_i)=m_i C_i, gives exactly C.MR.12 and the complete base-degree argument at the shared model owner.')

# Move the intact admitted rational obstruction before the common models.
idx67=main.index(r'\label{cdp:st:C.2.UN.67}')
a67=main.rfind(r'\subsection',0,idx67)
b67=main.index(inputs[67],a67)+len(inputs[67])
unit67=main[a67:b67]
assert 'subsec:II:torsion-normal-rational-obstruction' in unit67
header66=r'\subsection{Contractions to elliptic cores}\label{subsec:II:elliptic-core-reduction}'
assert main.count(header66)==1
insert=unit67+'\n\n'+parts['P354']+'\n'+parts['UN80']+'\n'+parts['UN70_UN83']+'\n'+header66
p.guard('Move admitted UN67 prerequisite: old position',unit67,'','Move this exact complete already-admitted subsection before the common models; no movement or new subsection-completion credit.')
p.guard('Insert shared ruling/field/model owners before UN66',header66,insert,'Dependency order is the current P260, intact UN67, P354, UN80, common UN83/UN70, then the unchanged-statement UN66 application.')
p.guard('UN66 exact shared-model application',inputs[66],new66,'Complete old/receiving proof comparison; the entire statement including its hidden header is byte-identical, and only the shared marked-alignment proof block changes.')
p.guard('Remove duplicate UN70 owner',inputs[70],'','All mathematical conclusions, stable labels and tags are at the single earlier UN83/UN70 classification and its explicit nonnegative-coefficient clause.')
p.guard('Remove old UN80 position',inputs[80],'','The complete generalized explicit-map owner is proved earlier before its first model consumer.')
p.guard('Remove duplicate later UN83 owner',inputs[83],'','The complete three-model statement and proof are consolidated at the earlier common owner.')
for label,title in [('subsec:II:vertical-elliptic-models','Reduction of exceptional configurations'),('subsec:II:negative-interface-reduction','Reduction above the maximum Hopf order')]:
 pattern=r'\\subsection\{[^{}]+\}\\label\{'+re.escape(label)+r'\}'
 matches=list(re.finditer(pattern,main));assert len(matches)==1,label
 old=matches[0].group();new=r'\subsection{'+title+r'}\label{'+label+'}'
 p.guard('Bound the remaining '+label,old,new,'The remaining reduction subsection stays open. Its header now describes the actual remainder after the earlier-owner transfer.')
 p.record('D13,D14',label,old,new,'Keep the unreviewed reduction remainder under its existing actual subsection identity; no relocation-only progress is claimed.')
p.record('D13,D14','lem:II:section-preserving-ruling',header66,insert,'Place the proved common inputs before the elliptic-core application and the later restoration arguments, in three descriptive actual subsections. The unchanged UN67 transfer is prerequisite placement only.')

fragment=parts['P354']+'\n'+parts['UN80']+'\n'+parts['UN70_UN83']+'\n'+header66+'\n\n'+new66+'\n'
p.write(fragment)

state=main
for guard in p.guards:
 assert state.count(guard['old'])==1,(guard['key'],state.count(guard['old']))
 state=state.replace(guard['old'],guard['new'],1)
# Only this bounded package's permanent-identifier transfer is checked.
oldall=''.join(g['old'] for g in p.guards)
newall=''.join(g['new'] for g in p.guards)
for pat in [r'\\label\{([^{}]+)\}',r'\\hypertarget\{([^{}]+)\}']:
 oldc=Counter(re.findall(pat,oldall));newc=Counter(re.findall(pat,newall))
 for key,value in oldc.items():
  assert newc[key]==value,(key,value,newc[key])
for body in re.findall(r'\\begin\{equation\}([\s\S]*?)\\end\{equation\}',fragment):
 assert not re.search(r'\n[ \t]*\n',body),'Blank paragraph in numbered display.'
 assert body.count(r'\SsixEquationAliases')<=1,'Multiple alias hooks in one display.'
assert r'\tag{' not in ''.join(parts.values())
print('Eight bounded guards replay once; old identifiers preserved; UN66 statement byte-identical. Full receiving read remains pending.')
