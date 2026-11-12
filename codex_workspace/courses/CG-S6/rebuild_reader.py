"""Rebuild the lesson reader from editable mathematics. CC0-1.0.

Requires Python 3 and Pandoc on PATH. Keeps the existing reader shell and
local MathJax/font assets; no network request is made.
"""
from pathlib import Path
import hashlib,json,subprocess

root=Path(__file__).resolve().parent
data=json.loads((root/'course.json').read_text(encoding='utf-8'))
for unit in data['units']+data.get('working_units',[])+data.get('proof_providers',[]):
    source=root/unit['source'];reader=root/unit['reader']
    content=subprocess.check_output(['pandoc','--from=markdown+tex_math_single_backslash+header_attributes'+('-markdown_in_html_blocks' if unit['id'].startswith('CG-S6-GENERAL-ANALYTIC-') else ''),
        '--to=html5','--mathjax',str(source)],text=True,encoding='utf-8')
    content=content.replace('src="../assets/','src="assets/')
    content=content.replace('href="../checks/','href="checks/')
    content=content.replace('href="../sources/','href="sources/')
    content=content.replace('href="../provenance.json', 'href="provenance.json')
    content=content.replace('href="../CG-S6-', 'href="CG-S6-')
    for other in data['units']+data.get('working_units',[])+data.get('proof_providers',[]):
        content=content.replace('href="'+Path(other['source']).name,'href="'+other['reader'])
    old=reader.read_text(encoding='utf-8')
    assert old.count('<article>')==old.count('</article>')==1
    new=old.split('<article>')[0]+'<article>'+content+'</article>'+old.split('</article>')[1]
    if new!=old:
        reader.write_text(new,encoding='utf-8',newline='\n')
    unit['sha256']=hashlib.sha256(source.read_bytes()).hexdigest()
    unit['reader_sha256']=hashlib.sha256(reader.read_bytes()).hexdigest()
(root/'course.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
print('Readers regenerated. Run the exact checkers and rebuild the download after any mathematical edit.')
