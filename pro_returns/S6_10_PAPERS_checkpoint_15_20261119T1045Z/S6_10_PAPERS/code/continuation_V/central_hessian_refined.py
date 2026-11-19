#!/usr/bin/env python3
"""Fresh subdivided Hessian enclosures, compared with printed broad bounds."""
from pathlib import Path
import json
import minimum_root_regions as rr
from flint import acb,arb
chart=rr.Chart('infinity')
def hessian(box):
 x0,x1,y0,y1=map(arb,box);z=acb(arb((x0+x1)/2,(x1-x0)/2),arb((y0+y1)/2,(y1-y0)/2));Y=chart.box(box);G,Gp=chart.connection(z);Yp=Y*G;Ypp=Y*(G*G+Gp);M,b,c,d=rr.equations(Y);Mi=M.inv();v=Mi*b;parts={key:rr.equations(V) for key,V in [('x',Yp),('y',Yp*acb(0,1)),('xx',Ypp),('xy',Ypp*acb(0,1)),('yy',-Ypp)]};dv={t:Mi*(parts[t][1]-parts[t][0]*v) for t in ['x','y']};out={}
 for ts,t,s in [('xx','x','x'),('xy','x','y'),('yy','y','y')]:
  Mt,bt,ct,dt=parts[t];Ms,bs,cs,ds=parts[s];Mts,bts,cts,dts=parts[ts];ddv=Mi*(bts-Mts*v-Mt*dv[s]-Ms*dv[t]);out[ts]=arb(96)/(625*arb.pi())*((cts*v+ct*dv[s]+cs*dv[t]+c*ddv)[0,0].real-dts)
 out['determinant']=out['xx']*out['yy']-out['xy']**2;return out
values=[]
for i in range(4):
 for j in range(4):
  b=[str(-arb('.1')+arb(i)/20),str(-arb('.1')+arb(i+1)/20),str(-arb('.1')+arb(j)/20),str(-arb('.1')+arb(j+1)/20)];h=hessian(b);values.append({'box':b,'hessian':h})
bounds={}
for k in ['xx','xy','yy','determinant']:
 lo=min([r['hessian'][k].lower() for r in values],key=float);hi=max([r['hessian'][k].upper() for r in values],key=float);bounds[k]={'lower':str(lo),'upper':str(hi)}
old=json.loads(Path('/workspace/scratch/ae06852560d6/materials/S6_10_PAPERS_2_night_run/night_run/code/part1/minimum_certificate_summary.json').read_text());contained={k:bool(arb(bounds[k]['lower'])>arb(old['hessian'][k]['lower']) and arb(bounds[k]['upper'])<arb(old['hessian'][k]['upper'])) for k in bounds}
assert all(contained.values())
out={'status':'PASS','method':'Sixteen fresh implicit-derivative ball squares, independently enclosing the entire central square','bounds':bounds,'within_all_printed_Hessian_bounds':contained,'boxes':[{'box':r['box'],'hessian':{k:str(v) for k,v in r['hessian'].items()}} for r in values]};Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='boxes'},indent=2))
