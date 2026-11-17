import json, sys, csv, re
sys.path.insert(0, "scripts")
HERE = "."
res = json.load(open("out/diff_rows.json", encoding="utf-8"))
import importlib.util
# csv vs tex: show the single op for three rows
spec = importlib.util.spec_from_file_location("s3", "scripts/s3_diff.py")
