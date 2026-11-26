"""Apply the wholly read, III-only bibliography publication candidate.

Citation substitutions belong to root and must already be complete.  This
editor preserves all surviving bibliography keys and every literal label or
hypertarget, records exact old/new entries in the local defects table, and
does not edit canonical source, body fragments, or shared records.
"""
from collections import Counter
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import csv
import re

ROOT = Path(__file__).resolve().parents[1]
REL = 'agents/continuation8_iii_integration/units/root/bibliography.tex'
SOURCE = ROOT / REL
RECORD = ROOT / 'agents/continuation8_iii_later/S6_SERIES_PUBLISH_III_bibliography_publication_defects.tsv'
EXPECTED = '49b76992a53e7606a53f8a418a67413414849132c6ab5df8ffcbe4e890c73bf4'

NEW = r'''\begin{thebibliography}{99}
\providecommand{\natexlab}[1]{#1}
\providecommand{\doi}[1]{\url{https://doi.org/#1}}

\bibitem[Andrus(1977)]{manAndrus77}
D.~G. Andrus.
\newblock \emph{Classification of Certain 6-Manifolds}.
\newblock M.Sc. thesis, McMaster University, January 1977.
\newblock \url{https://hdl.handle.net/11375/9107}.

\bibitem[Atiyah and Bott(1984)]{AtiyahBott1984}
M.~F. Atiyah and R.~Bott.
\newblock The moment map and equivariant cohomology.
\newblock \emph{Topology} \textbf{23} (1984), no.~1, 1--28.
\newblock \doi{10.1016/0040-9383(84)90021-1}.

\bibitem[Atiyah et~al.(1975)Atiyah, Patodi, and Singer]{mapsAPS2}
M.~F. Atiyah, V.~K. Patodi, and I.~M. Singer.
\newblock Spectral asymmetry and Riemannian geometry.~II.
\newblock \emph{Mathematical Proceedings of the Cambridge Philosophical Society}
\textbf{78} (1975), no.~3, 405--432.
\newblock \doi{10.1017/S0305004100051872}.

\bibitem[Atiyah and Singer(1968)]{AtiyahSinger1968IIIE}
M.~F. Atiyah and I.~M. Singer.
\newblock The index of elliptic operators.~III.
\newblock \emph{Annals of Mathematics} \textbf{87} (1968), no.~3, 546--604.
\newblock \doi{10.2307/1970717}.

\bibitem[Barden(1965)]{manBarden65}
D.~Barden.
\newblock Simply connected five-manifolds.
\newblock \emph{Annals of Mathematics} \textbf{82} (1965), no.~3, 365--385.
\newblock \doi{10.2307/1970702}.

\bibitem[Baues(1998)]{CuspInvariantBaues1998}
Hans-Joachim Baues.
\newblock The degree of maps between certain 6-manifolds.
\newblock \emph{Compositio Mathematica} \textbf{110} (1998), 51--64.
\newblock \doi{10.1023/A:1000203804884}.

\bibitem[Besser and Livn\'e(2012)]{manBesserLivne12}
Amnon Besser and Ron Livn\'e.
\newblock Picard--Fuchs equations of families of QM abelian surfaces.
\newblock arXiv:1202.2808v2, 14 February 2012.
\newblock \url{https://arxiv.org/abs/1202.2808v2}.

\bibitem[Borel and Serre(1953)]{BorelSerre1953}
Armand Borel and Jean-Pierre Serre.
\newblock Groupes de Lie et puissances r\'eduites de Steenrod.
\newblock \emph{American Journal of Mathematics} \textbf{75} (1953), no.~3, 409--448.
\newblock \doi{10.2307/2372495}.

\bibitem[Bott(1959)]{mapsBott59}
Raoul Bott.
\newblock The stable homotopy of the classical groups.
\newblock \emph{Annals of Mathematics} \textbf{70} (1959), no.~2, 313--337.
\newblock \doi{10.2307/1970106}.

\bibitem[Brown(1972)]{ffBrown72}
Edgar~H. Brown, Jr.
\newblock Generalizations of the Kervaire invariant.
\newblock \emph{Annals of Mathematics} \textbf{95} (1972), no.~2, 368--383.
\newblock \doi{10.2307/1970804}.

\bibitem[Brown(1982)]{manBrown82}
Kenneth~S. Brown.
\newblock \emph{Cohomology of Groups}.
\newblock Graduate Texts in Mathematics, vol.~87, Springer-Verlag, New York, 1982.
\newblock \doi{10.1007/978-1-4684-9327-6}.

\bibitem[Burklund et~al.(2023)Burklund, Hahn, and Senger]{BHS19}
Robert Burklund, Jeremy Hahn, and Andrew Senger.
\newblock On the boundaries of highly connected, almost closed manifolds.
\newblock \emph{Acta Mathematica} \textbf{231} (2023), no.~2, 205--344.
\newblock \doi{10.4310/ACTA.2023.v231.n2.a1}.
\newblock Page references use arXiv:1910.14116v3, 10 May 2022.
\newblock \url{https://arxiv.org/abs/1910.14116v3}.

\bibitem[Campana et~al.(1998)Campana, Demailly, and Peternell]{manCDP98}
Fr\'ed\'eric Campana, Jean-Pierre Demailly, and Thomas Peternell.
\newblock The algebraic dimension of compact complex threefolds with vanishing
second Betti number.
\newblock \emph{Compositio Mathematica} \textbf{112} (1998), no.~1, 77--91.
\newblock \doi{10.1023/A:1000313214795}.

\bibitem[Cartan(1954--1955)]{manCartan1955EML}
Henri Cartan.
\newblock D\'etermination des alg\`ebres \(H_*(\pi,n;\mathbf Z)\).
\newblock \emph{S\'eminaire Henri Cartan} \textbf{7} (1954--1955),
no.~1, expos\'e~11, 11-01--11-24, 31 January 1955.
\newblock \url{https://www.numdam.org/item/SHC_1954-1955__7_1_A11_0/}.

\bibitem[Cerf(1970)]{Cerf1970}
Jean Cerf.
\newblock La stratification naturelle des espaces de fonctions
diff\'erentiables r\'eelles et le th\'eor\`eme de la pseudo-isotopie.
\newblock \emph{Publications Math\'ematiques de l'IH\'ES} \textbf{39} (1970), 5--173.
\newblock \doi{10.1007/BF02684687}.

\bibitem[Claude and Alp{\"o}ge(2026)]{AC26}
Claude and Levent Alp{\"o}ge.
\newblock The $(3,4,\infty)$ modular family of $2$-tori, completed at its three
special points, is a complex structure on $S^6$.
\newblock Preprint, 2026, 108~pp.
\newblock \url{https://alpo.ge/s6.pdf}.

\bibitem[Debray and Gunningham(2018)]{DebrayGunningham2018Root}
Arun Debray and Sam Gunningham.
\newblock The Arf--Brown TQFT of $\mathrm{Pin}^-$ surfaces.
\newblock In \emph{Topology and Quantum Theory in Interaction},
Contemporary Mathematics, vol.~718, American Mathematical Society,
Providence, 2018, 49--87.
\newblock \doi{10.1090/conm/718/14478}.
\newblock Page references use arXiv:1803.11183v1, 29 March 2018,
whose title page is dated 30 March 2018.
\newblock \url{https://arxiv.org/abs/1803.11183v1}.

\bibitem[Demailly(2012)]{mapsDemailly2012CADG}
Jean-Pierre Demailly.
\newblock \emph{Complex Analytic and Differential Geometry}.
\newblock Version of 21 June 2012.
\newblock \url{https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf}.

\bibitem[Edixhoven and Lido(2023)]{manEdixhovenLido23}
B.~Edixhoven and G.~Lido.
\newblock Geometric quadratic Chabauty.
\newblock \emph{Journal of the Institute of Mathematics of Jussieu}
\textbf{22} (2023), no.~1, 279--333.
\newblock \doi{10.1017/S1474748021000244}.

\bibitem[Engel(2026{\natexlab{a}})]{E26}
Philip Engel.
\newblock Complex structures on $S^6$.
\newblock arXiv:2609.38442v1, 29 September 2026.
\newblock \url{https://arxiv.org/abs/2609.38442v1}.

\bibitem[Engel(2026{\natexlab{b}})]{manExplorer26}
Philip Engel.
\newblock Threefold explorer, 2026.
\newblock \url{https://philip-engel.github.io/threefold-explorer/}.

\bibitem[Fukae(2002)]{manFukae02}
Mitsuaki Fukae.
\newblock Monodromies of rational elliptic surfaces and extremal elliptic K3 surfaces.
\newblock arXiv:math/0205062v1, 7 May 2002.
\newblock \url{https://arxiv.org/abs/math/0205062v1}.

\bibitem[Galaz-Garc\'{i}a and Reiser(2025)]{manGR25}
Fernando Galaz-Garc\'{i}a and Philipp Reiser.
\newblock Free torus actions and twisted suspensions.
\newblock \emph{Forum of Mathematics, Sigma} \textbf{13} (2025), e3.
\newblock \doi{10.1017/fms.2024.141}.

\bibitem[Grauert(1960)]{Grauert1960Coherent}
Hans Grauert.
\newblock Ein Theorem der analytischen Garbentheorie und die
Modulr\"aume komplexer Strukturen.
\newblock \emph{Publications Math\'ematiques de l'IH\'ES} \textbf{5} (1960), 5--64.
\newblock \doi{10.1007/BF02684746}.

\bibitem[Grauert(1963)]{Grauert1963Correction}
Hans Grauert.
\newblock Berichtigung: Ein Theorem der analytischen Garbentheorie und die
Modulr\"aume komplexer Strukturen.
\newblock \emph{Publications Math\'ematiques de l'IH\'ES} \textbf{16} (1963), 35--36.
\newblock \doi{10.1007/BF02684291}.

\bibitem[Grothendieck(2003)]{SGA1Recomposed2004}
A.~Grothendieck (dir.), with two additional expos\'es by M.~Raynaud.
\newblock \emph{Rev\^etements \'etales et groupe fondamental (SGA~1)}.
\newblock Recomposed and annotated edition, Documents Math\'ematiques, vol.~3,
Soci\'et\'e Math\'ematique de France, 2003.
\newblock \url{https://smf.emath.fr/node/43215}.
\newblock Page references use arXiv:math/0206203v2, 4 January 2004.
\newblock \url{https://arxiv.org/abs/math/0206203v2}.

\bibitem[Hatcher(2002)]{Hatcher2002}
Allen Hatcher.
\newblock \emph{Algebraic Topology}.
\newblock Cambridge University Press, Cambridge, 2002.
\newblock \url{https://pi.math.cornell.edu/~hatcher/AT/AT.pdf}.

\bibitem[Hatcher(2017)]{CuspInvariantHatcherVB}
Allen Hatcher.
\newblock \emph{Vector Bundles and K-Theory}.
\newblock Version~2.2, November 2017.
\newblock \url{https://pi.math.cornell.edu/~hatcher/VBKT/VB.pdf}.

\bibitem[Hatcher(n.d.)]{HatcherSpectralSequences}
Allen Hatcher.
\newblock Spectral sequences.
\newblock Additional Chapter~5 of \emph{Algebraic Topology}, preliminary version.
\newblock \url{https://pi.math.cornell.edu/~hatcher/AT/ATch5.pdf}.

\bibitem[Herfurtner(1990)]{manHerfurtner90}
Stephan Herfurtner.
\newblock Elliptic surfaces with four singular fibres.
\newblock Max-Planck-Institut f\"ur Mathematik preprint MPI/90-28, 1990.
\newblock \url{https://archive.mpim-bonn.mpg.de/id/eprint/860/1/preprint_1990_28.pdf}.

\bibitem[Isaksen et~al.(2023)Isaksen, Wang, and Xu]{IsaksenWangXu2023}
Daniel~C. Isaksen, Guozhen Wang, and Zhouli Xu.
\newblock Stable homotopy groups of spheres: from dimension 0 to 90.
\newblock \emph{Publications Math\'ematiques de l'IH\'ES} \textbf{137} (2023), 107--243.
\newblock \doi{10.1007/s10240-023-00139-1}.

\bibitem[Iwase(2022)]{IwaseWhitney2022}
N.~Iwase.
\newblock Whitney approximation for smooth CW complex.
\newblock \emph{Kyushu Journal of Mathematics} \textbf{76} (2022), no.~1, 177--186.
\newblock \doi{10.2206/kyushujm.76.177}.
\newblock Page references use arXiv:2001.02893v4, 5 July 2021.
\newblock \url{https://arxiv.org/abs/2001.02893v4}.

\bibitem[Johnson(1980)]{Johnson1980Root}
Dennis Johnson.
\newblock Spin structures and quadratic forms on surfaces.
\newblock \emph{Journal of the London Mathematical Society} (2)
\textbf{22} (1980), no.~2, 365--373.
\newblock \doi{10.1112/jlms/s2-22.2.365}.

\bibitem[Kaplan(1979)]{mapsKaplan79}
Steve~J. Kaplan.
\newblock Constructing framed 4-manifolds with given almost framed boundaries.
\newblock \emph{Transactions of the American Mathematical Society}
\textbf{254} (1979), 237--263.
\newblock \doi{10.1090/S0002-9947-1979-0539917-X}.

\bibitem[Kas(1980)]{Kas1980}
Arnold Kas.
\newblock On the handlebody decomposition associated to a Lefschetz fibration.
\newblock \emph{Pacific Journal of Mathematics} \textbf{89} (1980), no.~1, 89--104.
\newblock \doi{10.2140/pjm.1980.89.89}.

\bibitem[Kervaire and Milnor(1963)]{manKM63}
Michel~A. Kervaire and John~W. Milnor.
\newblock Groups of homotopy spheres.~I.
\newblock \emph{Annals of Mathematics} \textbf{77} (1963), no.~3, 504--537.
\newblock \doi{10.2307/1970128}.

\bibitem[Li(1995)]{mapsLi1995Cycles}
Yingchen Li.
\newblock Analytic cycles and generically finite holomorphic maps.
\newblock \emph{Bulletin of the Australian Mathematical Society}
\textbf{52} (1995), 457--460.
\newblock \doi{10.1017/S0004972700014933}.

\bibitem[Liu and Rollenske(2026)]{manLR26}
Wenfei Liu and S{\"o}nke Rollenske.
\newblock Yet another family of complex structures on $S^6$.
\newblock arXiv:2609.33826v2, 9 October 2026.
\newblock \url{https://arxiv.org/abs/2609.33826v2}.

\bibitem[Milne(2017)]{mapsMilne2017}
James~S. Milne.
\newblock \emph{Modular Functions and Modular Forms (Elliptic Modular Curves)}.
\newblock Version~1.31, 22 March 2017.
\newblock \url{https://www.jmilne.org/math/CourseNotes/MF.pdf}.

\bibitem[Milnor(1964)]{MilnorDifferentialTopology1964}
John~W. Milnor.
\newblock Differential topology.
\newblock In Thomas~L. Saaty (ed.), \emph{Lectures on Modern Mathematics},
vol.~2, John Wiley and Sons, New York, 1964, 165--183.

\bibitem[Milnor(1965{\natexlab{a}})]{mapsMilnor65}
John~W. Milnor.
\newblock \emph{Lectures on the $h$-Cobordism Theorem}.
\newblock Notes by L.~Siebenmann and J.~Sondow.
\newblock Princeton University Press, Princeton, New Jersey, 1965.

\bibitem[Milnor(1965{\natexlab{b}})]{CuspNullMilnor1965}
John~W. Milnor.
\newblock \emph{Topology from the Differentiable Viewpoint}.
\newblock University Press of Virginia, Charlottesville, 1965.

\bibitem[Milnor and Stasheff(1974)]{MilnorStasheff1974}
John~W. Milnor and James~D. Stasheff.
\newblock \emph{Characteristic Classes}.
\newblock Annals of Mathematics Studies, vol.~76,
Princeton University Press, Princeton, 1974.
\newblock \doi{10.1515/9781400881826}.

\bibitem[Miranda(1990)]{manMiranda90}
Rick Miranda.
\newblock Persson's list of singular fibers for a rational elliptic surface.
\newblock \emph{Mathematische Zeitschrift} \textbf{205} (1990), 191--211.
\newblock \doi{10.1007/BF02571235}.
\newblock \url{https://www.math.colostate.edu/~miranda/preprints/Perssonslist.pdf}.

\bibitem[Oguiso and Shioda(1991)]{manOguisoShioda91}
Keiji Oguiso and Tetsuji Shioda.
\newblock The Mordell--Weil lattice of a rational elliptic surface.
\newblock \emph{Commentarii Mathematici Universitatis Sancti Pauli}
\textbf{40} (1991), 83--99.
\newblock \url{https://rikkyo.repo.nii.ac.jp/record/10006/files/AA00610867_40-01_08.pdf}.

\bibitem[Pontryagin(1950)]{Pontryagin1950Root}
L.~S. Pontryagin.
\newblock Homotopy classification of the mappings of an $(n+2)$-dimensional
sphere on an $n$-dimensional one.
\newblock \emph{Doklady Akademii Nauk SSSR} \textbf{70} (1950), 957--959 (Russian).

\bibitem[Pontryagin(1955, 1959)]{Pontryagin1955Root}
L.~S. Pontryagin.
\newblock Smooth manifolds and their applications in homotopy theory.
\newblock \emph{Trudy Matematicheskogo Instituta imeni V.~A.~Steklova}
\textbf{45}, Academy of Sciences of the USSR, Moscow, 1955, 3--139 (Russian).
\newblock \url{https://www.mathnet.ru/eng/tm1181}.
\newblock English translation by P.~J. Hilton, \emph{American Mathematical
Society Translations}, Series~2, vol.~11, 1959, 1--114.
Page references use this English translation.
\newblock \url{https://bookstore.ams.org/trans2-11}.

\bibitem[Redden(2011)]{Redden2011StringStructures}
Corbett Redden.
\newblock String structures and canonical 3-forms.
\newblock \emph{Pacific Journal of Mathematics} \textbf{249} (2011), no.~2, 447--484.
\newblock \doi{10.2140/pjm.2011.249.447}.
\newblock Page references use arXiv:0912.2086v2, 8 February 2011.
\newblock \url{https://arxiv.org/abs/0912.2086v2}.

\bibitem[Reiser(2024)]{manReiser24}
Philipp Reiser.
\newblock Positive Ricci curvature on twisted suspensions.
\newblock \emph{International Mathematics Research Notices}
\textbf{2024} (2024), no.~22, 14115--14137.
\newblock \doi{10.1093/imrn/rnae231}.

\bibitem[Sch\"utt and Shioda(2010)]{manSS10}
Matthias Sch\"utt and Tetsuji Shioda.
\newblock Elliptic surfaces.
\newblock In \emph{Algebraic Geometry in East Asia---Seoul 2008},
Advanced Studies in Pure Mathematics, vol.~60,
Mathematical Society of Japan, Tokyo, 2010, 51--160.
\newblock \doi{10.2969/aspm/06010051}.
\newblock Page references use arXiv:0907.0298v3, 9 July 2010.
\newblock \url{https://arxiv.org/abs/0907.0298v3}.

\bibitem[The Stacks Project Authors(2026)]{StacksProject}
The Stacks Project Authors.
\newblock \emph{The Stacks Project}, 2026.
\newblock \url{https://stacks.math.columbia.edu}.

\bibitem[Telen(2022)]{TelenToric2022}
S.~Telen.
\newblock Introduction to toric geometry.
\newblock arXiv:2203.01690v1, 3 March 2022.
\newblock \url{https://arxiv.org/abs/2203.01690v1}.

\bibitem[Teschl(2012)]{TeschlODE2012}
Gerald Teschl.
\newblock \emph{Ordinary Differential Equations and Dynamical Systems}.
\newblock Graduate Studies in Mathematics, vol.~140,
American Mathematical Society, Providence, 2012.
\newblock Page references use the author's preliminary version.
\newblock \url{https://www.mat.univie.ac.at/~gerald/ftp/book-ode/ode.pdf}.

\bibitem[Thomas(1956)]{ffThomas56}
Emery Thomas.
\newblock A generalization of the Pontrjagin square cohomology operation.
\newblock \emph{Proceedings of the National Academy of Sciences of the
United States of America} \textbf{42} (1956), no.~5, 266--269.
\newblock \doi{10.1073/pnas.42.5.266}.

\bibitem[Thomas(1959)]{ffThomas1959Suspension}
Emery Thomas.
\newblock The suspension of the generalized Pontrjagin cohomology operations.
\newblock \emph{Pacific Journal of Mathematics} \textbf{9} (1959), no.~3, 897--911.
\newblock \url{https://msp.org/pjm/1959/9-3/pjm-v9-n3-p26-p.pdf}.

\bibitem[Toda(1952)]{mapsToda52}
Hirosi Toda.
\newblock Some relations in homotopy groups of spheres.
\newblock \emph{Journal of the Institute of Polytechnics, Osaka City
University, Series~A} \textbf{2} (1952), no.~2, 71--80.
\newblock \url{https://www.i-repository.net/contents/osakacu/sugaku/DB-M-002-02-01.pdf}.

\bibitem[Ulmer and Urz\'ua(2021)]{manUU21}
Douglas Ulmer and Giancarlo Urz\'ua.
\newblock Bounding tangencies of sections on elliptic surfaces.
\newblock \emph{International Mathematics Research Notices}
\textbf{2021} (2021), no.~6, 4768--4802.
\newblock \doi{10.1093/imrn/rnaa222}.
\newblock Page references use arXiv:2002.01906v2, 26 May 2020.
\newblock \url{https://arxiv.org/abs/2002.01906v2}.

\bibitem[Viaclovsky(2026{\natexlab{a}})]{manViaclovskyLogs26}
Jeff Viaclovsky.
\newblock Logarithmic transformations on the six-sphere.
\newblock arXiv:2610.39102v1, 29 October 2026.
\newblock \url{https://arxiv.org/abs/2610.39102v1}.

\bibitem[Viaclovsky(2026{\natexlab{b}})]{manViaclovskyTwo26}
Jeff Viaclovsky.
\newblock A two-parameter family of complex structures on $S^6$.
\newblock arXiv:2609.33785v1, 27 September 2026.
\newblock \url{https://arxiv.org/abs/2609.33785v1}.

\bibitem[Waldhausen(1968)]{mapsWaldhausen68}
Friedhelm Waldhausen.
\newblock On irreducible 3-manifolds which are sufficiently large.
\newblock \emph{Annals of Mathematics} \textbf{87} (1968), no.~1, 56--88.
\newblock \doi{10.2307/1970594}.

\bibitem[Wang(2026)]{manWang26}
Zichang Wang.
\newblock A complex structure on a rational homology six-sphere with two-torsion.
\newblock arXiv:2609.11541v2, 2026.
\newblock \url{https://arxiv.org/abs/2609.11541v2}.

\bibitem[Whitehead(1950)]{mapsWhitehead50}
J.~H.~C. Whitehead.
\newblock The secondary boundary operator.
\newblock \emph{Proceedings of the National Academy of Sciences of the
United States of America} \textbf{36} (1950), no.~1, 55--60.
\newblock \doi{10.1073/pnas.36.1.55}.

\bibitem[Yang(2026)]{manYang26}
Xiufan Yang.
\newblock Compact complex threefolds fibred by two-dimensional complex tori.
\newblock arXiv:2609.29666v1, 13 September 2026.
\newblock \url{https://arxiv.org/abs/2609.29666v1}.

\bibitem[Zhubr(1975)]{manZhubr75}
A.~V. Zhubr.
\newblock Classification of simply-connected six-dimensional spinor manifolds.
\newblock \emph{Mathematics of the USSR-Izvestiya} \textbf{9} (1975), no.~4, 793--812.
\newblock \doi{10.1070/IM1975v009n04ABEH001498}.
\newblock English edition.

\bibitem[Zhubr(2010)]{manZhubr2010Gamma}
A.~V. Zhubr.
\newblock An exotic invariant for 6-manifolds: the direct construction.
\newblock \emph{St. Petersburg Mathematical Journal} \textbf{21} (2010), no.~3, 469--482.
\newblock \doi{10.1090/S1061-0022-10-01104-0}.

\bibitem[Zhubr(2013)]{ffZhubr13}
A.~V. Zhubr.
\newblock On the definition of ``exotic'' invariant for simply connected closed
6-dimensional spin manifolds.
\newblock \emph{Izvestia Komi Science Centre of the Ural Division of the
Russian Academy of Sciences} (2013), no.~4(16), 4--10.
\newblock \url{https://izvestia.komisc.ru/Archive/i16.pdf}.

\end{thebibliography}

\end{document}
'''

DUPLICATES = {
    'mapsAC26': 'AC26', 'manEngel26': 'E26', 'mapsEngel': 'E26',
    'mapsHatcher02': 'Hatcher2002', 'manSchuettShioda10': 'manSS10',
    'mapsLR': 'manLR26', 'mapsVia2': 'manViaclovskyTwo26',
    'mapsViaLog': 'manViaclovskyLogs26',
}
SPECIAL = {
    'AC26': 'Keep the exact Claude/Alpoge manuscript and author order, correct S^6 capitalization, remove attachment/process language, and consolidate its identical key after root citation replacement.',
    'manBrown82': 'Retain the 1982 GTM87 book and exact DOI from the wholly read staged LI record; remove the unrelated Hangzhou lecture-notes URL.',
    'BHS19': 'Add the opened publisher Acta231(2),2023,205--344 and exact DOI; retain the actually used arXiv1910.14116v3 pagination,10May2022. No published/preprint page equivalence is asserted.',
    'DebrayGunningham2018Root': 'Add the author/archive-confirmed Contemp.Math.718 publication and DOI; preserve the actual v1 PDF edition and its printed p.6 by an explicit preprint pagination convention.',
    'Pontryagin1955Root': 'Correct the edition-to-page relationship: the actual linked scan is Hilton English translation AMS Translations(2)11,1959,1--114, with Theorem24 on109--112. Retain original Russian1955 data separately; no page identification between languages is claimed.',
    'Pontryagin1950Root': 'Retain the actual Russian Doklady70,1950,957--959 article, whose original three printed pages were visually opened; remove the third-party scan URL and state the language.',
    'manLR26': 'Fix arXiv2609.33826v2,9Oct2026: actual downloaded PDF exactly matches the admitted c5 SHA; local pp.7--8,11--14 and Theorem5.1 p.21 read. Consolidation follows root actual five citation replacements.',
    'manViaclovskyTwo26': 'Fix the sole posted arXiv2609.33785v1,27Sep2026; actual title/version and Thm1.1/Prop6.4 pages read. Consolidation follows root actual four citation replacements.',
    'manViaclovskyLogs26': 'Fix the sole posted arXiv2610.39102v1,29Oct2026; actual title/version and Cor4.6 p.14 read. Consolidation follows root actual five citation replacements.',
    'manSS10': 'Preserve both the exact published chapter identity and the admitted v3 preprint pagination; consolidate the duplicate v3 key after root citation replacement. DOI resolved to the publisher record and is corroborated by the opened AMS research bibliography.',
    'Redden2011StringStructures': 'Add the publication and DOI explicitly supplied by the primary arXiv record while preserving the admitted v2 pagination.',
    'manUU21': 'Retain the journal edition/DOI; identify the actually retrieved v2 preprint and its printed-page convention, matching the body local-period citations.',
    'mapsAPS2': 'Add publisher-verified issue3 and DOI10.1017/S0305004100051872; replace the third-party scan URL with this exact publisher identifier.',
    'AtiyahBott1984': 'Add the exact DOI from the wholly read LV source record and remove the third-party scan URL; retained publication and original page locators unchanged.',
    'manMiranda90': 'Add DOI10.1007/BF02571235 from the actual Springer metadata opening; preserve the author-hosted original article URL and its page numbers.',
    'mapsMilne2017': 'Specify author PDF version1.31,22March2017 from its actual title/version-page opening; the body page locators remain attached to that edition.',
    'ffThomas56': 'Retain the title and Emery Thomas author identity read on the actual article by the admitted LV review; do not propagate the older LP note title error.',
    'ffThomas1959Suspension': 'Retain actual article author Emery Thomas and publisher PDF; the publisher HTML metadata incorrectly says Thomas,Paul, so that machine field is not adopted. No unverified DOI is added.',
    'manZhubr75': 'Retain the English793--812 edition and DOI; remove the URL with conflicting option_lang=rus. The precise English primary locator remains in the source-reading record.',
    'Grauert1960Coherent': 'Remove Verified and the process pointer to the following item; the separately cited1963 correction remains its own bibliography entry with its exact DOI.',
    'manReiser24': 'Retain the existing key and publication identity although no current III citation was found; correct Ricci capitalization and use the DOI rather than a secondary deposited copy.',
    'mapsWhitehead50': 'Retain the existing key and publication identity although no current III citation was found; use its exact DOI rather than a third-party scan.',
}

def entries(text):
    end = text.index(r'\end{thebibliography}')
    matches = list(re.finditer(r'^\\bibitem(?:\[[^\n]*\])?\{([^}]+)\}', text[:end], re.M))
    out = {}
    for i, match in enumerate(matches):
        stop = matches[i+1].start() if i+1 < len(matches) else end
        key = match.group(1)
        assert key not in out
        out[key] = (text[match.start():stop].strip(), text.count('\n', 0, match.start())+1)
    return out

old = SOURCE.read_text()
assert sha256(old.encode()).hexdigest() == EXPECTED, 'Bibliography input changed'
before, after = entries(old), entries(NEW)
assert set(before) - set(after) == set(DUPLICATES)
assert not set(after) - set(before)
for macro in ['label', 'hypertarget']:
    pattern = rf'\\{macro}\{{([^{{}}]+)\}}'
    assert Counter(re.findall(pattern, old)) == Counter(re.findall(pattern, NEW))
cite_pattern = re.compile(r'\\cite[a-zA-Z]*\s*(?:\[[^\]]*\]\s*)*\{([^{}]+)\}', re.S)
citations = set()
for path in (ROOT / 'agents/continuation8_iii_integration/units').rglob('*.tex'):
    if path == SOURCE or path.name == 'preamble.tex':
        continue
    for match in cite_pattern.finditer(path.read_text()):
        citations.update(key.strip() for key in match.group(1).split(','))
assert not citations.intersection(DUPLICATES), 'Root citation replacement is incomplete'
assert citations <= set(after), 'A current III citation key is missing'
assert '\r' not in NEW and 'Verified' not in NEW

fields = ['change_id', 'type', 'statement_id', 'old_location', 'old_page',
          'new_location', 'new_page', 'old_text', 'new_text', 'reason', 'review_status']
status = ('Whole original695-line bibliography, exact body citation uses and stated staged source records read; '
          'complete semantic replacement authored/read and final whole-source readback required before handoff. '
          'Exposed source-local publication work only; no independent/required-check/criterion credit. '
          'Root owns canonical application, final reference/PDF gates and joint counts.')
with RECORD.open('w', newline='') as handle:
    writer = csv.DictWriter(handle, fieldnames=fields, delimiter='\t', lineterminator='\n')
    writer.writeheader()
    for i, (key, (old_entry, old_line)) in enumerate(before.items(), 1):
        owner = DUPLICATES.get(key, key)
        new_entry, new_line = after[owner]
        if key in DUPLICATES:
            reason = ('Consolidate the exact same opened edition under '+owner+
                      ' only after root replaced every actual citation key. '
                      'The new_text field is the retained owner entry; no runtime alias and no mathematical result deletion. '
                      'All literal label/hypertarget multiplicities are preserved.')
            kind = 'D18;D20'
        else:
            reason = SPECIAL.get(key, 'Retain the exact work, edition and publication data; apply the common bibliographic style, alphabetical placement, and remove process words. Keep stated version/page conventions and publisher/author/archive identifiers.')
            kind = 'D18;D20'
        writer.writerow(dict(change_id=f'c8-III-bibliography-{i:03d}', type=kind,
                             statement_id='bib:'+key, old_location=f'{REL}:{old_line}',
                             old_page='pending final concordance', new_location=f'{REL}:{new_line}',
                             new_page='pending final build', old_text=old_entry,
                             new_text=new_entry, reason=reason, review_status=status))
SOURCE.write_text(NEW)
print('UTC', datetime.now(timezone.utc).isoformat())
print('bibliography_before_sha256', EXPECTED)
print('bibliography_after_sha256', sha256(NEW.encode()).hexdigest())
print('all current III citation keys retained; retired identical-edition keys have no remaining citation uses')
print('literal labels and hypertarget multiplicities retained; no body or canonical source edited')
print('local defects written with LF; source-local bibliography candidate written')
