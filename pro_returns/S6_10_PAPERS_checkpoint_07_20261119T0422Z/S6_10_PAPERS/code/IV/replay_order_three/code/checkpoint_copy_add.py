"""Lossless byte-exact copy/add patches; decoder uses only Python stdlib."""
import hashlib, struct

MAGIC = b'S6COPYADD1\x00'

def encode(base, target):
    block = 32
    index = {}
    for pos in range(0, len(base)-block+1, 16):
        key = base[pos:pos+block]
        found = index.setdefault(key, [])
        if len(found) < 4:
            found.append(pos)
    output = bytearray(MAGIC + hashlib.sha256(base).digest() + struct.pack('>Q',len(target)))
    cursor = literal = 0
    copies = copy_bytes = 0
    while cursor+block <= len(target):
        best_pos = best_len = 0
        for pos in index.get(target[cursor:cursor+block], ()):
            length = block
            maximum = min(len(base)-pos, len(target)-cursor)
            while length+4096 <= maximum and base[pos+length:pos+length+4096] == target[cursor+length:cursor+length+4096]:
                length += 4096
            low, high = 0, min(4096, maximum-length)
            while low < high:
                middle = (low+high+1)//2
                if base[pos+length:pos+length+middle] == target[cursor+length:cursor+length+middle]:
                    low = middle
                else:
                    high = middle-1
            length += low
            if length > best_len:
                best_pos, best_len = pos, length
        if best_len < 64:
            cursor += 1
            continue
        if literal < cursor:
            data = target[literal:cursor]
            output += b'L' + struct.pack('>Q',len(data)) + data
        output += b'C' + struct.pack('>QQ',best_pos,best_len)
        copies += 1
        copy_bytes += best_len
        cursor += best_len
        literal = cursor
    if literal < len(target):
        data = target[literal:]
        output += b'L' + struct.pack('>Q',len(data)) + data
    return bytes(output), {'copies':copies,'copy_bytes':copy_bytes,'literal_bytes':len(target)-copy_bytes,'patch_bytes':len(output)}

def decode(base, patch):
    assert patch.startswith(MAGIC)
    cursor = len(MAGIC)
    assert hashlib.sha256(base).digest() == patch[cursor:cursor+32]
    cursor += 32
    size, = struct.unpack_from('>Q',patch,cursor)
    cursor += 8
    output = bytearray()
    while cursor < len(patch):
        opcode = patch[cursor:cursor+1]
        cursor += 1
        if opcode == b'C':
            offset,length = struct.unpack_from('>QQ',patch,cursor)
            cursor += 16
            assert offset+length <= len(base)
            output += base[offset:offset+length]
        elif opcode == b'L':
            length, = struct.unpack_from('>Q',patch,cursor)
            cursor += 8
            assert cursor+length <= len(patch)
            output += patch[cursor:cursor+length]
            cursor += length
        else:
            raise ValueError('Invalid copy/add opcode')
        assert len(output) <= size
    assert len(output) == size
    return bytes(output)
