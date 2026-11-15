"""Exact assembly and orbit-mass check for the global plane classification."""
from B_global_lattice import *
from collections import Counter
CO0=8315553613086720000;TOTAL=61549107892647466000
A2=json.loads((REC/'B_A2_plane_orbits.json').read_text());F2={(x['stratum'],x['orbit_id']):x for x in json.loads((REC/'B_A2_flags.json').read_text())}
A1=json.loads((REC/'B_A1_plane_orbits.json').read_text());F1={(x['stratum'],x['orbit_id']):x for x in json.loads((REC/'B_A1_flags.json').read_text())}
rows=[]
for typ,groups,flags,H,mark in [('A2',A2['plane_orbits'],F2,277136640,'12A2'),('A1',A1['A1_only_plane_orbits'],F1,489646080,'24A1')]:
 for gr in groups:
  k=tuple(gr['representative']);r=flags[k];t=r['opposite'].count(mark);S=sum(flags[tuple(x)]['flag_orbit_size'] for x in gr['flags']);assert H*t%S==0;stab=H*t//S;assert CO0%stab==0;orb=CO0//stab
  for x in gr['flags']:assert flags[tuple(x)]['extensions']==r['extensions'] and sorted(flags[tuple(x)]['opposite'])==sorted(r['opposite'])
  rows.append({'type':typ,'representative':k,'stabilizer_order':stab,'plane_orbit_size':orb,'extensions':r['extensions'],'opposite':r['opposite'],'flag_orbits':gr['flags']})
S=sum(r['plane_orbit_size'] for r in rows);print('rooted-neighbour plane orbits',len(rows),'plane count',S,'residual all-Leech planes',TOTAL-S)
print('residual mass /Co0',F(TOTAL-S,CO0))
(REC/'B_rooted_plane_orbits.json').write_text(json.dumps(rows))
import csv
with (REC/'B_rooted_plane_orbits.csv').open('w',newline='') as f:
 w=csv.writer(f);w.writerow(['orbit','mark','representative','stabilizer_order','plane_orbit_size','eight_extensions','four_opposite_extensions'])
 for i,r in enumerate(rows):w.writerow([i+1,r['type'],r['representative'],r['stabilizer_order'],r['plane_orbit_size'],r['extensions'],r['opposite']])
