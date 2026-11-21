import sympy as s,pathlib,json,hashlib,datetime
z=s.symbols('z');P=11*z*z-6016*z+8192
Q=881*z**4+4745344*z**3-12079104*z*z+24641536*z-16777216
num=(89*z*z+4736*z-4096)*Q;den=1296*P**2
delta=27*z**8*(z-1)**3;psi=s.Rational(9,65536)*z**24*(z-1)**9*P
out={'finite_0':{'v_delta':8,'v_psi6':24,'x6':str(s.factor(num.subs(z,0)/den.subs(z,0))),'lambda':str(s.Rational(8,12)-s.Rational(24,36))},'finite_1':{'v_delta':3,'v_psi6':9,'x6':str(s.factor(num.subs(z,1)/den.subs(z,1))),'lambda':str(s.Rational(3,12)-s.Rational(9,36))},'infinity':{'delta_minimal':str(s.factor(z**12*delta.subs(z,1/z))),'psi6_minimal_at_0':str(s.limit(z**35*psi.subs(z,1/z),z,0)),'x6_minimal_at_0':str(s.limit(z**2*(num/den).subs(z,1/z),z,0)),'lambda':'1/12'},'normalization':'Arithmetic differential dx/(2y); (x_infinity,y_infinity)=(s^2 x,s^3 y); psi_6 weight35.','created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
p=pathlib.Path('/workspace/scratch/653608133b22/work/agents/i_provenance/S6_SERIES_PUBLISH_I_C64_valuation_check.json');p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
