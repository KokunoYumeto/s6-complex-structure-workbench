#!/usr/bin/env python3
"""Fresh bounded audit of 58 saved API-v2 replies.

Reads only the authorized claim packet and raw_responses. It neither imports
an earlier audit nor calls a remote engine. Exact set coverage is generated
from the catalogue, and output classification is recomputed from raw fields.
"""
from __future__ import annotations
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import product
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "agents/continuation7_iii_ku/raw_responses"
CLAIM = ROOT / "agents/continuation7_iii_ku/S6_SERIES_PUBLISH_III_02KU_claim_inputs.tex"

def no_duplicate_keys(pairs):
    ans = {}
    for key, value in pairs:
        assert key not in ans, ("duplicate JSON key", key)
        ans[key] = value
    return ans

def multiply(a, b):
    return tuple(tuple(sum(a[i][r]*b[r][j] for r in range(2))
                       for j in range(2)) for i in range(2))

def inverse(a):
    assert a[0][0]*a[1][1]-a[0][1]*a[1][0] == 1
    return ((a[1][1],-a[0][1]),(-a[1][0],a[0][0]))

def power(a, n):
    out = ((1,0),(0,1))
    for _ in range(n):
        out = multiply(out,a)
    return out

def first_unipotent_power(a):
    assert a[0][0]*a[1][1]-a[0][1]*a[1][0] == 1
    for n in range(1,13):
        p = power(a,n)
        if p[0][0]+p[1][1] == 2:
            return n
    raise AssertionError(("no power in range",a))

# Standard Kodaira monodromy representatives. Their finite parts, not any
# unpublished local topology, determine the reduction orders used in the slice.
monodromy = {
    "II": ((1,1),(-1,0)),
    "III": ((0,-1),(1,0)),
    "IV": ((0,-1),(1,-1)),
    "I1*": ((-1,-1),(0,-1)),
    "I3*": ((-1,-3),(0,-1)),
}
monodromy["III*"] = inverse(monodromy["III"])
monodromy["IV*"] = inverse(monodromy["IV"])
reduction = {kind:first_unipotent_power(a) for kind,a in monodromy.items()}

def unpack_configuration(text):
    assert text.startswith("$") and text.endswith("$"), text
    text = text[1:-1]
    out = []
    for term in text.split("+"):
        match = re.fullmatch(r"(\d*)(I_\d+|I{2,3}|IV)(\^\*)?", term)
        assert match, term
        count = int(match[1] or "1")
        name = match[2].replace("_","") + ("*" if match[3] else "")
        out.extend([name]*count)
    return tuple(out)

# Derive all 21 rows directly from the mathematical claim-only table.
catalogue = {}
heights = {}
narrow = {}
for line in CLAIM.read_text().splitlines():
    if not re.match(r"^\d+\s*&",line):
        continue
    os_text,h_text,n_text,configs_text = line.split("&")
    os_entry = int(os_text)
    h = Fraction(h_text.strip().strip("$"))
    n = int(n_text.strip())
    config_tokens = configs_text.strip().removesuffix(r"\\").split(";")
    configs = [unpack_configuration(s.strip()) for s in config_tokens]
    heights[os_entry],narrow[os_entry] = h,n
    for j,types in enumerate(configs):
        if j == 0:
            profile = "default"
        else:
            added = [s for s in ("II","III","IV") if s in types]
            assert len(added) == 1,(os_entry,types,added)
            profile = added[0]
        key = (os_entry,profile)
        assert key not in catalogue
        catalogue[key] = types
assert len(catalogue) == 21
assert set(narrow) == {43,45,46,47,49,50,55,56}

def multiplicative_n(name):
    match = re.fullmatch(r"I(\d+)",name)
    return int(match[1]) if match else None

def zero_position(types):
    ones = [i for i,s in enumerate(types) if s=="I1"]
    if ones:
        return ones[0]
    vals = [(multiplicative_n(s),i) for i,s in enumerate(types)
            if multiplicative_n(s) is not None]
    assert vals
    return min(vals)[1]

def additive_indices(types):
    out = [i for i,s in enumerate(types) if multiplicative_n(s) is None]
    assert all(types[i] in reduction for i in out)
    return tuple(out)

def occurrence_permutation(stored, printed):
    """Map stored position i to the matching printed position, occurrence by occurrence."""
    queues = defaultdict(list)
    for j,kind in enumerate(printed):
        queues[kind].append(j)
    permutation = []
    for kind in stored:
        assert queues[kind],("unmatched fibre occurrence",stored,printed,kind)
        permutation.append(queues[kind].pop(0))
    assert not any(queues.values()),("unmatched printed fibres",queues)
    assert sorted(permutation) == list(range(len(printed)))
    inverse_map = tuple(permutation.index(j) for j in range(len(printed)))
    assert all(stored[inverse_map[j]] == printed[j] for j in range(len(printed)))
    return tuple(permutation),inverse_map

expected = set()
for (os_entry,profile),types in catalogue.items():
    a = len(additive_indices(types))
    for choice in product((0,1),repeat=a):
        expected.add((os_entry,profile,choice))
assert len(expected) == 50

def groups_from_response(r, name):
    entries = r["cohomology"]
    assert len(entries) == 7,(name,"cohomology length")
    assert [q["degree"] for q in entries] == list(range(7)),name
    groups = []
    for q in entries:
        rank, tors = q["rank"],q["torsion"]
        assert type(rank) is int and rank >= 0,(name,q)
        assert isinstance(tors,list) and all(type(d) is int and d>1 for d in tors)
        assert all(b%a==0 for a,b in zip(tors,tors[1:])),(name,"invariant factors",tors)
        pieces = (["Z" if rank==1 else f"Z^{rank}"] if rank else [])
        pieces += [f"Z/{d}" for d in tors]
        exact_label = " + ".join(pieces) if pieces else "0"
        assert q["label"] == exact_label,(name,q,exact_label)
        groups.append((rank,tuple(tors)))
    assert groups[0] == groups[6] == (1,())
    assert sum((-1)**i*groups[i][0] for i in range(7)) == r["euler_characteristic"], (
        name,"Euler sum",groups,r["euler_characteristic"])
    # Duality/UCT consistency checks on reported groups, not a reconstruction
    # of the unpublished model cochain complexes.
    assert all(groups[i][0]==groups[6-i][0] for i in range(7))
    assert all(groups[i][1]==groups[7-i][1] for i in range(1,7))
    pi = r["fundamental_group"]
    description = pi["description"]
    if description == "trivial":
        assert pi == dict(description="trivial",trivial=True,order="1",abelianization="0")
        abelian_group = (0,())
    elif description == "Z":
        assert pi == dict(description="Z",trivial=False,order="None",abelianization="Z")
        abelian_group = (1,())
    else:
        match = re.fullmatch(r"Z/([1-9]\d*)",description)
        assert match and int(match[1]) > 1,(name,pi)
        d = int(match[1])
        assert pi == dict(description=description,trivial=False,order=str(d),
                          abelianization=description)
        abelian_group = (0,(d,))
    assert abelian_group == (groups[1][0],groups[2][1]),(name,"UCT/H1",groups,pi)
    sphere = groups == [(1,())]+[(0,())]*5+[(1,())]
    assert type(r["integral_homology_sphere"]) is bool
    assert type(r["S6_for_supplied_smooth_model"]) is bool
    assert r["integral_homology_sphere"] == sphere,(name,"sphere flag")
    assert r["S6_for_supplied_smooth_model"] == (sphere and pi["trivial"]),(name,"S6 flag")
    return tuple(groups),sphere,description

records = []
for f in sorted(DATA.glob("*.json")):
    raw = f.read_bytes()
    doc = json.loads(raw,object_pairs_hook=no_duplicate_keys)
    assert set(doc) == {"url","input","response","elapsed_seconds"},f.name
    assert doc["url"] == "https://threefold-explorer-api.onrender.com/api/compute"
    req,r = doc["input"],doc["response"]
    assert r["api_version"] == 2 and r["status"] == "computed from database cochains"
    assert r["qualification"] == ""
    assert set(r["input"]) == {"os_entry","profile","P","Q","linearization_divisor"}
    assert r["input"] == {key:req[key] for key in r["input"]},f.name
    assert isinstance(doc["elapsed_seconds"],(int,float)) and doc["elapsed_seconds"] >= 0
    models = r["local_models"]
    assert [m["index"] for m in models] == list(range(1,len(models)+1))
    assert all(re.fullmatch(r"[0-9a-f]{64}",m["model_id"]) for m in models)
    assert all(type(m["fiber_multiplicity"]) is int and m["fiber_multiplicity"] > 0
               for m in models)
    assert len(req["linearization_divisor"]) == len(req["log_data"]) == len(models)
    group,sphere,pi = groups_from_response(r,f.name)
    records.append(dict(name=f.name,doc=doc,groups=group,sphere=sphere,pi=pi))
assert len(records) == 58
all_rows = [v for v in records if v["name"].startswith("all21_")]
clutch_rows = [v for v in records if v["name"].startswith("semistable_")]
assert len(all_rows) == 50 and len(clutch_rows) == 8

observed = {}
family_counts = Counter()
markings = {}
for row in all_rows:
    req,r = row["doc"]["input"],row["doc"]["response"]
    os_entry,profile = req["os_entry"],req["profile"]
    printed_types = catalogue[(os_entry,profile)]
    types = tuple(m["type"] for m in r["local_models"])
    permutation,inverse_map = occurrence_permutation(types,printed_types)
    marked = (types,permutation,inverse_map)
    if (os_entry,profile) in markings:
        assert markings[(os_entry,profile)] == marked
    else:
        markings[(os_entry,profile)] = marked
    assert req["P"] == [1] and req["Q"] == [narrow[os_entry]]
    assert req["coordinates"] == "invariant"
    weight = [0]*len(types)
    weight[zero_position(types)] = 1
    assert req["linearization_divisor"] == weight,row["name"]
    assert r["euler_characteristic"] == 2*multiplicative_n(types[zero_position(types)])
    positions = additive_indices(types)
    bits = []
    for i,(kind,log,model) in enumerate(zip(types,req["log_data"],r["local_models"])):
        family_counts[(kind,model["family"],model["fiber_multiplicity"])] += 1
        if i not in positions:
            assert log is None,(row["name"],i,"unexpected nonadditive log")
            wanted_family = "mumford" if weight[i] else "original_plumbing"
            assert model["family"] == wanted_family and model["fiber_multiplicity"] == 1
            if weight[i]:
                assert model["parameters"]["weight"] == 1
                assert model["parameters"]["n"] == multiplicative_n(kind)
            continue
        if log is None:
            bits.append(0)
            assert model["family"] == "original_plumbing"
            assert model["fiber_multiplicity"] == 1
        else:
            assert len(log)==2 and tuple(Fraction(x) for x in log) == (0,Fraction(1,reduction[kind]))
            bits.append(1)
            assert model["fiber_multiplicity"] == reduction[kind]
            if kind in {"I1*","I3*"}:
                assert model["family"] == "star_semistable_quotient"
                assert model["parameters"]["n"] == int(kind[1:-1])
                assert model["parameters"]["e"] == 1
            else:
                assert model["family"] == "finite_quotient"
                assert model["parameters"]["denominator"] == reduction[kind]
                assert model["parameters"]["resolution"] == "free"
    # Carry each switch along the literal occurrence permutation. This fixes
    # the map between catalogue ordering and saved additive-fibre bit ordering.
    stored_switch = dict(zip(positions,bits))
    printed_bits = tuple(stored_switch[inverse_map[j]]
                         for j in additive_indices(printed_types))
    key = (os_entry,profile,printed_bits)
    assert key not in observed,("duplicate mathematical input",key)
    observed[key] = row
    row["key"],row["stored_bits"] = key,tuple(bits)
    suffix = "".join(map(str,bits)) or "none"
    assert row["name"] == f"all21_{os_entry}_{profile}_{suffix}.json"
assert set(observed) == expected,("missing",expected-set(observed),"extra",set(observed)-expected)

pi_counts = Counter(v["pi"] for v in all_rows)
simply = sum(v["doc"]["response"]["fundamental_group"]["trivial"] for v in all_rows)
sphere_keys = {v["key"] for v in all_rows if v["sphere"]}
target_spheres = {(43,"default",(1,)),(43,"II",(1,0)),(49,"III",(1,1))}
assert simply == 24 and len(all_rows)-simply == 26
assert sphere_keys == target_spheres
assert pi_counts == Counter({"trivial":24,"Z":21,"Z/3":1,"Z/4":1,"Z/5":1,"Z/8":1,"Z/10":1})

print("Fresh bounded archive audit: no prior audit code imported; no remote API execution.")
print("Reduction orders from exact matrix powers:",dict(sorted(reduction.items())))
print("Catalogue rows:",len(catalogue),"generated input choices:",len(expected))
print("JSON uniqueness, API-v2 status, echoed inputs, model indices/types, requested logs,")
print("weight selection, local families/multiplicities, group labels, Euler/duality/UCT,")
print("recognition flags and exact input-set equality: PASS")
print()
print("CATALOGUE COVERAGE AND CLASSIFICATION")
print("OS profile | catalogue types | stored-to-catalogue permutation (1-based) |")
print("stored zero position | expected/saved | trivial/nontrivial | catalogue sphere bits")
for (os_entry,profile),types in sorted(catalogue.items()):
    rows = [v for key,v in sorted(observed.items()) if key[:2] == (os_entry,profile)]
    a = additive_indices(types)
    sc = sum(v["pi"]=="trivial" for v in rows)
    spheres = ["".join(map(str,v["key"][2])) or "none" for v in rows if v["sphere"]]
    stored,permutation,inverse_map = markings[(os_entry,profile)]
    print(f"{os_entry} {profile} | {'+'.join(types)} | {tuple(i+1 for i in permutation)} | "
          f"{zero_position(stored)+1} | "
          f"{2**len(a)}/{len(rows)} | {sc}/{len(rows)-sc} | {','.join(spheres) or '-'}")
print()
print("ALL 50 EXACT REPORTED GROUPS")
print("saved file | catalogue input key | pi1 | H0;H1;H2;H3;H4;H5;H6 | sphere flag")
for key,row in sorted(observed.items()):
    labels = ";".join(q["label"] for q in row["doc"]["response"]["cohomology"])
    print(f"{row['name']} | {key} | {row['pi']} | {labels} | {row['sphere']}")
print()
print("PI1 descriptor counts:",dict(sorted(pi_counts.items())))
print("Simply recognized:",simply,"non-simply recognized:",len(all_rows)-simply)
print("Sphere keys:",sorted(sphere_keys))
print("Euler characteristic distribution:",
      dict(sorted(Counter(v["doc"]["response"]["euler_characteristic"]
                          for v in all_rows).items())))
print("All 50 reported Euler characteristics equal their alternating rank sums;")
print("all claimed recognition flags match the raw groups.")
print()
print("EIGHT CLUTCH RECORDS AND FOUR EXACT INPUT COMPARISONS")
clutches = {}
for row in clutch_rows:
    req,r = row["doc"]["input"],row["doc"]["response"]
    os_entry = req["os_entry"]
    assert os_entry in {45,47,55,56} and req["profile"]=="default"
    types = catalogue[(os_entry,"default")] + ("I0",)
    assert tuple(m["type"] for m in r["local_models"]) == types
    assert req["P"] == [narrow[os_entry]] and req["Q"] == [1]
    assert req["coordinates"] == "ambient"
    assert req["linearization_divisor"] == [0,0,0,0,1,0]
    assert req["log_data"][:-1] == [None]*5
    clutch = req["log_data"][-1]
    assert clutch in ([0,0,0,0],[0,0,0,1])
    c = clutch[-1]
    assert row["name"] == f"semistable_{os_entry}_clutch{c}.json"
    assert (os_entry,c) not in clutches
    clutches[(os_entry,c)] = row
    assert r["local_models"][-1]["family"]=="smooth_product"
    assert r["local_models"][-1]["fiber_multiplicity"]==1
    for model in r["local_models"][:-1]:
        n = multiplicative_n(model["type"])
        assert n is not None
        if n > 1:
            assert model["family"] == "original_plumbing"
            assert model["component_orbits"] == 1
            assert model["component_orbit_length"] == n
            assert model["parameters"] == {"type":"I1","P_component":0}
    assert req["P"] != [1] and req["Q"] != [narrow[os_entry]]
    labels = ";".join(q["label"] for q in r["cohomology"])
    print(f"OS{os_entry} c={c}: P={req['P']} Q={req['Q']} "
          f"clutch={clutch} | pi1={row['pi']} | {labels} | sphere={row['sphere']}")
assert set(clutches) == set(product((45,47,55,56),(0,1)))
for os_entry in (45,47,55,56):
    a,b = clutches[(os_entry,0)],clutches[(os_entry,1)]
    old,new = a["doc"]["input"],b["doc"]["input"]
    rebuilt = json.loads(json.dumps(old))
    rebuilt["log_data"][-1][-1] = 1
    assert rebuilt == new
    assert a["doc"]["response"]["local_models"] == b["doc"]["response"]["local_models"]
    assert a["doc"]["response"]["input"] == b["doc"]["response"]["input"]
    print(f"OS{os_entry}: exact sole input change log_data[5][3]:0->1; "
          "same local-model dictionaries/identities and echoed static input; PASS")
print()
print("The eight clutch inputs are outside the 50-input slice: P=nG,Q=G with n>1,")
print("ambient coordinates, and an additional I0 integral clutch, versus P=G,Q=nG")
print("and the specified additive-fibre alternatives. All eight are accounted for.")
print("No unpublished model cochain derivation or new remote execution is certified.")
print("Complete bounded archive audit PASSED.")

