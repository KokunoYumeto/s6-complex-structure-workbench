#!/usr/bin/env python3
"""Verify preserved provenance bytes and perform a redacted screening pass.

The expected hashes were measured from the supplied attachments. A pattern
scan cannot authenticate API execution metadata or certify that arbitrary
natural-language names are nonprivate; the accompanying audit records the
manual reading and the limits of this mechanical check.
"""
from pathlib import Path
import hashlib
import json
import re

BASE=Path(__file__).resolve().parents[1]
EXPECTED={
 'anc/Q03_DEPOSIT_prompt.md':(17129,'aa9d96d9e3a4125df1dc9151f5cf69de6580ce79c99208a7bc48df0dad5bb706'),
 'anc/ai-provenance/Q03_PROMPT.txt':(9551,'792b1a676ab01162d40d78ac73440d5a0dbe5e31b626cac398bcb882358fa54a'),
 'anc/ai-provenance/Q03-solution.md':(94789,'3ebeb452d6f461c23b4f8fa6f04ba6ed15abac541b5d2562fa814ba77977e60c'),
 'anc/ai-provenance/Q03-check.md':(8900,'0ce501f1241a87fcffe637657effbceb84b487bf20021b2dc95fa1a465f06079'),
 'anc/ai-provenance/Q03-b-check-b.md':(10676,'15ea0b95e4b23f68bb0b50a2eda1d08cae99793cf3ce46a9e15b5a5c95071b2a'),
 'anc/ai-provenance/Q03-c-check-c.md':(10207,'e1a821b14067ec136f80b6c6e0e2705dc04ffe84d28a4c7f15564de12bbdb30b'),
}
PATTERNS={
 'absolute_unix_path':re.compile(r'(?<![\w:])/(?:home|Users|workspace|mnt|tmp|private|var|root)/[^\s\])}>"\']+'),
 'file_uri':re.compile(r'file://[^\s\])}>"\']+'),
 'home_relative_path':re.compile(r'(?<!\w)~/[^\s\])}>"\']+'),
 'possible_windows_drive':re.compile(r'(?<![\w:])[A-Za-z]:\\[^\s\])}>"\']+'),
 'private_key_marker':re.compile(r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----'),
 'api_key_style':re.compile(r'(?<![A-Za-z0-9])(?:sk-[A-Za-z0-9_-]{20,}|gh[pousr]_[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16})'),
 'credential_assignment':re.compile(r'(?i)(?:api[_ -]?key|password|access[_ -]?token|secret[_ -]?key)\s*[:=]\s*["\']?[^\s"\']{12,}'),
 'email_address':re.compile(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'),
}
# These two matches were opened and read. Both are TeX function signatures
# beginning f:\mathscr; neither is a drive path. No substantive bytes change.
MANUAL_FALSE_POSITIVES={
 ('anc/ai-provenance/Q03-solution.md',545,'possible_windows_drive'),
 ('anc/ai-provenance/Q03-b-check-b.md',50,'possible_windows_drive'),
}

def main():
    result={'audit_date':'2026-11-15','copy_checks':[], 'screening':[],
            'privacy_scan_scope':'six mandatory provenance files; exact raw bytes retained'}
    for name,(nbytes,expected) in EXPECTED.items():
        b=(BASE/name).read_bytes();sha=hashlib.sha256(b).hexdigest()
        assert len(b)==nbytes and sha==expected, name
        result['copy_checks'].append({'file':name,'bytes':len(b),'sha256':sha,'matches_supplied':True})
        for no,line in enumerate(b.decode('utf8').splitlines(),1):
            for kind,pattern in PATTERNS.items():
                if pattern.search(line):
                    manual=(name,no,kind) in MANUAL_FALSE_POSITIVES
                    result['screening'].append({'file':name,'line':no,'class':kind,
                        'matched_text':'REDACTED','manual_disposition':'TeX function notation; false positive' if manual else 'REVIEW REQUIRED'})
                    assert manual, f'Unreviewed screening match: {name}:{no}:{kind}'
    b=(BASE/'anc/ai-provenance/Q03_PROMPT.txt').read_bytes()
    target='41db4774893d4ee075889202411db254e3884a111734b07d6959c5670faec13b'
    transforms={
        'identity':b,
        'CRLF_to_LF':b.replace(b'\r\n',b'\n'),
        'LF_to_CRLF':b.replace(b'\r\n',b'\n').replace(b'\n',b'\r\n'),
        'remove_UTF8_BOM':b.removeprefix(b'\xef\xbb\xbf'),
        'remove_terminal_newlines':b.rstrip(b'\r\n'),
    }
    result['prompt_manifest_comparison']={
        'manifest_path':'provenance/artifacts/MANIFEST.json, entries inputs/PROMPT.txt',
        'recorded_bytes':9383,'recorded_sha256':target,
        'supplied_prompt_LF_count':b.count(b'\n'),'supplied_prompt_CRLF_count':b.count(b'\r\n'),
        'supplied_prompt_CR_count':b.count(b'\r'),
        'exact_byte_maps_tested':[{'map':name,'bytes':len(x),'sha256':hashlib.sha256(x).hexdigest(),
          'matches_manifest':hashlib.sha256(x).hexdigest()==target} for name,x in transforms.items()],
        'verdict':'The recorded inputs/PROMPT.txt was not supplied; byte identity with supplied Q03_PROMPT.txt is unestablished. Supplied bytes remain unchanged.'
    }
    result['observed_private_credentials']=0
    result['observed_actual_local_paths']=0
    result['report_run_metadata']='Dates, API mode, and independent-run description are supplied-record metadata; raw API batch logs were not supplied.'
    print(json.dumps(result,indent=2,ensure_ascii=False))

if __name__=='__main__':main()
