"""Exact constant-plane representation of the retained RGB-row dictionary.

Each original row length, prefix, plane order and row index are retained.
A constant plane is represented by its exact byte; its original length is
computed from the retained row length. Other planes are copied verbatim.
"""
import struct
MAGIC=b'S6RGBCONST1\0'
RGB_MAGIC=b'S6RGBROW1\0'
def forward(row):
 n=len(row);skip=n%3;k=(n-skip)//3;flags=0;parts=[]
 for j in range(3):
  plane=row[skip+j*k:skip+(j+1)*k]
  if k and plane.count(plane[0])==k:flags|=1<<j;parts.append(plane[:1])
  else:parts.append(plane)
 return row[:skip]+bytes([flags])+b''.join(parts)
def read_inverse(source,n):
 skip=n%3;k=(n-skip)//3;prefix=source.read(skip);flag=source.read(1);assert len(prefix)==skip and len(flag)==1 and flag[0]<8
 parts=[prefix]
 for j in range(3):
  amount=1 if flag[0]&(1<<j) else k;plane=source.read(amount);assert len(plane)==amount
  if flag[0]&(1<<j):assert k;plane*=k
  parts.append(plane)
 return b''.join(parts)
def decode_rgb_stream(source,sink):
 assert source.read(len(MAGIC))==MAGIC;sink.write(RGB_MAGIC);count=0
 while True:
  h=source.read(4)
  if not h:break
  assert len(h)==4;n=struct.unpack('>I',h)[0];sink.write(h);sink.write(read_inverse(source,n));count+=1
 return count

class RGBReader:
 """Streaming exact inverse into the prior RGB dictionary byte stream."""
 def __init__(self,source):
  self.source=source;assert source.read(len(MAGIC))==MAGIC
  self.buffer=RGB_MAGIC;self.finished=False;self.rows=0
 def read(self,n=-1):
  assert n>=0
  parts=[self.buffer];amount=len(self.buffer)
  while amount<n and not self.finished:
   h=self.source.read(4)
   if not h:self.finished=True;break
   assert len(h)==4;length=struct.unpack('>I',h)[0];row=read_inverse(self.source,length);parts.extend([h,row]);amount+=4+length;self.rows+=1
  value=b''.join(parts);self.buffer=value[n:];return value[:n]
