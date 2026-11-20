#!/usr/bin/env python3
"""Fresh Arb enclosures for I A2.2; exact symbolic conclusions are in print.

The receiving proof was read first.  Two inputs are evaluated independently:
the modular q-series with an elementary uniform tail bound, and Arb's gamma
function expression.  No historical numerical program is imported.
"""
from pathlib import Path
import hashlib
import json
import os
import platform
import sys
import time

HERE=Path(__file__).resolve().parent
for candidate in [os.environ.get('PAPER_I_VENDOR'),str(HERE.parent/'vendor')]:
    if candidate and Path(candidate).exists():sys.path.insert(0,candidate)
import flint
from flint import arb,ctx

ctx.dps=120
START=time.monotonic()
CHECKS=[]


def check(name,test):
    CHECKS.append({'name':name,'pass':bool(test)})
    if not test:raise AssertionError(name)


def sigma(n,k):
    return sum(d**k for d in range(1,n+1) if n%d==0)


def rounded_overlap(value,printed):
    digits=len(printed.partition('.')[2])
    return value.overlaps(arb(printed,arb(10)**(-digits)))


N=100
pi=arb.pi()
qi=(-2*pi).exp()
rho_abs=(-pi*arb(3).sqrt()).exp()
check('e^-2pi < 1/500',qi<arb(1)/500)
check('e^-pi*sqrt3 < 1/200',rho_abs<arb(1)/200)
tail4=arb(250)*(N+1)**4/arb(500)**(N+1)
tail6=arb(1024)*(N+1)**6/arb(200)**(N+1)
E4=arb(1)+240*sum((arb(sigma(n,3))*qi**n for n in range(1,N+1)),arb(0))
E4+=arb(0,tail4.upper())
E6=arb(1)-504*sum((arb(sigma(n,5))*(-rho_abs)**n for n in range(1,N+1)),arb(0))
E6+=arb(0,tail6.upper())
check('E4(i) positive',E4>0)
check('E6(rho) positive',E6>0)
modular=(arb(2)/3).sqrt()/(pi*E4.root(4))
gamma=4*pi.sqrt()/(arb(3).root(4)**3*(arb(1)/4).gamma()**2)
check('independent modular/gamma balls overlap',modular.overlaps(gamma))
check('C4 positive',modular>0 and gamma>0)
realK=arb(9)/(8*pi*pi*E6.root(3))
imagK=arb(3).sqrt()*realK
printedC='0.2366093140807852246877051134504496062943051340858243372192243072'
printedRe='0.08010221108753827140763650309934451243'
printedIm='0.13874109940222333968402480721280640441'
check('printed C4 decimal enclosed at its displayed precision',rounded_overlap(modular,printedC))
check('printed Re(K2) decimal enclosed at its displayed precision',rounded_overlap(realK,printedRe))
check('printed Im(K2) decimal enclosed at its displayed precision',rounded_overlap(imagK,printedIm))

# Explicit strict rational intervals suitable for the text; widths 10^-16.
strict={
 'C4':['0.2366093140807852','0.2366093140807853'],
 'ReK2':['0.0801022110875382','0.0801022110875383'],
 'ImK2':['0.1387410994022233','0.1387410994022234']}
for name,value in [('C4',modular),('ReK2',realK),('ImK2',imagK)]:
    lo,hi=strict[name]
    check(name+' strict rational enclosure',value>arb(lo) and value<arb(hi))

OUT={'reviewer':'GPT-6 Astra (OpenAI), ChatGPT Pro mode, inherited effort; same model family',
 'chronology':'Fresh independent ball implementation after reading the printed proof; no historical replay',
 'python':platform.python_version(),'python_flint':flint.__version__,'decimal_working_precision':ctx.dps,
 'terms':N,'all_pass':all(x['pass'] for x in CHECKS),'check_count':len(CHECKS),'checks':CHECKS,
 'E4_i':E4.str(110),'E6_rho':E6.str(110),'C4_modular':modular.str(110),'C4_gamma':gamma.str(110),
 'ReK2':realK.str(110),'ImK2':imagK.str(110),'E4_tail_bound':tail4.str(20),'E6_tail_bound':tail6.str(20),
 'strict_rational_intervals':strict,
 'tail_argument':'sigma_k(n)<=n^(k+1); after N=100, successive majorant terms have ratio <=(102/101)^4/500<1/480 and <=(102/101)^6/200<1/180. Thus 240*480/479<250 and 504*180/179<1024, giving the printed tail bounds.',
 'elapsed_seconds':round(time.monotonic()-START,6)}
target=Path(__file__).with_suffix('.output.json')
target.write_text(json.dumps(OUT,indent=2)+'\n')
print(json.dumps({'all_pass':OUT['all_pass'],'check_count':OUT['check_count'],
 'C4':modular.str(66),'ReK2':realK.str(45),'ImK2':imagK.str(45),
 'elapsed_seconds':OUT['elapsed_seconds'],'output':str(target),
 'output_sha256':hashlib.sha256(target.read_bytes()).hexdigest()},indent=2))
