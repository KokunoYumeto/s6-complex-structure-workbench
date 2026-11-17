"""Give the four complete worked course exercises distinct printed numbers."""
import re

def number_worked_examples(text):
    pattern=r'\\textbf\{Exercise ([0-9.]+)([^}]*)\}\\label\{(mapsI:(?:cw|pf):exercise:[^}]+)\}'
    matches=list(re.finditer(pattern,text))
    for i in range(len(matches)-1,-1,-1):
        m=matches[i];stop=matches[i+1].start() if i+1<len(matches) else len(text)
        block=text[m.end():stop]
        statement,solution=block.split(r'\textbf{Solution.}',1)
        # Every byte of the mathematical statement and solution is retained.
        new='\\begin{example}[Worked Exercise '+m[1].rstrip('.')+']\n\\label{'+m[3]+'}'+statement+'\\end{example}\n\\begin{proof}[Solution]'+solution.rstrip()+'\n\\end{proof}\n\n'
        text=text[:m.start()]+new+text[stop:]
    return text
