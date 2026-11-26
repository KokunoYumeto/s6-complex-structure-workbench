from S6_SERIES_PUBLISH_c3_foundations_sec11_helpers import *

main=(ROOT/'S6_SERIES_PUBLISH_II.tex').read_text()
for number in [66,67,70,80,83]:
 key=f'cdp:st:C.2.UN.{number}'
 text=block(main,key)+'\n'
 path=OUT/f'S6_SERIES_PUBLISH_II_sec11_models_UN{number}_input.tex'
 if path.exists():
  assert path.read_text()==text, f'Current UN{number} changed after capture; compare before overwriting.'
 else:
  path.write_text(text,newline='\n')
 print(f'UN{number}: {len(text.splitlines())} lines')
