"""Install the frozen-before-target arguments; preserve complete former blocks."""
from pathlib import Path
import datetime, hashlib, json, re

P = Path(__file__).resolve().parents[2]
A = P / 'analysis/continuation_root'
targets = {
 'maps:src:F.2.6': 'F2_6_integral_cellular_proof.tex',
 'mapsaudit:order-four-torsion-transgression': 'order_four_transgression_cellular_proof.tex',
}
frozen = json.loads((A/'F2_6_prereading_frozen_receipt.json').read_text())
for item in frozen['files']:
    data = (P/item['path']).read_bytes()
    assert len(data) == item['size']
    assert hashlib.sha256(data).hexdigest() == item['sha256'], item['path']

def digest(s):
    return hashlib.sha256(s.encode()).hexdigest()

def block(text, label):
    key = r'\label{'+label+'}'
    assert text.count(key) == 1, label
    at = text.index(key)
    begins = list(re.finditer(r'\\begin\{(?:theorem|lemma)\}', text[:at]))
    start = begins[-1].start()
    ps = text.index(r'\begin{proof}', at)
    pe = text.index(r'\end{proof}', ps) + len(r'\end{proof}')
    return start, pe, ps, text[start:pe]

def record_args(s):
    i = s.index(r'\StatementRecord') + len(r'\StatementRecord')
    spans=[]
    for _ in range(4):
        while s[i].isspace(): i+=1
        assert s[i]=='{'
        a=i+1; depth=1; i+=1
        while depth:
            if s[i]=='{' and s[i-1]!='\\': depth+=1
            if s[i]=='}' and s[i-1]!='\\': depth-=1
            i+=1
        spans.append((a,i-1))
    return spans

uses = {
 'maps:src:F.2.6': r'\cref{maps:src:F.2.5}; \cref{night:P1.11}; \cref{night:P1.1}; \cref{maps:src:F.2.1}; \cref{maps:eq:F.5}; the displayed integral cellular maps; \cite[Theorem 3.2, p.~195; Corollary 3.3, p.~196; Theorem 3.30, p.~241; Theorem 4.32, p.~366]{Hatcher2002}',
 'mapsaudit:order-four-torsion-transgression': r'\cref{maps:src:F.2.5}; the integral quotient and explicit certificates in \cref{maps:src:F.2.6}; \cref{maps:eq:F.6}; the displayed cellular and boundary maps',
}
scope = r' \emph{Continuation current-proof scope.} The current proof is the argument written independently before the target was opened on 19 November 2026. Exact cellular maps and integral certificates are printed here; fresh FLINT programs reproduce them. The complete former proof is preserved with its separate review scope.'
receipt = {'installed_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'frozen_derivation_sha256':'bf6aa26f553abbbd61441cd3614f87b55c161a601f7da7b91eafc4a5f6c646b3',
 'prereading_receipt':'analysis/continuation_root/F2_6_prereading_frozen_receipt.json',
 'reason':'Install the complete preread cellular derivation. The former F2.6 pairing and suspension-period routes retain their prior scope and are not credited retrospectively. The audit lemma now states explicitly that its nonzero-image conclusion concerns the unique nonzero local torsion class; w=0 maps to0 by the displayed homomorphism.',
 'dependency_change':'P1.11 is explicit in F2.6. F2.6 proves its differential directly; the separate audit lemma cites the integral quotient calculation of F2.6. This keeps these two dependencies acyclic.',
 'files':[]}

for filename in ['body_source.tex','body.tex']:
    path=P/'papers/V'/filename
    text=path.read_text(); original=text
    changes=[]
    for label, revision in targets.items():
        start,end,ps,old=block(text,label)
        oldname=('F2_6' if label=='maps:src:F.2.6' else 'order_four_transgression')+'_'+filename.replace('.tex','')+'_before_cellular_replacement.tex'
        backup=A/oldname
        if backup.exists(): raise RuntimeError('Preserved file already exists: '+str(backup))
        backup.write_text(old+'\n')
        proof=(P/'papers/V/revisions'/revision).read_text().strip()
        new=old[:ps-start]+proof
        spans=record_args(new)
        a,b=spans[3];new=new[:a]+uses[label]+new[b:]
        a,b=record_args(new)[2];new=new[:b]+scope+new[b:]
        if label=='mapsaudit:order-four-torsion-transgression':
            before='For each of $q=2,3,4$, that image is\nthe nonzero class in the global $\\mathbb Z/2$ quotient.'
            after='For each of $q=2,3,4$, the unique nonzero local torsion class maps\nto the nonzero class in the global $\\mathbb Z/2$ quotient.'
            assert before in new
            new=new.replace(before,after,1)
        text=text[:start]+new+text[end:]
        changes.append({'label':label,'preserved':str(backup.relative_to(P)),
                        'old_block_sha256':digest(old),'current_block_sha256':digest(new),
                        'revision':str((Path('papers/V/revisions')/revision)),
                        'current_proof_sha256':digest(proof)})
    assert path.read_text()==original, 'Concurrent edit detected; retry against the current file.'
    path.write_text(text)
    receipt['files'].append({'path':str(path.relative_to(P)),'before_sha256':digest(original),'after_sha256':digest(text),'changes':changes})

for label, revision in targets.items():
    expected=(P/'papers/V/revisions'/revision).read_text().strip()
    for filename in ['body_source.tex','body.tex']:
        s=(P/'papers/V'/filename).read_text()
        start,end,ps,_=block(s,label)
        assert s[ps:end]==expected
receipt['active_proofs_exactly_match_revisions']=True
(A/'F2_6_replacement_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({'installed':list(targets),'proof_hashes':{k:digest((P/'papers/V/revisions'/v).read_text().strip()) for k,v in targets.items()},'frozen_files_unchanged':True},indent=2))
