from S6_SERIES_PUBLISH_c3_foundations_sec11_helpers import *
main=(ROOT/'S6_SERIES_PUBLISH_II.tex').read_text()
for n in [73,76]:
    body=block(main,f'cdp:st:C.2.UN.{n}')
    path=OUT/f'S6_SERIES_PUBLISH_II_sec11_toric_log_UN{n}_input.tex'
    if path.exists():assert path.read_text().rstrip()==body,n
    else:path.write_text(body+'\n',newline='\n')
    print(n,len(body.splitlines()))
