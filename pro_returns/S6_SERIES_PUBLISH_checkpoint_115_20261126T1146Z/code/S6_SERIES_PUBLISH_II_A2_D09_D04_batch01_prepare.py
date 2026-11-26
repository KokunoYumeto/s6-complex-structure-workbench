#!/usr/bin/env python3
"""Prepare a bounded, reversible three-proof editorial proposal.

The complete owning blocks were read first. This program changes only
A2 proposal files, never the canonical source, ledger or inventory.
"""
from pathlib import Path
import csv
import difflib
import hashlib
import json
import re

root=Path(__file__).resolve().parents[1]
d=root/'agents/continuation2_A/S6_SERIES_PUBLISH_II_A2_D09_D04_batch01_working'
paper=root/'S6_SERIES_PUBLISH_II.tex'
source=paper.read_text()
targets=[('night:P4R.10','02Y3'),('night:P4R.14','02Y7'),('night:P4R.15','02Y8')]
all_rows=[]
bound=[]
for owner,tag in targets:
    before=(d/f'S6_SERIES_PUBLISH_II_A2_{tag}_before.tex').read_text()
    assert source.count(before)==1,(owner,'current block changed')
    new=before
    rows=[]
    def edit(old,replacement,defects,reason,disposition='Every mathematical assertion, map and formula in this span is retained.'):
        global new
        assert old!=replacement
        assert new.count(old)==1,(tag,old[:100],new.count(old))
        assert replacement
        rows.append({'id':f'A2-ED01-{tag}-{len(rows)+1:02d}',
                     'owner':owner,'tag':tag,'old':old,'new':replacement,
                     'expected_count':1,'defect_ids':defects,
                     'reason':reason,'mathematical_disposition':disposition})
        new=new.replace(old,replacement)

    old_enum=r'\begin{enumerate}[label={$\langle1\rangle$\arabic*.},leftmargin=*]'
    edit(old_enum,r'\begin{enumerate}[label=\arabic*.,leftmargin=*]',['D10'],
         'Remove the production-marker prefix from the unchanged proof-item numbering.')

    if tag=='02Y3':
        edit('Let $S$ be an irreducible reduced fibre support in Part~4.2.',
             'Let $S$ be an irreducible reduced fibre support in the standing\n'
             r'torus-fibration setting of \cref{def:II:standing-torus-fibration}.',
             ['D04','D05'],'Resolve the former Part4.2 scope to the verbatim standing setting P204; the domain is unchanged.')
        for raw in ['P4.29','P4.30']:
            pattern=re.compile(r'(?<![A-Za-z0-9:{])'+re.escape(raw)+r'(?![A-Za-z0-9]|\.\d)')
            match=pattern.search(new);assert match
            lo=new.rfind('\n',0,match.start())+1;hi=new.find('\n',match.end())
            old=new[lo:hi]
            edit(old,pattern.sub(lambda _:r'\cref{night:'+raw+'}',old),['D04'],
                 'Replace the raw source-run statement number with its exact current owner reference.')
        old=r'''The program \texttt{code/part4/tacnode\_hessian.py} verifies the
two lattice inequalities for the stated bounds, the exact
rank-one Hessian on the singular parametrization
$(t^2,t^3,0)$, and the simple Hessian zero of the permitted
local model $zx^2+xy^2$. Its JSON and text outputs retain
the bounds; the preceding inequalities prove the unrestricted
statement.'''
        replacement=r'''The local Hessian calculations can also be written explicitly.
Put $H=y^2-x^3$ and
$F=(\alpha z+\gamma H)^2+H^4$, with constants
$\alpha\ne0$ and $\gamma$. Along $(t^2,t^3,0)$,
the first-order part of $\alpha z+\gamma H$ gives
\[
 \operatorname{Hess}(F)=2\ell\ell^{\mathsf T},
 \qquad\ell=(-3\gamma t^4,\,2\gamma t^3,\,\alpha)^{\mathsf T}.
\]
This matrix has rank one. For $zx^2+xy^2$, restriction
of the Hessian to $x=y=0$ gives
$\operatorname{diag}(2z,0,0)$, whose quadratic coefficient
has a simple zero at the origin.'''
        edit(old,replacement,['D09','D08'],
             'Move the program path, bounded-run report and output bookkeeping to Programs/check records while keeping both exact local examples in the proof.',
             'All preceding uniform lattice inequalities remain unchanged. The cusp-parameter example is now defined by its exact historical polynomial, with aa=alpha and cc=gamma; its rank-one Hessian is printed. The zx^2+xy^2 simple Hessian zero is retained explicitly. Historical finite test ranges and counts remain in the retrieval receipt and comparison, not as proof of an unrestricted theorem.')

    elif tag=='02Y7':
        edit('Let $S$ be an actual reduced support in Part~4.2. At a point',
             'Let $S$ be a reduced fibre support in the standing torus-fibration\n'
             r'setting of \cref{def:II:standing-torus-fibration}. At a point',
             ['D04','D05','D08'],'Resolve the input-fibration domain by P204 and remove process emphasis; no local hypothesis changes.')
        for raw in ['P4.28','P4.16']:
            pattern=re.compile(r'(?<![A-Za-z0-9:{])'+re.escape(raw)+r'(?![A-Za-z0-9]|\.\d)')
            while (match:=pattern.search(new)):
                lo=new.rfind('\n',0,match.start())+1;hi=new.find('\n',match.end())
                if hi<0:hi=len(new)
                old=new[lo:hi]
                edit(old,pattern.sub(lambda _:r'\cref{night:'+raw+'}',old),['D04'],
                     'Resolve the exact spherical-obstruction or boundary-comparison dependency. Original equation tags and raw equation references are reserved for the separate D19 pass.')
        edit('The actual coordinate $Z=U(y,z)$ gives $X^2+y^4Z$.',
             'The coordinate $Z=U(y,z)$ gives $X^2+y^4Z$.',['D08'],
             'Keep the explicit coordinate map and equation without process emphasis.')
        edit('sphere to the actual nearby torus. Its universal cover is',
             'sphere to the nearby torus. Its universal cover is',['D08'],
             'Keep the proper transported sphere and target unchanged.')
        edit('on which the positive degree is retained. This argument\nuses no analyticity assertion for the image of a nonproper\nmap.',
             'on which the positive degree is retained.',['D02'],
             'Remove the defensive description of an unused assertion; the complete stratified measure-zero argument and positive local degree remain.',
             'No image-analyticity theorem is inserted or used; the actual proof remains the same countable-stratum measure argument printed immediately before this sentence.')
        edit('sphere, of square $-2$, into an actual nearby torus. This is',
             'sphere, of square $-2$, into a nearby torus. This is',['D08'],
             'Keep the exact intersection square and proper comparison unchanged.')
        edit(r'''\item The distinction between a pole coefficient and this
torus-smoothing conclusion can be checked by an exact
retained local test. Take''',
             r'''\item The following reduced hypersurface has pole coefficient two
and a positive-genus exceptional curve:''',['D01','D02','D08'],
             'State the mathematical example directly. The entire subsequent normalization, discrepancy, pole and polar calculation is retained.',
             'The local example still proves compatibility of pole coefficient two with an elliptic exceptional curve, and its polar deformation still excludes a torus smoothing. No categorical distinction is asserted without the concrete maps.')
        edit('for the displayed total reduced hypersurface. It is excluded\nhere by the polar deformation, not by the coefficient alone.',
             'for the displayed total reduced hypersurface. Its polar\ndeformation excludes a torus smoothing, as follows.',
             ['D02','D08'],'Keep the demonstrated torus-smoothing obstruction and state its mechanism directly.')
        edit(r'''For $H\mapsto H-\varepsilon$ all six scale by
$\varepsilon^{1/3}$ and converge to the origin. The
identities and these exact rational calculations are
executed in \texttt{code/part4/smooth\_a3\_polar.py},
with JSON and text output retained.''',
             r'''For $H\mapsto H-\varepsilon$ all six scale by
$\varepsilon^{1/3}$ and converge to the origin.''',
             ['D09','D08'],'Move only the program filename and output report to Programs/check records.',
             'Every polynomial, both displayed Groebner generators, the six simple solutions, the three unit-ideal assertions, the nonzero critical values and the exact epsilon^(1/3) scaling remain in the proof.')
        edit('the exact Groebner basis',r'the exact Gr\"obner basis',['D23'],
             'Restore the accent in the mathematical name; the displayed basis is unchanged.')

    else:
        edit('At every critical-curve point of an actual reduced support in\nPart~4.2 with nonzero ambient Hessian, holomorphic coordinates',
             'At every critical-curve point of a reduced fibre support in the\n'
             'standing torus-fibration setting of\n'
             '\\cref{def:II:standing-torus-fibration} with nonzero ambient Hessian,\n'
             'holomorphic coordinates',
             ['D04','D05','D08'],'Resolve the former Part4.2 domain by P204; preserve every local hypothesis and conclusion.')
        edit(r'We exclude $r\ge2$ by an actual deformation of these factors.',
             r'We exclude $r\ge2$ by a deformation of these factors.',['D08'],
             'Keep the same exact factor deformation and local-degree construction.')
        edit('unit. Taking an actual local $m_i$th root of their unit',
             'unit. Taking a local $m_i$th root of their unit',['D08'],
             'Preserve the same holomorphic unit-root coordinate map.')
        edit('used in P4.28 therefore identifies the needed nearby\nlevels and transports the spherical class into the actual\nnearby torus.',
             'used in \\cref{night:P4.28} therefore identifies the needed nearby\n'
             'levels and transports the spherical class into the\nnearby torus.',
             ['D04','D08'],'Resolve the exact boundary-transport dependency and preserve its levels and spherical-class map.')
        old=r'''\item The Hessian identity is executed symbolically for the
arbitrary positive integer $m$ in
\texttt{code/part4/hessian\_product.py}. Its retained
output also checks the moving-node example
$X^2+(YZ-\varepsilon)^m$ at a nonzero critical value.'''
        replacement=r'''\item The Hessian identity holds for every positive integer $m$.
For the moving-node example
$X^2+(YZ-\varepsilon)^m$, the origin is a critical point
with value $(-\varepsilon)^m$ when $\varepsilon\ne0$.
The Hessian of $YZ-\varepsilon$ is
$\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)$.
Substituting it into the preceding formula gives the
full Hessian determinant $-2m^2\varepsilon^{2m-2}\ne0$.'''
        edit(old,replacement,['D09','D08'],
             'Move the program path and output report to Programs/check records; retain the arbitrary-positive-integer identity and moving-node calculation as explicit mathematics.',
             'The family X^2+(YZ-epsilon)^m is unchanged. Its value, two-by-two Hessian and full determinant are the values already checked by the named historical source, now printed and verified again by the Taylor-jet calculation.')

    # Exact inverse guards, applied in reverse order, restore every byte.
    inverse=[]
    check=new
    for row in reversed(rows):
        assert check.count(row['new'])==1,(tag,'inverse ambiguity',row['id'])
        inverse.append({'id':row['id']+'-inverse','owner':owner,'old':row['new'],
                        'new':row['old'],'expected_count':1})
        check=check.replace(row['new'],row['old'])
    assert check==before
    old_displays=re.findall(r'\\\[(.*?)\\\]',before,re.S)
    new_displays=re.findall(r'\\\[(.*?)\\\]',new,re.S)
    norm=lambda x:re.sub(r'\s+','',x)
    assert all(norm(x) in [norm(y) for y in new_displays] for x in old_displays)
    labels=re.findall(r'\\label\{([^}]+)\}',before)
    assert all(x in re.findall(r'\\label\{([^}]+)\}',new) for x in labels)
    assert re.findall(r'\\tag\{([^}]+)\}',before)==re.findall(r'\\tag\{([^}]+)\}',new)
    assert re.findall(r'\\hypertarget\{([^}]+)\}',before)==re.findall(r'\\hypertarget\{([^}]+)\}',new)
    before_items=len(re.findall(r'\\item\b',before));after_items=len(re.findall(r'\\item\b',new));assert before_items==after_items
    # Inline values in the examples are retained literally as well.
    old_inline=re.findall(r'(?<!\\)\$(.*?)(?<!\\)\$',before,re.S)
    new_inline=re.findall(r'(?<!\\)\$(.*?)(?<!\\)\$',new,re.S)
    excluded=[x for x in old_inline if x==r'\langle1\rangle']
    missing=[x for x in old_inline if x not in new_inline and x not in excluded]
    assert not missing,(tag,missing)
    for row in rows:
        row['source_snapshot_sha256']=hashlib.sha256(source.encode()).hexdigest()
        assert before.count(row['old'])==1,(tag,'original span not unique',row['id'])
        offset=source.index(before)+before.index(row['old'])
        row['source_character_span']=[offset,offset+len(row['old'])]
        row['source_byte_span']=[len(source[:offset].encode()),len(source[:offset+len(row['old'])].encode())]
        row['source_line_span']=[source.count('\n',0,offset)+1,
                                 source.count('\n',0,offset+len(row['old']))+1]
    after=d/f'S6_SERIES_PUBLISH_II_A2_{tag}_after.tex';after.write_text(new)
    (d/f'S6_SERIES_PUBLISH_II_A2_{tag}_exact.diff').write_text(''.join(difflib.unified_diff(
        before.splitlines(True),new.splitlines(True),fromfile=tag+' before',tofile=tag+' after')))
    (d/f'S6_SERIES_PUBLISH_II_A2_{tag}_inverse_guards.json').write_text(json.dumps(inverse,indent=2)+'\n')
    bound.append({'owner':owner,'tag':tag,'before_sha256':hashlib.sha256(before.encode()).hexdigest(),
       'after_sha256':hashlib.sha256(new.encode()).hexdigest(),'proof_items_preserved':before_items,
       'old_displays_preserved':len(old_displays),'new_displays':len(new_displays),
       'all_original_inline_math_preserved':True,'guards':len(rows),
       'labels':labels,'equation_tags_preserved':re.findall(r'\\tag\{([^}]+)\}',before)})
    all_rows.extend(rows)

(d/'S6_SERIES_PUBLISH_II_A2_D09_D04_batch01_guards.json').write_text(json.dumps(all_rows,indent=2)+'\n')
(d/'S6_SERIES_PUBLISH_II_A2_D09_D04_batch01_preservation.json').write_text(json.dumps(
    {'source_sha256':hashlib.sha256(source.encode()).hexdigest(),'owners':bound,
     'canonical_writes':0,'D19_scope':'All original equation tags and their raw references are left for the parent D19 pass.'},indent=2)+'\n')
with (d/'S6_SERIES_PUBLISH_II_A2_D09_D04_batch01_defects.tsv').open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=['id','owner','tag','source_line_span','source_byte_span','defect_ids','reason','mathematical_disposition','old','new'],delimiter='\t')
    writer.writeheader()
    for row in all_rows:
        writer.writerow({k:(';'.join(row[k]) if k=='defect_ids' else row[k]) for k in writer.fieldnames})

prefix='https://raw.githubusercontent.com/KokunoYumeto/s6-complex-structure-workbench/83d76022bc/pro_returns/S6_06_BLIND_checkpoint_15_20261117T1457Z/S6_06_BLIND/code/part4/'
rows=[]
for desc,owner,name in [
 ('Tacnodal conormal inequalities and local Hessians','night:P4R.10','tacnode_hessian.py'),
 ('Polar Hessians, exact six-point equations and scaling','night:P4R.14','smooth_a3_polar.py'),
 ('Product Hessians and the moving-node family','night:P4R.15','hessian_product.py')]:
    rows.append(desc+r' (\cref{'+owner+r'}) & \href{'+prefix+name+r'}{\nolinkurl{'+name+r'}} \\[3pt]')
(d/'S6_SERIES_PUBLISH_II_A2_D09_D04_batch01_Programs_rows.tex').write_text('\n'.join(rows)+'\n')
print(json.dumps({'source_snapshot_sha256':hashlib.sha256(source.encode()).hexdigest(),
                  'guards':len(all_rows),'owners':bound,'canonical_writes':0},indent=2))
