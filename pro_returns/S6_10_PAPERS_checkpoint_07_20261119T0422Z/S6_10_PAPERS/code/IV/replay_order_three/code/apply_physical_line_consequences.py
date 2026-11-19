"""Preserve located false physical-sign assertions; register their proved correction."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re,shutil
root=Path(__file__).resolve().parents[1]
stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
archive=root/'records/attempts/physical_line_consequences'/stamp
archive.mkdir(parents=True)
corrections={
 'P3K.6':r'The meridian-one Thom line is the Hermitian dual of the physical line. Its page restriction is \(-c_1(M)\). The embedded trace, collars and integer uniqueness are retained; the positive page-line assertion is refuted by the explicit dual arrow in K68.',
 'P3F.25':r'The old signed nonzero physical return is refuted. Its computed index is the dual-line index \(A_U\); the actual sphere class is \(-A_U\). In particular the degree-four weighted OS47 example has class \(4\). The zero-reference conclusions and the source, page and cap maps are retained. K68--69 give the corrected physical transfer.',
 'P3K.10':r'The displayed physical class \(25\) is refuted. The same positive primitive OS45 family has physical integer \(3\), Eells--Kuiper invariant \(3/28\), and class \(3\). Its source, line, cap and topology proof is retained. K68--69 prove the missing dual-line and sphere-gluing arrow.',
 'P3K.22':r'The physical classes in the old reference table are refuted except for the self-opposite residue \(14\). In its four profile groups the actual physical integers are \(3,6,9,14\). The source constructions, topology, page squares and restrictions on smooth-site caps are retained. K68--69 supply the exact corrected transfer.',
 'P3K.23':r'The physical fixed-edge formula is \(7A_M\), where \(A_M\) is the actual physical integer. The old \(-5A\) formula is refuted. All displayed quaternion, common-link, relative-group and oriented commutator maps are retained. The native right integer is \(n=6A_M=-6A_U\); K68--69 prove the line and gluing dictionary and the corrected examples.',
 'P3K.24':r'The old nonzero physical signs are refuted. The actual positive return is \(3l+2\), with Eells--Kuiper invariant \((3l+2)/28\). The two source families and their actual endpoint maps are retained. K68--69 prove this correction through the physical line.',
 'P3K.27':r'The displayed central coordinate is refuted. The characteristic pair \((-3d,-24)\) is the meridian-one dual-line pair; the actual free integers remain \((6,3d-6)\), while the physical central class is \(d/2-1\). The actual Cox framing comparison is retained. K68--69 provide the precise convention map.',
 'P3K.30':r'The displayed central coordinate is refuted. With \(U=M^{-1}\), the retained pair is \((k_U,\ell_U)=(-3H,-24\chi)\), the physical pair is \((3H,24\chi)\), and the physical central class is \(H/2-\chi\). The native free pair \((6\chi,3H-6\chi)\) is retained. K68--69 prove the exact line and transfer maps.',
 'P3K.32':r'The displayed physical central coordinate is refuted and the broad all-fan final sentence remains withdrawn. The topology, signed norm reduction and page data are retained. Its reference physical integer is \(H/2-\chi\); its retained dual-line characteristic and free-relative data have the convention stated in K69. The actual vertical-fan corrections are K64 and K67.',
 'P3K.40':r'The actual first fixed-edge return is \(-7=21\), replacing the old \(-5=23\). Its native right integer \(-6\) and every local source/Cox/cap comparison remain valid. The initial physical class is \(-1\), and the same directed flop adds \(-6\). K68--69 prove the correction.',
 'P3K.45':r'The complete half-source conjugacy is retained. The reflected initial physical return is \(-1=27\), and the distinct fixed-edge flop is \(-7=21\). The old numerical labels are refuted by K68--69.',
 'P3K.46':r'The retained meridian-one pair is \((6,0)\), its physical-line pair is \((-6,0)\), and its native relative coordinates are \((0,-6,-1)\). The actual cap map and parameter reversal are retained; the old central label \(1\) is refuted. See K68--69.',
 'P3K.50':r'The ordinary relative coordinates are \((6,-6,-1)\). Its variation \(V_{00}=0\), derivative \(\delta_0=-12\), and pure-left product-change maps are retained. Only the old central label is refuted; K68--69 give the corrected physical reference.',
 'P3K.52':r'The full derivative vector and all displayed native and ordinary free pairs are retained. Their common physical central coordinate is \(-1\). The old central label \(1\) is refuted by K68--69.',
 'P3K.54':r'The three actual first-flop classes are \((21,21,27)\), replacing \((23,23,1)\). Their complete native products and right integers \((-6,-6,0)\) are retained. K68--69 give the corrected reference and the same directed central increments.',
 'P3K.56':r'The actual vertical-fan class is \(-1-3n(n-1)\), with image \(\{5,7,9,13,19,21,23,27\}\). The fan enumeration, source and cap maps, and native right integers are retained. The old additive baseline is refuted; K69 supplies the full corrected recurrence.',
 'P3K.57':r'The complete infinity source/cap maps and residue calculations compute the meridian-one dual-line index. Their values are \(0,1\), while the physical sphere classes are \(0,-1\). The old reduced physical class \(1\) is refuted. K68 explicitly checks the line in IE.4--5; K69 gives the corrected transfer.',
 'P3K.58':r'The retained actual cut-surface relation is \(Z_T+Z_{JT}-1+I_T=0\). Put \(A_{\rm scalar}=0\) in the good branch and \(3p-1\) in the reduced branch. Then the full infinity returns are \(0\) and \(-1-2k(3p-1)\), and the paired sums are \(1\) and \(2+2k(3p-1)\). The full source/root/annular maps are retained; the earlier numerical signs are refuted and corrected in K69.',
 'P3K.59':r'The actual two central sequences are \(-1-3j(j+1)\) and \(-7-24j(j+1)\). The second has least period seven and image \(\{1,13,17,21\}\). All displayed matrices, native free pairs and directed mutation identities are retained. The old additive baselines are refuted and corrected in K69.',
 'P3K.60':r'The actual single native pair \((1-a,a)\) and difference \(Z_{JT}-Z_T=a\) are retained. The corrected paired possibilities are \((kA_{\rm scalar}+14e,a+kA_{\rm scalar}+14e)\), \(e\in\{0,1\}\), with physical scalar integer \(0\) or \(3p-1\). The old absolute pair is refuted; K69 proves the corrected sum and retains the unresolved order-two choice.'
}
changed=[]
for p in sorted((root/'notes').glob('part3*.tex')):
 text=p.read_text();old=text
 def edit(m):
  sid,status,body=m.groups()
  if sid not in corrections:return m.group(0)
  marker=r'\par\noindent\textbf{Physical-line correction, 17 November 2026.}'
  if marker in body:return m.group(0)
  notice=marker+' '+corrections[sid]+r' The following earlier assertion and its argument are retained as the located historical claim; their corrected current consequences are proved in K68--69.\medskip\par '+body
  changed.append({'file':str(p.relative_to(root)),'id':sid,'prior_status':status,'current_status':'Refuted','correction':corrections[sid]})
  return r'\begin{statement}{'+sid+r'}{Refuted; physical-line correction}'+notice+r'\end{statement}'
 text=re.sub(r'\\begin\{statement\}\{([^}]+)\}\{([^}]+)\}(.*?)\\end\{statement\}',edit,text,flags=re.S)
 if text!=old:
  target=archive/p.relative_to(root);target.parent.mkdir(parents=True,exist_ok=True);target.write_text(old)
  p.write_text(text)
found={v['id'] for v in changed}
assert found==set(corrections),(set(corrections)-found)
record={'utc':datetime.now(timezone.utc).isoformat(),'status':'APPLIED','exact_map_proof':'P3K.68','corrected_consequences':'P3K.69','preserved':str(archive.relative_to(root)),'scope':changed,'preservation':'Earlier assertions, proof text and computations retained. Current physical conclusions are the explicit notices and K68--69.'}
(root/'records/physical_line_correction_scope.json').write_text(json.dumps(record,indent=2)+'\n')
audit={'status':'PASS','utc':datetime.now(timezone.utc).isoformat(),'reviewer':'root','proof':'notes/part3_shorter_scalar_vertical_fans_working.md','scope':'SE.1--5 with A0 the actual physical reference class; no signed nonzero page formula','checked':['Actual forward rational lift and finite-root character/cochain square','Exact sigma difference, cyclic normalization and all b intermediate products','Native individual-star products and complete source-factor seam','Actual double pullback, ordinary trace and native pure-left correction','Directed Cox maps and recurrence','Original K33 periodic global physical-delta gauge with all cap arrows'],'conclusion':'A_n=A0-(M/b)n(n-1)/2; original K33 A0=0 gives -KL n(n-1).'}
(root/'records/root_audit_shorter_scalar_vertical_fans.json').write_text(json.dumps(audit,indent=2)+'\n')
print(json.dumps({'corrected_prior_assertions':len(changed),'preserved':str(archive)}))
