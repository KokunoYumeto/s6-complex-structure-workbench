from pathlib import Path
import subprocess, concurrent.futures, json, os, time
root=Path(__file__).resolve().parent
jobs={
'MAPS':['maps_exact','real_involutions','real_finite_four','manifolds_mapping_quotient','maps_quotient_classification','fourfolds_cusp_complex','maps_real_audit'],
'PUSH':['c_exact','ab_push_actual_line_comparison','d_push_affine_frame_defect','e_push_C_cubic','d_push_signed_cap','e_push_C_cap','d_push_cusp_product','d_push_cusp_orbit_cells','d_push_cusp_marking','d_push_cap_p1','d_push_monodromy']}
def run(job):
    run,name=job;p=root/run/'code'/f'{name}.py';start=time.time()
    r=subprocess.run([os.environ['CODEX_PRIMARY_RUNTIME_PYTHON'],str(p)],cwd=p.parent,capture_output=True,text=True)
    out=p.with_suffix('.audit_rerun.txt');out.write_text(r.stdout+'\n'+r.stderr)
    return dict(program=str(p.relative_to(root)),exit_code=r.returncode,seconds=round(time.time()-start,3),output=str(out.relative_to(root)))
record=[]
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:
    for r in ex.map(run,[(a,b) for a,bs in jobs.items() for b in bs]):
        record.append(r);print(r,flush=True)
        (root/'selected_reruns.json').write_text(json.dumps(record,indent=2))
