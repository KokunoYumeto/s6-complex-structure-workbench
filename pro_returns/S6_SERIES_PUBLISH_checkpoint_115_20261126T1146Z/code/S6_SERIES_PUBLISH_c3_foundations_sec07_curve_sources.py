from pathlib import Path
from urllib.request import Request, urlopen
import hashlib
from html.parser import HTMLParser

class TextParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts=[]
    def handle_data(self,data):
        value=data.strip()
        if value:
            self.parts.append(value)

out=Path('/workspace/scratch/9fcd229a9ed4/base/S6_PUBLISH_c3_foundations_sources')
url='https://stacks.math.columbia.edu/tag/0A7M'
dest=out/'S6_SERIES_PUBLISH_Stacks_0A7M.html'
with urlopen(Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=35) as response:
    content=response.read()
dest.write_bytes(content)
parser=TextParser()
parser.feed(content.decode('utf-8'))
text='\n'.join(parser.parts)
dest.with_suffix('.txt').write_text(text,newline='\n')
print(url,hashlib.sha256(content).hexdigest())
for term in ['Lemma 47.16.4','Lemma 47.16.7']:
    i=text.find(term)
    print(term,i)
    print(text[max(0,i-200):i+8500])
