"""Print the complete III concordance and exact producer-date appendix."""
from pathlib import Path
import csv,json,re
D=Path(__file__).resolve().parents[2];ROOT=D.parent
with (D/'S6_09_PAPERS_inventory.csv').open() as f:rows=[r for r in csv.DictReader(f) if r['paper']=='III']
s=(D/'S6_09_PAPERS_III.tex').read_text();labels=set(re.findall(r'\\label\{([^}]+)\}',s))
def esc(x):
    return ''.join({'&':r'\&','%':r'\%','#':r'\#','_':r'\_\allowbreak ','$':r'\$','{':r'\{','}':r'\}','~':r'\textasciitilde{}','^':r'\textasciicircum{}','\\':r'\textbackslash{}',',':r',\allowbreak{}'}.get(c,c) for c in str(x))
def path(x):return r'\path{'+str(x).replace(' ',r'}\ \path{')+'}'
short={'S6_04_MAPS_MANIFOLDS':'MAPS','S6_02_PUSH':'PUSH','S6_02_FAMILY':'FAM','working_edition':'WB','course_CG-S6':'CG--S6','WORKING_EDITION_COURSE_PROVIDER':'Provider','working_edition_reader_extension':'Reader extension','WRITING_REPAIR':'Writing repair'}
def credit_scope(r):
    if r['source_run'] in {'WORKING_EDITION_COURSE_PROVIDER','course_CG-S6'}:
        return 'Classical construction or receiving derivation; its original sources and exact application hypotheses are credited in the full proof. Complete source-unit and dependency comparisons are recorded for this label.'
    out=[]
    for field,src in [('found_in_AC26','AC26'),('found_in_E26','E26'),('found_in_DGKX_v1','DGKXv1'),('found_elsewhere','Other literature')]:
        try:o=json.loads(r[field])
        except Exception:
            if field=='found_elsewhere' and r[field]:out.append('Other literature: '+r[field])
            continue
        if not isinstance(o,dict):continue
        status=o.get('status','')
        if status.startswith('not_found'):out.append(src+': no full match in the recorded search');continue
        if 'found' not in status and not o.get('matches'):continue
        relation='known conclusion' if o.get('full_statement_found') or o.get('known_result_rederived') else 'antecedent or classical input'
        ms=o.get('matches',[])
        if ms:
            locs=[]
            for m in ms:
                if not isinstance(m,dict):continue
                locs.append(' '.join(str(m.get(k,'')) for k in ['citation_key','locator']).strip())
            locator='; '.join(dict.fromkeys(locs))
        else:locator=o.get('locator','')
        if not locator and field=='found_elsewhere':
            locator=', '.join(dict.fromkeys(str(x.get('citation_key','')) for x in o.get('sources_checked',[]) if isinstance(x,dict) and x.get('citation_key')))
        out.append(src+': '+relation+(' ('+locator+')' if locator else ''))
    return '; '.join(out) if out else r['credited_to']

out=r'''% BEGIN GENERATED RESULT INDEX
\section{Complete result and source concordance}\label{app:III:result-index}
Every source result assigned to this paper appears below. The printed number
locates the complete statement and proof; no proof is replaced by this
index. Shared statements are printed once, with all distinct arguments and
the expanded working-edition derivations retained. The companion inventory
contains the complete source file, actual statement, wording changes,
historical reading scope, current proof check, and the full credit search.

The baseline comparisons are with the controlling original manuscript of
\citet{AC26}, \citet{E26}, and the separately identified versions of
\citet{DuEtAl2026v1} and \citet{DuEtAl2026v2}. A negative entry means only that the
complete receiving conclusion was not found in the recorded term searches
and opened contexts. An antecedent entry credits the stated construction
or source theorem without attributing an additional marked calculation to
that source. Known conclusions and all their re-derivations are in the
credited appendices. The exact ordinary-filling questions of
\cref{maps:src:D.2.4} are in the separate final part.

The current independent readings, derivations, source-hypothesis matches
and reruns are by GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro),
17 November 2026. Historical checks by Claude Fable 5.2 (Anthropic),
effort high or effort max, and Claude Opus 5.5 (Anthropic), effort max,
12--16 November 2026, retain their recorded scopes. A producing run's
self-check is provenance, not an independent reading.

\begingroup\small
\begin{longtable}{@{}p{42mm}p{18mm}p{88mm}@{}}
\toprule Source result & Printed number & Kind and source comparison\\\midrule
\endfirsthead
\toprule Source result & Printed number & Kind and source comparison\\\midrule
\endhead
'''
missing=[]
for r in rows:
    lab=r['printed_label']
    if lab not in labels:missing.append((r['source_run'],r['source_id'],lab))
    out+=path(short.get(r['source_run'],r['source_run'])+' '+r['source_id'])+' & '+r'\ref{'+lab+'} & '+esc(r['kind'])+r'\par '+esc(credit_scope(r))+r'\\'+'\n'
out+=r'\bottomrule\end{longtable}\endgroup'+'\n% END GENERATED RESULT INDEX\n'
(D/'editorial/III_result_index.tex').write_text(out)
(D/'records/III_index_missing.json').write_text(json.dumps(missing,indent=2)+'\n')

manifest=json.loads((D/'work/maps_audit/III_course_conversion_manifest.json').read_text())
producer=[]
for r in manifest:
    p=ROOT/r['source'];lines=p.read_text().splitlines()
    candidates=[x for x in lines if re.search(r'GPT[-–]|Written by|Proof companion.*2026',x)]
    head=' '.join(candidates[:2])
    dates=re.findall(r'(?:(?:\d{1,2}[–-])?\d{1,2} October 2026|October 2026)',head)
    date=dates[0] if dates else 'October2026; no exact day in the source header'
    model='GPT-6 Astra (OpenAI), Codex reasoning effort ultra'
    if 'GPT-6.1 Sol' in head and 'GPT-6 Astra' in head:model+='; retained provider text by GPT-6.1 Sol (OpenAI), reasoning effort ultra'
    elif 'GPT-6.1 Sol' in head:model='GPT-6.1 Sol (OpenAI), reasoning effort ultra'
    if not head:
        model='GPT-6 Astra (OpenAI), Codex reasoning effort ultra; course attribution'
        date='October2026; no day recorded in this chapter header'
    item={'source':r['source'],'title':r['title'],'range':r['range'],'producer':model,'date_as_recorded':date,'raw_source_metadata':candidates[:2]}
    producer.append(item)
out=r'''% BEGIN GENERATED PROVENANCE INDEX
\section{Source editions and exact production records}\label{app:III:provenance}
The working edition was produced by GPT-5.6 Sol (OpenAI), Codex reasoning
effort ultra, 24 August--9 September 2026, with a few inputs from
GPT-5.6 Sol (OpenAI, ChatGPT Pro mode), 24 August--9 September 2026.
The research runs were produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode,
effort Pro), 12--16 November 2026. The current independent writing and
checking is by GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro),
17 November 2026. These are production and reading records, not date
comparisons between mathematical results.

The complete classical and course arguments below retain their recorded
producer dates. ``October 2026'' is a month-level record; it does not
silently supply an unrecorded day. The label concordance identifies all
249 receiving units within these 33 complete source ranges. Mathematical
setup following a producer line was retained in the proof. Missing image
assets are explicitly described, with all captions, alternative text,
anchors and adjacent coordinate calculations retained; no unseen image is
reported as inspected.

\begingroup\small
\begin{longtable}{@{}p{61mm}p{87mm}@{}}
\toprule Complete source range & Producer, effort and recorded date\\\midrule
\endfirsthead
\toprule Complete source range & Producer, effort and recorded date\\\midrule
\endhead
'''
for r in producer:
    out+=esc(r['title'])+r'\par '+esc('Source lines '+str(r['range'][0])+'–'+str(r['range'][1]))+' & '+esc(r['producer']+', '+r['date_as_recorded'])+r'\\'+'\n'
out+=r'\bottomrule\end{longtable}\endgroup'+'\n% END GENERATED PROVENANCE INDEX\n'
(D/'editorial/III_provenance.tex').write_text(out)
(D/'records/III_producer_concordance.json').write_text(json.dumps(producer,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'result_rows':len(rows),'unplaced':len(missing),'complete_source_ranges':len(producer)}))
