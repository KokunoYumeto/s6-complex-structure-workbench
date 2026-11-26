"""Small exact typography corrections found in the complete cohomology reread."""
from S6_SERIES_PUBLISH_c8_foundations_editing import Editor

e=Editor("elliptic_cohomology", "III-C8-FND-COHOM-READ-")
for old,new,kind,label,reason in [
    ("has fifty inputs. Consider their integral-cohomology and\nfundamental-group outputs. Their fundamental-group outputs are\ntrivial", "has fifty inputs. Their integral-cohomology and fundamental-group\noutputs have the following properties. The fundamental group is\ntrivial", "D23", "maps:src:D.2.2", "Remove the repeated output phrase while keeping the model-output scope explicit in the same opening."),
    ("The marked peripheral presentation\\cite[", "The marked peripheral presentation\n\\cite[", "D23", "maps:src:D.2.3", "Separate the prose from its existing precise primary citation."),
    ("there is one component orbit of length j,", "there is one component orbit of length $j$,", "D23", "maps:src:D.2.2", "Typeset the component-orbit length as the index already used in I_j."),
    ("with the same local \\(I_1\\) model and zero P component;", "with the same local \\(I_1\\) model and zero $P$ component;", "D23", "maps:src:D.2.2", "Typeset the named section variable in the local-model comparison."),
    ("For each of the four values of n the outputs are", "For each of the four values of $n$ the outputs are", "D23", "maps:src:D.2.2", "Typeset the integer parameter used in the displayed four-OS family."),
]:
    e.replace(old,new,kind,label,reason)
issues=e.presentation()
if issues: raise ValueError(issues)
e.finish()
