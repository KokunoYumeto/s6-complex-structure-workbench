from S6_SERIES_PUBLISH_c3_foundations_sec07_helpers import *
import sys

s=(ROOT/'S6_SERIES_PUBLISH_II.tex').read_text()
if len(sys.argv)>1:
    for key in sys.argv[1:]:
        print(block(s,key))
else:
    for m in re.finditer(r'\\begin\{(?:proposition|lemma|theorem|corollary|remark)\}[^\n]*',s):
        b=s.find(r'\end{proof}',m.end())
        if b<0:continue
        text=s[m.start():b+len(r'\end{proof}')]
        labels=re.findall(r'\\label\{([^{}]+)\}',m.group(0))
        if labels and 'night:P4.28' in text:
            print(labels[0])
            for line in text.splitlines():
                if 'P4.28' in line:print('  '+line)
