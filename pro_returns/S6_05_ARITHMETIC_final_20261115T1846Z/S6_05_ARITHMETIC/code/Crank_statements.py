"""Statement register, separate from the numerical rank table."""
from pathlib import Path
import csv
p=Path(__file__).resolve().parents[1]
rows=[
 ('C.6.R1','Ranks of all eleven rational CM fibres and full primitivity of nine rank-one section points','Proved by exact descent and saturation','sections/C_rank.tex C.6.R1; code/Crank_saturation.out','CM minimal models; exact two-descent; Cremona--Siksek height bound','C.6; Lead16(b)','Two rank-two cases have infinite section index; rank-one cases index1.'),
 ('C.6.R2','Analytic ranks and fifty-digit central derivative ratios with explicit truncation errors','Computed with explicit error bounds','sections/C_rank.tex C.6.R2; code/Crank_derivatives.out; code/Crank_cm_stream_163_check.out','Mellin transform; CM theta coefficients; Coates--Wiles central vanishing','C.6; Lead16(b)','Analytic ranks2 atj8000 andj−12288000;1otherwise. Large-conductor computation uses bounded memory.'),
 ('C.6.R3','Rank-one height is a positive rational multiple of Lprime/Omega; Sha is finite','Proved','sections/C_rank.tex C.6.R3','Gross--Zagier I.7.3; Kolyvagin; C.6.R1–R2','C.6; Lead16(b)','Exact rational factor unspecified. Numerical BSD quotients1 for8curves and9 for−163 are explicitly not exact Sha claims.'),
 ('C.6.T1','Order-four fibre minimal model, bad components, finite local heights and rank','Proved with exact local arithmetic','sections/C_torsion_heights.tex C.6.T1; code/Crank_torsion_final.out','Tate algorithm; division identity; two-descent','C.6; Lead16(a)','E:y²=x³−2x+1;rank0;torsionZ/4;finite_sum=log10/12.'),
 ('C.6.T2','Conjugate order-six fibres overQsqrt3: minimal models, local heights, global identity and rank1','Proved with exact number-field arithmetic','sections/C_torsion_heights.tex C.6.T2; code/Crank_torsion_descent_sage.out','Tate algorithm; division identity; deterministic two-isogeny descent','C.6; Lead16(a)','Natural fieldK=Qsqrt3;finite_weighted_sum=log11/12;torsionsection has infinite index inrank1freequotient. Rational-field rank requested literally is undefined.'),
]
with (p/'results_Crank_statements.csv').open('w') as f:
 w=csv.writer(f);w.writerow(['id','statement','status','where_proved','depends_on','item_of_the_prompt','notes']);w.writerows(rows)
print('Wrote',len(rows),'statement rows')
