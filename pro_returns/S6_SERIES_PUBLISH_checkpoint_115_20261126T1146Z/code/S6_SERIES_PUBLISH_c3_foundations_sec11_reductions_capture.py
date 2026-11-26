from S6_SERIES_PUBLISH_c3_foundations_sec11_helpers import *

main = (ROOT / 'S6_SERIES_PUBLISH_II.tex').read_text()
for number in [69, 77, 81, 84, 72, 85]:
    key = f'cdp:st:C.2.UN.{number}'
    original = block(main, key)
    path = OUT / f'S6_SERIES_PUBLISH_II_sec11_reductions_UN{number}_input.tex'
    if path.exists():
        assert path.read_text().rstrip() == original, key
    else:
        path.write_text(original + '\n', newline='\n')
    print(f'UN{number}: {len(original.splitlines())} current input lines captured.')
