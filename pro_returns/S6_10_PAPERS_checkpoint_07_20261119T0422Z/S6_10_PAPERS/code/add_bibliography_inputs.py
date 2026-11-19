"""Install exact missing reference entries and documented same-source aliases."""
from pathlib import Path
import re,json
P=Path(__file__).resolve().parents[1]
f=P/'S6_10_PAPERS_references.bib';s=f.read_text()
entries={m.group(1):m.group(0) for m in re.finditer(r'(?ms)^@\w+\{([^,]+),.*?(?=^@|\Z)',s)}
new={
'Papikian2004Tate':r'''@misc{Papikian2004Tate,
 author = {Papikian, Mihran},
 title = {Rigid analytic geometry and abelian varieties},
 year = {2004},
 howpublished = {Author notes, 13 June 2004},
 url = {https://math.stanford.edu/~vakil/snowbird/mihranjun21.pdf},
 verification = {unverified}
}
''',
'Kato1989Erratum':r'''@article{Kato1989Erratum,
 author = {Kato, Masahide},
 title = {Erratum to ``Topology of {Hopf} surfaces''},
 journal = {Journal of the Mathematical Society of Japan},
 volume = {41}, number = {1}, pages = {173--174}, year = {1989},
 url = {https://www.jstage.jst.go.jp/article/jmath1948/41/1/41_1_173/_pdf},
 verification = {unverified}
}
''',
'IVVKramerStolz':r'''@article{IVVKramerStolz,
 author = {Kramer, Linus and Stolz, Stephan},
 title = {A diffeomorphism classification of manifolds which are like projective planes},
 journal = {Journal of Differential Geometry},
 volume = {77}, pages = {177--188}, year = {2007},
 url = {https://archive.ymsc.tsinghua.edu.cn/pacm_download/21/694-JDG-77-2-A1-kramer.pdf},
 verification = {unverified}
}
''',
'IVVWallForm':r'''@misc{IVVWallForm,
 author = {Conway, Anthony and Crowley, Diarmuid and Powell, Mark and Sixt, J{\"o}rg},
 title = {Simply-connected manifolds with large homotopy stable classes},
 howpublished = {Author version, file large-homotopy-stable-class-v3.pdf},
 url = {https://www.maths.gla.ac.uk/~mpowell/large-homotopy-stable-class-v3.pdf},
 verification = {unverified}
}
''',
'IVVOkaOneV5':r'''@misc{IVVOkaOneV5,
 author = {Alarc{\'o}n, Antonio and Forstneri{\v c}, Franc},
 title = {{Oka}-1 manifolds},
 year = {2025}, eprint = {2303.15855v5},
 howpublished = {Version 5, 10 April 2025},
 url = {https://arxiv.org/pdf/2303.15855v5},
 verification = {unverified}
}
'''
}
for k,block in new.items():
 if k not in entries:s+='\n'+block;entries[k]=block
aliases={
'BM97':{'canonical':'BierstoneMilman1997','identity_evidence':'Exact title, authors and arXiv alg-geom/9508005; the theorem locators explicitly refer to the preprint, not journal pages.'},
'CDP2020':{'canonical':'CDP20','identity_evidence':'Same Campana–Demailly–Peternell 2020 title and DOI10.1112/S0010437X19007802; attached-source pagination remains explicitly identified.'},
'Grauert60':{'canonical':'Grauert1960D','identity_evidence':'Same 1960 Grauert direct-image article and printed Section6/7 locators; existing sign-source record names this same item.'},
'Fujimoto1988Root':{'canonical':'Fujimoto1988Log','identity_evidence':'Identical author, title, journal28(1),pp91–110,1988 and reproduced source URL. Only the recorded pp91–92,96–97,99 passages are inherited.'},
'ViaclovskyLog2026':{'canonical':'manViaclovskyLogs26','identity_evidence':'Same attached arXiv2610.39102v1 author source. Only the recorded local logarithmic-filling statements are inherited.'},
'ViaclovskyTwo2026':{'canonical':'Viaclovsky2026Two','identity_evidence':'Same attached arXiv2609.33785v1 author source; source-edition locators remain unchanged.'}
}
for alias,rec in aliases.items():
 if alias not in entries:
  block=entries[rec['canonical']]
  block=re.sub(r'^(@\w+\{)[^,]+,',lambda m:m[1]+alias+',',block,count=1)
  s+='\n'+block;entries[alias]=block
 rec['additional_independent_reading_credit']=False
f.write_text(s)
(P/'analysis/bibliography_aliases.json').write_text(json.dumps(aliases,indent=2,ensure_ascii=False))
print('Installed missing canonical entries and',len(aliases),'documented aliases.')
