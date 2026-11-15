"""Exact integral checks for A.4.8.

The theorem uses finite toroidal weak factorization, not an inference
from this bounded computation.  This program checks the normalization
maps of each reference n-cycle over Z, all stated blow-up increments,
and consistency with independently certified torus-stratum Euler counts.
"""
from pathlib import Path
import json
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

here = Path(__file__).parent
lat = json.loads((here / 'ab_push_monodromy.json').read_text())
G = s.Matrix(lat['intersection_matrix'])
F = s.Matrix(lat['F'])
m = s.Matrix(lat['m'])
T = s.Matrix(lat['T'])
n0 = m - F
I = s.eye(10)
rowF = F.T * G
rown = n0.T * G

def addblock(mat, row, col, value):
    nr, nc = value.shape
    mat[row:row+nr, col:col+nc] = mat[row:row+nr, col:col+nc] + value

def nonzero_smith(mat):
    sm = smith_normal_form(mat, domain=ZZ)
    return [abs(int(sm[j,j])) for j in range(min(sm.shape)) if sm[j,j]]

r0 = I.col_join(s.zeros(1,10)).col_join(rowF)
rinf = T.col_join(-rown).col_join(s.zeros(1,10))
e0 = I.col_join(s.zeros(1,10))
einf = I.col_join(rown)
r40 = m.col_join(s.Matrix([1,-1]))
r4inf = s.zeros(10,1).col_join(s.Matrix([1,0]))
e40 = s.zeros(10,1).col_join(s.Matrix([1]))
e4inf = n0.col_join(s.Matrix([1]))

reference = []
for degree in (1,2,3,4,6,12):
    target_rank = 11*degree+1
    d2 = s.zeros(target_rank,10*degree)
    addblock(d2,0,0,r0)
    addblock(d2,0,10*(degree-1),-rinf)
    d4 = s.zeros(target_rank,degree)
    addblock(d4,0,0,r40)
    addblock(d4,0,degree-1,-r4inf)
    d0 = s.zeros(degree,degree)
    d0[0,0] += 1
    d0[0,degree-1] -= 1
    for j in range(1,degree):
        off = 12+11*(j-1)
        addblock(d2,off,10*(j-1),-e0)
        addblock(d2,off,10*j,einf)
        addblock(d4,off,j-1,-e40)
        addblock(d4,off,j,e4inf)
        d0[j,j-1] -= 1
        d0[j,j] += 1
    sn2, sn4, sn0 = map(nonzero_smith,(d2,d4,d0))
    assert sn2 == [1]*(10*(degree-1)+3)
    assert sn4 == [1]*degree
    assert sn0 == [1]*(degree-1)
    betti = [1,1,target_rank-len(sn2),10*degree-len(sn2),
             target_rank-len(sn4),degree-len(sn4),degree]
    expected = [1,1,degree+8,7,10*degree+1,0,degree]
    assert betti == expected
    euler = sum((-1)**i*b for i,b in enumerate(betti))
    assert euler == 26+24*(degree-1)-12*degree == 12*degree+2
    reference.append(dict(n=degree,betti=betti,central_Euler=euler,
                          d2_shape=list(d2.shape),d2_nonzero_smith=sn2,
                          d4_shape=list(d4.shape),d4_nonzero_smith=sn4,
                          d0_nonzero_smith=sn0))
    print('REFERENCE',degree,'BETTI',betti,'ALL NONZERO SMITH FACTORS 1')

blowups = []
centre_data = [('point',0,[1],True),
               ('compact_curve',1,[1,0,1],True),
               ('horizontal_curve',1,[1],False)]
for h in (1,2,3,10,12):
    centre_data += [('compact_surface_b2_'+str(h),2,[1,0,h,0,1],True),
                    ('horizontal_surface_b2_'+str(h),2,[1,0,h],False)]
for tag,dim,b,compact in centre_data:
    delta = [0]*9
    for a in range(1,4-dim):
        for j,h in enumerate(b):
            delta[j+2*a] += h
    assert delta[2] == 1
    assert delta[6] == int(compact)
    assert all(delta[j] == 0 for j in (1,3,5,7))
    assert delta[0] == delta[8] == 0
    blowups.append(dict(centre=tag,complex_dimension=dim,compact=compact,
                        centre_betti=b,ambient_betti_increment=delta))
    print('BLOWUP',tag,'DELTA',delta)

fans = json.loads((here / 'ab_push_all_fan_topology.json').read_text())
checked_fans = []
for rec in fans:
    k,t4 = rec['pure_top_orbits'],rec['maximal_cones']
    mixed = int(rec['tag'].replace('point_stars','')) if rec['tag'].startswith('point_stars') else 0
    betti = [1,1,8+k+mixed,7,9*k+t4-2*mixed-1,0,k+mixed]
    assert all(b>=0 for b in betti)
    assert sum((-1)**i*b for i,b in enumerate(betti)) == rec['central_Euler']
    if rec['tag'].startswith('bridge'):
        n = rec['n']
        assert betti == [1,1,n+8,7,10*n+1,0,n]
    elif rec['tag'].startswith('point_stars'):
        assert betti == [1,1,9+mixed,7,11+mixed,0,1+mixed]
    elif rec['tag'].startswith('nonreduced_conductor_stars'):
        steps = int(rec['tag'].replace('nonreduced_conductor_stars',''))
        assert betti == [1,1,9+steps,7,11+10*steps,0,1+steps]
    checked_fans.append(dict(tag=rec['tag'],n=rec['n'],k=k,mixed=mixed,t4=t4,betti=betti))

output = dict(reference_cycles=reference,blowup_centres=blowups,
              certified_fan_checks=checked_fans,
              status='PASS',formula='(1,1,8+k+m,7,9k+t4-2m-1,0,k+m)')
Path(__file__).with_suffix('.json').write_text(json.dumps(output,indent=2)+'\n')
print('ALL CHECKS PASS:',len(reference),'REFERENCE CYCLES;',len(blowups),
      'CENTRE CASES;',len(checked_fans),'FAN CASES')
