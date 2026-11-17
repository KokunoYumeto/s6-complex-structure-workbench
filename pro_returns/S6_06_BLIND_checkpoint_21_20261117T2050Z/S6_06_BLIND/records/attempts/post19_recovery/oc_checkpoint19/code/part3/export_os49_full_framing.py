#!/usr/bin/env python3
"""Export the independently audited component-supported OS49 proof."""
from pathlib import Path
from datetime import datetime, timezone
import json
import re
import subprocess

root=Path(__file__).resolve().parents[2]
source=root/'notes/part3_os49_full_framing_working.md'
text=source.read_text()
assert 'Root independently passed the complete proof' in text
body=text[text.index('## 1.'):]

exact={
 'lambda=r^(3k)':r'\lambda=r^{3k}',
 'n(1,-1,0,0)+d delta':r'n(1,-1,0,0)^t+d\delta',
 'or(E_u) d beta':r'\operatorname{or}(E_u)\,d\beta',
 'or(Y)=or(F) or(nu_Hopf)':r'\operatorname{or}(Y)=\operatorname{or}(F)\operatorname{or}(\nu_{\rm Hopf})',
 'or(F) dr dtheta':r'\operatorname{or}(F)\,dr\,d\theta',
 'or(Y)=or(F) or(eta)':r'\operatorname{or}(Y)=\operatorname{or}(F)\operatorname{or}(\eta)',
 'd chi_K/db<0':r'\partial\chi_K/\partial b<0',
 'zj=j conjugate(z)':r'zj=j\bar z',
 'A+j conjugate(B)':r'A+j\overline B',
 'eta=q_H i conjugate(q_H)':r'\eta=q_Hi\overline{q_H}',
 '(delta,Z_re,Z_im,y_re,y_im,b)':r'(\delta,Z_{\rm re},Z_{\rm im},y_{\rm re},y_{\rm im},b)',
 '(eta_i,eta_j,eta_k)':r'(\eta_i,\eta_j,\eta_k)',
 'T_n=diag(1,1,n)':r'T_n=\operatorname{diag}(1,1,n)',
 'eta_rel=n(kappa-g(h,w))-theta':r'\eta_{\rm rel}=n(\kappa-g(h,w))-\theta',
 '(j,ceil(j/2),1)':r'(j,\lceil j/2\rceil,1)',
 'm_rel=-ell/4':r'm_{\rm rel}=-\ell/4',
 'n_rel=-(4 k_Jin-ell)/4':r'n_{\rm rel}=-(4k_{\rm Jin}-\ell)/4',
 's=(4 k_Jin-ell)/24 mod28':r's=(4k_{\rm Jin}-\ell)/24\pmod{28}',
 'n_rel=0':r'n_{\rm rel}=0',
 '-e_i+2 sum_{j!=i}e_j':r'-e_i+2\sum_{j\ne i}e_j',
 'delta_der=a_der w':r'\delta_{\rm der}=a_{\rm der}w',
 'a_der=-6k':r'a_{\rm der}=-6k',
 'S=sum w_i':r'S=\sum_iw_i',
 'gcd(a,b,56)=1':r'\gcd(a,b,56)=1',
}
greek=['lambda','delta','gamma','kappa','alpha','beta','sigma','eta','chi','phi','theta','rho','ell','pi','partial']

def math_code(match):
    s=match.group(1)
    if s.startswith(('code/','notes/','records/')):
        return r'\path{'+s+'}'
    if s in exact:
        return r'\('+exact[s]+r'\)'
    s=s.replace('->',r'\longrightarrow ')
    for a,b in [('S1',r'S^1'),('S2',r'S^2'),('S3',r'S^3'),('S5',r'S^5'),('T2',r'T^2')]:
        s=s.replace(a,b)
    s=s.replace(' x ',r'\times ')
    for word in greek:
        s=re.sub(r'(?<![A-Za-z\\])'+word+r'(?![A-Za-z])',lambda _: '\\'+word,s)
    for word in ['log','exp','sin','cos']:
        s=re.sub(r'(?<![A-Za-z\\])'+word+r'(?![A-Za-z])',lambda _: '\\'+word,s)
    for word in ['Re','Im']:
        s=re.sub(r'(?<![A-Za-z\\])'+word+r'(?![A-Za-z])',lambda _:r'\operatorname{'+word+'}',s)
    return r'\('+s+r'\)'

body=re.sub(r'`([^`]+)`',math_code,body)
body=re.sub(r'(?m)^## (.+)$',
    lambda m:r'\par\medskip\noindent\textbf{'+m.group(1)+r'}\par\nobreak',body)
# Long witness tuple is displayed in two typed rows.
body=body.replace(
 r'\((a,b)=(0,1),(1,10),(1,4),(3,14),(1,6),(1,3),(2,5),(3,7)\)',
 r'\[\begin{gathered}(a,b)=(0,1),(1,10),(1,4),(3,14),\\'
 r'(1,6),(1,3),(2,5),(3,7)\end{gathered}\]')
tex=subprocess.run(['pandoc','-f','markdown+tex_math_single_backslash+raw_tex',
                    '-t','latex','--wrap=preserve'],input=body,text=True,
                   capture_output=True,check=True).stdout

statement=r"""
Retain the actual component-supported OS49 families of P3F.31--32,
with \(\lambda=r^{3k}\), \(k>0\), and cap vector
\(n(1,-1,0,0)^t+d\delta\), where \(n=\pm1\) and \(d\in\mathbb Z\).
For one positive physical \(r\)-loop, in the initial positive-diagonal
Cox product the individual integers and relative coordinates are
\[
 k_{\rm Jin}=-6k,\qquad \ell_{\rm Jin}=-24k,\qquad
 (m_{\rm rel},n_{\rm rel},s)=(6k,0,0).
 \tag{OC.1}
\]
The pair is the same for both norm signs. The line used has its actual
\(I_2\) multidegree \((-1,+1)\) and relative square \(-2k\).
For every actual allowed index-one fan \(T(v,w)\), write the physical
delta cocharacter as \(\delta=a v+b w\), and set \(S=a^2-ab+b^2\).
Its oriented return class is
\[
 [\Sigma_{\Phi,T}]=\frac{3k}{4}(S-1)(S-3)\pmod{28}.
 \tag{OC.2}
\]
At fixed \(k\), its exact range is
\(k\{0,4,6,8,14,18,20,22\}\pmod{28}\).
These conclusions retain the component line, both signed norm maps,
the simultaneous closed Cox product, and the actual common-exterior
frame comparison. They use the stated physical parameter loop.
"""
out=(r'\subsection{The component-supported OS49 framing and every fan}'+'\n'+
     r'\begin{statement}{P3K.34}{Proved}'+'\n'+statement+'\n'+
     r'\end{statement}'+'\n'+r'\begin{proof}'+'\n'+tex+'\n'+
     r'\end{proof}'+'\n')
(root/'notes/part3_os49_full_framing.tex').write_text(out)
preamble=(root/'S6_06_BLIND_paper.tex').read_text().split(r'\begin{document}')[0]
(root/'code/part3/k34_standalone.tex').write_text(
    preamble+'\n'+r'\begin{document}'+'\n'+
    r'\input{notes/part3_os49_full_framing.tex}'+'\n'+r'\end{document}'+'\n')
mapping=dict(statement='P3K.34',status='Proved',
             timestamp_utc=datetime.now(timezone.utc).isoformat(),
             proof='notes/part3_os49_full_framing.tex',
             own_value=dict(parameter='lambda=r^(3k), positive r-loop',
                k_Jin='-6k',ell='-24k',m_relative='6k',n_relative=0,
                both_norm_signs=True,delta_twist='arbitrary fixed d',
                actual_line_square='-2k',actual_I2_multidegree=[-1,1],
                all_fan='3k*(S-1)*(S-3)/4 mod28',
                fixed_k_range='k*{0,4,6,8,14,18,20,22} mod28'),
             audits=['root: complete proof PASS',
                     'blind_control: signed boundary, Cox and normal clutch PASS'],
             comparison='Extends the already proved reference-fan index zero; no height substitution or division of a cover class.')
(root/'code/part3/os49_full_framing_results_mapping.json').write_text(json.dumps(mapping,indent=2)+'\n')
print('Exported K34 separate include, standalone wrapper, and result mapping; master untouched.')


# BEGIN POST-CHECKPOINT15 SCALAR-SCOPE RESTORATION
import importlib.util as _scalar_scope_importlib
from pathlib import Path as _ScalarScopePath
_scalar_scope_root = _ScalarScopePath(__file__).resolve().parents[2]
_scalar_scope_spec = _scalar_scope_importlib.spec_from_file_location(
    "_scalar_dependency_scope",
    _scalar_scope_root / "code/part3/scalar_dependency_scope.py")
_scalar_scope_module = _scalar_scope_importlib.module_from_spec(_scalar_scope_spec)
_scalar_scope_spec.loader.exec_module(_scalar_scope_module)
_scalar_scope_module.postprocess_generated(
    ['code/part3/os49_full_framing_results_mapping.json'], ['notes/part3_os49_full_framing.tex'], origin='code/part3/export_os49_full_framing.py')
# END POST-CHECKPOINT15 SCALAR-SCOPE RESTORATION
