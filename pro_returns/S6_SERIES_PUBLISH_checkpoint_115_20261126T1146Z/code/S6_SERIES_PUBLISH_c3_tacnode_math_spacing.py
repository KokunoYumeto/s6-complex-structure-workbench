"""Remove the two equation-internal paragraph breaks detected by pdfLaTeX."""
from S6_SERIES_PUBLISH_c3_edit import *

for number,spaces in [('4',16),('5',23)]:
    old='\n'+' '*spaces+'\n'+r'\label{eq:II:manual:P4R.14.'+number+'}'
    new='\n'+r'\label{eq:II:manual:P4R.14.'+number+'}'
    apply_edit(old,new,'II-C3-R14-EQUATION-PARAGRAPH-'+number,['D23'],
      'night:P4R.14','Equation '+number+' in the smooth tacnode unit',
      'The integrated pdfLaTeX pass stopped at a blank paragraph inside a math environment. Remove that paragraph token; every mathematical character and stable label remains.',
      'Root read the exact old/new display and failing build location; mathematical payload unchanged.')
add_event('night:P4R.14','II-C3-BUILD-TACNODE-MATH-PARAGRAPHS','used and rechecked in this run',
 'The first integrated pass after R14 admission stopped with Missing $ inserted at the blank line before equation label P4R.14.4. Root read the full two affected equation blocks and removed the two whitespace-only paragraphs before labels 14.4 and 14.5. The formulas and labels are unchanged. A fresh three-pass build is required; no clean-build or page-reading credit is assigned here.',
 'build/II_c3_working/S6_SERIES_PUBLISH_II.log; S6_SERIES_PUBLISH_II.tex',
 source='code/S6_SERIES_PUBLISH_c3_tacnode_math_spacing.py')
print('Two equation paragraph tokens removed; build rerun pending.')
