import re, sys, os
# prints title, abstract (truncated), and theorem-like heads for each file
pat = re.compile(r'^\\(?:sub)*section\*?\{|^\\begin\{(?:theorem|proposition|lemma|corollary|conjecture)\}')
maxabs = int(sys.argv[1])
for f in sys.argv[2:]:
    print('=' * 20, os.path.basename(f), os.path.getsize(f))
    with open(f, encoding='utf-8', errors='replace') as fh:
        lines = fh.readlines()
    n = len(lines)
    # title
    for i, l in enumerate(lines):
        if l.startswith('\\title'):
            print(''.join(lines[i:i+4]).strip()[:400])
            break
    for i, l in enumerate(lines):
        if l.startswith('\\date'):
            print(l.strip()[:200]); break
    for i, l in enumerate(lines):
        if l.startswith('\\begin{abstract}'):
            j = i
            while j < n and not lines[j].startswith('\\end{abstract}'):
                j += 1
            txt = ' '.join(x.strip() for x in lines[i+1:j])
            print('ABSTRACT:', txt[:maxabs])
            break
    heads = []
    for i, l in enumerate(lines, 1):
        if pat.match(l):
            s = l.rstrip('\n')
            if not s.rstrip().endswith('}') and i < n:
                s += ' ' + lines[i].strip()
            heads.append(f'{i}: {s[:150]}')
    secs = [h for h in heads if 'section' in h.split(':',1)[1][:14]]
    thms = [h for h in heads if h not in secs]
    print(f'-- {len(secs)} sections, {len(thms)} statements')
    for h in heads:
        if 'subsection' in h or 'subsub' in h:
            continue
        print(h)
