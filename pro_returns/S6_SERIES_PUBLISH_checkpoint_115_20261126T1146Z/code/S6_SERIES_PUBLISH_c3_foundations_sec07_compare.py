from S6_SERIES_PUBLISH_c3_foundations_sec07_helpers import *
import sys

package=sys.argv[1]
source=(ROOT/'S6_SERIES_PUBLISH_II.tex').read_text()
receiving=source
guards=json.loads((OUT/f'S6_SERIES_PUBLISH_sec07_{package}_guards.json').read_text())
for guard in guards:
    count=receiving.count(guard['old'])
    assert count==1,(guard['key'],count)
    receiving=receiving.replace(guard['old'],guard['new'],1)
for pattern in (r'\\label\{([^{}]+)\}',r'\\hypertarget\{([^{}]+)\}'):
    old=re.findall(pattern,source);new=re.findall(pattern,receiving)
    for identity in set(old):
        assert old.count(identity)==new.count(identity),(identity,old.count(identity),new.count(identity))
print(f'{package}: all {len(guards)} guards match once; every old label and target has unchanged multiplicity. No shared write.')
for key in sys.argv[2:]:
    print(block(receiving,key))
