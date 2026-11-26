#!/usr/bin/env python3
"""Assemble the local LQ receiver (corrected display parser); never touch canonical or global files."""
from hashlib import sha256
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
LANE = ROOT/'agents/continuation7_iii_star_logs_receiving'
P = 'S6_SERIES_PUBLISH_III_02LQ_'

def env(s, name):
    a = s.index('\\begin{'+name+'}')
    z = s.index('\\end{'+name+'}', a)+len('\\end{'+name+'}')
    return s[a:z]

def change(s, old, new):
    assert s.count(old) == 1, (old, s.count(old))
    return s.replace(old,new)

statement = env((LANE/(P+'released_statement.tex')).read_text(),'theorem')
original_statement = statement
original_proof = env((LANE/(P+'released_proof.tex')).read_text(),'proof')
statement = re.sub(r'^\\StatementRecord.*$',r'\\textnormal{\\small tag 02LQ.}',statement,flags=re.M)
statement = change(statement,'There are twelve actual marked star positions of this type','There are twelve marked star positions of this type')
statement = change(statement,'positions. Their unimodular bases are retained in the\ncertificate below. The theorem also applies to any further\ninput for which the displayed integral marked basis is supplied.',
    'positions. Their unimodular bases are given in the proof.\nThe conclusions hold for every marked boundary with the displayed basis.')
statement = change(statement,'retained in the peripheral marking.','part of the peripheral marking.')
statement = change(statement,'Every $j,r$ and every such $N$ is realized by an actual free\naffine root action. All its holomorphic unit factors and\ninteger affine twists are retained.',
    'Every $j,r$ and every such $N$ is realized by a free\naffine root action. Its maps include the holomorphic unit factors\nand integer affine twists.')
statement = change(statement,'Let $D,L$ be its literal fixed-normal tori in the\n$\\delta,\\ell$ directions.',
    'Let $D,L$ be the fixed normal tori defined by the marked origin\nsection in the $\\delta,\\ell$ directions.')
statement = change(statement,'These are unsaturated marked kernels where appropriate.\nTheir projected indices in the full fixed lattice are\nrespectively $k,k/2,2k$. The boundary cokernel is free of\nrank $\\rho-1$. In particular the last row retains the\nactual cap $\\mathbb Z/2$ and its nonzero fibre correction;\nit is not a conclusion from rational ranks or determinant\norders alone.',
    'These equations specify integral sublattices with projected indices\n$k,k/2,2k$ in the full fixed lattice. The boundary cokernel is free\nof rank $\\rho-1$. The last row includes the cap summand\n$\\mathbb Z/2$ and the nonzero torsion coordinates of both fibre images.')
statement = change(statement,'These columns can be inserted directly into the integral\nbar algorithm of', 'These columns enter the integral\nbar presentation of')
statement = change(statement,'contributes the actual regular-fibre representative of', 'contributes the regular-fibre representative of')
statement = change(statement,'the Euler number. Thus all other already proved cap\nchoices and full finite Thom columns can be retained.',
    'the Euler number. The same presentation includes the other cap\nchoices and their full finite Thom columns.')
statement = change(statement,'These are nonminimal star-log outputs, and no smooth\nclassification is inferred from their homology.','')
display_blocks = re.compile(r'\\\[(.*?)\\\]',re.S)
tail = re.compile(r'\\tag\{D\.SL(\d+)\}(\\hypertarget\{tag-[^}]+\}\{\}\\label\{maps:eq:D\.SL\d+\})\s*$')
converted = []
def equation(m):
    label = tail.search(m[1])
    if label is None:
        return m[0]
    converted.append(int(label[1]))
    return '\\begin{equation}'+label[2]+'\n'+m[1][:label.start()].strip()+'\n\\end{equation}'
statement = display_blocks.sub(equation,statement)
assert converted == list(range(1,10))

proof = env((LANE/(P+'receiving_proof_part.tex')).read_text(),'proof')
proof = change(proof,'The second is a section; their other composite differs from the\nidentity by $(ub-vc)(-2R,N,-2k)$, the exact primitive kernel.',
    'The second is a section. The identity minus its composite with\nthe first map is $(ub-vc)(-2R,N,-2k)$, the exact primitive kernel.')
start = proof.index('There is also a direct independent Wang calculation.')
end = proof.index('\\emph{The fibre and the complete torsion marking.}',start)
proof = proof[:start]+proof[end:]
proof = proof.replace('actual marked','marked').replace('actual component','component')
proof = proof.replace('actual periods','periods').replace('actual period','period')
proof = proof.replace('actual free-cover','free-cover').replace('actual gluing','gluing')
proof = proof.replace('actual fixed edges','fixed edges').replace('actual torus','torus')
proof = proof.replace('actual two-sector','two-sector').replace('actual cap','cap')
proof = proof.replace('actual-centre','chosen-centre').replace('actual vanishing','vanishing')
proof = proof.replace('actual gamma','gamma').replace('actual star','star')
proof = proof.replace('actual return','return').replace('actual cut-tree','cut-tree')
proof = proof.replace('an actual minimal filling','a minimal filling')
proof = proof.replace('already proved cap','cap')
proof = proof.replace('An actual period construction','A period construction')
proof = proof.replace('Here is an actual period construction','Here is a period construction')
proof = proof.replace('the actual word','the word').replace('the actual sphere','the sphere')
proof = proof.replace('retaining the analytic units','with the analytic units')
proof = proof.replace('retains\nevery unit and the integer lift $j$','includes\nevery unit and the integer lift $j$')
proof = proof.replace('The integer winding is retained in $j,r,N$ before applying this','The integer winding is encoded in $j,r,N$ before applying this')
proof = proof.replace('retaining integer winding','fixing integer winding')
proof = proof.replace('its retained real lift','its real lift')
proof = proof.replace('This retains the distinct branches','This distinguishes the branches')
proof = proof.replace('For clarity, retain also the reduced-component marking.','In the reduced-component marking,')
proof = proof.replace('This retains the literal correction for every positive or','These formulas give the correction for every positive or')
proof = proof.replace('can be retained in the same chain group.','belong to the same chain group.')
proof = proof.replace('Poincare--Lefschetz','Poincaré--Lefschetz')

proof = proof.replace('Here is an period construction','Here is a period construction')
proof = proof.replace('In the reduced-component marking,\nWrite','In the reduced-component marking,\nwrite')
proof = proof.replace('For the admitted minimal natural exterior','For the minimal natural exterior')
proof = proof.replace('use the actual $n\\alpha\\lambda$','use the $n\\alpha\\lambda$')
proof = proof.replace('The twelve marked inputs.','The twelve marked boundaries.')

# Put each permanent equation identity on its numbered environment header.
display = re.compile(r'\\begin\{equation\}\s*(.*?)\s*(\\hypertarget\{tag-[^}]+\}\{\}\\label\{maps:eq:D\.SL\d+\})\s*\\end\{equation\}',re.S)
proof,n = display.subn(lambda m:'\\begin{equation}'+m[2]+'\n'+m[1].strip()+'\n\\end{equation}',proof)
assert n == 15
receiver = statement+'\n\n'+proof+'\n'
for name in ('theorem','proof'):
    assert receiver.count('\\begin{'+name+'}') == receiver.count('\\end{'+name+'}') == 1
for pattern in (r'\\label\{([^}]+)\}',r'\\hypertarget\{([^}]+)\}'):
    assert re.findall(pattern,receiver) == re.findall(pattern,original_statement+original_proof)
stack=[]
for token in re.finditer(r'\\begin\{([^}]+)\}|\\end\{([^}]+)\}|\\\[|\\\]',receiver):
    if token[1]:
        if token[1]=='equation':
            assert 'equation' not in stack and '[' not in stack
        stack.append(token[1])
    elif token[2]:
        assert stack.pop()==token[2]
    elif token[0]==r'\[':
        assert 'equation' not in stack and '[' not in stack
        stack.append('[')
    else:
        assert stack.pop()=='['
assert not stack
assert receiver.count('\\begin{equation}') == receiver.count('\\end{equation}') == 24
assert r'\tag{' not in receiver and r'\StatementRecord' not in receiver
assert all(ord(c)>=32 or c in '\n\t' for c in receiver)
assert not re.search(r'\.py|\.json|SHA256|code/',receiver)
for filename,body in (('receiving.tex',receiver),('receiving_statement.tex',statement+'\n'),('receiving_proof.tex',proof+'\n')):
    path=LANE/(P+filename)
    prior = {'receiving.tex':'3722510d7cccc0d15d347f016f84f19276518dde4a367c52cbe092430fe0ec8c','receiving_statement.tex':'43ffa176216627c57503cf5c84feeab0761e43999c7b997118876b28a4d9bc64','receiving_proof.tex':'04a910d2ecdaf508374abdb91bd495b787977489c115e8236cb1f7f5991c226c'}
    assert sha256(path.read_bytes()).hexdigest()==prior[filename]
    path.write_text(body)
    print('WRITTEN',filename,'lines',len(body.splitlines()),'sha256',sha256(body.encode()).hexdigest())
print('PASS one theorem, one proof, 24 automatic equations, all 25 identities and LF/control-byte guards')
print('PASS no canonical or global file is written')
