#!/usr/bin/env python3
"""Prepare the fully read Euler/normal-jets unit and targeted missing-owner repairs.

This script writes agent fragments only. It neither edits shared TeX nor refreshes
an inventory, manifest, seal, receipt, or census.
"""
from pathlib import Path
import csv
import re
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'agents/continuation3_conductor'
PRE = 'S6_SERIES_PUBLISH_c3_conductor_02'
SOURCE = ROOT / 'S6_SERIES_PUBLISH_II.tex'
source = SOURCE.read_text()
START = r'\section{Euler identities, normal-crossing fibres and conductor jets}'
END = r'\section{Irreducible supports: topology, conductor and equality}'
start, end = source.index(START), source.index(END)
original = source[start:end]
working = original
rows = []

def owner_at(text, pos):
    ms = list(re.finditer(r'\\StatementRecord\{([^{}]+)\}', text[:pos]))
    return ms[-1].group(1) if ms else 'sec:II:08'

def log(kind, old, new, reason, owner, location=None):
    p = source.find(old)
    line = source[:p].count('\n') + 1 if p >= 0 else ''
    rows.append(dict(change_id=f'II-C3-EUL-{len(rows)+1:04d}', type=kind,
        statement_id=owner, old_location=location or f'cp35 source line {line}',
        old_page='cp35 PDF omitted from supplied checkpoint; source locus given',
        new_location=owner, new_page='pending integrated final PDF',
        old_text=old, new_text=new, reason=reason,
        review_status='Complete original and receiving proof context read and compared; integrated PDF reading remains open.'))

def replace(old, new, kind, reason, owner=None):
    global working
    assert working.count(old) == 1, (old[:100], working.count(old))
    owner = owner or owner_at(working, working.index(old))
    log(kind, old, new, reason, owner)
    working = working.replace(old, new, 1)

replace(r'\label{sec:II:08}',
        r'\label{sec:II:08}'+'\n\n'+r'\subsection{Euler localization}\label{subsec:II:euler-localization}',
        'D14', 'The localization identity has its own subsection before the local normal-crossings formula and its global consequences.', 'sec:II:08')
replace(r'\subsection{Normal-crossing fibre identities}',
        r'\subsection{Normal-crossing fibre identities}\label{subsec:II:normal-crossing-identities}',
        'D14', 'Retained the existing subsection title and supplied a stable subsection label for the complete local-to-global chain.', 'sec:II:08')
replace(r'\subsection{Normal jets along conductor curves}',
        r'\subsection{Normal jets along conductor curves}\label{subsec:II:normal-conductor-jets}',
        'D14', 'Retained the existing subsection title and supplied a stable label. This whole section precedes the normalization applications of C2d.', 'sec:II:08')

# The pre-existing SRef entry is correct; its mathematical owner was absent.
assert r'\hypertarget{tag-01C8}' not in source
assert r'\label{cdp:st:C.2.NC.1}' not in source
restored = r'''\begin{cited}[The local-to-global Euler formula with multiplicities and self-intersections]\hypertarget{tag-01C8}{}\label{cdp:st:C.2.NC.1}
\StatementRecord{cdp:st:C.2.NC.1}{proved}{01C8}{\cite[\S2.1--2.2, pp.~237--241, and \S2.4--3, pp.~242--245]{ACampo1975}}
Let $g:U\to\Delta$ be a proper holomorphic map from a smooth complex threefold to a disc, smooth over $\Delta^*$, whose central fibre is $\sum_i m_iS_i$ and whose reduced support $S$ has normal crossings. Let $\nu:\coprod_i T_i\to S$ be normalization and let $D_i\subset T_i$ be its reduced conductor divisor. For a sufficiently small nonzero $t$,
\begin{equation}
 e(U_t)=\sum_i m_i e(T_i\setminus D_i).
 \label{cdp:eq:C.NC.1}
\end{equation}
\end{cited}

\begin{proof}
The proper analytic boundary fibration is the construction and lemma of \cite[\S2.1--2.2, pp.~237--241]{ACampo1975}. In a chart where
$g=z_1^{a_1}\cdots z_r^{a_r}$, write $z_j=\rho_j u_j$ with $u_j\in S^1$. Its boundary fibre over an argument $\theta$ maps to $S$, with fibre over that $r$-branch stratum
\[
 \{(u_1,\ldots,u_r)\in(S^1)^r:
                 u_1^{a_1}\cdots u_r^{a_r}=e^{i\theta}\}.
\]
An integral change of angular basis identifies this fibre with
$\gcd(a_1,\ldots,a_r)$ copies of $(S^1)^{r-1}$.
For self-intersections, changing a local branch equation multiplies its modulus by a positive function and translates its argument; a branch permutation permutes the corresponding factors. These transition maps preserve the lifted equation of $g$ and glue the same boundary projection. Thus the local product comparison in the cited lemma applies to these charts as well.

The boundary fibre is homeomorphic to $U_t$. The constructible cohomology of its projection to $S$ is the proper comparison of \cite[\S2.4--3, pp.~242--245]{ACampo1975}. Euler integration on the strata gives zero from $r\ge2$, since their angular tori have positive dimension, and gives $m_i$ from a one-branch point of $S_i$. Normalization identifies that one-branch stratum with $T_i\setminus D_i$, proving the displayed formula.
\end{proof}

'''
needle = '\\begin{proposition}[The normalized double curves and the coherent Euler formula]'
replace(needle, restored+needle, 'D06',
        'Restored the formerly absent reader target 01C8 from its attached compendium statement. Opened A\'Campo\'s complete proper analytic construction and comparison; retained only the exact self-intersection transition maps and Euler-stratum specialization. The pre-existing local SRef entry already resolves to this tag and label.', 'cdp:st:C.2.NC.1')
log('D17', 'Compendium C.2.NC.1 complete independent radial-inversion re-derivation', restored,
    'The known proper analytic formula has one cited owner. The source begins with globally smooth components, so the short branch-permutation descent remains explicitly proved. No general theorem is inferred merely from a local singularity formula.', 'cdp:st:C.2.NC.1', 'attached compendium C.2.NC.1; current owner absent')

old = r'\CompendiumRef{II}{cdp:st:C.2.NC.1}'
replace(old, r'\cref{cdp:st:C.2.NC.1}', 'D06',
        'The uniform-multiplicity specialization now refers to the actual restored owner in this paper; its map is the same proper fibration on a disc around mS.', 'cdp:st:C.2.NC.3')

replace("Ehresmann's theorem makes it a smooth locally trivial fibre bundle.",
        r'The finite map in the Stein factorization of $g$ has generic degree one because $F$ is connected; normality of $C$ makes it an isomorphism, so the fibres of $g$ are connected. The compact-fibre proposition and horizontal-lift lemma in \cite[p.~154]{Ehresmann1952Connections} therefore give a smooth locally trivial fibre bundle on this punctured base.',
        'D18', 'Opened the complete proposition, proof reduction and horizontal-lift lemma on the original printed p.154. The receiving proper submersion has exactly the compact connected fibres required there.', 'cdp:st:C2a')

old_local = r'''The nearby Euler function is $m_i$ along the smooth part of $S_i$. At a double crossing the local map is $x^{m_i}y^{m_j}$, with equal exponents for a self-intersection of one global component; its transverse nearby fibre is a disjoint union of annuli and has Euler number zero. Euler integration gives $e(Y_t)=\sum_i m_i e(T_i\setminus D_i)$.'''
replace(old_local,
        r'Apply \cref{cdp:st:C.2.NC.1} to the restriction of $g$ over a disc about this fibre, retaining its multiplicities $m_i$. It gives $e(Y_t)=\sum_i m_i e(T_i\setminus D_i)$.',
        'D12', 'The exact local angular comparison is now owned once by the restored cited formula. This application keeps the actual restriction map, multiplicities and open conductor strata.', 'cdp:st:C.2.NC.4')

# The one-paragraph proof needs no one-item list.
a = working.index(r'\begin{proof}')
b = working.index(r'\end{proof}', a)
part = working[a:b]
old_enum = r'\begin{enumerate}[label=\arabic*.,leftmargin=*]'+'\n'+r'\item '
assert part.count(r'\item') == 1
new_part = part.replace(old_enum, '').replace(r'\end{enumerate}', '')
replace(part, new_part, 'D23', 'Removed the vacuous one-item enumeration while preserving the entire localization comparison.', 'cdp:st:C2a')

# Existing precise display identities and targets survive the numbering change.
equations = []
def convert(m):
    old = m.group()
    ts = re.findall(r'\\tag\{([^{}]+)\}', old)
    if not ts: return old
    assert len(ts) == 1
    label = re.findall(r'\\label\{([^{}]+)\}', old)[0]
    new = old.replace(r'\[',r'\begin{equation}',1)
    new = new[:-2]+r'\end{equation}'
    new = new.replace(r'\tag{'+ts[0]+'}', '')
    ident = owner_at(working, m.start())
    equations.append(dict(old_tag=ts[0],target_label=label,statement_id=ident))
    log('D19',old,new,'Only the display wrapper and manual tag change; the same equation label and mathematical display use the section counter.',ident)
    return new
working = re.sub(r'\\\[.*?\\\]',convert,working,flags=re.S)
assert not re.search(r'\\tag\{',working)
for typ in ['label','hypertarget']:
    pat=r'\\'+typ+r'\{([^{}]+)\}'
    assert set(re.findall(pat,original)) <= set(re.findall(pat,working))
assert working.count(r'\begin{proof}') == original.count(r'\begin{proof}')+1
assert working.count(r'\begin{proof}') == working.count(r'\end{proof}')

groups = [
 ('Euler localization','euler-localization',['cdp:st:C2a']),
 ('Normal-crossing fibre identities','normal-crossing-identities',['cdp:st:C.2.NC.1','cdp:st:C.2.NC.2','cdp:st:C.2.NC.3','cdp:st:C.2.NC.4','cdp:st:C.2.NC.5']),
 ('Normal jets along conductor curves','normal-conductor-jets',['cdp:st:C2d']),
]
for title,slug,ids in groups:
    for ident in ids:
        log('D14', 'sec:II:08 after sec:II:05; '+ident,
            'sec:II:08 before sec:II:05; subsec:II:'+slug+'; '+ident,
            'Moved the complete section and its proof owners ahead of the normalization section. C2d then precedes every A.5 conductor application; the C.3.1/C.3.5 smooth-fibre inputs already occur before this section.',ident)

# These two receiving proofs were read in full. They are outside the replacement
# range, so root receives exact small edits, never a rewrite of those blocks.
remote = []
for ident in ['cdp:st:C.2.IRR.1','cdp:st:C.2.UN.7']:
    pos = source.index(r'\label{'+ident+'}')
    lo = source.rfind(r'\begin{proposition}',0,pos)
    hi = source.index(r'\end{proof}',pos)+len(r'\end{proof}')
    block = source[lo:hi]
    assert block.count(old) == 1
    new = r'\cref{cdp:st:C.2.NC.1}'
    remote.append(dict(statement_id=ident,old_text=old,new_text=new))
    log('D06',old,new,
        'Read the complete receiving proof. IRR.1 specializes the proper formula to mS with elliptic conductor; UN.7 uses its boundary homeomorphism and angular fibre on the embedded normal-crossings resolution. Both maps are precisely those stated in the restored owner. Only this reference token is changed.',ident,
        'complete receiving proof '+ident+'; sole CompendiumRef to C.2.NC.1')

def tsv(suffix,fields,data):
    with (OUT/(PRE+suffix)).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(data)

(OUT/(PRE+'_replacement.tex')).write_text(working,newline='\n')
with (ROOT/'S6_SERIES_PUBLISH_defects_II.tsv').open() as f: df=next(csv.reader(f,delimiter='\t'))
tsv('_defects.tsv',df,rows)
tsv('_equations.tsv',['old_tag','target_label','statement_id'],equations)
tsv('_remote_reference_repairs.tsv',['statement_id','old_text','new_text'],remote)

now=datetime.now(timezone.utc)
with (ROOT/'CHECK_EVENTS.tsv').open() as f: ef=next(csv.reader(f,delimiter='\t'))
events=[]
owner_units={ident:slug for _,slug,ids in groups for ident in ids}
owner_units.update({r['statement_id']:'outside-unit-missing-reference' for r in remote})
for ident,slug in owner_units.items():
    row={k:'' for k in ef}
    scope='Complete cp35 original and receiving statement/proof read and compared.'
    if ident=='cdp:st:C.2.NC.1':
        scope='Complete attached compendium original statement/proof read; primary A\'Campo proper analytic construction and proof read at pp237–245; receiving cited statement and exact branch-permutation comparison read.'
    if slug=='outside-unit-missing-reference':
        scope='Complete receiving statement/proof read to verify its sole missing-owner reference; only that reference token is proposed for change. Other proof premises and unrelated defects are not certified by this event.'
    row.update(statement_id=ident,date=now.date().isoformat(),date_utc=now.isoformat(),
        who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; inherited effort not separately exposed; continuation3 conductor agent',
        type='used and rechecked in this run',outcome=scope+' This is an exposed editorial comparison, not an independent reproof or computation. Integrated typesetting remains open.',
        event_id='publish:c3:conductor02:'+ident,phase='publication editorial comparison',
        source_file='agents/continuation3_conductor/'+PRE+'_replacement.tex',
        source_event_type='used and rechecked in this run',evidence_group='publish:c3:conductor02:'+slug,
        where='subsec:II:'+slug if not slug.startswith('outside') else ident)
    events.append(row)
tsv('_CHECK_EVENTS.tsv',ef,events)

status=[]
for title,slug,ids in groups:
    for n in range(1,26):
        state='done'; reason='Complete unit read for this class; each identified change is logged individually.'
        if n==18:
            state='open';reason='New A\'Campo and Ehresmann receiving citations opened at their exact primary loci; common bibliography form and inherited locator pass remain open.'
        if n==23:
            state='open';reason='Local proof-list typography corrected; integrated typesetting and rendered-page reading remain open.'
        status.append(dict(unit='subsec:II:'+slug,title=title,criterion=f'D{n:02d}',status=state,reason=reason))
    status.append(dict(unit='subsec:II:'+slug,title=title,criterion='structure',status='done',reason='Local prerequisite order complete: Euler formula precedes its applications and C2d precedes the normalization section. The external C.3 smooth-fibre inputs already precede this section; whole-paper ordering outside this range is not certified.'))
tsv('_unit_status.tsv',['unit','title','criterion','status','reason'],status)
print('Euler section prepared:',len(original),'->',len(working),'characters')
print('Defect rows:',len(rows),'; exposed comparison events:',len(events),'; old display identities:',len(equations))
print('Restored existing permanent owner 01C8; no new P-series tags used.')
print('Two exact outside-unit reference repairs supplied; the local SRef definition already targets 01C8 correctly.')
print('Section order for admission: cotangent, this Euler section, normalization, irreducible supports.')
