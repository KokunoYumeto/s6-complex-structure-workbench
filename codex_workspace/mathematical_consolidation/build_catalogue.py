import collections
import gzip
import hashlib
import io
import json
import pathlib
import re
import sqlite3
import zipfile

ROOT = pathlib.Path(__file__).resolve().parent
CORPUS = ROOT.parent
WORK = pathlib.Path(r'C:\Users\user\Documents\math\work\s6_main_01a0ea06-5fdc-7a60-97f3-4f4347467d95')
ROOT.joinpath('nested_source_blobs').mkdir(exist_ok=True)
TEXT_EXT = {'.tex','.bib','.md','.txt','.py','.json','.jsonl','.csv','.tsv','.sty','.cls','.lean','.sage','.jl','.r','.m','.wl','.c','.cpp','.h','.js','.ts','.html','.sh','.ps1','.bat'}
LANES = {
 'analytic_candidate': r'candidate_geometry|analytic_picard|integral_leray|algebraic_dimension|hodge_frolicher|topology_reduction|cdp_program|local_repairs|nearby.cycle|gluing|marked_arithmetic',
 'cusp_spectral': r'cusp|spectral|magnetic|period_discriminant|worldline',
 'arithmetic_selector': r'koide|erdos.straus|p1201|selector|c123|divisor',
 'lattice_jordan': r'niemeier|leech|triality|albert|umbral|symmetric.group|rank.six|rank.nine|24d|octonion',
 'quaternionic_gauge': r'quaternion|4441|gauge|hermitian_normal|lorentz|gram.cone|geometric_unity',
 'measured_fibres': r'nolan|gaussian|fisher|residual_measure|kernel_projection|chirality|decoherence',
 'finite_quantum': r'quantum|wilson|plaquette|vacuum|weak_coupling|blocking|confinement',
 'rh_heat_crossrefs': r'xi4|rh_|zeta|heat_transport|arithmetic_resolvent|connes|dbn_ns',
}
db_path = ROOT / 'CORPUS_CATALOGUE.sqlite'
if db_path.exists():
    raise RuntimeError('Existing catalogue retained; use a separately named edition for changed scope.')
db = sqlite3.connect(db_path)
db.executescript('''
CREATE TABLE versions(sha256 TEXT PRIMARY KEY, corpus_file TEXT, bytes INTEGER, suffix TEXT, lines INTEGER, lexical_status TEXT);
CREATE TABLE occurrences(id INTEGER PRIMARY KEY, sha256 TEXT, archive_sha256 TEXT, archive_path TEXT, member TEXT, container_chain TEXT, source_root TEXT, origin TEXT);
CREATE TABLE spans(id INTEGER PRIMARY KEY, sha256 TEXT, kind TEXT, name TEXT, start_line INTEGER, end_line INTEGER, start_offset INTEGER, end_offset INTEGER, span_sha256 TEXT, status TEXT);
CREATE TABLE references_found(id INTEGER PRIMARY KEY, sha256 TEXT, kind TEXT, target TEXT, line INTEGER);
CREATE TABLE topics(sha256 TEXT, lane TEXT, basis TEXT, PRIMARY KEY(sha256,lane));
CREATE TABLE opaque_members(id INTEGER PRIMARY KEY, archive_sha256 TEXT, member TEXT, container_chain TEXT, bytes INTEGER, suffix TEXT, status TEXT);
CREATE TABLE nested_packages(sha256 TEXT PRIMARY KEY, members INTEGER, status TEXT);
CREATE INDEX occurrence_hash ON occurrences(sha256);
CREATE INDEX span_hash ON spans(sha256);
CREATE INDEX reference_target ON references_found(kind,target);
''')
counts = collections.Counter()
known = {}
archive_routes = {r['sha256']:r['archive'] for r in json.loads((WORK/'FINAL_CUSTODY_AUDIT.json').read_text())['archives']}
bindings = {}

def lines_at(text, offset):
    return text.count('\n',0,offset)+1

def add_version(digest, path):
    if digest in known:
        return
    raw = path.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == digest, str(path)
    suffix = path.suffix.lower()
    try:
        text = raw.decode('utf-8-sig')
        decode_status = 'strict UTF-8 text; source bytes unchanged'
    except UnicodeDecodeError:
        db.execute('insert into versions values(?,?,?,?,?,?)',(digest,str(path),len(raw),suffix,None,'undecoded exact bytes; not structurally extracted'))
        known[digest] = path
        counts['undecoded_text_versions'] += 1
        return
    db.execute('insert into versions values(?,?,?,?,?,?)',(digest,str(path),len(raw),suffix,len(text.splitlines()),decode_status))
    known[digest] = path
    counts['unique_versions'] += 1
    if suffix == '.tex':
        counts['tex_versions'] += 1
        # Literal lexical inventory, including inactive branches and comments.
        # It deliberately makes no macro expansion or semantic proof decision.
        stack = []
        for m in re.finditer(r'\\(begin|end)\s*\{([^{}]+)\}',text):
            action, env = m.groups()
            if action == 'begin':
                stack.append((env,m.start()))
            elif stack and stack[-1][0] == env:
                env,start = stack.pop()
                if re.search(r'theorem|lemma|proposition|corollary|definition|remark|proof|counterexample|auditrecord|sourcequote|equation|align|gather|multline',env,re.I):
                    span = text[start:m.end()]
                    kind = 'proof' if re.search('proof',env,re.I) else 'display' if re.search('equation|align|gather|multline',env,re.I) else 'statement_or_note'
                    db.execute('insert into spans(sha256,kind,name,start_line,end_line,start_offset,end_offset,span_sha256,status) values(?,?,?,?,?,?,?,?,?)',(digest,kind,env,lines_at(text,start),lines_at(text,m.end()),start,m.end(),hashlib.sha256(span.encode('utf-8')).hexdigest(),'lexical exact span; not independently audited'))
                    counts['spans_'+kind] += 1
            else:
                counts['lexical_unmatched_end'] += 1
        counts['lexical_unclosed_begin'] += len(stack)
        for m in re.finditer(r'\\(section|subsection|subsubsection|paragraph|chapter)\*?\s*(?:\[[^\]]*\])?\s*\{([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}',text):
            db.execute('insert into spans(sha256,kind,name,start_line,end_line,start_offset,end_offset,span_sha256,status) values(?,?,?,?,?,?,?,?,?)',(digest,'heading',m.group(2),lines_at(text,m.start()),lines_at(text,m.end()),m.start(),m.end(),hashlib.sha256(m.group().encode()).hexdigest(),'literal heading; topic routing only'))
        for m in re.finditer(r'\\(label|ref|eqref|cref|Cref|input|include|cite[a-zA-Z]*)\*?\s*(?:\[[^\]]*\]\s*)*\{([^{}]+)\}',text):
            kind,target = m.groups()
            for part in target.split(',') if kind not in ['input','include'] else [target]:
                db.execute('insert into references_found(sha256,kind,target,line) values(?,?,?,?)',(digest,kind,part.strip(),lines_at(text,m.start())))

def occurrence(row, source, path=None, chain='', origin='previous exact transfer'):
    digest = row['sha256']
    path = path or CORPUS/row['corpus_file']
    add_version(digest,path)
    ar = row.get('archive_sha256','')
    member = row['member']
    db.execute('insert into occurrences(sha256,archive_sha256,archive_path,member,container_chain,source_root,origin) values(?,?,?,?,?,?,?)',(digest,ar,archive_routes.get(ar,''),member,chain,source,origin))
    bindings[(ar,member)] = digest
    for lane,pattern in LANES.items():
        if re.search(pattern,member,re.I):
            db.execute('insert or ignore into topics values(?,?,?)',(digest,lane,'source/member-name routing; not semantic classification'))
    counts['text_occurrences'] += 1

ledger_routes = [(CORPUS/'ledgers/source_files.jsonl.gz','01a03492-84a8-7d20-b7bf-667a02b24479')]
ledger_routes += [(p,p.parent.name) for p in sorted((CORPUS/'related_sources').glob('*/exact_source_files.jsonl.gz'))]
for p,sid in ledger_routes:
    with gzip.open(p,'rt',encoding='utf-8') as f:
        for line in f:
            occurrence(json.loads(line),sid)
db.commit()
print(json.dumps({'phase':'transferred texts structurally inventoried','unique_versions':len(known)}),flush=True)

seen_packages = set()
active_packages = set()
def expand_package(data, outer_hash, outer_member, chain):
    digest = hashlib.sha256(data).hexdigest()
    if digest in seen_packages:
        counts['duplicate_nested_packages'] += 1
        return 'byte-identical nested package already expanded; locate nested_packages by member hash'
    if digest in active_packages:
        return 'recursive package byte identity retained; expansion not repeated'
    active_packages.add(digest)
    try:
        with zipfile.ZipFile(io.BytesIO(data)) as package:
            infos = package.infolist()
            for info in infos:
                if info.is_dir():
                    continue
                counts['nested_member_occurrences'] += 1
                suffix = pathlib.PurePosixPath(info.filename).suffix.lower()
                nested_chain = chain+'!'+outer_member
                if suffix in TEXT_EXT:
                    raw = package.read(info)
                    h = hashlib.sha256(raw).hexdigest()
                    path = ROOT/'nested_source_blobs'/(h+suffix)
                    if not path.exists():
                        path.write_bytes(raw)
                    occurrence({'sha256':h,'archive_sha256':outer_hash,'member':info.filename},'nested_preserved_source',path,nested_chain,'new extraction from intact nested custody package')
                    counts['nested_text_occurrences'] += 1
                elif suffix == '.zip':
                    status = expand_package(package.read(info),outer_hash,info.filename,nested_chain)
                    db.execute('insert into opaque_members(archive_sha256,member,container_chain,bytes,suffix,status) values(?,?,?,?,?,?)',(outer_hash,info.filename,nested_chain,info.file_size,suffix,status))
                else:
                    db.execute('insert into opaque_members(archive_sha256,member,container_chain,bytes,suffix,status) values(?,?,?,?,?,?)',(outer_hash,info.filename,nested_chain,info.file_size,suffix,'exact nested member retained; nontext or unsupported format not semantically mined'))
            db.execute('insert into nested_packages values(?,?,?)',(digest,len(infos),'source-bearing text extracted; binary/unsupported members explicitly registered'))
        seen_packages.add(digest)
        return 'nested source text extracted; exact original ZIP retained'
    except (zipfile.BadZipFile,RuntimeError,NotImplementedError) as e:
        db.execute('insert into nested_packages values(?,?,?)',(digest,None,type(e).__name__+': '+str(e)))
        seen_packages.add(digest)
        return 'nested package unreadable in this attempt; exact original retained'
    finally:
        active_packages.remove(digest)

with gzip.open(ROOT/'ARCHIVE_MEMBER_COVERAGE.jsonl.gz','wt',encoding='utf-8') as coverage:
    for a in json.loads((WORK/'FINAL_CUSTODY_AUDIT.json').read_text())['archives']:
        archive = pathlib.Path(a['archive'])
        with zipfile.ZipFile(archive) as z:
            for info in z.infolist():
                counts['direct_archive_members'] += 1
                suffix = pathlib.PurePosixPath(info.filename).suffix.lower()
                digest = bindings.get((a['sha256'],info.filename))
                if digest:
                    status = 'exact text transferred; lexical structure indexed where supported; independent proof status remains passage-specific'
                elif suffix == '.zip':
                    data = z.read(info)
                    status = expand_package(data,a['sha256'],info.filename,'')
                    counts['direct_nested_package_occurrences'] += 1
                elif info.filename.startswith(('histories/','history/','database_rows/')):
                    status = 'exact history/projection preserved; full semantic extraction of mathematical tool calls and dialogue remains incomplete'
                elif suffix in TEXT_EXT:
                    data = z.read(info)
                    digest = hashlib.sha256(data).hexdigest()
                    path = ROOT/'nested_source_blobs'/(digest+suffix)
                    if not path.exists():path.write_bytes(data)
                    occurrence({'sha256':digest,'archive_sha256':a['sha256'],'member':info.filename},'additional_direct_text',path,origin='new extraction of previously untransferred direct text')
                    status = 'previously untransferred direct text now captured and structurally inventoried; not independently audited'
                    counts['additional_direct_text'] += 1
                else:
                    status = 'exact custody retained; nontext/unsupported/compressed data not semantically mined'
                    db.execute('insert into opaque_members(archive_sha256,member,container_chain,bytes,suffix,status) values(?,?,?,?,?,?)',(a['sha256'],info.filename,'',info.file_size,suffix,status))
                coverage.write(json.dumps({'archive':str(archive),'archive_sha256':a['sha256'],'member':info.filename,'bytes':info.file_size,'crc32':info.CRC,'text_sha256':digest,'status':status},ensure_ascii=False)+'\n')
        db.commit()
        print(json.dumps({'phase':'archive registered','archive':archive.name,'direct_members_so_far':counts['direct_archive_members'],'unique_versions':len(known)}),flush=True)

for digest in known:
    if not db.execute('select 1 from topics where sha256=?',(digest,)).fetchone():
        db.execute('insert into topics values(?,?,?)',(digest,'unclassified','retained without forced topic assignment'))
db.commit()
lanes = {lane:db.execute('select count(*) from topics where lane=?',(lane,)).fetchone()[0] for lane in list(LANES)+['unclassified']}
counts['unique_versions_including_undecoded'] = db.execute('select count(*) from versions').fetchone()[0]
counts['nested_unique_packages'] = db.execute('select count(*) from nested_packages').fetchone()[0]
counts['opaque_member_records'] = db.execute('select count(*) from opaque_members').fetchone()[0]
counts['literal_reference_records'] = db.execute('select count(*) from references_found').fetchone()[0]
counts['catalogue_spans'] = db.execute('select count(*) from spans').fetchone()[0]
integrity = db.execute('pragma integrity_check').fetchone()[0]
assert integrity == 'ok'
db.close()
result = {'scope':'all nine verified direct custody ZIPs; complete registered direct-member set; recursively expanded nested ZIP byte versions; previously transferred and newly extracted source text','counts':dict(counts),'overlapping_routing_lanes':lanes,'sqlite_integrity':integrity,'audit_limitations':['literal TeX extraction does not expand macros, validate active branches, resolve every include convention, or prove claims','all binary/unsupported/compressed members remain registered with exact custody access','history text is preserved; complete mathematical mining of every raw tool call and projection is unfinished','2039 first-source original histories remain unlocated; projected records do not replace original bytes','source-era proof claims and duplicate versions do not count as newly accepted theorems'],'all_original_custody_unchanged':True}
(ROOT/'CATALOGUE_RECEIPT.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(result,ensure_ascii=False),flush=True)
