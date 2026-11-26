#!/usr/bin/env python3
"""Fetch the exact pinned section-ten program sources; do not execute them."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
CACHE = ROOT.parents[1] / 'tmp/c3_programs'
CACHE.mkdir(parents=True, exist_ok=True)
prior = json.loads((CACHE / 'programs160_metadata.json').read_text())[0]
base_url = prior['url'][:-len(prior['repository_path'])]
inventory = set((ROOT.parent / 'REPOSITORY_PROGRAM_PATHS.txt').read_text().splitlines())
names = [
    'A_mixed_cycles.py', 'A_rooted_hopf_trees.py', 'A_tree_periods.py',
    'A_twistor_log_cycles.py', 'D_all_weighted_cycles.py',
    'D_hopf_cycle_matrices.py', 'D_quasibundle_trees.py',
    'D_weighted_hopf_cycles.py', 'E_hopf_graph_reduction.py',
    'E_hopf_tree_heights.py', 'E_hopf_tree_pruning.py',
    'root_all_diagonal_cycles.py', 'root_mixed_hopf_stars.py',
]
prefix = 'pro_returns/S6_03_CDP_checkpoint_13_20261116T0136Z/S6_03_CDP/code/'

def fetch(name):
    path = prefix + name
    assert path in inventory
    url = base_url + path
    with urllib.request.urlopen(url, timeout=45) as response:
        assert response.status == 200
        content = response.read()
    content.decode('utf-8')
    local = CACHE / ('162_' + name)
    local.write_bytes(content)
    return dict(printed_path=path, repository_path=path,
        sha256=hashlib.sha256(content).hexdigest(), bytes=len(content),
        url=url, local_path=str(local))

with ThreadPoolExecutor(max_workers=6) as pool:
    data = list(pool.map(fetch, names))
(CACHE / 'programs162_metadata.json').write_text(
    json.dumps(data, indent=2) + '\n', newline='\n')
for row in data:
    print(Path(row['local_path']).name, row['bytes'], row['sha256'])
print('Downloaded complete sources only; no listed program executed.')
