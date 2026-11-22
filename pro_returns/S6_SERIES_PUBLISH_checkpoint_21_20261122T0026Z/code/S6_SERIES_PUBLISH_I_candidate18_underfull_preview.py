#!/usr/bin/env python3
"""Isolated two-paragraph typography preview; canonical source is read-only."""
import datetime,hashlib,json,os,re,shutil,subprocess
from pathlib import Path
import fitz
ROOT=Path(__file__).resolve().parents[1];AREA=ROOT/'agents/continuation_infra'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
EXPECTED='3542f2632cad8f1eb78f0f30f8a64ca91998f3bd1d97010ca76d89297c4bffe7'
source_path=ROOT/'S6_SERIES_PUBLISH_I.tex';assert sha(source_path)==EXPECTED
source=source_path.read_text()
start=source.index('The second equality identifies the remaining monomials\n')
end=source.index('\n\n\\item Put $b=d-12z$',start)
before321=source[start:end]
after321=before321.replace('$x^{-i-1}y^{-j-1}$.\nThe bundles', '$x^{-i-1}y^{-j-1}$.\n\nThe bundles')
assert before321!=after321 and re.sub(r'\s','',before321)==re.sub(r'\s','',after321)
start272=source.index('\\item Enclose the real periods from the exact minimal invariants.')
end272=source.index('\n\\[',start272)
before272=source[start272:end272]
after272=before272.replace('invariants.  For rows','invariants.\n\nFor rows').replace('$\\tau=iT$;\nfor rows','$\\tau=iT$.\n\nFor rows')
assert before272!=after272
assert re.findall(r'(?<!\\)\$[^$]*\$',before272)==re.findall(r'(?<!\\)\$[^$]*\$',after272)
stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
work=AREA/('layout_I18_'+stamp);work.mkdir()
preview=source.replace(before321,after321).replace(before272,after272)
tex=work/'S6_SERIES_PUBLISH_I.tex';tex.write_text(preview)
output=work/'build';output.mkdir()
for suffix in ['aux','out','toc']:
    old=ROOT/'build/I_candidate18'/('S6_SERIES_PUBLISH_I.'+suffix)
    if old.exists():shutil.copy2(old,output/old.name)
guard={'id':'I18-infra-D23-01','type':'D23','statement_id':'push:src:E.2.1','source_sha256':EXPECTED,'page':321,'line':source[:start].count('\n')+1,'before':before321,'after':after321,'reason':'Separate the monomial-identification sentence from the acyclicity paragraph to remove visible stretched spacing. One blank line is inserted; every word, punctuation mark and mathematical token is unchanged.','original_full_block':before321,'proposed_full_block':after321,'original_full_block_sha256':hashlib.sha256(before321.encode()).hexdigest(),'proposed_full_block_sha256':hashlib.sha256(after321.encode()).hexdigest(),'scope':'Local paragraph formatting inside the existing proof; every label, environment, citation and mathematical token is unchanged.','status':'proposal; isolated layout preview pending','mathematical_events_added':0}
for name,text in [('I18-infra-D23-01_original.tex',before321),('I18-infra-D23-01_proposed.tex',after321),('peer_p272_original.tex',before272),('peer_p272_proposed.tex',after272)]:
    (work/name).write_text(text+'\n')
guard['original_full_block_path']=str((work/'I18-infra-D23-01_original.tex').relative_to(ROOT));guard['proposed_full_block_path']=str((work/'I18-infra-D23-01_proposed.tex').relative_to(ROOT))
env=os.environ.copy()
env['TEXMFCNF']=str(ROOT/'tex-runtime/web2c')+':/usr/share/texlive/texmf-dist/web2c'
env['TEXMFCACHE']=str(ROOT/'tex-runtime/lua-cache')
env['OSFONTDIR']='/usr/share/texmf/fonts/opentype:/usr/share/fonts'
with (output/'preview_pass1.out').open('w') as log:
    proc=subprocess.run(['pdflatex','-interaction=nonstopmode','-halt-on-error','-no-shell-escape','-synctex=1','-output-directory='+str(output),str(tex)],cwd=ROOT,env=env,stdout=log,stderr=subprocess.STDOUT)
assert proc.returncode==0,(output/'preview_pass1.out').read_text()[-2000:]
log=(output/'S6_SERIES_PUBLISH_I.log').read_text(errors='replace')
def warnings(log):return [{'badness':int(m[1]),'line_start':int(m[2]),'line_end':int(m[3]),'log_context':log[m.start():m.start()+650]} for m in re.finditer(r'Underfull \\[hv]box \(badness (\d+)\) in paragraph at lines (\d+)--(\d+)',log)]
pdf=output/'S6_SERIES_PUBLISH_I.pdf';doc=fitz.open(pdf)
rendered=[]
for page in [272,321,322]:
    p=work/f'page_{page:03d}.png';doc[page-1].get_pixmap(matrix=fitz.Matrix(1.6,1.6),alpha=False).save(p);rendered.append({'page':page,'path':str(p.relative_to(ROOT)),'sha256':sha(p)})
diagnostics={}
for n in [17,18]:
    p=ROOT/f'build/I_candidate{n}/S6_SERIES_PUBLISH_I.log';diagnostics[str(n)]={'log_path':str(p.relative_to(ROOT)),'log_sha256':sha(p),'underfull':warnings(p.read_text(errors='replace'))}
guard['status']='proposal; isolated build completed; full image review pending'
gp=AREA/'S6_SERIES_PUBLISH_I_candidate18_infra_layout_guard.json';assert not gp.exists();gp.write_text(json.dumps({'source_sha256':EXPECTED,'guards':[guard],'mathematical_events_added':0},ensure_ascii=False,indent=2)+'\n')
receipt={'recorded_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source_sha256':EXPECTED,'canonical_source_unchanged':sha(source_path)==EXPECTED,'preview_source_path':str(tex.relative_to(ROOT)),'preview_source_sha256':sha(tex),'preview_pdf_path':str(pdf.relative_to(ROOT)),'preview_pdf_sha256':sha(pdf),'preview_pages':len(doc),'preview_underfull':warnings(log),'preview_overfull':len(re.findall(r'Overfull \\[hv]box',log)),'preview_undefined_references':len(re.findall(r'Reference .*? undefined',log)),'preview_undefined_citations':len(re.findall(r'Citation .*? undefined',log)),'rendered_pages':rendered,'inherited_diagnostics':diagnostics,'historical_summary_scope':'Historical build_summary counts overfull boxes but has no underfull count. Both17 and18 have the same four warning badness values; no zero-underfull claim is inferred from that summary.','p321_guard_path':str(gp.relative_to(ROOT)),'p321_guard_sha256':sha(gp),'p272_private_proposal_scope':'Peer-owned proposal preview only: paragraph break after invariants; semicolon after tau=iT becomes period, following for becomes For, and a paragraph break separates the two row groups. Every math segment is unchanged.','mathematical_events_added':0,'page_reading_credit_added':0}
rp=AREA/'S6_SERIES_PUBLISH_I_candidate18_underfull_preview_receipt.json';assert not rp.exists();rp.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'work':str(work.relative_to(ROOT)),'receipt':str(rp.relative_to(ROOT)),'receipt_sha256':sha(rp),'preview_underfull':receipt['preview_underfull'],'pages':len(doc),'rendered_pages':rendered,'guard_sha256':sha(gp)}))
