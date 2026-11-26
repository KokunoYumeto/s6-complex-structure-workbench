// Actual GitHub connector calls used for the LK following-auxiliary retrieval.
// The single source request was completed first; the remaining three requests
// were completed together with Promise.allSettled. No helper body was printed.
const repo = "KokunoYumeto/s6-complex-structure-workbench";
const ref = "a02f2eacf5a8c3db7cf8cdfcdba50c0002ee91c7";
const dir = "pro_returns/S6_10_PAPERS_checkpoint_15_20261119T1045Z/S6_10_PAPERS/code/III/";
const first = {repository_full_name: repo, ref, encoding: "base64",
               path: dir + "manifolds_general_cusp.py"};
const firstResponse = await tools.mcp__codex_apps__github_fetch_file(first);
const names = ["manifolds_general_cusp.json",
               "manifolds_rankone_families.py",
               "manifolds_weighted_profiles.py"];
const rest = await Promise.allSettled(names.map(async name => {
  const request = {repository_full_name: repo, ref, encoding: "base64",
                   path: dir + name};
  return {request, response: await tools.mcp__codex_apps__github_fetch_file(request)};
}));
// The retained .out contains each complete request and tool response.
// Full source bytes and the recorded Git blob identities are decoded and
// verified by c7_lk_historical_cache_v1.py; no mathematical execution occurs here.
