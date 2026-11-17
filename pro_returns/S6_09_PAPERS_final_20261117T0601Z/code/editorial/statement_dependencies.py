"""Expose the dependencies already named in each retained proof.

This is an editorial index, not an inferred proof graph or a correctness test.
It neither changes a proof nor promotes a partial argument to a theorem.
"""
from pathlib import Path
import re,json

ENV=r'theorem|lemma|proposition|corollary|claim|statement|remark|question|problem|conjecture|definition|example|test|computed|cited|refuted|openq'
def add_uses(text,paper):
    matches=list(re.finditer(r'\\begin\{('+ENV+r')\}(?:\[[^\]]*\])?.*?\\end\{\1\}',text,re.S))
    records=[]; insertions=[]
    for i,m in enumerate(matches):
        stop=matches[i+1].start() if i+1<len(matches) else len(text)
        after=text[m.end():stop]
        if re.match(r'\s*\\Uses\{',after):continue
        proof=re.search(r'\\begin\{proof\}(?:\[[^\]]*\])?(.*?)\\end\{proof\}',after,re.S)
        if proof: scope=proof[1]
        else:
            # A statement whose complete proof has been moved still names its
            # internal proof location; do not pretend to inspect another block.
            scope=re.split(r'\\(?:sub)*section\b',after,maxsplit=1)[0]
        own=set(re.findall(r'\\label\{([^}]+)\}',m[0]))
        dependencies=[]
        for ref in re.finditer(r'\\(?:ref|eqref|cref|Cref|autoref)\{([^}]+)\}|\\cite\w*(?:\[[^\]]*\])*\{[^}]+\}',m[0]+'\n'+scope):
            token=ref[0]
            if ref[1]:
                keys=[k for k in ref[1].split(',') if k not in own]
                if not keys:continue
                token='\\cref{'+','.join(keys)+'}'
            if token not in dependencies:dependencies.append(token)
        base='the hypotheses, notation and definitions stated here'
        if dependencies: base+='; '+ '; '.join(dependencies)
        elif proof:base+='; the explicit constructions and calculations in the proof'
        else:base+='; the argument and qualifications immediately following'
        insertions.append((m.end(),'\n\\Uses{'+base+'}\n'))
        records.append({'statement_labels':sorted(own),'environment':m[1],
                        'named_dependencies':dependencies,'direct_proof_follows':bool(proof),
                        'scope':'Named references in the statement and its immediately associated retained proof or argument; standing definitions are not an assertion of no other dependency.'})
    for pos,value in reversed(insertions):text=text[:pos]+value+text[pos:]
    out=Path(__file__).resolve().parents[2]
    (out/'records'/f'{paper}_statement_dependencies.json').write_text(json.dumps(records,indent=2)+'\n')
    return text
