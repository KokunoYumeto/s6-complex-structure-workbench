from pathlib import Path
import json, hashlib
BASE=Path('/workspace/scratch/490d8ca4e928')
OUT=BASE/'work/S6_10_PAPERS/analysis/IV_K107'
changes=[]
def add(name,file,old,new,reason,scope):
    p=OUT/file; text=p.read_text()
    assert text.count(old)==1,(name,text.count(old))
    changes.append(dict(id=name,label='night:P3K.107',source_file='sources/newer_night/checkpoint29/notes/'+file,source_file_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),exact_old=old,exact_new=new,reason=reason,scope=scope))
add('K107-OG5-theta-derivative','part3_e6_order_three_m2_return_source_caps.tex',
 r'\eta=a\frac{\Theta_Q(P^2)}{\Theta_Q(P)^2},',
 r"\eta=a\,\Theta'_Q(1)\frac{\Theta_Q(P^2)}{\Theta_Q(P)^2},",
 "OG.5 identifies a as the same full differential unit as E81.6. E81.6 gives the displayed derivative factor; it is a nonconstant unit and its sixth power cannot be omitted. The later full eta identity in OG.6 and the downstream unit formulas already use E81.6.",
 "Corrects the exact source-to-Tate coefficient without changing the native exponents, characteristic pair, cap range or all-fan image.")
old='''The actual outer members are the spheres supplied by the E6
source/root/Cartier interval to the F41 reference.'''
new=r'''The reference here is the E6-B source in F41, with its actual
\((a,b)=(2,3)\) row, good root \(m=3l\), primitive cap
\(n=\pm1\), and retained finite character. To specify the
source/root/Cartier interval, write
\[
 r=(1-\rho^2)/3,\qquad
 t_c=(1-3\rho^2+2\rho^3)/27.
\]
Choose an ordered compact \(\rho\)-arc from the actual selected root
near \(+1/2\) to \(-1\), with interior avoiding
\(0,1,-1,1/2,-1/2\). Throughout it retain
\(M_2=\mathcal O([2G]-[O])\), translation by \(-3G\),
and the full selected Hom coefficient \((t-t_c)B_{2,3}/t^3\).
The source, point-line and ordinary quotient maps vary along this
arc; the compact-arc scalar bound is chosen for these full maps.
At its endpoint \(r=0\), \(t_c=-4/27\), K96, EX.1--5,
supplies the actual extension through the unselected type III
fibre and the good-root Cartier/translation maps, whose central
triple coefficient is \(4\). Applying the interval construction
of EC.25 with these explicit M2 data gives the F41 E6-B sphere
reference. The good-cap comparison OG.4 retains the same exterior
and carries this sphere and its physical action to every cap and
finite character in the stated range. Thus the actual outer
members are the standard oriented spheres of that specified
source/root/Cartier interval.'''
add('K107-MO6-explicit-M2-reference','part3_e6_order_three_m2_return_outer.tex',old,new,
 "The cited EC.25 proof illustrates an M6 reference. Its interval construction must be applied with the actual M2 point line, -3G translation and six-factor Hom map. F41 expressly includes the (2,3) E6-B good-root row, and K96 supplies its endpoint source/Cartier/cap extension.",
 "Explicates the existing M2 application and exact parameter arc; no identification with M6 is asserted and no cap domain is enlarged.")
j=dict(label='night:P3K.107',source_checkpoint=29,checker='GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro)',corrections=changes,applied_to_source=False,receiving_owner='monodromy_fourfold',proof_verdict='pending final local dependency and current finite-certificate checks')
(OUT/'receiving_replacements.json').write_text(json.dumps(j,indent=2)+'\n')
(OUT/'receiving_replacements.tex').write_text('\n\n'.join('% '+c['id']+'\n'+c['exact_new'] for c in changes)+'\n')
print(json.dumps({'path':str(OUT/'receiving_replacements.json'),'replacements':len(changes)}))
