from S6_SERIES_PUBLISH_c3_edit import *

text=SOURCE.read_text()
a=text.rfind('\\begin{proposition}',0,text.index('\\label{cdp:st:A.5.2}'))
b=text.index('\n',a)
marker=text[a:b]
lemma=(ROOT/'agents/continuation3_root/S6_SERIES_PUBLISH_exceptional_intersection.tex').read_text()
apply_edit(marker,lemma+'\n\n'+marker,'II-C3-EXCEPTIONAL-OWNER',['D12','D13'],
    'lem:II:exceptional-intersection','Normalization foundations before A.5.2',
    'Insert the single earlier complete analytic exceptional-matrix lemma, read against both P4.12 and P4R.6 and the opened Mumford identity. Its local principal divisor, diagonal change of variables and inverse series preserve the exact maps and signs. The normalization fragment retains this identical owner and will supply its earlier A.5.20 application.')
add_event('lem:II:exceptional-intersection','II-C3-ROOT-EXCEPTIONAL-OWNER',
    'used and rechecked in this run',
    'Full receiving lemma compared with the two complete prior intersection proofs and opened Mumford p.6. Connectedness, effective local principal divisor, weighted quadratic identity, negative definiteness and strict positivity of the inverse follow by the explicit diagonal and spectral-series maps. Exposed consolidation only.',
    'S6_SERIES_PUBLISH_II.tex; agents/continuation3_root/S6_SERIES_PUBLISH_exceptional_intersection.tex',
    source='code/S6_SERIES_PUBLISH_c3_exceptional_owner_admit.py')
print('P243 is now present before all current applications.')
