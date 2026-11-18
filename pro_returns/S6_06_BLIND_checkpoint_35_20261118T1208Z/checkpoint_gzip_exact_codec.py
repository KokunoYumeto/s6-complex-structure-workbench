"""Reconstruct an original gzip object from JSON and exact gzip/DEFLATE data.

The encoded record retains the complete original gzip header and trailer.
The raw DEFLATE parameter tuple is admitted only after byte equality with
the original stream. Decoding checks both the plain and complete gzip SHA.
"""
from pathlib import Path
import hashlib
import struct
import zlib


def sha(path):
    with Path(path).open('rb') as source:
        return hashlib.file_digest(source, 'sha256').hexdigest()


def header_end(data):
    assert data[:3] == b'\x1f\x8b\x08'
    flags = data[3]
    assert flags & 0xe0 == 0
    position = 10
    if flags & 4:
        length = struct.unpack_from('<H', data, position)[0]
        position += 2 + length
    for bit in (8, 16):
        if flags & bit:
            position = data.index(b'\0', position) + 1
    if flags & 2:
        expected = struct.unpack_from('<H', data, position)[0]
        assert zlib.crc32(data[:position]) & 0xffff == expected
        position += 2
    assert position < len(data) - 8
    return position


def encode_file(original, plain):
    original, plain = Path(original), Path(plain)
    data = original.read_bytes()
    position = header_end(data)
    header, payload, trailer = data[:position], data[position:-8], data[-8:]
    decoder = zlib.decompressobj(-15)
    digest = hashlib.sha256()
    amount = crc = 0
    with plain.open('wb') as target:
        for offset in range(0, len(payload), 1024 * 1024):
            block = decoder.decompress(payload[offset:offset + 1024 * 1024])
            target.write(block); digest.update(block)
            amount += len(block); crc = zlib.crc32(block, crc)
        block = decoder.flush()
        target.write(block); digest.update(block)
        amount += len(block); crc = zlib.crc32(block, crc)
    assert decoder.eof and not decoder.unused_data and not decoder.unconsumed_tail
    assert struct.unpack('<II', trailer) == (crc & 0xffffffff, amount & 0xffffffff)
    match = None
    attempts = []
    for level in (6, 9, 1, 5, 4, 7, 8, 2, 3, 0):
        compressor = zlib.compressobj(level, zlib.DEFLATED, -15, 8, zlib.Z_DEFAULT_STRATEGY)
        cursor = 0
        equal = True
        with plain.open('rb') as source:
            for block in iter(lambda: source.read(1024 * 1024), b''):
                compressed = compressor.compress(block)
                if compressed != payload[cursor:cursor + len(compressed)]:
                    equal = False
                    break
                cursor += len(compressed)
        if equal:
            compressed = compressor.flush(zlib.Z_FINISH)
            equal = compressed == payload[cursor:cursor + len(compressed)]
            cursor += len(compressed)
            equal = equal and cursor == len(payload)
        attempts.append({'level': level, 'memLevel': 8, 'strategy': 0,
                         'exact_raw_stream': equal})
        if equal:
            match = {'level': level, 'method': zlib.DEFLATED, 'wbits': -15,
                     'memLevel': 8, 'strategy': zlib.Z_DEFAULT_STRATEGY}
            break
    assert match is not None, 'No exact DEFLATE parameter match; original is retained.'
    return {'codec': 'gzip_exact_v1', 'header_hex': header.hex(),
            'trailer_hex': trailer.hex(), 'deflate': match,
            'zlib_compile_version': zlib.ZLIB_VERSION,
            'zlib_runtime_version': zlib.ZLIB_RUNTIME_VERSION,
            'plain_bytes': amount, 'plain_sha256': digest.hexdigest(),
            'raw_deflate_bytes': len(payload),
            'raw_deflate_sha256': hashlib.sha256(payload).hexdigest(),
            'original_bytes': len(data),
            'original_sha256': hashlib.sha256(data).hexdigest(),
            'parameter_trials': attempts}


def decode_file(plain, destination, record, chunk_size=65537):
    plain, destination = Path(plain), Path(destination)
    assert record['codec'] == 'gzip_exact_v1'
    assert plain.stat().st_size == record['plain_bytes']
    assert sha(plain) == record['plain_sha256']
    header, trailer = bytes.fromhex(record['header_hex']), bytes.fromhex(record['trailer_hex'])
    compressor = zlib.compressobj(**record['deflate'])
    digest = hashlib.sha256()
    amount = crc = 0
    raw_digest = hashlib.sha256()
    raw_amount = 0
    with plain.open('rb') as source, destination.open('wb') as target:
        target.write(header); digest.update(header)
        for block in iter(lambda: source.read(chunk_size), b''):
            amount += len(block); crc = zlib.crc32(block, crc)
            compressed = compressor.compress(block)
            target.write(compressed); digest.update(compressed)
            raw_digest.update(compressed); raw_amount += len(compressed)
        compressed = compressor.flush(zlib.Z_FINISH)
        target.write(compressed); digest.update(compressed)
        raw_digest.update(compressed); raw_amount += len(compressed)
        target.write(trailer); digest.update(trailer)
    assert struct.unpack('<II', trailer) == (crc & 0xffffffff, amount & 0xffffffff)
    assert raw_amount == record['raw_deflate_bytes']
    assert raw_digest.hexdigest() == record['raw_deflate_sha256']
    assert destination.stat().st_size == record['original_bytes']
    assert digest.hexdigest() == record['original_sha256']

