"""Retain the complete Part 4 text with explicit statement metadata.

This assembler preserves mathematical material and records only review
events actually present in sign_events.tsv.  It creates no check event.
"""
from pathlib import Path
import csv,re,json,importlib.util
from fix_verified_legacy_locators import fix_legacy_locators

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT.parents[1]
NIGHT=BASE/'sources/newer_night/checkpoint29'
spec=importlib.util.spec_from_file_location('sign_body',ROOT/'code/build_sign_bodies.py')
mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
rows={r['label']:r for r in mod.ROWS if r['source_run']=='S6_06_BLIND'}

def flatten(path):
    s=path.read_text()
    return re.sub(r'\\input\{([^}]+)\}',lambda m: flatten(NIGHT/m.group(1)),s)

def rewrite(s):
    # These are literal source typography repairs, not mathematical changes.
    s=re.sub(r'(?<![A-Za-z\\])quad\b',r'\\quad',s)
    s=s.replace('the torus-fibration setting of Part 4.2','the standing torus-fibration setting of this section')
    s=s.replace('the setting of Part~4.2','the standing torus-fibration setting of this section')
    s=s.replace(r'\texttt{code/part4/simple\_elliptic\_weighted.py}',
                r'\path{code/part4/}\allowbreak\path{simple_elliptic_weighted.py}')
    # Original statement identifiers remain printable and link to their new
    # canonical label.  The original stmt:* labels remain aliases.
    def stmt(m):
        ident,status,body=m.groups(); label='night:'+ident
        row=rows[label]
        uses='; '.join('\\ref{night:'+x.strip()+'}' for x in row.get('uses','').split(';') if x.strip()) or 'the hypotheses and explicit local calculation stated here'
        if ident=='P4.56':
            uses='; '.join('\\ref{night:'+x+'}' for x in ['P4.55','P4R.7','P4R.9','P4R.19'])
        check='The night-run re-derivation was by GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), 16--18 November 2026. '
        event=mod.EVENTS.get(label)
        if event and event['type']=='D': check+=r'Also checked in this writing by \CurrentChecker. '+mod.tex_escape(event['scope'])
        elif event: check+=r'Current review by \CurrentChecker: '+mod.tex_escape(event['scope'])
        else: check+='Current-writing re-derivation is in progress; the historical re-derivation is retained.'
        source_status=status
        status='open' if status.lower() in ('open','running') else ('refuted' if status.lower().startswith('refuted') else ('proved' if status.lower()=='proved' else status))
        env='refuted' if status=='refuted' else 'proposition'
        return ('\\begin{'+env+'}['+ident+']\\label{'+label+'}\\label{stmt:'+ident+'}\n'
                '\\StatementRecord{'+label+'}{'+status+'}{'+check.rstrip('. ')+'}{'+uses+'}\n'+body+'\\end{'+env+'}')
    s=re.sub(r'\\begin\{statement\}\{([^}]+)\}\{([^}]+)\}(.*?)\\end\{statement\}',stmt,s,flags=re.S)
    return fix_legacy_locators(mod.numbered_proof(s), 'build_sign_night.rewrite')[0]

def main():
    text=('\\section{Irreducible supports: topology, conductor and equality}\n'
          '\\label{sec:II:night-sign}\n'
          'The following proofs retain every Part~4 result of the night run. '
          'The final classification is Theorem~\\ref{night:P4.58}; its exact normalization '
          'maps and its local exclusions are proved below.\n'
          '\\paragraph{Standing torus-fibration setting.} '
          'The ambient space is a smooth compact complex threefold $Y$ with $b_1(Y)=b_2(Y)=0$, '
          'and $f:Y\\to B$ is proper and surjective with connected fibres and smooth general fibre a complex two-torus. '
          'Every statement below concerning an irreducible support uses its actual full fibre $mS$, normalization and resolution. '
          'The global assertions expressly retaining the hypothesis that every support is irreducible or has normal crossings are used with that hypothesis. '
          'Constructions and comparison examples with different Betti numbers state their own assumptions.\n'
          +flatten(NIGHT/'notes/part4.tex')+'\n'
          +flatten(NIGHT/'notes/part4_unibranch.tex'))
    replacement_file=ROOT/'analysis/II_independent_night_replacements.json'
    if replacement_file.exists():
        for record in json.loads(replacement_file.read_text()):
            for change in record['replacements']:
                if text.count(change['old']) != 1:
                    raise ValueError('Night receiving replacement is not unique: '+record['label'])
                text=text.replace(change['old'],change['new'],1)
    for change in json.loads((ROOT/'analysis/sign_night_source_replacements.json').read_text()):
        count=text.count(change['old'])
        if count != change.get('count',1):
            raise ValueError('Source-locator receiving replacement count mismatch: '+change['name']+' '+str(count))
        text=text.replace(change['old'],change['new'])
    (ROOT/'papers/II/body_night.tex').write_text(rewrite(text))
    index=mod.INDEX['S6_06_BLIND:P3K.36']
    src=(BASE/index['file']).read_text()
    text='\\section{The Liu--Rollenske parameter covering}\n'+src[index['start']:index['end']]
    revision=ROOT/'papers/II/revisions/lr_cover.tex'
    receiving=revision.read_text() if revision.exists() else rewrite(text)
    (ROOT/'papers/II/lr_cover.tex').write_text(fix_legacy_locators(receiving, 'build_sign_night.lr_cover')[0])
    print('night source characters:',len(text))

if __name__=='__main__': main()
