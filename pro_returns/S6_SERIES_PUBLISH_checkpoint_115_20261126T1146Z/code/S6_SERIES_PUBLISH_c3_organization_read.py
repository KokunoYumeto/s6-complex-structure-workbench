"""Record the completed local first-part organization and results-list read."""
from S6_SERIES_PUBLISH_c3_edit import *

text = SOURCE.read_text()
start = text.index(r'\subsection{How the paper is organized}')
end = text.index(r'\section{Common conventions}', start)
unit = text[start:end]
assert r'\cite' not in unit
for target in re.findall(r'\\(?:[Cc]ref|ref)\*?\{([^}]+)\}', unit):
    for label in target.split(','):
        assert r'\label{' + label.strip() + '}' in text, label
for name in [
    'cotangent-fibre-geometry', 'irreducible-euler', 'periods-tangent-deformations',
    'component-geometry', 'compact-occurrence', 'canonical-reduction', 'remaining-splitting']:
    assert r'\label{part:II:' + name + '}' in text

event = 'II-C3-ORGANIZATION-FULL-LOCAL-READ'
detail = (
    'Root read the complete current organization prose, figure and exact five-edge premise table; '
    'the complete Further-results list was read before the three precisely recorded duplicate-owner consolidations, '
    'whose full old/new entries and body owners were then compared. Every unchanged line is included in that complete reading. '
    'All25 register classes were considered. The seven parts, final splitting problem and exact figure premises '
    'agree with their current body owners. All local surviving entries resolve through current labels; this unit has '
    'no external citation or bibliography entry. Final global order, first-part reconciliation and rendered typography '
    'remain open. No independent derivation, required-check or final-page credit.')
for kind in [f'D{i:02}' for i in range(1,10)] + ['D11','D12','D13','D17','D18','D19','D20','D21','D22','D25']:
    set_unit_status('how-the-paper-is-organized',kind,'done',detail,'CHECK_EVENTS.tsv: '+event)
add_event('II',event,'used and rechecked in this run',detail,
    'How the paper is organized, dependency figure and Further results; '
    'earlier complete first-part/figure comparison and the common-model, Cartier-duality, weighted-cycle and Euler alias edits',
    source='code/S6_SERIES_PUBLISH_c3_organization_read.py')
print('Nineteen stable local organization rows closed; D14/D15/D23/D24 and structure remain open.')
