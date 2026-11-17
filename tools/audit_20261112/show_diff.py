"""Print changed paragraphs between a before-copy and a new prompt, with the changed words marked (read only)."""
import difflib
import io
import sys


def words_diff(a, b):
    sa, sb = a.split(' '), b.split(' ')
    out = []
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, sa, sb, autojunk=False).get_opcodes():
        if op == 'equal':
            seg = sa[i1:i2]
            out.append(' '.join(seg if len(seg) <= 12 else seg[:5] + ['...'] + seg[-5:]))
        else:
            if i2 > i1:
                out.append('[-' + ' '.join(sa[i1:i2]) + '-]')
            if j2 > j1:
                out.append('{+' + ' '.join(sb[j1:j2]) + '+}')
    return ' '.join(out)


a = io.open(sys.argv[1], encoding='utf-8').read().split('\n')
b = io.open(sys.argv[2], encoding='utf-8').read().split('\n')
sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
for op, i1, i2, j1, j2 in sm.get_opcodes():
    if op == 'equal':
        continue
    if op == 'replace' and (i2 - i1) == (j2 - j1):
        for k in range(i2 - i1):
            print('~ ' + words_diff(a[i1 + k], b[j1 + k]))
    else:
        for line in a[i1:i2]:
            print('- ' + line[:400])
        for line in b[j1:j2]:
            print('+ ' + line[:400])
    print()
