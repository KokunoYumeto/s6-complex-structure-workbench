"""Remove empty paragraphs left by tag placement in all math displays."""
import re
from S6_SERIES_PUBLISH_editing import Editor
ed=Editor('I');snapshot=ed.text
for m in re.finditer(r'(?<!\\)\\\[(.*?)(?<!\\)\\\]',snapshot,re.S):
 new=re.sub(r'\n[ \t]*\n(?:[ \t]*\n)*','\n',m.group(0))
 if new!=m.group(0):ed.replace(m.group(0),new,'D25','Remove empty paragraph breaks left by deleted tag records inside a math display; mathematical tokens are unchanged.','I:display-tag-spacing')
snapshot=ed.text
for m in re.finditer(r'\\begin\{(equation\*?|align\*?|gather\*?|multline\*?|flalign\*?|alignat\*?)\}(.*?)\\end\{\1\}',snapshot,re.S):
 new=re.sub(r'\n[ \t]*\n(?:[ \t]*\n)*','\n',m.group(0))
 if new!=m.group(0):ed.replace(m.group(0),new,'D25','Remove empty paragraph breaks inside a numbered math environment after deleting misplaced tag metadata; mathematical tokens are unchanged.','I:display-tag-spacing')
ed.save()
