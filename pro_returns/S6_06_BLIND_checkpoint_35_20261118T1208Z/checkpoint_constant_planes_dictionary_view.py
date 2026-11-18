"""Exact original-row access through a fully verified constant-plane file.

The encoded dictionary is stored once. Before any row access, its entire
encoded, intermediate RGB and original dictionary hashes are verified.
Each unchanged row ID then resolves to its original byte string by the
same two inverse maps. A bounded cache never changes those bytes.
"""
import array,hashlib,io,os,struct
from collections import OrderedDict
from checkpoint_rgb_constant_planes_codec import MAGIC,RGBReader,read_inverse
from checkpoint_png_rgb_dictionary import decode_stream as decode_original,inverse as inverse_rgb_row
from checkpoint_png_rows_codec import MAGIC as PNG_ROWS_MAGIC

class HashReader:
    def __init__(self,source,sink=None):
        self.source=source;self.sink=sink;self.bytes=0;self.hash=hashlib.sha256()
    def read(self,n=-1):
        data=self.source.read(n)
        if self.sink is not None:self.sink.write(data)
        self.bytes+=len(data);self.hash.update(data);return data

class HashSink:
    def __init__(self):self.bytes=0;self.hash=hashlib.sha256()
    def write(self,data):
        self.bytes+=len(data);self.hash.update(data);return len(data)

def store_verified_dictionary(source,destination,row,cache_bytes=32*1024*1024):
    """Store exact encoded bytes and verify both complete inverse streams."""
    with open(destination,'xb') as encoded_sink:
        encoded=HashReader(source,encoded_sink)
        rgb=RGBReader(encoded);middle=HashReader(rgb);original=HashSink()
        count=decode_original(middle,original)
        assert count==rgb.rows==row['rows']
        assert (encoded.bytes,encoded.hash.hexdigest())==(row['encoded_bytes'],row['encoded_sha256'])
        assert (middle.bytes,middle.hash.hexdigest())==(row['prior_rgb_bytes'],row['prior_rgb_sha256'])
        assert (original.bytes,original.hash.hexdigest())==(row['original_bytes'],row['original_sha256'])
    receipt={'status':'PASS_COMPLETE_ENCODED_RGB_ORIGINAL_DICTIONARY',
             'encoded_bytes':encoded.bytes,'encoded_sha256':encoded.hash.hexdigest(),
             'prior_rgb_bytes':middle.bytes,'prior_rgb_sha256':middle.hash.hexdigest(),
             'original_bytes':original.bytes,'original_sha256':original.hash.hexdigest(),
             'rows':count}
    return DictionaryView(destination,row,receipt,cache_bytes)

class DictionaryView:
    def __init__(self,path,row,receipt,cache_bytes=32*1024*1024):
        assert receipt['status']=='PASS_COMPLETE_ENCODED_RGB_ORIGINAL_DICTIONARY'
        for key in ('encoded_bytes','encoded_sha256','prior_rgb_bytes','prior_rgb_sha256',
                    'original_bytes','original_sha256','rows'):
            assert receipt[key]==row[key]
        self.path=os.fspath(path);self.receipt=dict(receipt);self.closed=False
        self.stream=open(path,'rb');stat=os.fstat(self.stream.fileno())
        assert stat.st_size==row['encoded_bytes']
        assert hashlib.file_digest(self.stream,'sha256').hexdigest()==row['encoded_sha256']
        self.stream.seek(0);assert self.stream.read(len(MAGIC))==MAGIC
        self.offsets=array.array('Q');self.lengths=array.array('I')
        while True:
            header=self.stream.read(4)
            if not header:break
            assert len(header)==4
            length=struct.unpack('>I',header)[0];skip=length%3;k=(length-skip)//3
            self.offsets.append(self.stream.tell());self.lengths.append(length)
            prefix=self.stream.read(skip);flag=self.stream.read(1)
            assert len(prefix)==skip and len(flag)==1 and flag[0]<8
            assert k or flag[0]==0
            payload=sum(1 if flag[0]&(1<<j) else k for j in range(3))
            assert self.stream.tell()+payload<=stat.st_size
            self.stream.seek(payload,1)
        assert self.stream.tell()==stat.st_size and len(self.lengths)==row['rows']
        # Consecutive row payload offsets differ by the previous payload and
        # the next four-byte length. The final sentinel preserves that formula.
        self.offsets.append(stat.st_size+4)
        self.snapshot=(stat.st_dev,stat.st_ino,stat.st_size,stat.st_mtime_ns)
        self.cache=OrderedDict();self.cache_bytes=0;self.cache_limit=cache_bytes
        assert cache_bytes>=0

    def check_unchanged(self):
        assert not self.closed
        stat=os.fstat(self.stream.fileno())
        assert (stat.st_dev,stat.st_ino,stat.st_size,stat.st_mtime_ns)==self.snapshot

    def row(self,index):
        assert not self.closed and 0<=index<len(self.lengths)
        if index in self.cache:
            value=self.cache.pop(index);self.cache[index]=value;return value
        length=self.lengths[index];offset=self.offsets[index]
        amount=self.offsets[index+1]-offset-4
        packed=os.pread(self.stream.fileno(),amount,offset)
        assert len(packed)==amount
        source=io.BytesIO(packed);rgb=read_inverse(source,length)
        assert source.read(1)==b''
        value=inverse_rgb_row(rgb);assert len(value)==length
        if length<=self.cache_limit:
            while self.cache and (self.cache_bytes+length>self.cache_limit or len(self.cache)>=8192):
                _,old=self.cache.popitem(last=False);self.cache_bytes-=len(old)
            self.cache[index]=value;self.cache_bytes+=length
        return value

    def close(self):
        if self.closed:return
        self.cache.clear();self.cache_bytes=0
        self.stream.close();self.closed=True

def decode_file(encoded_path,dest_path,dictionary):
    """Retain the PNG row-object decoder; replace only its row-read source."""
    dictionary.check_unchanged()
    source=open(encoded_path,'rb')
    with source,open(dest_path,'wb') as sink:
        assert source.read(len(PNG_ROWS_MAGIC))==PNG_ROWS_MAGIC
        original_size=struct.unpack('>Q',source.read(8))[0]
        original_hash=source.read(32)
        prefix_size=struct.unpack('>I',source.read(4))[0]
        prefix=source.read(prefix_size)
        if len(prefix)!=prefix_size:raise ValueError('Truncated original header')
        count=struct.unpack('>I',source.read(4))[0]
        digest=hashlib.sha256();digest.update(prefix);sink.write(prefix)
        size=len(prefix)
        for _ in range(count):
            raw=source.read(4)
            if len(raw)!=4:raise ValueError('Truncated row index')
            index=struct.unpack('>I',raw)[0]
            if index>=len(dictionary.lengths):raise ValueError('Invalid row index')
            row=dictionary.row(index)
            if len(row)!=dictionary.lengths[index]:raise ValueError('Truncated dictionary')
            sink.write(row);digest.update(row);size+=len(row)
        if source.read(1):raise ValueError('Trailing row object bytes')
        assert size==original_size and digest.digest()==original_hash
    dictionary.check_unchanged()
