#!/usr/bin/env python3
"""Export the complete reviewed real-trace argument, retaining all formulas."""
from pathlib import Path
import re
root=Path(__file__).resolve().parents[2]
source=(root/'notes/part3_fourfold.md').read_text()
source+='\n'+(root/'notes/part3_os45.md').read_text().replace('# P3K.10.','## P3K.10.',1)
source+='\n'+(root/'notes/part3_higher_parameter.md').read_text().replace('# P3K.11.','## P3K.11.',1)
vertical=(root/'notes/part3_vertical_scope.md').read_text()
vertical=vertical[vertical.index('## P3K.12.'):]
source+='\n'+vertical
source+='\n'+(root/'notes/part3_log_caps.md').read_text().replace('# P3K.15.','## P3K.15.',1)
source+='\n'+(root/'notes/part3_seifert_scope.md').read_text().replace('# P3K.16.','## P3K.16.',1)
source+='\n'+(root/'notes/part3_flop_cobordism.md').read_text().replace('# P3K.17.','## P3K.17.',1)
caps=(root/'notes/part3_cap_restrictions.md').read_text()
source+='\n'+caps[caps.index('## P3K.18.'): ]
source+='\n'+(root/'notes/part3_whole_zero.md').read_text()
source+='\n'+(root/'notes/part3_source_reduction.md').read_text()
source+='\n'+(root/'notes/part3_primitive_sources.md').read_text()
source+='\n'+(root/'notes/part3_fixed_edge_flop.md').read_text()
parts=re.split(r'^## (P3K\.(?:[1-9]|1[0-9]|2[0-3]))\. Proved: (.+)\n',source,flags=re.M)
assert len(parts)==70
pieces=[r'\section{The local obstruction and the real trace of the actual return}'+'\n']
def markdown_table(match):
    rows=[line.strip().strip('|').split('|') for line in match.group(0).strip().splitlines()]
    rows=[row for row in rows if not all(set(c.strip()) <= set('-: ') for c in row)]
    def cell(c):
        c=c.strip()
        return r'\('+c.replace('−','-')+r'\)' if re.fullmatch('[−-][0-9]+',c) else c
    body=[' & '.join(cell(c) for c in row)+r' \\' for row in rows]
    spec='c p{0.48\\textwidth} c c c' if len(rows[0])==5 else 'c l l'
    return '\n'+r'\begin{center}\small\begin{tabular}{'+spec+r'}\hline'+'\n'+body[0]+'\n'+r'\hline'+'\n'+'\n'.join(body[1:])+'\n'+r'\hline\end{tabular}\end{center}'+'\n'

def tex(s):
    s=re.sub(r'(?m)^\|[^\n]+\|\n(?:\|[^\n]+\|\n)+',markdown_table,s)
    s=s.replace('**End of proof.**','')
    s=re.sub(r'\*\*Proof: (.*?)\.\*\*',lambda m:r'\par\medskip\noindent\textbf{'+m.group(1).capitalize()+r'.}\enspace',s)
    s=s.replace('**Proof.**','')
    s=re.sub(r'\*\*(.*?)\*\*',lambda m:r'\textbf{'+m.group(1)+'}',s)
    s=re.sub(r'`([^`]+)`',lambda m:r'\path{'+m.group(1)+'}',s)
    s=re.sub(r'^#{1,2} (.+)$',lambda m:r'\subsection{'+m.group(1)+'}',s,flags=re.M)
    return s.strip()+'\n'
for k in range(1,len(parts),3):
    ident,title,body=parts[k:k+3]
    after=''
    if ident in {'P3K.1','P3K.2','P3K.3','P3K.4'}:
        statement,proof=body.split('**Proof.**',1)
        proof,after=proof.split('**End of proof.**',1)
    elif ident=='P3K.5':
        statement=(r'The integral connecting class from the marked boundary '
            r'\(T^3\) has square zero and pairs trivially with every extension '
            r'of the page line.  In particular an odd cap correction does not '
            r'change the normal Euler square.')
        proof=body
    elif ident=='P3K.6':
        marker='**Proof: the actual orbit trivialization.**'
        statement,proof=body.split(marker,1)
        proof=marker+proof
    elif ident=='P3K.7':
        statement=(r'The real trace gives a spin bordism carrying the Euler '
            r'line from the actual covered conifold return to a normal sphere '
            r'bundle.  Its index is zero.  The original return also has index '
            r'zero, and its actual Hopf-lift gluing is the standard sphere.')
        proof=body
    elif ident=='P3K.8':
        statement=(r'The same actual return index vanishes by a second '
            r'calculation: vertical sphere quantization, an explicit marked '
            r'cap switch, and acyclicity of the elliptic Picard line.  This '
            r'calculation does not evaluate the page signature, its line '
            r'square, or its first Pontryagin number.')
        proof=body
    elif ident=='P3K.9':
        marker='**Proof: frames on the two pieces.**'
        statement,proof=body.split(marker,1)
        proof=marker+proof
    elif ident=='P3K.10':
        marker='**Proof: the source and its section.**'
        statement,proof=body.split(marker,1)
        proof=marker+proof
    elif ident=='P3K.11':
        marker='**Proof: the integral orbifold complex.**'
        statement,proof=body.split(marker,1)
        proof=marker+proof
    elif ident=='P3K.15':
        marker='**Proof: semifreeness from the actual fixed sphere.**'
        statement,proof=body.split(marker,1)
        proof,after=proof.split('**End of proof.**',1)
        proof=marker+proof
    elif ident=='P3K.16':
        marker='**Proof: construction of the map.**'
        statement,proof=body.split(marker,1)
        proof,after=proof.split('**End of proof.**',1)
        proof=marker+proof
    elif ident=='P3K.17':
        marker='**Proof: the real master space and its actual resolution maps.**'
        statement,proof=body.split(marker,1)
        proof,after=proof.split('**End of proof.**',1)
        proof=marker+proof
    elif ident=='P3K.19':
        marker='**Proof: the actual component maps and their multiplicities.**'
        statement,proof=body.split(marker,1)
        proof,after=proof.split('**End of proof.**',1)
        proof=marker+proof
    elif ident=='P3K.22':
        marker='**Proof: the source automorphisms and the line lift.**'
        statement,proof=body.split(marker,1)
        proof,after=proof.split('**End of proof.**',1)
        proof=marker+proof
    elif ident=='P3K.23':
        marker='**Proof: the actual two local products and the parameter clutch.**'
        statement,proof=body.split(marker,1)
        proof,after=proof.split('**End of proof.**',1)
        proof=marker+proof
    elif ident in {'P3K.20','P3K.21'}:
        marker={'P3K.20':'**Proof: the actual line-frame determinant.**',
                'P3K.21':'**Proof: the marked quadratic root.**'}[ident]
        statement,proof=body.split(marker,1)
        proof,after=proof.split('**End of proof.**',1)
        proof=marker+proof
    else:
        statement,proof=body.split('**Proof.**',1)
        proof,after=proof.split('**End of proof.**',1)
    pieces.append('\\begin{statement}{'+ident+'}{Proved}\n'+tex(statement)+'\\end{statement}\n')
    pieces.append('\\begin{proof}\n'+tex(proof)+'\\end{proof}\n')
    if after.strip():
        pieces.append(tex(after))
(root/'notes/part3_fourfold.tex').write_text('\n'.join(pieces))
print('Exported P3K.1--23 in full to notes/part3_fourfold.tex')
