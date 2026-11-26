"""Place the complete universal proof early, preserving the native setup."""
from datetime import datetime, timezone
import S6_SERIES_PUBLISH_c8_integrate_units as u
import S6_SERIES_PUBLISH_c8_root_units as r

folder = u.ROOT / 'agents/continuation8_iii_weighted_units'
rows = r.table(folder / 'S6_SERIES_PUBLISH_SPHERE_PAIRING_publication_defects.tsv')[1]
row = [x for x in rows if x['change_id'] == 'III-C8-SPHERE-PUB-005-D14']
assert len(row) == 1
old = row[0]['old_text'].rstrip() + '\n'
native_source = (u.WORK / 'root/full_sphere_nullity.tex').read_text()
start = native_source.index(r'\begin{corollary}[The two-copy sphere carrier]')
end = native_source.index(r'\paragraph{The one-copy coefficient and the framed fibre.}', start)
native = native_source[start:end].rstrip() + '\n'
early = (u.WORK / 'root/sphere_smash_pairing.tex').read_text()
regular = (u.WORK / 'root/regular_quotients.tex').read_text()
before = u.repairs.SOURCE.read_text()
assert before.count(old) == before.count(regular) == 1
assert before.count(early) == 0 and before.count(native) == 0
after = before.replace(old, native, 1).replace(regular, regular + early + '\n', 1)
u.check_permanent_identifiers(before, after,
    {'wb:def:ordered-cube-spheres', 'wb:cusp-s12-native-smash-null'},
    {'tag-Q253', 'tag-Q254'})
assert after.count(early) == after.count(native) == 1
assert after.replace(early + '\n', '', 1).replace(native, old, 1) == before
assert after.index(early) < after.index(r'\label{wb:cusp-cone-section}')
assert after.index(native) > after.index(r'\label{wb:cusp-cone-section}')
df, ds = r.table(r.DEFECTS)
ident = 'III-C8-PLACE-SPHERE-UNIVERSAL-SPLIT'
assert not any(x['change_id'] == ident for x in ds)
ds.append(dict(change_id=ident, type='D14', statement_id='038V; 038T; Q253; Q254',
    old_location='canonical universal block in the038U native subsection', old_page='pending page concordance',
    new_location='universal unit immediately after regular_quotients; Q254 at the same native block position', new_page='pending final PDF',
    old_text=old, new_text=early + '\n% Separate native application at its original geometric boundary:\n' + native,
    reason='Move the fully read universal theorem and higher-power proof before carrierU8. Preserve the entire038U heading/setup and all038X/038W text byte-for-byte; replace only the old universal block by its exact Q254 native application. The two substitutions reverse exactly, and every old identity keeps its multiplicity. The local15-row substantive edit record is admitted separately.',
    review_status='bounded canonical split applied; actual boundary reading and attributed admission pending; no helper criterion credit'))
u.repairs.SOURCE.write_text(after, encoding='utf-8', newline='\n')
r.write_table(r.DEFECTS, df, ds)
print('UTC', datetime.now(timezone.utc).isoformat())
print('UNIVERSAL_EARLY_NATIVE_LATER; EXACT_REVERSE_AND_ALL_OLD_IDENTITIES_VERIFIED')
for name, fragment in [('UNIVERSAL', early), ('NATIVE_APPLICATION', native)]:
    i = after.index(fragment)
    j = i + len(fragment)
    print(name, 'LINES', after.count('\n', 0, i) + 1, after.count('\n', 0, j))
    print('FOLLOWING_BOUNDARY', repr(after[j:j+400]))
print('NO_PROOF_OR_CRITERION_CREDIT; NATIVE_PUBLICATION_PASS_REMAINS_OPEN')
