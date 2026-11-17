"""Print the entire verified finite cobar certificate as a LaTeX proof block."""
from pathlib import Path
import hashlib
import json

ROOT=Path(__file__).resolve().parents[3]
SOURCE=ROOT/'deliverables/code/maps_audit/course/stable/ORIGINAL_COEFFICIENT_H28_CERTIFICATE.json'
WORK=ROOT/'deliverables/work/maps_audit'
data=json.loads(SOURCE.read_text())
lines=[r'''% Full finite certificate, transcribed from the independently reproduced JSON.
% This is an appendix proof block, not an assembly of Paper III.
\subsection{Complete original-coefficient matrix certificate}
\label{courseIII:coefficient-complete-certificate}
We retain the coefficient ring $\mathbb F_2[\tau_{\mathrm h}]$,
where $|\tau_{\mathrm h}|=(0,-1)$ in internal degree and weight.
Write $t_i=\tau_i$ and $x_i=\xi_i$ in the tables below.
Their ordered internal degrees are $(1,3,7,2,6)$ and their weights
are $(0,1,3,1,3)$. The first three exponents in every basis
monomial are zero or one; multiplication uses
$t_0^2=\tau_{\mathrm h}x_1$ and
$t_1^2=\tau_{\mathrm h}x_2$. Terms involving $t_2^2$ lie above
the internal degree under consideration.

Here are all the original basis words in internal degree eight.
The numbering in each length starts at one and is independent of
the numbering in the other lengths. If $b_{f,j}$ has weight $v$,
its weight-$w$ representative is
$\tau_{\mathrm h}^{v-w}b_{f,j}$ whenever $v\geq w$.
No such representative is present when $v<w$.
''']
names=[r't_0',r't_1',r't_2',r'x_1',r'x_2']
def monomial(m):
 result=[]
 for name,power in zip(names,m):
  if power: result.append(name if power==1 else name+'^{'+str(power)+'}')
 return ' '.join(result) or '1'
def word(v):
 return '['+r'\mid '.join(monomial(m) for m in v)+']'
def weight(v): return sum(sum(a*b for a,b in zip(m,data['weights'])) for m in v)
def key(v): return tuple(tuple(m) for m in v)
indices={f:{key(v):i+1 for i,v in enumerate(data['full_bases'][str(f)])} for f in [1,2,3]}
for f in [1,2,3]:
 lines += [r'\paragraph{Length '+str(f)+r'.}',r'\begin{longtable}{r l r}',r'Index & Original basis word & Weight\\\hline',r'\endhead']
 for j,v in enumerate(data['full_bases'][str(f)],1):
  lines.append(f'{j} & ${word(v)}$ & {weight(v)}'+r'\\')
 lines.append(r'\end{longtable}')

lines.append(r'''\paragraph{All coefficient differential columns.}
The next tables give every term of every column of $d_1$ and
$d_2$ before any coefficient is inverted. A target index denotes
the basis vector of the next length. Unlisted terms in a displayed
column have coefficient zero; the symbol $0$ denotes the zero column.
Thus these are full matrices in sparse form, with all coefficient
powers specified. They follow by multiplying the full coproducts
\[
\begin{aligned}
\overline\Delta t_0&=0,&
\overline\Delta t_1&=x_1\otimes t_0,&
\overline\Delta t_2&=x_2\otimes t_0+x_1^2\otimes t_1,\\
\overline\Delta x_1&=0,&
\overline\Delta x_2&=x_1^2\otimes x_1,
\end{aligned}
\]
and inserting each reduced coproduct at each place of the word.
Every full coproduct also has its two counit terms.
''')
for f in [1,2]:
 lines += [r'\begin{longtable}{r p{0.78\linewidth}}',r'Column of $d_'+str(f)+r'$ & Full image in the original next-length basis\\\hline',r'\endhead']
 for row in data['full_original_differential']:
  if row['length']!=f: continue
  terms=[]
  for t in row['terms']:
   power=t['coefficient_power']
   coef='' if not power else (r'\tau_{\mathrm h}' if power==1 else r'\tau_{\mathrm h}^{'+str(power)+'}')
   terms.append(coef+'b_{'+str(f+1)+','+str(indices[f+1][key(t['target_word'])])+'}')
  lines.append(str(row['column']+1)+' & $'+(' + '.join(terms) or '0')+r'$\\')
 lines.append(r'\end{longtable}')

def list_rows(label,values,chunk=8):
 vals=[str(v) for v in values]
 if not vals: vals=['\varnothing']
 out=[]
 for start in range(0,len(vals),chunk):
  out.append((label if start==0 else '')+' & $'+r',\ '.join(vals[start:start+chunk])+r'$\\')
 return out

lines.append(r'''\paragraph{The five weight slices and exact rank witnesses.}
For each weight below, the listed basis indices refer to the complete
bases above and are taken in that order. The binary column integer
$c$ means that row $i$ is the coefficient of $2^{i-1}$ in $c$.
This convention specifies every zero and nonzero matrix entry.
All columns are listed, including zero columns. For each rank witness,
the listed row and column indices are local to that weight slice and
start at one. The minor row integers use the displayed selected-column
order. The last integer specifies a row functional on the length-two
basis by the same binary convention.
''')
for row in data['weight_slices']:
 w=row['weight']; n=row['dimensions']['2']
 lines += [r'\subparagraph{Weight $'+str(w)+r'$.}',r'\begin{longtable}{l l}',r'\endhead']
 for f in [1,2,3]:
  lines += list_rows('$C^{'+str(f)+'}$ basis indices',[indices[f][key(v)] for v in row['bases'][str(f)]])
 lines += list_rows('$d_1$ columns',row['d1_columns_binary'])
 lines += list_rows('$d_2$ columns',row['d2_columns_binary'],chunk=4)
 for d in [1,2]:
  witness=row[f'd{d}_rank_witness']
  lines += list_rows('$d_'+str(d)+'$ minor rows',[i+1 for i in witness['rows']])
  lines += list_rows('$d_'+str(d)+'$ minor columns',[i+1 for i in witness['columns']])
  lines += list_rows('$d_'+str(d)+'$ minor row integers',witness['minor_rows_binary'],chunk=6)
  lines += ['$d_'+str(d)+r'$ minor determinant & $1\in\mathbb F_2$'+r'\\']
 lines += list_rows('Cycle column',[row['cycle_column']+1])
 lines += list_rows('Nonboundary functional',[row['nonboundary_functional_binary']])
 lines.append(r'\end{longtable}')
 r1=row['d1_rank_witness']['rank_lower_bound'];r2=row['d2_rank_witness']['rank_lower_bound']
 lines.append(f'The two displayed minors have orders ${r1}$ and ${r2}$, and ${n}={r1}+{r2}+1$. ')
 lines.append(r'The full columns give $d_2d_1=0$. The displayed functional vanishes on every $d_1$ column and takes value one on the displayed cycle, whose $d_2$ column is zero. Therefore the ranks are exactly the two displayed minor orders and the quotient has dimension one. Its generator is $\tau_{\mathrm h}^{'+str(4-w)+r'}[x_1^2\mid x_1^2]$.' if w!=4 else r'The full columns give $d_2d_1=0$. The displayed functional vanishes on every $d_1$ column and takes value one on the displayed cycle, whose $d_2$ column is zero. Therefore the ranks are exactly the two displayed minor orders and the quotient has dimension one, generated by $[x_1^2\mid x_1^2]$.')

lines.append(r'''\paragraph{Why these finite matrices give the whole coefficient module.}
In this internal degree the weight of an original word is at most four,
so all larger weight slices have zero cochains. In nonpositive weights,
the previously proved coefficient comparison identifies the entire
original complex with the corresponding classical complex, retaining
its polynomial coefficients. The weight-zero slice above supplies its
one-dimensional cohomology. Multiplication by $\tau_{\mathrm h}$
takes each displayed generator to the displayed generator in the
next lower weight. Consequently
\[
 H^{2,8,*}=\mathbb F_2[\tau_{\mathrm h}]\,
 e,\qquad e=[x_1^2\mid x_1^2],\quad |e|_{\rm weight}=4.
\]
There is no coefficient torsion and no additional class in any weight.
The original quadratic relation gives
$[t_0^4\mid t_0^4]=\tau_{\mathrm h}^4e$.
The exact localized comparison sends $e$ to
$\tau_{\mathrm h}^{-4}[\zeta_1^4\mid\zeta_1^4]$, and thus
sends $\tau_{\mathrm h}^4e$ to the unscaled original classical class.

The two matrix ranks in each slice are justified by the displayed
nonzero minors, the full differential identity, and the displayed
nonboundary functional. The tabulated finite verification is therefore
a complete rank certificate, rather than a numerical estimate.
''')
out=WORK/'coefficient_h28_complete_certificate.tex'
out.write_text('\n'.join(lines)+'\n')
record=dict(source_json=str(SOURCE.relative_to(ROOT)),source_sha256=hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
            printed_proof=str(out.relative_to(ROOT)),printed_proof_sha256=hashlib.sha256(out.read_bytes()).hexdigest(),
            full_basis_sizes={f:len(v) for f,v in data['full_bases'].items()},
            all_original_columns_printed=len(data['full_original_differential']),weight_slices=5,
            completeness='Every original monomial basis word, every coefficient differential term, every weight-slice column, and every minor/nonboundary witness is printed. No original equation or zero column is dropped.',
            dependency='The previously printed original coefficient/weight comparison is used only for nonpositive weights; this is already fully read in the coefficient-ring chapter.',
            reader='GPT-6 Astra (OpenAI, ChatGPT Pro mode)',effort='Pro',date='2026-11-17')
(WORK/'coefficient_h28_printed_certificate_record.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(record))
