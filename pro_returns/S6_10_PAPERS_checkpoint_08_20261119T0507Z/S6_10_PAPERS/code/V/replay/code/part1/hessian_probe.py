from certified_minimum_root import *
ev=RootEvaluator('infinity',1000)
for z in [0,.1,.25,.4,.6,.8,.3+.3j,.5+.5j]:
    z=acb(str(z.real),str(z.imag)) if isinstance(z,complex) else acb(str(z))
    val=ev.evaluate(z,True)
    print(z,{k:v.str(20) if isinstance(v,arb) else v for k,v in val.items()},flush=True)
