"""Retain the inherited restorer with a verified encoded dictionary view."""

def change(source,before,after):
    assert source.count(before)==1,before
    return source.replace(before,after)

def patch(source):
    source=change(source,
        'stage=Path(temporary);seen=set();completed=set();decoded_png=set();dict_left={};dict_verified={}',
        'stage=Path(temporary);seen=set();completed=set();decoded_png=set();dict_left={};dict_verified={};dict_views={}')
    source=change(source,
        "streaming={row['encoded_name']:(i,row)for i,row in enumerate(rows)if row['codec']=='png_rgb_dictionary_v1'}",
        "streaming={row['encoded_name']:(i,row)for i,row in enumerate(rows)if row['codec']in('png_rgb_dictionary_v1','png_rgb_constant_planes_v1')}")
    source=change(source,
        "if row['codec']=='png_filtered_rows_v1'and not target(stage,row['dictionary_name']).exists():continue",
        "if row['codec']=='png_filtered_rows_v1'and row['dictionary_name']not in dict_views and not target(stage,row['dictionary_name']).exists():continue")
    source=change(source,"""     if name not in dict_verified:verified(dictionary,*identity);dict_verified[name]=identity
     else:assert dict_verified[name]==identity
     decode_png_rows(packed,original,dictionary)
""","""     if name in dict_views:
      from checkpoint_constant_planes_dictionary_view import decode_file as decode_png_rows_view
      assert dict_verified[name]==identity
      decode_png_rows_view(packed,original,dict_views[name])
     else:
      if name not in dict_verified:verified(dictionary,*identity);dict_verified[name]=identity
      else:assert dict_verified[name]==identity
      decode_png_rows(packed,original,dictionary)
""")
    source=change(source,
        "if not dict_left[name]:close_dictionaries();dictionary.unlink();print('Consumed verified dictionary '+name,flush=True)",
        """if not dict_left[name]:
      if name in dict_views:
       view=dict_views.pop(name);view.close();target(stage,view.path).unlink()
      else:close_dictionaries();dictionary.unlink()
      print('Consumed verified dictionary '+name,flush=True)""")
    source=change(source,"""     original=target(stage,row['original_name']);original.parent.mkdir(parents=True,exist_ok=True)
     reader=HashReader(source)
     with source,original.open('xb')as sink:decoded_rows=decode_rgb_dictionary(reader,sink)
     assert decoded_rows==row['rows']and reader.bytes==row['encoded_bytes']and reader.hash.hexdigest()==row['encoded_sha256']
     verified(original,row['original_bytes'],row['original_sha256']);completed.add(rowindex)
     print('Streamed exact original dictionary '+row['original_name'],flush=True)
""","""     if row['codec']=='png_rgb_constant_planes_v1':
      from checkpoint_constant_planes_dictionary_view import store_verified_dictionary
      with source:view=store_verified_dictionary(source,out,row)
      name=row['original_name'];assert name not in dict_views
      dict_views[name]=view;dict_verified[name]=(row['original_bytes'],row['original_sha256'])
      completed.add(rowindex)
      print('Verified complete original dictionary with encoded row access '+name,flush=True)
     else:
      original=target(stage,row['original_name']);original.parent.mkdir(parents=True,exist_ok=True)
      reader=HashReader(source)
      with source,original.open('xb')as sink:decoded_rows=decode_rgb_dictionary(reader,sink)
      assert decoded_rows==row['rows']and reader.bytes==row['encoded_bytes']and reader.hash.hexdigest()==row['encoded_sha256']
      verified(original,row['original_bytes'],row['original_sha256']);completed.add(rowindex)
      print('Streamed exact original dictionary '+row['original_name'],flush=True)
""")
    source=change(source,
        "ready();assert len(completed)==len(rows)and all(n==0 for n in dict_left.values());close_dictionaries()",
        "ready();assert len(completed)==len(rows)and all(n==0 for n in dict_left.values())and not dict_views;close_dictionaries()")
    compile(source,'restore_checkpoint.py','exec')
    return source
