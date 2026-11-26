"""Record an actually completed exposed unit reading; no independent credit."""
from S6_SERIES_PUBLISH_c3_edit import *
import json
import sys

data=json.load(sys.stdin)
unit=data['unit']
event=data['event_id']
assert data['complete_original_and_receiving_read'] is True
add_event(data.get('statement',unit),event,'used and rechecked in this run',
    data['outcome'],'S6_SERIES_PUBLISH_II.tex; S6_SERIES_PUBLISH_defects_II.tsv',
    group=data.get('evidence_group',''),source='code/S6_SERIES_PUBLISH_c3_read_unit.py')
for number in range(1,26):
    kind=f'D{number:02}'
    if kind in ['D10','D16']:continue
    status='open' if kind in ['D14','D23'] else 'done'
    detail=('Final whole-paper placement remains open.' if kind=='D14'
        else 'Integrated typesetting and final rendered-page reading remain open.' if kind=='D23'
        else 'Complete unit read against this defect type; every identified instance logged and no residual local instance found. '+data.get('unit_detail',''))
    set_unit_status(unit,kind,status,detail,'CHECK_EVENTS.tsv: '+event)
set_unit_status(unit,'structure','open','Local proof ownership reviewed; final whole-paper placement remains open.',
    'CHECK_EVENTS.tsv: '+event)
print(unit+': complete exposed unit reading; 21 previously open local defect rows closed; final placement and page reading remain open.')
