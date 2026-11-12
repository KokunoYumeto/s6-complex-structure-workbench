import pathlib
import re
import subprocess

ROOT = pathlib.Path(__file__).resolve().parent
p = ROOT/'MATHEMATICAL_NOTE.md'
appendix = ROOT/'TOMOGRAPHY_DESIGN.md'
text = p.read_text(encoding='utf-8')
if '\\(J=' not in text:
    # Restore the intended inline math delimiters after transport escaping.
    out = []
    in_display = False
    for line in text.splitlines(keepends=True):
        if line.strip() == r'\[':
            in_display = True
        if in_display:
            out.append(line)
            if line.strip() == r'\]':
                in_display = False
            continue
        protected = {}
        def protect(m):
            key = f'PROTECTEDTOKEN{len(protected)}'
            protected[key] = m.group()
            return key
        tick = chr(96)
        line = re.sub(r'\[[^\]]+\]\(https?://[^)]+\)|'+tick+'[^'+tick+']+'+tick,protect,line)
        line = line.replace(r'\)',')')
        result = []
        i = 0
        while i < len(line):
            if line[i] != '(':
                result.append(line[i]);i += 1;continue
            start = i
            depth = 1
            i += 1
            while i < len(line) and depth:
                if line[i] == '(':depth += 1
                elif line[i] == ')':depth -= 1
                i += 1
            if depth:
                raise RuntimeError('Unbalanced prose math at '+line)
            result.append(r'\('+line[start+1:i-1]+r'\)')
        line = ''.join(result)
        for key,value in protected.items():
            line = line.replace(key,value)
        out.append(line)
    text = ''.join(out)
    old = 'where \\(\\sigma_j\\) are the usual displayed Pauli matrices,'
    new = ('where\n\n\\[\n'
           '\\sigma_1=\\begin{pmatrix}0&1\\\\1&0\\end{pmatrix},\\quad\n'
           '\\sigma_2=\\begin{pmatrix}0&-i\\\\i&0\\end{pmatrix},\\quad\n'
           '\\sigma_3=\\begin{pmatrix}1&0\\\\0&-1\\end{pmatrix}.\n'
           '\\]\n\n')
    assert old in text
    text = text.replace(old,new)
    text = text.replace('\n\n and take the four','\n\nTake the four')
    p.write_text(text,encoding='utf-8')

subprocess.run(['pandoc',str(p),str(appendix),'-f','markdown+tex_math_single_backslash',
                '-t','latex','--standalone','--pdf-engine=xelatex',
                '-V','documentclass=article','-V','geometry:margin=24mm',
                '-V','fontsize=11pt','-o',str(ROOT/'CONSOLIDATION.tex')],
               check=True,capture_output=True,text=True,encoding='utf-8')
tex_path = ROOT/'CONSOLIDATION.tex'
tex = tex_path.read_text(encoding='utf-8')
tex = tex.replace(r'\usepackage{amsmath,amssymb}',r'\usepackage{amsmath,amssymb,mathrsfs}')
tex = tex.replace('∎',r'\ensuremath{\square}')
tex_path.write_text(tex,encoding='utf-8')
assert r'\operatorname{Herm}' in tex and r'\mathscr L' in tex
assert tex.count(r'\begin{document}') == 1 and tex.count(r'\end{document}') == 1
print('Complete mathematical note converted to standalone TeX.')
