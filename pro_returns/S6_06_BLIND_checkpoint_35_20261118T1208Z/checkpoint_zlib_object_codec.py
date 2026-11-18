"""Byte-exact object transport using complete reproducible zlib streams.

Literal bytes are retained verbatim. A stream is transformed only after a
valid zlib header, successful checksum/eof decode, and byte-identical full
recompression. The decoder checks each stream and the complete object.
"""
from pathlib import Path
import hashlib
import io
import re
import struct
import zlib

MAGIC=b'S6ZLIBOBJECT1\0'
HEADER=re.compile(rb'[\x08\x18\x28\x38\x48\x58\x68\x78].',re.S)
MAX_PLAIN=64*1024*1024
STREAM=struct.Struct('>BBBBQQ32s')
CACHE={}

def sha(path):
    with Path(path).open('rb') as source:
        return hashlib.file_digest(source,'sha256').hexdigest()

def complete_stream(data,start):
    cmf,flg=data[start:start+2]
    if (cmf*256+flg)%31 or flg&32:
        return None
    decoder=zlib.decompressobj(15)
    position=start
    blocks=[];amount=0
    try:
        while position<len(data):
            block=data[position:position+65536]
            plain=decoder.decompress(block,MAX_PLAIN+1-amount)
            blocks.append(plain);amount+=len(plain)
            if amount>MAX_PLAIN:
                return None
            if decoder.eof:
                end=position+len(block)-len(decoder.unused_data)
                assert not decoder.unconsumed_tail
                return end,b''.join(blocks)
            if decoder.unconsumed_tail:
                return None
            position+=len(block)
    except zlib.error:
        return None
    return None

def matching_parameters(raw,plain):
    if raw in CACHE:
        return CACHE[raw]
    hint=raw[1]>>6
    levels={0:[1,0],1:[5,4,3,2],2:[6],3:[9,8,7]}[hint]
    levels+= [level for level in (6,9,1,5,4,7,8,2,3,0) if level not in levels]
    window=8+(raw[0]>>4)
    for level in levels:
        compressor=zlib.compressobj(level,zlib.DEFLATED,window,8,zlib.Z_DEFAULT_STRATEGY)
        encoded=compressor.compress(plain)+compressor.flush(zlib.Z_FINISH)
        if encoded==raw:
            result=(level,window,8,zlib.Z_DEFAULT_STRATEGY)
            CACHE[raw]=result
            return result
    return None

def encode_bytes(data):
    out=io.BytesIO()
    out.write(MAGIC+struct.pack('>Q',len(data))+hashlib.sha256(data).digest())
    position=literal=0;rows=[];unmatched=small=0
    def emit_literal(body):
        if body:out.write(b'L'+struct.pack('>Q',len(body))+body)
    while position+2<=len(data):
        match=HEADER.search(data,position)
        if match is None:break
        start=match.start()
        decoded=complete_stream(data,start)
        if decoded is None:
            position=start+1
            continue
        end,plain=decoded
        raw=data[start:end]
        position=end
        if len(raw)<256:
            small+=1
            continue
        params=matching_parameters(raw,plain)
        if params is None:
            unmatched+=1
            continue
        emit_literal(data[literal:start])
        digest=hashlib.sha256(raw).digest()
        out.write(b'Z'+STREAM.pack(*params,len(raw),len(plain),digest)+plain)
        rows.append({'original_offset':start,'original_stream_bytes':len(raw),
                     'plain_bytes':len(plain),'parameters':list(params),
                     'original_stream_sha256':digest.hex()})
        literal=end
    emit_literal(data[literal:]);out.write(b'E')
    return out.getvalue(),{'stream_count':len(rows),'streams':rows,
                          'small_complete_streams_retained_raw':small,
                          'unmatched_complete_streams_retained_raw':unmatched,
                          'transformed_original_stream_bytes':sum(r['original_stream_bytes'] for r in rows),
                          'transformed_plain_bytes':sum(r['plain_bytes'] for r in rows)}

def read_exact(source,amount):
    data=source.read(amount)
    if len(data)!=amount:raise ValueError('Truncated exact object encoding')
    return data

def decode_stream(source,target,chunk_size=65537):
    assert read_exact(source,len(MAGIC))==MAGIC
    original_size,=struct.unpack('>Q',read_exact(source,8))
    original_hash=read_exact(source,32)
    whole=hashlib.sha256();whole_size=0
    def emit(data):
        nonlocal whole_size
        target.write(data);whole.update(data);whole_size+=len(data)
        assert whole_size<=original_size
    while True:
        opcode=read_exact(source,1)
        if opcode==b'E':break
        if opcode==b'L':
            remaining,=struct.unpack('>Q',read_exact(source,8))
            while remaining:
                amount=min(chunk_size,remaining);emit(read_exact(source,amount));remaining-=amount
        elif opcode==b'Z':
            level,window,mem,strategy,raw_size,plain_size,raw_hash=STREAM.unpack(read_exact(source,STREAM.size))
            compressor=zlib.compressobj(level,zlib.DEFLATED,window,mem,strategy)
            digest=hashlib.sha256();amount=0
            remaining=plain_size
            while remaining:
                count=min(chunk_size,remaining)
                block=compressor.compress(read_exact(source,count));remaining-=count
                emit(block);digest.update(block);amount+=len(block)
            block=compressor.flush(zlib.Z_FINISH)
            emit(block);digest.update(block);amount+=len(block)
            assert amount==raw_size and digest.digest()==raw_hash
        else:raise ValueError('Unknown exact object opcode')
    assert source.read()==b''
    assert whole_size==original_size and whole.digest()==original_hash

def decode_bytes(data,chunk_size=65537):
    target=io.BytesIO();decode_stream(io.BytesIO(data),target,chunk_size)
    return target.getvalue()

def decode_file(source,destination):
    with Path(source).open('rb') as encoded,Path(destination).open('wb') as original:
        decode_stream(encoded,original)
