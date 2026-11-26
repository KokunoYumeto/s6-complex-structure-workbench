"""Corrections found by the complete rereading of the edited KM proof."""
from S6_SERIES_PUBLISH_c8_foundations_editing import Editor


def main():
    e = Editor("elliptic_poincare", "c8-III-foundations-KM-reread-")
    label = "maps:src:D.2.12"
    changes = [
        ("The following coefficient pairs are in the order of the theorem:",
         r"The following coefficient pairs use the order in Definition~\ref{mapsIII:def:seven-log-profiles}:",
         "D04", "The ordered data table now belongs to Q115; point to its actual numbered owner."),
        ("Neron models", r"N\'eron models", "D23", "Restore the accent in the identity-model extension argument."),
        ("surface's Neron--Severi lattice", r"surface's N\'eron--Severi lattice", "D23", "Restore the accent in the unimodular height calculation."),
        (r"""The odd theta function satisfies
$\theta(z+1)=-\theta(z)$ and
$\theta(z+\tau)=-e^{-\pi i\tau-2\pi iz}\theta(z)$;
hence $\theta(z-P)/\theta(z)$ has divisor $P-O$ and
$\tau$-multiplier $e^{2\pi iP}$.""",
         r"""The identities for $\vartheta$ above give
$\vartheta(z-P)/\vartheta(z)$ divisor $P-O$ and
$\tau$-multiplier $e^{2\pi iP}$.""", "D20",
         "Use the already defined odd theta function, leaving theta for the circle coordinate; retain the exact divisor and multiplier that determine the signed lift."),
        ("We also give the integral fibre quotient. Order bivectors as",
         "For the integral fibre quotient, order bivectors as", "D08",
         "Begin with the mathematical quotient construction rather than an announcement."),
        ("We spell out the collar, including its radial and unit terms.\nWrite",
         "For the collar's radial and unit terms, write", "D08",
         "Introduce the explicit collar coordinates directly; all radial/unit maps and their inverse remain."),
        ("$H_1(X)=\\operatorname{coker}\\mathcal G$, with no kernel\nterm left for an extension.",
         "$H_1(X)=\\operatorname{coker}\\mathcal G$.", "D02",
         "The preceding injectivity and pair exact sequence already prove these identifications; remove the repeated defensive extension clause."),
    ]
    for old, new, kind, reason in changes:
        e.replace(old, new, kind, label, reason)
    e.finish()


if __name__ == "__main__":
    main()
