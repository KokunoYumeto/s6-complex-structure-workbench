"""Make the reference fan explicit in the retained zero-return results."""
def prefix_reference_fan(t):
 pos=t.index('{',t.index(r'\StatementRecord'))
 for j in range(4):
  depth=1;pos+=1
  while depth:
   if t[pos]=='{' and t[pos-1]!='\\':depth+=1
   if t[pos]=='}' and t[pos-1]!='\\':depth-=1
   pos+=1
  if j<3:pos=t.index('{',pos)
 prefix=r'''

Retain the reference cusp fan fixed in the construction of this
family, with its specified lattice basis and collar maps.
'''
 return t[:pos]+prefix+t[pos:]
for label in [
 'push:src:C.3.15','push:src:C.3.24','push:src:C.3.27',
 'push:src:C.4.1','push:src:C.5.1',
 'maps:src:B.6.2','maps:src:B.6.16','maps:src:B.6.17',
 'maps:src:B.6.19','maps:src:B.6.20','maps:src:B.6.21',
 'maps:src:B.6.22','maps:src:B.6.23','maps:src:B.6.24','maps:src:B.6.25',
]:
 change(label,prefix_reference_fan,
  'Make the actual retained reference cusp fan, lattice basis and collar maps explicit. The zero-return and fixed-curve calculations have this scope; the other fan returns are computed by their separate full prism maps.')
