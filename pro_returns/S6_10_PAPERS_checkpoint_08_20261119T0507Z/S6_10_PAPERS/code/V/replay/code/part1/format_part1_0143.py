from pathlib import Path
p=Path(__file__).parents[2]/'notes/part1.tex';v=p.read_text()
v=v.replace('''-1.0342766224163217994942488453783461
 <h_b(1)<
-1.0342766224163217994942488453783460.''','''\\begin{aligned}
-1.0342766224163217994942488453783461&<h_b(1),\\\\
h_b(1)&<-1.0342766224163217994942488453783460.
\\end{aligned}''')
v=v.replace('''The corresponding enclosure at zero is centered at
$-0.9317933763565235054307951057960111149908282005165194125$
with radius $7.91\\cdot10^{-56}$.''','''The corresponding enclosure at zero has center
\\[
-0.9317933763565235054307951057960111149908282005165194125
\\]
and radius $7.91\\cdot10^{-56}$.''')
v=v.replace('''We keep these evaluations separate from the still-unproved assertion
that the first is the global minimum.''','''P1.18 proves, by a complete interval covering argument, that the
first value is the unique global minimum.''')
v=v.replace('''This proves all claimed integral homology groups without setting the
unknown higher-degree cusp suspension to zero.''','''This proves all claimed integral homology groups without making an
assumption about the higher-degree cusp suspension chain term.''')
v=v.replace('''The request in item 1.3 for a second, independent full global cell
computation remains outstanding; the proof above is the completed
integral Mayer--Vietoris computation in the degrees that determine
the homology, followed by duality.''','''P1.19 supplies the requested independent full global cell computation.
It proves that the local secondary cusp term is nonzero, gives the
explicit integral reduction to the corrected global matrix, and
recovers every homology group without global Poincar\\'e duality.''')
v=v.replace('''coefficients in $v$.  Since $v\\geq0$, the determinant is positive''','''coefficients in $v$; their certified lower bounds, in increasing
order, are $0.8111$, $3.6097$, $3.5346$, and $1$.
The sharp endpoints are in \\texttt{cusp\\_cubic\\_bounds.json}.
Since $v\\geq0$, the determinant is positive''')
p.write_text(v)
print('Resolved requested overflows and superseded provisional statements; P1.18 and P1.19 remain complete.')
