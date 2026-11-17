from flint import arb
x=arb('0.3423 +/- 0.0000847');y=arb('0 +/- 0.00005')
print('x>0',x>0,'square',y**2,'mult',y*y,'detpower',x*x-y**2,'detproduct',x*x-y*y)
print('finite determinant',x*x-y*y>0)
