"""Stage the tested display-label writer and remove unused production macros."""
from datetime import datetime, timezone
import re
import S6_SERIES_PUBLISH_c8_integrate_units as u
import S6_SERIES_PUBLISH_c8_root_units as r

path=u.WORK/'root/preamble.tex'
before=path.read_text()
after=before
source=u.repairs.SOURCE.read_text()
assert source.startswith(before)
body=source[len(before):]
df,ds=r.table(r.DEFECTS)
changes=[]
def replace(suffix,kind,old,new,reason):
    global after
    assert after.count(old)==1,(suffix,after.count(old))
    after=after.replace(old,new,1)
    changes.append((suffix,kind,old,new,reason))

proposal=(u.ROOT/'code/S6_SERIES_PUBLISH_c8_tex_alias_proposal.tex').read_text()
block=proposal[proposal.index('\\makeatletter'):]
anchor='\\usepackage[nameinlink,noabbrev]{cleveref}\n'
replace('DISPLAY-ALIASES','D19',anchor,anchor+block+'\n',
 'The actual unpatched equation/align/LV tests drop earlier literal labels. Embed the exact tested deferred AMS queue: each alias uses the same saved cleveref/hyperref writer, number and live target at the existing row flush. The complete diagnostic review, stable third pass, aux equality and all PDF destinations were read. No mathematical display or literal identity is changed.')

workflow=r'''\newcommand{\Uses}[1]{\par\smallskip\noindent\textit{Uses:} #1.\par\smallskip}
\newcommand{\Verified}{}\newcommand{\AuthorSelfCheck}{}\newcommand{\NeedsCheck}{}\newcommand{\Open}{\textbf{Open.}\ }

\newcommand{\RungZero}[1]{\par\noindent\textbf{Result and mechanism.} #1\par\smallskip}
\newcommand{\RungOne}{\par\Needspace{6\baselineskip}\noindent\textbf{Proof at the first rung.}\par\nobreak\smallskip}
\newcommand{\CurrentChecker}{GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), 18 November 2026}
'''
for name in ('Uses','Verified','AuthorSelfCheck','NeedsCheck','Open','RungZero','RungOne','CurrentChecker'):
    assert not re.search(r'\\'+name+r'(?![A-Za-z])',body),name
replace('WORKFLOW-MACROS','D07',workflow,'',
 'These production/status macros have no body uses. Remove them, including the obsolete checker/effort string; the actual model/date/effort provenance belongs to the reviewed methodology.')

unused=r'''\newcommand{\StatementRecord}[4]{{\normalfont\scriptsize tag #3}\par}
\newcommand{\ExternalPaperRef}[3]{#1#2 (Paper~#3)}
\newcommand{\CompendiumRef}[2]{\ifmmode\text{\upshape S6\_09, Paper~#1, label~\nolinkurl{#2}}\else S6\_09, Paper~#1, label~\nolinkurl{#2}\fi}
'''
for name in ('ExternalPaperRef','CompendiumRef'):
    assert not re.search(r'\\'+name+r'(?![A-Za-z])',body),name
replace('OBSOLETE-REFERENCE-MACROS','D04',unused,'',
 'Remove the unused compendium/old-reference fallbacks and the production statement header macro. Canonical application is paired with the complete frontmatter rewrite, whose A–G statements print literal small tags; every permanent label and target remains.')

anchor='\\crefname{maintheorem}{theorem}{theorems}\n'
records=r'''\newcommand{\SsixPublishRecords}{https://github.com/KokunoYumeto/s6-complex-structure-workbench/blob/main/RECORDS.md\#paper-iii}
\newcommand{\SsixRepositoryCommit}{a02f2eacf5a8c3db7cf8cdfcdba50c0002ee91c7}
'''
assert 'SsixPublishRecords' not in after and 'SsixRepositoryCommit' not in after
replace('RECORDS-MACROS','D15',anchor,anchor+records,
 'Define the sole prescribed Paper III repository address and commit. Their sole printed uses belong to §1.5 of the complete frontmatter; programs remain plain paths in the final table.')

backlines=[line for line in after.splitlines(keepends=True) if line.startswith('\\expandafter\\def\\csname SBack@')]
assert backlines and 'SBack@' not in body
old=''.join(backlines)
assert after.count(old)==1
replace('UNUSED-BACKLINKS','D07',old,'',
 'Remove the unused generated production back-link definitions. Their introduction step destinations and all actual labels/targets remain unchanged; source check records retain the historical dependencies.')
u.check_permanent_identifiers(before,after)
for suffix,kind,old,new,reason in changes:
    ident='III-C8-PREAMBLE-'+suffix
    assert not any(x['change_id']==ident for x in ds)
    ds.append(dict(change_id=ident,type=kind,statement_id='preamble:III',
      old_location='Paper III preamble before final publication integration',old_page='source preamble',
      new_location='same self-contained preamble',new_page='pending final PDF',old_text=old,new_text=new,reason=reason,
      review_status='exact staged source change; tested alias block and all contexts read; apply with reviewed frontmatter, final full build remains open'))
path.write_text(after,encoding='utf-8',newline='\n')
r.write_table(r.DEFECTS,df,ds)
print('UTC',datetime.now(timezone.utc).isoformat())
print('EXACT_PREAMBLE_EDITS',len(changes),'UNCHANGED_OLD_IDENTITIES')
print('STAGED_ONLY; APPLY_WITH_COMPLETE_FRONTMATTER; FINAL_PDF_GATES_OPEN')
