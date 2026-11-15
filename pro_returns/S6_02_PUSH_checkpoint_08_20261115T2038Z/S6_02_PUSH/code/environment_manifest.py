#!/usr/bin/env python3
"""Record the actual computation environment without listing secrets or env vars."""
import sys,platform,json,importlib.metadata,subprocess
from pathlib import Path
packages={}
for name in ['python-flint','sympy','numpy','scipy','mpmath','PyMuPDF','Pillow','reportlab']:
    try:packages[name]=importlib.metadata.version(name)
    except importlib.metadata.PackageNotFoundError:packages[name]='not installed'
commands={}
for name in ['lualatex','bibtex','pdftotext','pdftoppm']:
    try:
        r=subprocess.run([name,'--version' if name in ['lualatex','bibtex'] else '-v'],capture_output=True,text=True,timeout=10)
        commands[name]=(r.stdout+r.stderr).splitlines()[:3]
    except Exception as exc:commands[name]=str(exc)
record={'python':sys.version,'platform':platform.platform(),'packages':packages,'commands':commands}
Path(__file__).with_suffix('.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
