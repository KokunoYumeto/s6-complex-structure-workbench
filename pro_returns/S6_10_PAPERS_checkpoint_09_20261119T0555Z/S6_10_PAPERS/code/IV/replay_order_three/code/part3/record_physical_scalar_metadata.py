#!/usr/bin/env python3
"""Preserve old fields and record K68's actual physical-line arrow; no TeX writes."""
from pathlib import Path
from datetime import datetime,timezone
import json,shutil,hashlib,re
R=Path(__file__).resolve().parents[2]
stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
A=R/'records/attempts/physical_scalar_reference_sign'/stamp
A.mkdir(parents=True)
paths=['code/part3/results_mapping.json','notes/part3_canonical_scalar_catalogue.md','code/part3_root/export_canonical_scalar_catalogue.py']
for s in paths:
 p=R/s;q=A/s;q.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,q)
changes=[]
p=R/paths[0];d=json.loads(p.read_text())
def walk(x,path='$'):
 if isinstance(x,dict):
  ident=x.get('id')
  if ident in {'P3K.26','P3K.28'}:
   old=x.get('statement')
   new=('Actual physical return A=m*a^2/(2d)-[m(12-e)+e_root]/12, identical for n=+/-1; K68 retains M=U* and the inverse-closing gluing map.' if ident=='P3K.26' else 'Actual joint cap/page/line/Thom comparison for F38/F46/F47; physical A=Ma^2/(2d)-chi in all nine sectors and both determinant signs; F36 one-star physical A=+2 for both profiles and norms, by K68.')
   x['statement']=new;x['physical_sign_proof']='P3K.68';changes.append({'field':path+'.statement','old':old,'new':new})
  for k,v in x.items():walk(v,path+'.'+k)
 elif isinstance(x,list):
  for i,v in enumerate(x):walk(v,path+f'[{i}]')
walk(d);p.write_text(json.dumps(d,indent=2)+'\n')
p=R/paths[1];t=p.read_text()
t=t.replace('P3F.53. Proved. The complete synthesis and the exact catalogue\ncertificate have passed independent mathematical audits.', 'P3F.53. The prior compound all-fan claim is refuted. The source, root, cap, topology and actual reference page maps are retained. P3K.68 supplies the physical-line correction, and P3K.64/P3K.67 give the proved vertical-edge fan scopes. All prior text is preserved in the timestamped correction archive.')
start=t.index('For one positive \\(r\\)-circle, the actual reference Cox')
end=t.index('## C3.',start)
t=t[:start]+r'''For one positive \(r\)-circle the retained positive-meridian line
\(U\) has the previously computed characteristic pair
\((-3H,-24\chi)\). P3K.68 gives the actual map from the physical
circle line \(M=U^*\), including the inverse closing in the clutch:
\(\lambda_M=-\lambda_U=\Sigma_{\Phi}\). Consequently the physical
pair and the physical reference return are
\[
 (k_M,\ell_M)=(3H,24\chi),\qquad
 A_{\rm phys}=H/2-\chi.                         \tag{SC.5}
\]
The original relative rotating coordinates are retained only in
their stated \(U\)-frame; they are not assigned to every native star.
The actual page, root and line maps in (SC.3)--(SC.4) are unchanged.

The old all-fan polynomial (SC.6), and its proposed universal
recurrence, are refuted by P3K.61--64. The exact earlier expression
and every associated computation are preserved in the correction
archive and as explicitly withdrawn arithmetic in the catalogue JSON.
For the actual canonical parameter \(\lambda=r^M\), the proved
physical-vertical-edge fan formula is instead
\[
 A_n=H/2-\chi-M\frac{n(n-1)}2\pmod {28},
 \qquad T_n:\ e_2,(1,n),(1,n-1),                \tag{SC.6-corrected}
\]
by P3K.64's individual native-star and Cox maps. P3K.67 retains the
bounded source factor for the actual shorter endpoint and replaces
\(M\) by \(M/b\) in the relative fan correction. This supplies no
universal formula for other fans. Positive parameter covers multiply
the actual return by their degree; F50's displayed inverse-action
map carries a positive expanding loop to the inverse contracting loop.

'''+t[end:]
t=t.replace('including the simultaneous Cox\nproduct used by K31. Thus the class (SC.6)\nbelongs to the constructed closed family.', 'with every source and line factor retained. The earlier further\nassertion of a simultaneous equivariant plumbing product was refuted\nby P3K.61; its corrected individual-star application is P3K.64.')
t=t.replace('and\ngives (SC.5). Finally K31\'s common-exterior\nmeridians, stable frame transitions and\nexplicit flop recurrence apply to that\nsimultaneous product and give (SC.6).', 'and\ngives the retained U-line pair. The exact dual-line and inverse-closing\nmap P3K.68 gives (SC.5). The literal individual-star maps of P3K.64\ngive (SC.6-corrected).')
start=t.index('K33 supplies the explicit shorter closed')
end=t.index('This catalogue fixes the source',start)
t=t[:start]+r'''K33 and K35 retain their exact shorter scalar endpoint maps.
P3K.67 proves the actual physical-vertical-edge fan formula for those
endpoints, including their full bounded source factors. For the
original coprime \((3K,4L)\) construction, the exact parameter is
\(w_h=e^{-\pi ic/(KL)}\), the initial class is zero, and
\(A_n=-KL\,n(n-1)\pmod {28}\). No value for every other fan is
assigned by that statement.

For the component-supported OS49 line, P3K.65 gives the actual
negative-fan classes \(-3k\) for \(\lambda=r^{3k}\) and \(-k\)
for the shorter \(w=r^3\) loop; the positive fan has integer and
class zero. The relative native flop comparison is unchanged by
P3K.68's physical reference correction. The former both-fan zero
and universal-polynomial claims are preserved as refuted attempts.

'''+t[end:]
p.write_text(t)
p=R/paths[2];t=p.read_text()
t=t.replace('pair \\((-3H,-24\\chi)\\) and return index \\(A=\\chi-H/2\\).','pair \\((3H,24\\chi)\\) and physical return index \\(A=H/2-\\chi\\), by the exact dual-line and inverse-closing map P3K.68.')
start=t.index('On the actual fan \\(T(v_1,v_2)\\)')
end=t.index('"""',start)
t=t[:start]+r'''The former universal all-fan polynomial is refuted. In the proved
physical-vertical-edge fan scope of P3K.64, the actual canonical loop
has \(A_n=H/2-\chi-Mn(n-1)/2\). P3K.67 retains the actual shorter
endpoint and proves its relative correction with winding \(M/b\).
P3K.65 gives the two specified OS49 fan values. No universal fan
formula is assigned here. The complete earlier compound claim is
preserved in the correction archive.
'''+t[end:]
t=t.replace(r'\begin{statement}{P3F.53}{Proved}',r'\begin{statement}{P3F.53}{Refuted prior compound claim; retained corrected scope}')
p.write_text(t)
(A/'field_changes.json').write_text(json.dumps({'utc':datetime.now(timezone.utc).isoformat(),'proof':'P3K.68','changes':changes,'notes':'F53 MD/exporter corrected for future regeneration. Exporter was not run; frozen manuscript untouched. All old files preserved here.'},indent=2)+'\n')
print(json.dumps({'archive':str(A),'mapping_fields':len(changes),'tex_writes':0}))
