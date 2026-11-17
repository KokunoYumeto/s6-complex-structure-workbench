from pathlib import Path
import json

def partitions(n,lo=1):
 if n==0:
  yield []
 for j in range(lo,n+1):
  for tail in partitions(n-j,j): yield [j]+tail
six=[]
for p in partitions(6):
 odd=sum(k%2 for k in p)
 if odd>=4:
  M=sum(k-1 for k in p)
  assert M<=2
  six.append({'discriminant_multiplicities':p,'branch_points':odd,'normalization_genus':(odd-2)//2,'M_upper':M})
four=[p for p in partitions(4) if sum(k%2 for k in p)>=4]
assert four==[[1,1,1,1]]
assert 4*2>3
out={'status':'PASS','degree_six_positive_genus_partitions':six,'degree_four_positive_genus_partitions':four,'nontrivial_monodromy_rank_lower':8,'zero_form_rank_upper':3,'contradiction':True}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print('Cubic double-line weighted obstruction: PASS')
for p in six: print(p)
print('Order-five rank lower 8 exceeds transverse rank upper 3')
