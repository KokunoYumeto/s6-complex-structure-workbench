"""Exact publication-form edits after the complete K111/K112 proof review."""
from pathlib import Path
import datetime,hashlib,json,re
R=Path(__file__).resolve().parents[1]
p=R/'parts/IV.body.linked.tex';before=p.read_text();s=before;changes=[]
def change(old,new,count=1):
    global s
    assert s.count(old)==count,(old,s.count(old),count)
    s=s.replace(old,new);changes.append(dict(old=old,new=new,count=count))
# These prefixes contain only execution dates. Every mathematical sentence,
# formula, source condition and original tag is retained immediately after it.
for prefix in ['Working proof, 18 November 2026. ','Working exact construction, 18 November 2026. ']:
    count=s.count(prefix);assert count>0
    change(prefix,'',count)
titles=[
'The original cells and the actual common maps.',
'The three complete endpoint atlases.',
'The unchanged exterior modules and the second action.',
'Complete physical ownership and compact localization.',
'The actual moving cap and twelve source doubles.',
'The outer physical bundle, finite square and directed conclusion.',
'Exact construction records.']
mapping={letter:i for i,letter in enumerate('ABCDEFG',1)}
for letter,title in zip('ABCDEFG',titles):
    change(r'\medskip\noindent\textbf{'+letter+'. '+title+'}',r'\medskip\noindent\textbf{\(\langle2\rangle'+str(mapping[letter])+r'\). '+title+'}')
for letter in ['C','D','E']:
    old='supporting proof 20 '+letter
    change(old,'supporting proof 20, substep '+str(mapping[letter]),s.count(old))
for old,new in [
('atlas constructed in A--B','atlas constructed in substeps 1--2'),
('identity-character\nisomorphisms of B','identity-character\nisomorphisms of substep 2'),
('endpoint character matrices obtained from B','endpoint character matrices obtained from substep 2'),
('localized identity-character maps in B','localized identity-character maps in substep 2'),
('The graph maps in C','The graph maps in substep 3'),
('divisor bundles computed in E','divisor bundles computed in substep 5'),
('explicitly checked in C','explicitly checked in substep 3'),
('line maps from E','line maps from substep 5'),
('the one proved in A--F','the one proved in substeps 1--6')]:change(old,new)
change('These equalities evaluate differences of its actual returns. This\nnote does not assign the still unevaluated constant \\(S_0\\). Its complete\nsource, native products and signs are proved below.',
'These equalities evaluate differences of its actual returns. The\nabsolute value \\(S_0=2\\) follows from the proved K111 seed and the\ninitial native \\(T_{-1}\\)-to-\\(T_0\\) arrow in the theorem above.\nThe complete source, native products and signs underlying the displayed\ndifferences are proved below.')
tagpat=r'\\(?:tag|label)\{[^}]+\}'
assert re.findall(tagpat,before)==re.findall(tagpat,s),'Every tag/label must be retained in identical order.'
p.write_text(s)
receipt=dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),before_sha256=hashlib.sha256(before.encode()).hexdigest(),after_sha256=hashlib.sha256(s.encode()).hexdigest(),heading_bijection=mapping,changes=changes,all_tag_label_sequence_preserved=True,mathematical_change='None. The formerly unevaluated-S0 wording is synchronized with the already proved seed and displayed native arrow. Numeric heading references are transported by the explicit A-G to1-7 bijection.',pending='Build and actual changed-page inspection before whole-row closure.')
(R/'analysis/IV_publication_format_07.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({'exact_replacements':len(changes),'removed_date_prefixes':sum(x['count'] for x in changes[:2]),'all_tags_preserved':True}))
