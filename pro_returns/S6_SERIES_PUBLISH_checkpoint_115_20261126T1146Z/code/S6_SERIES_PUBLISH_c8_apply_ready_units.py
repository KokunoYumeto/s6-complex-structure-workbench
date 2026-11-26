"""Apply explicitly selected finished fragments at an exact current boundary.

This is source application only. It preserves every unselected byte in its
current order and every existing identity. Reviews, events and progress are
admitted separately; this helper creates no inventory, manifest or receipt.
"""
from __future__ import annotations
import argparse
from collections import Counter
from datetime import datetime, timezone
import re
import S6_SERIES_PUBLISH_c8_integrate_units as u
import S6_SERIES_PUBLISH_c8_root_units as r

def current_owners():
    result={}
    for spec in u.UNITS:
        text=(u.WORK/spec.owner/(spec.key+'.tex')).read_text(encoding='utf-8')
        for tag,label in u.ANCHOR_LABEL.findall(text):
            if tag in result and result[tag].key != spec.key:
                raise ValueError('Conflicting fragment ownership: '+tag)
            result[tag]=spec
    return result

def headings(text):
    out=[]
    pattern=re.compile(r'(?m)^\\(?:part|section|subsection)\*?(?:\[[^\n]*\])?\{')
    for match in pattern.finditer(text):
        end=u.group_end(text,match.end()-1)
        out.append(text[match.start():end])
    return '\n'.join(out)

def prepare(keys,anchor_key,after=False):
    source=u.repairs.SOURCE.read_text(encoding='utf-8')
    owners=current_owners()
    pieces=u.parse_pieces(source,owners)
    assert ''.join(source[p.start:p.end] for p in pieces)==source
    selected=set(keys)
    assert anchor_key not in selected
    anchor_pieces=[p for p in pieces if p.unit_key==anchor_key]
    assert anchor_pieces,anchor_key
    anchor=anchor_pieces[-1] if after else anchor_pieces[0]
    anchor_text=source[anchor.start:anchor.end]
    kept=''.join(source[p.start:p.end] for p in pieces if p.unit_key not in selected)
    assert kept.count(anchor_text)==1,'Unique insertion boundary'
    fragments={key:(u.WORK/u.BY_KEY[key].owner/(key+'.tex')).read_text(encoding='utf-8') for key in keys}
    joined=''.join(fragments[key] for key in keys)
    candidate=kept.replace(anchor_text,anchor_text+joined if after else joined+anchor_text,1)
    old_labels=Counter(u.repairs.LABEL.findall(source))
    new_labels=Counter(u.repairs.LABEL.findall(candidate))
    old_targets=Counter(u.ALL_TARGETS.findall(source))
    new_targets=Counter(u.ALL_TARGETS.findall(candidate))
    allowed_labels=set(new_labels-old_labels)
    allowed_targets=set(new_targets-old_targets)
    for tag in allowed_targets:
        if not re.fullmatch(r'tag-Q[0123][0-9A-Z]{2}',tag):
            raise ValueError('Unreserved new target: '+tag)
    for target in allowed_targets:
        expected=owners[target.removeprefix('tag-')]
        assert expected.key in selected
    u.check_permanent_identifiers(source,candidate,allowed_labels,allowed_targets)
    candidate_pieces=u.parse_pieces(candidate,owners)
    assert ''.join(candidate[p.start:p.end] for p in candidate_pieces)==candidate
    for key in keys:
        assert candidate.count(fragments[key])==1,'Exact completed fragment: '+key
    details=[]
    for key in keys:
        old_pieces=[p for p in pieces if p.unit_key==key]
        assert old_pieces,key
        old_text=''.join(source[p.start:p.end] for p in old_pieces)
        details.append((key,u.range_text(source,old_pieces),headings(old_text),headings(fragments[key])))
    return source,candidate,details,sorted(allowed_labels),sorted(allowed_targets)

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--group',required=True)
    parser.add_argument('--keys',nargs='+',required=True,choices=u.BY_KEY)
    parser.add_argument('--anchor',required=True,choices=u.BY_KEY)
    parser.add_argument('--after',action='store_true')
    parser.add_argument('--apply',action='store_true')
    args=parser.parse_args()
    source,candidate,details,labels,targets=prepare(args.keys,args.anchor,args.after)
    print('INSERT', 'after' if args.after else 'before',args.anchor)
    for key,ranges,old_heads,new_heads in details:
        print('UNIT',key,'FROM_CURRENT_LINES',ranges)
        print('OLD_HEADINGS',repr(old_heads))
        print('NEW_HEADINGS',repr(new_heads))
    print('NEW_LABELS',labels)
    print('NEW_TARGETS',targets)
    print('ALL_OLD_IDENTITIES_AND_UNSELECTED_TEXT_PRESERVED')
    print('NO_PROOF_OR_CRITERION_CREDIT')
    if not args.apply:
        print('INSPECT_ONLY; NO_WRITES')
        return
    fields,rows=r.table(r.DEFECTS)
    for key,ranges,old_heads,new_heads in details:
        ident='III-C8-PLACE-'+args.group+'-'+key
        assert not any(x['change_id']==ident for x in rows)
        rows.append(dict(change_id=ident,type='D14',statement_id='; '.join(u.BY_KEY[key].tags),old_location='current canonical lines '+ranges,old_page='pending page concordance',new_location=('after ' if args.after else 'before ')+args.anchor,new_page='pending final PDF',old_text=old_heads,new_text=new_heads,reason='Apply the fully reviewed fragment with its complete statements/proofs at the stated dependency boundary. Its individual text edits are in the attributed local defects table; the whole-fragment and identity guards match exactly. This placement operation alone assigns no source criterion or proof credit.',review_status='completed fragment placed; attributed review admission and final PDF reading pending'))
    u.repairs.SOURCE.write_text(candidate,encoding='utf-8',newline='\n')
    r.write_table(r.DEFECTS,fields,rows)
    print('CANONICAL_APPLIED_UTC',datetime.now(timezone.utc).isoformat())

if __name__=='__main__': main()
