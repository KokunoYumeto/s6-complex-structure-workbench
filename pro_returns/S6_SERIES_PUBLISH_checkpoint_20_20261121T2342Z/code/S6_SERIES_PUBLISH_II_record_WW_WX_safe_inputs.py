"""Citation-only target metadata and the already printed standing domain."""
from pathlib import Path
import datetime as dt,hashlib,json,re
R=Path(__file__).resolve().parents[1]
p=R/'S6_SERIES_PUBLISH_II.tex';data=p.read_bytes();s=data.decode()
sha=lambda b:hashlib.sha256(b).hexdigest()
assert sha(data)=='deed2de0d348b9644cf56307296423d59a62a5947ac7ac0ba9ba41a9ec3e42fc'
def packet(label):
    a=s.index('\\label{'+label+'}');a=s.rfind('\\begin{',0,a)
    b=s.index('\\begin{proof}',a);c=s.index('\\end{proof}',b)+len('\\end{proof}')
    return {'label':label,'statement':s[a:b],'statement_sha256':sha(s[a:b].encode()),
            'target_proof_sha256':sha(s[b:c].encode()),'target_proof_included':False}
standing=next(l for l in s.splitlines() if l.startswith('\\paragraph{Standing torus-fibration setting.}'))
bib=s[s.index('\\begin{thebibliography}'):]
blocks=re.split(r'(?=\\bibitem)',bib)
khaled=next(b for b in blocks if '{Khaled2024Hopf}' in b)
ww=packet('night:P4.24');wx=packet('night:P4.25')
ww['named_primary_inputs']=[{'author':'Zahraa Khaled','title':'Real structures on primary Hopf surfaces','locators':['Theorem 2.1(1)','formula (1)'],'current_bibliography_key':'Khaled2024Hopf','current_bibliography_entry':khaled,'primary_edition_not_yet_verified_by_this_record':True}]
ww['explicit_internal_locator_tokens']=[]
wx['named_primary_inputs']=[{'authors':'Liu–Rollenske','title':'Two-dimensional semi-log-canonical hypersurfaces','locators':['Definition 2.3','Lemma 2.2','main Theorem','Table 1','Proposition 3.1','Proposition 4.1'],'current_bibliography_key':None,'bibliography_scope':'Root read every current bibliography block containing Rollenske. Those are LRS2019 and LiuRollenske2026, with different explicit titles; no matching title is provided by those two blocks. This is a bounded bibliography inspection.','primary_edition_not_yet_verified_by_this_record':True}]
wx['explicit_internal_locator_tokens']=['night:P4.16','night:P4.20','night:P4.6','night:P4.8']
r={'recorded_utc':dt.datetime.now(dt.timezone.utc).isoformat(),'source':{'path':p.name,'sha256':sha(data)},
   'standing_domain':{'text':standing,'sha256':sha(standing.encode())},
   'targets':[ww,wx],
   'scope':'Only complete target statements, named source titles/locators, existing bibliography metadata and the standing setting are supplied. No target proof argument or method is included. Root inspected the named-citation paragraphs solely to identify these inputs and has no fresh-check credit for these targets.',
   'events_added':0,'canonical_mutations':0}
q=R/'records/S6_SERIES_PUBLISH_II_WW_WX_safe_named_inputs.json';assert not q.exists();q.write_text(json.dumps(r,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'path':str(q.relative_to(R)),'sha256':sha(q.read_bytes())}))

matches=[]
for n,line in enumerate(s.splitlines(),1):
    if re.search(r'\\omega(?![A-Za-z_])',line):matches.append({'line':n,'text':line})
r={'recorded_utc':dt.datetime.now(dt.timezone.utc).isoformat(),'source_sha256':sha(data),
   'literal_standalone_omega_hits_actually_read':matches,
   'root_reading':'Root read all the returned standalone omega contexts and all omega-containing contexts within lines30000–40000. The only displayed base/Leray generator is in IM at35406–35407. Other explicit occurrences designate metric forms, dualizing/holomorphic forms, a cube root of unity or IH indexed whisker paths.',
   'conclusion':'No pre-existing fixed orientation for the IM generator was found in this exact inspection. The source transport must still name the actual differential sign or define its generator through the actual differential; no uncomputed sign is silently fixed here.',
   'events_added':0,'canonical_mutations':0}
q=R/'records/S6_SERIES_PUBLISH_II_IM_omega_root_scope.json';assert not q.exists();q.write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps({'path':str(q.relative_to(R)),'sha256':sha(q.read_bytes())}))
