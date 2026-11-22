from S6_SERIES_PUBLISH_editing import Editor
ed=Editor('I')
ed.replace(r'\begin{longtable}{@{}p{.08\textwidth}p{.87\textwidth}@{}}',r'\begin{longtable}{@{}p{.10\textwidth}p{.85\textwidth}@{}}',
 'D24','Give the Theorem column enough width for its heading; the current build reported a 1.7175pt excess. The mathematical table content is unchanged.','pub:I:known-new')
ed.save()
