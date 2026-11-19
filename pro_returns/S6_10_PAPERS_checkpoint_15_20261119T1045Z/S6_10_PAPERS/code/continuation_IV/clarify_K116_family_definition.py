#!/usr/bin/env python3
"""Clarify the defined K116 continuation without erasing a family scalar.

Only receiving prose changes. Original cp36 sources stay byte-identical.
The receipt preserves both exact paragraphs and the before/after file hashes.
"""
from pathlib import Path
from datetime import datetime, timezone
import argparse, hashlib, json

ROOT = Path(__file__).resolve().parents[2]
RECEIPT = ROOT / 'analysis/continuation_IV/K116_family_definition_patch.json'
FILES = ['papers/IV/continuation_night36.tex', 'papers/IV/body.tex', 'papers/IV/body_source.tex']

OLD1 = r'''whole-fibre zero. \(C_*\ne0\) retains the initially prescribed
linearization. Explicitly, evaluate the initial map divided
by \((t-t_c)B_{8,1}\) at one fixed regular point. The zero
divisors agree, so their ratio is constant on the compact
source. Continue that same constant on \(\Delta\). This is
an exact match of the reference, not a change in the scalar.'''
NEW1 = r'''whole-fibre zero. Here is the definition of the continuation
family used in this proof. Let \(a_0\) denote its initial marked
source and \(L_{a_0}\) the prescribed directed whole-zero line map.
At a protected regular point \(s_0\), evaluate both maps in the
same Cartier frames and set
\[
 C_*=
 \frac{L_{a_0}(s_0)}
 {(t(s_0)-t_c(a_0))B_{8,1,a_0}(s_0)}\ne0.
\]
The ratio is an invertible function on the compact initial source,
so it is constant on that source. Thus (O45.20) agrees with
\(\lambda L_{a_0}\) on the entire initial source. For every
subsequent marked parameter, the continuation family is defined
by (O45.20) with this fixed \(C_*\). The full coefficient maps
and inverses establish the analytic extension of this defined
family. Its boundary family is its restriction with the prescribed
initial cap and reference continued by the displayed maps.

The initial evaluation proves equality at \(a_0\); it does not
identify an independently prescribed varying linearization
\(L_a\) with the defined continuation. Its exact fibrewise ratio,
evaluated in the same frames on a protected section \(s(a)\), is
\[
 c(a)=\frac{L_a(s(a))}
 {(t(s(a))-t_c(a))B_{8,1,a}(s(a))}.
\]
Such an additional comparison retains \(c(a)\) in the full
suspension coefficient. No constancy or disc extension of that
additional ratio is deduced from the one initial evaluation.'''
OLD2 = r'''The initial nonzero \(C_*\) is fixed by evaluation at one
protected regular point. The ratio of two such linearizations
with the same divisor is an invertible function on the compact
source, hence is constant there. Continuing this actual constant
along the prescribed source path retains the original scalar
normalization throughout the new disc.'''
NEW2 = r'''The continuation in (O45P.22) is defined using the single
nonzero \(C_*\) obtained from the prescribed initial line map
\(L_{a_0}\) at a protected regular point \(s_0\), in the same
Cartier frames:
\[
 C_*=
 \frac{L_{a_0}(s_0)}
 {(t(s_0)-t_c(a_0))B_{8,1,a_0}(s_0)}.
\]
Equality of the divisors makes this ratio an invertible function
on the compact initial source, hence constant on that source.
This proves equality of the entire initial map with
\(C_*(t-t_c)B_{8,1}\). At later marked parameters (O45P.22),
with this same specified \(C_*\), defines the continuation
family whose coefficient maps and inverses extend over the disc.
The boundary identification in this proof concerns this defined
continuation of the initial source, line, cap and reference.

For an independently prescribed varying line map \(L_a\), the
exact comparison retains the analytic evaluation ratio
\[
 c(a)=\frac{L_a(s(a))}
 {(t(s(a))-t_c(a))B_{8,1,a}(s(a))}
\]
wherever these maps and the protected section are defined. Its value
\(c(a_0)=C_*\) alone proves neither constancy nor extension
through a missing parameter. That further family comparison
is not asserted here.'''

def sha(x):
    return hashlib.sha256(x).hexdigest()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--undo', action='store_true')
    args = parser.parse_args()
    if args.undo:
        receipt = json.loads(RECEIPT.read_text())
        for rec in receipt['files']:
            path = ROOT / rec['file']
            raw = path.read_bytes()
            if sha(raw) != rec['after_sha256']:
                raise ValueError('Refusing undo after subsequent source change: ' + rec['file'])
            text = raw.decode()
            for change in reversed(rec['changes']):
                assert text.count(change['after']) == 1
                text = text.replace(change['after'], change['before'], 1)
            assert sha(text.encode()) == rec['before_sha256']
            path.write_text(text)
        return
    if RECEIPT.exists():
        data = json.loads(RECEIPT.read_text())
        for rel in FILES:
            text = (ROOT / rel).read_text()
            assert text.count(NEW1) == text.count(NEW2) == 1
        print(json.dumps({'already_applied': True, 'receipt': str(RECEIPT)}))
        return
    prepared=[]
    for rel in FILES:
        path=ROOT/rel;before=path.read_bytes();text=before.decode();changes=[]
        for old,new in [(OLD1,NEW1),(OLD2,NEW2)]:
            assert text.count(old)==1, (rel, text.count(old))
            text=text.replace(old,new,1);changes.append({'before':old,'after':new})
        prepared.append((path,text,{'file':rel,'before_sha256':sha(before),'after_sha256':sha(text.encode()),'changes':changes}))
    for path,text,_ in prepared:path.write_text(text)
    sources=[]
    for filename in ['part3_os45_unselected_ii_o45_proof.tex','part3_os45_unselected_ii_o45p_proof.tex']:
        path=ROOT.parents[1]/'night36/S6_06_BLIND/notes'/filename
        sources.append({'file':str(path),'sha256':sha(path.read_bytes()),'changed':False})
    data={'timestamp_utc':datetime.now(timezone.utc).isoformat(),
          'authorization':'Root requested the exact fixed-C_* family definition following fresh prereading review and target comparison, 19 November 2026.',
          'scope':'Definition and matching scope only. Initial equality is proved fibrewise; no equality to an independently prescribed varying L_a or constancy/extension of its ratio is inferred. Receiving K116 remains open pending the outstanding complete proof gates.',
          'files':[x[2] for x in prepared], 'original_cp36_sources':sources}
    RECEIPT.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'files':len(prepared),'paragraphs_per_file':2,'receipt':str(RECEIPT)}))

if __name__=='__main__':main()
