#!/usr/bin/env python3
"""Preserve equation anchors while replacing inherited visible tags by section counters."""
import re,json,argparse
from S6_SERIES_PUBLISH_editing import Editor,ROOT
p=argparse.ArgumentParser();p.add_argument('paper');a=p.parse_args();e=Editor(a.paper)
mapping={};unhandled=[]
pat=re.compile(r'(?<!\\)\\\[(.*?)(?<!\\)\\\]',re.S)
# Build guarded replacements before mutating text. Row spacings \\[2pt] are not displays.
for m in list(pat.finditer(e.text)):
 b=m[1];tags=re.findall(r'\\tag\{([^{}]+)\}',b)
 if not tags:continue
 assert len(tags)==1,(m.start(),tags)
 tag=tags[0];labs=re.findall(r'\\label\{([^{}]+)\}',b)
 label=labs[0] if labs else 'pub:'+a.paper+':eq:'+re.sub(r'[^A-Za-z0-9]+','-',tag)
 if tag in mapping and mapping[tag]!=label:raise ValueError(('duplicate equation tag',tag))
 mapping[tag]=label
 c=re.sub(r'\\tag\{[^{}]+\}', '',b)
 if not labs:c=c.rstrip()+'\n\\label{'+label+'}\n'
 c=re.sub(r'\n[ \t]*\n(?:[ \t]*\n)*','\n',c)
 new='\\begin{equation}'+c+'\\end{equation}'
 e.replace(m.group(0),new,'D19','Replace the inherited visible equation tag by section-based automatic numbering, preserving all permanent anchors.',label)
# Tags already in amsmath numbered environments are deleted with their labels retained.
for tag in re.findall(r'\\tag\{([^{}]+)\}',e.text):
 pos=e.text.index('\\tag{'+tag+'}')
 lo=e.text.rfind('\\begin{',0,pos);hi=e.text.find('\\end{',pos)
 env=e.text[lo:hi]
 labels=re.findall(r'\\label\{([^{}]+)\}',env)
 if labels:
  mapping[tag]=labels[0]
  e.replace('\\tag{'+tag+'}','', 'D19','Use the current section equation counter in an existing numbered display.',labels[0])
 else:unhandled.append(tag)
# Rewrite literal equation references; names in bibliography locators are outside this mapping.
for tag,label in sorted(mapping.items(),key=lambda x:-len(x[0])):
 old='('+tag+')'
 if old in e.text:
  count=e.text.count(old)
  e.replace(old,'\\eqref{'+label+'}','D19','Resolve a literal inherited equation number by its stable mathematical label.',label,count)
if '\\numberwithin{equation}{section}' not in e.text:
 e.replace('\\allowdisplaybreaks[2]','\\allowdisplaybreaks[2]\n\\numberwithin{equation}{section}', 'D19','Number all equations by section in order of appearance.')
e.save();(ROOT/'records'/f'S6_SERIES_PUBLISH_{a.paper}_equation_map.json').write_text(json.dumps({'mapping':mapping,'unhandled':unhandled},indent=2)+'\n')
print('Equation mappings',len(mapping),'unhandled',unhandled)
