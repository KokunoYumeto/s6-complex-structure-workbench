"""Read only the completed bounded alias MWE's source, aux, and PDF links."""
from collections import Counter
from pathlib import Path
import re
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
CODE = ROOT / "code"
stem = "S6_SERIES_PUBLISH_c8_tex_alias_"
before = (CODE / (stem + "baseline_adjacent.tex")).read_text().split(r"\begin{document}", 1)[1]
after = (CODE / (stem + "patched_3.tex")).read_text().split(r"\begin{document}", 1)[1]
assert before == after, "The diagnostic body changed"
print("Baseline/patched diagnostic bodies are byte-identical after begin{document}.")

source_labels = Counter(re.findall(r"\\label(?:\[[^\]]+\])?\{([^}]+)\}", after))
source_targets = Counter(re.findall(r"\\hypertarget\{([^}]+)\}", after))
aux = (CODE / (stem + "patched_3.aux")).read_text()
label_rows = re.findall(
    r"\\newlabel\{([^}]+)\}\{\{([^}]*)\}\{([^}]*)\}\{([^}]*)\}\{([^}]*)\}\{([^}]*)\}\}",
    aux,
)
labels = {row[0]: row[1:] for row in label_rows if not row[0].endswith("@cref")}
written_labels = Counter(row[0] for row in label_rows if not row[0].endswith("@cref"))
assert source_labels == written_labels, "A literal label was lost or repeated"
print(f"All {sum(source_labels.values())} literal labels have one corresponding aux entry.")

pdf = PdfReader(ROOT / "agents/continuation8_tex_runtime/aliases" / (stem + "patched.pdf"))
destinations = pdf.named_destinations

def name_keys(node):
    node = node.get_object()
    names = node.get("/Names", [])
    for index in range(0, len(names), 2):
        yield str(names[index])
    for child in node.get("/Kids", []):
        yield from name_keys(child)

destination_counts = Counter(name_keys(pdf.trailer["/Root"]["/Names"]["/Dests"]))
for name, count in source_targets.items():
    assert destination_counts[name] == count == 1, (name, count, destination_counts[name])
    destination = destinations[name]
    print(f"Explicit target {name}: exactly once, page {pdf.get_destination_page_number(destination)+1}")

for key, (number, page, title, target, extra) in labels.items():
    assert target in destinations, (key, target)
    print(f"Label {key}: number={number}, page={page}, live target={target}")

links = []
for page_index, page in enumerate(pdf.pages, 1):
    for reference in page.get("/Annots", []):
        annotation = reference.get_object()
        action = annotation.get("/A", {})
        if action.get("/S") == "/GoTo":
            target = str(action["/D"])
            assert target in destinations, (page_index, target)
            links.append(target)
print(f"All {len(links)} internal GoTo annotations resolve to named PDF destinations.")
print("Final pass 2/3 aux equality:", (CODE / (stem + "patched_2.aux")).read_bytes() == (CODE / (stem + "patched_3.aux")).read_bytes())
print("Read-only diagnostic; no manuscript or shared records changed.")
