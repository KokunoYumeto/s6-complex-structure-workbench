#!/usr/bin/env python3
"""Apply a reviewed, sequential set of guarded exact replacements atomically."""
import argparse,json
from S6_SERIES_PUBLISH_editing import Editor
p=argparse.ArgumentParser();p.add_argument('paper');p.add_argument('patch');a=p.parse_args()
e=Editor(a.paper)
data=json.load(open(a.patch))
rows=data.get('patches',[]) if isinstance(data,dict) else data
for r in rows:
 e.replace(r.get('old_text',r.get('old')),r.get('new_text',r.get('new')),r.get('type','D24'),r.get('reason','Apply the integrated mathematical review repair; see the matching review record for the derivation.'),r.get('location',r.get('id','')),r.get('expected_count',1))
e.save()
