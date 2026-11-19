from pathlib import Path
p=Path(__file__).parents[2]/'notes/part1.tex';v=p.read_text()
v=v.replace('\\Gamma_W=\\frac1{3125\\lambda+256}\n\\begin{pmatrix}', '\\resizebox{\\textwidth}{!}{$\\displaystyle\n\\Gamma_W=\\frac1{3125\\lambda+256}\n\\begin{pmatrix}')
v=v.replace('8(625\\lambda+48)/\\lambda\n\\end{pmatrix}.\n\\tag{1.15.2}', '8(625\\lambda+48)/\\lambda\n\\end{pmatrix}.$}\n\\tag{1.15.2}')
v=v.replace('''These are numerical evaluations, not certified bounds: the current
Taylor continuation discards interval radii after each step and checks
small residuals.  A certified continuation and an independent lifted
period evaluation are being developed.  The two independent curve
period methods are already complete; they do not replace those
remaining requirements for the lifted rank-six periods.''','''The preliminary loop calculation uses midpoint recentering and residual
checks.  P1.16 supplies the rigorous interval continuation and the
independent Frobenius computation of the lifted rank-six periods;
the curve periods have the additional independent quadrature and
cosine-moment evaluations just described.''')
v=v.replace('''-1.03427662241632179949424884537834605259496477790218821133
 <h_b(1)<
-1.03427662241632179949424884537834605259496477790218821131.''','''-1.0342766224163217994942488453783461
 <h_b(1)<
-1.0342766224163217994942488453783460.''')
v=v.replace('''88279007523.2167451846066607088299709479845\\ldots,
\\qquad
3178499608.3637608517583236010752861132441\\ldots.''','''\\begin{gathered}
88279007523.2167451846066607088299709479845\\ldots,\\\\
3178499608.3637608517583236010752861132441\\ldots.
\\end{gathered}''')
p.write_text(v)
print('Wrapped connection matrix, shortened displayed interval, split determinants, removed superseded provisional prose.')
