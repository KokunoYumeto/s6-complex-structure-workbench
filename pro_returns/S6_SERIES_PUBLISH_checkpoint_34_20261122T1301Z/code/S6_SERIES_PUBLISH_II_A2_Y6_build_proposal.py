#!/usr/bin/env python3
"""Build only A2's R13 proposal, with exact sequential text guards."""
from pathlib import Path
import hashlib,json,re,difflib

root=Path(__file__).resolve().parents[1]
A=root/'agents/continuation2_A'
original=root/'agents/ii_infra/released_proofs/02Y6/e2c1bb7f36a82389/S6_SERIES_PUBLISH_full_owning_block.tex'
old=original.read_text();new=old;guards=[]
def edit(before,after,defects,reason,count=1):
    global new
    actual=new.count(before)
    assert actual==count,(before[:100],actual,count)
    guards.append({'id':f'Y6-{len(guards)+1:03d}','old':before,'new':after,
      'expected_count':count,'defect_ids':defects,'reason':reason})
    new=new.replace(before,after)

old_statement=old[:old.index('\\begin{proof}')]
statement=r'''\begin{proposition}[Elliptic components of the conductor]\hypertarget{tag-02Y6}{}\label{night:P4R.13}\label{stmt:P4R.13}\label{night:P4R.13:elliptic-components}
\StatementRecord{night:P4R.13}{proved}{02Y6}{}

In the standing torus-fibration setting of
\cref{def:II:standing-torus-fibration}, let $mS$ be a fibre
with irreducible, reduced, singular support. Suppose that the
normalization of $S$ has a ruled resolution and that the
reduced image conductor has a component with elliptic
normalization. Then the normalization of $S$ is a smooth
minimal elliptic ruled surface, the image conductor is a
disjoint union of one or two smooth elliptic curves, and
$e(S)=0$. Along each of these curves every local germ is the
product of its generic transverse germ with a disc. No
rational conductor component is attached to them.

When there are two image components, the normalization
conductor consists of two disjoint sections of the minimal
ruling. Each section maps to its own image curve by an
unramified double cover, and every transverse germ is $A_1$.
\end{proposition}
'''
edit(old_statement,statement,['D25','D10','D04','D16'],
 'Refute the unqualified one-image assertion by the frozen compact example; retain the whole standing domain, preserve owner/tag and original labels, add the exact refined alias, and state the proved one-or-two component classification.')
enumeration=r'\begin{enumerate}[label={$\langle1\rangle$\arabic*.},leftmargin=*]'
added=(A/'S6_SERIES_PUBLISH_II_A2_Y6_added_cases_working.tex').read_text()
edit(enumeration,added.rstrip(),['D25','D04'],
 'Add the omitted genus-zero exclusion and full reduced-horizontal classification before the thirteen retained doubled-horizontal items; move their common normalization setup here and remove the production-marker enumeration.')
prefix=r'''\item Let $\rho_N:T\to N$ be the minimal normalization resolution,
let $\nu:N\to S$ be the finite normalization, and put
$\rho=\nu\rho_N$. The reduced-horizontal case is already
proved by P4R.9. We therefore use the actual double-horizontal
pole divisor $D$ of P4R.6.'''
replacement=r'''\item In the remaining case the minimal-model divisor is
$D_0=2H_0+V_0$, where $H_0$ is a smooth section and $V_0$
is vertical. The pole divisor $D$ of \cref{night:P4R.6}
has the doubled-horizontal form.'''
edit(prefix,replacement,['D25'],
 'Remove the false delegation of one-image uniqueness to R9. The preceding two items now establish positive genus and exclude the reduced-horizontal case before entering the original doubled-section argument. The exact normalization maps were moved unchanged to the common setup.')

edit('P4R.7--P4R.9',r'\cref{night:P4R.7,night:P4R.9}',['D04'],
 'Resolve the existing pushout and curve-group reference by its permanent statement labels.')
for name in ['P4.33','P4R.6','P4.31','P4.30','P4R.10']:
    pattern=r'(?<![A-Za-z0-9:{])'+re.escape(name)+r'(?![A-Za-z0-9]|\.\d)'
    hits=list(re.finditer(pattern,new))
    # Replace each bounded textual occurrence separately, using enough
    # neighbouring prose to make its exact guard unique.
    for match in reversed(hits):
        lo=new.rfind('\n\n',0,match.start())+2
        hi=new.find('\n\n',match.end())
        if hi<0:hi=len(new)
        paragraph=new[lo:hi]
        changed=re.sub(pattern,lambda _:r'\cref{night:'+name+'}',paragraph)
        if paragraph==changed:continue
        edit(paragraph,changed,['D04'],
             'Replace the existing prose result identifier by its exact statement reference.')
        # A paragraph with repeated same references is handled in one guard.
        break
    # Handle any further paragraphs after the initial reverse-index pass.
    while re.search(pattern,new):
        match=re.search(pattern,new);lo=new.rfind('\n\n',0,match.start())+2
        hi=new.find('\n\n',match.end())
        if hi<0:hi=len(new)
        paragraph=new[lo:hi]
        edit(paragraph,re.sub(pattern,lambda _:r'\cref{night:'+name+'}',paragraph),
             ['D04'],'Resolve remaining existing prose result identifiers to exact statement labels.')

labels={
 'P4R.13.1':'eq:II:elliptic-conductor-algebra-injection',
 'P4R.13.2':'eq:II:elliptic-conductor-blowup-pushforward',
 'P4R.13.3':'eq:II:elliptic-primary-Euler-comparison',
 'P4R.13.4':'eq:II:elliptic-primary-zero-Euler-chain',
 'P4R.13.5':'eq:II:elliptic-tacnode-fourth-jet'}
for tag,label in labels.items():
    before='\\tag{'+tag+'}'
    edit(before,before+'\\label{'+label+'}',['D04'],
         'Preserve the original displayed equation tag and mathematical expression; add a semantic hyperlink label.')
    before='('+tag+')'
    count=new.count(before)
    if count:edit(before,'\\eqref{'+label+'}',['D04'],
       'Replace a raw internal equation reference by its new semantic hyperlink.',count)

edit('''singularities. We use Greb, Remark~2.1, p.~415
\\cite{Greb2011}.''',
     '''singularities \\cite[Remark~2.1, p.~415]{Greb2011}.''',
     ['D18'],'Keep the same primary theorem and exact analytic hypotheses; place its opened precise locator in the citation.')
program=r'''The exact coefficient changes, discriminant
weights and degree identities are executed
in \texttt{code/part4/elliptic\_primary\_restriction.py};
its JSON and text outputs are retained.
'''
edit(program,'',['D09'],
 'Move the program citation to the Programs table; the retained proof already states the computations, inputs and exact results.')

style=[
 ('yields the actual\nmorphism','yields the\nmorphism'),
 ('in the actual\nmap to the minimal ruled surface','in the\nmap to the minimal ruled surface'),
 ('and on the actual equation of','and on the equation of'),
 ('a nonempty actual\nblowup sequence','a nonempty\nblowup sequence'),
 ('We evaluate the right side using the actual primary\nideal, without removing the rational components from\nthe left side.',
  'We evaluate the primary quotient on the right side;\nthe left side is the Euler characteristic of the\nentire conductor scheme.')]
for before,after in style:
 edit(before,after,['D08','D02'],
      'State the same mathematical map or scope directly; remove process emphasis and defensive phrasing.')

before='''The\nparametrized Morse lemma and a cube root\nof the residual unit now give the product\nequation $X^2+Y^3=0$ at every point of $E$.'''
after=r'''The parametrized Morse lemma gives
$F=a(x,y,z)(x-\chi(y,z))^2+h(y,z)$, with $a$ a unit
and $\chi$ solving $F_x=0$. Here $h=y^3b(y,z)$ with
$b$ a unit. The coordinates
$X=(x-\chi)\sqrt a$ and $Y=y\sqrt[3]b$, together with $z$,
give the product equation $X^2+Y^3=0$ at every point of $E$.'''
edit(before,after,['D22'],
     'Keep the same parametrized Morse and unit-root argument, displaying its exact coordinate maps at the point where the product form is asserted.')
before='''it never vanishes. The residual function
is $y^4$ times a unit, giving a product
tacnode at every point of $E$.'''
after=r'''it never vanishes. In the same Morse coordinates the
residual function is $h=y^4b(y,z)$ with $b$ a unit.
The coordinate $Y=y\sqrt[4]b$, together with the quadratic
coordinate $X$ and $z$, gives the product tacnode
$X^2+Y^4=0$ at every point of $E$.'''
edit(before,after,['D22'],
     'Keep the residual-quartic argument and exhibit the exact fourth-root coordinate map for its asserted product germ.')

assert len(re.findall(r'\\item\b',new))==15
assert new.count(r'\hypertarget{tag-02Y6}')==1
assert all(x in re.findall(r'\\label\{([^}]+)\}',new) for x in re.findall(r'\\label\{([^}]+)\}',old))
old_displays=re.findall(r'\\\[(.*?)\\\]',old,re.S)
new_displays=re.findall(r'\\\[(.*?)\\\]',new,re.S)
def canonical_display(x):return re.sub(r'\s+','',re.sub(r'\\label\{[^}]+\}','',x))
assert len(old_displays)==14
old_c=[canonical_display(x) for x in old_displays]
new_c=[canonical_display(x) for x in new_displays]
assert all(x in new_c for x in old_c)
proposal=A/'S6_SERIES_PUBLISH_II_A2_02Y6_proposed_working.tex'
proposal.write_text(new)
(A/'S6_SERIES_PUBLISH_II_A2_Y6_proposal_guards_working.json').write_text(json.dumps(guards,indent=2)+'\n')
(A/'S6_SERIES_PUBLISH_II_A2_Y6_proposal_working.diff').write_text(''.join(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile=str(original.relative_to(root)),tofile=str(proposal.relative_to(root)))))
replay=old
for g in guards:
 assert replay.count(g['old'])==g['expected_count']
 replay=replay.replace(g['old'],g['new'])
assert replay==new
print(json.dumps({'proposal_sha256':hashlib.sha256(new.encode()).hexdigest(),
 'proposal_bytes':len(new.encode()),'guards':len(guards),'original_items':13,
 'new_items':15,'original_displays_preserved':len(old_c),
 'new_displays':len(new_c),'old_item_to_new_item':{str(i):i+2 for i in range(1,14)}},indent=2))
