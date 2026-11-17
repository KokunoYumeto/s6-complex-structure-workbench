"""Resolve original prompt shorthand to the unique proved companion result.

Mappings were read from the actual MAPS checkpoint input table and the PUSH
prompt's R-register; they are not inferred from coincident local numbers.
"""
import re

MAPS_K={
 'K1':r'\cref{push:src:E.1.1,push:src:E.1.2}',
 'K3':r'\cref{push:src:C.1.1,push:src:C.1.2,push:src:C.2.1}',
 'K7':r'\cref{push:src:C.3.4}',
 'K8':r'\cref{push:src:C.3.5}',
 'K11':r'\cref{push:src:E.5.1,push:src:E.5.2,push:src:E.5.3}',
 'K13':r'\cref{push:src:A.1.1,push:src:A.1.2,push:src:A.2.1,push:src:A.2.2,push:src:A.4.1,push:src:A.4.2}',
 'K15':r'\cref{cdp:st:C2a,cdp:st:C2c}',
}
PUSH_R={
 'R2':r'\cref{fam:src:A.2.1,fam:src:A.3.1,fam:src:A.5.1}',
 'R5':r'\cref{fam:src:B.2.1,fam:src:B.2.2,fam:src:B.2.3,fam:src:B.3.1}',
 'R6':r'\cref{fam:src:B.4.1,fam:src:B.4.2,fam:src:C.4.1}',
 'R12':r'\cref{fam:src:E.2.2}',
}

def maps(s):
    # These two original source locators refer to PUSH, not the local MAPS
    # theorem with the same numeric suffix. Resolve before local raw_refs.
    s=re.sub(r'K13,\s*A\.2\.2',lambda m:r'\cref{push:src:A.2.2}',s)
    s=re.sub(r'K1,\s*E\.1\.2',lambda m:r'\cref{push:src:E.1.2}',s)
    s=s.replace('precise scope of K7','The sixfold congruence')
    s=re.sub(r'(?<![A-Za-z0-9_.:-])(?:K15|K13|K11|K8|K7|K3|K1)\b',lambda m:MAPS_K[m[0]],s)
    s=re.sub(r'The first isotopy assertion of Lead 8 is false for the marked\s+return of the original family\.',
        lambda m:r'The proposed isotopy over the ordinary locus from the marked return to the fibrewise scalar twist $x\mapsto\rho(-2\theta(x))x$ is false for the original family.',s)
    s=s.replace('The conditional clause of Lead 5 has an impossible premise for $d>1$;',
        'The proposed connected-sum classification under vanishing second homology has an impossible premise for $d>1$;')
    s=s.replace('in Lead 6 is not the normalization','in the proposed fibre-product model is not the normalization')
    s=s.replace('marked punctured-fibre product in Lead 6','marked punctured-fibre product specified here')
    s=s.replace('diagonal elliptic finite monodromies in Lead 7','diagonal elliptic finite monodromies of the rank-six proposal')
    s=re.sub(r';?\s*we claim no priority for integral-conjugacy\s+decidability\.', '.', s)
    s=s.replace('displayed immediately after\n$\\ell=-s_0/12+\\kappa_0(q)$ in\n\\texttt{S6\\_02\\_PUSH\\_C\\_closing\\_cocycle.tex}',
        r'with $\ell=-s_0/12+\kappa_0(q)$ in the complete companion proof')
    return s

def push(s):
    s=re.sub(r'(?<![A-Za-z0-9_.:-])(?:R12|R6|R5|R2)\b',lambda m:PUSH_R[m[0]],s)
    s=s.replace("Lead 6's formula",'The spin and spin-c characteristic formula')
    s=re.sub(r'the local\s+twist in Lead 7','the proposed local scalar twist',s)
    s=re.sub(r'This confirms the last sentence of Lead 7 without extracting a\s+spurious order-two restriction\.',
        'The antiholomorphic symmetry therefore supplies no order-two restriction.',s)
    return s
