#!/usr/bin/env python3
"""Export independently audited K20--21 and their exact construction scope."""
from pathlib import Path
from datetime import datetime, timezone
import json

root = Path(__file__).resolve().parents[2]
names = ['notes/part3_whole_zero.md', 'notes/part3_source_reduction.md',
         'code/part3_fourfold/export_trace_tex.py',
         'code/part3_fourfold/results_mapping.json']
with (root / 'records/literature_fourfold.md').open('a') as log:
    for name in names:
        log.write('\n- ' + datetime.now(timezone.utc).isoformat() +
                  ' — Opened current-team `' + name +
                  '`; reason: finalize root-audited K20–21; material: '
                  'general monomial deck shear, exact Euler and starred-cap '
                  'restrictions, and necessary source enumeration.\n')

p = root / names[0]
s = p.read_text()
start = s.index('There is also an explicit invariant unimodular height-one')
end = s.index('\nThe canonical-form normalization', start)
s = s[:start] + r'''There is also an explicit invariant unimodular height-one
choice, without a restriction to the rank-one generator
marking.  Write the actual monomial deck on valuations as
\(R(x,y)=(-x,y-jx)\), with \(j\in\mathbb Z\).
It sends the source period \(h=(2s,\alpha)\) to
\(-h\); comparison of the second coordinate gives
\[
                         j=\alpha/s.
\]
Thus the integrality of this shear follows from the
actual deck morphism.  The whole-zero identity is now
\(2\beta+cj=4e\).  For odd \(j\), the integral
shear \(y'=y-(j-1)x/2\) gives
\(R(x,y')=(-x,y'-x)\).  The positive unit-square
triangulation is invariant, since its edge vectors
\(u,v,u+v\) go to \(-(u+v),v,-u\).
For even \(j\), use \(y'=y-jx/2\).  The reflection
is then \((-x,y')\) and the periods are
\((2s,0),(-c,2e)\).  Give the square with lower-left
corner \((v,k)\) its diagonal according to the parity
\[
                       v+c\left\lfloor k/(2e)\right\rfloor.
\]
Both periods preserve this parity.  Reflection sends the
square to \((-v-1,k)\), changes the parity, and exchanges
the two diagonals.  This is the required invariant
unimodular periodic triangulation.

In the marked rank-one case the generic point \(aG\)
has root Tate lift \(Z_G^a\), hence \(\alpha=as\),
\(c=bs\), and \(j=a\).  Changing that lift by a
Tate-period power \(Q_T^k\) is the actual line-frame
map \(V\mapsto Z^kV\).  Vertical component divisors
change the graph heights periodically and do not change
the quasiperiod.  These explicit maps recover the
rank-one spelling while the preceding deck argument
proves the starred-zero bound before that specialization.
''' + s[end:]
p.write_text(s)

p = root / 'code/part3_fourfold/export_trace_tex.py'
s = p.read_text()
s = s.replace("parts=re.split(r'^## (P3K\\.(?:[1-9]|1[0-9]))\\. Proved: (.+)\\n',source,flags=re.M)",
              "source+='\\n'+(root/'notes/part3_whole_zero.md').read_text()\n"
              "source+='\\n'+(root/'notes/part3_source_reduction.md').read_text()\n"
              "parts=re.split(r'^## (P3K\\.(?:[1-9]|1[0-9]|2[01]))\\. Proved: (.+)\\n',source,flags=re.M)")
s = s.replace('assert len(parts)==58', 'assert len(parts)==64')
s = s.replace("def tex(s):\n", r'''def markdown_table(match):
    rows=[line.strip().strip('|').split('|') for line in match.group(0).strip().splitlines()]
    rows=[row for row in rows if not all(set(c.strip()) <= set('-: ') for c in row)]
    body=[' & '.join(c.strip() for c in row)+r' \\' for row in rows]
    return '\n'+r'\begin{center}\small\begin{tabular}{c l l}\hline'+'\n'+body[0]+'\n'+r'\hline'+'\n'+'\n'.join(body[1:])+'\n'+r'\hline\end{tabular}\end{center}'+'\n'

def tex(s):
    s=re.sub(r'(?m)^\|[^\n]+\|\n(?:\|[^\n]+\|\n)+',markdown_table,s)
''')
s = s.replace("    else:\n        statement,proof=body.split('**Proof.**',1)",
              "    elif ident in {'P3K.20','P3K.21'}:\n"
              "        marker={'P3K.20':'**Proof: the actual line-frame determinant.**',\n"
              "                'P3K.21':'**Proof: the marked quadratic root.**'}[ident]\n"
              "        statement,proof=body.split(marker,1)\n"
              "        proof,after=proof.split('**End of proof.**',1)\n"
              "        proof=marker+proof\n"
              "    else:\n        statement,proof=body.split('**Proof.**',1)")
s = s.replace('Exported P3K.1--19', 'Exported P3K.1--21')
p.write_text(s)

p = root / 'code/part3_fourfold/results_mapping.json'
data = json.loads(p.read_text())
data['results'] = [r for r in data['results'] if r['id'] not in {'P3K.20','P3K.21'}]
data['results'] += [
    dict(id='P3K.20', status='Proved', item_of_prompt='3.4',
         proof_file='notes/part3_whole_zero.md', latex_file='notes/part3_fourfold.tex',
         statement='In the actual published root, monomial quotient and Kulikov construction, a sphere member has exactly one simple whole I1 zero.',
         own_value='For I_N order e the period determinant is Ne and central Euler number is 2Ne; I_s* order e contributes at least 4se. The generic coefficients satisfy ab=1/h(G).',
         exact_maps=['actual line graph defect and period determinant',
                     'integral monomial deck R(h)=-h and explicit invariant fans',
                     'invariant nowhere-zero three-form through the A1 quotient resolution',
                     'direct cocharacter isomorphism for the published invariant zero twist'],
         code='code/part3_fourfold/whole_zero.py', certificate='code/part3_fourfold/whole_zero.json',
         scope='Every periodic unimodular Mumford fan; stated smooth-root monomial quotient/resolution maps and published invariant-translation zero twists.'),
    dict(id='P3K.21', status='Proved', item_of_prompt='3.4',
         proof_file='notes/part3_source_reduction.md', latex_file='notes/part3_fourfold.tex',
         statement='The starred cap is necessarily I1* with primitive root order 2, a even and b=2 mod4; the full source table reduces to 26 positive generic pairs in 16 profiles.',
         own_value={'profiles':16,'generic_pairs':26,'starred_cap':{'s':1,'m':2,'a_mod_2':0,'b_mod_4':2}},
         exact_maps=['quadratic Tate quotient and D-graph component marking',
                     'affine reflection norm with central unit sign',
                     'row50 vertical line correction O(aG-O-L0)'],
         code='code/part3_fourfold/source_reduction.py', certificate='code/part3_fourfold/source_reduction.json',
         scope='Necessary source restrictions in the established orbit/root-line cap scope; no unverified cap tuple is assigned sphere topology or a return index.')]
p.write_text(json.dumps(data, indent=2)+'\n')
print('Finalized root-audited K20–21 with the general deck shear and an explicit table exporter.')
