#!/usr/bin/env python3
"""A target-only review overlay; it does not edit the shared course source."""
from pathlib import Path
import datetime, hashlib, json, re

BASE = Path(__file__).resolve().parents[2]
W = BASE/'work/maps_audit'
OUT = BASE/'work/cdp_audit/course_residual_locator_review.json'
prior = json.loads((BASE/'work/cdp_audit/course_reference_locator_review.json').read_text())
names = {
 'belt':'belt-sphere-complements-and-the-whitney-disk',
 'pair':'creating-an-original-cancelling-handle-pair',
 'slides':'framed-handle-slides-and-index-one-removal',
 'pt':'framed-manifolds-and-the-pontryagin-thom-map',
 'chains':'integral-handle-chains-and-signed-incidences',
 'recognition':'integral-homology-and-sphere-recognition',
 'cancel':'morse-cancellation-with-controlled-support',
 'trajectory':'morse-trajectories-and-critical-value-lowering',
 'middle':'realizing-framed-handles-and-middle-cancellation',
 'arrangement':'rearranging-the-original-framed-handles',
 'morse':'relative-morse-functions-and-original-handles',
 'zero':'removing-the-original-zero-and-top-handles',
 'twist':'sphere-twists-and-the-original-smooth-six-sphere-comparison',
 'move':'whitney-move-with-controlled-support',
 'receiving':'whitney-moves-in-the-receiving-dimensions',
}
other={
 'frame':'the-original-six-dimensional-framing-invariant',
 'spin':'spin-six-and-the-framing-comparison',
 'ac':'almost-complex-structures-and-integrability',
}
def lab(short,tail): return 'courseIII:'+({**names,**other}[short])+':'+tail
def sec(short,*ns): return [lab(short,'section-'+str(n)) for n in ns]
def cref(ts): return r'\cref{'+','.join(ts)+'}'
def eq(t): return r'\eqref{'+t+'}'
HOMOTOPY='mapsI:course:CG-S6-07-HOMOTOPY'
HOMOLOGY='mapsI:top:cor:candidate-mv-sphere'
plain_input=W/'III_course_residual_plain_number_locators.json'
local_input=W/'III_course_remaining_local_section_reference_candidates.json'
plain=json.loads(plain_input.read_text())
local=json.loads(local_input.read_text())
prior_by_context={(r['file'],r['line']):r for r in prior['rows']}
assigned={x+'.tex' for x in names.values()}
rows=[]

def replace_one(row, old, new, targets, why):
    assert old in row['after'], (row['record_number'],old)
    row['after']=row['after'].replace(old,new,1)
    row['replacements'].append({'before':old,'after':new,'target_labels':targets,'reason':why})

cross = {
 19:[('Sections 5--6',sec('move',5,6))],
 31:[('Sections 5--6',sec('pair',5,6))],
 33:[('Sections 2--3',sec('belt',2,3))],
 40:[('Sections 2--3',sec('trajectory',2,3))],
 49:[('Section 7',sec('chains','3.1'))],
 50:[('Section 9',[HOMOTOPY])],
 51:[('Theorem 7.1',[HOMOLOGY])],
 53:[('Section 6',sec('middle',6))],
 54:[('Section 9',[HOMOTOPY])],
 58:[('Section 9',[HOMOTOPY])],
 59:[('Section 9',[HOMOTOPY])],
 62:[('Sections 1–3',sec('twist',1,2,3))],
 63:[('Section 5',sec('twist',5))],
 65:[('Section 9',[HOMOTOPY])],
 67:[('Theorem 7.1',[HOMOLOGY])],
 105:[('Sections 1--5',sec('trajectory',1,2,3,4,5))],
 107:[('Theorem 2.1',[lab('cancel','morse-cancellation-data')]),('Sections 3--5',sec('cancel',3,4,5))],
 114:[('Section 9',sec('frame',9))],
 118:[('Sections 2--5',sec('middle',2,3,4,5))],
 120:[('Sections 5--6',sec('spin',5,6))],
 181:[('Sections 5--7',sec('belt',5,6,7))],
 182:[('Sections 2-3',sec('belt',2,3))],
 183:[('Section 7.1',sec('belt','7.1'))],
 186:[('Section 2',sec('ac',2))],
 189:[('Sections 3-4',sec('move',3,4))],
 190:[('Sections 2--5',sec('middle',2,3,4,5))],
}

pattern=re.compile(r'\b(Sections?|Theorem|Lemma)\s+(\d+(?:\.\d+)*)(?:\s*(--|–|-)\s*(\d+(?:\.\d+)*))?(?:\s+and\s+(\d+(?:\.\d+)*))?')
preserve_all={75:'External Laudenbach Sections1–3 locator.',76:'The source statement title Theorem2.1, not an operative cross-reference.',78:'External Laudenbach Sections1–2 locator.',86:'External Laudenbach Lemma2 and original-author file/line locator.',99:'External Laudenbach Sections1–3 locator.'}
for i,r in enumerate(plain,1):
    if r['file'] not in assigned: continue
    row={'record_number':i,'file':r['file'],'line':r['line'],'before':r['paragraph'],'after':r['paragraph'],'replacements':[],'status':'read and target-matched in the specified locator scope'}
    p=prior_by_context.get((r['file'],r['line']))
    if p:
        for m in p['mappings']:
            if m.get('suggested_tex') is not None and m['exact_original_phrase'] in row['after']:
                replace_one(row,m['exact_original_phrase'],m['suggested_tex'],m['target_labels'],'Already independently matched in course_reference_locator_review.json: '+m['matched_target_content'])
    if i in preserve_all:
        row['status']='retained external locator or statement title'
        row['retention_reason']=preserve_all[i]
        rows.append(row);continue
    for phrase,targets in cross.get(i,[]):
        replace_one(row,phrase,cref(targets),targets,'Explicit companion or cross-Paper-I reference, matched against the named receiving target and its operative content.')
    if i==53:
        replace_one(row,'Its exact map (6.8)','Its exact map '+eq(lab('middle','eq:6.8')),[lab('middle','eq:6.8')],'The full product diffeomorphism and inverse are the actual middle-cancellation equation6.8, opened lines715–727.')
    if i==60:
        ts=sec('frame',8,9)
        replace_one(row,"The latter's Sections 8–9",cref(ts),ts,'The framed-bordism invariance and original nullbordism are in the geometric-framing chapter, not sphere-twists sections8–9 (there is no sphere-twists section9).')
    if i==66:
        t=lab('recognition','eq:11.5')
        replace_one(row,'the degree-two row of Section 3','the degree-two row displayed in '+eq(t),[t],'The same complete row (s,-s,s), s=sum b_i-a is printed in the retained exercise solution; Paper I also prints it in the proof of p0-integral-specialization, lines28522–28541. Use its exact local displayed label.')
    if i==119:
        replace_one(row,'the actual compact smooth manifold of lesson 7','the constructed compact smooth manifold',[],'Remove the obsolete source-lesson designation, retaining the same X.')
        replace_one(row,'Section 9 of that lesson',cref([HOMOTOPY]),[HOMOTOPY],'The specified degree-one map and its actual inverse homotopies are retained in Paper I under this exact theorem label.')
    # The remaining operative locators in these fully screened paragraphs are
    # local. External occurrences inside a mixed paragraph are excluded below.
    skip_phrases={'Sections 1--3'} if i==110 else set()
    for m in list(pattern.finditer(row['after'])):
        phrase=m.group(0)
        if phrase in skip_phrases: continue
        kind,a,dash,b,c=m.groups()
        if kind in ('Theorem','Lemma'):
            assert i in (77,80) and phrase=='Theorem 2.1',(i,phrase)
            ts=[lab('cancel','morse-cancellation-data')]
        else:
            nums=[a]
            if b:
                if '.' not in a and '.' not in b:
                    nums=[str(z) for z in range(int(a),int(b)+1)]
                else: nums=[a,b]
            if c: nums.append(c)
            ts=['courseIII:'+r['file'][:-4]+':section-'+z for z in nums]
        replace_one(row,phrase,cref(ts),ts,'Local operative reference: the paragraph context and actual same-chapter target heading/content were matched; no companion namespace is implied here.')
    if i==110: row['retained_external_locator']='Laudenbach Sections1–3 remains a published-source locator.'
    rows.append(row)

local_rows=[]
for i,r in enumerate(local,1):
    if r['file'] not in assigned:continue
    row={'record_number':i,'file':r['file'],'line':r['line'],'before':r['paragraph'],'after':r['paragraph'],'replacements':[],'status':'Existing local section reference matches the actual local construction'}
    if i==19:
        old=r'The connected-intersection van Kampen lemma, proved in lesson 6, \cref{courseIII:framed-handle-slides-and-index-one-removal:section-3}'
        target=lab('slides','section-1')
        new='The connected-intersection case of the path-class gluing argument in '+cref([target])
        replace_one(row,old,new,[target],'The local section3 is a belt crossing. The actual subdivision/triangle gluing proof is in local section1, lines41–47: with one overlap basepoint its overlap loop relations yield the normal-closure quotient used here.')
        row['status']='Concrete wrong namespace corrected in the suggested overlay'
    if i==28:
        old=r'\cref{courseIII:framed-manifolds-and-the-pontryagin-thom-map:section-1}'
        target=lab('morse','section-1')
        replace_one(row,old,cref([target]),[target],'The explicitly named relative Morse/Sard provider is relative-morse section1, lines68–88. PT section1 is the original embedding, so its namespace is wrong here.')
        row['status']='Concrete wrong namespace corrected in the suggested overlay'
    row['checked_local_section_labels']=re.findall(r'\\(?:c|C)?ref\{([^}]*:section-[^}]*)\}',row['after'])
    row['scope']='Read the entire candidate paragraph and matched its named construction to the actual target section. This does not reassert a new complete proof audit.'
    local_rows.append(row)

labels=set()
for r in rows+local_rows:
    for v in r['replacements']: labels.update(v['target_labels'])
    for s in r.get('checked_local_section_labels',[]):labels.update(s.split(','))
evidence={}
for t in sorted(labels):
    f=BASE/'S6_09_PAPERS_I.tex' if t.startswith('mapsI:') else BASE/'editorial/III_course'/(t.split(':',2)[1]+'.tex')
    ls=f.read_text().splitlines();needle=r'\label{'+t+'}';found=[i for i,l in enumerate(ls) if needle in l]
    assert len(found)==1,(t,found)
    i=found[0];a=max(0,i-4);b=min(len(ls),i+18)
    evidence[t]={'file':str(f.relative_to(BASE)),'label_line':i+1,'excerpt_lines':[a+1,b],'text':'\n'.join(ls[a:b]),'file_sha256':hashlib.sha256(f.read_bytes()).hexdigest()}
changes=[]
for group,rs in [('plain',rows),('local',local_rows)]:
    for r in rs:
        if r['before']!=r['after']:
            changes.append({'id':f'cdp-course-{group}-{r["record_number"]:03d}','source_tex':r['file'],'converted_line_before':r['line'],'before':r['before'],'after':r['after'],'reason':'Independent target-only locator review; complete source argument retained.','replacements':r['replacements']})
d={'reader':'GPT-6 Astra (OpenAI, ChatGPT Pro mode)','effort':'Pro','date':'2026-11-17','timestamp_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'scope':'All114 assigned plain-locator paragraphs and41 remaining-local-reference paragraphs were read. Named targets, section openings and operative equations were matched at the recorded scope. This is a reference-identity audit, not a second mathematical proof audit. Actual external published-source locators and original statement titles are preserved.',
 'inputs':[{'file':str(f.relative_to(BASE)),'sha256':hashlib.sha256(f.read_bytes()).hexdigest()} for f in (plain_input,local_input)],
 'plain_rows':rows,'local_reference_rows':local_rows,'target_evidence':evidence,'changes':changes,
 'counts':{'plain_rows':len(rows),'local_reference_rows':len(local_rows),'changed_paragraphs':len(changes),'target_labels':len(labels)},
 'manuscripts_or_converter_modified_by_reviewer':False,
 'notable_outcomes':['Zero/top removal has two distinct eq1.2 targets; that correction is already recorded in the preceding raw54 review.','Remaining-local candidate19: connected-intersection gluing must cite the local section1 subdivision proof, not belt-crossing section3.','Remaining-local candidate28: the named relative-Morse/Sard construction must use the relative-morse section1 namespace, not PT section1.','Recognition source Section9 references use the actual Paper I degree-one homotopy theorem; source Theorem7.1 references use the exact printed integral-homology conclusion.','The framed-bordism Sections8–9 in recognition refer to the geometric-framing chapter, not the immediately preceding sphere-twists chapter.']}
OUT.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'path':str(OUT),'counts':d['counts']},indent=2))
