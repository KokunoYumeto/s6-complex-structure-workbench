#!/usr/bin/env python3
"""Prepare exact editorial proposals for nine actually compared owning blocks.

This writes proposals only. It does not edit canonical source, approve a guard,
claim a rereading, or add a check event.
"""
from pathlib import Path
import datetime,hashlib,json,re
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'agents/ii_checks_A/editorial/group01'
OUT.mkdir(parents=True,exist_ok=True)
def sha(b):return hashlib.sha256(b).hexdigest()
releases=[]
for name in ('initial','second'):
    releases+=json.loads((ROOT/f'agents/ii_checks_A/S6_SERIES_PUBLISH_II_A_{name}_releases.json').read_text())
releases.append({'receipt':'agents/ii_infra/released_proofs/01FW/86275670ca93258f/S6_SERIES_PUBLISH_release_receipt.json','full_block':'agents/ii_infra/released_proofs/01FW/86275670ca93258f/S6_SERIES_PUBLISH_full_owning_block.tex'})
bytag={Path(r['full_block']).parts[-3]:r for r in releases}
titles={
'01G0':'Components of exceptional fibres',
'01G5':'Real cohomology and the structure sheaf',
'01G6':'Injectivity of integral generization',
'01G7':'Line bundles of infinite order on every fibre',
'01FV':'Invariant classes in the restriction image',
'01G2':'Restriction maps and splitting degrees',
'01FX':'Cup products and cohomological flatness',
'01FZ':'Constant integral monodromy and coherent splitting',
'01FW':'Generic line bundles on every fibre'}
old_enum=r'\begin{enumerate}[label={$\langle1\rangle$\arabic*.},leftmargin=*]'
manifest=[]
for tag in titles:
    release=bytag[tag];old=(ROOT/release['full_block']).read_text();new=old;edits=[]
    def replace(a,b,types,identity):
        global new
        count=new.count(a)
        assert count==1,(tag,a,count)
        new=new.replace(a,b,1)
        edits.append({'defect_types':types,'old':a,'new':b,'occurrences':1,'mathematical_reference_identity':identity})
    owner=re.search(r'\\label\{([^}]+)\}',old).group(1)
    header=re.search(r'\\begin\{proposition\}(?:\[[^\]]*\])?',new).group(0)
    replace(header,r'\begin{proposition}['+titles[tag]+']',['D16']+(['D08'] if tag=='01FZ' else []),'Only the optional mathematical title changes; owner, hypotheses, conclusion, label and hypertarget remain exact.')
    if tag in ('01G5','01G2'):
        start=old_enum+'\n\\item \n\\noindent\\textbf{Step 1.} '
        replace(start,'',['D10'],'Remove the one-item list wrapper and duplicate Step1 marker; the single proof body retains its order.')
        replace('\n\\end{enumerate}\n','\n',['D10'],'Close the removed one-item wrapper; no proof sentence is removed.')
    else:
        replace(old_enum,r'\begin{enumerate}[leftmargin=*]',['D10'],'Remove the inherited angle-bracket iteration marker while retaining the ordered proof steps.')
    for m in list(re.finditer(r'\\\[((?:(?!\\\[).)*?\\tag\{[^}]+\}(?:(?!\\\[).)*?)\\\]',new,re.S)):
        a=m.group(0);body=re.sub(r'\\tag\{[^}]+\}','',m.group(1));b='\\begin{equation}'+body+'\\end{equation}'
        replace(a,b,['D19'],'Equation body, label, hypertarget and every reference target remain identical; the equation counter now supplies its section number instead of an inherited D-number.')
    if tag=='01G0':
        replace('The last assertion concerns the indicated quotient of $H_1(F;\\Z)$;\nit does not assert that $H_1(F;\\Z)$ itself is torsion-free.',
                'The freeness assertion concerns the displayed coinvariant quotient of\n$H_1(F;\\Z)$.',['D02','D11'],'The same quotient is the sole subject of the freeness conclusion; no property of the source group is added.')
        paragraph='The rational component-count formula is the correction in \\citet[Section~10.5, p.~91]{AC2026}. The integral torsion-free conclusion under the displayed integral hypotheses is an additional clause; its full argument is included here.'
        replace(paragraph,'',['D13','D08'],'Move the accurate primary credit into the owning proof; the formula and the integral assertion remain in the statement.')
        replace('\\begin{proof}\n','\\begin{proof}\nThe rational component formula is due to \\citet[Section~10.5, p.~91]{AC2026}.\n',['D13'],'The exact same primary source and locator supply the rational formula credit in the proof.')
        replace('Proposition \\CompendiumRef{II}{cdp:st:D.1.1} therefore gives',
                '\\citet[Lemma~10.7, p.~90]{AC2026} therefore gives',['D06','D18'],'The opened primary lemma gives G^ab ≅ Q^ab ⊕ (K^ab)_Q via [(k,q)]↦([q],[k]); this is exactly the supplemental compendium D.1.1 statement. No current label is invented.')
    if tag=='01G5':
        replace('real \\v Cech cocycle','real \\v{C}ech cocycle',['D23'],'Only the TeX accent grouping changes.')
    if tag=='01G7':
        replace('No local-freeness assumption on $R^1f_*\\OO_Y$ or constant-dimension\nassumption on fibre cohomology is required.','',['D02','D11'],'The displayed theorem hypotheses already specify the exact scope. No assumption is inserted; the proof continues to use the natural base-change map.')
        replace('Choose $\\gamma$ mapped to $d$. By Lemma \\ref{cdp:st:D.1.8},\neach $\\gamma_c\\in H^1(f^{-1}(c);\\Z)$ is nonzero.',
                'Choose $\\gamma$ mapped to $d$. The local meridian argument in\nthe proof of Proposition~\\ref{cdp:st:D.1.8} applies in every complex\ndimension: the local equation is $t=z^m u$ with $u$ a unit and $m>0$,\nand evaluation on a positive normal circle gives $km=0$, hence $k=0$.\nThus each $\\gamma_c\\in H^1(f^{-1}(c);\\Z)$ is nonzero.',
                ['D25','D23'],'The target has arbitrary manifold dimension, while the cited statement is worded for threefolds. The inserted positive-normal-circle computation is the exact dimension-independent proof from the frozen01G6 derivation and released proof; it establishes the needed extension before use.')
        replace('Lemma \\ref{cdp:st:D.1.7} implies','Proposition~\\ref{cdp:st:D.1.7} implies',['D23'],'Owner cdp:st:D.1.7 is a proposition; reference identity is unchanged.')
        replace('This uses the natural\ncoherent base-change homomorphism, but does not require it to be\nan isomorphism.','This is the image under the natural coherent base-change\nhomomorphism.',['D02'],'The same natural homomorphism supplies the equality. The new text makes no isomorphism claim and introduces no new hypothesis.')
    if tag=='01FV':
        replace('Surjectivity of\nthe full restriction map need not have its image generated only by\nthis lattice, so that last equivalence describes the stated argument.',
                'This characterization concerns the subspace generated by the\nindicated invariant lattice in the restriction image.',
                ['D02','D11'],'The containment and the lattice-spanning equivalence remain exact; the sentence positively specifies which subspace is characterized.')
        replace('Lemma \\ref{cdp:st:D.1.7} makes','Proposition~\\ref{cdp:st:D.1.7} makes',['D23'],'Correct the statement kind without changing the referenced coefficient-injection theorem.')
    if tag=='01G2':
        replace('the asserted identification of the actual maps.','the asserted identification of the maps.',['D08'],'The three displayed morphisms and their equality are unchanged.')
    if tag=='01FX':
        para='The torus-fibred six-sphere case and the cup-product index method are \\citet[Theorem~2.3, pp.~5--6]{Viaclovsky2026Combs}. The statement here has the displayed broader hypotheses: $b_2=0$, an arbitrary base curve, and also primary Kodaira general fibres. The complete proof specifies the additional integral comparison for those hypotheses.'
        replace(para,'',['D13','D08'],'Move the precise primary credit into the proof; the displayed broad hypotheses and all arguments remain.')
        replace('\\begin{proof}\n','\\begin{proof}\nThe cup-product index argument for torus-fibred six-spheres is due to\n\\citet[Theorem~2.3, pp.~5--6]{Viaclovsky2026Combs}. We apply it under\nthe displayed hypotheses and verify the cup product for primary Kodaira fibres.\n',['D13'],'The primary source proves its six-sphere/torus case; the following unchanged degree calculation and Kodaira coframe argument establish this statement at its own scope.')
    if tag=='01FZ':
        replace('Both\nexamples have $b_1=4$; this comparison does not assert a new\ncounterexample under $b_1=b_2=0$.','Both\nexamples have $b_1=4$.',['D11','D02'],'Both examples retain the explicit Betti number4. Their construction and hypotheses therefore retain exactly their stated scope.')
        replace('The polynomial identity is\nalso checked in the attached exact program.',
                'More explicitly, with\n\\[\nJ=\\begin{pmatrix}0&1&0&0\\\\-1&0&0&0\\\\0&0&0&1\\\\0&0&-1&0\\end{pmatrix},\n\\qquad S=\\begin{pmatrix}0&1\\\\1&0\\end{pmatrix},\n\\]\none has $B=SPJ$ and $PJP^t=0$, so $BP^t=0$.',
                ['D09'],'The frozen independent quotient was PJ; the target quotient B is obtained by the explicit constant invertible row map S with det(S)=−1. Fresh exact code verified B−SPJ=0 and BP^t=0. This replaces file bookkeeping by the actual identity.')
    if tag=='01FW':
        replace('In particular the general-line-bundle conclusion of CDP20\nProposition 5.6 holds with this precise quantifier, without the\nnonnegative-summand assertion of Proposition 5.5.',
                'This gives the general-line-bundle conclusion of\n\\citet[Proposition~5.6]{CDP2020} under the displayed hypotheses.',
                ['D02','D18'],'The mathematical quantifier and hypotheses have just been stated in full and remain. The source Proposition5.6 was opened in its Section5 context.')
        replace('Lemma'+r's \ref{cdp:st:D.1.7} and \ref{cdp:st:D.1.8} prove nonvanishing.',
                'Proposition~\\ref{cdp:st:D.1.7} and the dimension-independent local\nmeridian argument in the proof of Proposition~\\ref{cdp:st:D.1.8}\nprove nonvanishing.',
                ['D23','D25'],'Both referenced owners are propositions. For the broader-dimensional hypothesis, the same t=z^m u normal-disc computation is transported explicitly, as spelled out in the01G7 replacement.')
    original=OUT/f'S6_SERIES_PUBLISH_II_A_{tag}_original_block.tex'
    proposed=OUT/f'S6_SERIES_PUBLISH_II_A_{tag}_proposed_block.tex'
    assert not original.exists() and not proposed.exists()
    original.write_text(old);proposed.write_text(new)
    labels_old=re.findall(r'\\(?:label|hypertarget)\{([^}]+)\}',old)
    labels_new=re.findall(r'\\(?:label|hypertarget)\{([^}]+)\}',new)
    assert labels_old==labels_new,(tag,labels_old,labels_new)
    manifest.append({'tag':tag,'statement_owner':owner,'release_receipt':release['receipt'],
      'original_block_path':str(original.relative_to(ROOT)),'original_block_sha256':sha(original.read_bytes()),
      'proposed_block_path':str(proposed.relative_to(ROOT)),'proposed_block_sha256':sha(proposed.read_bytes()),
      'literal_edits':edits,'labels_and_hypertargets_identical':True,
      'D10_statement_header_disposition':'Canonical StatementRecord is already tag-only by root-owned preamble definition; its nonprinting metadata arguments remain exact.',
      'E4_reference_disposition':'Every remaining CompendiumRef{II}{cdp:st:E4} is separately transported by S6_SERIES_PUBLISH_II_E4_locator_transport_v2.json; root owns that complete citation integration.',
      'actual_comparative_rereading_record':None,'approved':False})
dest=OUT/'S6_SERIES_PUBLISH_II_A_group01_editorial_proposals.json'
assert not dest.exists();dest.write_text(json.dumps({'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'checker':'ii_check_a','proposals':manifest,'canonical_source_changed':False,'events_added':0},indent=2)+'\n')
print(json.dumps({'manifest':str(dest.relative_to(ROOT)),'sha256':sha(dest.read_bytes()),'owners':len(manifest),'literal_edits':sum(len(x['literal_edits']) for x in manifest),'approved':False}))
