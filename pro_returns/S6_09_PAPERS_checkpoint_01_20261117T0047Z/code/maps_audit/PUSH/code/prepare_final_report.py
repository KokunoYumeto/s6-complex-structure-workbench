#!/usr/bin/env python3
"""Preserve the former report generator, then install the final assembler."""
from pathlib import Path
import ast, hashlib, json
root = Path(__file__).resolve().parents[1]
oldpath = root / "code/refresh_report.py"
old = oldpath.read_text()
archive = root / "evidence/refresh_report_before_final.py"
assert not archive.exists(), "One-shot preservation has already run"
archive.write_text(old)
tree = ast.parse(old)
head = None
order = []
for node in tree.body:
    if isinstance(node, ast.Assign):
        for target in node.targets:
            if isinstance(target, ast.Name) and target.id == "head":
                head = ast.literal_eval(node.value)
            if isinstance(target, ast.Name) and target.id == "additional_reports":
                order.extend(ast.literal_eval(node.value))
    if isinstance(node, ast.For) and isinstance(node.iter, ast.List):
        values = ast.literal_eval(node.iter)
        if all(isinstance(value, str) and value.endswith(".md") for value in values):
            order = values + order
assert head is not None
start = head.index("## Execution and retention")
(root/"sections/execution_history_through_checkpoint09.md").write_text(head[start:])
(root/"code/report_record_order.json").write_text(json.dumps(order, indent=2)+"\n")
new = (root/"code/refresh_report_final.py").read_text()
oldpath.write_text(new)
print(json.dumps({"preserved": str(archive.relative_to(root)),
                  "old_sha256": hashlib.sha256(old.encode()).hexdigest(),
                  "historical_record_order_count": len(order),
                  "new_generator_sha256": hashlib.sha256(new.encode()).hexdigest()}, indent=2))
