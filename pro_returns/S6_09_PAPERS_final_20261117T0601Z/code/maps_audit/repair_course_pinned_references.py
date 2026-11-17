"""Build an exact, auditable post-conversion reference correction ledger.

Only references and source-availability sentences change. Original course files
and converted files remain untouched. The assembler may call transform().
"""
from pathlib import Path
import json,re,hashlib
D=Path(__file__).resolve().parents[2]
W=D/'work/maps_audit'; C=D/'editorial/III_course'
LEDGER=W/'III_course_common_reference_repairs.json'
META={'reader':'GPT-6 Astra (OpenAI, ChatGPT Pro mode)','effort':'Pro','date':'2026-11-17'}

def transform(text, filename):
    records=json.loads(LEDGER.read_text())['changes']
    for r in records:
        if Path(filename).name!=r['source_tex']: continue
        if r['before'] in text:
            assert text.count(r['before'])==1,(filename,r['id'],'ambiguous')
            text=text.replace(r['before'],r['after'],1)
        elif r['after'] not in text:
            raise AssertionError((filename,r['id'],'neither original nor replacement found'))
    return text

def build():
    current={p.name:p.read_text() for p in C.glob('*.tex')}
    originals=dict(current); changes=[];provenance_moves=[]
    linkmap=json.loads((W/'III_course_link_map.json').read_text())
    def lab(name,kind='section'):
        return 'courseIII:'+name+':'+kind
    def cref(*ls):return r'\cref{'+','.join(ls)+'}'
    def eq(name,num):return r'\eqref{'+lab(name,'eq:'+num)+'}'
    def change(file,needle,fn,reason):
        file=file+'.tex' if not file.endswith('.tex') else file
        lines=current[file].splitlines()
        hits=[i for i,l in enumerate(lines) if needle in l]
        assert len(hits)==1,(file,needle,hits)
        i=hits[0]; old=lines[i]; new=fn(old)
        assert new!=old,(file,needle,'no change')
        lines[i]=new;current[file]='\n'.join(lines)+'\n'
        changes.append({'id':f'course-ref-{len(changes)+1:03d}','source_tex':file,'converted_line_before':i+1,'before':old,'after':new,'reason':reason})
    def subst(file,needle,repls,reason='Correct the namespace of an explicitly named companion reference; the actual target statement/formula was matched.'):
        def f(s):
            for a,b in repls:
                assert a in s,(file,needle,a)
                s=s.replace(a,b)
            return s
        change(file,needle,f,reason)
    def brace(s,start):
        assert s[start]=='{'
        dep=0
        for i in range(start,len(s)):
            if s[i]=='{' and (i==0 or s[i-1]!='\\'):dep+=1
            if s[i]=='}' and (i==0 or s[i-1]!='\\'):
                dep-=1
                if dep==0:return s[start+1:i],i+1
        raise ValueError('unbalanced href')
    pinned=[]
    def hrefs(line,file):
        pos=0;out=''
        while True:
            i=line.find(r'\href{https://github.com/KokunoYumeto/open-math-courses/',pos)
            if i<0:return out+line[pos:]
            url,end=brace(line,i+5);caption,end2=brace(line,end)
            path=url.split('/src/',1)[1].replace(r'\#','#');name=path.split('#')[0];stem=name[:-3]
            target=linkmap.get(path) or linkmap.get(name)
            assert target,(file,path)
            # The historical Thom source is split between Paper I (1--4)
            # and Paper III (5--8); resolve its actual mathematical use.
            if stem=='thom-euler-for-lesson11':
                if file.startswith('the-adams-tower-and-exact'):
                    target='mapsI:chain:lemma:1.1';replacement='signed-prism proof ('+cref(target)+')'
                elif file.startswith('the-original-integral'):
                    target='mapsI:chain:lemma:4.1';replacement='product-chain comparison and universal-coefficient theorem ('+cref(target,lab(stem,'CG-S6-CHAIN-THEOREM-5.2'))+')'
                else:
                    target='mapsI:chain:lemma:4.1';replacement='full shuffle and front/back comparison ('+cref(target)+')'
            elif stem=='cw-models-and-the-first-hurewicz-map':
                target='mapsI:cw:hurewicz-theorem-result' if '#hurewicz' in path else 'mapsI:cw:section'
                caption=re.sub(r',?\s*\\cref\{[^}]+\}','',caption)
                replacement=caption+' ('+cref(target)+')'
            elif stem=='path-fibres-and-integral-homotopy-equivalences':
                target='mapsI:pf:path-lifting' if not '#' in path else 'mapsI:pf:serre-homology'
                caption=re.sub(r',?\s*Sections 1--5','',caption)
                refs=['mapsI:pf:path-lifting','mapsI:pf:filtered-chains','mapsI:pf:serre-homology','mapsI:pf:integral-comparison'] if '#' in path else [target]
                replacement=caption+' ('+cref(*refs)+')'
            else:
                # Embedded section labels are references to the linked file,
                # not the receiving chapter with an accidentally equal number.
                replacement=re.sub(r'\\cref\{courseIII:[^}]+:section-([^}]+)\}',lambda m:cref(lab(stem,'section-'+m[1])),caption)
                def sections(m):
                    lo=int(m[1]);hi=int(m[2] or lo)
                    return cref(*(lab(stem,'section-'+str(j)) for j in range(lo,hi+1)))
                replacement=re.sub(r'(?i)Sections? (\d+)(?:--(\d+))?',sections,replacement)
                if r'\cref{' not in replacement:replacement+=' ('+cref(target)+')'
            pinned.append({'source_tex':file,'original_url':url,'original_caption':caption,'target_label':target,'replacement':replacement})
            out+=line[pos:i]+replacement;pos=end2
    for file,text in list(current.items()):
        for old in text.splitlines():
            if r'\href{https://github.com/KokunoYumeto/open-math-courses/' in old:
                change(file,old,lambda s,f=file:hrefs(s,f),'Replace the pinned external course pointer by the fully printed, content-matched prerequisite and its actual labels; retain all descriptive mathematical text.')
    ad='the-adams-tower-and-exact-inverse-limits';ar='the-original-adams-tower-and-arithmetic-completion';cb='the-degree-six-milnor-cobar-calculation';co='coefficient-rings-and-the-original-degree-six-class';st='the-original-integral-stable-group-and-its-completion-maps';d8='the-actual-mod-two-cooperation-comparison-through-degree-eight';res='the-actual-mod-two-adams-resolution-and-cooperation-maps';pt='framed-manifolds-and-the-pontryagin-thom-map';odd='the-original-odd-prime-cooperations-and-degree-six-adams-calculation'
    subst(co,'Apply the complete all-length',[(eq(co,'1.8'),eq(cb,'1.8')),('Sections 2--5',cref(*(lab(cb,'section-'+str(i)) for i in range(2,6))))])
    change(co,'The cited proof is available in the private repository',lambda s:'The full proof in '+cref(*(lab(cb,'section-'+str(i)) for i in range(2,6)))+r' covers every length \(f\), not a finite truncation.','Replace the private-source availability sentence by the full printed all-length proof; retain the all-length mathematical assertion.')
    subst(ad,'Use the original Hopf algebra', [('Its Sections 2--5',cref(*(lab(cb,'section-'+str(i)) for i in range(2,6))))])
    subst(ad,'Such a bundle has the disk homotopy-lifting', [(', Section 1.', '.'),('the cited (1.13)',r'\eqref{mapsI:pf:eq:1.13}')])
    subst(ad,'Apply the signed prism from', [(', '+cref(lab(ad,'section-1')), '')])
    subst(res,'All these are the actual objects constructed', [('Sections 1 and 8--11',cref(lab(ad,'section-1'),*(lab(ad,'section-'+str(i)) for i in range(8,12))))])
    subst(res,'We first construct the multiplication',[(eq(res,'3.2'),eq(ar,'3.2')),(eq(res,'3.3'),eq(ar,'3.3'))])
    subst(st,'The same prerequisite proofs have pinned external copies:', [('The same prerequisite proofs have pinned external copies:','The full prerequisite proofs are printed here:'),(' Their local navigation links above remain usable offline.','')])
    subst(st,'The receiving completed groups are proved',[(cref(lab(st,'section-8')),cref(lab(d8,'section-8'))),('Sections 5--6',cref(lab(odd,'section-5'),lab(odd,'section-6'))),(eq(st,'5.8'),eq(ar,'5.8')),(cref(lab(st,'section-7')),cref(lab(ar,'section-7'))),(' These pinned GitHub links belong to the private course repository and require access. The complete sources are also in the offline edition.','')])
    subst(d8,'The included prerequisites are pinned to', [('The included prerequisites are pinned to the verified course edition:','The complete prerequisite proofs are printed in the following places:'),(' The full proofs remain in the course sources and offline readers.','')])
    # Clear companion references affected by the same local-number conversion.
    def move(file,needle,target,kind,numbers):
        subst(file,needle,[(lab(file,kind+':'+n),lab(target,kind+':'+n)) for n in numbers])
    move(st,'This chapter supplies the integral receiving',pt,'eq',['8.1','8.2'])
    move(st,'Faces and degeneracies pull back',ad,'eq',['8.1','8.4','8.7','8.9'])
    subst(st,'Faces and degeneracies pull back',[('Sections 8--9 of the included Adams-tower chapter',cref(lab(ad,'section-8'),lab(ad,'section-9'))),('The quotient-bundle proof (9.1)--(9.4)','The quotient-bundle proof '+eq(ad,'9.1')+'--'+eq(ad,'9.4'))])
    subst(st,'Its internal face and multiplication identities',[(cref(lab(st,'section-2'))+' of the actual degree-eight companion',cref(lab(d8,'section-2'))),(cref(lab(st,'section-4'))+' of the Thom/Euler companion',cref('mapsI:chain:lemma:4.1'))])
    subst(st,'The finite filtered-chain convergence proved',[(cref(lab(st,'section-2'))+' of the path-fibre companion',cref('mapsI:pf:filtered-chains'))])
    subst(st,'The realization argument of the Adams companion',[(cref(lab(st,'section-9')),cref(lab(ad,'section-9')))])
    subst(st,'Apply the proved integral fibration spectral sequence',[(cref(lab(st,'section-3')),cref('mapsI:pf:serre-homology'))])
    subst(st,'No CW hypothesis on',[(eq(st,'1.1'),r'\eqref{mapsI:pf:eq:1.1}'),(eq(st,'1.3'),r'\eqref{mapsI:pf:eq:1.3}')])
    subst(st,'The bottom edge proved in the path-fibre companion',[('(3.10)',r'\eqref{mapsI:pf:eq:3.10}')])
    move(st,'Fix \\(m\\geq3\\)',pt,'eq',['8.1','8.2'])
    subst(st,'The finite-group difference-map proof',[(cref(lab(st,'section-2'))+' of the Adams companion',cref(lab(ad,'section-2')))])
    move(st,'These are the actual completion spectra',ar,'eq',['5.8'])
    subst(d8,'The CW realization argument in the Adams-tower companion',[(cref(lab(d8,'section-9')),cref(lab(ad,'section-9')))])
    subst(d8,'The middle realization is contractible.',[(cref(lab(d8,'section-9')),cref(lab(ad,'section-9')))])
    move(d8,'Their adjoint loops have the same connecting value',ad,'eq',['9.6'])
    subst(d8,'its iterated desuspension sign',[('equation (11.2a) of the Adams-tower chapter',eq(ad,'11.2a'))])
    subst(ad,'Apply the full fibration filtration',[(cref(lab(ad,'section-3')),cref('mapsI:pf:serre-homology'))])
    subst(ad,'so the all-page argument of the path-fibre companion',[(cref(lab(ad,'section-2')),cref('mapsI:pf:filtered-chains'))])
    subst(ad,'Its chain maps, including all shuffle terms',[(cref(lab(ad,'section-4')),cref('mapsI:chain:lemma:4.1'))])
    # Remaining geometric companions: exact theorem/section text checked against
    # the already fully read provider chapters.
    sp='sphere-twists-and-the-original-smooth-six-sphere-comparison';fr='the-original-six-dimensional-framing-invariant';wh='whitney-moves-in-the-receiving-dimensions';mid='realizing-framed-handles-and-middle-cancellation';sl='framed-handle-slides-and-index-one-removal';traj='morse-trajectories-and-critical-value-lowering';arr='rearranging-the-original-framed-handles';hi='higher-index-framed-slides-and-chain-maps';hc='integral-handle-chains-and-signed-incidences';belt='belt-sphere-complements-and-the-whitney-disk';cancel='morse-cancellation-with-controlled-support'
    for file,needle,target,num in [(sp,'Every class used in this algorithm',fr,'7'),(sp,'The rank-four adapted normal-frame calculation',wh,'4'),(sp,'of the Pontryagin--Thom companion proved',pt,'8'),(mid,'the full block permutation, function sign',sl,'8'),(mid,'Its outgoing map is the actual flow endpoint',cancel,'6'),(sl,'Apply the outward radial flow',arr,'3'),(sl,'Use the supported critical-value lowering',traj,'4'),(wh,'The relative embedded-disk proof',belt,'5'),(traj,'of that receiving companion verifies',mid,'5'),(hi,'The ambient tube compression',arr,'2'),(hi,'To prove this, apply the finite Euclidean',hc,'4'),(hi,'In particular the explicit six-',hc,'6')]:
        subst(file,needle,[(cref(lab(file,'section-'+num)),cref(lab(target,'section-'+num)))])
    subst(hi,'The ambient tube compression',[(cref(lab(hi,'section-3')),cref(lab(arr,'section-3')))])
    subst(sl,'The compact-limit and hitting-time proof',[(cref(lab(sl,'section-2')),cref(lab(traj,'section-2'))),(cref(lab(sl,'section-4')),cref(lab(traj,'section-4')))])
    subst(belt,'coordinate embedding and normal-neighbourhood',[(cref(lab(belt,'section-2')),cref('mapsI:cw:cw-manifolds'))])
    subst(hi,'all its cutoff and seam terms',[(cref(lab(hi,'section-1')),cref(lab(belt,'section-1'))),('the arrangement chapter, Section 1',cref(lab(arr,'section-1')))])
    for needle,target,oldrange,nums in [
        ('The original integral stable group and its completion maps',st,'Sections 1--7',range(1,8)),
        ('Framed handle slides and removal of index one',sl,'Sections 1, 7--8',[1,7,8]),
        ('Whitney moves in the original receiving dimensions',wh,'Sections 1--5',range(1,6)),
        ('Actual Morse data for the modified framed handles',mid,'Sections 2--6',range(2,7))]:
        subst(fr,needle+' ('+cref(lab(target))+')',[(oldrange,cref(*(lab(target,'section-'+str(i)) for i in nums)))])
    # Further content-matched companion formulas found by the exhaustive
    # chapter scan; each target is the displayed formula actually described.
    rel='relative-morse-functions-and-original-handles';spin='spin-six-and-the-framing-comparison';proj='the-original-projective-coordinate-and-actual-cooperations';zero='removing-the-original-zero-and-top-handles'
    move(sp,'the ordered lower handle coordinates',fr,'eq',['8.4'])
    move(sp,'Let \\(B:g^*TX',spin,'eq',['6.3'])
    move(res,'In the mapping-cylinder proof',ad,'eq',['1.5'])
    subst(sl,'Here \\(F_j\\)',[(eq(sl,'1.8'),eq(belt,'1.8')),('(1.13)',eq(belt,'1.13')),('(1.13a)',eq(belt,'1.13a'))])
    move(sl,'Substituting into the original full attaching formula',rel,'eq',['4.3'])
    move(proj,'The actual-cooperation chapter, equation',res,'eq',['6.4'])
    change(zero,'Realize this isotopy as descending holonomy',lambda s:s.replace(eq(zero,'1.2'),eq(traj,'1.2'),1).replace('(1.9)',eq(traj,'1.9')),'The first equation 1.2 and the endpoint 1.9 cite the trajectory companion holonomy construction; the later stable-set equation 1.2 in this same paragraph remains local. Exact content independently checked by cdp_audit.')
    move(hi,'of the handle-chain chapter, equation',hc,'eq',['3.5'])
    move(arr,'the complete smooth symmetric step',rel,'eq',['4.15'])
    move(arr,'the \\(dB\\)-term',rel,'eq',['4.8'])
    subst(arr,'Its inverse and both complete tangent maps',[(eq(arr,'1.12'),eq(belt,'1.12')),('(1.13a)',eq(belt,'1.13a')),('(1.13b)',eq(belt,'1.13b'))])
    subst(sp,'by the geometric framing chapter, Section 7',[('the geometric framing chapter, Section 7',cref(lab(fr,'section-7')))])
    subst(sp,'by the full integral duality comparison',[('the geometric framing chapter, Section 6.3',cref(lab(fr,'section-6.3')))])
    # All 33 chapters were scanned, including relative links and references
    # whose named target is in the preceding paragraph rather than this one.
    pair='creating-an-original-cancelling-handle-pair'
    subst(sp,'For actual cancellation, factor',[(cref(lab(sp,'section-6')),cref(lab(hi,'section-6')))])
    subst(mid,'For the attaching tubes this extension',[(cref(lab(mid,'section-2')),cref(lab(arr,'section-2')))])
    subst(sl,'We now apply all these constructions',[(cref(lab(sl,'section-6')),cref(lab(pair,'section-6'))),(cref(lab(pair)) + ', Section 5',cref(lab(pair,'section-5')))])
    subst(sl,'the closure described in',[(cref(lab(sl,'section-3')),cref(lab(cancel,'section-3')))])
    move(wh,'In particular its equations',mid,'eq',['4.6','4.7'])
    subst(arr,'Apply the proved ambient core-avoidance',[(cref(lab(arr,'section-2')),cref(lab(belt,'section-2')))])
    subst(traj,'The proved finite-parameter core-avoidance',[(cref(lab(traj,'section-2')),cref(lab(belt,'section-2')))])
    move(traj,'The relative coordinate comparison proved',cancel,'eq',['1.5','1.6'])
    move(ad,'degrees as in its',cb,'eq',['3.1'])
    subst(ar,'The human literature context is Neil Strickland',[(cref(lab(ar,'section-5')),'the author\'s Section~5'),(cref(lab(ar,'section-3')),'the author\'s Section~3')],reason='Both section numbers refer to the opened Strickland original, not the receiving course chapter. Its telescope/Moore statements were matched in stable_primary_source_checks.json under mapsStrickland2024; the adjacent receiving equations 2.2 and6.1 remain local.')
    subst(ar,'We give the prerequisite that relates', [('the Adams companion, Sections 8--9',cref(lab(ad,'section-8'),lab(ad,'section-9')))])
    subst(ar,'Combining this specific map with Section 11', [('Section 11 of the Adams companion',cref(lab(ad,'section-11')))])
    subst(ar,'The associated-graded isomorphism is precisely', [('its equation (11.8)',eq(ad,'11.8'))])
    subst(ad,'where \\(F^0=', [('(5.7)',eq(ar,'5.7')),('(5.8)',eq(ar,'5.8')),('(6.8)',eq(ar,'6.8')),('(7.9)',eq(ar,'7.9')),('(7.10)',eq(ar,'7.10')),('(7.13)',eq(ar,'7.13'))])
    subst(sp,'For a bordism, extend the prescribed boundary embedding',[('(8.15)',eq(pt,'8.15'))])
    subst(sl,'has exactly the rounding of the relative Morse', [('the relative Morse companion, Section 4.2',cref(lab(rel,'section-4.2'))),('Section 4.3 of that companion',cref(lab(rel,'section-4.3')))])
    subst(sl,'Here \\(F_j\\)', [('the handle-arrangement companion, Section 1',cref(lab(arr,'section-1')))])
    subst(st,'Their precise receiving uses are:',[
       (cref(lab('thom-euler-for-lesson11'))+', Sections 4--5',cref('mapsI:chain:lemma:4.1',lab('thom-euler-for-lesson11','CG-S6-CHAIN-THEOREM-5.2'))),
       (cref('mapsI:cw:hurewicz-theorem-result')+', Sections 3--4',cref('mapsI:cw:hurewicz-coherent','mapsI:cw:hurewicz-theorem-result')),
       (cref('mapsI:pf:serre-homology')+', Sections 1--5',cref('mapsI:pf:path-lifting','mapsI:pf:filtered-chains','mapsI:pf:serre-homology','mapsI:pf:integral-comparison')),
       (cref(lab(ad,'adams-original-cocycles'))+', Sections 8--9',cref(lab(ad,'section-8'),lab(ad,'section-9'))),
       (cref(lab(d8,'actual-eight-original-suspension'))+', Sections 1--2',cref(lab(d8,'section-1'),lab(d8,'section-2'))),
       (cref(lab(st,'section-8')),cref(lab(pt,'section-8')))])
    subst(res,'Every \\(\\Gamma_n\\) is finite-dimensional', [('Sections 10--11 of the Adams chapter',cref(lab(ad,'section-10'),lab(ad,'section-11')))])
    subst(d8,'For a simplicial abelian group', [('the Thom/Euler companion, Section 4',cref('mapsI:chain:lemma:4.1'))])
    ac='almost-complex-structures-and-integrability'
    broader=r'The same finite linearization is developed in the CC0 supporting course \emph{K-theory for operator algebras}, lesson \emph{Bott periodicity}, '+cref(lab(ac,'section-5'))+'; its full Toeplitz proof gives periodicity for a larger class of coefficient algebras than we need here.'
    required='The complete polynomial clutching and integral generation argument needed here is printed in '+cref(*(lab(ac,'section-10.'+str(i)) for i in range(1,4)))+'.'
    subst(ac,'The same finite linearization is developed',[(broader,required)],reason='The external supporting-course section5 was incorrectly given the receiving associator section5 namespace. Root approved retaining the first three mathematical sentences and attribution, replacing only this nonoperative broader-course comparison by the actual complete printed generation proof; the original broader sentence is preserved verbatim in the provenance move record.')
    provenance_moves.append({'source_tex':ac+'.tex','converted_line':957,'original_sentence':broader,'replacement_sentence':required,'placement':'Exact source-comparison provenance retained here; required polynomial clutching/generation proof remains in the manuscript in full.','root_authorized_scope':'Retain all three preceding mathematical sentences and original attribution; move only the nonoperative broader-course availability/comparison sentence. No operator-algebra result imported.','mathematical_argument_removed':False,**META})
    # Supplemental exact target checks are kept in their original independent
    # review records. Apply only a uniquely identified literal phrase on its
    # immutable converted source line. Do not infer targets from equal numbers.
    applied_reviews=[]
    review_paths=[
        W/'III_course_stable_locator_review.json',
        D/'work/cdp_audit/course_reference_locator_review.json',
        D/'work/invariants_arithmetic/course_characteristic_reference_substitutions.json',
        D/'work/cdp_audit/course_residual_locator_review.json',
    ]
    for review_path in review_paths:
        if not review_path.exists():continue
        review_text=review_path.read_text();review=json.loads(review_text)
        supporting_review=None
        if isinstance(review,list):
            assert review_path.name=='course_characteristic_reference_substitutions.json'
            supporting_review=review_path.with_name('course_characteristic_reference_review.json')
            metadata=json.loads(supporting_review.read_text())['reviewer']
            review={'reader':metadata['model'],'effort':metadata['effort'],'date':metadata['date_utc'],'rows':[{'file':r['file'],'line':r['line'],'record_number':i+1,'mappings':[{'exact_original_phrase':r['before'],'suggested_tex':r['after'],'matched_target_content':r['reason'],'target_labels':r['target_labels']}]} for i,r in enumerate(review)]}
        elif 'rows' not in review and 'plain_rows' in review:
            review['rows']=[{'file':r['file'],'line':r['line'],'record_number':r['record_number'],'mappings':[{'exact_original_phrase':v['before'],'suggested_tex':v['after'],'matched_target_content':v['reason'],'target_labels':v['target_labels']} for v in r.get('replacements',[])]} for r in review['plain_rows']+review['local_reference_rows']]
        applied=0;already=0
        for row in review['rows']:
            for mapping in row.get('mappings',[]):
                if 'suggested_tex' not in mapping:continue
                file=row['file'];line_no=row['line'];old=mapping['exact_original_phrase'];new=mapping['suggested_tex']
                paragraph=current[file].splitlines()[line_no-1]
                if old==new:already+=1;continue
                if old not in paragraph:
                    assert new in paragraph,(str(review_path),row.get('record_number'),file,line_no,old,'neither exact phrase nor replacement')
                    already+=1;continue
                assert paragraph.count(old)==1,(str(review_path),row.get('record_number'),file,line_no,old,'ambiguous')
                change(file,paragraph,lambda s,a=old,b=new:s.replace(a,b,1),mapping.get('matched_target_content',row.get('reason','Exact target matched in independent review.')))
                changes[-1]['target_review_record']=str(review_path.relative_to(D))
                changes[-1]['target_review_row']=row.get('record_number')
                changes[-1]['target_review_reader']=review.get('reader')
                changes[-1]['target_review_effort']=review.get('effort')
                changes[-1]['target_review_date']=review.get('date')
                applied+=1
        applied_reviews.append({'record':str(review_path.relative_to(D)),'sha256':hashlib.sha256(review_text.encode()).hexdigest(),'supporting_review':str(supporting_review.relative_to(D)) if supporting_review else None,'supporting_review_sha256':hashlib.sha256(supporting_review.read_bytes()).hexdigest() if supporting_review else None,'applied_exact_mappings':applied,'already_applied_exact_mappings':already,'reader':review.get('reader'),'effort':review.get('effort'),'date':review.get('date')})
    step_changes=changes
    merged={}
    for r in step_changes:
        key=(r['source_tex'],r['converted_line_before'])
        if key not in merged:
            merged[key]=dict(r); merged[key]['step_ids']=[r['id']]
        else:
            merged[key]['after']=r['after']; merged[key]['step_ids'].append(r['id'])
            merged[key]['reason']+=' '+r['reason']
    changes=list(merged.values())
    # Validate every introduced reference against the actual printed labels and
    # retain nearby mathematical target text for independent inspection.
    labels={}
    files=list(C.glob('*.tex'))+list((D/'editorial').glob('I_paperI_course_*.tex'))+[D/'S6_09_PAPERS_I.tex']
    for p in files:
        ls=p.read_text().splitlines()
        for i,l in enumerate(ls):
            for key in re.findall(r'\\label\{([^}]+)\}',l):
                labels[key]={'file':str(p.relative_to(D)),'line':i+1,'text':'\n'.join(ls[max(0,i-4):min(len(ls),i+12)])}
    for r in changes:
        refs=[]
        for group in re.findall(r'\\(?:c|C|eq|auto)?ref\{([^}]+)\}',r['after']):refs+=group.split(',')
        newrefs=sorted(set(refs)-set(x for g in re.findall(r'\\(?:c|C|eq|auto)?ref\{([^}]+)\}',r['before']) for x in g.split(',')))
        assert all(x in labels for x in newrefs),(r['id'],[x for x in newrefs if x not in labels])
        r['introduced_target_evidence']={x:labels[x] for x in newrefs}
        r['source_sha256']=hashlib.sha256(originals[r['source_tex']].encode()).hexdigest()
    result={**META,'scope':'Every pinned course URL and the content-matched companion-number namespace corrections from the exhaustive 33-chapter reference screen, including nonpinned named-companion formulas and sections. No proof argument removed; the explicitly authorized nonoperative broader-course comparison is retained verbatim in provenance_moves.','pinned_links':pinned,'changes':changes,'individual_step_changes':step_changes,'independent_target_reviews':applied_reviews,'provenance_moves':provenance_moves,'counts':{'pinned_links':len(pinned),'paragraph_changes':len(changes),'files':len(set(r['source_tex'] for r in changes))},'application':'Run transform(text, source_tex) on each converted course chapter before shared cross-paper reference resolution. Exact before/after strings are checked, not broad replacements.'}
    LEDGER.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(result['counts'])
if __name__=='__main__':build()
