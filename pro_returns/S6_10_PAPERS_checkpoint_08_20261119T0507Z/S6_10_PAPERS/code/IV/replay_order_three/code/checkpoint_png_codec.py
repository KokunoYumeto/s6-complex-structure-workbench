"""Reversible PNG transport: preserve chunks and regenerate verified IDAT bytes.

This is a byte-storage codec, not an image edit. The original PNG is verified
both when encoded and when restored. The required zlib version is recorded.
Unmatched streams are retained as raw original PNGs by the calling packer.
"""
import base64, hashlib, json, struct, zlib

MAGIC = b'S6PNG01\0'

def digest(data):
    return hashlib.sha256(data).hexdigest()

def compress(raw, level, strategy, mem_level=8):
    c = zlib.compressobj(level, zlib.DEFLATED, 15, mem_level, strategy)
    return c.compress(raw) + c.flush()

def filter_pixels(pixels, filters, stride, bpp):
    output=bytearray(); previous=bytes(stride)
    for y,kind in enumerate(filters):
        row=pixels[y*stride:(y+1)*stride];assert len(row)==stride
        output.append(kind)
        if kind==0: filtered=row
        elif kind==1:
            filtered=row[:bpp]+bytes((row[i]-row[i-bpp])&255 for i in range(bpp,stride))
        elif kind==2: filtered=bytes((v-previous[i])&255 for i,v in enumerate(row))
        elif kind==3:
            filtered=bytes((v-(((row[i-bpp] if i>=bpp else 0)+previous[i])//2))&255 for i,v in enumerate(row))
        elif kind==4:
            values=bytearray(stride)
            for i,v in enumerate(row):
                a=row[i-bpp] if i>=bpp else 0;b=previous[i];c=previous[i-bpp] if i>=bpp else 0
                p=a+b-c;pa=abs(p-a);pb=abs(p-b);pc=abs(p-c)
                q=a if pa<=pb and pa<=pc else b if pb<=pc else c
                values[i]=(v-q)&255
            filtered=values
        else:raise ValueError('Unknown PNG filter')
        output.extend(filtered);previous=row
    return bytes(output)

def encode(data, pixels=False):
    assert data[:8] == b'\x89PNG\r\n\x1a\n'
    chunks = []; idat = bytearray(); offset = 8
    while offset < len(data):
        length = struct.unpack('>I', data[offset:offset+4])[0]
        block = data[offset:offset+12+length]
        assert len(block) == length+12
        if block[4:8] == b'IDAT':
            chunks.append({'idat': length})
            idat.extend(block[8:-4])
        else:
            chunks.append({'bytes': base64.b64encode(block).decode('ascii')})
        offset += length+12
    assert offset == len(data)
    idat = bytes(idat); raw = zlib.decompress(idat); parameter = None
    for level, strategy, mem_level in [(6,0,8),(9,1,8),(6,1,9),(9,0,8),(6,1,8),(1,0,8),(1,1,8),(6,3,8),(9,3,8)]:
        if compress(raw, level, strategy, mem_level) == idat:
            parameter = [level, strategy, mem_level]; break
    if parameter is None:
        return None
    header = {'chunks':chunks,'parameter':parameter,'zlib_version':zlib.ZLIB_RUNTIME_VERSION,
              'idat_sha256':digest(idat),'png_sha256':digest(data),'png_bytes':len(data)}
    if pixels:
        import io
        from PIL import Image
        width,height,depth,color,compression,filter_method,interlace=struct.unpack('>IIBBBBB',data[16:29])
        modes={0:('L',1),2:('RGB',3),4:('LA',2),6:('RGBA',4)}
        if depth==8 and interlace==0 and color in modes:
            mode,bpp=modes[color];stride=width*bpp
            filters=bytes(raw[y*(stride+1)] for y in range(height))
            im=Image.open(io.BytesIO(data));assert im.mode==mode
            unfiltered=im.tobytes();assert filter_pixels(unfiltered,filters,stride,bpp)==raw
            header.update(layout='pixels',filters=base64.b64encode(filters).decode('ascii'),stride=stride,bpp=bpp)
            raw=unfiltered
    meta = json.dumps(header,separators=(',',':')).encode()
    encoded = MAGIC + struct.pack('>I',len(meta)) + meta + raw
    assert decode(encoded) == data
    return encoded

def decode(data):
    assert data[:8] == MAGIC
    n = struct.unpack('>I',data[8:12])[0]
    meta = json.loads(data[12:12+n]); raw = data[12+n:]
    if meta.get('layout')=='pixels':
        raw=filter_pixels(raw,base64.b64decode(meta['filters']),meta['stride'],meta['bpp'])
    packed = compress(raw,*meta['parameter'])
    assert digest(packed) == meta['idat_sha256'], ('Exact PNG restoration requires a zlib '
        'encoder matching '+meta['zlib_version']+'; current '+zlib.ZLIB_RUNTIME_VERSION)
    output = bytearray(b'\x89PNG\r\n\x1a\n'); offset = 0
    for chunk in meta['chunks']:
        if 'idat' in chunk:
            n = chunk['idat']; piece = packed[offset:offset+n]; offset += n
            assert len(piece) == n
            body = b'IDAT'+piece
            output.extend(struct.pack('>I',n)+body+struct.pack('>I',zlib.crc32(body)&0xffffffff))
        else:
            output.extend(base64.b64decode(chunk['bytes']))
    assert offset == len(packed)
    output = bytes(output)
    assert len(output) == meta['png_bytes'] and digest(output) == meta['png_sha256']
    return output
