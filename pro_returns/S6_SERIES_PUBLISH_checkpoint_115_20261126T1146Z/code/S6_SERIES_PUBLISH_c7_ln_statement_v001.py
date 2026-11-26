"""Extract only the canonical LN theorem, leaving its proof and old packet closed."""
from pathlib import Path
from hashlib import sha256
import re

ROOT=Path(__file__).resolve().parents[1]
raw=(ROOT/'S6_SERIES_PUBLISH_III.tex').read_bytes()
assert sha256(raw).hexdigest()=='9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0'
text=raw.decode()
marker=r'\label{maps:src:D.2.46}'
assert text.count(marker)==1
position=text.index(marker)
starts=list(re.finditer(r'\\begin\{(theorem|proposition|lemma|corollary)\}',text[:position]))
match=starts[-1]
start=match.start()
environment=match.group(1)
end=text.index('\\end{'+environment+'}',position)+len('\\end{'+environment+'}')
statement=text[start:end]
assert r'\begin{proof}' not in statement and r'\end{proof}' not in statement
assert 'tag-02LN' in statement
folder=ROOT/'agents/continuation7_iii_ln_statement'
folder.mkdir(exist_ok=True)
target=folder/'S6_SERIES_PUBLISH_III_02LN_statement_only.tex'
assert not target.exists()
header=('% Clean canonical statement-only intake for02LN.\n'
        '% The prior862-line packet remains closed: it contains argument-bearing additions.\n'
        '% This file includes only the exact theorem environment, with its stated dependencies.\n'
        '% The canonical original proof and historical target programs remain embargoed.\n')
target.write_text(header+statement+'\n',newline='\n')
print('Statement lines',text[:start].count('\n')+1,'through',text[:end].count('\n')+1)
print('Exact statement lines',len(statement.splitlines()),'SHA256',sha256(statement.encode()).hexdigest())
print('Intake',target.relative_to(ROOT),'SHA256',sha256(target.read_bytes()).hexdigest())
print('No original proof, old packet, historical target program or global progress mutation.')
