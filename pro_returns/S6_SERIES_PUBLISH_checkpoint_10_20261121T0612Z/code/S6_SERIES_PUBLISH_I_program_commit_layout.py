from S6_SERIES_PUBLISH_editing import Editor
ed = Editor('I')
ed.replace(
    'The following files contain the indicated computations at commit\n\\texttt{\\SsixRepositoryCommit}. Each link identifies the complete repository path.',
    'The following files contain the indicated computations at commit\n\\begin{center}\\small\\ttfamily\\SsixRepositoryCommit\\end{center}\nEach link identifies the complete repository path.',
    'D23',
    'Place the unchanged full pinned commit on its own line; candidate10 logged a 75.28482pt overfull paragraph at the program-table introduction.',
    'tab:I:programs')
ed.save()
