# Supplementary C.6 rank and derivative research record

## Status at first integration checkpoint, 15 November 2026

`sections/C_rank.tex` contains statements C.6.R1--R3, with explicit distinction between exact rank/primitivity results, numerical leading-term quotients, and the exact but unspecified positive rational factor provided by Gross--Zagier. `results_Crank.csv` and `records/Crank_summary.json` contain the numerical table. Parent owns Library, checkpoint and master integration.

All nine rank-one section points are primitive modulo torsion. Algebraic and analytic rank are two only at j=8000 and j=-12288000. The huge-conductor discriminant -163 curve has numerical BSD quotient 9, rather than 1, after full saturation. We do **not** infer exact Sha order from this numerical agreement.

## Executed computations

* Parent's `C_cm_models.gp/out`, `C_cm_local_heights.gp/out`, `C_cm_rank_lvalues.gp/out`: minimal models, local heights, exact descent bounds, first ten analytic derivatives and all eleven periods.
* `Crank_cm_theta_test.gp/out`: exact coefficient identity for first 10000 coefficients of both canonical CM curve and twist, for D=163 and d=185801.
* `Crank_cm_stream.cpp`: bounded-memory CM theta-series central derivative. Default build `g++ -O3 -I .apt/runtime/usr/include S6_05_ARITHMETIC/code/Crank_cm_stream.cpp -o S6_05_ARITHMETIC/code/Crank_cm_stream -lgmp /usr/lib/x86_64-linux-gnu/libmpfr.so.6`. Check build adds `-DWORK_PREC=512 -DWORK_RAD=96` and changes executable suffix to `_check`.
* `Crank_cm_stream_67.out`: D=67,d=217,cutoff170; agrees with PARI beyond65 digits.
* `Crank_cm_stream_163.out`: 384 bits, block radius128,cutoff170; omitted-tail bound1.68e-69, elapsed78sec.
* `Crank_cm_stream_163_check.out`:512 bits,radius96,cutoff190;915818441coefficients,69802132nonzero,tail3.10e-78,elapsed122sec. Independent block partition and precision agree beyond75 digits.
* `Crank_coefficients.gp/out`: first ten exact coefficient lists, cutoffs ceil(180sqrt(N)/(2pi)), stored `records/Crank_coeff_1.dat` through `_10.dat`. Warning: original GP write() appends; do not rerun without clearing or truncating those outputs first.
* `Crank_derivatives.cpp/out`:1024-bit direct E1 sum or rank-two G power series; largest tail3.46e-77. Both rank-two sums positive and hence analytic rank exactly2, using central zero from Coates--Wiles.
* `Crank_summary.py/out`:collates all results and checks numerical BSD quotients to69digits. No BSD equality is an input.
* `Crank_mwrank.in/out`: independent mwrank descent and full bases completed for first nine curves; run interrupted while computing tenth. The partial output and exit130 were retained. No last-two rank statement is attributed to this interrupted run.
* `Crank_saturation.cpp/out`:eclib20250122 full saturation of known P for all9rank-one curves; every automatic prime bound exhausted, index1, unsaturated-prime list empty. Uses200-bit real precision and exact finite-field maps. Runtime libraries under local `.apt/runtime`.
* `Crank_torsion_local.gp/out`: rational order4 and quadratic order6 minimal models and exact finite heights. A smaller unit-scaled quadratic model is E:y²=x³−(18+10sqrt3)x+(21+12sqrt3),P=(0,3+2sqrt3); its conjugate gives the other parameter. Natural rank overQ(sqrt3) still being checked by Simon descent at this checkpoint.

## Literature audit

1. Gross--Zagier (1986), *Heegner points and derivatives of L-series*, Invent.Math.84(2),225--320,doi10.1007/BF01388809. Opened original1985MPIM preprint https://archive.mpim-bonn.mpg.de/id/eprint/3578/1/preprint_1985_30.pdf . TheoremI.7.3 printedpp11--12; proofV.2pp125--130. ModularE/Q and centralzero yield rational-multiple relation to height of rationalR. Does not supply full BSD constant or Sha order.
2. Gross (1991), *Kolyvagin's work on modular elliptic curves*,LMSLNS153,235--256. Opened scannedPDF https://wstein.org/papers/bib/gross-kolyvagins_work_on_modular_elliptic_curves.pdf . Theorem1.3: nontorsionHeegnerpoint gives rank1 and finiteSha overauxiliaryimaginaryquadraticfield. Text extraction unavailable; detailed OCR/page verification is being pursued. The analytic-rank≤1 consequence with finiteSha is also explicitly printed in the independently opened Darmon notes below,p3.
3. Jetchev,Lauter,Stein (2008),JNT128,3394--3410, https://arxiv.org/pdf/0707.0032 opened. Theorem1.1 inarxivv1 statesanalyticrank≤1 impliesrankequality; do not cite that particularversionaloneforfiniteSha.
4. Rubin (1999), CIME notes https://swc-math.github.io/aws/1999/99RubinCM.pdf openedcomplete. Theorem10.1printedp47:nonzerocentralCMHeckeLvalue⇒finiteMW overCMfield. LaterTheorems12.13/12.19 concernrankzero pBSD, notrankone. FullCMhypothesis reachedbyisogenyfornonmaximalorders.
5. Rubin (1991),Invent.Math.103,25--68,doi10.1007/BF01239508. Authorbibliography andpublisherlandingpageopened; fullpaperbehindpublisherbarrier. No unverified claim that an ordinary-prime theorem proves fullBSD.
6. Bertolini,Darmon,Prasanna (2012),PacificJMath260(2),261--303,doi10.2140/pjm.2012.260.261, https://www.math.mcgill.ca/darmon/pub/Articles/Research/52.BDP2/bdp-pjm.pdf openedfull. Theorem1 restatesRubinrankonep-adicformula forfullCMcurveoverQ,splitgoodprimep,analyticrank1. Formula involvingKatzLp,formal-log-square,pperiod; noarchimedeanalgebraicityconclusion. Theorem2hasodd-discriminant/different-conductorhypotheses.
7. Castella (2025),*Tamagawa number conjecture for CM modular forms and Rankin--Selberg convolutions*,PLMS131(4),e70089,doi10.1112/plms.70089. https://web.math.ucsb.edu/~castella/Katz.pdf openedfull37pp,version14Feb2025. TheoremA:fullCM,abeliantorsionextensionoverK,Heckecentralorder1,p∤6hKsplit,conductorprimep,differentexactdivisibility. The lattermustbechecked; notautomaticforCMdiscriminant−16. Remark1.1.1explainsRubin1991F=Qconnection. Doesnotsettle3-partforK=Qsqrt−163.
8. Cremona,Siksek (2006),ANTS7LNCS4076,275--286, https://johncremona.github.io/papers/HeightLB.pdf openedfull. Theorem1andProp1provideheightlowerboundforpointsinallfiniteidentitycomponentsandrealidentitycomponent. Eclibsaturationappliesthisindexbound.
9. Darmon (2009),*Cycles on modular varieties and rational points on elliptic curves*,authorlecturenotes31Jul2009, https://www.math.mcgill.ca/darmon/pub/Articles/Expository/13.Oberwolfach/paper.pdf openedfull16pp. Section3,Assumption3.1andfollowingthetaformulaforclassnumberoneoddD; Section1p3statesrank≤1andfiniteShaimplication.
10. Simon(2002),*Computing the rank of elliptic curves over number fields*,LMSJCM5,7--17,doi10.1112/S1461157000000668. FullpublisherPDFopened. Paperrestrictsitsmainexpositiontonorational2torsion; softwareell.gphandles2torsionbyisogeny. Official https://simond.users.lmno.cnrs.fr/ ell.gp(version6Apr2011)andellcommon.gp(version6Sep2017)downloadedandpreservedunmodified. Thedefaultprobabilisticlocaltestflagwillbedisabledandbnfcertifyused.

## Independent C.7 review

Checked the positive Rosati central bracket and period-field elimination against BPSS source. Full ΩG includes quasi-periods; the Lie-period lattice alone would not suffice. At parent's request patched `C_periods.tex` to say full deRham--Betti matrix and prove the kernel over the semiabelian period torsor has only its central weight−2 part. No nonvanishing obstruction gap identified; the common sign in the polarization/extension convention does not affect positive proportionality of the two central brackets.
