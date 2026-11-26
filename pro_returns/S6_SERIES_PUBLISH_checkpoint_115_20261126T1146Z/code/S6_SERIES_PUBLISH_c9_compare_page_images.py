"""Locate changed full-page images against an actually read prior candidate.

Equality uses the entire decoded pixel array, with identical size and mode,
at the same physical page. No crop, footer removal, rescaling, perceptual
tolerance or OCR comparison is used. This command supplies page locators;
it grants no new reading or mathematical-check credit and writes no ledger.
"""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import argparse
from PIL import Image


def pages(directory):
    result = {int(p.stem.split('-')[-1]): p for p in directory.glob('page-*.png')}
    assert result and sorted(result) == list(range(1, max(result) + 1))
    return result


def intervals(values):
    groups = []
    first = last = None
    for value in values:
        if first is None:
            first = last = value
        elif value == last + 1:
            last = value
        else:
            groups.append(str(first) if first == last else f'{first}-{last}')
            first = last = value
    if first is not None:
        groups.append(str(first) if first == last else f'{first}-{last}')
    return ', '.join(groups) or '(none)'


parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--prior', required=True, type=Path)
parser.add_argument('--current', required=True, type=Path)
args = parser.parse_args()
old = pages(args.prior.resolve())
new = pages(args.current.resolve())


def equal(number):
    if number not in old:
        return number, False
    with Image.open(old[number]) as left, Image.open(new[number]) as right:
        same = left.mode == right.mode and left.size == right.size
        if same:
            same = left.tobytes() == right.tobytes()
    return number, same


with ThreadPoolExecutor(max_workers=4) as pool:
    results = list(pool.map(equal, sorted(new)))
unchanged = [number for number, same in results if same]
changed = [number for number, same in results if not same]
removed = sorted(set(old) - set(new))
assert sorted(unchanged + changed) == sorted(new)
print('Prior images:', len(old), 'Current images:', len(new))
print('Full decoded pixel equality at the same physical page:', len(unchanged))
print('UNCHANGED:', intervals(unchanged))
print('Current pages requiring actual new image reading:', len(changed))
print('CHANGED:', intervals(changed))
print('Prior physical pages beyond the current document:', intervals(removed))
print('Every changed current page remains open for authored actual-image reading.')
print('Identical pixels only preserve the exact prior image observation, with its original scope and attribution. No additional proof or reading credit is created.')
