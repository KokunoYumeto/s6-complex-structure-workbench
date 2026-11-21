#!/usr/bin/env python3
"""Keep cited authors' lettered theorem locators independent of main letters."""
from S6_SERIES_PUBLISH_editing import Editor
e=Editor('I')
for old,new,n in [
    (r'Theorem~\ref{series:I:B}.1',r'Theorem~B.1',1),
    (r'Theorem~\ref{series:I:A}.1',r'Theorem~A.1',2),
    (r'[Theorem~\ref{series:I:A}]',r'[Theorem~A]',2),
]:
    e.replace(old,new,'D06','Restore the external author\'s exact lettered theorem locator after the introductory-letter reference pass; its cited work supplies the context.','external theorem locator',n)
e.save()
