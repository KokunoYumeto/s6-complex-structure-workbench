from pathlib import Path
import re, subprocess
root=Path(__file__).resolve().parents[2]
# Retain the complete independently authored include sequence on regeneration.
existing_aggregate=(root/'notes/part3.tex').read_text()
preserved_includes=re.findall(r'^\\input\{notes/[^}]+\}\s*$',existing_aggregate,re.M)
source=(root/'notes/part3_family.md').read_text()
extra=(root/'notes/part3_other_families.md').read_text()
source+='\n'+extra[extra.index('## P3F.16.'): ]
weighted=(root/'notes/part3_os47.md').read_text()
weighted=re.sub(r'^## (?!P3F)', '### ', weighted, flags=re.M)
weighted=weighted.replace('# P3F.21.', '## P3F.21.',1)
source+='\n'+weighted
for filename in ('part3_transfer.md','part3_os47_clutch.md','part3_mapping_torus.md','part3_return_classes.md','part3_os49_component.md','part3_os49_index_input.md','part3_os49_all_orders.md','part3_os49_norm.md','part3_os49_positive_fan.md','part3_os49_positive_orders.md','part3_os49_cap_scope.md','part3_os49_noncoprime_homology.md','part3_arbitrary_fan.md'):
    addition=(root/'notes'/filename).read_text()
    addition=re.sub(r'^## (?!P3F)', '### ', addition, flags=re.M)
    addition=re.sub(r'^# (P3F\.)', r'## \1', addition, flags=re.M)
    source+='\n'+addition
parts=re.split(r'^## P3F\.(\d+)\. (.*)$',source,flags=re.M)
summary={
1:r'The torsion-free rank-one Mordell--Weil rows are exactly eight, and their Kodaira refinements give exactly twenty-one realized configurations.',
2:r'The section-intersection formula has the positive local-correction term, and the primitive sections in the eight rows have intersection zero with the zero section.',
3:r'The exact Torelli presentation is $I(S^2\times S^3)=\Z a\oplus\Z b$, with $(k,\ell)(a)=(1,4)$ and $(k,\ell)(b)=(8,8)$.',
4:r'The Hopf lift of every $a$-power extends over $D^4\times S^3$; its specified sphere gluing is standard.',
5:r'The Haefliger formula applies to an actual Seifert surface. The compact elliptic page has characteristic class $K=5F$, so the determinant correction must be retained.',
6:r'The two explicit degree-twelve maps of the same genus-three curve give respectively one $I_{12}$ fibre and twelve $I_1$ fibres. Both give $\chi(\mathcal O)=1$, signature $-8$, height $2$, and $(mP)\cdot O=m^2-1$.',
7:r'The actual circle orbit pair is $(S^5,S^2)$, with fixed normal bundle $\mathcal O(-1)\oplus\mathcal O(-1)$ of weights $(-1,+1)$. The specified conifold replacement is free with quotient $S^2\times S^3$.',
8:r'The actual equivariant family return has a typed Hopf-lift image in the Torelli group, and its clutched sphere is the displayed Hopf gluing.',
9:r'The resolved cusp orbit has a relative product comparison with a nodal elliptic neighbourhood times the marked gamma circle, retaining the stable outer framing.',
10:r'The actual regular-binding page has twelve nodal fibres and boundary $T^3$. Its circle-line square is $s_\delta=-2$ and its relative Pontryagin pairing is $p_{\rm rel}=-24$.',
11:r'The integer $A=(4k-\ell)/24$ is independent of the equivariant normal trivialization and is additive. Six parameter loops give exactly six times the integer of one loop.',
12:r'The compact fixed-sheet torsor is smoothly translation-trivial through the specified $I_{12}$ model; the transported circle line differs from $\mathcal O(P-O)$ only by an integral fibre class.',
13:r'The angular origin comparison is $\theta\gamma+6\theta(1-\theta)\delta$ and its full $Q$-deck line clutch has winding $-12$. The earlier complex corner attempt remains uncompleted; the actual real trace P3K.6--9 now proves the monodromy application.',
14:r'The inherited spin$^c$ index of a fixed-sheet Hopf boundary is precisely $\chi(S,L_+)$, independently of the negative-weight normal line.',
15:r'The explicit cyclic action on the twelve labelled node charts extends by units and has the required twelfth-iterate gamma period and circle-line winding. Its free labelled central quotient has multiplicity twelve and is not asserted to be the outer cusp chart.',
16:r'The actual labelled comb-smoothing parameter loop has identity smooth monodromy, by a single-valued radial trivialization of the entire glued family.',
17:r'For coprime multiplicities $(3k,4l)$ the regular-binding page has degree $12kl$, Euler characteristic $12kl$, signature $-8kl$, section-line square $-2kl$ and relative Pontryagin pairing $-24kl$.',
18:r'The two supplied one-logarithmic families have degree-four regular-binding page covers; their precise source and page fibre types are those listed below.',
19:r'Yang Type B and Type C have explicit nontrivial cyclic quotients of their fundamental groups, excluding homeomorphisms to the six-sphere.',
20:r"Wang's supplied threefold is simply connected with $H_2=H_3=\Z/2$, as computed by the full integral exterior and clutch complex.",
21:r'The weighted OS47 data $M=\mathcal O(7G-O)$ and $Q=2G$ give an actual holomorphic sphere family over $\lambda=r^4$. Its actual page has $s_\delta=-14$ and $p_{\rm rel}=-72$; its circle action is semifree through the entire $I_7$ filling.',
22:r'The specified Hopf gluing has Eells--Kuiper invariant $\mu(\lambda(f))=A(f)/28$. It is a homomorphism to $\Theta_7$, and $\lambda(b)$ is the generator with $\mu=1/28$.',
23:r'The positive OS47 $r$-loop has angular clutch $\theta\gamma+2\theta(\theta-1)\delta$, hence one positive gamma turn; its fourth-root cusp deck gauge has winding positive four.',
24:r'The forward sphere mapping torus is $(S^1\times S^6)\#\Sigma_\Phi$; both spin structures have Eells--Kuiper invariant $\mu(\Sigma_\Phi)$. A nonzero value excludes even an unoriented diffeomorphism with the product.',
25:r'The actual real trace gives $A=(12s_\delta-p_{\rm rel})/24=-R\cdot O$, with both mapping-torus and bordism boundary reversals included. The original, coprime higher, Viaclovsky and Liu--Rollenske values are zero. The positive weighted OS47 loop has $A=-4$, oriented class $24\pmod{28}$, and a mapping torus not diffeomorphic to the product.',
26:r'The explicit $IV^*+II+I_2$ source with $M=\mathcal O(G-O)$ and $Q=3G$ has component-supported linearization divisor $C_0$. Its specified local fillings and order-three cap give a simply connected integral homology six-sphere, hence the standard smooth $S^6$.',
27:r'The positive OS49 loop over $\lambda=r^3$ has actual cusp angular cycle $K=3u+2\gamma$ and retained line clutch of winding six on the sixth-root cusp cover. The exact change of page marking is given below. Its original direct graph-line comparison remains an auxiliary route; P3F.31 proves positive-fan index zero, and P3K.65 gives negative-fan class \(-3\) for this \(r\)-loop.',
28:r'The actual OS49 linearization gives the exact sequence $0\to T^*M\to M\to\mathcal O_{C_0}(-1)\to0$. Its iterates alternate the two components, and all the translated source-line direct images vanish. The direct mixed-circle symbol comparison remains an auxiliary route. The actual positive-fan index is computed in P3F.31--32, and P3K.65 computes the corrected negative-fan sphere class by the native Cox arrow.',
29:r'For every OS49 cap order $m=3k$ and invariant vector $\ell=n(1,-1,0,0)+d\delta$ with $\gcd(n,m)=1$, the specialization indices are $(m,k,k,m)$ and all four integral Leray differentials are multiplication by $n$. The fundamental group and homology in degrees one through four are $\Z/|n|$. Every $n=\pm1$ member is the standard $S^6$, for every $k$ and $d$.',
30:r'The actual quadratic norm morphism has target line $N=M\otimes T^*M=M^2(-C_0)$ and scalar $\lambda^2$. It completes to $X/\mu_2$, with transverse $A_1$ equation along the fixed curve. The two fixed sections of its resolution have opposite Hopf-line base shifts $+1,-1$, which must be retained in this auxiliary norm route. The positive-fan return index is zero by P3F.31; P3K.65 gives the original negative-fan \(r\)-loop class \(-3\) by the full native Cox comparison.',
31:r'The explicit positive-diagonal OS49 filling over $\lambda=r^3$ is a sphere family with positive-loop return index zero, oriented homotopy-sphere class zero, and product mapping torus. Its actual page carries the source line through both $I_2$ components and nodes. P3K.65 gives the actual native C2 flop comparison and the negative-diagonal \(r\)-loop class \(-3\).',
32:r'For the positive-diagonal OS49 filling, every cap order $m=3k$, numerator $n=\pm1$, and integral delta twist gives a sphere family with zero positive-loop return index and product mapping torus. The actual angular clutch is $n\theta K+nm\theta(\theta-1)\delta$, and its root-deck line gauge has winding $2mn$.',
33:r'The explicit order-$3k$ OS49 affine cap is free exactly when $\gcd(k,n,d)=1$ and either $3\nmid n$ or $3\mid k$. Every free cap gives fundamental group $\Z/|n|$, so its sphere sector is exactly $n=\pm1$.',
34:r'For every free affine OS49 cap with $n\ne0$, let $g=\gcd(3k,n,3d)\in\{1,3\}$. Then $H_1=H_4=\Z/|n|$ and $H_2=H_3=\Z/|n|\oplus\Z/g$. The free cap $(m,n,d)=(9,3,1)$ has $H_2=H_3=(\Z/3)^2$, correcting the general-n CSV value. The complete $n=0$ groups are also computed below.',
35:r'Every one-vertex unimodular cusp fan is an integral-basis triangulation, and explicit periodic diagonal flops connect it to the vertical-edge fan while preserving sphere topology. For every prime, its cusp fixed set has total mod-prime Betti number two; Smith--Floyd therefore forces every separate cap in a sphere member to have free delta action, without a semifree hypothesis at the cusp.'
}

def normalize_math(md):
    # Preserve all already well-formed single-backslash delimiters before
    # repairing the older mixed ( ... \\) notation in the working notes.
    md=re.sub(r'\\\((.*?)\\\)',lambda m:'$'+m.group(1)+'$',md,flags=re.S)
    md=md.replace(r'\[','$$').replace(r'\]','$$')
    md=md.replace(r'\)',')').replace(r'\(','(')
    lines=[]
    def mathematical(t):
        stripped=re.sub(r'\\[A-Za-z]+','',t)
        words=re.findall(r'[A-Za-z]{4,}',stripped)
        if words: return False
        return bool(re.search(r'[\\_^=<>]',t) or re.fullmatch(r'[A-Za-z0-9*+., /;:|{}\-]+',t))
    in_display=False
    in_fence=False
    for line in md.splitlines():
        if line.strip().startswith('```'):
            in_fence=not in_fence
            lines.append(line);continue
        if line.strip()=='$$':
            in_display=not in_display
            lines.append(line);continue
        if in_display or in_fence or line.startswith('    ') or '$' in line:
            lines.append(line); continue
        # Balanced outer parentheses, including h(P), are converted together.
        out=[]; i=0
        while i<len(line):
            if line[i]!='(':
                out.append(line[i]);i+=1;continue
            depth=1;j=i+1
            while j<len(line) and depth:
                if line[j]=='(':depth+=1
                elif line[j]==')':depth-=1
                j+=1
            if depth:
                out.append(line[i:]);break
            inside=line[i+1:j-1]
            out.append('$'+inside+'$' if mathematical(inside) else line[i:j])
            i=j
        lines.append(''.join(out))
    return '\n'.join(lines)+'\n'
out=['% Generated from the current-run complete proofs by code/part3/render_part3_tex.py.\n',r'\providecommand{\tightlist}{\setlength{\itemsep}{0pt}\setlength{\parskip}{0pt}}'+'\n',r'\noindent The following proofs retain their explicit construction maps and scope. Uncompleted auxiliary comparisons are identified at their exact remaining step.'+'\n']
for j in range(1,len(parts),3):
 n=int(parts[j]);title=parts[j+1];body=parts[j+2]
 title=re.sub(r'^(Proved:\s*)','',title)
 if n==4:
  title='The Hopf gluing associated with the first cyclic subgroup'
 body=body.replace('**Proved.**','').replace('**End of proof.**','').replace('Proof. ','').replace('End of proof.','')
 # The supplied working prose includes older mixed parenthesis math markup.
 body=normalize_math(body)
 # Restore proper math for expressions that already used paired dollar or display delimiters.
 p=subprocess.run(['pandoc','-f','markdown+tex_math_single_backslash-raw_tex','-t','latex','--wrap=none'],input=body,text=True,capture_output=True,check=True)
 tex=p.stdout
 if n==1:
  for width in ['0.1000','0.2100','0.1000','0.5900']:
   tex=tex.replace(r'\real{0.2500}',r'\real{'+width+'}',1)
 if n==25:
  widths=iter(['0.46','0.06','0.18','0.08','0.07','0.05','0.10'])
  tex=re.sub(r'\\real\{[0-9.]+\}',lambda m:r'\real{'+next(widths)+'}',tex,count=7)
 tex=re.sub(r'\\texttt\{((?:code|records|notes)/[^}]+)\}',lambda m:r'\path{'+m.group(1).replace(r'\_','_')+'}',tex)
 tex=tex.replace('arXiv:math/0506356',r'\nolinkurl{arXiv:math/0506356}')
 tex=re.sub(r'\\begin\{verbatim\}',r'\\begin{lstlisting}',tex)
 tex=tex.replace(r'\end{verbatim}',r'\end{lstlisting}')
 # The monospace font lacks Unicode superscripts; text superscripts are
 # emitted as TeX, while executable-looking blocks retain plain ASCII.
 sup=dict(zip('⁰¹²³⁴⁵⁶⁷⁸⁹⁻','0123456789-'))
 chunks=re.split(r'(\\begin\{lstlisting\}.*?\\end\{lstlisting\})',tex,flags=re.S)
 for ci,chunk in enumerate(chunks):
  if chunk.startswith(r'\begin{lstlisting}'):
   chunks[ci]=''.join('^'+sup[c] if c in sup else c for c in chunk)
  else:
   chunks[ci]=''.join(r'\textsuperscript{'+sup[c]+'}' if c in sup else c for c in chunk)
 tex=''.join(chunks)
 # Headings with naked symbols stay text; the proof itself retains display equations.
 title=title.replace('&',r'\&').replace('_',r'\_').replace('%',r'\%')
 out += [f'\\subsection{{{title}}}\n',f'\\begin{{statement}}{{P3F.{n}}}{{Proved}}\n',summary[n]+'\n',r'\end{statement}'+'\n',r'\begin{proof}'+'\n',tex,r'\end{proof}'+'\n']
for include in (preserved_includes or [r'\input{notes/part3_fourfold.tex}']):
    out.append(include.strip()+'\n')
(root/'notes/part3.tex').write_text(''.join(out))
print(root/'notes/part3.tex')
