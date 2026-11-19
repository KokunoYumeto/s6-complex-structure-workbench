"""Reconcile superseded pending prose in receiving check records.

The chronological event ledgers are unchanged.  Replacements below are tied to
the exact receiving labels and to the subsequently recorded source/replay
scopes.  This operation awards no mathematical or computational check credit.
"""
from pathlib import Path
import hashlib
import json
import sys

OUT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(OUT / 'code'))
from inventory_reconcile import argument, commands

RULES = []


def rule(labels, old, new):
    RULES.append((set(labels.split()), old, new))


rule('fam:src:C.1.1 fam:src:C.1.2 fam:src:C.2.1 fam:src:C.2.2 fam:src:C.2.3 '
     'ari:C.1.1 ari:C.4.2 ari:C.8.1 ari:C.8.2 ari:C.8.3 ari:C.8.4',
     'Numerical interval certificates have not yet been independently recomputed; analytic division-ladder proof checked separately.',
     'Numerical replay scopes are recorded with their exact statement labels; the analytic argument is checked here.')
rule('fam:src:D.1.1 fam:src:D.1.3 fam:src:D.1.4 fam:src:D.1.5',
     'Source Weierstrass scaling direction will be corrected using I:weierstrass-comparison; exact polynomial replay pending.',
     'The Weierstrass scaling direction is carried by the explicit map I:weierstrass-comparison.')
rule('fam:src:D.1.1 fam:src:D.1.3 fam:src:D.1.4 fam:src:D.1.5',
     'Exact background citations and the indicated finite symbolic programs remain separate gates.',
     'Exact source passages and finite symbolic replays retain their separately recorded scopes.')
rule('push:src:A.2.5',
     'Matsuki corrected relative-factorization locator pending.',
     r'opened Matsuki\textquoteright s corrected Weak Factorization Theorem for Toroidal Birational Morphisms, Section~2, p.~2, for smooth-stratum blowups and blowdowns over the target.')
rule('push:src:B.3.6',
     'HS53/CDL24/Xiao91 exact source gates remain pending. ', '')
rule('push:src:B.3.7',
     'Brauer/relative-Picard source gate pending. ', '')
rule('push:src:B.4.2',
     'Nakayama-Ogus5.1 exact source gate pending for the first route; the second route is derived directly.',
     r'Opened Nakayama--Ogus Theorem~5.1, Corollary~5.2 and Proposition~5.3, p.~2226, and matched the proper separated exact relatively smooth log-analytic hypotheses for the oriented fibre-bundle route. The second route is derived directly.')
rule('push:src:B.4.4 push:src:B.4.27 push:src:B.4.30 push:src:B.4.32 push:src:B.4.33 '
     'push:src:D.1.1 push:src:D.1.2 push:src:D.1.3',
     'For B4.30/B4.32/B4.33 external log-de-Rham hypotheses remain a separately tracked citation gate; current main no-filling proof is being transferred to the direct commuting-meridian argument night:P2.7.',
     'The external logarithmic comparison applications in B4.30/B4.32/B4.33 were audited separately against IKN and its erratum; the independent direct commuting-meridian proof is night:P2.7.')
rule('inv:D4.1 inv:D4.2 inv:D4.3 inv:D4.4 inv:D4.5 inv:D1.1 inv:D1.2',
     'Exact Koszul and twist-program replay pending.',
     'Exact Koszul and twist-program computations retain their separately recorded replay scopes.')
rule('ari:C.6.3',
     'Rank, saturation, directed L-derivative replays and precise external theorem matches remain explicit gates; no proof verdict is awarded to those computational claims by this read.',
     'Rank, saturation, directed L-derivative replays and precise external theorem matches have their separately recorded scopes.')
rule('ari:C.6.3',
     'Rank and L-value claims have their own pending gates. ', '')
rule('ari:C.7.3',
     'Read the relevant Bertolin source propositions; exact source-edition pagination remains pending. ', '')
rule('ari:C.7.11',
     'External criterion locators and receiving reformulation remain pending. ', '')
rule('ari:C.7.11',
     'with no algebraicity premise; the finite-order criterion source is still pending.',
     'with no algebraicity premise.')
rule('ari:C.7.12',
     'The receiving statement is being reformulated as unconditional algebraic ratios and scalar models; no unresolved algebraicity hypothesis is adopted.',
     'The receiving statement uses unconditional algebraic ratios and scalar models; no unresolved algebraicity hypothesis is adopted.')
rule('ari:C.7.12',
     'External criterion-audit source matches remain pending. ', '')


def clean_check_scope(label, check):
    for labels, old, new in RULES:
        if label in labels:
            check = check.replace(old, new)
    return check


def rewrite(text):
    edits = []
    for command in commands(text, 'StatementRecord'):
        label = command['value']
        at = command['end']
        for slot in range(3):
            while text[at].isspace():
                at += 1
            start = at
            value, at = argument(text, at)
            if slot == 1:
                changed = clean_check_scope(label, value)
                if changed != value:
                    edits.append({'label': label, 'start': start + 1,
                                  'end': at - 1, 'old': value, 'new': changed})
    for edit in reversed(edits):
        text = text[:edit['start']] + edit['new'] + text[edit['end']:]
    return text, edits


def main():
    paths = sorted((OUT / 'papers/I').glob('*.tex'))
    preview = OUT / 'build/I_preview/preview.tex'
    if preview.exists():
        paths.append(preview)
    receipt = {'date': '2026-11-18',
               'scope': 'Receiving check prose only; unchanged event ledgers and unchanged statements/proofs; no new proof or replay credit.',
               'evidence': ['analysis/root_checkrecord_stale_scope_audit.json',
                            'analysis/I_sources/current_source_matches.json',
                            'records/root_events.tsv'], 'files': []}
    for path in paths:
        old = path.read_text()
        new, edits = rewrite(old)
        if not edits:
            continue
        assert rewrite(new)[0] == new
        path.write_text(new)
        receipt['files'].append({'file': str(path.relative_to(OUT)),
                                 'old_sha256': hashlib.sha256(old.encode()).hexdigest(),
                                 'new_sha256': hashlib.sha256(new.encode()).hexdigest(),
                                 'edits': edits})
    target = OUT / 'analysis/I_checkrecord_scope_reconciliation.json'
    target.write_text(json.dumps(receipt, indent=2) + '\n')
    print(json.dumps({'receipt': str(target), 'files': len(receipt['files']),
                      'records': sum(len(x['edits']) for x in receipt['files'])}))


if __name__ == '__main__':
    main()
