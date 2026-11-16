"""Compile the standalone deliverable twice with a standard LuaLaTeX installation."""
from pathlib import Path
import argparse, os, subprocess, sys

parser = argparse.ArgumentParser()
parser.add_argument('--workspace-runtime', action='store_true', help='Use the recorded repair of this assembly workspace, if present.')
args = parser.parse_args()
paper_dir = Path(__file__).resolve().parents[2]
os.chdir(paper_dir)
env = None
if args.workspace_runtime:
    from tex_env import tex_environment
    env = tex_environment()
for i in range(1, 3):
    run = subprocess.run(['lualatex', '-interaction=nonstopmode', '-halt-on-error', 'S6_07_PAPER_paper.tex'], env=env)
    if run.returncode:
        sys.exit(run.returncode)
