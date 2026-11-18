"""Exact new streaming branch for the inherited checkpoint restorer.

Only the dictionary stream dispatcher is extended. All PNG, copy/add,
gzip, zlib, content and final original-file verification code is retained.
"""

def patch(source):
    before = "streaming={row['encoded_name']:(i,row)for i,row in enumerate(rows)if row['codec']=='png_rgb_dictionary_v1'}"
    after = "streaming={row['encoded_name']:(i,row)for i,row in enumerate(rows)if row['codec']in('png_rgb_dictionary_v1','png_rgb_constant_planes_v1')}"
    assert source.count(before) == 1
    source = source.replace(before, after)
    before = """     reader=HashReader(source)
     with source,original.open('xb')as sink:decoded_rows=decode_rgb_dictionary(reader,sink)
     assert decoded_rows==row['rows']and reader.bytes==row['encoded_bytes']and reader.hash.hexdigest()==row['encoded_sha256']
"""
    after = """     reader=HashReader(source)
     with source,original.open('xb')as sink:
      if row['codec']=='png_rgb_constant_planes_v1':
       from checkpoint_rgb_constant_planes_codec import RGBReader
       rgb=RGBReader(reader);middle=HashReader(rgb)
       decoded_rows=decode_rgb_dictionary(middle,sink)
       assert decoded_rows==rgb.rows==row['rows']
       assert middle.bytes==row['prior_rgb_bytes']and middle.hash.hexdigest()==row['prior_rgb_sha256']
      else:decoded_rows=decode_rgb_dictionary(reader,sink)
     assert decoded_rows==row['rows']and reader.bytes==row['encoded_bytes']and reader.hash.hexdigest()==row['encoded_sha256']
"""
    assert source.count(before) == 1
    result = source.replace(before, after)
    compile(result, 'restore_checkpoint.py', 'exec')
    return result
