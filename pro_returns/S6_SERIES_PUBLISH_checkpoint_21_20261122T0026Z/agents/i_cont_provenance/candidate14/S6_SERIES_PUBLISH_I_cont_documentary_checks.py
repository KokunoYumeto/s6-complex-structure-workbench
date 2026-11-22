#!/usr/bin/env python3
"""Reproduce the continuation's documentary-link and visible-reference checks."""
from pathlib import Path
import argparse,csv,datetime,hashlib,json,re,urllib.request

PIN='1fb9194767aef92abcc06071e3820c2f226b9512'
REPO='KokunoYumeto/s6-complex-structure-workbench'
FOLDER='pro_returns/S6_SERIES_PUBLISH_checkpoint_10_20261121T0612Z/'

def write(path,value):
    path.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def group(text,start):
    while text[start].isspace():start+=1
    assert text[start]=='{'
    depth=1;index=start+1
    while depth:
        if text[index]=='{' and text[index-1]!='\\':depth+=1
        elif text[index]=='}' and text[index-1]!='\\':depth-=1
        index+=1
    return text[start+1:index-1],index

def references(root,base,out):
    source=root/'S6_SERIES_PUBLISH_I.tex';text=source.read_text()
    start=text.index(r'\begin{document}');body=text[start:]
    for name,nargs in [('StatementRecord',4),('Uses',1),('UsedBy',1)]:
        while True:
            found=re.search(r'\\'+name+r'\s*\{',body)
            if found is None:break
            end=found.end()-1
            for _ in range(nargs):_,end=group(body,end)
            body=body[:found.start()]+' '*(end-found.start())+body[end:]
    body=re.sub(r'(?<!\\)%[^\n]*',lambda m:' '*len(m[0]),body)
    with (root/'S6_SERIES_PUBLISH_tags.tsv').open(newline='') as stream:
        tags=list(csv.DictReader(stream,delimiter='\t'))
    registry={row['label']:row for row in tags}
    vkeys={row['label'] for row in tags if row['paper']=='V'}
    references=[]
    for found in re.finditer(r'\\(SeriesRef|SeriesRefText|cref|Cref|ref|eqref)\*?\{([^}]+)\}',body):
        for key in found[2].split(','):
            if key in vkeys:
                references.append({'form':found[1],'key':key,'tag':registry[key]['tag'],
                                   'registry_number':registry[key]['number'],
                                   'line':text.count('\n',0,start+found.start())+1,
                                   'context':body[max(0,found.start()-120):found.end()+120]})
    literal=[]
    for found in re.finditer(r'\\ExternalPaperRef|(?:Paper|paper)[~\s]+V\b|S6_[^\s{}]*_V\.pdf|(?<!\w)V\.[A-G0-9]',body):
        literal.append({'line':text.count('\n',0,start+found.start())+1,
                        'context':body[max(0,found.start()-90):found.end()+120]})
    series_rows=[line for line in body.splitlines() if re.match(r'\s*V\s*&',line)]
    public_v=base/'S6_series_V_public_v2.tex';vtext=public_v.read_text()
    result={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
            'source_sha256':digest(source),'public_V_source_sha256':digest(public_v),
            'visible_cross_paper_V_refs':references,'visible_count':len(references),
            'other_literal_forms':literal,'common_table_rows':series_rows,
            'table_rows_exactly_present_in_public_V':[line in vtext for line in series_rows],
            'table_scope_note':'The shared shorthand a resolved fibre product is present in public V v2. Its full theorem gives a small crepant resolution of the Weierstrass model and a bimeromorphic map to the literal fibre product; the final series-table pass can state that exact construction.',
            'scope':'Document body after exact span masking of the nonprinting four-argument StatementRecord metadata, one-argument Uses and UsedBy metadata, and comments. The printed StatementRecord tag argument contains the permanent four-character tag. Hidden SRef declarations are excluded. No mathematical check event.',
            'mathematical_events_added':0}
    write(out/'S6_SERIES_PUBLISH_I_cont_V_references.json',result)
    print(json.dumps(result,ensure_ascii=False,indent=2))

def pin_open(root,base,out):
    urls=[
        ('pin_tree','https://github.com/'+REPO+'/tree/'+PIN+'/'+FOLDER),
        ('pin_api','https://api.github.com/repos/'+REPO+'/commits/'+PIN),
        ('pin_report','https://raw.githubusercontent.com/'+REPO+'/'+PIN+'/'+FOLDER+'S6_SERIES_PUBLISH_report.md')]
    results=[]
    for name,url in urls:
        row={'name':name,'url':url,'checked_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
        try:
            request=urllib.request.Request(url,headers={'User-Agent':'S6-Series-Publish-Records-Verification'})
            with urllib.request.urlopen(request,timeout=20) as response:
                data=response.read()
                row.update(status=response.status,final_url=response.url,bytes=len(data),
                           sha256=hashlib.sha256(data).hexdigest())
            suffix='.json' if name=='pin_api' else '.html' if name=='pin_tree' else '.md'
            saved=out/('S6_SERIES_PUBLISH_I_cont_'+name+suffix)
            saved.write_bytes(data);row['saved']=str(saved)
            if name=='pin_api':
                parsed=json.loads(data);row.update(commit=parsed.get('sha'),message=parsed.get('commit',{}).get('message'))
            if name=='pin_report':
                row['byte_equal_to_attached_checkpoint_report']=digest(saved)==digest(base/'S6_SERIES_PUBLISH_checkpoint_10/S6_SERIES_PUBLISH_report.md')
        except Exception as error:
            row['error']=repr(error)
        results.append(row);print(json.dumps(row))
    write(out/'S6_SERIES_PUBLISH_I_cont_pin_open.json',results)

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action',choices=['references','pin'])
    parser.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[2])
    parser.add_argument('--base',type=Path)
    parser.add_argument('--out',type=Path)
    args=parser.parse_args();root=args.root.resolve()
    base=(args.base or root.parent/'S6_SERIES_PUBLISH_work').resolve()
    out=(args.out or root/'agents/i_cont_provenance').resolve();out.mkdir(parents=True,exist_ok=True)
    (references if args.action=='references' else pin_open)(root,base,out)

if __name__=='__main__':main()
