"""Lossless compact receipt; --unpack reconstructs the census's original bytes.

Format after gzip decoding: records [gap: little-endian uint16, multiplicity:
uint8], with initial previous height 0. A height equals previous+gap.
Every sorted height from the original u32 stream is reproduced exactly.
"""
import gzip,hashlib,sys
from pathlib import Path
import numpy as np
p=Path(__file__).parent
raw=p/'A_census_1e9.u32';packed=p/'A_census_1e9.d16m8.gz'
expected='29bc345c303f0f1885b13f459669411fc4202a43d3ed95509844f8fac2c65a48'
dt=np.dtype([('gap','<u2'),('multiplicity','u1')])
if '--unpack' in sys.argv:
 with gzip.open(packed,'rb') as f: a=np.frombuffer(f.read(),dtype=dt)
 h=np.cumsum(a['gap'],dtype=np.uint64)
 data=np.repeat(h,a['multiplicity']).astype('<u4').tobytes()
 assert hashlib.sha256(data).hexdigest()==expected
 raw.write_bytes(data)
 print('unpacked_bytes',len(data),'sha256',expected,'PASS')
else:
 h=np.fromfile(raw,dtype='<u4')
 u,m=np.unique(h,return_counts=True);g=np.diff(u,prepend=0)
 assert 0<g.min()<=g.max()<65536 and 0<m.min()<=m.max()<256
 a=np.empty(len(u),dtype=dt);a['gap']=g;a['multiplicity']=m
 with gzip.open(packed,'wb',compresslevel=9) as f:f.write(a.tobytes())
 assert np.array_equal(np.repeat(np.cumsum(a['gap'],dtype=np.uint64),a['multiplicity']),h)
 assert hashlib.sha256(h.tobytes()).hexdigest()==expected
 print('format gap_u16_multiplicity_u8_little_endian_gzip')
 print('occupied_heights',len(u),'maximum_gap',g.max(),'maximum_multiplicity',m.max())
 print('packed_bytes',packed.stat().st_size,'expanded_bytes',raw.stat().st_size)
 print('expanded_sha256',expected,'exact_round_trip PASS')
