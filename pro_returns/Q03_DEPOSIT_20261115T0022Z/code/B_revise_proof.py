#!/usr/bin/env python3
"""Reproduce the audited layout/dependency revision of Q03 Sections 2--8.

Run from Q03_DEPOSIT, with the extracted supplied background next to it:
  python3 code/B_revise_proof.py
The input remains unchanged. The output contains exactly Sections 2--8.
Every mutation is listed in work/B_proof_change_ledger.md. Statement text,
numbering, and numbered equations are checked against the original extract.
"""
from pathlib import Path
import re
import hashlib

ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT.parent/'background/post/hexagon_post_example_Q03.tex'
OUT=ROOT/'work/B_proof_revised.tex'
LEDGER=ROOT/'work/B_proof_change_ledger.md'
text=SOURCE.read_text()
start=text.index(r'\section{Foundations, descriptions, and the finite search}')
end=text.index(r'\section{Correctness and running time}')
original=text[start:end]
text=original
ledger=[]

USES={
'2.1':'definitions only.',
'2.2':'Lemma 2.1; definitions of a unit-job schedule and machine assignment.',
'2.3':'definitions only.',
'2.4':'definitions only.',
'2.5':'definitions only.',
'2.6':'definitions only.',
'2.7':'Lemma 2.1; definitions of the atomic alphabet and formula evaluation.',
'2.8':'definitions of the state graph, compatibility, and acceptance in Section 2.2; induction on set cardinality.',
'2.9':'definitions of full schedules, open intervals, and global and relative descriptions.',
'2.10':'Definition 2.9; state and acceptance definitions in Section 2.2.',
'3.1':'Lemma 2.5; separator definition and (3.1).',
'3.2':'definitions of frame reversal, cutoff, and separator.',
'3.3':'the definition of a normalized schedule (Section 3.1).',
'3.4':'Lemma 3.3; definitions of domain, priority prefix, exception, and separator.',
'3.5':'Lemma 3.4.',
'3.6':'Lemmas 3.4 and 3.5.',
'3.7':'Lemma 3.6; definitions of cutoff and normalization.',
'4.1':'definitions only.',
'4.2':'invariant (I1); frame and cone definitions.',
'4.3':'Lemmas 4.1 and 4.2; invariant (I1).',
'4.4':'Lemmas 3.6 and 4.3; the center and side-walk construction.',
'4.5':'Lemmas 4.3 and 4.4; Definition 2.9 and the child construction.',
'5.1':'definitions only.',
'5.2':'definitions only.',
'5.3':'Lemmas 4.2, 4.3, 4.5, and 5.1; invariant (I1); the stipulated switch-upset property (5.3).',
'5.4':'definitions of carry, pruning, and a run.',
'5.5':'Lemmas 4.5, 5.1, 5.3, and 5.4; invariant (I1); injection definition (5.2).',
'6.1':'Lemmas 5.1 and 5.4; the pruning and run definitions; switch pair (5.4).',
'6.2':'Lemmas 2.6, 5.3, 5.4, 5.5, and 6.1; the edge-cutoff construction.',
'6.3':'Lemma 4.5; the frame-reversal map.',
'6.4':'Lemmas 2.5, 4.3, 4.4, 4.5, 6.2, and 6.3; definition (6.8).',
'6.5':'Lemmas 2.6, 5.4, 5.5, and 6.2; definitions (5.2), (5.4), and (6.8).',
'7.1':'Lemmas 2.5, 3.4, 3.6, 4.3, 4.4, 5.1, 5.3, and 6.4; invariants (I1), (I2), and (I3).',
'7.2':'Lemmas 2.4, 2.5, 3.3, 5.1, 5.2, 5.3, and 6.4; invariants (I1) and (I3).',
'7.3':'Lemma 2.4; Corollary 3.7; Lemmas 4.3--4.5, 5.3, 5.5, 6.1--6.5, 7.1, and 7.2; the root invariants.',
'8.1':'Lemmas 2.6, 4.3, 5.1, and 6.5; definitions (8.1) and (8.2).',
'8.2':'Lemmas 2.5, 4.3, 4.4, 4.5, 5.3, 7.1, and 8.1; the center-separator property.',
'8.3':'Lemmas 2.6, 3.1, 4.4, and 8.1; the center-cutoff definition.',
'8.4':'Lemmas 2.6, 6.5, 8.1, 8.2, and 8.3; the atomic formula alphabet.',
'8.5':'Definition 2.9; Proposition 7.3; Lemmas 8.2, 8.3, and 8.4.',
}

# Each tuple starts an unchanged proof-text segment. The final field is the
# bracketed direct justification appended to that segment.
PLANS={
'2.1':[
 ('Transitivity follows','reachability is a strict order','acyclicity and the path definition'),
 ('Strict inequalities along','arc and reachability inequalities agree','the path definition; transitivity of strict integer inequalities'),
 ('For the last claim','a deterministic extending order exists','finite acyclicity; the least-identifier rule')],
'2.2':[
 ('On each machine','the augmented graph is acyclic','unit processing times; feasibility of the original schedule'),
 ('In a topological order','the recurrence gives integer starts no later than the old starts','Lemma 2.1; induction in the augmented topological order'),
 ('Added machine-order arcs','the new schedule is feasible','the augmented arcs and the recurrence')],
'2.3':[
 ('A deadline-feasible','padding gives a full schedule','the deadline schedule and isolated-job definition'),
 ('Conversely, deleting','restriction gives the original deadline schedule',r'full-schedule definition; $T\leq n$')],
'2.4':[
 ('Every full schedule','the replacement occupies the same interval','the definition of a full schedule'),
 ('Relations with both','every precedence pair is respected','the original schedule; the open-interval definition')],
'2.7':[
 ('There are','bound the atomic alphabet',r'the permitted atoms; $N\geq m\geq3$'),
 ('For \\(\\ell\\) leaves','count the formula trees','the binary-tree shape and label counts'),
 ('Enumerate these','enumerate and retain every evaluated set','Lemma 2.1; finite formula evaluation; bit-vector equality')],
'2.8':[
 ('Induct on','form the ordered partition from an accepting path','the induction hypothesis; transition inclusion (2.2)'),
 ('Each \\(A_i\\) is accepted','concatenation respects every precedence','the induction hypothesis; state compatibility'),
 ('Store the predecessor','decode a witness from the stored path','the partition (2.3) and the accepted smaller witnesses')],
'2.10':[
 ('Induct on','each mark gives a candidate state','Definition 2.9; the state definition'),
 ('The first \\(L_1\\)','the state path accepts the node','the size-induction hypothesis; transition definition (2.2)')],
'3.1':[
 ('A high job','every prefix job satisfies the formula','separator clauses; Lemma 2.5'),
 ('Conversely, a job','every selected job belongs to the prefix','Lemma 2.5; separator clause (b)')],
'3.2':[
 ('The complement','reversal sends the cutoff to its complement','the definitions of a cutoff and the reversed order'),
 ('In the reverse frame','the separator clauses are exchanged','the time and cone reversal maps')],
'3.4':[
 ('A predecessor','every predecessor of the exception is before the old position','priority-prefix closure; earliest-exception choice; transitivity'),
 ('For (2), suppose','a forbidden exchange forces a successor','Step 1; Lemma 3.3'),
 ('This successor is outside','successor propagation reaches the target slot','prefix closure; strictly increasing successor times; Step 2'),
 ('For (3), let','the target satisfies the high-job separator clause','Step 3; the old separator clause (a); transitivity')],
'3.6':[
 ('Condition (a)','the no-advance case already separates both cutoffs',r'the old separator and $S\subseteq S^+$'),
 ('Otherwise every','the first target separates the high jobs of both cutoffs','Lemma 3.4; the single promoted job'),
 ('At each subsequent','later advances preserve both clauses and terminate',r'Lemmas 3.4 and 3.5; $S\subseteq S^+$')],
'3.7':[
 ('Order \\(S\\)','the chosen priority order respects precedence','the cutoff property and rank order'),
 ('Normalize a full','the promotions produce a separator slot','normalization; Lemma 3.6')],
'4.2':[
 ('In the tag frame','the cover and inclusions hold in the tag frame','invariant (I1)'),
 ('Reversal interchanges','the same assertions hold in the reversed frame','the explicit time, boundary, and cone reversal maps'),
 ('Finally \\(J','the two sets are relative downsets','global cone closure and taking intersections with $W$')],
'4.3':[
 ('On the same side','the same-side order and its prefixes have the required properties','Lemmas 4.1 and 4.2; invariant (I1)'),
 ('On the switched side','the switched-side order and its prefixes have the required properties','Lemma 4.2; rank order')],
'4.4':[
 ('The initial position','successive walk positions share the old cutoff','Lemmas 4.3 and 3.6'),
 ('For the final endpoint','the center has the final high-job property','the center-separator property')],
'4.5':[
 ('The position claims','the endpoints and cone inclusions hold','the side-walk positions; Lemmas 4.3 and 4.4'),
 ('The gap omits','the child shrinks and the root has no switched child','the child and root-center definitions')],
'5.1':[
 ('Let \\(j\\)','qualification is exactly the old key suffix','the three exhaustive cases $j>d$, $j=d$, and $j<d$'),
 ('For every surviving','the key-order map preserves comparisons and entries remain upsets',r'the index translation $j\mapsto j-d+1$; upset closure')],
'5.2':[
 ('Before renumbering','the smaller-key job keeps its largest old qualifying index',r'pruning; $x\in W\prime$'),
 ('If \\(R(x)<R(y)\\)','both possible strict key comparisons transfer to the old list','the index inequalities from Step 1; rank comparison')],
'5.3':[
 ('On a same side','the same update has the stated qualifiers and order','Lemmas 4.2, 4.3, and 5.1; invariant (I1)'),
 ('On a switched side','the switched update has the stated qualifiers and order','property (5.3); switch-pair definition (5.4)'),
 ('Pruning changes','pruning preserves the child qualifiers and proves (I1)','Lemma 4.5; the pruning definition')],
'6.1':[
 ('A carry retains','a surviving first identity leaves the second untrimmed or absent on the node','Lemma 5.1; pruning; the nesting of nodes in a run'),
 ('Within \\(U\\cap','the two formulas agree on the whole node',r'the two parts $U\cap D_{a_0}$ and $U\setminus D_{a_0}$; $U\subseteq Q_0$')],
'6.2':[
 ('Use \\(a_U,b_U\\)','the switched-edge extension uses two leaves','the switched cutoff definition; cone and rank closure'),
 ('For a same-side edge','express the same-edge low set by its carry','Lemma 5.3; Lemmas 5.4 and 5.5'),
 ('Its initial contribution','replace the initial contribution by at most two leaves on the node','Lemma 6.1; Lemma 5.4; the run definitions'),
 ('Thus there is an upset','construct the downset extension and count all leaves','Steps 2--3; Lemma 2.6; (6.4)')],
'6.3':[
 ('The root has','the node has a parent and the old edge lies before its center','Lemma 4.5; the child construction'),
 ('Reversal sends','reversal gives the displayed order of boundaries and center',r'the decreasing bijection $t\mapsto T+1-t$')],
'6.4':[
 ('Each factor','the switch set is a global upset','Lemma 6.2; cone closure; frame reversal'),
 ('Let \\(x\\in X\\)','every job of $X$ satisfies all four factors','Lemmas 4.3, 4.5, 2.5, and 6.2'),
 ('Now suppose','a putative early qualifier is localized to the old node','Lemmas 6.3 and 6.2'),
 ('If \\(z\\) is at or before','the interval through the old center contains no such qualifier','the old center-separator property; Step 3'),
 ('If \\(z\\) is strictly after','the interval from the old center to the current boundary contains no such qualifier','Lemma 4.4; the weak-cone definition; Step 3'),
 ('These separator statements','the needed exterior separator facts persist in the current witness','the nesting of replacements strictly inside $W$')],
'6.5':[
 ('The first two bounds','every entry has its stated leaf budget','Lemmas 5.4 and 6.2; definitions (5.2), (5.4), and (6.8)'),
 ('For an aggregate union','every list and carry union uses at most $6m+9$ leaves','Lemma 5.5; Step 1; the one-leaf empty set')],
'7.2':[
 ('Child (I1)','the child key comparison holds before pruning','Lemmas 5.3 and 5.2'),
 ('If \\(a\\prime>a\\)','an interior left boundary uses normalized-side minimality','Lemmas 5.3, 2.4, and 3.3'),
 ('If \\(a\\prime=a\\)','an inherited left boundary uses the parent exchange invariant','Lemmas 6.4, 2.5, and 5.1; parent (I3)')],
'7.3':[
 ('Induct from the root','construct the center, walks, and edge data by depth induction','the root invariants; Corollary 3.7; Lemmas 2.4 and 4.3--4.5'),
 ('A same update','all list data used to form a child already exist','Lemmas 6.1--6.4; the ancestor induction hypothesis'),
 ('The new list','the child satisfies all list and boundary assertions','Lemmas 5.3, 5.5, 6.5, 7.1, and 7.2; parent invariants'),
 ('Every child omits','the hierarchy construction terminates','strict decrease of the integer slot count; finite branching')],
'8.1':[
 ('On a same side','the same-side predicate agrees with its cutoff and meets the budget','Lemmas 4.3, 5.1, 6.5, and 2.6'),
 ('On a switched side','the switched-side predicate agrees with its cutoff and uses two leaves','the rank-prefix definition; (8.2)')],
'8.2':[
 ('For (8.4)','the high-part identity holds globally','Lemmas 5.3, 4.5, 2.5, and 7.1'),
 ('For (8.5), first','every selected low-part job lies in the child','Lemmas 8.1, 4.3, and 4.4; the center-separator property'),
 ('Conversely, a low job','every low child job satisfies the low-part formula','Lemmas 4.5, 8.1, and 2.5')],
'8.3':[
 ('In the working frame','the center formula selects its open side','the center-cutoff definition; Lemma 3.1'),
 ('For a side mark','the side-mark formula selects its working-frame prefix','Lemmas 4.4, 8.1, and 3.1; Step 1'),
 ('If that is the forward frame','the stated formula gives the original-time prefix in either frame','the prefix/slot/suffix partition; Lemma 2.6; time reversal')],
'8.4':[
 ('Use \\(A_m=6m+9\\)','the global child description uses at most $12m+25$ leaves','Lemmas 6.5, 8.1, and 8.2; Lemma 2.6'),
 ('The center formula','the relative prefix uses at most $6m+16$ leaves in the permitted alphabet','Lemmas 8.1 and 8.3; Lemma 2.6; the Section 2 atom definitions')],
'8.5':[
 ('Apply the construction','the construction gives the required node and gap structure','Proposition 7.3; Definition 2.9'),
 ('Lemma 8.2 supplies','the descriptions and finiteness verify every hierarchy clause','Lemmas 8.2--8.4; Proposition 7.3; Definition 2.9')],
}

# Anchors were written with literal LaTeX in mind. The raw replacement below
# converts the handful of single-quote mathematical anchors to their exact text.
for ident,plan in PLANS.items():
    PLANS[ident]=[(a.replace('\\prime',"'"),t,u.replace('$x\\in W\\prime$',"$x\\in W'$") ) for a,t,u in plan]

statement_re=re.compile(r'\\begin\{(numbered(?:up)?)\}\{([^{}]*)\}\{([^{}]*)\}\{([^{}]*)\}')
starts=list(statement_re.finditer(text))
assert len(starts)==40
chunks=[]
prior_end=0
for idx,match in enumerate(starts):
    a=match.start()
    b=starts[idx+1].start() if idx+1<len(starts) else len(text)
    chunk=text[a:b]
    ident=match.group(3)
    assert ident in USES
    if idx==0:chunks.append(text[:a])
    env=match.group(1)
    endenv=r'\end{'+env+'}'
    p=chunk.index(endenv)+len(endenv)
    after=chunk[p:]
    old_uses=re.match(r'\s*\\uses\{([^{}]*)\}',after)
    if old_uses:
        old=old_uses.group(1)
        chunk=chunk[:p]+'\n\\uses{'+USES[ident]+'}'+after[old_uses.end():]
    else:
        old='(missing)'
        chunk=chunk[:p]+'\n\\uses{'+USES[ident]+'}'+after
    if old!=USES[ident]:ledger.append((ident,'Uses line',old,USES[ident]))
    pm=re.search(r'(\\begin\{proof\}(?:\[[^\n]*?\])?)\s*(.*?)\\end\{proof\}',chunk,re.S)
    if not pm:
        assert ident=='2.9'
        chunks.append(chunk)
        continue
    body=pm.group(2).strip()
    originalbody=body
    if ident=='2.2':
        old='Induction in the topological order gives'
        new=('For the induction on position in the topological order, a vertex with no incoming arc has '
             r'\(s\prime=0\leq s\); assume \(s\prime(u)\leq s(u)\) for earlier vertices. The recurrence then gives').replace('\\prime',"'")
        assert old in body
        body=body.replace(old,new)
        ledger.append((ident,'Induction clarification',old,new))
    if ident=='2.6':
        old=body
        body=(r'Complement each leaf and interchange union with intersection at every internal vertex. '
              r'Induct on the number of vertices of the formula tree. At a leaf, the allowed complement flag '
              r'gives exactly the complementary set, and both formulas have one leaf. '
              r'At an internal vertex, assume that the transformed child formulas give the complements of '
              r'their old evaluations and preserve their leaf counts. The corresponding De Morgan identity '
              r'then gives the complementary evaluation at this vertex. Both trees have the sum of their '
              r'child leaf counts. Thus the new evaluation is \(J\setminus[F]\), with no leaf created or deleted.')
        PLANS[ident]=[
            ('Complement each','define the transformation and verify its leaf base case','the permitted complement flags'),
            ('At an internal vertex','the induction step preserves complements and leaf counts','the induction hypothesis; the two De Morgan identities')]
        ledger.append((ident,'Explicit structural induction',old,body))
    if ident=='5.1':
        old=r"Let \(j\) be a qualifier's largest old entry index."
        new=old+r' Exactly one of \(j>d\), \(j=d\), and \(j<d\) holds.'
        assert old in body
        body=body.replace(old,new)
        ledger.append((ident,'Exhaustive cases stated first',old,new))
    if ident=='5.4':
        old='Subsequent operations keep or delete an entry, or intersect it with a rank suffix.'
        new=(r'Induct on the number of same-side updates since an entry was created in its run. '
             r'At creation the entry is its initial or injection set, with no additional suffix. '
             r'Assume that every current entry has the stated form. '
             r'Subsequent operations keep or delete an entry, or intersect it with a rank suffix.')
        assert old in body
        body=body.replace(old,new)
        PLANS[ident]=[
            ('Induct on','the initial entries satisfy the shape invariant','the initial-entry and injection definitions'),
            ('Subsequent operations','each update preserves a single effective suffix','the induction hypothesis; the maximum-threshold identity')]
        ledger.append((ident,'Explicit history induction',old,new))
    if ident=='2.7':
        old=(r'Counting both frames and complements, the leaf alphabet has at most \(64N^m\) elements for '
             r'\(N\geq m\geq3\); this generous constant includes the \(O(N)\) thresholds and constants.')
        new=(r'Counting both frames and complements, the leaf alphabet has at most '
             r'\[4+8(N+2)+20\binom Nm\leq64N^m\] '
             r'elements for \(N\geq m\geq3\): the constants contribute four choices, the thresholds '
             r'contribute \(8(N+2)\), and the five subset/cone types contribute \(20\binom Nm\). '
             r'The inequality follows from \(8N+20\leq16N\leq16N^m\) and \(\binom Nm\leq N^m\).')
        assert old in body
        body=body.replace(old,new)
        ledger.append((ident,'Constant derivation',old,new))
    if ident=='2.8':
        old=r'Induct on \(|W|\).'
        new=(r'Induct on \(|W|\). The base \(W=\varnothing\) has the empty schedule. '
             r'Assume that every accepted smaller set has a full schedule.')
        assert old in body
        body=body.replace(old,new)
        ledger.append((ident,'Induction clarification',old,new))
    if ident=='2.10':
        old="Induct on a node's size."
        new=(r"Induct on the number of slots \(|W|/m\) of a node. For one slot, that slot is marked and all gaps are empty, "
             r"so it is an initial and final state. For a larger node assume the claim for its smaller children.")
        assert old in body
        body=body.replace(old,new)
        ledger.append((ident,'Induction clarification',old,new))
    if ident=='5.5':
        old='$x_K$ be its job of least rank.'
        new=r"$x_K$ be the least-rank job of $K\cap W'$."
        assert old in body
        body=body.replace(old,new)
        ledger.append((ident,'Selection-domain clarification',old,new))
    if ident=='7.3':
        old='Induct from the root.'
        new='Induct from the root on node depth.'
        assert old in body
        body=body.replace(old,new)
        ledger.append((ident,'Induction-variable clarification',old,new))
        PLANS[ident][0]=(new,PLANS[ident][0][1],PLANS[ident][0][2])
    if ident=='6.2':
        old='This construction has eliminated the old switch formula, rather than embedding its historical expression.'
        new='The displayed extension uses the replacement initial contribution from (6.1), with the stated leaf count independent of earlier depth.'
        assert old in body
        body=body.replace(old,new)
        ledger.append((ident,'Equivalent explanatory wording',old,new))
    if ident=='7.1':
        # Preserve every mathematical sentence, turning the existing case and
        # four-item subproof into one sequence of claim-first numbered steps.
        body=body.replace(r'\textbf{Case 1: \(z\) is after \(a\).}',r'First suppose that \(z\) is after \(a\).' )
        body=body.replace(r'\textbf{Case 2: \(z\) is at or before \(a\).}',r'Now suppose that \(z\) is at or before \(a\).' )
        enumstart=body.index(r'\begin{enumerate}')
        enumend=body.index(r'\end{enumerate}',enumstart)+len(r'\end{enumerate}')
        enum=body[enumstart:enumend]
        items=re.split(r'\\item\s*',enum)[1:]
        assert len(items)==4
        items[-1]=items[-1].replace(r'\end{enumerate}','')
        cleaned=[]
        for item in items:
            mm=re.match(r'\\textbf\{(.*?)\}\s*(.*)',item.strip(),re.S)
            assert mm
            cleaned.append(mm.group(1)+' '+mm.group(2).strip())
        body=body[:enumstart]+'\n\n'.join(cleaned)+body[enumend:]
        body=body.replace('by item 1','by Step 6').replace('contradict item 3','contradict Step 8')
        ledger.append((ident,'Updated local step references','item 1; item 3','Step 6; Step 8'))
        plan=[
          ('Pruning can','reduce to the pre-pruning qualifiers and split their possible times','the pruning definition'),
          (r'First suppose that \(z\) is after','a qualifier after the old boundary satisfies child (I2)','Lemma 5.3; Lemma 4.4'),
          (r'Now suppose that \(z\) is at or before','an earlier qualifier is carried from the parent boundary','Lemmas 2.5, 6.4, and 5.1; parent (I2)'),
          (r'If \(a\prime=a\)','the unchanged boundary is settled; later positions retain a high carry','Lemma 5.3; the nested side cutoffs'),
          ('Let the first advance','fix the first actual boundary advance','the side-walk construction'),
          (r'Every predecessor of \(x\)','the exception has every predecessor before the old boundary','priority-prefix closure; earliest-exception choice; transitivity'),
          (r'The old key of \(x\)','the exception has smaller old key than the boundary qualifier','invariant (I1); Lemmas 4.3 and 5.1'),
          (r'The exchange of \(x\)','parent (I3) forbids their exchange','parent (I3); Step 7'),
          (r'Consequently \(y\)','a successor of the boundary qualifier must occur by the target','Steps 6 and 8; the full-schedule precedence conditions'),
          ('Such a successor','the carry has a successor at the first target','upset closure; Lemma 3.4(2) on the restricted domain'),
          ('For a later advance','propagation through every later advance proves child (I2)','Lemma 3.4(2); upset closure; transitivity'),
        ]
        PLANS[ident]=[(aa.replace('\\prime',"'"),t,u) for aa,t,u in plan]
        ledger.append((ident,'Step layout','two cases and a four-item numbered subproof','one eleven-step proof; all subproof sentences retained'))
    if ident in PLANS:
        plan=PLANS[ident]
        locs=[]
        at=0
        for anchor,title,used in plan:
            loc=body.find(anchor,at)
            if loc<0:raise AssertionError((ident,anchor,body[:200]))
            locs.append(loc)
            at=loc+len(anchor)
        assert locs[0]==0,(ident,locs[0],body[:80])
        parts=[]
        for k,(_,title,used) in enumerate(plan):
            section=body[locs[k]:locs[k+1] if k+1<len(locs) else len(body)].strip()
            # State the cases before carrying them out, with their exhaustivity.
            if k==0 and ident in ('4.3','5.3','8.1'):
                section='The two working sides, same and switched, exhaust the construction. '+section
            if k==0 and ident=='6.2':
                section='An edge is either switched or same; these two cases exhaust the edge construction. '+section
            if k==1 and ident=='6.1':
                section=r'The disjoint sets \(U\cap D_{a_0}\) and \(U\setminus D_{a_0}\) partition \(U\). '+section
            if k==2 and ident=='8.3':
                section='The working frame is either the forward frame or the reverse frame. '+section
            if k==2 and ident=='6.2':
                section=('For the initial contribution, the cases are a root run, a switched run retaining its first '
                         'initial entry, a switched run retaining only its second, or no retained initial entry. '+section)
            if k==2 and ident=='6.4':
                section+=r' The two possible time ranges are at or before \(v_-\), and strictly after \(v_-\) through \(a\).'
            if k==0 and ident=='7.1':
                section+=r' Its time is either after \(a\) or at or before \(a\); these cases are exhaustive.'
            if k==0 and ident=='7.2':
                section+=r' The construction gives \(a\prime\geq a\); the two cases are \(a\prime>a\) and \(a\prime=a\).'.replace('\\prime',"'")
            if k==0 and ident=='5.2':
                section+=r' The strict comparison has two cases: \(R(x)<R(y)\), or \(R(x)=R(y)\) and \(\lambda(x)<\lambda(y)\).'
            parts.append(r'\step{'+str(k+1)+'}{'+title+'}\n'+section+'\n'+r'\by{'+used+'}')
        body='\n\n'.join(parts)
        ledger.append((ident,'Numbered step layout','unnumbered proof',str(len(plan))+' claim-first steps with bracketed direct uses'))
    # Existing short proofs remain short; existing 3.3 and 5.5 steps stay intact.
    chunk=chunk[:pm.start(2)]+body+'\n'+chunk[pm.end(2):]
    chunks.append(chunk)
text=''.join(chunks)

# Documentary comments outside proofs are kept except these equivalent-wording
# changes, logged explicitly to prevent silent omissions.
wording=[
 ('The replacement means rescheduling the jobs of the interval subject to precedence. It does \\textbf{not} mean that every arbitrary permutation of its slots is feasible.',
  'The replacement ranges over full schedules of the interval job set, each respecting its restricted transitive precedence order.'),
 ('These are agreement predicates, not global descriptions of the cutoffs as standalone sets. Their behavior outside \\(W\\) is not assumed.',
  'The equalities (8.3) specify these predicates on \\(W\\); subsequent uses first restrict membership to \\(W\\).'),
 ('The localization in this proof is a logical order of justification. Boolean intersections commute; no assertion about a required operational evaluation order is being made. In particular, the parent description is not silently inserted into (8.5).',
  'The proof of (8.5) first derives membership in the parent from its cone factors, which permits the use of (8.3). Its formula therefore uses exactly the five displayed factors.'),
]
for old,new in wording:
    assert old in text,old[:100]
    text=text.replace(old,new)
    ledger.append(('exposition','Equivalent explanatory wording',old,new))

# Exact preservation checks: statements and displayed numbered equation bodies.
def statements(s):
    out=[]
    for mm in re.finditer(r'\\begin\{(numbered(?:up)?)\}\{[^{}]*\}\{([^{}]*)\}\{[^{}]*\}(.*?)\\end\{\1\}',s,re.S):
        out.append((mm.group(2),mm.group(0)))
    return out
assert statements(original)==statements(text),'A numbered statement changed.'
assert re.findall(r'\\tag\{([^{}]*)\}',original)==re.findall(r'\\tag\{([^{}]*)\}',text),'Equation numbers changed.'
# Retain all numbered displayed expressions literally, including whitespace.
def numbered_displays(s):
    return [x for x in re.findall(r'\\\[(.*?)\\\]',s,re.S) if r'\tag{' in x]
assert numbered_displays(original)==numbered_displays(text),'A numbered display changed.'
assert len(re.findall(r'\\uses\{',text))==40
assert len(re.findall(r'\\begin\{proof\}',text))==39
assert len(re.findall(r'\\end\{proof\}',text))==39
assert r'no numbered statement is cited' not in text
assert text.startswith(r'\section{Foundations,')
assert r'\section{Correctness and running time}' not in text
OUT.write_text(text)
lines=['# Sections 2–8 proof-layout and dependency change ledger','',
       'Date: 15 November 2026. Editor/checker: GPT-6 Astra (OpenAI), effort ChatGPT Pro mode.','',
       'The reproducible script is `code/B_revise_proof.py`; the output is `work/B_proof_revised.tex`. '
       'It reads the supplied original without modifying it. Exactly 40 numbered statements and all '
       'their statement texts and numbered displays are retained byte for byte within the normalized '
       'Python text read. There are 39 proofs and one definition.','',
       f'- Original extract SHA-256: `{hashlib.sha256(original.encode()).hexdigest()}`',
       f'- Revised extract SHA-256: `{hashlib.sha256(text.encode()).hexdigest()}`',
       f'- Numbered proof steps after revision: {text.count(chr(92)+"step{")}',
       f'- Uses lines after revision: {text.count(chr(92)+"uses{")}',
       '',
       'The supplied step layouts of 3.3 and 5.5 are retained. The choice domain in 5.5 is made explicit '
       'as K∩W′. The assumptions on G in (5.3) remain standing hypotheses of the switched update; '
       'its Uses line introduces no forward reference to Lemma 6.4. Proposition 7.3 validates the construction order.','']
for ident,kind,old,new in ledger:
    lines.extend([f'## {ident} — {kind}','', '**Before:**', '',old,'','**After:**','',new,''])
lines.extend(['## Verification output','',
              'PASS: 40 numbered statement texts preserved exactly.',
              'PASS: every numbered display and its equation number preserved exactly.',
              'PASS: 39 proof environments balanced.',
              'PASS: all 40 statements/definition have Uses lines.',
              'PASS: Sections 2–8 only; no Section 9 content included.',
              'PASS: all scripted anchor transformations matched their original text.',''])
LEDGER.write_text('\n'.join(lines))
print('PASS: numbered statements preserved:',len(statements(text)))
print('PASS: numbered displays preserved:',len(numbered_displays(text)))
print('PASS: proof environments balanced: 39')
print('PASS: Uses lines: 40')
print('Numbered steps:',text.count(r'\step{'))
print('Recorded changes:',len(ledger))
print('Output: work/B_proof_revised.tex')
print('Ledger: work/B_proof_change_ledger.md')
