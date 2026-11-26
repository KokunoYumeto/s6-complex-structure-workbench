#!/usr/bin/env python3
"""Prepare one exact bounded carrier P15 wording edit; never write TeX."""
from pathlib import Path
import csv,re
ROOT=Path(__file__).resolve().parents[1]
s=(ROOT/'S6_SERIES_PUBLISH_III.tex').read_text()
old=r'''Choose its sphere maps $a,b$ for these generators and put
$\alpha=a$, $\beta=b$. Its wedge equivalence, denoted here by $G$, is'''
new=r'''Denote the lemma's sphere maps for $u$ and $v$ by
$\alpha:S^2\to\mathcal C$ and $\beta:S^3\to\mathcal C$,
respectively. Their wedge equivalence is'''
assert s.count(old)==1
candidate=s.replace(old,new,1)
assert re.findall(r'\\label\{[^}]+\}',s)==re.findall(r'\\label\{[^}]+\}',candidate)
assert re.findall(r'\\hypertarget\{[^}]+\}',s)==re.findall(r'\\hypertarget\{[^}]+\}',candidate)
row=dict(change_id='CLAUDE-III-P15-CARRIER-SPHERE-MAPS',type='D20',statement_id='wb:cusp-cone-target-homotopy-types',old_location='Paper III, tag037M; comparison with02QC',old_page='cp100 later carrier section',new_location='Paper III, tag037M; comparison with02QC',new_page='pending final build',old_text=old,new_text=new,reason='In this same proof a,b already denote the fundamental-group generators rho1,rho2. Name the supplied sphere maps directly alpha:S2->C and beta:S3->C, with images u,v. The exact old-to-new assignment is a_lemma=alpha,b_lemma=beta; its inverse restores those two lemma-local names. The wedge G, homotopy inverse L=kj_C, both based homotopies and their generator maps remain unchanged. Full037M and full cited02QC proof reread.',review_status='Bounded full-source P15 reread completed; exact replacement prepared; canonical admission and final PDF gate pending.')
fields=['change_id','type','statement_id','old_location','old_page','new_location','new_page','old_text','new_text','reason','review_status']
p=ROOT/'agents/continuation9_findings/S6_SERIES_PUBLISH_c9_carrier_notation_defects.tsv'
with p.open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerow(row)
print('One guarded carrier P15 edit prepared; labels/targets unchanged; canonical TeX untouched.')
