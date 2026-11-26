"""Print actual paragraph separators inside Paper III display environments."""
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
source = (root / 'S6_SERIES_PUBLISH_III.tex').read_text(encoding='utf-8')
pattern = r'\\begin\{(equation\*?|align\*?|gather\*?|multline\*?)\}.*?\\end\{\1\}|(?<!\\)\\\[.*?\\\]'
found = []
for match in re.finditer(pattern, source, re.S):
    blank = list(re.finditer(r'\n[ \t]*\n', match[0]))
    if blank:
        found.append((match, blank))
print('DISPLAY_COUNT', len(found), 'PARAGRAPH_SEPARATORS', sum(len(b) for _, b in found))
for index, (match, blank) in enumerate(found, 1):
    print('DISPLAY', index, 'SOURCE_LINE', source.count('\n', 0, match.start()) + 1,
          'SEPARATORS', len(blank))
    print(match[0])
