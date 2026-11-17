"""Preserve the initial structural-equality failure, then compare expanded maps."""
from pathlib import Path
import shutil

here=Path(__file__).resolve().parent
attempt=here/'attempts/source_zero_prism_structural_equality'
attempt.mkdir(parents=True,exist_ok=True)
for suffix in ['py','out','err']:
    p=here/f'source_zero_prism_fan.{suffix}'
    shutil.copy2(p,attempt/p.name)
p=here/'source_zero_prism_fan.py'
s=p.read_text()
old='translation * vector == ray(Pside,z+s.Matrix([n1,n2]),side)'
new='(translation * vector - ray(Pside,z+s.Matrix([n1,n2]),side)).applyfunc(s.expand) == s.zeros(4,1)'
assert s.count(old)==1
p.write_text(s.replace(old,new))
(attempt/'correction.md').write_text(
    'The initial period-ray check used structural equality of SymPy expressions. '
    'The entries differ only by unexpanded distributive products. The corrected '
    'check subtracts the two actual lattice maps and expands every entry before '
    'comparison with the zero matrix. The original source and output remain here.\n'
)
print('Preserved the initial structural-equality failure and corrected its exact comparison.')
