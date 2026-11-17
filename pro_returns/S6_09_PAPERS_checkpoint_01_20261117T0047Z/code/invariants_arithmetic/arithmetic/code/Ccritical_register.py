from pathlib import Path
import csv
root=Path(__file__).resolve().parents[1]
rows=[
('C.8.12','For X=3W wpprime/g2, (t-1)L_t=X(X-2)/24 and F=1-X=6 pi i (wpprime/g2)(muprime-a); X extends to X(0)=1/4 and X(1)=0.','Proved','sections/C_critical.tex','C.3.1; C.3.2; C.8.11','C.8; Lead 15(c); K4','Exact radial derivative identity; sign and modular normalization checked.'),
('C.8.13','For Im(tau)>=7/5, |1-3W wpprime/g2|<17/20.','Proved','sections/C_critical.tex','C.8.12; Eichler-Zagier 1982 unnumbered theorem p399','C.8; Lead 15(c); K4','Cauchy estimate on one q-disc; all scalar constants displayed; no grid or cover.'),
('C.8.14','For 0<|(tau-i)/(tau+i)|<=2-sqrt(3), |1-3W wpprime/g2|<1, including the removable equianharmonic points.','Proved','sections/C_critical.tex','C.3.1; C.3.2; C.8.12; Eichler-Zagier 1982','C.8; Lead 15(c); K4','Exact ODE coefficient recurrences, Cauchy tails, and one positive Bernstein polynomial. Independent exact integer/rational arithmetic verifies all finite scalar inequalities.'),
('C.8.15','W=0 exactly on the i and rho modular orbits; 3W wpprime-2g2=0 exactly on the rho orbit. L decreases strictly on every ray from t=1; no other coarse critical point; every lower level is one star-shaped Jordan curve.','Proved','sections/C_critical.tex','C.3.1; C.3.2; C.8.12; C.8.13; C.8.14','C.8; Lead 15(c); K4; K5; R4','The suggested saddle in 0<t<1 does not exist. t=0 is noncritical C1 on the coarse base but a cubic degenerate critical point on its root chart; t=1 is the unique maximum, nondegenerate on its h chart.'),
]
with (root/'results_Ccritical.csv').open('w',newline='') as f:
 w=csv.writer(f);w.writerow(['id','statement','status','where_proved','depends_on','item_of_the_prompt','notes']);w.writerows(rows)
print('Wrote',len(rows),'numbered-statement rows')
