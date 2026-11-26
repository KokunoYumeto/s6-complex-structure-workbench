"""Bounded identity/diff inspection of the wholly read LF/LJ fragment."""
import difflib,hashlib,re
from pathlib import Path
root=Path(__file__).resolve().parent.parent
p=root/'agents/continuation8_iii_integration/units/weighted/three_primary_types.tex'
s=p.read_text()
print('INPUT_LINES',len(s.splitlines()),'SHA256',hashlib.sha256(p.read_bytes()).hexdigest())
for tag,lane in [('LF','three_primary_receiving'),('LJ','mixed_three_receiving')]:
 rp=root/f'agents/continuation7_iii_{lane}/S6_SERIES_PUBLISH_III_02{tag}_receiving.tex'
 old=rp.read_text()
 a=s.index(r'\begin{theorem}',s.index('tag-02'+tag)-200 if tag=='LJ' else 0)
 b=s.index(r'\end{proof}',a)+len(r'\end{proof}')
 block=s[a:b].strip()+'\n'
 print('RECEIVER',tag,'LINES',len(old.splitlines()),'SHA256',hashlib.sha256(rp.read_bytes()).hexdigest())
 print(''.join(difflib.unified_diff(old.splitlines(True),block.splitlines(True),n=2)))
 lj=s[s.index(r'\begin{theorem}[the mixed'):]
 nums=re.findall(r'\\qquad\\textnormal\{\((\d+)\)\}',lj)
 print('LJ_MANUAL_NUMBERS',len(nums),'UNIQUE',len(set(nums)),','.join(nums))
 stripped=re.sub(r'\\qquad\\textnormal\{\(\d+\)\}', '', lj)
 matches=list(re.finditer(r'\((\d+)\)',stripped))
 print('LJ_PARENTHESIZED_INTEGER_OCCURRENCES',len(matches))
 for m in matches:
  print(repr(stripped[max(0,m.start()-42):m.end()+42]))
print('READ_ONLY; NO_CRITERION_CREDIT')
