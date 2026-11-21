from pathlib import Path
import re,json,hashlib,datetime
R=Path('/workspace/scratch/653608133b22'); O=R/'work/agents/i_provenance';P=R/'work/S6_SERIES_PUBLISH_I.tex';original=P.read_text();s=original;changes=[];archives=[]
def add(old,new,reason,scope):
 global s
 assert s.count(old)==1,(scope,s.count(old),old[:150])
 changes.append(dict(id=f'IP-C11-T{len(changes)+1:02}',statement=scope,old=old,new=new,reason=reason))
 s=s.replace(old,new,1)
def block(text,label,kind='proof'):
 k=text.index('\\label{'+label+'}');a=text.rfind('\\begin{',0,k)
 if kind=='proof': b=text.index('\\end{proof}',k)+len('\\end{proof}')
 else:b=text.index('\\end{'+kind+'}',k)+len('\\end{'+kind+'}')
 return text[a:b]
def archive(label,kind='proof'):
 old=block(original,label,kind);new=block(s,label,kind);slug=label.replace(':','_').replace('.','_')
 a=O/f'S6_SERIES_PUBLISH_I_candidate11_tail_{slug}_old.tex';b=O/f'S6_SERIES_PUBLISH_I_candidate11_tail_{slug}_proposed.tex';a.write_text(old);b.write_text(new)
 archives.append(dict(statement=label,old=str(a),proposed=str(b),old_sha256=hashlib.sha256(old.encode()).hexdigest(),proposed_sha256=hashlib.sha256(new.encode()).hexdigest()))

lab='ari:C.6.R5';old=block(s,lab)
for m in re.finditer(r'\\item \\textbf\{[1-6]\. [^}]+\}',old):
 a=m.group();b=re.sub(r'\\textbf\{[1-6]\. ',r'\\textbf{',a)
 add(a,b,'Remove a literal stage number already supplied by the enclosing numbered list. Every mathematical word, formula and step is retained.',lab)
archive(lab)
add('The mean of $U$ is zero by the theta product calculation in C.1,','The mean of $U$ is zero by the theta product calculation in \\cref{ari:C.1.1},','Replace an inherited section shorthand by the exact supplying result.','ari:C.8.6')
add('identity of C.1 gives the product of $N$ at those half-periods','identity of \\cref{ari:C.1.1} gives the product of $N$ at those half-periods','Replace an inherited section shorthand by the exact supplying result.','ari:C.8.6');archive('ari:C.8.6')
add('For $P$ as in Statement \\ref{ari:C.7.1}, $N(P)$','For $P$ as in \\cref{ari:C.7.1}, $N(P)$','Use the numbered statement kind supplied by cleveref.','ari:C.7.2');archive('ari:C.7.2')
old=block(s,'push:section:E.4','remark')
new=old.replace('[Independent interval verification]','[Interval enclosures]').replace('An independent proof of \\cref{fam:src:C.2.3} uses contraction\nenclosures for the zeros of $\\wp$, explicit theta and eta tails,\nand an exact cover of the compact modular region. The verification records linked in Section~1.5 give this proof\nand its separate local argument.','The interval bounds for the norm in \\cref{fam:src:C.2.3} combine\ncontraction enclosures for the zeros of $\\wp$, explicit theta and eta\ntails, and an exact cover of the compact modular region.')
assert new!=old
add(old,new,'Retain the exact interval ingredients and all four old anchors; archive the independence and check-record narration. The full maximum proof remains in the supplying result.','push:section:E.4');archive('push:section:E.4','remark')

lab='ari:C.7.12';old=block(s,lab)
for m in re.finditer(r'\\begin\{enumerate\}\[label=\{\$\\langle[23]\\rangle\$\\arabic\*\.\}[^\n]*\n\\item[^\n]*',old):
 a=m.group();b=a.replace(r'label={$\langle2\rangle$\arabic*.}',r'label=(\alph*)').replace(r'label={$\langle3\rangle$\arabic*.}',r'label=(\roman*)')
 add(a,b,'Replace proof-production hierarchy markers by ordinary nested list labels; preserve all words, formulas, steps, labels and citations.',lab)
archive(lab)

# The supplying period-morphism and finite-norm equations were reread in full.
lab='night:P5.5';old=block(s,lab);new=old
a='''\\item On each ordinary torus, a lifted holomorphic automorphism
has lattice-periodic derivative, hence constant derivative by
compactness. Thus it is affine. Its integral linear part commutes
with $A_1,A_2$, and \\cref{fam:src:A.2.1} gives
$P=aI+bE_{41}$ with $a,b\\in\\mathbb Z$ and $a=\\pm1$.
The identity period columns in $H\\Pi=\\Pi P$ give $H=aI$;
the first column then gives $b=0$.

\\item The linear part $-I$ is excluded by the first multiple fibre.  Normalize
the root base change $t=s^3$.  The automorphism lifts, fixing $s$; on the
central covering torus it is $z\\mapsto-z+b$.  Commutation with the affine
deck transformation gives
\\[
 (I-A_1)b=2v_1/3\\pmod\\Lambda.
\\]
The torus character $\\gamma:\\Lambda_{\\mathbb R}/\\Lambda\\to\\mathbb R/\\mathbb Z$
annihilates $I-A_1$, whereas the right side has character $2l_1/3$.
Freeness implies $3\\nmid l_1$, a contradiction.  Thus every automorphism
is fibrewise translation.'''
b='''\\item Apply the affine-lift and centralizer calculation of
\\cref{fam:src:A.2.1} with $c'=c$. The period equation
\\eqref{wb:pshift:eq:period-morphism} gives the integral linear part
$P=aI+bE_{41}$, $a=\\pm1$, and the complex linear part $H=aI$;
its first column gives $b=0$.

\\item The finite-root equation
\\eqref{wb:pshift:eq:finite-norm-obstruction}, with $n=0$,
gives $N_1\\ell=-(1-a)v_1$. For $a=-1$, applying the invariant
covector $\\gamma$ gives $3\\gamma(\\ell)=-2l_1$, where
$l_1=\\gamma(v_1)$. Freeness gives $3\\nmid l_1$, so this
integer equality is impossible. Thus $a=1$, and every
automorphism is fibrewise translation.'''
assert a in new;new=new.replace(a,b)
a='''A cocycle on the punctured orbifold is a pair $(x_1,x_2)$ with
$N_1x_1=N_2x_2=0$, where
\\[
 N_1=\\begin{pmatrix}3&0&0&0\\\\6&0&0&0\\\\-12&0&0&0\\\\0&2&1&3\\end{pmatrix},\\qquad
 N_2=\\begin{pmatrix}4&0&0&0\\\\12&0&0&0\\\\-12&0&0&0\\\\0&2&2&4\\end{pmatrix}.
\\]'''
b='''A cocycle on the punctured orbifold is a pair $(x_1,x_2)$ with
$N_1x_1=N_2x_2=0$, for the norm matrices in
\\eqref{wb:pshift:eq:norms}.'''
assert a in new;new=new.replace(a,b)
add(old,new,'Use the same exact affine, period and finite-norm maps from the preceding integral parameter comparison. Keep the general twist integer l1, all translation-sheaf/cusp-extension arguments, and the complete torsion-sensitive H1 calculation.',lab);archive(lab)

# Positive mathematical wording: no mathematical step is deleted.
for lab,a,b in [
('ari:C.6.5','that pair, so no unproved choice of root is needed.','that pair, so either zero gives the same value of $N$.'),
('ari:C.6.R5','values, with no BSD input','values from the displayed integrality and interval bounds'),
]:
 if a in s:
  k=s.index(a);context=s[s.rfind('\n',0,k)+1:s.find('\n',k+len(a))]
  add(context,context.replace(a,b),'State the exact mathematical reason in positive form.',lab)
archive('ari:C.6.5')

# Refresh archives after the final wording edits.
for a in archives:
 f=Path(a['proposed']);new=block(s,a['statement'],'remark' if a['statement']=='push:section:E.4' else 'proof');f.write_text(new);a['proposed_sha256']=hashlib.sha256(new.encode()).hexdigest()

payload=dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),source=str(P),source_sha256=hashlib.sha256(original.encode()).hexdigest(),source_writes=False,changes=changes,complete_proof_archives=archives,presentation_changes_create_mathematical_events=False,substantive_consolidation_scope='night:P5.5 only: exposed full proof comparison; no independent/targeted/computational credit')
(O/'S6_SERIES_PUBLISH_I_candidate11_tail_guards.json').write_text(json.dumps(payload,indent=2,ensure_ascii=False)+'\n')
print(len(changes),'tail guards',len(archives),'complete proof/remark archives; source SHA',payload['source_sha256'])
