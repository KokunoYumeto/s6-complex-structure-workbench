from S6_SERIES_PUBLISH_c3_edit import *
import re
folder=ROOT/'agents/continuation3_provenance/next_part';fragment=folder/'S6_SERIES_PUBLISH_next_part_proposed.tex'
s=SOURCE.read_text();start=r'\section{Connected deformation chains and two independent periods}\hypertarget{tag-034G}{}\label{sec:II:push-stability}';end=r'\section{Analytic duality and the exact Picard restriction maps}'
assert s.count(start)==s.count(end)==1
a,z=s.index(start),s.index(end);old=s[a:z];new=fragment.read_text();after=s[:a]+new+s[z:]
def statement(text,label):
 at=text.index('\\label{'+label+'}',text.find('\\begin{document}')+1 if '\\begin{document}' in text else 0)
 first=text.rfind('\\begin{',0,at);kind=re.match(r'\\begin\{([^}]+)\}',text[first:])[1]
 last=text.index('\\end{'+kind+'}',at)+len('\\end{'+kind+'}')
 return text[first:last]
for label in ['push:src:E.5.2','push:src:E.5.3','push:src:E.2.4']:
 assert statement(s,label)==statement(after,label),label
 print('Complete original statement preserved:',label)
preserve_identifiers(s,after)
for previous,current in zip(identifiers(s),identifiers(after)):
 for name,count in previous.items():assert current[name]==count,name
SOURCE.write_text(after,newline='\n')
for name,target,key in [('S6_SERIES_PUBLISH_next_defects.tsv','S6_SERIES_PUBLISH_defects_II.tsv','change_id'),('S6_SERIES_PUBLISH_next_CHECK_EVENTS.tsv','CHECK_EVENTS.tsv','event_id')]:
 _,rows=read_tsv(folder/name);print(name,append_rows(ROOT/target,rows,key))
path=ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv';fields,progress=read_tsv(path)
oldunits={'push:src:E.5.1','sec:II:combs','sec:II:uniform-nontorsion'}
selected=[r for r in progress if r['paper']=='II' and r['unit_id'] in oldunits];assert len(selected)==78
progress=[r for r in progress if not(r['paper']=='II' and r['unit_id'] in oldunits)]
# The former large pre-subsection prefix receives explicit section units now; their creation earns no movement credit.
titles={m[2]:m[1] for m in re.finditer(r'\\section\{([^\n]+?)\}\\hypertarget\{[^}]+\}\{\}\\label\{([^}]+)\}',new)}
_,incoming=read_tsv(folder/'S6_SERIES_PUBLISH_next_unit_status.tsv');assert len(incoming)==200
for item in incoming:
 criterion=item['type'];status='open' if criterion in ['D14','D15','D23','D24'] else 'done'
 detail=item['evidence']+' Complete original and receiving proofs read by the exposed provenance agent; no independent credit. New unit creation or subdivision earns no movement credit.'
 progress.append(dict(paper='II',unit_id=item['unit'],unit_title=titles[item['unit']],row_kind='defect',defect_type=criterion,status=status,date_utc=now(),evidence='CHECK_EVENTS.tsv; '+str((folder/'S6_SERIES_PUBLISH_next_comparison.md').relative_to(ROOT)),detail=detail))
for unit,title in titles.items():
 progress.append(dict(paper='II',unit_id=unit,unit_title=title,row_kind='structure',defect_type='',status='open',date_utc=now(),evidence=str(fragment.relative_to(ROOT)),detail='Local prerequisite order is compared; whole-paper placement and front-matter synchronization remain open. No subdivision or unit-creation movement credit.'))
write_tsv(path,fields,progress)
add_event('sec:II:push-stability; sec:II:critical-fibre-extension; sec:II:normal-crossing-cusps; sec:II:analytic-cusp-identification; sec:II:connected-deformation-chains; sec:II:two-independent-periods; sec:II:combs; sec:II:uniform-nontorsion',
 'II-C3-ROOT-NEXT-PART-ADMISSION','used and rechecked in this run',
 'Imported the exposed provenance agent complete original/receiving comparisons for all31 owners and applications; their exact source loci and reading limits remain in the proposal records. Root read the complete comparison report, every line of the receiving two-period and uniform-nontorsion sections, the complete retained E.2.4 statement/proof and the extracted comb-kernel definition with its receiving use. Root checked the local parameter/logarithmic inverse, fixed marking and ell vector, monodromy centralizer/norm maps, full-fibre Picard parameter scalar inverse, and component-stabilizer root character. The complete protected E.5.2 and E.5.3 statements and the legacy E.2.4 statement compare byte-for-byte with the pre-admission source. All old labels/targets retain their multiplicity.227 defect rows and31 exposed events admitted; local unit statuses preserve D10/D16 and leave final placement, front matter, build/page reading open. Root does not claim an additional full reading of all4814 receiving lines or independent proof credit.',
 'S6_SERIES_PUBLISH_II.tex: canonical pencils through uniform non-torsion',source='code/S6_SERIES_PUBLISH_c3_next_part_admit.py')
print('Admitted eight bounded mathematical sections; protected statements unchanged.')
