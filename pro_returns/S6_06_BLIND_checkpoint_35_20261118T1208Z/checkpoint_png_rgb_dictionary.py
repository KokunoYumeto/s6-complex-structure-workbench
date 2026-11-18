"""Byte-exact row plane/difference layer, independent of pixel semantics."""
import struct
from pathlib import Path
MAGIC=b'S6RGBROW1\0'
ORIGINAL_MAGIC=b'S6PNGROWDICT1\0'
def forward(row):
    n=len(row);skip=n%3;body=row[skip:]
    r,g,b=body[0::3],body[1::3],body[2::3]
    return row[:skip]+g+bytes((a-c)&255 for a,c in zip(r,g))+bytes((a-c)&255 for a,c in zip(b,g))
def inverse(row):
    n=len(row);skip=n%3;k=(n-skip)//3
    g=row[skip:skip+k];r=row[skip+k:skip+2*k];b=row[skip+2*k:]
    out=bytearray(n);out[:skip]=row[:skip]
    out[skip::3]=bytes((a+c)&255 for a,c in zip(r,g))
    out[skip+1::3]=g
    out[skip+2::3]=bytes((a+c)&255 for a,c in zip(b,g))
    return bytes(out)
def decode_stream(source,sink):
    assert source.read(len(MAGIC))==MAGIC
    sink.write(ORIGINAL_MAGIC);rows=0
    while True:
        header=source.read(4)
        if not header:break
        assert len(header)==4
        n=struct.unpack('>I',header)[0];row=source.read(n);assert len(row)==n
        sink.write(header);sink.write(inverse(row));rows+=1
    return rows
def decode_file(source,destination):
    with Path(source).open('rb')as a,Path(destination).open('xb')as b:return decode_stream(a,b)
