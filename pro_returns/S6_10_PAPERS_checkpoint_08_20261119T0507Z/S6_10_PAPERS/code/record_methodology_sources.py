from pathlib import Path
import json,re
P=Path(__file__).resolve().parents[1]
rows={
 'OpenAIReasoning2026':('OpenAI','Reasoning models','https://developers.openai.com/api/docs/guides/reasoning','Reasoning effort and Reasoning mode; lines1274–1303 in the opened page.','Reasoning allocation controls and the named configuration fields.'),
 'OpenAIChatGPTPro2026':('OpenAI','GPT-6 and other models in ChatGPT','https://help.openai.com/en/articles/20001354-gpt-6-and-other-models-in-chatgpt','Choose a thinking level; lines25–36 in the opened page.','The documented Pro selection and GPT-6 Astra model mapping.'),
 'AnthropicEffort2026':('Anthropic','Effort','https://platform.claude.com/docs/en/build-with-claude/effort','How effort works and Effort levels; lines138–155.','Response-token effort control, including thinking.'),
 'CC01Universal':('Creative Commons','CC0 1.0 Universal','https://creativecommons.org/publicdomain/zero/1.0/','Official deed, No Copyright, items1–2.','Public-domain dedication identified by the official deed.')}
f=P/'S6_10_PAPERS_references.bib';s=f.read_text()
g=P/'analysis/I_sources/current_source_matches.json';d=json.loads(g.read_text())
for key,(author,title,url,loc,scope) in rows.items():
 if not re.search(r'^@\w+\{'+key+r',',s,re.M):
  s+='\n@misc{'+key+',\n author={{'+author+'}},\n title={'+title+'},\n year={2026},\n url={'+url+'},\n howpublished={Official documentation; accessed 18 November 2026},\n verification={verified at listed scope}\n}\n'
 d[key]={'exact_locator':loc,'scope':scope,'date':'2026-11-18','checker':'GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro','url':url,'verification':'opened and matched at listed scope'}
f.write_text(s);g.write_text(json.dumps(d,indent=2,ensure_ascii=False));print('Four official methodology/dedication source records added.')
