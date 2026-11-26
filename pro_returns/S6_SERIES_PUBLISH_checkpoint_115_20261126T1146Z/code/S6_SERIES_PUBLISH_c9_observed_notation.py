#!/usr/bin/env python3
"""Bounded notation proposals from actual candidate02 reading; no master writes."""
from pathlib import Path
import csv
import difflib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'agents/continuation9_findings'
s = (ROOT / 'S6_SERIES_PUBLISH_III.tex').read_text()
packets = []

class Proof:
    def __init__(self, tag, unit, pages):
        self.tag, self.unit, self.pages = tag, unit, pages
        a = s.index(r'\hypertarget{tag-' + tag + '}')
        self.start = s.rfind(r'\begin{theorem}', 0, a)
        proof_start = s.index(r'\begin{proof}', a)
        self.end = s.index(r'\end{proof}', proof_start) + len(r'\end{proof}')
        self.old = s[self.start:self.end]
        self.new = self.old
        self.maps = []
    def change(self, start, end, replacements, reason):
        a = self.new.index(start)
        b = self.new.index(end, a) if end else len(self.new)
        old = self.new[a:b]
        new = old
        for source, target in replacements:
            assert source in new, (self.tag, source)
            assert target not in self.old, (self.tag, 'preexisting alias', target)
            new = new.replace(source, target)
            self.maps.append((source,target,reason))
        self.new = self.new[:a] + new + self.new[b:]
    def exact(self, old, new, reason, inverse_pairs):
        assert self.new.count(old) == 1, (self.tag, old[:80])
        self.new = self.new.replace(old,new,1)
        self.maps.extend((a,b,reason) for a,b in inverse_pairs)
    def finish(self):
        back = self.new
        aliases = {}
        for old,new,reason in self.maps:
            if new in aliases:
                assert aliases[new] == old
            aliases[new] = old
        for new,old in sorted(aliases.items(),key=lambda item:-len(item[0])):
            back = back.replace(new,old)
        assert back == self.old, (self.tag, 'inverse rename')
        for pattern in [r'\\label\{[^}]+\}',r'\\hypertarget\{[^}]+\}',r'\d+']:
            assert re.findall(pattern,self.new) == re.findall(pattern,self.old),self.tag
        oldlines=self.old.splitlines(keepends=True)
        newlines=self.new.splitlines(keepends=True)
        matcher=difflib.SequenceMatcher(a=oldlines,b=newlines,autojunk=False)
        groups=list(matcher.get_grouped_opcodes(n=3))
        rows=[]
        for k,group in enumerate(groups,1):
            a,b=group[0][1],group[-1][2]
            c,d=group[0][3],group[-1][4]
            old=''.join(oldlines[a:b]);new=''.join(newlines[c:d])
            assert s.count(old)==1,(self.tag,k,'guard count',s.count(old))
            reasons=[]
            for _,target,reason in self.maps:
                if target in new and reason not in reasons: reasons.append(reason)
            assert reasons,(self.tag,k)
            rows.append(dict(change_id=f'CLAUDE-III-P15-current02-{self.tag}-{k:03}',
                type='D20',statement_id=self.unit,
                old_location='Paper III, tag '+self.tag+'; bounded proof fragment '+str(k),
                old_page='candidate02 '+self.pages,new_location='same permanent proof',
                new_page='pending changed build',old_text=old,new_text=new,
                reason=' '.join(reasons),
                review_status='Used and rechecked after exposure. Complete proof read in rendered context; source roles and all changed occurrences compared. Every renamed object/map has identical underlying value and inverse. Exact reverse rename, labels, targets and numeric literals verified. No independent mathematical-check credit; canonical admission and new PDF review pending.'))
        candidate=s
        for row in rows:
            assert candidate.count(row['old_text'])==1
            candidate=candidate.replace(row['old_text'],row['new_text'],1)
        restored=candidate
        for row in reversed(rows):
            assert restored.count(row['new_text'])==1
            restored=restored.replace(row['new_text'],row['old_text'],1)
        assert restored==s
        packets.extend(rows)
        (OUT/f'S6_SERIES_PUBLISH_c9_current02_{self.tag}_notation.diff').write_text(''.join(difflib.unified_diff(oldlines,newlines,fromfile=self.tag+' before',tofile=self.tag+' proposed',n=5)))
        print(self.tag, 'statement/proof lines',len(oldlines),'guarded rows',len(rows),'exact inverse and invariant tokens passed')

p=Proof('02L2','maps:src:D.2.27','283–292')
p.change(r'Write the power vector modulo $w$',r'Minimal rational rank requires',
         [('U(q)',r'U_{\rm per}(q)'),('V(q)',r'V_{\rm per}(q)'),
          ('$U$',r'$U_{\rm per}$'),('$V$',r'$V_{\rm per}$'),
          ('U^{',r'U_{\rm per}^{'),('V,',r'V_{\rm per},'),('V^{-1}',r'V_{\rm per}^{-1}')],
         'Name the two period-unit functions U_per and V_per, preserving U as the cap and V as the later Smith matrix. For every base point q, the renamed units are exactly the original nonzero holomorphic multipliers; the same logarithms, fractional powers, deck maps and reciprocal chart inverses are retained.')
p.exact(r'$(s,Z)\mapsto(\zeta s,sU(q)^{1/3}Z)$ and the corresponding',
        r'$(s,Z)\mapsto(\zeta s,sU_{\rm per}(q)^{1/3}Z)$ and the corresponding',
        'Propagate the same U_per period unit into the order-three example. The deck transformation, its cube and the transverse period are identical pointwise.',
        [('U(q)',r'U_{\rm per}(q)')])
p.finish()

p=Proof('02L7','maps:src:D.2.31','302–315')
p.change(r'Let $\mathbb Z^r\oplus A_1$',None,
         [('A_1',r'{\mathcal A}_1')],
         'Name the torsion summand mathcal A_1 of the Seifert abelianization, preserving A_i for the elliptic monodromy family. This is identity on the same torsion subgroup with the same peripheral-generator coordinates; its appearances in the statement, homology table and proof remain the same group.')
p.change(r'the latter is \(\operatorname{Exp}L\)',r'Here \(P\) is narrow.',
         [(r'\operatorname{Exp}L',r'\operatorname{Exp}L_{\rm log}'),(r'\operatorname{Exp}(sL)',r'\operatorname{Exp}(sL_{\rm log})')],
         'Name the inverse-Hodge-line logarithm L_log, retaining the later long period basis L. The section L_log equals the original L at every base point, so Q_s, its translation and inverse translation are unchanged.')
p.change(r'Here \(P\) is narrow.',r'\item \emph{The complete integral original-cap map.}',
         [('M',r'{\mathcal M}')],
         'Name the line bundle mathcal M=O(P-O), retaining M for the regular-multiplicity product in the theorem. The identification is identity on that very line bundle, including its total space, Chern class, frame maps, restriction and all reciprocal gauges.')
p.change(r'frame as \((y,w)\mapsto(f(y),a(y)w)\)',r'Fix the forward-quotient convention',
         [('a(y)',r'u_{\rm line}(y)'),('a(f^{-1}y)',r'u_{\rm line}(f^{-1}y)'),
          ('r(y)',r'r_{\rm roof}(y)'),(r'\max r<',r'\max r_{\rm roof}<')],
         'Give the line multiplier u_line and positive roof r_roof their own symbols, retaining the section coefficient a and homology rank r. Both functions have exactly the same pointwise values, so the fundamental domain, increasing roof integral, endpoint derivatives and inverse F_y^{-1} remain identical.')
p.change(r'Cutting the base along the marked tree gives',r'\item \emph{All finite and regular affine data',
         [('N',r'{N_{\partial}}')],
         'Name the cut-graph boundary count N_partial, preserving N as the original neighbourhood. This is the same integer count at every input. Every matrix block index, rank and coordinate number is unchanged under N_partial=N_old.')
assert p.new.count(r'{N_{\partial}}oncanonical') == 1
p.new=p.new.replace(r'{N_{\partial}}oncanonical','Noncanonical')
p.exact('Cutting the base along the marked tree gives\n',
        'Write \\(N_{\\partial}\\) for the number of marked boundary circles.\nCutting the base along the marked tree gives\n',
        'Define the renamed cut-graph count at its first occurrence. It is the same number of marked boundary circles used by the original N-indexed matrix and inverse; this adds a notation declaration without changing the indexed set.',
        [('Cutting the base along the marked tree gives\n','Write \\(N_{\\partial}\\) for the number of marked boundary circles.\nCutting the base along the marked tree gives\n')])
p.change(r'For \(B=[j_iF_i]\)',r'The matrix made from the columns',
         [('B',r'{\mathsf B}')],
         'Name the actual graph matrix mathsf B, including its indexed Smith transforms, preserving the mapping torus B. The new matrix has exactly the same columns j_i F_i, and the projection, Smith identity, kernel vector and inverse coordinate recipe are unchanged.')
p.exact(r'Its inverse projects to the graph chain, uses the inverse of \(B\),',
        r'Its inverse projects to the graph chain, uses the inverse of \({\mathsf B}\),',
        'Propagate the same graph matrix mathsf B into the later inverse splitting; all projected coordinates and actual sweeps remain identical.',
        [('B',r'{\mathsf B}')])
p.change(r'At a finite site, let \(d_i\)',r'\item \emph{The full integral global calculation.}',
         [('g_i',r'g_{i,\rm den}'),('r_i',r'r_{i,\rm tw}')],
         'Name the finite denominator index g_{i,den} and finite twist coefficient r_{i,tw}, preserving the earlier elliptic cocycle g_i and long period r_i. These are the same integers in every fixed vector, norm, pairing, freeness condition, Thom column and primitive relation; the marked affine action and its inverse translation are unchanged.')
p.change(r'The next Mayer--Vietoris kernel is a subgroup',r'Choose an integral basis of that kernel',
         [('c_i',r'c_i^{\rm fix}')],
         'Name the fixed-lattice rank c_i^{fix}, preserving c_i for the peripheral group generators. The rank integer and the boundary/cap ranks are identical, so the exact-sequence rank argument is unchanged.')
p.change(r'For \(b=1\), every finite additive place',r'For the finite sites put',
         [('g=q>1',r'g_{\rm den}=q>1'),('q=g=q_v',r'q=g_{\rm den}=q_v'),
          ('A_i n_i+B_i m_i',r'A_{i,\rm Bez} n_i+B_{i,\rm Bez} m_i'),('r_i',r'r_{i,\rm tw}')],
         'Distinguish the finite denominator g_den and Bezout coefficients A_{i,Bez},B_{i,Bez} from the earlier cocycle g and monodromy family A_i; propagate r_{i,tw}. Their numerical values and determinant-one Bezout identity are unchanged, as are the two solved sweep equations and inverse substitutions.')
p.change(r'The selected cusp has the Jordan fan of',r'The identity on the complex universal cover',
         [('C',r'{\mathsf C}')],
         'Name the cusp comparison matrix mathsf C, its columns and inverse, preserving C for the global homology presentation. Every entry is unchanged, including the OS47 example and the period change H_E. Both basis maps and the entire fan word are therefore identical.')
a=p.new.index(r'The final cusp fan has one orbit')
old=p.new[a:]
new=re.sub(r'(?<![A-Za-z\\])C(?![A-Za-z])',lambda m:r'{\mathcal C}',old)
p.exact(old,new,
        'Name the fixed sphere mathcal C and its quotient image mathcal C_mathcalQ, preserving the homology group C and the newly named matrix mathsf C. Identity on the fixed sphere and on its singleton orbits identifies every normal chart, complement, residue class and isotopy used below.',
        [('C',r'{\mathcal C}')])
p.change(r'The matrix and collar map from that reconstruction satisfy',r'For the linking realization',
         [('A',r'{\mathsf A}')],
         'Name the diagonal reconstruction involution mathsf A, preserving the elliptic monodromy A. Its five diagonal entries, conjugacy identity, collar restriction and product gluing map remain literally the same; its inverse is the same diagonal involution.')
p.finish()

fields=['change_id','type','statement_id','old_location','old_page','new_location','new_page','old_text','new_text','reason','review_status']
with (OUT/'S6_SERIES_PUBLISH_c9_current02_observed_notation_defects.tsv').open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');writer.writeheader();writer.writerows(packets)
(OUT/'S6_SERIES_PUBLISH_c9_current02_observed_notation.json').write_text(json.dumps(packets,ensure_ascii=False,indent=2)+'\n')
print('Total guarded rows',len(packets),'; canonical source unchanged.')
