#!/usr/bin/env python3
"""Exact scoped P15 extensions, with reversible mathematical symbol maps.

Only owned proposal rows are written. The source, shared defects/events, unit
statuses and derived publication records are left for root admission.
"""
from __future__ import annotations
from collections import Counter
import csv
from datetime import datetime, timezone
import json
from pathlib import Path
import re
from S6_SERIES_PUBLISH_c8_III_check_counts import parse_statements

ROOT=Path(__file__).resolve().parents[1]
OWN=ROOT/'agents/continuation9_global_sweep'
SOURCE=(ROOT/'S6_SERIES_PUBLISH_III.tex').read_text(encoding='utf-8')
OWNERS,_,_=parse_statements(SOURCE)
PROPOSALS=[]


def statement(sid):
    owner=next(o for o in OWNERS if o.statement_id==sid)
    return SOURCE[owner.start:owner.stop]


def between(text,start,end,include_end=False):
    assert text.count(start)==1,(start,text.count(start))
    a=text.index(start)
    b=text.index(end,a)+(len(end) if include_end else 0)
    return text[a:b]


def brace_end(s,i):
    assert s[i]=='{'
    depth=1;j=i+1
    while depth:
        if s[j]=='\\':j+=2;continue
        if s[j]=='{':depth+=1
        if s[j]=='}':depth-=1
        j+=1
    return j


def rename_math(payload,mapping,skip_subscript=False):
    """Rename reviewed single-letter math tokens, preserving control sequences.

    Reference/label and textual/font arguments are passed through literally.
    Braced replacement names work both as factors and as existing subscripts.
    """
    literal={'label','hypertarget','ref','eqref','cref','Cref','SeriesRef',
             'cite','begin','end','text','textrm','mathrm','operatorname',
             'mathbb','mathcal','mathsf','mathbf','mathfrak','mathit'}
    result=[];i=0
    while i<len(payload):
        if payload[i]=='\\':
            m=re.match(r'\\[A-Za-z]+|\\.',payload[i:],re.S)
            token=m.group();result.append(token);i+=len(token)
            name=token[1:]
            if name in literal:
                while i<len(payload) and payload[i].isspace():result.append(payload[i]);i+=1
                if i<len(payload) and payload[i]=='{':
                    j=brace_end(payload,i);result.append(payload[i:j]);i=j
                elif name.startswith('math') and i<len(payload):
                    result.append(payload[i]);i+=1
            continue
        c=payload[i]
        if c in mapping and not(skip_subscript and i+1<len(payload) and payload[i+1]=='_'):
            result.append('{'+mapping[c]+'}')
        else:result.append(c)
        i+=1
    return ''.join(result)


def rename(text,mapping,skip_subscript=False):
    # Every selected block uses these inline/display delimiters. Reference and
    # environment argument preservation is additionally checked below.
    pattern=re.compile(r'\$[^$]*\$|\\\[.*?\\\]|\\\(.*?\\\)',re.S)
    return pattern.sub(lambda m:rename_math(m.group(),mapping,skip_subscript),text)


def add(name,sid,old,new,reason,reverse):
    assert SOURCE.count(old)==1,(name,SOURCE.count(old))
    assert old!=new,name
    assert reverse(new)==old,('exact inverse failed',name)
    controls=r'\\(?:label|hypertarget|ref|eqref|cref|Cref|SeriesRef|cite)\s*(?:\[[^]]*\])?\{[^{}]*\}'
    assert Counter(re.findall(controls,old))==Counter(re.findall(controls,new)),name
    p=SOURCE.index(old)
    owner=next(o for o in OWNERS if o.statement_id==sid)
    assert owner.start<=p and p+len(old)<=owner.stop,(name,'owner scope')
    PROPOSALS.append(dict(name=name,finding='P15',statement_id=sid,tag=owner.tag,
        source_line=SOURCE.count('\n',0,p)+1,old=old,new=new,reason=reason))


def rename_block(name,sid,old,mapping,reason,skip_subscript=False,extras=None,protected=()):
    extras=extras or {}
    renamable=old
    holds={term:r'\operatorname{SsixProtected'+str(i)+'}' for i,term in enumerate(protected)}
    for term,hold in holds.items():
        assert term in renamable and hold not in renamable
        renamable=renamable.replace(term,hold)
    new=rename(renamable,mapping,skip_subscript)
    for term,hold in holds.items():new=new.replace(hold,term)
    for a,b in extras.items():
        assert a in new,(name,a)
        new=new.replace(a,b)
    def reverse(t):
        for a,b in reversed(list(extras.items())):t=t.replace(b,a)
        for a,b in mapping.items():t=t.replace('{'+b+'}',a)
        return t
    add(name,sid,old,new,reason,reverse)


def prepare():
    sid='maps:src:D.2.11';text=statement(sid)
    old=between(text,'Put $U=M_{IV}$',r'\emph{The product type-$II$ filling')
    rename_block('02KL-period-comparison-matrices',sid,old,
        {'U':r'\mathsf U','V':r'\mathsf V','S':r'\mathsf S'},
        'The proof already uses S for the elliptic surface and V for a vertical divisor. The local comparison matrices now carry mathsf font. The symbol map sends each old matrix U,V,S to the same displayed matrix mathsf U,mathsf V,mathsf S, fixes every entry and other symbol, and has the reverse name map. Matrix multiplication, transpose, inverse, determinant and the Hurwitz pair are therefore the identical expressions under this bijection. The entire comparison paragraph was read against the source; P16 independently corrects the IV* subscript.',protected=('M_{IV}',))
    old=between(text,'Thus the complete augmented integral map is',
        'The preceding target/source maps for the augmented matrix specialize')
    rename_block('02KL-augmented-matrix',sid,old,{'D':r'\mathsf D'},
        'D denotes the divisor P-O-(P-Q)+(-Q) earlier in the proof. The augmented 4-by-7 matrix now has symbol mathsf D. The displayed entries and unit-elimination target are fixed by the forward/reverse name map D_matrix <-> mathsf D; the divisor keeps its original symbol.')
    old='primitive generator. Hence the relative map\n$H_2(N,M)=\\mathbb Z\\to H_1(X^\\circ)=\\mathbb Z$ is injective,'
    new='primitive generator. For the cusp tube $N$, the relative map\n$H_2(N,\\partial N)=\\mathbb Z\\to H_1(X^\\circ)=\\mathbb Z$ is injective,'
    add('02KL-cusp-boundary-name',sid,old,new,
        'M names the section line bundle in this theorem. In the cited cusp-pair calculation the relative pair is the cusp tube and its boundary: the immediately preceding cusp meridian maps to -g. Writing (N,partial N) gives the same inclusion pair (N,M_boundary), under the pointwise identity on N and its boundary; it also defines N at this use. The relative group, map, sign, injectivity argument and conclusion are unchanged.',
        lambda t:t.replace(new,old))
    sid='os49:rem:type-c-marking';text=statement(sid)
    old='For its displayed \\(S\\), one has \\(S^tF_0=G_0\\); these identities'
    assert old in text
    rename_block('TypeC-reference-to-period-comparison-matrix',sid,old,{'S':r'\mathsf S'},
        'This is the explicit dependent use of the matrix renamed in 02KL. The identical matrix now has symbol mathsf S in both its definition and this equality; F_0 and G_0 and their displayed entries are unchanged.')
    sid='maps:src:D.2.25';text=statement(sid)
    old=between(text,'The contraction and base parameter are',
        '\\smallskip\\noindent\\emph{The actual curve class remains zero')
    rename_block('02L0-local-conifold-matrix',sid,old,{'M':r'\mathsf N'},
        'The statement and the torsion reduction use M=product m_i. The local node matrix is renamed mathsf N throughout its contraction, entry formula q=N_11 N_22, inverse charts and matrix-norm link. The exact map M_node <-> mathsf N fixes the entries (x,xw;y,yw) and the pair xi,eta; no multiplicity M is in this local block. The transition/inverse and orientation argument were read unchanged.')
    old=between(text,r'Let \(Q=X/S^1\)',r'\end{proof}')
    rename_block('02L0-orbit-and-free-complement-names',sid,old,{'Q':r'\mathcal Q'},
        'Q is the elliptic section bG earlier; X_0 is the weighted scalar sum in the statement. In this final smooth reconstruction the orbit five-manifold Q is renamed mathcal Q and the free complement X_0 is renamed X_free. Their defining sets and every inclusion, projection, tangent bundle, meridian, residue, spin, linking and surgery map remain the same under identity maps of those sets. The full quotient/reconstruction passage was read; its exact inverse name substitution recovers all prior formulas, including the image C_Q and quotient puncture Q_0.',
        extras={'X_0':r'X_{\rm free}'})
    sid='maps:src:D.2.26';text=statement(sid)
    old='Also the complete abelian determinant is\n$M(\\sum_i n_i/m_i-e)=\\pm1$.'
    new='Also the complete abelian determinant is\n$\\bigl(\\prod_i m_i\\bigr)(\\sum_i n_i/m_i-e)=\\pm1$.'
    add('02L1-explicit-total-multiplicity',sid,old,new,
        'The Seifert abelianization has the diagonal multiplicities m_i and last Euler relation. Its determinant expands as (product m_i)(sum n_i/m_i-e), up to the irrelevant sign in the displayed plus-or-minus-one condition. The old M denotes that same product in the referenced preceding calculation; writing the product explicitly removes the undeclared short name and avoids the later node matrix. Empty products retain value one.',
        lambda t:t.replace(new,old))
    old=between(text,'Put\n\\[\n\\begin{aligned}\nF&=\\prod_{\\mathrm{finite}}m_i',
        '\\emph{The complete list and its parameters.}')
    rename_block('02L1-integral-reduction-notation',sid,old,
        {'F':'F_f','Q':'Q_f','P':'P_f','D':'D_f','V':r'v_{\rm reg}',
         'T':r'T_{\rm reg}','X':'X_0','Y':'Y_0','Z':'Z_0','N':r'N_{\rm reg}'},
        'P,Q already denote the two elliptic sections; X denotes the threefold, T the torsion group, and V an exterior elsewhere. In this exact finite/regular reduction block, the scalar products are F_f=product_finite m_i, Q_f=product q_i (the statement name), P_f=F_f/Q_f; D_f is sum D_i; v_reg is the regular weighted vector; T_reg is its aggregate homomorphism; its coordinates X_0,Y_0 match the statement, with Z_0,N_reg for the other two. The symbol map fixes each underlying integer, vector, group element and homomorphism, including N_f and every D_i,t_j,p_i. Applying it to every displayed relation and inverse substitution leaves the mathematical calculation identical; the reverse map recovers the complete old block. The whole arithmetic reduction and exceptional empty-product cases were read.',
        skip_subscript=True)
    old=between(text,'The contraction is the rank-one matrix',
        'For an exceptional curve $C_0$')
    rename_block('02L1-local-conifold-matrix',sid,old,{'M':r'\mathsf N'},
        'The local node matrix receives the same symbol mathsf N as the identical local node comparison in 02L0. The forward/reverse name map fixes all four entries, q, the resolution coordinates and inverse charts. The total multiplicity has already been expanded as a product.')
    old=between(text,'write $M=\\varepsilon ab^t$ modulo',
        'Gluing the opposite normal neighbourhood')
    rename_block('02L1-conifold-link-factors',sid,old,
        {'M':r'\mathsf N','a':r'\xi','b':r'\eta'},
        'The statement uses a,b for fixed integral section coefficients. Here they are unit vectors in the rank-one matrix link, so they are renamed xi,eta and the node matrix consistently mathsf N. The map (a_link,b_link,M_node)->(xi,eta,mathsf N) is coordinatewise identity on vectors/matrices, has the reverse name map, and carries the gauge (a,b)~(ta,t^-1 b) to (xi,eta)~(t xi,t^-1 eta). The factor-swap map, its inverse and both orientation signs are unchanged.')
    old=between(text,'Let $Q$ be the closed oriented quotient,',r'\end{proof}')
    rename_block('02L1-orbit-and-free-complement-names',sid,old,{'Q':r'\mathcal Q'},
        'The elliptic section retains symbol Q, and the scalar X_0 remains the regular weighted sum. The smooth orbit manifold is renamed mathcal Q and the free complement is X_free. The two defining sets, all principal-bundle maps, spin/residue calculations, linking coordinates, twisted-suspension comparison and surgery are carried by identity maps, with the inverse name substitution recovering the whole passage. The entire smooth reconstruction was read.',
        extras={'X_0':r'X_{\rm free}'})


def main():
    prepare()
    now=datetime.now(timezone.utc).isoformat()
    defects=[];events=[]
    candidate=SOURCE
    for i,p in enumerate(PROPOSALS,1):
        ident=f"CLAUDE-III-P15-GLOBAL-{i:03d}"
        p['change_id']=ident
        assert candidate.count(p['old'])==1,p['name']
        candidate=candidate.replace(p['old'],p['new'],1)
        defects.append(dict(change_id=ident,type='D20',statement_id=p['statement_id'],
            old_location=f"source line {p['source_line']}; tag {p['tag']}",old_page='cp100 regrouped source; page concordance pending',
            new_location='same scoped proof/remark passage; '+p['name'],new_page='pending current rendered-PDF review',
            old_text=p['old'],new_text=p['new'],reason=p['reason'],
            review_status='Exact old/new passage and surrounding argument read '+now+' by continuation9_global_sweep; proposed, awaiting root admission and visual review.'))
        print(ident,p['statement_id'],p['name'])
    df=next(csv.reader((ROOT/'S6_SERIES_PUBLISH_defects_III.tsv').open(),delimiter='\t'))
    ef=next(csv.reader((ROOT/'CHECK_EVENTS.tsv').open(),delimiter='\t'))
    for sid in dict.fromkeys(p['statement_id'] for p in PROPOSALS):
        ps=[p for p in PROPOSALS if p['statement_id']==sid]
        eid='publish:c9:III:notation:'+sid
        e={k:'' for k in ef}
        e.update(statement_id=sid,date=now[:10],who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; continuation nine global notation reviewer',
            type='used and rechecked in this run',event_id=eid,phase='continuation9 Paper III notation',
            outcome='Read and compared the complete changed notation passages with their immediately relevant statement/proof scopes: '+', '.join(p['name'] for p in ps)+'. Every symbol map has an exact inverse recorded in the defects; all mathematical entries, relations, parameters and referenced identities are retained. No independent-proof, required-check or PDF-page credit is claimed.',
            source_file='code/S6_SERIES_PUBLISH_c9_notation_proposals.py',source_event_type='used and rechecked in this run',
            evidence_group=eid,date_utc=now,where='agents/continuation9_global_sweep/S6_SERIES_PUBLISH_c9_notation_proposals.json')
        events.append(e)
    OWN.mkdir(parents=True,exist_ok=True)
    (OWN/'S6_SERIES_PUBLISH_c9_notation_proposals.json').write_text(json.dumps(PROPOSALS,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
    for name,fields,data in [('S6_SERIES_PUBLISH_c9_notation_defects.tsv',df,defects),('S6_SERIES_PUBLISH_c9_notation_events.tsv',ef,events)]:
        with (OWN/name).open('w',encoding='utf-8',newline='') as f:
            w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(data)
    print(len(PROPOSALS),'guarded notation proposals;',len(events),'scope-specific comparison events; canonical source untouched.')


if __name__=='__main__':main()
