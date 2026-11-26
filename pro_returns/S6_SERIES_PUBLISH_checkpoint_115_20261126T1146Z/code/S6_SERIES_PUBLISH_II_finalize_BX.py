from pathlib import Path
import datetime as dt,hashlib,json
R=Path(__file__).resolve().parents[1]
def bind(p):return dict(path=p,sha256=hashlib.sha256((R/p).read_bytes()).hexdigest())
path='agents/continuation2_root/01BX/S6_SERIES_PUBLISH_II_root_BX_prepared_plan.json'
plan=json.loads((R/path).read_text());plan['previous_plan']=bind(path)
text=(R/plan['proposed']['path']).read_text()
for old,new in [
 ('in \\eqref{cdp:eq:C.D4.7}\ngives $\\sum p_g\\le1$', 'in \\eqref{cdp:eq:C.D4.7}\ngive $\\sum p_g\\le1$'),
 ('number zero, by\nCited result~','number zero, by\ncited result~')]:
 assert text.count(old)==1;text=text.replace(old,new,1)
 plan['guards'].append(dict(old=old,new=new,type='D23',reason='Correct grammar in the new resolved citation; no mathematical expression or step changes.'))
proposed='agents/continuation2_root/01BX/S6_SERIES_PUBLISH_II_root_BX_v2_proposed.tex'
assert not (R/proposed).exists();(R/proposed).write_text(text);plan['proposed']=bind(proposed)
events=json.loads((R/plan['events']['path']).read_text())
events['draft_prepared_utc']=events['created_utc']
events['created_utc']=dt.datetime.now(dt.timezone.utc).isoformat()
events['events'][1]['date_utc']=events['created_utc']
events['events'][1]['outcome']+=' The initial event text was a staged proposal; this final timestamp follows the actual complete original/v1 reading and the exact two grammar corrections. Root batch review records the finalv2 reading separately.'
ep='agents/continuation2_root/01BX/S6_SERIES_PUBLISH_II_root_BX_final_events.json'
assert not (R/ep).exists();(R/ep).write_text(json.dumps(events,indent=2)+'\n');plan['events']=bind(ep)
plan['created_utc']=events['created_utc'];plan['root_proposed_full_reading']='Original and fullv1 read; finalv2 consists of the two exact displayed grammar guards and will be read in full before admission.'
out='agents/continuation2_root/01BX/S6_SERIES_PUBLISH_II_root_BX_final_plan.json'
assert not (R/out).exists();(R/out).write_text(json.dumps(plan,indent=2)+'\n')
print(json.dumps(dict(plan=bind(out),proposed=plan['proposed'],events=plan['events']),indent=2))
