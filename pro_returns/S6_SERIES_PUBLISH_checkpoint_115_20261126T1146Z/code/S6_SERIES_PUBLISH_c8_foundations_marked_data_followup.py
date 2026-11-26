"""Exact corrections found while rereading the first edited foundations fragment."""
import csv
from datetime import datetime, timezone

from S6_SERIES_PUBLISH_c8_foundations_marked_data import (
    DEFECTS, FIELDS, FRAGMENT, ROOT, WHO, identities,
)


def main():
    source = FRAGMENT.read_text()
    text = source
    now = datetime.now(timezone.utc).isoformat()
    with DEFECTS.open(newline="") as stream:
        rows = list(csv.DictReader(stream, delimiter="\t"))
    edits = [
        ("D13", "mapsIII:def:triangular-cusp",
         " [v+e_1,v+e_1+e_2,v+e_2].\n\\]\nThe two period generators",
         " [v+e_1,v+e_1+e_2,v+e_2].\n\\]\n"
         "Use the toroidal space of this fan, with the base character \\(q\\)\n"
         "given by height in \\(\\mathbb Z^2\\oplus\\mathbb Z\\).\nThe two period generators",
         "Specify the toroidal space and height character in the numbered definition before q is used; the proof still supplies the inverse monomial charts and q=z1z2z3."),
        ("D23", "maps:src:D.2.43",
         "These maps commute and extend by the displayed character maps.",
         "The two period maps of Definition~\\ref{mapsIII:def:triangular-cusp}\ncommute and extend by the displayed character maps.",
         "After the exact definition relocation, name the period maps explicitly so that the pronoun does not appear to refer to the immediately preceding toric surface."),
        ("D02", "maps:src:D.2.43",
         "is \\(|q|=\\epsilon\\); there is no additional side boundary.",
         "is \\(|q|=\\epsilon\\).",
         "The positive boundary identification in the same sentence already gives the complete boundary; remove its repeated negative formulation."),
        ("D02", "maps:src:D.2.43",
         "sign from the positive square orientation without dividing a\ntransfer relation by \\(D\\).",
         "sign from the positive square orientation.",
         "The explicit Koszul lift and adjugate identities establish the sign; remove the defensive comparison with a different transfer calculation while retaining every chain map."),
        ("D23", "maps:src:D.2.47",
         "Let $N_L$ be the smooth triangular Mumford cap of \\ref{maps:src:D.2.43},",
         "Let $N_L$ be the smooth triangular Mumford cap of Theorem~\\ref{maps:src:D.2.43},",
         "Name the cited statement's observed theorem type in the cap hypothesis."),
    ]
    for kind, label, old, new, reason in edits:
        if text.count(old) != 1:
            raise ValueError((old, text.count(old)))
        start = text.index(old)
        row = dict(zip(FIELDS, [
            f"III-C8-FND-MARKED-{len(rows)+1:03}", kind, label,
            str(FRAGMENT.relative_to(ROOT))+f"; pre-edit fragment line {text.count(chr(10), 0, start)+1}",
            "pending final page concordance", str(FRAGMENT.relative_to(ROOT))+"; "+label,
            "pending final build", old, new, reason,
            "Applied to owned fragment "+now+". "+WHO+" Found during full rereading; no central criterion or rendered-page gate closed.",
        ]))
        rows.append(row)
        text = text[:start]+new+text[start+len(old):]
    for command in ("label", "hypertarget"):
        if identities(source, command) != identities(text, command):
            raise ValueError(command)
    with DEFECTS.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=FIELDS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    FRAGMENT.write_text(text)
    print("Five exact rereading corrections applied and recorded; all labels/targets unchanged.")
    print("No canonical or central progress/event mutation.")


if __name__ == "__main__":
    main()
