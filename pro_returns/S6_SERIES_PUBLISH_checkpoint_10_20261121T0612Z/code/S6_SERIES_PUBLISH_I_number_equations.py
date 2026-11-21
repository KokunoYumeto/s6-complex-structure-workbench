"""Number Paper I's inherited and labelled displays; preserve all anchors."""
from pathlib import Path
import re,json,hashlib,datetime,argparse
from S6_SERIES_PUBLISH_editing import Editor
pa=argparse.ArgumentParser();pa.add_argument('--apply',action='store_true');args=pa.parse_args()
ed=Editor('I');mapping={};numbered_labelled=[]
pat=re.compile(r'(?<!\\)\\\[(.*?)(?<!\\)\\\]',re.S)
for m in list(pat.finditer(ed.text)):
 b=m[1];tags=re.findall(r'\\tag\{([^{}]+)\}',b);labs=re.findall(r'\\label\{([^{}]+)\}',b)
 if not tags and not labs:continue
 assert len(tags)<=1 and len(labs)<=1,(tags,labs)
 tag=tags[0] if tags else None
 label=labs[0] if labs else 'pub:I:eq:'+re.sub(r'[^A-Za-z0-9]+','-',tag)
 if tag:
  assert tag not in mapping;mapping[tag]=label
 c=re.sub(r'\\tag\{[^{}]+\}','',b)
 if not labs:c=c.rstrip()+'\n'+r'\label{'+label+'}\n'
 c=re.sub(r'\n[ \t]*\n(?:[ \t]*\n)*','\n',c)
 ed.replace(m.group(0),r'\begin{equation}'+c+r'\end{equation}',
  'D19','Use automatic section equation numbering for a tagged or referenced display; preserve its exact formula and every anchor.',label)
 numbered_labelled.append(label)

# The sole inherited tagged align* is one four-line displayed formula.
for m in list(re.finditer(r'\\begin\{align\*\}(.*?)\\end\{align\*\}',ed.text,re.S)):
 tags=re.findall(r'\\tag\{([^{}]+)\}',m[1]);labs=re.findall(r'\\label\{([^{}]+)\}',m[1])
 if not tags and not labs:continue
 assert len(tags)==1 and len(labs)<=1,(tags,labs)
 tag=tags[0];label=labs[0] if labs else 'pub:I:eq:'+re.sub(r'[^A-Za-z0-9]+','-',tag)
 assert tag not in mapping;mapping[tag]=label
 b=re.sub(r'\\tag\{[^{}]+\}','',m[1]);b=re.sub(r'\\label\{[^{}]+\}','',b)
 new=r'\begin{equation}\begin{aligned}'+b+r'\end{aligned}'+'\n'+r'\label{'+label+'}\n'+r'\end{equation}'
 ed.replace(m[0],new,'D19','Give the complete four-line twist formula one automatic section equation number.',label)

for m in list(re.finditer(r'\\begin\{equation\}(.*?)\\end\{equation\}',ed.text,re.S)):
 tags=re.findall(r'\\tag\{([^{}]+)\}',m[1])
 if not tags:continue
 labs=re.findall(r'\\label\{([^{}]+)\}',m[1]);assert len(tags)==len(labs)==1,(tags,labs)
 assert tags[0] not in mapping;mapping[tags[0]]=labs[0]
 ed.replace(m[0],re.sub(r'\\tag\{[^{}]+\}','',m[0]),'D19','Replace the inherited display tag by its section counter while retaining the existing label.',labs[0])
assert not re.search(r'\\tag\{',ed.text)

# Hybrid statement-number-plus-suffix references identify exact historical tags.
hybrid=re.compile(r'\(\\(?:ref|cref)\{(push:src:([^}]+))\}\.([0-9]+)\)')
for m in list(hybrid.finditer(ed.text)):
 tag=m[2]+'.'+m[3];assert tag in mapping,tag
 old=m[0]
 if old in ed.text:ed.replace(old,r'\eqref{'+mapping[tag]+'}','D19','Resolve the inherited composite equation reference through its exact display label.',mapping[tag],ed.text.count(old))

# All inherited literal equation references occur before the bibliography.
for tag,label in sorted(mapping.items(),key=lambda z:-len(z[0])):
 old='('+tag+')';body,tail=ed.text.split(r'\begin{thebibliography}',1)
 if old in body:
  assert old not in tail,('ambiguous bibliography token',tag)
  ed.replace(old,r'\eqref{'+label+'}','D19',
   'Resolve literal equation references through permanent labels.',label,body.count(old))
# These two references were printed without parentheses in the inherited
# prose. The separate AC Theorem B.1 citation keeps its source numbering.
for tag,old,new in [
 ('A.24c','orbit representatives in A.24c and','orbit representatives in '+r'\eqref{'+mapping['A.24c']+'} and'),
 ('A.24d','monomial in A.24d.','monomial in '+r'\eqref{'+mapping['A.24d']+'}.')]:
 if old in ed.text:
  ed.replace(old,new,'D19','Resolve the bare inherited equation reference through its exact permanent display label.',mapping[tag])
if r'\numberwithin{equation}{section}' not in ed.text:
 ed.replace(r'\allowdisplaybreaks[2]',r'\allowdisplaybreaks[2]'+'\n'+r'\numberwithin{equation}{section}',
  'D19','Number all equations by section in their current mathematical order.')
root=Path(__file__).resolve().parents[1]
out={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'mapping':mapping,'labelled_displays_numbered':numbered_labelled,'source_before_sha256':hashlib.sha256(ed.before.encode()).hexdigest(),'source_after_sha256':hashlib.sha256(ed.text.encode()).hexdigest(),'guards':len(ed.rows),'applied':args.apply}
if args.apply:
 ed.save();(root/'records/S6_SERIES_PUBLISH_I_equation_map.json').write_text(json.dumps(out,indent=2)+'\n')
else:
 (root/'records/S6_SERIES_PUBLISH_I_equation_numbering_preview.json').write_text(json.dumps(out,indent=2)+'\n')
 (root/'records/S6_SERIES_PUBLISH_I_equation_numbering_preview.tex').write_text(ed.text)
print(json.dumps({k:v for k,v in out.items() if k not in ('mapping','labelled_displays_numbered')}))
