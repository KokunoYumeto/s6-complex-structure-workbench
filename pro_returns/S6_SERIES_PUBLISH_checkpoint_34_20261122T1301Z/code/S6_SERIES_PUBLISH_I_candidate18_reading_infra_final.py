#!/usr/bin/env python3
"""Freeze all assigned candidate18 readings plus the extra layout page."""
import datetime,hashlib,importlib.util,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];AREA=ROOT/'agents/continuation_infra'
spec=importlib.util.spec_from_file_location('partial',ROOT/'code/S6_SERIES_PUBLISH_I_candidate18_reading_infra.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
findings=dict(m.findings)
findings.update({
336:'Read the complete bibliography page: Cossec–Dolgachev–Liedtke through Dloussky–Teleman. The distinct2024/2025 editions, Cremona–Siksek DOI, Darmon published contribution/report DOI, Demailly dated edition and DeMarco DOI/v2 note all render clearly; no new actionable finding.',
337:'Read the complete bibliography page: Dloussky–Teleman through Engel–de Gaay Fortman–Schreieder. Both Du editions retain four authors and their exact versioned URLs; the Drinfeld original/translation metadata and other cited-edition notes are legible. The last entry continues normally on338.',
338:'Read the complete bibliography page: continuation of Engel–de Gaay Fortman–Schreieder through Fujimoto. Exact v3 date, Erban Article25, source-bound preprint editions, Fujiki–Pontecorvo15–71 and Fujimoto’s separately identified conference/journal records and DOI scopes are legible; no clipping or new actionable finding.',
339:'Read the complete bibliography page: Gasbarri through the opening Herblot entry. Gauduchon collection/publisher data, Grauert erratum DOI, Gross–Zagier preprint note and Gross’s author-confirmed title render clearly. The Herblot entry continues on340.',
340:'Read the complete bibliography page: Herblot continuation through Kajiwara–Kato–Nakayama. Honda’s journal versus v1 locator note, Huber’s DOI macro and v8 note, IKN/erratum pages, Jetchev’s corrected2009/129(2)/284–302 record and v1 note all render correctly.',
341:'Read the complete bibliography page: Kajiwara–Kato–Nakayama continuation through McHugh. The official69–193 page range, Łojasiewicz Series3, Matsuki correction edition and Mazur–Stein–Tate DOI are legible; McHugh continues on342 with its exact edition note.',
342:'Read the complete bibliography page: McHugh continuation through Nishiguchi. Exact McHugh v4 and Miller v3 notes, NIST1.2.8 release/access date, Nguyen DOI and pinned v1, and the retained MPI/88-48 title are clear; no new actionable finding.',
343:'Read the complete bibliography page: Nishiguchi continuation through Rubin. Oda’s official retypeset-edition note, Parusiński’s1994 publication and explicitly cited1990 report, and all DOI/URL line wraps are legible; no new actionable finding.',
344:'Read the complete bibliography page: Rubin continuation through Székelyhidi–Tosatti–Weinkove. Rubin and Schröer–Siebert DOI fields, exact source-bound Shin v6 date, Stein DOI and Sutherland21November2023 lecture date render correctly. The retained author-title transcription “Appel–Humbert” follows the primary lecture PDF.',
345:'Read the complete bibliography page: Székelyhidi–Tosatti–Weinkove edition note through Xiao. Versioned Viaclovsky URLs, Waldschmidt journal accents and chapter DOI, retained theta pagination1–7, and Gang Xiao’s complete name are legible; no new actionable finding.',
346:'Read the complete final bibliography page: Xiao URL continuation, Xie, Yang and Yuan–Zhang–Zhang. Xie/Yang versioned URLs, YZZ formal2013 book metadata/DOI, explicit6November2011 cited-edition note and verified primary author-upload URL fit cleanly; no new actionable finding.',
})
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
partial=AREA/'S6_SERIES_PUBLISH_I_final_candidate18_reading_infra_partial_01.json';d=json.loads(partial.read_text())
assert sha(partial)=='f45722450fce4a631ed6283bf31625a1af3f7057f9155fc5090aff966bba5409'
manifest=ROOT/'render/I_candidate18/manifest.json';images={r['page']:r for r in json.loads(manifest.read_text())['rendered_pages']}
pages=[]
for p,finding in sorted(findings.items()):
    image=ROOT/'render/I_candidate18'/f'page_{p:03d}.png';h=sha(image);assert h==images[p]['image_sha256']
    pages.append({'page':p,'finding':finding,'image_sha256':h,'pdf_sha256':d['pdf_sha256'],'actual_full_page_image_read':True,'pending_guards':'D23 paragraph-break-only layout proposal pending; inherited underfull warning' if p==321 else ''})
assert len(pages)==32 and set(d['assigned_pages'])<set(findings)
assert sha(ROOT/'S6_SERIES_PUBLISH_I.tex')==d['source_sha256']
d.update({'recorded_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'pages':pages,'status':'complete immutable actual reading:31 of31 assigned pages plus extra321','assigned_pages_read':31,'total_pages_actually_read':32,'partial_record_preserved':{'path':str(partial.relative_to(ROOT)),'sha256':sha(partial)},'all_assigned_pages_read':True,'certified':False})
out=AREA/'S6_SERIES_PUBLISH_I_final_candidate18_reading_infra.json';assert not out.exists();out.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
md=AREA/'S6_SERIES_PUBLISH_I_final_candidate18_reading_infra.md';assert not md.exists();md.write_text('# Complete candidate18 infrastructure reading\n\n'+d['scope']+'\n\n31assigned pages and additional page321 were actually viewed in full. The p321 layout finding remains pending; zero mathematical events.\n\n'+''.join(f'## Page {r["page"]}\n\n{r["finding"]}\n\nPNG SHA-256: `{r["image_sha256"]}`.\n\n' for r in pages))
print(json.dumps({'record':str(out.relative_to(ROOT)),'sha256':sha(out),'markdown_sha256':sha(md),'assigned':31,'actual':32,'mathematical_events_added':0}))
