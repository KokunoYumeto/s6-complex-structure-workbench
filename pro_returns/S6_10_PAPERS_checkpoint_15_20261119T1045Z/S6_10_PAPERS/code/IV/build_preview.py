"""Build the current receiving IV preview and record exact production hashes.

The local wrapper intentionally leaves external-paper references and the
shared bibliography to the root standalone builder. Its actual diagnostics
are reported and never treated as mathematical proof checks.
"""
from pathlib import Path
import hashlib
import json
import os
import re
import subprocess
from datetime import datetime, timezone

W = Path(__file__).resolve().parents[2]
P = W/'papers/IV'
B = W/'analysis/IV/preview'
B.mkdir(parents=True, exist_ok=True)
env=os.environ.copy()
env.update(json.loads((W/'build/tex_runtime/environment.json').read_text()))
sources=[W/'preamble.tex', P/'frontmatter.tex', P/'opening.tex', P/'body.tex']
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
text=sources[0].read_text()+'\n\\begin{document}\n'+'\n'.join(p.read_text() for p in sources[1:])+'\n\\end{document}\n'
tmp=B/'preview.tex.tmp';tmp.write_text(text);tmp.replace(B/'preview.tex')
manifest={'started_at':datetime.now(timezone.utc).isoformat(),
 'source_checkpoint':30,'source_files':[{'file':str(p.relative_to(W)), 'sha256':sha(p)} for p in sources],
 'operation':'two-pass local layout preview; external bibliography and other-paper references are integrated by the root canonical builder',
 'passes':[]}
for n in range(1,3):
    stdout=B/f'cp30_pass{n}.stdout'
    with stdout.open('w') as out:
        result=subprocess.run(['lualatex','-interaction=nonstopmode','-halt-on-error','-file-line-error','preview.tex'],cwd=B,env=env,stdout=out,stderr=subprocess.STDOUT)
    manifest['passes'].append({'pass':n,'exit_code':result.returncode,'stdout':str(stdout.relative_to(W))})
    print('IV preview pass',n,'exit',result.returncode,flush=True)
    if result.returncode:
        manifest['completed_at']=datetime.now(timezone.utc).isoformat()
        (W/'analysis/IV/cp30_preview_build.json').write_text(json.dumps(manifest,indent=2)+'\n')
        print(stdout.read_text()[-5000:],flush=True)
        raise SystemExit(result.returncode)
log=(B/'preview.log').read_text(errors='replace')
widths=[float(x) for x in re.findall(r'Overfull \\hbox \(([0-9.]+)pt too wide\)',log)]
manifest.update(completed_at=datetime.now(timezone.utc).isoformat(),
    files=[{'file':str(p.relative_to(W)),'sha256':sha(p),'bytes':p.stat().st_size} for p in [B/'preview.tex',B/'preview.pdf',B/'preview.log',B/'preview.aux']],
    diagnostics={'overfull_hboxes':len(widths),'max_overfull_pt':max(widths,default=0),
        'font_substitution_warnings':len(re.findall(r'Font shape .* undefined|Some font shapes were not available',log)),
        'missing_character_messages':len(re.findall(r'Missing character:',log)),
        'undefined_reference_occurrences':len(re.findall(r'Reference .* undefined',log)),
        'undefined_citation_occurrences':len(re.findall(r'Citation .* undefined',log))},
    visual_inspection='pending; build success does not certify the rendered pages')
(W/'analysis/IV/cp30_preview_build.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps(manifest['diagnostics']),flush=True)
