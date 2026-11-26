"""Use direct current-paper references in the Further results list."""
from S6_SERIES_PUBLISH_c3_edit import *

s=SOURCE.read_text();a=s.index(r'\paragraph{Further results.}');b=s.index(r'\section{',a)
old=s[a:b];labels=set(re.findall(r'\\label\{([^}]+)\}',s))
refs=re.findall(r'\\SeriesRef\{([^}]+)\}',old)
assert len(refs)==312 and all(x in labels for x in refs)
new=old.replace(r'\SeriesRef{',r'\cref{')
assert Counter(re.findall(r'\\cref\{([^}]+)\}',new))-Counter(re.findall(r'\\cref\{([^}]+)\}',old))==Counter(refs)
apply_edit(old,new,'II-C3-FURTHER-DIRECT-LABELS',['D06','D22'],
 'how-the-paper-is-organized','Further results, all312 entries',
 'Working PDF page18 visibly printed UNRESOLVED for the new conormal definition although LaTeX reported no undefined reference. Every list entry targets a label in this same paper. Use direct typed references to those identical312 labels, preserving every description and item. This bypasses the stale generated cross-paper dictionary without refreshing it.',
 'Root read working page18 in full, inspected the macro fallback and verified each of the312 literal target labels exists. This is a navigation edit only; no mathematical claim review or whole-list completion credit.')
apply_edit(r'{Twisted cotangent vanishing\\\hyperref[cdp:st:A.4.9]',
 r'{Twisted cotangent\\vanishing\\\hyperref[cdp:st:A.4.9]',
 'II-C3-FIGURE-COTANGENT-LINE',['D23'],'how-the-paper-is-organized','Dependency figure',
 'Give the node a deliberate word-boundary line break after the working page showed a hyphenated cotangent label.')
apply_edit(r'\node[draw,rounded corners,text width=4.1cm,minimum height=1cm] (NT) at (3,-2)'+'\n'+r' {Persistent normalization pullback\\',
 r'\node[draw,rounded corners,text width=4.6cm,minimum height=1cm] (NT) at (3,-2)'+'\n'+r' {Persistent normalization\\pullback\\',
 'II-C3-FIGURE-NORMALIZATION-LINE',['D23'],'how-the-paper-is-organized','Dependency figure',
 'Give the normalization node a wider box and a deliberate word-boundary break after the working page showed a split word. Arrow endpoints remain tied to the node anchors.')
add_event('how-the-paper-is-organized','II-C3-WORKING-PAGE18-REFERENCES','used and rechecked in this run',
 'Root actually viewed and read the entire rendered page18 of the803-page5367214-byte working PDF, including all four diagram nodes, five arrows, the full premise-use table and the visible Further-results entries. The diagram and table fit; two node words hyphenated awkwardly and one list entry printed the SeriesRef UNRESOLVED fallback. Exact source edits supply word-boundary line breaks and direct typed current-paper labels in all312 list entries. This reading applies to that working page only; it is not final PDF-page credit and does not establish absence of fallback text on other pages.',
 'Working PDF page18; exact source edit script',source=__file__)
with (ROOT/'S6_SERIES_PUBLISH_reading_II.md').open('a',newline='\n') as f:
 f.write('\n\n## Third-continuation working page18 — '+now()+'\n\nRoot viewed and read the entire rendered page18 of the803-page5367214-byte working PDF. The four-node/five-arrow figure and full table fit. Two node labels were hyphenated awkwardly; one Further-results reference displayed UNRESOLVED. The exact corrections are in II-C3-WORKING-PAGE18-REFERENCES and the matching defect rows. This is working-page reading only; all final-page rows remain open.\n')
print('All312 Further-results targets are unchanged and use direct current-paper references; page18 findings recorded, with no final-page credit.')
