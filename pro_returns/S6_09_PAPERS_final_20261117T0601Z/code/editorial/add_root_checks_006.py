"""Record opened methodology documentation and exact bibliography aliases."""
from pathlib import Path
import json
OUT=Path(__file__).resolve().parents[2]
p=OUT/'work/root/references_verified.json';rows=json.loads(p.read_text())
new=[{
 'keys':['AnthropicEffort2026'],
 'url':'https://platform.claude.com/docs/en/build-with-claude/effort',
 'status':'verified in specified scope',
 'opened_locators':'How effort works and Effort levels, lines127–145; model-specific paragraphs165–181 in opened web rendering.',
 'verification_scope':'The max effort level is the maximum capability setting with unrestricted token spending, supported by the two Claude models named in the historical reading record. This is effort-setting documentation, not evidence for mathematical correctness.',
 'own_check':'GPT-6 Astra (OpenAI, ChatGPT Pro mode), effort Pro, 17 November 2026.',
 'web_refs':['turn181view0','turn181view1']
}]
for r in json.loads((OUT/'work/cdp_audit/references_verified.json').read_text()):
 if r.get('key')=='CDP2020':
  new.append({**r,'keys':['CDP20','CDP2020D','CDP2020'],'alias_basis':'Same original publication and DOI; all aliases share the exact opened scope, without broadening it.'})
 if r.get('key')=='CDP1998':
  new.append({**r,'keys':['CDP98','CDP1998'],'alias_basis':'Same original publication; all aliases share the exact opened scope.'})
for r in new:
 if not any(x.get('keys')==r.get('keys') for x in rows):rows.append(r)
p.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
(OUT/'work/root/source_checks_006.json').write_text(json.dumps(new,ensure_ascii=False,indent=2)+'\n')
bib=OUT/'work/root/additional_checked_references.bib'
s=bib.read_text()
if 'AnthropicEffort2026' not in s:
 s+='''\n@misc{AnthropicEffort2026,
 author={{Anthropic}},title={Effort},year={2026},
 howpublished={Claude Platform official documentation, accessed 17 November 2026},
 url={https://platform.claude.com/docs/en/build-with-claude/effort}
}\n'''
bib.write_text(s)
print('Added or preserved',len(new),'scoped source records.')
