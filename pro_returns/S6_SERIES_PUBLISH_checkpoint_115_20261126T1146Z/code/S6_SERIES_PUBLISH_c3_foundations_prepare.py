from pathlib import Path
import csv
import datetime
import re

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'agents/continuation3_foundations'
OUT.mkdir(parents=True, exist_ok=True)
SOURCE = (ROOT / 'S6_SERIES_PUBLISH_II.tex').read_text()
DEFECT_FIELDS = ['change_id','type','statement_id','old_location','old_page','new_location','new_page','old_text','new_text','reason','review_status']
EVENT_FIELDS = next(csv.reader((ROOT / 'CHECK_EVENTS.tsv').open(), delimiter='\t'))
changes = []
events = []
units = []
now = datetime.datetime.now(datetime.timezone.utc).isoformat()

def unit(start, end):
    a = SOURCE.index(start)
    b = SOURCE.index(end, a + len(start))
    return SOURCE[a:b]

def change(text, old, new, kinds, owner, location, reason):
    assert text.count(old) == 1, (owner, location, text.count(old))
    for kind in kinds.split(','):
        changes.append(dict(change_id=f'II-C3-FOUND-{len(changes)+1:03}', type=kind,
            statement_id=owner, old_location=location, old_page='cp35; final page concordance pending',
            new_location=location, new_page='integrated build pending', old_text=old,new_text=new,
            reason=reason, review_status='Complete original and replacement read; exact mathematical scope preserved.'))
    return text.replace(old,new)

def event(owner, where, outcome):
    row={k:'' for k in EVENT_FIELDS}
    row.update(statement_id=owner,date=now[:10],who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; inherited effort not separately exposed; continuation3 foundations',
      type='used and rechecked in this run',outcome=outcome,event_id=f'publish:c3:foundations:{owner}',
      phase='publication text and proof comparison',source_file='agents/continuation3_foundations/S6_SERIES_PUBLISH_foundations_CHECK_EVENTS.tsv',
      source_event_type='used and rechecked in this run',evidence_group=f'publish:c3:foundations:{owner}',date_utc=now,where=where)
    events.append(row)

def save_unit(name, old, new, unit_label, open_rows=None):
    open_rows = open_rows or {}
    # Every old label and permanent target remains at exactly one location.
    for pat in [r'\\label\{([^}]+)\}',r'\\hypertarget\{([^}]+)\}\{\}']:
        assert sorted(re.findall(pat,old)) == sorted(re.findall(pat,new)),name
    (OUT/f'S6_SERIES_PUBLISH_II_{name}.tex').write_text(new,newline='\n')
    for kind in [f'D{i:02}' for i in range(1,26)]+['structure']:
        units.append(dict(unit=unit_label,row=kind,status='open' if kind in open_rows else 'done',
          basis=open_rows.get(kind,'Read the complete unit against the register; every changed instance is in the defects rows. No remaining instance found in this unit.'),
          fragment=f'agents/continuation3_foundations/S6_SERIES_PUBLISH_II_{name}.tex'))

common_start='\\section{Common conventions}'
index_start='\\section{Index, Picard components and endpoint cohomology}'
integral_start='\\section{Integral specialization, coherent restrictions and component counts}'
smooth_start='\\section{Complete smooth-fibre classification and actual Hopf occurrence}'
cotangent_start='\\section{Cotangent torsion, conductor and the printed endpoint error}'

old=unit(common_start,index_start)
new=change(old,
 r'''$v_1=r_1\varepsilon+k_1\widehat\delta$ and
$v_2=r_2\varepsilon'+k_2\widehat\delta$; the coefficients
$r_1,r_2$ are also denoted $l_1,l_2$ in the peripheral presentation.''',
 r'''$v_1=l_1\varepsilon+k_1\widehat\delta$ and
$v_2=l_2\varepsilon'+k_2\widehat\delta$, using the coefficients
$l_1,l_2$ of the peripheral presentation.''',
 'D20','def:II:marked-conventions','Common conventions: finite affine coefficients',
 'The original explicitly identifies r_1=l_1 and r_2=l_2. Substituting these two identities in the two displayed vector expressions keeps their vectors unchanged and gives one notation in this unit.')
new=change(new,
 r'''$p=12l_0-4l_1-3l_2$, retaining $\pi_1(X)=\Z/|p|$.''',
 r'''$p=12l_0-4l_1-3l_2$ and $\pi_1(X)=\Z/|p|$.''',
 'D08','def:II:marked-conventions','Common conventions: fundamental group',
 'Remove the production verb. The parameter and fundamental-group formula are identical.')
new=change(new,
 'Homology and cohomology retain their displayed\ncoefficient groups, and complex manifolds carry their complex orientations.',
 'The coefficient group is displayed in each homology or cohomology group.\nComplex manifolds carry their complex orientations.',
 'D08','def:II:marked-conventions','Common conventions: coefficient groups',
 'State the coefficient and orientation conventions directly; neither convention changes.')
save_unit('common_conventions',old,new,'sec:II:conventions',{'D06':'The inherited broad reference to the complete marked transport and construction in Paper I needs its exact statement locator; Paper I stays closed until the five-together step.','D22':'The inherited fundamental-group formula needs the exact Paper I proving locator in the joint reference pass.','structure':'Unit text is ready; final placement and cross-paper locator are controlled by the integrating root.'})
event('def:II:marked-conventions','Common conventions: full definition and explicit coefficient identities',
 'Read the complete original and replacement definition. The old identities r_1=l_1 and r_2=l_2 give exactly the same two affine vectors after substitution. All period, monodromy, multiplicity, determinant and fundamental-group formulas remain unchanged. The existing broad Paper I construction reference remains an explicit locator gate; no independent mathematical check or final-page reading is claimed.')

old=unit(index_start,integral_start)
orphan=r'''Statements \ref{cdp:st:C.1.1}--\ref{cdp:st:C.1.3} prove the stated index obstruction with rational Betti-number
vanishing. No integral trivialization of either Chern class is needed
for the index. The existence of the divisor enters in the endpoint
vanishing, and a positive multiple of its actual Cartier divisor
enters the Picard family. These statements supply an index
obstruction; they make no assertion that the failed degree-two
vanishing holds.'''
new=change(old,orphan,'','D01,D02,D08,D11,D12,D13','cdp:st:C.1.1; cdp:st:C.1.3','Index section: paragraph after the twisted-tangent lower-bound proof',
 'The first proof already establishes rational Chern-class vanishing, and the second explicitly uses the divisor through CDP98 Corollary 1.3 and exponentiates Cech classes in each Picard component. The deleted paragraph repeats these exact conclusions and adds a draft-facing disclaimer; no assumption, conclusion or proof step is removed.')
new=change(new,
 r'''The identity
$g_*\mathcal O_Y=\mathcal O_C$, supplied by Stein factorization and
the normality of $C$, therefore gives a holomorphic descended function''',
 r'''The identity
$g_*\mathcal O_Y=\mathcal O_C$, given by Stein factorization and
the normality of $C$, therefore gives a holomorphic descended function''',
 'D08','cdp:st:E1','Vertical divisors proof, meromorphic descent',
 'The map and descent argument are unchanged; replace the production vocabulary with the named mathematical justification.')
# Whitespace here is source formatting only; no printed mathematical paragraph is removed.
new=re.sub(r'\n{4,}', '\n\n\n',new)
save_unit('index_picard_endpoints',old,new,'sec:II:01',{'D19':'The unit has no manual equation tags; section-based equation counter must be set once in the preamble by root.','structure':'All content is in its unique proving owner within the unit; final whole-paper placement remains with root.'})
event('cdp:st:C.1.1','Index/Picard proof, complete comparison and removed recap',
 'Read both complete versions. UCT, exponential-sequence maps, finite H^2, rational c_1/c_2, Dolbeault index and complex-orientation Euler calculation are unchanged. Deleted only the separate recap of the same rational-cohomology conclusions.')
event('cdp:st:C.1.3','Twisted-tangent lower bound, complete comparison and CDP98 Corollary 1.3',
 'Read the complete proof and the attached primary source at CDP98 Corollary 1.3 and its proof. The source supplies generic H^0 vanishing with b_2=0 and an effective divisor. Applying it to the two displayed bundles, Serre duality, the explicit exponential Picard family and semicontinuity remain unchanged. The separate recap and disclaimer were removed.')
event('cdp:st:E1','Vertical divisors and meromorphic descent: complete original/receiving proof',
 'Read the entire proof before and after editing. The restriction of the divisor class, positive Kahler integral, Stein-factor identity, proper graph image, generic-degree-one descent and injective field pullback are identical. One production word changes; no new independent proof is claimed.')

def write_table(path,fields,rows):
    with path.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n')
        w.writeheader();w.writerows(rows)

write_table(OUT/'S6_SERIES_PUBLISH_foundations_defects.tsv',DEFECT_FIELDS,changes)
write_table(OUT/'S6_SERIES_PUBLISH_foundations_CHECK_EVENTS.tsv',EVENT_FIELDS,events)
write_table(OUT/'S6_SERIES_PUBLISH_foundations_unit_progress.tsv',['unit','row','status','basis','fragment'],units)
print(f'{len(changes)} defect rows; {len(events)} exposed-reading events; {len(units)} unit rows. No shared deliverable changed.')
