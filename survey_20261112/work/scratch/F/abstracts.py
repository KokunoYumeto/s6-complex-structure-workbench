import re, sys
n = int(sys.argv[1])
for f in sys.argv[2:]:
    s = open(f, encoding='utf-8', errors='replace').read()
    print('#####', f, len(s))
    i = s.find('\\begin{abstract}')
    j = s.find('\\end{abstract}')
    if i >= 0:
        print(' '.join(s[i + 16:j].split())[:n])
    else:
        k = s.find('\\begin{document}')
        print(' '.join(s[k:k + n].split()))
    print('inputs:', re.findall(r'\\input\{([^}]*)\}', s)[:14])
