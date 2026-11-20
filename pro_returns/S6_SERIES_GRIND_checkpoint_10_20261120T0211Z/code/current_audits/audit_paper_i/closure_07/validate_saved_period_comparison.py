"""Validate the published bounds and complete rational path receipts.

This independently reads saved balls and rational path data.  It does not
repeat the Taylor propagation and does not replace that computation.
"""
from pathlib import Path
from fractions import Fraction as F
import json, sys, os, hashlib
HERE=Path(__file__).resolve().parent
sys.path.insert(0,os.environ.get('S6_P116_VENDOR',str(HERE.parent/'vendor')))
from flint import arb, ctx
ctx.dps=160
p=HERE/'period_loop_comparison.output.json'
d=json.loads(p.read_text()); checks=[]
def ck(name,predicate):
    assert predicate,name
    checks.append(name)
def r(x):
    x=F(x);return arb(x.numerator)/x.denominator
norms=[]
for key in ['residue_zero','residue_star']:
    norms.append(max(sum(abs(F(x))for x in row)for row in d[key]))
ck('exact two residue norms',norms==[F(3125,256),F(14575,768)])
a=F(256,3125)
paths={'positive-zero-meridian':d['vertices_zero'],'positive-infinity-meridian':d['vertices_infinity'],'positive-one-to-two':[['1','0'],['2','0']]}
counts={key:0 for key in paths}; maxn=0
for tag,vertices in paths.items():
    vertices=[tuple(map(F,z))for z in vertices]
    current=vertices[0]
    selected=[s for s in d['step_receipts']if s['tag'].startswith(tag+'/')]
    for s in selected:
        z=tuple(map(F,s['z']));h=tuple(map(F,s['h']));R=F(s['R']);N=s['N']
        edge=int(s['tag'].split('/')[1]);goal=vertices[edge+1]
        ck(f'{s["tag"]}: connected rational center',z==current)
        d0=max(abs(z[0]),abs(z[1]));ds=max(abs(z[0]+a),abs(z[1]))
        ck(f'{s["tag"]}: exact radius',R==min(d0,ds)/2 and R>0)
        length=abs(h[0])+abs(h[1]); ck(f'{s["tag"]}: step inside quarter disk',0<length<=R/4)
        delta=(goal[0]-z[0],goal[1]-z[1]); fac=next(h[i]/delta[i]for i in range(2)if delta[i])
        ck(f'{s["tag"]}: oriented segment containment',0<fac<=1 and h==(fac*delta[0],fac*delta[1]))
        M=r(norms[0]/(d0-R)+norms[1]/(ds-R));q=r(length/R)
        E=(M*r(R)).exp()*q**(N+1)/(1-q)
        ck(f'{s["tag"]}: independent Cauchy bound',E<arb('1e-100') and E.upper()<=arb(s['tail']).upper())
        current=(z[0]+h[0],z[1]+h[1]); counts[tag]+=1;maxn=max(maxn,N)
    ck(f'{tag}: exact final vertex',current==vertices[-1])
ck('complete counts and maximum order',list(counts.values())==[120,66,6] and maxn==192)
h=arb(d['h_b_one']); mid=arb('-1.03427662241632179949424884537834605259496477790218821132')
ck('stored height radius',h.rad()<arb('4e-91'))
ck('displayed wider height interval',abs(h-mid)<arb('8.11e-57'))
ck('strict lower theorem endpoint',h>arb('-1.0342766224163217994942488453783461'))
ck('strict upper theorem endpoint',h<arb('-1.0342766224163217994942488453783460'))
ck('matrix comparison at one',arb(d['matrix_difference_one_upper'])<arb('1.37e-73'))
ck('matrix comparison at two',arb(d['matrix_difference_two_upper'])<arb('4.71e-74'))
root=d['root_at_two']
ck('root at two order and radius',root['N']==880 and F(root['R'])==F(5,4))
ck('root denominator lower and norm',arb(root['denominator_lower']).contains(arb('2343.75')) and arb(root['norm_bound']).contains(arb('65.6375')))
ck('root tail',arb(root['tail'])<arb('5.39e-103'))
for j,(s,limit)in enumerate(zip(d['c10_determinants'],['4e-79','2e-80'])):
    re,im=s[:-1].rsplit(' + ',1);x,y=arb(re),arb(im)
    ck(f'determinant {j+1}: positive imaginary enclosure',x.contains(0) and y>0)
    ck(f'determinant {j+1}: total coordinate radius',x.rad()+y.rad()<arb(limit))
for name,sha in d['input_files'].items():
    p2=HERE.parent/'paper_v_review/output'/name
    ck('input exact hash '+name,hashlib.sha256(p2.read_bytes()).hexdigest()==sha)
payload={'author':'GPT-6 Astra, ChatGPT Pro mode, inherited effort; same family','phase':'S6_SERIES_GRIND','result':'PASS','checks':len(checks),'check_names':checks,'counts':counts,'max_order':maxn,'input_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'program_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Saved-ball published-bound and complete rational-step receipt validation; the loop and root Taylor propagation remains the separate primary calculation.'}
(HERE/'validate_saved_period_comparison.output.json').write_text(json.dumps(payload,indent=2)+'\n')
print(json.dumps({k:payload[k]for k in ['result','checks','counts','max_order']}))
