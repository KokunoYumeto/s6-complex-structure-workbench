from pathlib import Path
import csv
import datetime
import hashlib
import json
import re

ROOT = Path('/workspace/scratch/653608133b22')
OUT = ROOT / 'work/agents/i_analytic'
LIT = OUT / 'literature'
source = ROOT / 'work/S6_SERIES_PUBLISH_I.tex'
original = ROOT / 'source/S6_SERIES_GRIND_I.tex'
current_text = source.read_text()
original_text = original.read_text()
now = datetime.datetime.now(datetime.timezone.utc).isoformat()

def sha(data):
    if isinstance(data, str):
        data = data.encode()
    return hashlib.sha256(data).hexdigest()

def block(text, label):
    pos = text.index(r'\label{' + label + '}')
    start = text.rfind(r'\begin{proposition}', 0, pos)
    end = text.index(r'\end{proof}', pos) + len(r'\end{proof}')
    return text[start:end]

old = r'''The hypotheses are satisfied separately by the positive derivative
and exact sign in each of the nine rows.  Explicitly, the auxiliary
imaginary quadratic field $K$ in the proof of Gross--Zagier I.7.3
\citep[Chapter~V, \S2, preprint p.~129]{CrGrossZagier1986} has split Heegner primes and $L(E_i^D,1)\ne0$; hence
$L'(E_i/K,1)=L'(E_i,1)L(E_i^D,1)\ne0$.  Its Heegner point has
positive height, so Gross's Theorem~1.3 gives finite
$\operatorname{Sha}(E_i/K)$.  The restriction map'''
new = r'''For each of the nine rows, the associated weight-two newform has
sign $-1$ by \cref{ari:C.6.R2}. Apply the nonvanishing theorem
\citep[Introduction, Theorem~(ii), pp.~543--544]{BumpFriedbergHoffstein1990}
with $S=\{2\}\cup\{p:p\mid N_i\}$, where $N_i$ is the conductor.
It gives a negative fundamental discriminant $D$ such that every
prime in $S$ splits in $K=\Q(\sqrt D)$ and $L(E_i^D,1)\ne0$.
Since $2$ splits, $D\equiv1\pmod8$, so $D\ne-3,-4$ and
$\mathcal O_K^\times=\{\pm1\}$, as required in Gross's setup.
The Gross--Zagier formula
\citep[Chapter~V, Theorem~2.1, preprint p.~127; proof of I.7.3, p.~129]{CrGrossZagier1986}
then gives a nonzero height for the Heegner trace, because
$L'(E_i/K,1)=L'(E_i,1)L(E_i^D,1)\ne0$.
Thus Gross's Theorem~1.3 gives finite $\operatorname{Sha}(E_i/K)$.
The restriction map'''

record_old = r'''\StatementRecord{ari:C.6.R3}{proved}{0012}{\citep[Chapter~I, Theorem~7.3, preprint p.~12]{CrGrossZagier1986}; \citet[Theorem~1.3, pp.~235--236]{CrGross1991}; \citet[Theorem~1.1, p.~2 of arXiv v1]{CrJetchev2008}}'''
record_new = record_old[:-1] + r'''; \citet[Introduction, Theorem~(ii), pp.~543--544]{BumpFriedbergHoffstein1990}}'''

bib_anchor = r'''\bibitem[Cai et~al.(2014)Cai, Shu, and Tian]{CgzCai2014}'''
bib = r'''\bibitem[Bump et~al.(1990)Bump, Friedberg, and Hoffstein]{BumpFriedbergHoffstein1990}
Daniel Bump, Solomon Friedberg, and Jeffrey Hoffstein.

\newblock Nonvanishing theorems for {$L$}-functions of modular forms and their derivatives.

\newblock \emph{Inventiones Mathematicae}, 102:\penalty0 543--618, 1990.

\newblock URL \url{https://wstein.org/papers/bib/bump-friedberg-hoffstein-nonvanishing.pdf}.

'''

guards = [
    {'id':'IA-GROSS-AUX-01','old':old,'new':new,'expected_count':1,
     'reason':'Supply an admissible nonvanishing auxiliary field for Gross Theorem1.3: prescribed splitting at2 excludes discriminants -3,-4.'},
    {'id':'IA-GROSS-AUX-02','old':record_old,'new':record_new,'expected_count':1,
     'reason':'Record the operative nonvanishing input in the statement dependency record; the printed permanent tag is unchanged.'},
    {'id':'IA-GROSS-AUX-03','old':bib_anchor,'new':bib+bib_anchor,'expected_count':1,
     'reason':'Add the primary theorem used to make the auxiliary-field choice; title, authors, volume and page range read on its primary first page.'},
]
preview = current_text
for g in guards:
    assert preview.count(g['old']) == g['expected_count'], (g['id'],preview.count(g['old']))
    preview = preview.replace(g['old'],g['new'],g['expected_count'])

original_block = block(original_text,'ari:C.6.R3')
current_block = block(current_text,'ari:C.6.R3')
new_block = block(preview,'ari:C.6.R3')
assert current_block.split(r'\end{proposition}')[0].split('\n',2)[2].replace(record_old,record_new) == new_block.split(r'\end{proposition}')[0].split('\n',2)[2]
assert re.findall(r'\\label\{[^}]+\}|\\hypertarget\{[^}]+\}',current_block) == re.findall(r'\\label\{[^}]+\}|\\hypertarget\{[^}]+\}',new_block)

payload = {'source':str(source),'source_base_sha256':sha(current_text),
           'created_utc':now,'guards':guards,
           'mathematical_scope':'Only ari:C.6.R3 proof Step2 auxiliary-field selection. Statement unchanged; all labels/tags preserved; ari:C.6.R5 untouched.'}
(OUT/'S6_SERIES_PUBLISH_I_Gross_auxiliary_guards.json').write_text(json.dumps(payload,indent=2)+'\n')
(OUT/'S6_SERIES_PUBLISH_I_Gross_auxiliary_replacement.tex').write_text(new_block+'\n')
(OUT/'S6_SERIES_PUBLISH_I_Gross_auxiliary_archive.json').write_text(json.dumps({
    'original_source':str(original),'original_sha256':sha(original_text),
    'current_source':str(source),'current_sha256':sha(current_text),
    'original_complete_result':original_block,
    'current_complete_result':current_block,
    'replacement_complete_result':new_block,
    'guarded_old_span':old,'guarded_new_span':new,
    'created_utc':now,'exposure':'Complete receiving proof was already exposed in earlier editing. The present complete original/current/replacement comparison is a reread and application-hypothesis check, not an independent derivation.',
},indent=2)+'\n')

images = [
 ('Gross1991',ROOT/'work/agents/i_marking/literature/S6_SERIES_PUBLISH_I_Gross1991_p001.png','printed235, complete setup/definition/formula'),
 ('Gross1991',ROOT/'work/agents/i_marking/literature/S6_SERIES_PUBLISH_I_Gross1991_p002.png','printed236-237, complete Theorem1.3 and subsequent proof-sketch restriction'),
 ('GrossZagier1985preprint',ROOT/'work/agents/i_marking/literature/S6_SERIES_PUBLISH_I_GrossZagier1985preprint_p008.png','printed11-12, height/period setup and TheoremI.7.3'),
 ('GrossZagier1985preprint',ROOT/'work/agents/i_marking/literature/S6_SERIES_PUBLISH_I_GrossZagier1985preprint_p065.png','printed125-126, Waldspurger existence assertion and definition of Heegner trace'),
 ('GrossZagier1985preprint',LIT/'S6_SERIES_PUBLISH_I_GZ127128.png','printed127-128, TheoremV.2.1 and rational-period normalization'),
 ('GrossZagier1985preprint',ROOT/'work/agents/i_marking/literature/S6_SERIES_PUBLISH_I_GrossZagier1985preprint_p067.png','printed129-130, proof of I.7.3 and following abelian-variety application'),
 ('BFH1990',LIT/'S6_SERIES_PUBLISH_I_BFH1990-02.png','printed543, introduction setup and unnumbered theorem assumptions'),
 ('BFH1990',LIT/'S6_SERIES_PUBLISH_I_BFH1990-03.png','printed544, unnumbered theorem(i),(ii) and surrounding explanation'),
]
receipt = {
 'created_utc':now,'scope':'Actual explicit image views of the named pages; no whole-source-proof reading claimed.',
 'sources':[
  {'id':'Gross1991','pdf':str(ROOT/'work/agents/i_marking/literature/S6_SERIES_PUBLISH_I_Gross1991_primary.pdf'),'url':'https://wstein.org/papers/bib/gross-kolyvagins_work_on_modular_elliptic_curves.pdf','locator':'Theorem1.3 printed236; setup235; proof-sketch restriction237','read_outcome':'The theorem assumes the Heegner trace has infinite order. Its setup excludes discriminants -3,-4; the non-CM restriction begins only in the later illustrative proof.'},
  {'id':'GrossZagier1985preprint','pdf':str(ROOT/'work/agents/i_marking/literature/S6_SERIES_PUBLISH_I_GrossZagier1985preprint_primary.pdf'),'url':'https://archive.mpim-bonn.mpg.de/id/eprint/3578/1/preprint_1985_30.pdf','locator':'I.7.3 printed12; V.1 printed125; V.2 printed126-129','read_outcome':'Gives the rational-point factor and Heegner trace/height formula. The printed nonvanishing choice does not itself expressly impose the two-discriminant exclusion.'},
  {'id':'BFH1990','pdf':str(LIT/'S6_SERIES_PUBLISH_I_BumpFriedbergHoffstein1990.pdf'),'url':'https://wstein.org/papers/bib/bump-friedberg-hoffstein-nonvanishing.pdf','locator':'Introduction, unnumbered Theorem(ii), printed543-544; PDF2-3','read_outcome':'For any finite S containing conductor primes, supplies a fundamental D with epsilon D>0, every prime in S split, and nonzero central twisted value. Apply k=2, epsilon=-1, and add2 to S.'},
 ],
 'images':[{'source':ident,'path':str(p),'sha256':sha(p.read_bytes()),'actual_read_scope':scope} for ident,p,scope in images],
 'application':{'S':'{2} union {p : p divides N_i}','weight':2,'epsilon':-1,'D':'negative fundamental discriminant','local_argument':'Splitting at2 implies D is odd. For odd fundamental D, O_K=Z[(1+sqrt(D))/2], whose defining polynomial is X^2-X+(1-D)/4. Splitting modulo2 requires (1-D)/4 even, hence D=1 mod8. Thus D is neither -3 nor -4 and O_K units are ±1.','twist_map':'The twist E_i^D is the curve obtained from D y^2=x^3+A x+B after a rational Weierstrass change; over K, (x,y) maps to (x,sqrt(D)y) on E_i. This is the character twist occurring in BFH and the factorization L(E_i/K,s)=L(E_i,s)L(E_i^D,s).','Heegner_trace_map':'With the same modular parametrization phi:X_0(N_i)->E_i sending infinity to O, P_K=Tr_{H/K}(phi(x)) in GZ V.2 is Gross y_K=Tr_{K_1/K}(phi(x_1)); H=K_1 is the Hilbert class field. The ideal chosen above N_i changes this trace only up to sign and torsion, preserving nonzero height.'},
 'limits':['The existence statement is used exactly; no infinitude assertion is needed or inferred.','No rereading of the complete BFH proof or Gross proof is claimed.','The explicit D=-3 entries in ari:C.6.R5 are unchanged; the new auxiliary choice belongs only to the finiteness argument in ari:C.6.R3.','The initial tool attempt that returned truncated output did not count as a page read; the later singly emitted images did.'],
}
for item in receipt['sources']:
    p=Path(item['pdf']);item['sha256']=sha(p.read_bytes())
(LIT/'S6_SERIES_PUBLISH_I_Gross_BFH_auxiliary_scope_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')

group='eg:publish-ianalytic-gross-auxiliary-7270766c405d61cb'
event='ce:publish-ianalytic-gross-auxiliary-3e9335e6ab489843'
fields=['statement_id','date','who','type','outcome','event_id','phase','source_file','source_row','source_event_type','evidence_group']
row={'statement_id':'ari:C.6.R3','date':'2026-11-21','who':'GPT-6 Astra (OpenAI), ChatGPT Pro mode, inherited effort, S6_SERIES_PUBLISH/v_analytic_check','type':'used and rechecked in this run','outcome':'PASS AFTER SUPPLIED PROOF REPAIR; EXPOSED REREAD ONLY. Complete original/current/replacement comparison of rational-factor and Sha-finiteness proof. Gross setup excludes discriminants -3,-4; BFH Introduction Theorem(ii), pp543-544 with S including2 yields negative fundamental D=1 mod8 and nonzero twist, so all Gross hypotheses hold. Exact Heegner-trace/twist maps and restriction-inflation descent checked. Statement and all labels/tags unchanged; R5 D=-3 computations untouched. No independent, targeted, computational, or statement-refuted credit.','event_id':event,'phase':'S6_SERIES_PUBLISH','source_file':str(OUT/'S6_SERIES_PUBLISH_I_Gross_auxiliary_comparison.md'),'source_row':'','source_event_type':'used and rechecked in this run','evidence_group':group}
with (OUT/'S6_SERIES_PUBLISH_I_Gross_auxiliary_CHECK_EVENTS.tsv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerow(row)

print(json.dumps({'source_sha256':sha(current_text),'guards':len(guards),'event_group':group,'event_count':1,'statement_modified':False,'root_source_modified':False},indent=2))
