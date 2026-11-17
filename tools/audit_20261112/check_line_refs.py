"""Check that every line reference of an S6 prompt falls inside the file it names (read only)."""
import io
import os
import re
import sys
import zipfile

for folder in sys.argv[1:]:
    name = os.path.basename(folder)
    prompt = io.open(os.path.join(folder, 'PROMPT.md'), encoding='utf-8').read()
    z = zipfile.ZipFile(os.path.join(folder, name + '_background.zip'))
    lines = {}
    for i in z.infolist():
        if i.filename.endswith(('.tex', '.md')):
            lines[i.filename] = z.read(i).decode('utf-8', 'replace').count('\n') + 1
    print('=====', name)
    bad = 0
    # `file` ... l. a-b, c-d  (within the same parenthesis/sentence, up to 200 chars)
    for m in re.finditer(r'`((?:workbench|course|correction_note|original)/[^`]+)`([^`]{0,220})', prompt):
        f, tail = m.group(1), m.group(2)
        tail = re.split(r'[;)]', tail)[0]
        nums = [int(x) for x in re.findall(r'(?<![\d.§])(\d{2,5})(?![\d.])', ' '.join(re.findall(r'l\. ?[\d\-–, ]+', tail)))]
        if not nums:
            continue
        n = lines.get(f)
        if n is None:
            print('  missing file for line ref:', f)
            bad += 1
            continue
        if max(nums) > n:
            print('  OUT OF RANGE: %s has %d lines, prompt cites %s' % (f, n, nums))
            bad += 1
    tl = lines.get('original/AC26_transcription.tex')
    tnums = [int(x) for x in re.findall(r'T l\. ?(\d+)', prompt)] + [int(b) for a, b in re.findall(r'T l\. ?(\d+)-(\d+)', prompt)]
    if tnums:
        print('  transcription: %d lines; max T l. cited %d' % (tl, max(tnums)))
        if max(tnums) > tl:
            bad += 1
    print('  line references out of range:', bad)
