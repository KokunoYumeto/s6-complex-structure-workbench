"""Read-only source-dependency aid for splitting Paper III's elliptic block.

Only statement headings, permanent labels and explicit reference commands are
reported. No closed LG original/historical input is opened or printed.
This is a working reordering aid, not a refreshed inventory or a proof check.
"""
from bisect import bisect_right
from collections import defaultdict
import contextlib
import io
import re

import S6_SERIES_PUBLISH_c8_integrate_repairs as repairs

source = repairs.read(repairs.SOURCE)
with contextlib.redirect_stdout(io.StringIO()):
    progress, packets, edits, unguarded = repairs.collect(source, repairs.EXTRA_ADMITTED)
    projected, applications = repairs.simulate(source, packets, edits)

begin = projected.index(r"\begin{document}")
protected = projected.index(r"\section{Limits and open points}", begin)
body = projected[begin:protected]
environments = "theorem|proposition|lemma|corollary|definition|remark|example|computed|cited|statement|auditrecord|test|refuted|question|openq"
opening = re.compile(r"(?m)^\\begin\{(" + environments + r")\}")
statements = []
for match in opening.finditer(body):
    # Permanent tag and owner label occur in the statement's header, including
    # the few headers whose mathematical title spans more than one source line.
    head = body[match.start():match.start() + 1400]
    identity = re.search(r"\\hypertarget\{tag-([0-9A-Z]{4})\}\{\}\s*\\label\{([^}]+)\}", head)
    if not identity:
        continue
    prefix = head[:identity.start()]
    if r"\begin{proof}" in prefix or len(prefix) > 900:
        continue
    title = prefix[len(match[0]):].strip()
    if title.startswith("[") and title.endswith("]"):
        title = title[1:-1]
    statements.append({"start": begin + match.start(), "tag": identity[1],
                       "label": identity[2], "title": " ".join(title.split()),
                       "environment": match[1]})

starts = [r["start"] for r in statements]
label_owner = {}
for match in repairs.LABEL.finditer(projected, begin, protected):
    index = bisect_right(starts, match.start()) - 1
    if index >= 0:
        label_owner[match[1]] = statements[index]["tag"]

ref = re.compile(r"\\(?:eqref|ref|ref\*|cref|Cref|SeriesRef)\{([^}]+)\}|\\hyperref\[([^\]]+)\]")
elliptic_start = projected.index(r"\subsection{Rational elliptic starting configurations and exact computations}")
elliptic_end = projected.index(r"\subsection{Moving the zero of the linearization}", elliptic_start)
elliptic = [r for r in statements if elliptic_start <= r["start"] < elliptic_end]
elliptic_tags = {r["tag"] for r in elliptic}
edges = defaultdict(set)

def without_machine_record(text):
    token = r"\StatementRecord"
    while token in text:
        start = text.index(token)
        cursor = start + len(token)
        for argument in range(4):
            while text[cursor].isspace():
                cursor += 1
            assert text[cursor] == "{"
            depth = 1
            cursor += 1
            while depth:
                if text[cursor] == "{" and text[cursor - 1] != "\\":
                    depth += 1
                elif text[cursor] == "}" and text[cursor - 1] != "\\":
                    depth -= 1
                cursor += 1
        text = text[:start] + text[cursor:]
    return text

for n, statement in enumerate(statements):
    end = starts[n + 1] if n + 1 < len(starts) else protected
    text = without_machine_record(projected[statement["start"]:end])
    for match in ref.finditer(text):
        for key in (match[1] or match[2]).split(","):
            owner = label_owner.get(key.strip())
            if owner and owner != statement["tag"]:
                edges[statement["tag"]].add(owner)

print("ELLIPTIC_STATEMENTS", len(elliptic))
print("TAG | OWNER LABEL | TITLE | EXPLICIT IN-BLOCK REFERENCES | OTHER CURRENT-PAPER REFERENCES")
for row in elliptic:
    deps = edges[row["tag"]]
    print(" | ".join((row["tag"], row["label"], row["title"],
                      ",".join(sorted(deps & elliptic_tags)) or "-",
                      ",".join(sorted(deps - elliptic_tags)) or "-")))

# Tarjan components expose places where explicit references alone do not
# determine a total order; root must resolve their actual mathematical uses.
counter = 0
indices = {}
low = {}
stack = []
on_stack = set()
components = []

def visit(v):
    global counter
    indices[v] = low[v] = counter
    counter += 1
    stack.append(v)
    on_stack.add(v)
    for nxt in edges[v] & elliptic_tags:
        if nxt not in indices:
            visit(nxt)
            low[v] = min(low[v], low[nxt])
        elif nxt in on_stack:
            low[v] = min(low[v], indices[nxt])
    if low[v] == indices[v]:
        component = []
        while True:
            item = stack.pop()
            on_stack.remove(item)
            component.append(item)
            if item == v:
                break
        components.append(sorted(component))

for row in elliptic:
    if row["tag"] not in indices:
        visit(row["tag"])
print("MULTI_STATEMENT_REFERENCE_COMPONENTS")
for component in components:
    if len(component) > 1:
        print(",".join(component))

print("LATER CARRIER / COLLISION / CLASSIFICATION HEADINGS")
later_start = projected.index(r"\section{Local covers, global quotients and cusp carriers}")
for row in statements:
    if later_start <= row["start"] < protected:
        print(" | ".join((row["tag"], row["label"], row["title"])))

print("CLOSED_LG_TARGET_EXCLUDED; no source or record mutation")
