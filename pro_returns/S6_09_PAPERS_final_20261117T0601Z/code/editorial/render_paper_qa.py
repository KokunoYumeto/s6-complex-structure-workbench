"""Render former overflow loci and a reproducible spread sample for visual QA.

Creating this manifest does not claim that any page has been visually inspected.
The separate final validation records only images actually opened and reviewed.
"""
from pathlib import Path
import subprocess,json,hashlib,re,sys,math
from PIL import Image,ImageOps,ImageDraw

OUT=Path(__file__).resolve().parents[2]
paper=sys.argv[1]
pdf=OUT/f'S6_09_PAPERS_{paper}.pdf'
sha=hashlib.sha256(pdf.read_bytes()).hexdigest()
dest=OUT/'validation'/(paper+'_'+sha[:12]);dest.mkdir(parents=True,exist_ok=True)
text=subprocess.run(['pdftotext','-layout',str(pdf),'-'],capture_output=True,text=True,check=True).stdout
pages=text.split('\f')
if not pages[-1].strip():pages.pop()
(dest/'extracted_text.txt').write_text(text)
selected={}
def add(p,why):
    if 1<=p<=len(pages):selected.setdefault(p,[]).append(why)
for p in range(1,5):add(p,'Front matter and beginning of conventions')
for p in range(5,len(pages)+1,35):add(p,'Spread sample every 35 pages')
for p in range(max(1,len(pages)-2),len(pages)+1):add(p,'Final bibliography pages')
if paper=='I':
    for p in [335,336,345,346,347]:add(p,'Page number associated with former overflow builds')
    for i,p in enumerate(pages,1):
        normal=' '.join(p.split()).lower()
        if 'write its coordinates in the ordered basis' in normal:
            add(i,'Current location of repaired 6.88432pt inline-basis overflow')
            add(i-1,'Page preceding repaired overflow locus')
            add(i+1,'Page following repaired overflow locus')
        compact=re.sub(r'\s+','',p).lower()
        if any(name in compact for name in ['viaclovsky_comb_s6_draft_','logarithmic_s6_october_','compact_complex_threefolds_repaired_']):
            add(i,'Current complete-credit filename locus that overflowed in builds 19–20')
    # The final common-reference pass resolves historical prompt shorthand.
    # Locate every distinctive literal replacement in current PDF text,
    # so these prose-only edits receive their own page inspection.
    edits=OUT/'work/invariants_arithmetic/paper_I_checkpoint_shorthand_changes.json'
    if edits.exists():
        norm=lambda t:re.sub(r'[^a-z0-9]','',t.casefold())
        page_keys=[norm(p) for p in pages]
        for edit in json.loads(edits.read_text())['literal_substitutions']:
            after=edit['after']
            head=re.match(r'\\begin\{[^}]+\}\[([^]]+)\]',after)
            phrase=head[1] if head else re.split(r'[\\$]',after)[0]
            key=norm(phrase)
            if len(key)<15:continue
            found=[i+1 for i,p in enumerate(page_keys) if key in p]
            if not found:
                key=norm(' '.join(phrase.split()[:7]))
                found=[i+1 for i,p in enumerate(page_keys) if len(key)>=15 and key in p]
            for p in found:add(p,'Final exact source-alias replacement '+edit['scope_id'])
aux=(OUT/f'S6_09_PAPERS_{paper}.aux').read_text()
labels={m[1]:(m[2],int(m[3])) for m in re.finditer(r'\\newlabel\{([^}]+)\}\{\{([^}]*)\}\{(\d+)\}',aux)}
if paper=='II':
    # The old source-line numbers changed when known results were moved.
    # Map each unique former overflow by the literal equation tags in its
    # Uses line, or the exact preserved heading/citation string, to the
    # nearest statement/section label in the current standalone manuscript.
    source=(OUT/'S6_09_PAPERS_II.tex').read_text()
    label_positions=list(re.finditer(r'\\label\{((?:cdp:st:|sec:II:)[^}]+)\}',source))
    uses=list(re.finditer(r'^\\Uses\{.*$',source,re.M))
    loci=[];seen=set()
    for log in sorted((OUT/'editorial').glob('S6_09_PAPERS_II_build_*.stdout.txt')):
        old=log.read_text()
        for match in re.finditer(r'Overfull \\hbox \(([\d.]+)pt too wide\) in paragraph at lines (\d+)--(\d+)',old):
            end=old.find('\n\n',match.end());chunk=old[match.end():end]
            clean=re.sub(r'\\TU/LatinModernRoman\(0\)/[^ /\n]+/[^ /\n]+/[0-9.]+','',chunk).replace('\n','').replace('[]','')
            if '2.18–2.21,4.5–4.8.12' in clean:
                # The final credit matrix introduced three identical long
                # locator strings in the result index. Inspect every current
                # page carrying that string, not the source theorem's page.
                current_pages=[i for i,p in enumerate(pages,1) if
                    '2.18–2.21,4.5–4.8.12' in re.sub(r'\s+','',p)]
                assert current_pages,('Unmapped result-index credit overflow',clean)
                key=('result-index-Kulikov-locators',clean)
                if key not in seen:
                    seen.add(key)
                    loci.append({'build':log.name,'old_lines':[int(match[2]),int(match[3])],
                      'excess_pt':float(match[1]),'text':clean,'current_pages':current_pages,
                      'mapping':'Exact credit-locator text in the current result index'})
                    for p in current_pages:
                        add(p,'Former long Kulikov credit-locator overflow in result index')
                continue
            tags=set(re.findall(r'C\.[A-Z]+\.\d+',clean));anchor=None
            if tags:
                ranked=[(sum(('cdp:eq:'+tag+'}') in u[0] for tag in tags),u.start()) for u in uses]
                score,pos=max(ranked)
                assert score>0,(log,clean)
                anchor=max((q for q in label_positions if q.start()<pos),key=lambda q:q.start())[1]
            elif 'Unrestricted Euler topology' in clean:
                pos=source.index('\\section{Unrestricted Euler topology and component covers}')
                anchor=next(q[1] for q in label_positions if q.start()>pos)
            elif 'Marked Hopf, ruled and elliptic supports' in clean:
                pos=source.index('\\section{Marked Hopf, ruled and elliptic supports')
                anchor=next(q[1] for q in label_positions if q.start()>pos)
            else:
                needle='2.2.2--2.2.5' if '2.2.2--2.2.5' in clean else '4.8.5--4.8.12,4.16.2--4.16.6' if '4.8.5--4.8.12' in clean else None
                if needle:
                    u=next(u for u in uses if needle in u[0])
                    anchor=max((q for q in label_positions if q.start()<u.start()),key=lambda q:q.start())[1]
            assert anchor and anchor in labels,('Unmapped former overflow',log.name,clean)
            current_page=labels[anchor][1]
            key=(anchor,clean)
            if key in seen:continue
            seen.add(key)
            loci.append({'build':log.name,'old_lines':[int(match[2]),int(match[3])],
                         'excess_pt':float(match[1]),'text':clean,'current_anchor':anchor,'current_statement_page':current_page})
            for p in range(current_page,min(len(pages),current_page+2)+1):
                add(p,'Former overflow locus '+anchor+'; statement and following Uses/proof pages')
    (dest/'former_overflow_loci.json').write_text(json.dumps(loci,indent=2)+'\n')
if paper=='III':
    # Observed late conversion defects require their own final-image check:
    # raw fence wrappers, restored theorem/proof boundaries, and the one
    # missing proof-end glyph.  These are in addition to every overflow locus.
    source=(OUT/'S6_09_PAPERS_III.tex').read_text()
    positions=list(re.finditer(r'\\label\{([^}]+)\}',source))
    structural=OUT/'records/III_course_structure_repairs.json'
    if structural.exists():
        fixes=json.loads(structural.read_text())
        for event in fixes['events']:
            if 'raw-LaTeX wrapper' not in event['reason']:continue
            needle=event['after'].strip()
            at=source.find(needle)
            assert at>=0,('Final raw-fence repair body missing',event['converted'])
            keys=re.findall(r'\\label\{([^}]+)\}',needle)
            key=next((k for k in keys if k in labels),None)
            if key is None:
                key=max((q for q in positions if q.start()<at and q[1] in labels),key=lambda q:q.start())[1]
            p=labels[key][1]
            add(p,'Actual former raw-LaTeX fence body at '+key)
            add(p+1,'Continuation of former raw-LaTeX fence body at '+key)
        changed_keys=[k for k in labels if ':source-theorem-' in k or
                      k.startswith('courseIII:thom-euler-for-lesson11:CG-S6-CHAIN-') or
                      k=='courseIII:manifold-duality-the-diagonal-and-wu-classes.source:eq:4.1']
        for key in changed_keys:
            p=labels[key][1]
            add(p,'Repaired formal theorem/proof boundary '+key)
            add(p+1,'Continuation of repaired formal theorem/proof '+key)
        for event in fixes['events']:
            if not event['reason'].startswith('Distinguish historical source self-review'):continue
            at=source.find(event['after'])
            assert at>=0,('Final historical-status wording missing',event['converted'])
            key=max((q for q in positions if q.start()<at and q[1] in labels),key=lambda q:q.start())[1]
            for p in range(labels[key][1],labels[key][1]+3):
                add(p,'Historical/current review-status distinction in '+event['converted'])
    refwords=OUT/'records/III_external_reference_wording_repairs.json'
    if refwords.exists():
        for event in json.loads(refwords.read_text()):
            for hit in re.finditer(re.escape(event['after']),source):
                key=max((q for q in positions if q.start()<hit.start() and q[1] in labels),key=lambda q:q.start())[1]
                for p in range(labels[key][1],labels[key][1]+2):
                    add(p,'Resolved external reference kind wording: '+event['after'])
    # Each first observed overflow is tied to a literal preserved source
    # repair, with a final-PDF anchor. Longtable's stale width cache generated
    # repeated warnings at table heads; inspect every page of all five final
    # weight tables, including the continuation pages.
    anchors={4.06342:['qa:III:layout:1'],6.1479:['qa:III:layout:2'],
      32.27287:['qa:III:layout:3'],150.32729:['qa:III:layout:4'],
      40.46014:['qa:III:layout:5'],22.0679:['qa:III:layout:6'],
      19.55638:['qa:III:layout:7'],2.53334:['qa:III:layout:8'],
      99.594:['qa:III:coefficient-weight-'+str(i) for i in range(5)],
      28.41891:['qa:III:coefficient-weight-'+str(i) for i in range(5)],
      39.4914:['qa:III:layout:10'],16.68358:['qa:III:layout:11']}
    loci=[]
    for log in sorted((OUT/'editorial').glob('S6_09_PAPERS_III_build_*.stdout.txt')):
        for match in re.finditer(r'Overfull \\[hv]box \(([\d.]+)pt[^\n]*',log.read_text()):
            width=float(match[1])
            known=next((w for w in anchors if abs(w-width)<0.0001),None)
            assert known is not None,('Unmapped III overflow',log.name,match[0])
            mapped=anchors[known]
            assert all(a in labels for a in mapped),(log.name,mapped)
            current_pages=[]
            for a in mapped:
                p=labels[a][1]
                for q in range(max(1,p-1),min(len(pages),p+2)+1):
                    add(q,'Former overflow '+str(width)+'pt at '+a)
                    current_pages.append(q)
            loci.append({'build':log.name,'diagnostic':match[0],
              'excess_pt':width,'current_anchors':mapped,'current_pages':sorted(set(current_pages))})
    for a in [x for x in labels if x.startswith('qa:III:layout:')]:
        add(labels[a][1],'Current exact layout repair '+a)
    (dest/'former_overflow_loci.json').write_text(json.dumps(loci,indent=2)+'\n')
for key in [f'app:{paper}:result-index',f'app:{paper}:programs',f'sec:{paper}:verification',
            'mapsI:chain:section','mapsI:cw:section','mapsI:pf:section','mapsI:course:homotopy-section']:
    if key in labels:
        p=labels[key][1];add(p,'Section start '+key);add(p+1,'Section continuation '+key)
for i,p in enumerate(pages,1):
    if re.search(r'^\s*References\s*$',p,re.M):
        add(i,'Start of inline references');add((i+len(pages))//2,'Middle of inline references')
    if 'Questions not established by the present arguments' in ' '.join(p.split()):
        add(i,'Separate part for unestablished questions');add(i+1,'Continuation of unestablished questions')
files=[]
for p,reasons in sorted(selected.items()):
    prefix=dest/f'page_{p:04d}'
    subprocess.run(['pdftoppm','-f',str(p),'-l',str(p),'-r','110','-png','-singlefile',str(pdf),str(prefix)],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
    files.append({'page':p,'file':str(prefix.with_suffix('.png').relative_to(OUT)),'reasons':reasons})
contacts=[]
for start in range(0,len(files),4):
    group=files[start:start+4];thumbs=[]
    for row in group:
        im=Image.open(OUT/row['file']).convert('RGB');im.thumbnail((600,800))
        tile=Image.new('RGB',(620,840),'#d9dfe7');tile.paste(im,((620-im.width)//2,30))
        ImageDraw.Draw(tile).text((14,8),f"Paper {paper}, page {row['page']}",fill='black')
        thumbs.append(tile)
    canvas=Image.new('RGB',(1240,840*math.ceil(len(group)/2)),'white')
    for j,t in enumerate(thumbs):canvas.paste(t,((j%2)*620,(j//2)*840))
    path=dest/f'contact_{start//4+1:02d}.png';canvas.save(path)
    contacts.append({'file':str(path.relative_to(OUT)),'pages':[x['page'] for x in group]})
manifest={'paper':paper,'pdf_sha256':sha,'pages':len(pages),'rendered':files,'contacts':contacts,
          'visual_inspection_status':'Not yet asserted; rendering alone is not visual review.'}
(dest/'render_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
(OUT/'records'/f'{paper}_qa_render_manifest_pointer.json').write_text(json.dumps({'manifest':str((dest/'render_manifest.json').relative_to(OUT))},indent=2)+'\n')
print(json.dumps({'directory':str(dest),'pages':len(pages),'rendered_pages':[x['page'] for x in files],'contact_sheets':len(contacts)},indent=2))
