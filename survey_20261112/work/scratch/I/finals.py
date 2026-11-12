import io, sys as _s
_s.stdout = io.TextIOWrapper(_s.stdout.buffer, encoding="utf-8", errors="replace")
import sys, re
path = sys.argv[1]
mode = sys.argv[2] if len(sys.argv) > 2 else 'assistant'
maxlen = int(sys.argv[3]) if len(sys.argv) > 3 else 6000
start = int(sys.argv[4]) if len(sys.argv) > 4 else 0
txt = open(path, encoding='utf-8').read()
blocks = re.split(r'(?m)^(?=## (?:user|assistant) )', txt)
n = 0
for b in blocks:
    head = b.split('\n', 1)[0]
    if mode == 'assistant' and not head.startswith('## assistant'):
        continue
    if mode == 'user' and not head.startswith('## user'):
        continue
    m = re.search(r'raw line (\d+)', head)
    ln = int(m.group(1)) if m else -1
    if ln < start:
        continue
    if mode == 'user' and '<codex_internal_context' in b[:400]:
        print(head, '[machine goal context, %d chars, skipped]' % len(b))
        continue
    n += 1
    print(b[:maxlen])
    if len(b) > maxlen:
        print('...[truncated, %d chars]' % len(b))
    print()
