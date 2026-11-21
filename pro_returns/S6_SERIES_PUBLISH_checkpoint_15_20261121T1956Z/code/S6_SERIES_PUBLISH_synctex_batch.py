#!/usr/bin/env python3
"""Query the same libsynctex used by the installed CLI, parsing each PDF once.

The caller supplies an exact input path and PDF. Only page numbers returned by
libsynctex are recorded; this supplies source-location metadata, never reading
or mathematical check evidence. The CLI remains the validation reference.
"""
import ctypes
import ctypes.util
import hashlib
import json
from pathlib import Path


class Scanner:
    def __init__(self, pdf):
        name = ctypes.util.find_library('synctex')
        if not name:
            raise RuntimeError('libsynctex is unavailable')
        self.lib = lib = ctypes.CDLL(name)
        lib.synctex_scanner_new_with_output_file.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int]
        lib.synctex_scanner_new_with_output_file.restype = ctypes.c_void_p
        lib.synctex_display_query.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_int, ctypes.c_int, ctypes.c_int]
        lib.synctex_display_query.restype = ctypes.c_int
        lib.synctex_scanner_next_result.argtypes = [ctypes.c_void_p]
        lib.synctex_scanner_next_result.restype = ctypes.c_void_p
        lib.synctex_node_page.argtypes = [ctypes.c_void_p]
        lib.synctex_node_page.restype = ctypes.c_int
        lib.synctex_scanner_free.argtypes = [ctypes.c_void_p]
        lib.synctex_scanner_free.restype = ctypes.c_int
        self.scanner = lib.synctex_scanner_new_with_output_file(str(Path(pdf).resolve()).encode(), None, 1)
        if not self.scanner:
            raise RuntimeError('Could not parse SyncTeX for '+str(pdf))

    def pages(self, source, line):
        result = self.lib.synctex_display_query(self.scanner, str(Path(source).resolve()).encode(), int(line), 0, -1)
        if result < 0:
            raise RuntimeError('SyncTeX query failed for source line '+str(line))
        pages = set()
        while True:
            node = self.lib.synctex_scanner_next_result(self.scanner)
            if not node:
                break
            page = self.lib.synctex_node_page(node)
            if page > 0:
                pages.add(page)
        return sorted(pages)

    def close(self):
        if self.scanner:
            self.lib.synctex_scanner_free(self.scanner)
            self.scanner = None

    def __enter__(self):
        return self

    def __exit__(self, *_):
        self.close()


def prepare(doc, requests):
    needed = sorted(set(requests) - set(doc.cache))
    if needed:
        with Scanner(doc.pdf) as scanner:
            for line in needed:
                doc.cache[line] = scanner.pages(doc.source, line)
    doc.cache_path.write_text(json.dumps(doc.cache, sort_keys=True)+'\n')

