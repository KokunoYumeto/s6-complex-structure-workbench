# List theorem-like statements of a TeX file between two line numbers (reading aid; runs nothing from the paper).
# usage: python -I -B list_statements.py FILE FIRST LAST MAXCHARS [env1,env2,...]
import sys, re
path, first, last, maxc = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
envs = sys.argv[5].split(',') if len(sys.argv) > 5 else ['theorem', 'proposition', 'corollary']
L = open(path, encoding='utf-8', errors='replace').read().split('\n')
BS = chr(92)
i = first - 1
n = 0
while i < min(last, len(L)):
    line = L[i].lstrip()
    hit = None
    for e in envs:
        if line.startswith(BS + 'begin{' + e + '}'):
            hit = e
            break
    if hit:
        j = i
        body = []
        while j < len(L) and (BS + 'end{' + hit + '}') not in L[j]:
            body.append(L[j])
            j += 1
        text = re.sub(r'\s+', ' ', ' '.join(body))
        print(('[%d] ' % (i + 1)) + text[:maxc].encode('ascii', 'replace').decode())
        print()
        n += 1
        i = j
    i += 1
print(n, 'statements')
