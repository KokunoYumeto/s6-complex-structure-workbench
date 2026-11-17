from pathlib import Path
import re,json,csv,hashlib
root=Path('/workspace/scratch/037cd144174c')
out=root/'deliverables/work/invariants_arithmetic'
files=['hodge_frolicher.tex','bott_chern_algebra.tex','analytic_picard.tex']
mp={
'prop:workbench-holomorphic-form-vanishing':('INV A3.1','Independent direct period proof; preserve.'),
 'thm:parametric-hodge-diamond':('INV A3.1; INV C1.1','Earlier parameterized statement retained as derivation; exact value supplied by INV.'),
 'thm:frolicher-e2-candidate':('INV C1.1','Compare full proof; spectral-degree argument expected duplicate.'),
 'prop:period-derivative-determinant':('INV A2.1','Global degree and elliptic local orders proof; preserve beside modular formula.'),
 'prop:log-relative-direct-images':('INV A1.2','Tensor-lattice filtration differs from INV upper-modification/duality proof; preserve.'),
 'prop:log-ks-divisor':('INV A2.1','Coarse divisor proof with invariant lattices; preserve if not identical.'),
 'prop:absolute-cotangent-direct-images':('INV A1.3','Residue proof, compare boundary ranks and extension splitting.'),
 'thm:h12-scalar':('INV A2.4','Scalar evaluation proof, compare branch and sign.'),
 'cor:exact-hodge-diamond':('INV A3.1','Duplicate exact statement.'),
 'thm:exact-bott-chern-aeppli':('INV C2.1; INV C2.2','McHugh formula proof is independent of dots/arrows proof; preserve.'),
 'record:h12-direct-images':('INV A1.2; INV A1.3; INV A2.4','Historical audit record; absence of human replication is not a premise gap.'),
 'lem:bcpr-degree-one-input':('INV C3.1; INV C3.2','Detailed Picard normalization and representative proof.'),
 'lem:bcpr-eta-extension':('INV A3.2','Detailed finite/cusp gluing and edge-map proof; preserve if longer.'),
 'rem:bcpr-literal-gauge':('INV C3.8','Operator existence versus unevaluated coefficient atlas; exact open boundary.'),
 'prop:bcpr-generators-are-bases':('INV C1.2; INV C3.3','Detailed representative independence and Serre pairing proof.'),
 'thm:bcpr-square-zero-algebra':('INV C3.3','Same square-zero mechanism with expanded bidegree proof; retain once.'),
 'rem:bcpr-global-gauge-boundary':('INV C3.8','Same open literal coefficient-atlas target.'),
 'lem:hodge-line-audit':('INV A1.0','Independent canonical-form/character proof of Hodge line; preserve.'),
 'lem:finite-normal-order-audit':('INV B2.1; FAM finite filling','Exact-order normal character lemma is a separate useful dependency.'),
 'lem:cusp-structure-sheaf-audit':('INV A1.0; INV D1.2','Expanded normalization and intrinsic nearby-cycle proof; preserve.'),
 'thm:structure-direct-images-audit':('INV A1.0','Expanded finite scheme-fibre and cusp base-change proof; preserve.'),
 'cor:picard-line-audit':('INV C3.1','Picard isomorphism and fibrewise injectivity; print as dependency.'),
 'thm:uniform-nontorsion-audit':('INV D4.2; CDP uniform non-torsion','Independent countability proof; Paper II dependency with Paper I cross-reference.'),
}
rows=[]
for f in files:
    p=root/'sources/workbench'/f;s=p.read_text(); pat=r'\\begin\{(lemma|theorem|proposition|corollary|remark|auditrecord)\}(?:\[([^\]]*)\])?'
    for n,m in enumerate(re.finditer(pat,s),1):
        kind,title=m.group(1),m.group(2) or ''
        e=s.find('\\end{'+kind+'}',m.end())+len('\\end{'+kind+'}')
        if e<len('\\end{'+kind+'}'):raise Exception(f)
        st=s[m.start():e]; labs=re.findall(r'\\label\{([^}]+)\}',st); sid=labs[0] if labs else f'{f[:-4]}:{kind}:{n}'
        eproof=e;post=s[e:]; pm=re.match(r'\s*\\begin\{proof\}(?:\[[^\]]*\])?',post)
        if pm:
            pe=s.find('\\end{proof}',e+pm.end())
            if pe<0:raise Exception(sid)
            eproof=pe+len('\\end{proof}')
        block=s[m.start():eproof];slug=re.sub('[^A-Za-z0-9_-]','_',sid)
        ep=out/'extracted'/('WB_'+slug+'.tex');ep.write_text(block+'\n')
        takeover,note=mp.get(sid,('','Historical explanatory remark; compare against successor text.'))
        row={'source_run':'WORKING_INV','source_id':sid,'source_file':'workbench/'+f,'source_line_start':s.count('\n',0,m.start())+1,'source_line_end':s.count('\n',0,eproof)+1,'kind':kind,'title':title,'paper':'II' if sid=='thm:uniform-nontorsion-audit' else 'I','printed_label':'inv:wb:'+sid,'source_statement':st,'extracted_file':str(ep.relative_to(root/'deliverables')),'source_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'taken_over_by':takeover,'distinct_proof':note,'recorded_checks':'Pending evidence locator mapping; source status labels are not counted as checks.','own_check':'Pending full candidate-to-printed comparison.','check_outcome':'pending','notes':note}
        rows.append(row)
    if f=='bott_chern_algebra.tex':
        for sid,a,b,target in [('formula:bcpr-fibre-representatives',79,194,'INV A3.2; INV C3.7'),('formula:bcpr-factor-twelve-chern',371,487,'INV C3.1; INV C3.2')]:
            block='\n'.join(s.splitlines()[a-1:b]);ep=out/'extracted'/('WB_'+sid.replace(':','_')+'.tex');ep.write_text(block+'\n')
            rows.append({'source_run':'WORKING_INV','source_id':sid,'source_file':'workbench/'+f,'source_line_start':a,'source_line_end':b,'kind':'numbered_formula_block','title':sid.split(':')[-1],'paper':'I','printed_label':'inv:wb:'+sid,'source_statement':block,'extracted_file':str(ep.relative_to(root/'deliverables')),'source_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'taken_over_by':target,'distinct_proof':'Expanded explicit formulas; incorporate with full derivation.','recorded_checks':'Pending locator mapping.','own_check':'First fibre formula block read; full source-to-candidate comparison pending.','check_outcome':'pending','notes':'Equations comprise a standalone result not enclosed in a theorem environment.'})
(out/'working_edition_inventory.json').write_text(json.dumps(rows,indent=2)+'\n')
with (out/'working_edition_inventory.csv').open('w') as h:
 w=csv.DictWriter(h,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
print(len(rows),'working-edition rows, including duplicate takeover mappings and two theorem-free numbered formula blocks')
