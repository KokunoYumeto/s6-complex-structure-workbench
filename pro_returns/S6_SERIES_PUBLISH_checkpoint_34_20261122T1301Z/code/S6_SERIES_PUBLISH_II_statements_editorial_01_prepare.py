from pathlib import Path
import datetime as dt, difflib, hashlib, json, re

R=Path(__file__).resolve().parents[1]
sha=lambda b:hashlib.sha256(b).hexdigest()
s=(R/'S6_SERIES_PUBLISH_II.tex').read_text()
assert sha(s.encode())=='7257ede51d989e545eb8f887bbcc4fb50201e0c1ff55159afbc077970dcdc7e5'
out=R/'records/S6_SERIES_PUBLISH_II_statements_editorial_01';assert not out.exists();out.mkdir()
def block(tag):
    at=s.index('\\hypertarget{tag-'+tag+'}');a=s.rfind('\\begin{proposition}',0,at)
    b=s.index('\\end{proof}',at)+len('\\end{proof}')
    return s[a:b]
old=block('01GP');new=old
changes=[]
def change(text,a,b,kind,reason):
    assert text.count(a)==1,(a,text.count(a))
    changes.append(dict(tag='01GP',old=a,new=b,type=kind,reason=reason,offset_at_change=text.index(a)))
    return text.replace(a,b,1)
new=change(new,'Counterexample: The square theta formula for arbitrary sections','Theta determinants at an elliptic half-period','D16','State the mathematical content in the title.')
a=r'''The square-only formula in Lead~9 is false as a local period
identity for arbitrary elliptic sections and linearizations.
The exact formula for the theta expression specified there is
\eqref{cdp:eq:E-theta-general}. The assertion for the actual original
period family remains true, by its equation $\wp(\mu)=0$.'''
b=r'''For the theta expression in \eqref{cdp:eq:E-theta-general}, the
constant elliptic section $\mu(\tau)=1/2$ admits a holomorphic
contracting linearization over a disc about $\tau=i$ for which
\[
 \mu'-\frac{i}{2\pi}\partial_\mu\log\vartheta_1(\mu,\tau)=0,
 \qquad
 \det\Omega'(i)=-\frac{\wp(1/2;i)}{4\pi^2}\ne0.
\]
The determinant for the specified theta expression is given by
\eqref{cdp:eq:E-theta-general}. On the period family satisfying
$\wp(\mu)=0$, its Weierstrass term vanishes.'''
new=change(new,a,b,'D03','Move the explicit witness already proved in the block into the statement. The old failed universal identity is witnessed by the same section and linearization with zero square term and nonzero determinant; the general theta identity and the wp=0 specialization are retained.')
new=change(new,r'\begin{enumerate}[label={$\langle1\rangle$\arabic*.},leftmargin=*]',r'\begin{enumerate}[label=\arabic*.,leftmargin=*]','D04','Use ordinary mathematical proof-item numbering.')
new=change(new,r'\noindent\textbf{Step 1.} \noindent\textbf{Step 1.} We use',r'We use','D23','Remove duplicated step decoration; retain the first existing item.')
new=change(new,r'\noindent\textbf{Step 2.} Let',r'\item Let','D23','Give the next existing proof step one enumerate item.')
for first,second,start in [(3,2,'This family'),(4,3,'There is'),(5,4,'The identity'),(6,5,'For completeness, the direct images')]:
    a=rf'\noindent\textbf{{Step {first}.}} \noindent\textbf{{Step {second}.}} '+start
    b=r'\item '+('The direct images' if first==6 else start)
    new=change(new,a,b,'D23','Replace two conflicting step labels by one proof-item label; preserve the mathematical step.')
new=change(new,r'\noindent\textbf{Step 6.} Since',r'Since','D23','Keep the Stein-cohomology conclusion in the same final proof item.')
new=change(new,'the proposed square is zero. The actual determinant, by the\nproved heat-equation formula, is','the square term in \\eqref{cdp:eq:E-theta-general} is zero. The\ndeterminant, by that heat-equation formula, is','D03','Replace an internal proposal reference by the exact mathematical identity.')
new=change(new,'Thus even the zero sets in the asserted formula\ndiffer in this fully specified family. Extra holomorphic terms','Thus the square term vanishes at $i$ and the determinant is\nnonzero there. Extra holomorphic terms','D03','State the two computed values directly; retain the exact witness and the linearization-derivative observation.')
first=dict(tag='01GP',owner='cdp:st:E18',old=old,new=new,changes=changes.copy())
changes=[];old=block('033N');new=old
def change_second(a,b,kind,reason):
    global new
    assert new.count(a)==1
    changes.append(dict(tag='033N',old=a,new=b,type=kind,reason=reason,offset_at_change=new.index(a)));new=new.replace(a,b,1)
change_second('The proposed configuration with three rank-one reduced singular fibres\ndoes not describe the construction of \\cite{Viaclovsky2026Two}. The elliptic surface',
    'In the construction of \\cite{Viaclovsky2026Two}, the elliptic surface','D03','State the published fibre configuration positively with its source credit.')
change_second(r'\begin{enumerate}[label={$\langle1\rangle$\arabic*.},leftmargin=*]',r'\begin{enumerate}[label=\arabic*.,leftmargin=*]','D04','Use ordinary proof-item numbering.')
change_second(r'\noindent\textbf{Step 1.} Put','Put','D23','Remove the repeated label inside the sole enumerate item.')
change_second('independently have nilpotent ranks $1,1,2$; their exact\ncalculation rules out the assertion that all three are rank one.\nThese are the types stated in Proposition 3.1 and Theorem 1.1\nof the cited source, not a correction to that source.',
    'have nilpotent ranks $1,1,2$. These are the fibre types in\n\\cite[Proposition~3.1 and Theorem~1.1]{Viaclovsky2026Two}.','D03','Retain all three ranks and the published locators while removing the discarded draft and defensive history.')
second=dict(tag='033N',owner='push:src:E.5.1',old=old,new=new,changes=changes.copy())
guards=[first,second]
for g in guards:
    (out/(g['tag']+'_before.tex')).write_text(g['old'])
    (out/(g['tag']+'_after.tex')).write_text(g['new'])
    assert re.findall(r'\\label\{[^}]+\}|\\hypertarget\{[^}]+\}|\\tag\{[^}]+\}',g['old'])==re.findall(r'\\label\{[^}]+\}|\\hypertarget\{[^}]+\}|\\tag\{[^}]+\}',g['new'])
    # Every pre-existing display, including the full proof calculations, remains.
    displays=lambda t:re.findall(r'\\\[.*?\\\]',t,re.S)
    assert all(x in displays(g['new']) for x in displays(g['old']))
    back=g['new']
    for c in reversed(g['changes']):
        at=c['offset_at_change'];end=at+len(c['new'])
        assert back[at:end]==c['new'],(g['tag'],c['new'])
        back=back[:at]+c['old']+back[end:]
    assert back==g['old']
    (out/(g['tag']+'.diff')).write_text(''.join(difflib.unified_diff(g['old'].splitlines(True),g['new'].splitlines(True),fromfile=g['tag']+' before',tofile=g['tag']+' after')))
(out/'guards.json').write_text(json.dumps(guards,indent=2)+'\n')
index=dict(created_utc=dt.datetime.now(dt.timezone.utc).isoformat(),source_sha256=sha(s.encode()),status='Prepared for root full after-text read; unapplied.',
    execution_history='Initial inverse guard rejected the nonunique replacement word Since; before/after files from that failed prepare are preserved in the sibling failed_attempt_01 directory. No canonical writes. Repaired inverse binds each replacement to its exact intermediate offset.',
    guards=2,individual_edits=sum(len(g['changes']) for g in guards),all_old_displays_preserved=True,all_labels_tags_preserved=True,exact_inverse=True,
    events_added=0,source_mutations=0,
    files=[dict(path=p.relative_to(R).as_posix(),bytes=p.stat().st_size,sha256=sha(p.read_bytes())) for p in sorted(out.iterdir())])
(out/'proposal_index.json').write_text(json.dumps(index,indent=2)+'\n')
print(json.dumps(index,indent=2))
