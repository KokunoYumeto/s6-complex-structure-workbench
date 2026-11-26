#!/usr/bin/env python3
"""Exact receiving readback repairs and placement of the permanent GI9 tag."""
from pathlib import Path
from hashlib import sha256
import re
p=Path('agents/continuation7_iii_general_initial_receiving/S6_SERIES_PUBLISH_III_02LN_receiving.tex')
s=p.read_text()
assert sha256(s.encode()).hexdigest()=='64e2838bc235c1e3b41db162ca07248d28a1edac773d945df6803d5c0462f509'
oldids={c:re.findall(r'\\'+c+r'\{([^{}]+)\}',s) for c in ('label','hypertarget','tag')}
patches={
 'For a positive regular weight the actual charts the node charts use the':'For a positive regular weight these node charts use the',
 'diagram and all maps the rank-one quotient, specialization and cap-group maps.':'diagram and the rank-one quotient, specialization and cap-group maps above.',
 'Equation the integral rim identity kills':'The integral rim identity kills',
 'the last-boundary maps the last-boundary maps,':'the last-boundary maps,',
 'Include all fixed-normal columns the fixed-normal formula, expressed using':'Include all columns of the fixed-normal formula, expressed using',
 'all five columns the full five-column formula.':'all five columns of the displayed Thom formula.',
 'These are the actual quotient maps the short/long quotient map, the rank-one quotient map, the map \\(\\phi,\\chi\\),\n   the row \\(\\omega\\) and the three displayed killed wedges, with their sections.':'The short/long quotient, the rank-one quotient and \\((\\phi,\\chi)\\)\n   give the first two rows; the additive and multiplicative Gysin maps\n   give the last two. Their inverse sections were specified above.',
 'the boundary-kernel calculation the displayed Smith maps.':'the displayed Smith boundary maps.',
 'At a cusp these are exactly the component-disc boundary formula--the complete disc map.':'At a cusp their boundaries are exactly \\(\\mu+[v]\\), with the\ncomplete disc map displayed above.',
 r'rank in \(Mz=Pz\prime\) gives':r'rank in \(Mz=Pz\prime\) gives',
 'Writing the Smith quotient \\(\\mathbb Z^g\\oplus T\\), equations the splitting and rank identities prove':'The Smith quotient \\(\\mathbb Z^g\\oplus T\\), together with these\nsplitting and rank identities, proves',
 'the displayed Klein-four actions therefore makes':'the displayed Klein-four actions therefore make',
 'and the complete boundary kernels of the full boundary-kernel calculation give':'and the complete boundary kernels proved above give',
}
patches.pop(r'rank in \(Mz=Pz\prime\) gives')
for a,b in patches.items():
 assert s.count(a)==1,(a,s.count(a))
 s=s.replace(a,b)
s=s.replace(r'\(Mz=Pz\prime\)',r"\(Mz=Pz'\)")
old=r'''The normal-meridian map is
\[
 (y,s)\longmapsto(y-sv,\ \tau+ms).
\]
Its inverse collar map subtracts \(\tau v/m\) on the selected
root and uses \(q=s^m\).'''
new=r'''The boundary map in a lifted peripheral coordinate is
\[
 (y,\tau)\longmapsto
 \bigl(y+(\tau/m)v,\exp(2\pi i\tau/m)\bigr).
\]
Its inverse chooses a root sheet and subtracts \((\tau/m)v\);
changing the sheet is exactly the deck identification. At a fixed
lift \((y,\tau_0)\), the positive normal circle is
\(s\mapsto(y-sv,\tau_0+ms)\). The radial collar uses \(q=z^m\).'''
assert s.count(old)==1
s=s.replace(old,new)
old="Excision and Poincar\\'e--Lefschetz duality give"
new="Each nonlogarithmic cap retracts to the displayed component complex\nof real dimension at most four. Thus its fifth cohomology vanishes.\nExcision and Poincar\\'e--Lefschetz duality give"
assert s.count(old)==1;s=s.replace(old,new)
# The group argument follows its finite-core maps and precedes GI10--GI11.
start=s.index('\\smallskip\\noindent\\emph{The complete fundamental group and the exceptional extension.}')
end=s.index('\\smallskip\\noindent\\emph{Euler number, ranks and every integral homology group.}',start)
group=s[start:end]
s=s[:start]+s[end:]
insert=s.index('\\smallskip\\noindent\\emph{The complete integral algorithm.}')
s=s[:insert]+group+s[insert:]
for c,ids in oldids.items():assert sorted(ids)==sorted(re.findall(r'\\'+c+r'\{([^{}]+)\}',s))
assert s.count('\\begin{proof}')==s.count('\\end{proof}')==1
assert s.index('\\tag{D.GI9}')<s.index('\\tag{D.GI10}')<s.index('\\tag{D.GI11}')
p.write_text(s)
print('RECEIVER',p,'LINES',len(s.splitlines()),'SHA256',sha256(s.encode()).hexdigest())
print('CHANGES exact local-reference prose repairs; complete admitted finite boundary map/inverse; H5=0 retraction justification; GI9 before GI10--GI11; no statement or mathematical conclusion change.')
print('IDENTITIES all12 labels,12 hypertargets,11 equation tags unchanged; one complete proof; canonical/frozen inputs unchanged.')
