"""Exact byte dictionary for existing PNG-codec filtered scanline members.

No PNG field or compressed stream is changed.  This layer restores the
complete original PNG-codec member before its existing decoder executes.
Only the Python standard library is required for decoding.
"""
import array
import hashlib
import os
import struct

MAGIC=b'S6PNGROWS1\0'
DICT_MAGIC=b'S6PNGROWDICT1\0'
_CACHE={}

def close_dictionaries():
    """Release shared file descriptors before deleting decoded dictionaries."""
    for stream,_,_ in _CACHE.values():stream.close()
    _CACHE.clear()

def _dictionary(path):
    key=os.fspath(path)
    if key in _CACHE:return _CACHE[key]
    stream=open(path,'rb')
    assert stream.read(len(DICT_MAGIC))==DICT_MAGIC
    offsets=array.array('Q');lengths=array.array('I')
    while True:
        raw=stream.read(4)
        if not raw:break
        if len(raw)!=4:raise ValueError('Truncated row length')
        length=struct.unpack('>I',raw)[0]
        offsets.append(stream.tell());lengths.append(length)
        stream.seek(length,1)
    if stream.tell()!=os.fstat(stream.fileno()).st_size:
        raise ValueError('Truncated dictionary row')
    _CACHE[key]=(stream,offsets,lengths)
    return _CACHE[key]

def decode_file(encoded_path,dest_path,dictionary_path):
    source=open(encoded_path,'rb')
    with source,open(dest_path,'wb') as sink:
        assert source.read(len(MAGIC))==MAGIC
        original_size=struct.unpack('>Q',source.read(8))[0]
        original_hash=source.read(32)
        prefix_size=struct.unpack('>I',source.read(4))[0]
        prefix=source.read(prefix_size)
        if len(prefix)!=prefix_size:raise ValueError('Truncated original header')
        count=struct.unpack('>I',source.read(4))[0]
        stream,offsets,lengths=_dictionary(dictionary_path)
        digest=hashlib.sha256();digest.update(prefix);sink.write(prefix)
        size=len(prefix)
        for _ in range(count):
            raw=source.read(4)
            if len(raw)!=4:raise ValueError('Truncated row index')
            index=struct.unpack('>I',raw)[0]
            if index>=len(offsets):raise ValueError('Invalid row index')
            row=os.pread(stream.fileno(),lengths[index],offsets[index])
            if len(row)!=lengths[index]:raise ValueError('Truncated dictionary')
            sink.write(row);digest.update(row);size+=len(row)
        if source.read(1):raise ValueError('Trailing row object bytes')
        assert size==original_size and digest.digest()==original_hash

