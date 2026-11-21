from pathlib import Path
import json,hashlib
b=Path('/workspace/scratch/653608133b22');p=b/'work/S6_SERIES_PUBLISH_V.tex';s=p.read_text();rows=[]
def add(fid,gid,pages,types,old,new,why):
 n=s.count(old)
 assert n==1,(gid,n)
 rows.append({'finding_id':fid,'guard_id':gid,'pages':pages,'defect_types':types,'old':old,'new':new,'expected_occurrences':1,'proof_scope':why})
add('AQA01','analytic_final_01',[31],['D23'],r'The local filling theorem \cref{night:P1.9} applies to this bounded',r'\Cref{night:P1.9} applies to this bounded','Remove duplicated theorem noun printed by cref; theorem cited and application unchanged.')
add('AQA02','analytic_final_02',[38],['D23'],r'The proposition \cref{sec:V-known-inputs} gives',r'\Cref{sec:V-known-inputs} gives','Remove duplicated proposition noun; characteristic-number input unchanged.')
add('AQA03','analytic_final_03',[38],['D23'],r'\item The theorem \cref{maps:src:F.2.6} gives three-connectivity,',r'\item \Cref{maps:src:F.2.6} gives three-connectivity,','Remove duplicated theorem noun; topology input unchanged.')
add('AQA04','analytic_final_04',[40],['D23','D18'],"\\item Kramer--Stolz's\n\\cite[Theorem~A, p.~178]{IVVKramerStolz} applies to", "\\item The theorem of Kramer and Stolz\n\\cite[Theorem~A, p.~178]{IVVKramerStolz} applies to",'Supply the missing noun and retain the exact primary locator; no change to the absorption argument.')
add('AQA05','analytic_final_05',[42],['D22'],r'''In particular $h_b(1)<-1$. The parameter $c=5/(3\pi)$,
the exceptional value of \cref{night:P1A.2}, lies outside
the global transversality domain.''',r'''In particular $h_b(1)<-1$. The value $c=5/(3\pi)$, for which
the determinant $\det C_1$ in \cref{night:P1A.2} vanishes at
$\xi=ic$, lies outside the global transversality domain.''','Name the algebraic reason for this value at its first occurrence. The unchanged displayed determinant is a nonzero constant times384z+3125 and z=(625pi i/128)xi, so xi=5i/(3pi) is its unique zero.')
add('AQA06','analytic_final_06',[45],['D22','D20'],r'''weights $(0,1,2)$, and those of $G$ as $(g_0,g_1,g_2)$ of
weights $(0,-1,-2)$. The residue of the quotient connection is''',r'''weights $(0,1,2)$, and those of $G$ as $(g_0,g_1,g_2)$ of
weights $(0,-1,-2)$. Put $z=(625\pi i/128)\xi$.
The residue of the quotient connection is''','Move the exact auxiliary-coordinate definition before the residue coefficients that use it; this is the same morphism already printed in Step5 of the attached original.')
add('AQA06','analytic_final_07',[45],['D22','D12'],r'''whole admissible parameter domain. \Cref{night:P1.15} identifies $z=(625\pi i/128)\xi$ on the full complex
parameter plane, and hence $z=-(625\pi/128)c$ when $\xi=ic$.''',r'''whole admissible parameter domain. For $\xi=ic$ the preceding
coordinate relation gives $z=-(625\pi/128)c$.''','The conversion is now defined in Step1; preserve its exact specialization and the subsequent exceptional-zero calculation.')
add('AQA07','analytic_final_08',[46],['D08','D12'],r'''The bound used here is
\cref{night:P1.18}.
Consequently the three connecting ranks are $1,3,1$.''',r'''Consequently the three connecting ranks are $1,3,1$.''','The same theorem and bound are already cited in the immediately preceding sentence. Remove the redundant dependency sentence only.')
add('AQA08','analytic_final_09',[48],['D20'],r'''In a fixed holomorphic splitting, two members of the full
admissible complex parameter half-plane are biholomorphic
exactly when their parameters are equal.''',r'''Two members $M_\xi,M_\eta$ of the family in
\cref{pub:V:parameter} are biholomorphic exactly when $\xi=\eta$.''','Use the canonical family already defined in section1. The stronger any-fixed-splitting formulation follows under the exact translation in Remark3.8; parameter equality is preserved because both coordinates translate by the same scalar.')
add('AQA08','analytic_final_10',[50],['D20'],r'''$(\sigma+\xi\alpha e)(P)$ are equal precisely when their''',r'''$(\sigma_b+\xi\alpha e)(P)$ are equal precisely when their''','Use the canonical splitting in the graph comparison. Exact translation between arbitrary splitting and sigma_b was proved in Remark3.8 and is unchanged.')
old=r'''\item We first recover the base intrinsically.  An effective divisor on
$M_c$ cannot be horizontal: its first Chern class vanishes by
$H^2(M_c;\mathbb Z)=0$, whereas its nonzero effective restriction to a
general torus fibre would have positive pairing with the square of a
flat K\"ahler class.  The pole divisor of any meromorphic function is
therefore vertical.  On every regular fibre outside that divisor the
function is holomorphic and hence constant.  It factors through a
meromorphic function on the base, which is rational on
$\mathbb P^1$.  Thus the function field is exactly $\mathbb C(\lambda)$.
An anti-biholomorphism consequently induces an anti-M\"obius map of
the base.  The two distinct multiplicities $5,4$ and the singular cusp'''
new=r'''\item By \cref{night:P1A.4}, the meromorphic function field of each
member is $\mathbb C(\lambda)$, with the given base map as its
algebraic reduction.  An anti-biholomorphism therefore induces an
anti-M\"obius map of the base.  The two distinct multiplicities $5,4$
and the singular cusp'''
add('AQA09','analytic_final_11',[50],['D12'],old,new,'Replace the second proof of intrinsic algebraic reduction by the preceding theorem, whose first proof step establishes precisely the same function field and base map for every admissible complex parameter. The subsequent fixing of three real marked values and every anti-intertwiner/fan calculation are unchanged. The attached original alternative H2/divisor proof is retained in this guarded before-text/check record.')
add('AQA10','analytic_final_12',[54],['D02','D11'],r'''All contradictions occur on a noncentral compact smooth
torus fibre of the recovered marked map.  The reductions and
modifications are proper and preserve the prescribed open
family; they impose no smoothness, multiplicity or component
condition on the original central fibre.  The permitted
central spaces therefore do not avoid the contradiction.
Both nonextension assertions follow.''',r'''The contradiction occurs on a noncentral compact smooth torus
fibre of the recovered marked map.  The proper reductions and
modifications preserve the prescribed open family.  Thus the
argument applies to every extension in
\cref{def:V:analytic-boundary-extension}, proving both assertions.''','Consolidate the repeated central-fibre scope disclaimer into the precise already-numbered definition. All geometric scope is preserved: the contradiction is on the noncentral locus, and the allowed central singularities/multiplicities/components remain those of Definition9.1.')
for r in rows:
 assert r['old']!=r['new']
 # Review guards sequentially against a temporary in-memory string, never the source.
 assert s.count(r['old'])==1
 s=s.replace(r['old'],r['new'],1)
out=b/'work/agents/v_analytic/S6_SERIES_PUBLISH_V_final_reading_analytic_guards.json'
out.write_text(json.dumps({'candidate':'V_candidate_01','source_sha256_at_guard_creation':hashlib.sha256(p.read_bytes()).hexdigest(),'pdf_sha256':'8b2d18bb43fedda842510e01967074589e0439c491fa3bb53928ab1d7eeedc2d','scope':'Rendered-page findings; edits are proposed only. No source file modified and no mathematical CHECK_EVENTS added.','edits':rows},indent=2,ensure_ascii=False)+'\n')
print(len(rows),'unique nonoverlapping guarded edits across',len({r['finding_id'] for r in rows}),'findings');print(out)
