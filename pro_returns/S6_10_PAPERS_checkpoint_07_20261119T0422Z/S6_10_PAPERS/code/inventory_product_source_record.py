from pathlib import Path
import datetime,hashlib,json
R=Path('/workspace/scratch/490d8ca4e928');W=R/'work/S6_10_PAPERS';now=datetime.datetime.now(datetime.timezone.utc).isoformat()
p=W/'analysis/IV/references/Takase2005v1.pdf'
record={
 'source_key':'Takase2005','source':'https://arxiv.org/abs/math/0506356',
 'locus':'arXiv math/0506356v1 (17 June 2005), PDF/printed p. 5 Corollaries 2.13–2.15 and Theorem 3.2 statement; p. 6 Definition 3.6, Remark 3.7 and Theorem 3.8; p. 7 complete proof of Theorem 3.2 and the preceding normal-Euler-class identification',
 'used_by':'night:P3K.42',
 'scope':'Actually read the complete specified-normal-field argument: the normal framing map pi3(SO3) to pi3(S2) to Z consists of isomorphisms, and Corollary 2.13 supplies the Seifert surface used in Corollary 2.15. The complete proof of Theorem 3.2 takes a framing whose third vector is the projection direction and chooses the Seifert surface with the prescribed first vector as its boundary normal. The projection is nonsingular at the boundary. Theorem 3.8 gives omega=(3 sigma+e[xi])/2; Remark 3.7 and the displayed p. 7 calculation identify the singular surface with the Poincare dual of the normal Euler class and xi with its restriction, so e[xi]=e squared. This closes exactly the outward-field and 2 omega=3 sigma+e squared input in K42 SP.1. The source uses its own Smale convention; K42 retains its separately proved F55 convention bridge. No direct rereading of Ekholm–Szucs is claimed, no journal-page numbering is inferred, and no new independent review of the whole Takase paper is asserted.',
 'date':now,'who':'GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro)',
 'status':'opened and matched at stated locus',
 'web_refs':['turn236734032view0'],
 'aliases':['Takase2007E'],
 'alias_evidence':'Compared author Masamichi Takase, title The Hopf invariant of a Haefliger knot, arXiv math/0506356 and official journal metadata Math. Z. 256 (2007), 35–44, DOI 10.1007/s00209-006-0053-8. The two bibliography keys denote this work; this record reads the v1 pages explicitly, not an inferred journal-page locus.',
 'local_file':str(p.relative_to(R)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
 'visual_openings':['analysis/IV_product_batch/references/Takase_v1_p5_small.png','analysis/IV_product_batch/references/Takase_v1_p7_small.png']}
out=W/'analysis/IV_product_batch/source_reads.json';rows=json.loads(out.read_text()) if out.exists() else [];rows=[x for x in rows if x['source_key']!=record['source_key']];rows.append(record);out.write_text(json.dumps(rows,indent=2,ensure_ascii=False)+'\n')
# Explicitly register the newly supplied all-cap working theorem without awarding
# a proof event before its receiving author supplies the stable TeX/event hashes.
p=W/'analysis/inventory_additions.json';adds=json.loads(p.read_text());label='iv:i3_all_reduced_caps'
if not any(x['label']==label for x in adds):
 tex=W/'papers/IV/i3_all_reduced_caps.tex'
 row={'paper':'IV','label':label,'s6_09_label':'','source_run':'S6_10_PAPERS','source_id':'IV.i3_all_reduced_caps','kind':'Main all-cap source-return theorem; receiving intake pending','status':'current full proof event and receiving hash pending intake','main_or_supporting':'main','uses':'night:P3K.106; exact ICAP1–5 source/root/line/cap morphisms','check_record':'Author reports current mathematical derivation and two program replays; intake does not award a completed proof check before the exact event and receiving source are supplied. No supplement-specific historical checker/date inferred.','credited_to':'CP29 unregistered all-cap working proof, with the actual receiving extension and exact literature inputs separately recorded','in_compendium_only_because':'','notes':json.dumps({'placement':'papers/IV/i3_all_reduced_caps.tex','receiving_integration_pending':True,'proof_owner':'monodromy_fourfold','source_working_file':'sources/newer_night/checkpoint29/notes/part3_e6_selected_i3_all_caps_working.md','source_working_sha256':'cc59c071750694d7043f626b73c7243333733a4e5c18d179b32870df4db936c0','scope':'All m=3l+2, primitive signed norm, admitted finite characters/references/fans; each stated common strict scalar range.'})}
 if tex.exists():row['_source_file']=str(tex.relative_to(R))
 adds.append(row);p.write_text(json.dumps(adds,indent=2,ensure_ascii=False)+'\n')
print(now)
print(out)
