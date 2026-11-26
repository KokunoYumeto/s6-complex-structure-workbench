"""Admit the factor-preserving contact proof and close the R15 multiplicity premise."""
from S6_SERIES_PUBLISH_c3_edit import *
import json
import subprocess
import sys

folder=ROOT/'agents/continuation3_foundations/sec07'
prefix='S6_SERIES_PUBLISH_sec07_smooth_contact_'
guards=json.loads((folder/(prefix+'guards.json')).read_text())
before=SOURCE.read_text();after=before
for row in guards:
    assert after.count(row['old'])==1,row['key']
    if row['key']=='R15 exact full-function applications':
        a=row['old'].index('At every critical-curve point')
        b=row['old'].index('\\end{proposition}',a)
        c=row['new'].index('At every critical-curve point')
        d=row['new'].index('\\end{proposition}',c)
        assert row['old'][a:b]==row['new'][c:d]
    after=after.replace(row['old'],row['new'],1)
    print('Applied',row['key'])
preserve_identifiers(before,after)
for old,new in zip(identifiers(before),identifiers(after)):
    for name,count in old.items():assert new[name]==count,name
SOURCE.write_text(after,newline='\n')
for suffix,target,key in [('defects.tsv','S6_SERIES_PUBLISH_defects_II.tsv','change_id'),
                         ('CHECK_EVENTS.tsv','CHECK_EVENTS.tsv','event_id')]:
    _,rows=read_tsv(folder/(prefix+suffix))
    print(suffix,append_rows(ROOT/target,rows,key))
add_event('prop:II:smooth-branch-contact; night:P4R.15; cdp:st:A.5.17',
 'II-C3-ROOT-SMOOTH-CONTACT-ADMISSION','used and rechecked in this run',
 'Root read the complete receiving P298 and R15, the complete old R15, all three guards, the A.5.17 old/new Hessian paragraph, and the complete comparison. The foundations agent additionally read the entire receiving A.5.17 proof. The full family U(X-H_s)^a(X+H_s)^b retains U,a,b. Boundary charts cover both smooth component strata and intersection links with fixed weighted transverse functions. The critical-centre equation, Lambda/R inverse, H_0=H identity, XX bracket -N^3/(4ab), Schur complement kN*v^(kN-1)*Q and full determinant were checked algebraically from the displayed maps. Both analytic branches and their powers persist. P295 with g_s=F_s,m=1 transports the compact weighted or Morse sphere into the original torus fibre. The locally irreducible R15 case applies A.5.17 through F=(U^(1/M)f)^M; the reducible monic quadratic factors give exactly the two smooth branches required by P298. The R15 printed statement is byte-identical. Its full-fibre multiplicity premise is resolved. P4R.14, P4.41 and P4.45 remain open. No independent or final-page credit.',
 'S6_SERIES_PUBLISH_II.tex: P298, A.5.17 and nonzero-Hessian rigidity',source='agents/continuation3_foundations/sec07/S6_SERIES_PUBLISH_sec07_smooth_contact_comparison.md')
data=dict(unit='night:P4R.15',event_id='II-C3-ROOT-NONZERO-HESSIAN-UNIT-READ',
 complete_original_and_receiving_read=True,
 outcome='Complete original and receiving nonzero-Hessian unit read and compared, including the precise common-power map in its irreducible case and both monic analytic factors in its reducible case. The entire new P298 proof and A.5.17 formula transfer were read as recorded in the admission event. Every original mathematical formula remains at its stated owner, and the original full domain and printed conclusion are unchanged. All local defect instances found are logged; D14/D23 and whole-paper structure remain open. The other three multiplicity gates remain open. No independent credit.',
 unit_detail='R15 full-fibre multiplicity premise closed by the exact factor-preserving P298 construction; the three other broad consumers remain under review.')
subprocess.run([sys.executable,str(ROOT/'code/S6_SERIES_PUBLISH_c3_read_unit.py')],input=json.dumps(data),text=True,check=True)
print('Admitted P298 and R15; three remaining full-fibre deformation gates stay open.')
