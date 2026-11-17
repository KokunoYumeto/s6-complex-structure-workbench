"""Preserve upstream Simon scripts; adapt obsolete PARI structure access only."""
from pathlib import Path
import re
import urllib.request

p=Path(__file__).resolve().parents[1]/'records'
for name in ['ell.gp','ellcommon.gp']:
    target=p/('Crank_Simon_'+name)
    if not target.exists():
        target.write_bytes(urllib.request.urlopen(
            'https://simond.users.lmno.cnrs.fr/'+name,timeout=30).read())
    print(name,target.stat().st_size)
s=(p/'Crank_Simon_ell.gp').read_text()
s=s.replace('ell *= Mod(1,bnf.pol);',
            'ell = ellinit(ell[1..5]*Mod(1,bnf.pol),bnf);')
s=s.replace('ell = ellinit(Mod(lift(ell),bnf.pol),1);',
            'ell = ellinit(Mod(lift(ell[1..5]),bnf.pol),bnf);')
s=re.sub(r'([A-Za-z][A-Za-z0-9]*)\.tufu',r'concat([\1.tu[2]],\1.fu)',s)
s=re.sub(r'([A-Za-z][A-Za-z0-9]*)\.futu',r'concat(\1.fu,[\1.tu[2]])',s)
(p/'Crank_Simon_ell_compat.gp').write_text(s)
print('Compatibility changes: only elliptic coefficient-vector coercion and obsolete tufu/futu accessors.')
