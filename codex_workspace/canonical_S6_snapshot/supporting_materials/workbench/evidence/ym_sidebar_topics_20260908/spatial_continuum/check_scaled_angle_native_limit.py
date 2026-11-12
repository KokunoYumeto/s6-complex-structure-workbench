from pathlib import Path
import re, json
p=Path("sources/scaled_angle_native_limit.md")
s=p.read_text(encoding="utf-8")
checks = {
 "hamiltonian": r"H_g=.*H_0",
 "hc": r"H_c=-2T_3",
 "inverse_sign": r"inverse translated link",
 "delta_factor": r"\\delta\(q\):=-2\\tau R\^\*\\eta\(q\)",
 "eta": r"\\eta_e\(q\)=n_2",
 "strong": r"\\mathcal B_gK_\{\\theta_g\}\\mathcal B_g\^\*u\\to A_\\tau u",
 "mass": r"d_\\tau=\\iint e",
 "kernel": r"e\^{-t\\Lambda/a}",
 "spectral": r"\\langle\\chi_\{\\theta_g,g\},F\(A_g\)",
}
out={}
for k,pat in checks.items():
    out[k]=bool(re.search(pat,s))
out["all"]=all(out.values())
Path("SCALED_ANGLE_NATIVE_LIMIT_CHECKS.json").write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps(out))
if not out["all"]: raise SystemExit(1)


