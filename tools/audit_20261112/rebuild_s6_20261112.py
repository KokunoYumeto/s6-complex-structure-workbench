r"""Audit of 12 November 2026: rebuild the S6 upload folders in sending order, with one merge.

Old -> new:  S6_2_INVARIANTS -> S6_01_INVARIANTS;  S6_3_FAMILY -> S6_02_FAMILY;  S6_1_CDP -> S6_03_CDP;
             S6_4_MAPS + S6_5_MANIFOLDS -> S6_04_MAPS_MANIFOLDS (Parts D-F = the former Parts A-C of S6_5);
             S6_6_ARITHMETIC -> S6_05_ARITHMETIC.
Always rebuilds from the before-copies in s6_pro_prompts_20261112_work\<new>\ (PROMPT_before_audit_20261112*.md and
<old>_background.zip), which step 1 makes from the upload folders the first time it runs.
Prompt changes: wording and pointers only (outcome sections to rule 0, Parts preambles, escape hatches, two wrong or
missing pointers); no change to what the Parts ask, except that the merge renumbers.
Zip changes: local paths in the survey and the readers' notes replaced by zip paths or neutral names; prompt names in
the survey updated; MANIFEST.tsv recomputed. Everything else byte-identical.
"""
import hashlib
import io
import os
import re
import shutil
import sys
import zipfile

DOCS = r'C:\Users\user\Documents'
UP = DOCS + r'\s6_pro_prompts_20261112'
WORK = DOCS + r'\s6_pro_prompts_20261112_work'
NEW = [
    ('S6_01_INVARIANTS', ['S6_2_INVARIANTS']),
    ('S6_02_FAMILY', ['S6_3_FAMILY']),
    ('S6_03_CDP', ['S6_1_CDP']),
    ('S6_04_MAPS_MANIFOLDS', ['S6_4_MAPS', 'S6_5_MANIFOLDS']),
    ('S6_05_ARITHMETIC', ['S6_6_ARITHMETIC']),
]
OLD2NEW = {'S6_2_INVARIANTS': 'S6_01_INVARIANTS', 'S6_3_FAMILY': 'S6_02_FAMILY', 'S6_1_CDP': 'S6_03_CDP',
           'S6_4_MAPS': 'S6_04_MAPS_MANIFOLDS', 'S6_5_MANIFOLDS': 'S6_04_MAPS_MANIFOLDS',
           'S6_6_ARITHMETIC': 'S6_05_ARITHMETIC'}
TEXT_EXT = ('.md', '.tex', '.py', '.txt', '.c', '.tsv', '.json', '.bib')
STAMP = 'audit of 12 November 2026'


def sha(b):
    return hashlib.sha256(b).hexdigest()


def rep1(s, old, new, label):
    n = s.count(old)
    if n != 1:
        raise SystemExit('%s: expected 1 occurrence, found %d: %r' % (label, n, old[:80]))
    return s.replace(old, new)


def before_name(new, old, n_old):
    return 'PROMPT_before_audit_20261112.md' if n_old == 1 else 'PROMPT_before_audit_20261112_%s.md' % old


# ------------------------------------------------------------------ step 1: before-copies (first run only)
def make_before_copies():
    for new, olds in NEW:
        wd = os.path.join(WORK, new)
        os.makedirs(wd, exist_ok=True)
        for old in olds:
            src_dir = os.path.join(UP, old)
            bp = os.path.join(wd, before_name(new, old, len(olds)))
            bz = os.path.join(wd, old + '_background.zip')
            if not os.path.exists(bp):
                shutil.copyfile(os.path.join(src_dir, 'PROMPT.md'), bp)
            if not os.path.exists(bz):
                shutil.copyfile(os.path.join(src_dir, old + '_background.zip'), bz)
            for a, b in ((os.path.join(src_dir, 'PROMPT.md'), bp),
                         (os.path.join(src_dir, old + '_background.zip'), bz)):
                if os.path.exists(a) and sha(open(a, 'rb').read()) != sha(open(b, 'rb').read()):
                    raise SystemExit('before-copy differs from upload file: ' + b)


def read_before(new, old, n_old):
    return io.open(os.path.join(WORK, new, before_name(new, old, n_old)), encoding='utf-8').read()


# ------------------------------------------------------------------ shared wording changes
ENV_OLD = ('every deliverable file in full, each in its own code block headed by its file name; then continue the '
           'mathematics in the chat as far as possible.')
ENV_NEW = ('every deliverable file in full, each in its own code block headed by its file name, taken from the code '
           'that saved it; then continue the mathematics in the chat as far as possible.')

STD_NOT_ACCEPTABLE = ('a survey or a status report; "open, see [reference]"; a plan, a sample or an outline; a summary '
                      'of what would be done; a computation described and not run; an item dropped without a row.')
KNOWN_OPEN = (' A statement labelled Known counts only together with its derivation from the cited theorem, in the '
              'form needed here (rule 10); a statement labelled Open counts only as outcome (c), with all its parts '
              'on the page.')


def deliverables_item(pid):
    return ('1. **Deliverables:** the files listed under "What to deliver" below. `%s_results.csv` has one row per '
            'numbered statement, and every item of the Parts (A.1, A.2, …) is answered by at least one numbered '
            'statement, named in the column `item_of_the_prompt`. `%s_report.md` opens with a table: one line per '
            'item, giving the statement numbers that answer it and its outcome, (a), (b) or (c) of point 2.'
            % (pid, pid))


def finished_item(pid):
    return ('4. **Finished** only when every item meets the bar of 2. Anything short of it is marked "unfinished" in '
            'the table of `%s_report.md`, item by item, with what is missing. Do not present the work as complete '
            'while one such line remains.' % pid)


def common_fixes(t, label):
    t = rep1(t, ENV_OLD, ENV_NEW, label + ' env')
    return t


def outcome_fixes(t, pid, old_pid, label, not_acc_old_tail, item2_tail_old, finished_old):
    # item 1
    t = rep1(t, '1. **Deliverables:** the files listed under "What to deliver" below; `%s_results.csv` has one row '
                'for every item (A.1, A.2, …)' % old_pid, '@@D1@@', label + ' item1')
    t = re.sub(r'@@D1@@[^\n]*', lambda m: deliverables_item(pid), t, count=1)
    # item 2: append Known/Open clause after the given tail
    t = rep1(t, item2_tail_old, item2_tail_old + KNOWN_OPEN, label + ' item2')
    # item 3: replace the tail of the "not acceptable" list by the standard list
    t = rep1(t, not_acc_old_tail, STD_NOT_ACCEPTABLE, label + ' item3')
    # item 4
    t = rep1(t, finished_old, finished_item(pid), label + ' item4')
    return t


# ------------------------------------------------------------------ the five prompts
def build_invariants():
    old = 'S6_2_INVARIANTS'
    pid = 'S6_01_INVARIANTS'
    t = read_before(pid, old, 1)
    t = rep1(t, '# S6_2_INVARIANTS:', '# S6_01_INVARIANTS:', 'title')
    t = rep1(t, 'File prefix for your deliverables: `S6_2_INVARIANTS`.', 'File prefix for your deliverables: `%s`.' % pid, 'prefix')
    t = outcome_fixes(
        t, pid, old, pid,
        not_acc_old_tail='a plan; an item dropped without a row.',
        item2_tail_old='(for instance "h¹(T_X) ∈ {1, 2}, decided by the vanishing of the following explicit scalar").',
        finished_old='4. **Finished** only when every item meets the bar of 2; anything short of it is reported as unfinished, item by item.')
    t = rep1(t, 'compute that numerically by two methods, and say exactly what remains.',
             'compute that numerically by two methods, and state exactly the quantity that remains undecided, with your '
             'attack on it. Carry each Part to where it stops.', 'preamble')
    t = rep1(t, 'at least (k, l) = (1,1), (3,1), (1,5)… the first cases with gcd(3k, 4l) = 1. Say whether the Hodge numbers distinguish the families.',
             'at least (k, l) = (1,1), (3,1), (1,5) (each with gcd(3k, 4l) = 1; the admissible pairs with 3k·4l ≤ 60 are '
             '(1,1), (1,2), (3,1), (1,4), (5,1), (1,5)). Decide whether the Hodge numbers distinguish the families.', 'B.2')
    t = rep1(t, 'If explicit global representatives G, Q of the generators exist, give them.',
             'If explicit global representatives G, Q of the generators exist (the ∂̄-closed forms G ∈ A^{0,1}(X), '
             'Q ∈ A^{1,1}(X) of `workbench/bott_chern_algebra.tex`, `rem:bcpr-literal-gauge`, l. 350-372; '
             '`notes/B_notes.md`, B-17(f)), give them.', 'C.3')
    t = rep1(t, 'D.2. Describe H¹(X, T_X) explicitly:', 'D.2. Determine H¹(X, T_X) explicitly:', 'D.2')
    return pid, common_fixes(t, pid)


def build_family():
    old = 'S6_3_FAMILY'
    pid = 'S6_02_FAMILY'
    t = read_before(pid, old, 1)
    t = rep1(t, '# S6_3_FAMILY:', '# S6_02_FAMILY:', 'title')
    t = rep1(t, 'File prefix for your deliverables: `S6_3_FAMILY`.', 'File prefix for your deliverables: `%s`.' % pid, 'prefix')
    t = outcome_fixes(
        t, pid, old, pid,
        not_acc_old_tail='a plan; an item dropped without a row.',
        item2_tail_old='A number counts with its method, its precision and a second independent computation.',
        finished_old='4. **Finished** only when every item meets the bar of 2; anything short of it is reported as unfinished, item by item.')
    t = rep1(t, '## Parts\n\n**A. The classification theorem, established.**',
             '## Parts\n\nEvery Part asks for mathematics: a theorem with its proof, a counterexample given completely, or '
             'a computation done by program with its code, its output and, for a number, its precision. Where a statement '
             'resists, prove the strongest case within reach, compute, and state the obstruction as an exact statement '
             'with its smallest undecided instance. Carry each Part to where it stops.\n\n'
             '**A. The classification theorem, established.**', 'preamble')
    t = rep1(t, 'A.5. State the theorem with all hypotheses, and say exactly what it does not cover.',
             'A.5. State the theorem with all its hypotheses and its proof assembled from A.1-A.4; for each case it does '
             'not cover, give the smallest instance and your attack on it.', 'A.5')
    t = rep1(t, 'C.3. The boundary. Describe what happens as Im c → −M:', 'C.3. The boundary. Determine what happens as Im c → −M:', 'C.3')
    t = rep1(t, 'describe its closure and its behaviour at the three punctures.',
             'determine its closure and its behaviour at the three punctures.', 'F.3')
    return pid, common_fixes(t, pid)


def build_cdp():
    old = 'S6_1_CDP'
    pid = 'S6_03_CDP'
    t = read_before(pid, old, 1)
    t = rep1(t, '# S6_1_CDP:', '# S6_03_CDP:', 'title')
    t = rep1(t, 'File prefix for your deliverables: `S6_1_CDP`.', 'File prefix for your deliverables: `%s`.' % pid, 'prefix')
    t = rep1(t, '1. **Deliverables:** the files listed under "What to deliver" below; `S6_1_CDP_results.csv` has one row for every item (A.1, A.2, …) of the Parts.',
             deliverables_item(pid), 'item1')
    t = rep1(t, 'A statement of CDP98, CDP20, [AC26], the workbench or the course counts only with its proof read and rewritten by you, or refuted.',
             'A statement of CDP98, CDP20, [AC26], the workbench or the course counts only with its proof read and rewritten by you, or refuted.' + KNOWN_OPEN, 'item2')
    t = rep1(t, 'a plan or an outline; an item dropped without a row; a proof of a special case offered as the general statement.',
             'a proof of a special case offered as the general statement; ' + STD_NOT_ACCEPTABLE, 'item3')
    t = rep1(t, '4. **Finished** only when every item meets the bar of 2. Anything short of it is reported as unfinished, item by item, in `S6_1_CDP_report.md`.',
             finished_item(pid), 'item4')
    t = rep1(t, 'and state the obstruction as an exact statement with its smallest undecided instance. Carry each Part to where it stops.\n\n**A. The conormal step',
             'and state the obstruction as an exact statement with its smallest undecided instance. Where a computation '
             'can decide or test a case (the local algebra of A.2 and A.3, the cohomology groups of B.1 and B.2, the '
             'monodromy lattices of D), do it by program and attach the code and its output. Carry each Part to where it '
             'stops.\n\n**A. The conormal step', 'preamble')
    t = rep1(t, 'or the exact step that is not proved, with a counterexample if you can make one.',
             'or the exact step that is not proved, with a counterexample to it or, failing one, the obstruction stated '
             'exactly with its smallest undecided instance.', 'E.2')
    t = rep1(t, '(for X_c: every small deformation carries the pencil |−2K|, if you can prove it; `workbench/analytic_canonical_ring.tex`)',
             '(for X_c: prove that every small deformation carries the pencil |−2K|, or show where this fails; '
             '`workbench/analytic_canonical_ring.tex`)', 'E.3')
    return pid, common_fixes(t, pid)


def section(t, start, end):
    a = t.index(start)
    b = t.index(end, a + len(start))
    return t[a + len(start):b]


def build_maps_manifolds():
    pid = 'S6_04_MAPS_MANIFOLDS'
    m = read_before(pid, 'S6_4_MAPS', 2)
    n = read_before(pid, 'S6_5_MANIFOLDS', 2)
    W, O, L, P = '## What is to be settled\n\n', '## What the outcome must be\n\n', '## Leads (unverified; prove or refute each)\n\n', '## Parts\n\n'
    m_settled = section(m, W, O).rstrip()
    n_settled = section(n, W, O).rstrip()
    outcome = section(m, O, L)
    if outcome != section(n, O, L).replace('S6_5_MANIFOLDS', 'S6_4_MAPS'):
        raise SystemExit('the two outcome sections differ beyond the prefix')
    m_leads = section(m, L, P)
    n_leads = section(n, L, P)
    m_parts = section(m, P, '\n---\n')
    n_parts = section(n, P, '\n---\n')
    common = m[m.index('\n---\n'):]
    if common != n[n.index('\n---\n'):]:
        raise SystemExit('the two common blocks differ')
    # settled: split each into intro, "Where the matter stands" list, closing sentence
    m_intro, m_rest = m_settled.split('\n\nWhere the matter stands', 1)
    n_intro, n_rest = n_settled.split('\n\nWhere the matter stands', 1)
    m_list, m_close = m_rest.rsplit('\n\nThis prompt asks for the theorems:', 1)
    n_list, n_close = n_rest.rsplit('\n\nThis prompt asks for the manifolds:', 1)
    settled = ('**I. The maps (Parts A-C).** ' + m_intro + '\n\nWhere the matter stands' + m_list +
               '\n\n**II. The manifolds (Parts D-F).** ' + n_intro + '\n\nWhere the matter stands' + n_list +
               '\n\nThis prompt asks for the theorems on the maps:' + m_close.rstrip().rstrip('.') +
               ' (Parts A-C); and for the manifolds:' + n_close.rstrip().rstrip('.') + ' (Parts D-F).\n\n')
    # leads: renumber S6_5's Leads 1-3 as 5-7
    m_from, m_body = m_leads.split('\n\n', 1)
    n_from, n_body = n_leads.split('\n\n', 1)
    n_body = rep1(n_body, '- **Lead 1 (the members with |p| > 1).**', '- **Lead 5 (the members with |p| > 1).**', 'lead5')
    n_body = rep1(n_body, '- **Lead 2 (the fourfold).**', '- **Lead 6 (the fourfold).**', 'lead6')
    n_body = rep1(n_body, '- **Lead 3 (dimension eight).**', '- **Lead 7 (dimension eight).**', 'lead7')
    if not (m_from.startswith('From the survey') and n_from.startswith('From the survey')):
        raise SystemExit('unexpected Leads source lines')
    leads_from = ('Leads 1-4 come from' + m_from[len('From'):].rstrip().rstrip('.') + '; Leads 5-7 from' +
                  n_from[len('From'):].rstrip().rstrip('.') + '.')
    leads = leads_from + '\n\n' + m_body.rstrip() + '\n' + n_body.rstrip() + '\n\n'
    # parts: preamble merged; S6_5 A, B, C -> D, E, F
    m_pre, m_items = m_parts.split('\n\n', 1)
    n_pre, n_items = n_parts.split('\n\n', 1)
    pre = ('Every Part asks for mathematics: a theorem with its proof, a manifold identified with proof, a construction '
           'carried out, or a computation or search checked by program, with its code and its bounds. Where a class, a '
           'manifold or a construction resists, prove the strongest partial statement, compute, and state the obstruction '
           'exactly with its smallest undecided instance. Carry each Part to where it stops.')
    for a, b in (('**A. The other manifolds.**', '**D. The other manifolds.**'),
                 ('**B. The fibre-product fourfold.**', '**E. The fibre-product fourfold.**'),
                 ('**C. A 3-connected complex fourfold fibred in 3-tori?**', '**F. A 3-connected complex fourfold fibred in 3-tori?**')):
        n_items = rep1(n_items, a, b, 'part heading')
    for a, b in (('\nA.1. ', '\nD.1. '), ('\nA.2. ', '\nD.2. '), ('\nA.3. ', '\nD.3. '), ('\nB.1. ', '\nE.1. '),
                 ('\nB.2. ', '\nE.2. '), ('\nC.1. ', '\nF.1. '), ('\nC.2. ', '\nF.2. '), ('\nC.3. ', '\nF.3. '),
                 ('\nC.4. ', '\nF.4. ')):
        n_items = rep1(n_items, a, b, 'item ' + a.strip())
    n_items = rep1(n_items, 'D.1. Prove or refute Lead 1:', 'D.1. Prove or refute Lead 5:', 'ref lead5')
    n_items = rep1(n_items, '(identified by A.1\'s method)', '(identified by D.1\'s method)', 'ref D.1')
    n_items = rep1(n_items, 'E.1. Prove or refute Lead 2:', 'E.1. Prove or refute Lead 6:', 'ref lead6')
    n_items = rep1(n_items, 'F.1. Prove the facts of Lead 3', 'F.1. Prove the facts of Lead 7', 'ref lead7')
    n_items = rep1(n_items, 'no datum of type C.2 gives', 'no datum of type F.2 gives', 'ref F.2')
    if re.search(r'\b[ABC]\.\d\b', n_items):
        raise SystemExit('stray A./B./C. reference left in the former S6_5 parts: %s' % re.findall(r'.{30}\b[ABC]\.\d\b.{10}', n_items))
    if re.search(r'Lead [1-4]\b', n_items):
        raise SystemExit('stray Lead 1-4 reference in the former S6_5 parts')
    parts = pre + '\n\n' + m_items.rstrip() + '\n\n' + n_items.rstrip() + '\n'
    title = ('# S6_04_MAPS_MANIFOLDS: the maps from the complex S^6 to S^3, S^2 and S^4 given by its torus fibration, and '
             'their homotopy classes; the other manifolds the construction gives (covers, other elliptic surfaces, the '
             'conifold transition, the fibre-product fourfold, a 3-connected analogue in dimension eight)\n\n'
             'Development prompt, 12 November 2026. File prefix for your deliverables: `%s`.\n\n' % pid)
    outcome = outcome.replace('S6_4_MAPS', pid)
    t = title + W + settled + O + outcome + L + leads + P + parts + common
    t = outcome_fixes(
        t, pid, pid, pid,
        not_acc_old_tail='a plan; an item dropped without a row.',
        item2_tail_old='what was computed by program, and the exact undecided instance.',
        finished_old='4. **Finished** only when every item meets the bar of 2; anything short of it is reported as unfinished, item by item.')
    return pid, common_fixes(t, pid)


def build_arithmetic():
    old = 'S6_6_ARITHMETIC'
    pid = 'S6_05_ARITHMETIC'
    t = read_before(pid, old, 1)
    t = rep1(t, '# S6_6_ARITHMETIC:', '# S6_05_ARITHMETIC:', 'title')
    t = rep1(t, 'File prefix for your deliverables: `S6_6_ARITHMETIC`.', 'File prefix for your deliverables: `%s`.' % pid, 'prefix')
    t = outcome_fixes(
        t, pid, old, pid,
        not_acc_old_tail='a plan; an item dropped without a row.',
        item2_tail_old='For a group or a lattice: generators, order, and the program that verifies them.',
        finished_old='4. **Finished** only when every item meets the bar of 2; anything short of it is reported as unfinished, item by item.')
    t = rep1(t, '## Parts\n\n**A. The count.**',
             '## Parts\n\nEvery Part asks for mathematics: a theorem with its proof, or an exact computation by program with '
             'its code and output. Where a statement resists, prove the strongest case within reach, compute, and state '
             'the obstruction as an exact statement with its smallest undecided instance. Carry each Part to where it '
             'stops.\n\n**A. The count.**', 'preamble')
    t = rep1(t, 'or say what blocks it;', 'or state exactly what blocks it;', 'A.5 omega')
    t = rep1(t, 'extend the exact count to 10⁹ if your environment allows',
             'extend the exact count to 10⁹ (if the environment stops you earlier, state the range reached)', 'A.5 census')
    return pid, common_fixes(t, pid)


# ------------------------------------------------------------------ zip members
PATH_RULES = [
    ('the local Codex workspace `<DOCS>\\math\\research\\s6_recent_results_main` (LW)', 'the local Codex workspace (LW)'),
    ('Copies: `<DOCS>\\s6_pro_prompts_20261112_work\\literature\\`.',
     'Copies of the papers a prompt uses are attached under `papers/` in its background zip.'),
    ('`<DOCS>\\workbench_review_20261112\\repo\\s6\\STATUS_2026-10-05.md`', '`status/STATUS_2026-10-05.md`'),
    ('<DOCS>\\math\\research\\s6_recent_results_main', 'LW'),
]
SCRATCH_RE = re.compile(r'<DOCS>\\workbench_review_20261112\\work\\scratch\\([A-Za-z0-9]+)\\([A-Za-z0-9_.]*)')
REL_SCRATCH_RE = re.compile(r'(?<![A-Za-z0-9_/])work\\scratch\\([A-Za-z0-9]+)\\([A-Za-z0-9_.]*)')


def sanitize_member(name, s, members):
    for a, b in PATH_RULES:
        s = s.replace(a, b)

    def scratch(mo):
        reader, f = mo.group(1), mo.group(2)
        if f and ('notes/scripts/%s_%s' % (reader, f)) in members:
            return 'notes/scripts/%s_%s' % (reader, f)
        if not f:
            return 'notes/scripts/%s_*' % reader
        return 'the reader\'s scratch file %s' % f
    s = SCRATCH_RE.sub(scratch, s)
    # relative references to the review's local folders
    s = s.replace('(clone in `repo\\`)', '(a local clone)')
    s = s.replace('repo\\s6\\STATUS_2026-10-05.md', 'status/STATUS_2026-10-05.md')
    s = s.replace('work\\*_notes.md', 'notes/*_notes.md').replace('work\\<reader>_notes.md', 'notes/<reader>_notes.md')
    s = re.sub(r'work\\([A-Za-z0-9]+)_notes\.md', r'notes/\1_notes.md', s)
    s = REL_SCRATCH_RE.sub(scratch, s)
    return s


def survey_update(s):
    s = rep1(s, 'Prompts: S6_1_CDP, S6_2_INVARIANTS, S6_3_FAMILY, S6_4_MAPS, S6_5_MANIFOLDS, S6_6_ARITHMETIC\n(`<DOCS>\\s6_pro_prompts_20261112\\`).',
             'Prompts, in sending order: S6_01_INVARIANTS, S6_02_FAMILY, S6_03_CDP, S6_04_MAPS_MANIFOLDS,\nS6_05_ARITHMETIC.', 'survey prompts line')
    s = rep1(s, 'Six prompts, each built for one Pro run.', 'Five prompts, each built for one Pro run.', 'survey six')
    s = rep1(s, '`LW\\source_text_blobs\\aca0913df424f72b0efc94546498f1f427786191628503ff56208f4153060abb.tex`',
             '`correction_note/N_singular_fibre_vanishing_step.tex` (attached to S6_03_CDP)', 'survey [N]')
    s = rep1(s, 'its `s6\\STATUS_2026-10-05.md` is', 'its `s6/STATUS_2026-10-05.md` (attached as `status/STATUS_2026-10-05.md`) is', 'survey status')
    # the table
    a = s.index('| Prompt | What it asks to crack | Findings |')
    b = s.index('\n\n', a)
    rows = {}
    for line in s[a:b].split('\n')[2:]:
        mo = re.match(r'\| `([^`]+)` \| (.*) \| ([^|]*) \|$', line)
        rows[mo.group(1)] = (mo.group(2), mo.group(3))
    new_rows = ['| Prompt | What it asks to crack | Findings |', '|---|---|---|']
    for pid, olds in NEW:
        parts_ = [rows[o][0] for o in olds]
        what = '; '.join([parts_[0]] + [x[0].lower() + x[1:] for x in parts_[1:]])
        fnd = '; '.join(rows[o][1] for o in olds)
        new_rows.append('| `%s` | %s | %s |' % (pid, what, fnd))
    s = s[:a] + '\n'.join(new_rows) + s[b:]
    s = rep1(s, 'Order by interest: S6_2_INVARIANTS and S6_3_FAMILY first, then S6_1_CDP, S6_4_MAPS, S6_5_MANIFOLDS, S6_6_ARITHMETIC.\n'
                'They do not depend on one another. S6_2 Part A.2 and S6_3 Part C.1 both evaluate μ;',
             'Sending order: S6_01_INVARIANTS, S6_02_FAMILY, S6_03_CDP, S6_04_MAPS_MANIFOLDS, S6_05_ARITHMETIC.\n'
             'They do not depend on one another. S6_01 Part A.2 and S6_02 Part C.1 both evaluate μ;', 'survey order')
    s = re.sub(r'S6_5_MANIFOLDS, Parts? ([A-C])', lambda mo: 'S6_04_MAPS_MANIFOLDS, Part ' + 'DEF'['ABC'.index(mo.group(1))], s)
    for o, nw in OLD2NEW.items():
        s = s.replace(o, nw)
    if re.search(r'S6_[1-6]_[A-Z]', s):
        raise SystemExit('old prompt name left in survey: %s' % re.findall(r'S6_[1-6]_[A-Z]+', s))
    return s


def build_zip(pid, olds):
    wd = os.path.join(WORK, pid)
    members, origin = {}, {}
    manifest_rows = {}
    for old in olds:
        z = zipfile.ZipFile(os.path.join(wd, old + '_background.zip'))
        man = z.read('MANIFEST.tsv').decode('utf-8').split('\n')
        header = man[0].split('\t')
        for line in man[1:]:
            if line.strip():
                row = dict(zip(header, line.split('\t')))
                p = row['path_in_zip']
                if p in manifest_rows and manifest_rows[p]['sha256'] != row['sha256']:
                    raise SystemExit('same path, different content in the merged zips: ' + p)
                manifest_rows.setdefault(p, row)
        for i in z.infolist():
            if i.filename == 'MANIFEST.tsv' or i.filename.endswith('/'):
                continue
            data = z.read(i)
            if i.filename in members and members[i.filename] != data:
                raise SystemExit('same path, different bytes in the merged zips: ' + i.filename)
            members[i.filename] = data
    if set(members) != set(manifest_rows):
        raise SystemExit('manifest and members differ in the before-zips')
    changed = []
    names = set(members)
    for p in sorted(members):
        if p.endswith(TEXT_EXT):
            s = members[p].decode('utf-8')
            s2 = sanitize_member(p, s, names)
            if p == 'S6_SURVEY_20261112.md':
                s2 = survey_update(s2)
            if '<DOCS>' in s2 or '<HOME>' in s2:
                raise SystemExit('local path left in ' + p)
            if p != 'S6_SURVEY_20261112.md' and re.search(r'S6_[1-6]_[A-Z]', s2):
                print('WARNING: old prompt name in %s: %s' % (p, sorted(set(re.findall(r'S6_[1-6]_[A-Z]+', s2)))))
            if s2 != s:
                members[p] = s2.encode('utf-8')
                changed.append(p)
    rows = []
    for p in sorted(members):
        r = manifest_rows[p]
        org = r['origin']
        if p in changed:
            org += '; local paths replaced by zip paths or neutral names' + (
                ', prompt names updated' if p == 'S6_SURVEY_20261112.md' else '') + ' (%s)' % STAMP
        rows.append((p, org, str(len(members[p])), sha(members[p]), r['why_attached']))
    man_text = 'path_in_zip\torigin\tbytes\tsha256\twhy_attached\n' + ''.join('\t'.join(r) + '\n' for r in rows)
    return members, man_text, changed


# ------------------------------------------------------------------ main
def main():
    make_before_copies()
    built = []
    for fn in (build_invariants, build_family, build_cdp, build_maps_manifolds, build_arithmetic):
        pid, text = fn()
        olds = dict(NEW)[pid]
        members, man_text, changed = build_zip(pid, olds)
        out = os.path.join(UP, pid)
        if os.path.isdir(out):
            shutil.rmtree(out)
        os.makedirs(out)
        with io.open(os.path.join(out, 'PROMPT.md'), 'w', encoding='utf-8', newline='\n') as f:
            f.write(text)
        zpath = os.path.join(out, pid + '_background.zip')
        with zipfile.ZipFile(zpath, 'w', zipfile.ZIP_DEFLATED) as z:
            z.writestr('MANIFEST.tsv', man_text.encode('utf-8'))
            for p in sorted(members):
                z.writestr(p, members[p])
        with io.open(os.path.join(WORK, pid, 'MANIFEST.tsv'), 'w', encoding='utf-8', newline='\n') as f:
            f.write(man_text)
        built.append((pid, len(members) + 1, os.path.getsize(zpath), changed))
    for pid, n, size, changed in built:
        print('%-22s files in zip: %3d  zip: %.2f MB  changed members: %s' % (pid, n, size / 1e6, changed))
    if '--remove-old' in sys.argv:
        for new, olds in NEW:
            for old in olds:
                d = os.path.join(UP, old)
                if os.path.isdir(d):
                    for f in os.listdir(d):
                        a = os.path.join(d, f)
                        b = os.path.join(WORK, new, before_name(new, old, len(olds)) if f == 'PROMPT.md' else f)
                        if sha(open(a, 'rb').read()) != sha(open(b, 'rb').read()):
                            raise SystemExit('not removing %s: its copy in the work tree differs' % a)
                    shutil.rmtree(d)
                    print('removed old upload folder', old, '(kept in the work tree)')


if __name__ == '__main__':
    main()
