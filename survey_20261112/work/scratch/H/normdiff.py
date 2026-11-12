import sys, difflib, re
def norm(p):
    s = open(p, encoding='utf-8', errors='replace').read().replace('\r\n','\n').replace('\r','\n')
    for a,b in ((r'\(', '$'), (r'\)', '$'), (r'\[', '$$'), (r'\]', '$$')):
        s = s.replace(a,b)
    return s.split('\n')
a = norm(sys.argv[1]); b = norm(sys.argv[2])
n = 0
for l in difflib.unified_diff(a,b,lineterm='',n=0):
    if l.startswith(('+++','---','@@')): continue
    n += 1
    if n <= int(sys.argv[3]) : print(l[:500])
print('TOTAL changed lines', n)
