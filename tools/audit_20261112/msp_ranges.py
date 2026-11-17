"""Manuscript-page ranges (\\msp marks) of the corrected Derivateurs chunks (read only)."""
import io
import os
import re

CF = r'C:\Users\user\Documents\derivateurs_companion_20261109\corrected_french_20261111'
for n in ['DER_III-V', 'DER_VII-a', 'DER_VII-b', 'DER_VII-c', 'DER_VIII-X', 'DER_XIIapp']:
    s = io.open(os.path.join(CF, n + '.tex'), encoding='utf-8').read()
    marks = re.findall(r'\\msp\{([^}]*)\}', s)
    chap = re.findall(r'\\(?:chapter|section)\*?\{([^}]{0,60})', s)
    print('%-11s %3d marks; first %s; last %s' % (n, len(marks), marks[:4], marks[-4:]))
    # chapter changes: where the page numbers restart
    restarts = [marks[i] for i in range(1, len(marks)) if re.sub(r'\D', '', marks[i]) and re.sub(r'\D', '', marks[i - 1])
                and int(re.sub(r'\D', '', marks[i])) < int(re.sub(r'\D', '', marks[i - 1]))]
    print('            page-number restarts at: %s; headings: %s' % (restarts[:6], chap[:6]))
