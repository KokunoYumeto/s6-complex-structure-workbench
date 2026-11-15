"""Authorized current standalone B status reconciliation after B.4.33.

Preserves all theorem scopes and statuses.  Never edits master AB files,
B_global_noncompletion files, historical reports, or referee records.
Every changed passage and the original complete file are retained.
"""
from pathlib import Path
from datetime import datetime, timezone
import csv
import io
import json

ROOT = Path(__file__).resolve().parents[1]
replacements = {
 'sections/B_hodge_obstruction.tex': [(
  'The existence and least base-change exponent in B.4.1 therefore\nremain open in the unrestricted analytic category.',
  'These Hodge arguments alone give conditional restrictions, not\nunrestricted nonexistence. The latter is proved in B.4.33 for\nevery finite parameter cover, using the actual affine clutching.')],
 'sections/B_analytic_comparison_audit.tex': [(
  '\\paragraph{The remaining analytic comparison.}',
  '\\paragraph{Why automatic analytic comparison is not used.}'),(
  'that every proper analytic filling is one of these models. We have\nnot constructed that global log input with the required finite-place\nand cusp markings for the six-sphere family.',
  'that every proper analytic filling is one of these models.\nB.4.24 constructs the actual local Jacobian log input and isolates\nits affine torsor obstruction. B.4.33 derives an associated torsor\nfrom traces in a hypothetical cap; it does not identify that cap\nwith a proper fan model.'),(
  'unrestricted proof still needs a specific extension or boundedness\nargument for the comparison, or an actual non-toroidal cusp\nconstruction with the prescribed punctured restriction.',
  'unrestricted proof needs additional information beyond a\npunctured isomorphism. B.4.30--B.4.33 supply exactly such information:\nbounded differences of extending sections and a global radial-loop\ninvariant. Their contradiction proves nonexistence without extending\nan individual punctured isomorphism meromorphically.')],
 'sections/B_comparison_literature.tex': [(
  'failure directly. None of these comparisons closes B.4.',
  'failure directly. None of these automatic-comparison results\nproves the conclusion of B.4.33, whose argument instead uses\nextending-section differences and the global affine loop invariant.')],
 'sections/ab_push_parabolic_insertion.tex': [(
  '\\begin{remark}[The third component and the actual cusp remain open]',
  '\\begin{remark}[Auxiliary normal matching and the actual filling obstruction]'),(
  'If such a smoothing exists, its topological Euler number is\n$4+8-2\\chi(E)=12$ and its holomorphic Euler number is one.\nThese necessary data do not supply a compact third threefold or\nprove the existence of that smoothing.',
  'The surface smoothing is constructed in B.4.11--B.4.12.\nIts topological Euler number is $4+8-2\\chi(E)=12$ and its\nholomorphic Euler number is one. Its total space over an open\ndisc is not a compact third threefold, so that construction\ndoes not supply a compact threefold assembly.'),(
  'Thus B.4.1 and B.5.1 remain open after this auxiliary construction.',
  'These auxiliary matching statements do not produce a filling\nof the actual family. B.4.33 proves that no such proper analytic\nfilling exists after any finite parameter cover.')],
 'sections/ab_push_hopf_cap.tex': [(
  '\\begin{remark}[Relation to the primary literature and to the remaining cusp]',
  '\\begin{remark}[Primary literature and the scope of the auxiliary cap]'),(
  'component rotations.  These comparisons remain open.',
  'component rotations. The construction here establishes none of\nthose additional comparisons. B.4.33 separately rules out a proper\nanalytic filling of the actual global family, without denying the\nauxiliary Hopf degeneration constructed above.')],
 'sections/ab_push_corrected_cusp_overlap.tex': [(
  'The next local construction must complete this\nproper family over the single missing base point.',
  'This construction fills the punctured bidisc, not its\norigin. B.4.30 proves that its prescribed partial family\nhas no proper analytic completion at that point.'),(
  'comparison over $q$ between them. A successful\norigin cap must retain the actual two-open\ncomparison just constructed and prove its own\nanalytic extension and properness.',
  'comparison over $q$ between them. B.4.33 further\nexcludes every proper filling of the actual global family,\neven if its other central axial model is changed. Thus\nthe missing origin is not left as a construction claim.')],
 'sections/ab_push_global_partial.tex': [(
  'is $(\\infty,0)$; no proper completion over it, and no\nproper filling over the whole $r$ disc, is asserted.',
  'is $(\\infty,0)$. This proposition constructs only the\npartial family: B.4.30 proves its noncompletion, and\nB.4.33 excludes every proper filling of the actual\nfamily over the whole $r$ disc.'),(
  'saved output. They do not supply an origin cap.',
  'saved output. They do not supply an origin cap; the\nnonexistence statements are proved in B.4.30 and B.4.33.')],
 'sections/ab_push_tate_interface.tex': [(
  'Mumford cusp. Global plumbing data and that\nperiod comparison are still missing.',
  'Mumford cusp. This auxiliary proposition supplies neither\nglobal plumbing data nor that period comparison. B.4.33\nsubsequently excludes any proper filling of the actual family.')],
 'sections/B_degree_one_tate_repair.tex': [(
  'with the prescribed torus family.\n\\end{proposition}',
  'with the prescribed torus family. Such a proper filling of\nthe actual family is excluded by B.4.33; the present\nstatement retains its auxiliary embedded-collar scope.\n\\end{proposition}')],
 'sections/ab_push_corner_resolution.tex': [(
  'fixed-base obstruction in B.4.20 is not removed\nby recognizing a local Mumford triple chart.',
  'fixed-base obstruction in B.4.20 is not removed\nby recognizing a local Mumford triple chart. B.4.30 and\nB.4.33 exclude the respective actual origin completion\nand global proper filling; the local model above remains\na proved auxiliary construction.')],
 'sections/B_log_base_modification.tex': [(
  'therefore removes a specific logarithmic\nrepair by base blowups without removing the\nremaining unrestricted analytic possibility.',
  'therefore removes a specific logarithmic\nrepair by base blowups. B.4.30--B.4.33 supply the\nadditional extending-section and global-loop arguments\nthat exclude an arbitrary proper filling; no such\ncomparison is assumed in this proposition.')],
 'sections/B_log_torsor_obstruction.tex': [(
  'the obstruction has exactly the\nscope stated. The period differences and complete',
  'the obstruction has exactly the\nscope stated. The additional bridge from hypothetical\narbitrary caps is proved later in B.4.30--B.4.33,\nusing traces and a global radial-loop invariant.\nThe period differences and complete')],
 'sections/B_fixed_partial_noncompletion.tex': [(
  'It does not exclude every possible filling over\nthe $r$ disc: a different completion along\n$r=0$, $q\\ne0$ need not have the axial model of\nB.4.19. In particular, resolving the graph of the\nmarked map in B.4.4 does not by itself supply\nthat additional identification.',
  'This proposition alone does not exclude every filling\nover the $r$ disc: a different completion along\n$r=0$, $q\\ne0$ need not have the axial model of\nB.4.19. Resolving the graph in B.4.4 does not by\nitself supply that identification. B.4.31--B.4.33\nremove the need for it by controlling meridians and\nthe global affine loop class, and prove unrestricted\nnonexistence for the actual family.'),(
  'Along the strict $r$ axis\nalone the monodromy has rank one, so an\narbitrary other cap can have additional\ninvariant elliptic residues. The proof\ndoes not silently identify such a cap\nwith B.4.19.',
  'Along the strict $r$ axis the linear monodromy\ncondition alone leaves invariant elliptic directions.\nThe proof here does not control their geometric\nresidues or identify an unknown cap with B.4.19.\nThat control is supplied by the global argument in\nB.4.31 and used, together with B.4.32, in B.4.33.')],
 'sections/ab_push_global_meridians.tex': [(
  'Comparing the resulting unknown axial torsor with the\nparticular origin of B.4.19 is an additional question.\nThe invariant-form counterexample B.4.29 is consistent with\nthis limitation. No unrestricted nonexistence theorem for\nPart B is inferred here.',
  'Controlling its affine loop relative to the particular\norigin of B.4.19 is an additional step, proved in B.4.32.\nThe invariant-form counterexample B.4.29 is consistent with\nthis limitation. B.4.33 uses the loop class, rather than\nan extending comparison of individual origins, to prove\nunrestricted nonexistence for Part B.')],
 'sections/B_forms_translation_counterexample.tex': [(
  'such a difference. That stronger possible\nbridge remains separate. Exact chart,',
  'such a difference. The difference-extension bridge\nis proved in B.4.30; B.4.31--B.4.33 add the global\nmeridian and loop control needed for the actual family.\nThey do not contradict this counterexample. Exact chart,')],
 'sections/ab_push_log_canonical_torus.tex': [(
  '\\begin{remark}[The missing reduction for an arbitrary completion]\nThe proposition cannot alone complete B.4.19 at its\nmissing origin.',
  '\\begin{remark}[The separate canonical-model reduction]\nThis conditional proposition is not the noncompletion\nargument for B.4.19.'),(
  'that missing reduction.\n\\end{remark}',
  'that missing reduction. The unrestricted nonexistence\nof the actual sphere filling in B.4.33 does not require\nsuch a canonical model; it uses extending-section traces\nand the global affine loop invariant instead.\n\\end{remark}')],
 'sections/ab_push_kato_period_lift.tex': [(
  'These observations leave open connected unfoldings of noncompact\npieces with a new boundary geometry. Their analytic transition\nmaps, proper discontinuity, correct punctured quotient and compact\ncentral quotient would all have to be proved; none follows from\nthe auxiliary compact family in B.4.10.',
  'These observations alone do not classify connected unfoldings\nof noncompact pieces with a new boundary geometry. Analytic\ntransition maps, proper discontinuity and the retained punctured\nquotient are not supplied by the auxiliary compact family in\nB.4.10. Independently of that restricted classification question,\nB.4.33 rules out any such construction giving a proper filling\nof the actual global family.')],
 'sections/B_origin_fibre_dimension.tex': [(
  'has an\nproper analytic completion', 'has a\nproper analytic completion'),(
  'geometry retained.\n\\end{proposition}',
  'geometry retained. B.4.30 subsequently excludes even\nthe permitted vertical-component completions of the\nfixed partial family, and B.4.33 excludes every proper\nfilling of the actual global family.\n\\end{proposition}')]
}

csv_changes = {
 'sections/B_hodge_results.csv': {
  'B.4.3': {'notes': [('unrestricted analytic fillings remain open.', 'unrestricted nonexistence for the actual family is proved separately in B.4.33.')]},
  'B.4.4': {'statement': [(None, 'After resolving the reduced main component of any proper analytic filling of a finite cover of the actual family, the intrinsic marked map to P1 extends meromorphically on the smooth dominating fourfold and becomes holomorphic on a proper projective graph modification unchanged over the punctured disc.')],
              'notes': [(None, 'Coherent bi-anticanonical frame and three labelled critical-value branches remove essential PGL2 gauges. No hypothesis on the central divisor or its multiplicities is used. No Moishezon assertion for unknown vertical components is inferred. Independent original referee E_B44_referee.md; arbitrary-filling scope checked by root and limits_ab in B.4.31.')]},
  'B.4.5': {'notes': [('The arbitrary analytic filling remains open.', 'The arbitrary proper analytic filling is excluded by the separate global argument in B.4.33.')]}
 },
 'sections/ab_push_corrected_cusp_overlap_results.csv': {'B.4.18': {'notes': [('The origin completion and global finite-place overlaps remain open.', 'The global finite-place overlaps are constructed in B.4.19. The prescribed origin completion is excluded in B.4.30, and arbitrary proper fillings of the actual global family are excluded in B.4.33.')]}},
 'sections/ab_push_global_partial_results.csv': {'B.4.19': {'notes': [('Origin completion, global B filling, central topology, and analytic C.5.1 remain Open.', 'B.4.30 excludes this partial family\'s origin completion; B.4.33 excludes every proper filling of the actual global family after finite covers. Thus no actual global central topology or analytic filling of C.5.1 arises from such a degeneration.')]}},
 'sections/ab_push_tate_interface_results.csv': {'B.4.20': {'notes': [('Full second-period extension and actual origin cap remain Open.', 'No full second-period extension is constructed here. The actual fixed origin cap is excluded by B.4.30 and every proper global sphere filling by B.4.33; the embedded Tate-interface theorem remains auxiliary.')]}},
 'sections/B_degree_one_tate_repair_results.csv': {'B.4.21': {'notes': [('The B.4.19 origin cap remains Open.', 'The B.4.19 origin cap is excluded by B.4.30, and arbitrary proper global fillings are excluded by B.4.33. The proved collar remains an auxiliary construction.')]}},
 'sections/ab_push_corner_resolution_results.csv': {'B.4.22': {'notes': [('Global complement, whole second-period action, surviving rational-curve families and origin cap remain Open.', 'A global complementary Kato model and whole second-period action are not constructed. B.4.30 excludes the fixed actual origin cap, and B.4.33 excludes every proper filling of the actual global family. The local resolution and retained collar comparison remain proved.')]}},
 'sections/ab_push_kato_period_lift_results.csv': {'B.4.13': {'notes': [('connected noncompact unfoldings and central-only caps remain open.', 'the restricted lemma does not classify connected noncompact unfoldings or central-only modifications. B.4.33 independently excludes any construction producing a proper filling of the actual family.')]}},
 'sections/ab_push_hopf_cap_results.csv': {'B.4.7': {'notes': [('the actual cusp comparison remains open.', 'this auxiliary family is not an actual cusp comparison. B.4.33 independently excludes proper fillings of the actual global family.')]}},
 'sections/ab_push_log_canonical_results.csv': {'B.4.28': {'notes': [('obtaining such a modification of an arbitrary analytic completion remains Open.', 'a general canonical-model reduction for arbitrary analytic torus degenerations is not proved. B.4.33 excludes the actual sphere filling without that reduction.')]}},
 'sections/B_elliptic_weights_results.csv': {'B.4.14': {'notes': [('Nonisolated local deformation compatibility and analytic globalization remain open; no compact third component or S6 filling is inferred.', 'Nonisolated local deformation compatibility and analytic globalization for this auxiliary associated bundle are not proved; no compact third component is inferred. The actual proper S6 filling is excluded by B.4.33.')]}},
 'sections/B_hopf_resonance_obstruction_results.csv': {'B.4.25': {'notes': [('and does not exclude arbitrary completions of the actual two-torus family.', 'and alone does not exclude arbitrary completions of the actual two-torus family; the actual global noncompletion is proved in B.4.33.')]}},
 'sections/B_fixed_partial_noncompletion_results.csv': {'B.4.30': {'notes': [('This result alone does not exclude arbitrary r-only fillings with different r-axis caps.', 'This result alone does not exclude arbitrary r-only fillings with different r-axis caps. B.4.31--B.4.33 supply the global meridian and affine-loop bridge and exclude them without identifying their models.')]}},
 'sections/B_log_torsor_results.csv': {'B.4.24': {'notes': [('No implication from an arbitrary analytic cap with vertical threefolds to this torsor category is assumed.', 'No implication from an arbitrary analytic cap with vertical threefolds to this torsor category is assumed here. B.4.30--B.4.33 later construct the required associated torsor from extending trace differences.')]}},
 'sections/ab_push_global_meridians_results.csv': {'B.4.31': {'notes': [('Affine origins and comparison with B.4.19 remain separate.', 'The separate affine-loop control is proved in B.4.32 and used in B.4.33; no extending identification of individual origins is asserted.')]}},
 'sections/B_global_loop_defect_results.csv': {'B.4.32': {'notes': [('Root final full-source PASS; E and AB working-proof PASS.', 'Root and limits_ab final full-source PASS; E working-proof PASS. Independent AB full-source referee and exact symbolic all-degree audit saved.')]}}
}

plans = {}
passages = []
for name, pairs in replacements.items():
    path = ROOT/name
    old = path.read_text()
    new = old
    for before,after in pairs:
        count = new.count(before)
        assert count == 1, (name, count, before)
        new = new.replace(before,after,1)
        passages.append({'file':name,'before':before,'after':after})
    plans[name]=(old,new)

for name, by_id in csv_changes.items():
    path=ROOT/name
    old=path.read_text()
    reader=csv.DictReader(io.StringIO(old))
    fields=reader.fieldnames
    rows=list(reader)
    assert fields is not None
    seen=set()
    for row in rows:
        rid=row['id']
        if rid not in by_id:
            continue
        seen.add(rid)
        for column,pairs in by_id[rid].items():
            val=row[column]
            for before,after in pairs:
                if before is None:
                    newval=after
                else:
                    assert val.count(before)==1,(name,rid,before)
                    newval=val.replace(before,after,1)
                passages.append({'file':name,'id':rid,'column':column,'before':val,'after':newval})
                val=newval
            row[column]=val
    assert seen==set(by_id),(name,seen,set(by_id))
    buf=io.StringIO()
    writer=csv.DictWriter(buf,fieldnames=fields,lineterminator='\n')
    writer.writeheader(); writer.writerows(rows)
    plans[name]=(old,buf.getvalue())

for name in plans:
    assert name.endswith(('.tex','.csv'))
    assert Path(name).name not in {'AB_push.tex','AB_push_results.csv'}
    assert not Path(name).name.startswith('B_global_noncompletion')
    assert 'report' not in Path(name).name and 'referee' not in Path(name).name

retention=ROOT/'evidence/ab_push_final_status_before'
retention.mkdir(exist_ok=True)
for name,(old,new) in plans.items():
    backup=retention/Path(name).name
    assert not backup.exists(),backup
    backup.write_text(old)
    (ROOT/name).write_text(new)

audit={
 'date_utc':datetime.now(timezone.utc).isoformat(),
 'authorization':'Root requested current standalone B source/CSV stale-status cleanup after accepting B.4.33; master and B_global_noncompletion files excluded.',
 'files_changed':list(plans),
 'passages':passages,
 'scopes_preserved':True,
 'numbered_status_values_changed':False,
 'historical_reports_referees_changed':False,
 'before_directory':'evidence/ab_push_final_status_before'
}
(ROOT/'evidence/ab_push_final_status_audit.json').write_text(json.dumps(audit,indent=2)+'\n')
lines=['# Current standalone B status reconciliation', '',
 '**Date:** 15 November 2026. **Authorization:** root, after full acceptance of B.4.33.', '',
 'Only current standalone B TeX/CSV files were updated. Master AB files, the new B.4.33 files, all historical reports and all referee records were left untouched. No numbered status value or local theorem scope changed. Complete originals are retained in `evidence/ab_push_final_status_before`; the structured before/after ledger is `evidence/ab_push_final_status_audit.json`.', '',
 'The corrections replace stale global-open wording with precise B.4.30/B.4.33 forward references. Independent auxiliary deformation/classification questions remain explicitly outside the proved local lemmas. The B.4.4 registry now states its proved scope for a resolved main component of any proper analytic filling, with no central reducedness assumption.', '',
 f'**Changed files:** {len(plans)}. **Recorded changed passages/cells:** {len(passages)}.', '']
for item in passages:
    title=item['file']+(f" / {item['id']} / {item['column']}" if 'id' in item else '')
    lines += ['## '+title,'','**Previous passage**','','```text',item['before'],'```','','**Current passage**','','```text',item['after'],'```','']
(ROOT/'sections/ab_push_final_status_audit.md').write_text('\n'.join(lines))
print(f'PASS: updated {len(plans)} current files and recorded {len(passages)} passages/cells.')
print('PASS: all exact anchors checked before any mutation.')
print('PASS: master, B_global_noncompletion, historical reports and referees unchanged.')
print('PASS: complete before files and structured/full-text audit retained.')
