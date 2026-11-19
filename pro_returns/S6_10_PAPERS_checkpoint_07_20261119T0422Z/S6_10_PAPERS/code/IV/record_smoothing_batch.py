"""Record completed whole-proof and bounded execution scopes."""
from pathlib import Path
import csv,datetime,json
root=Path(__file__).resolve().parents[2]
dest=root/'analysis/IV'
events=json.loads((dest/'current_check_events.json').read_text())
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
checker='GPT-6 Astra Pro (OpenAI, ChatGPT; current writing, 18 November 2026)'
new=[
('IV-D-030','D',['maps:src:B.6.1'],'proved','Actual sixfold mapping-torus cover and complete residue fibres',
 'Replaced the old conditional residue phrasing by the unconditional homomorphism mu6:Z/28 to Z/28, a maps to6a. The actual cover is [x,t] maps to[x,6t] from M_(Phi^6) to M_Phi; the endpoint relation [x,6t+6]=[Phi^6 x,6t] proves it is well defined. Its class is6a under the actual sphere-gluing group isomorphism. Solving6a=2r gives a=5r modulo14, hence the two fibres5r and5r+14; odd targets have no preimage, the kernel is{0,14} and the image is the even subgroup. No unknown geometric residue is assigned.',
 ['papers/IV/body.tex']),
('IV-D-031','D',['maps:src:B.6.3'],'proved','Full smoothing monodromy on integral middle cohomology',
 'Read and rederived the complete proof. The added logarithm L_s of1-st cancels exactly between beta_c,s and ell_s, retaining b_h and the explicit scalar h_s^12=t^4/((t-1)^3(1-st)). The actual finite/root/cusp maps give A1,A2,Cw,Cd with product one; S=I-2E commutes with all four. Re-derived the local invariant-cycle identifications for every exterior degree using finite free transfer and the actual degree-zero line translations in the nodal product. In exterior degree2 the four image ranks are4,4,2,2; relation and coboundary ranks are5 each, leaving H1 dimension2. Computed the displayed P1–4 representatives and both exact coboundaries for wedge^2(S^-t)-I. The base has cohomological dimension2, so E2^(1,2) survives; b3=2 from the stated earlier integral topology exhausts it. The resulting rational identity on H3, together with its integral torsion freeness, proves the integral identity.',
 ['papers/IV/body.tex','code/IV/replay_smoothing/current_execution.json']),
('IV-D-032','D',['maps:src:B.6.4'],'proved','Full affine defects, critical-cycle vanishing and central mapping class',
 'Read and rederived the full proof, including the local-to-global spectral-sequence step. The two actual affine defects are(0,1,-1,-1) and(0,0,-1,1), and d1+A1d2=0. The nil-fibre differential is dtheta=2kappa gamma. Under the full inverse-transpose actions, (Cw*-I)gamma omega=-gamma u and (A2tilde*-I)gamma u=gamma omega-gamma u-gamma kappa, with gamma kappa exact; thus both candidate Wang classes die in global coinvariants. The local rank-one-zero critical fibres contribute precisely the two skyscraper classes kappa gamma u and kappa gamma omega. Their connecting map has representatives -gamma u/2,-gamma omega/2 and is zero by the just computed coinvariants. There are no higher differentials, and the Wang b3 count exhausts global H3. Restricting to the actual critical traces makes gamma a multiple of kappa, proving their rational homology classes zero. For the complex vertical bundle, the saturated rank-two subbundle has a nowhere-zero abstract section and c2=0; the K-class identity [E]=[V]+[L]-[L|C] and the local Koszul resolution give c2(E)=PD[C], hence p1=-2PD[C]=0 rationally and then integrally by H4=Z^2. Opened Krylov §2.1 pp2–4: the actual normal-clutch map detects the two stable generators by absolute Pontryagin number4, and its zero kernel is the supported-disc Theta7 subgroup because S3 times S3 bounds the framed S3 times D4. The stated conclusion therefore follows for the actual return.',
 ['papers/IV/body.tex','code/IV/replay_smoothing/current_execution.json','analysis/IV/references/Krylov2001.pdf']),
('IV-D-033','D',['fam:src:E.2.2'],'proved','Actual positive loop, two-disc gluing isomorphism and spin filling',
 'Read the complete proof and rederived the positive loop c(r)=c0-2r, its closing map F_(2,c0-2), and the connection-independence isotopy. The glued oriented seven-manifold is a homotopy sphere by van Kampen and integral Mayer–Vietoris. Opened Milnor1965 Theorem9.1p107 and PropositionsA–Bpp108–110 with their full displayed proofs, then inserted the exact two-ball complement, relative homology vanishing and product boundary parametrization. The parametrized-ball isotopy gives injectivity up to a disc extension; the opened Cerf1970Theorem0/Corollaries1–2p8 turn that extension into isotopy. Smale1961TheoremJp393 identifies oriented h-cobordism and diffeomorphism classes. Opened Eells–Kuiper1962§3p96 and§6pp101–103; the explicit h=2 rank-four disc bundle has Euler1,p1=6x,signature1 and mu1/28. Boundary sums and orientation reversal supply a spin filling of every class, including the actual Sigma_Phi. Vanishing rational H3/H4 on the boundary makes the relative Pontryagin lift unique. The exact formula divided by896 and multiplied by28 gives the displayed residue modulo28.',
 ['papers/IV/body.tex','analysis/IV/references/Milnor1965.pdf','analysis/IV/references/Cerf1970.pdf','analysis/IV/references/EellsKuiper1962.pdf']),
('IV-C-007','C',['maps:src:B.6.3','maps:src:B.6.4'],'pass','Current exact smoothing and mapping-torus programs',
 'Read both received programs and executed unchanged copies at03:46:50–51UTC. Source/copy SHA256 values agree in current_execution.json. The smoothing program reproduces the exterior-square image/relation/coboundary ranks, all displayed cocycles and the exact correction coboundaries. The mapping-torus program reproduces the nilmanifold cohomology and verifies that gamma u and gamma omega vanish in global coinvariants. The generic nil-fibre invariant classes are not asserted to extend globally: the manuscript proof separately uses the actual skyscraper and connecting-map calculation.',
 ['code/IV/replay_smoothing/current_execution.json','code/IV/replay_smoothing/maps_smoothing_monodromy.current.stdout','code/IV/replay_smoothing/maps_mapping_torus_cohom.current.stdout'])
]
seen={x['event_id'] for x in events}
for eid,typ,labels,verdict,scope,derivation,artifacts in new:
 if eid in seen:raise RuntimeError(eid+' already recorded')
 events.append(dict(event_id=eid,type=typ,labels=labels,verdict=verdict,scope=scope,derivation=derivation,checker=checker,recorded_at=now,artifacts=artifacts))
(dest/'current_check_events.json').write_text(json.dumps(events,indent=2)+'\n')
cols=['event_id','type','labels','verdict','scope','derivation','checker','recorded_at','artifacts']
with (dest/'current_check_events.tsv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=cols,delimiter='\t');w.writeheader()
 for rec in events:w.writerow({k:'; '.join(rec[k]) if isinstance(rec.get(k),list) else rec.get(k,'') for k in cols})
print(json.dumps({'recorded_at':now,'events_added':len(new),'D_labels':len({x for e in events if e['type']=='D' for x in e['labels']})}))
