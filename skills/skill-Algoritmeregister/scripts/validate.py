#!/usr/bin/env python3
"""Valideer een Algoritmeregister-registratie tegen Publicatiestandaard v1.0.0.

Gebruik:
    python scripts/validate.py <pad-naar-ingevuld.json>

Meldt FOUTEN (moeten opgelost worden) en WAARSCHUWINGEN (bewuste keuze nodig).
Exit-code 1 als er fouten zijn, anders 0.
"""
import json
import re
import sys

# (sectie, sleutel) -> eigenschappen
# limiet = max aantal tekens (exclusief); None = geen limiet
# verplicht = publicatie geweigerd indien leeg
# altijd_tonen = veld wordt altijd getoond (leeg -> waarschuwing)
# soort = "tekst" | "url" | "url_of_mail" | "datum" | "lijst"
FIELDS = {
    ("algemene_informatie", "naam"):            dict(limiet=100, verplicht=True,  altijd_tonen=True,  soort="tekst"),
    ("algemene_informatie", "korte_omschrijving"): dict(limiet=350, verplicht=True, altijd_tonen=True, soort="tekst"),
    ("algemene_informatie", "organisatie"):     dict(limiet=100, verplicht=True,  altijd_tonen=True,  soort="tekst"),
    ("algemene_informatie", "thema"):           dict(limiet=None, verplicht=False, altijd_tonen=True,  soort="lijst"),
    ("algemene_informatie", "status"):          dict(limiet=None, verplicht=True,  altijd_tonen=True,  soort="tekst"),
    ("algemene_informatie", "begindatum"):      dict(limiet=None, verplicht=False, altijd_tonen=True,  soort="datum"),
    ("algemene_informatie", "einddatum"):       dict(limiet=None, verplicht=False, altijd_tonen=True,  soort="datum"),
    ("algemene_informatie", "contactgegevens"): dict(limiet=None, verplicht=True,  altijd_tonen=True,  soort="url_of_mail"),
    ("algemene_informatie", "link_publiekspagina"): dict(limiet=None, verplicht=False, altijd_tonen=False, soort="url"),
    ("algemene_informatie", "publicatiecategorie"): dict(limiet=None, verplicht=True, altijd_tonen=True, soort="tekst"),
    ("algemene_informatie", "link_bronregistratie"): dict(limiet=None, verplicht=False, altijd_tonen=False, soort="url"),

    ("verantwoord_gebruik", "doel_en_impact"):       dict(limiet=2500, verplicht=False, altijd_tonen=True,  soort="tekst"),
    ("verantwoord_gebruik", "afwegingen"):           dict(limiet=2500, verplicht=False, altijd_tonen=True,  soort="tekst"),
    ("verantwoord_gebruik", "menselijke_tussenkomst"): dict(limiet=2500, verplicht=False, altijd_tonen=True, soort="tekst"),
    ("verantwoord_gebruik", "risicobeheer"):         dict(limiet=2500, verplicht=False, altijd_tonen=True,  soort="tekst"),
    ("verantwoord_gebruik", "wettelijke_basis"):     dict(limiet=2500, verplicht=False, altijd_tonen=False, soort="tekst"),
    ("verantwoord_gebruik", "link_wettelijke_basis"): dict(limiet=None, verplicht=False, altijd_tonen=True,  soort="url"),
    ("verantwoord_gebruik", "titel_wettelijke_basis"): dict(limiet=100, verplicht=False, altijd_tonen=False, soort="tekst"),
    ("verantwoord_gebruik", "verwerkingsregister"):  dict(limiet=None, verplicht=False, altijd_tonen=False, soort="url"),
    ("verantwoord_gebruik", "impacttoetsen"):        dict(limiet=None, verplicht=False, altijd_tonen=True,  soort="tekst"),
    ("verantwoord_gebruik", "link_impacttoets"):     dict(limiet=None, verplicht=False, altijd_tonen=False, soort="url"),
    ("verantwoord_gebruik", "toelichting_impacttoetsen"): dict(limiet=2500, verplicht=False, altijd_tonen=False, soort="tekst"),

    ("werking", "gegevens"):           dict(limiet=2500, verplicht=False, altijd_tonen=True,  soort="tekst"),
    ("werking", "link_gegevensbron"):  dict(limiet=None, verplicht=False, altijd_tonen=False, soort="url"),
    ("werking", "titel_gegevensbron"): dict(limiet=500,  verplicht=False, altijd_tonen=False, soort="tekst"),
    ("werking", "technische_werking"): dict(limiet=5000, verplicht=False, altijd_tonen=True,  soort="tekst"),
    ("werking", "leverancier"):        dict(limiet=200,  verplicht=False, altijd_tonen=True,  soort="tekst"),
    ("werking", "link_broncode"):      dict(limiet=None, verplicht=False, altijd_tonen=False, soort="url"),

    ("metadata", "taal"):      dict(limiet=None, verplicht=True,  altijd_tonen=False, soort="tekst"),
    ("metadata", "schema"):    dict(limiet=None, verplicht=True,  altijd_tonen=False, soort="tekst"),
    ("metadata", "bron_id"):   dict(limiet=100,  verplicht=False, altijd_tonen=False, soort="tekst"),
    ("metadata", "zoektermen"): dict(limiet=2500, verplicht=False, altijd_tonen=False, soort="tekst"),
}

STATUS_KEUZES = {"In ontwikkeling", "In gebruik", "Buiten gebruik"}
CATEGORIE_KEUZES = {"Hoog-risico AI-systemen", "Impactvolle algoritmes", "Overige algoritmes"}
DATUM_RE = re.compile(r"^\d{4}-\d{2}$")
MAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def is_leeg(waarde):
    if waarde is None:
        return True
    if isinstance(waarde, str):
        return waarde.strip() == ""
    if isinstance(waarde, list):
        return len(waarde) == 0
    return False


def main():
    if len(sys.argv) != 2:
        print("Gebruik: python scripts/validate.py <pad-naar-ingevuld.json>")
        sys.exit(2)

    pad = sys.argv[1]
    try:
        with open(pad, encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"FOUT: bestand niet gevonden: {pad}")
        sys.exit(2)
    except json.JSONDecodeError as e:
        print(f"FOUT: ongeldige JSON: {e}")
        sys.exit(2)

    fouten = []
    waarschuwingen = []

    for (sectie, sleutel), eig in FIELDS.items():
        label = f"{sectie}.{sleutel}"
        waarde = data.get(sectie, {}).get(sleutel)
        leeg = is_leeg(waarde)

        # verplicht / altijd tonen
        if leeg:
            if eig["verplicht"]:
                fouten.append(f"{label}: verplicht veld is leeg.")
            elif eig["altijd_tonen"]:
                waarschuwingen.append(f"{label}: 'altijd tonen'-veld is leeg; op de site verschijnt 'Veld niet ingevuld'.")
            continue

        # tekstvelden: geen regeleinden, tekenlimiet
        if eig["soort"] in ("tekst", "url", "url_of_mail", "datum") and isinstance(waarde, str):
            if "\n" in waarde or "\r" in waarde:
                fouten.append(f"{label}: bevat een regeleinde (enter); het register ondersteunt geen enters.")
            if re.search(r"^\s*[-*\u2022]\s", waarde, re.MULTILINE):
                waarschuwingen.append(f"{label}: lijkt een opsomming te bevatten; opsommingen worden niet ondersteund.")
            if eig["limiet"] is not None and len(waarde) >= eig["limiet"]:
                fouten.append(f"{label}: {len(waarde)} tekens; limiet is < {eig['limiet']}.")

        # keuzevelden
        if sleutel == "status" and waarde not in STATUS_KEUZES:
            fouten.append(f"{label}: '{waarde}' is geen geldige status ({', '.join(sorted(STATUS_KEUZES))}).")
        if sleutel == "publicatiecategorie" and waarde not in CATEGORIE_KEUZES:
            fouten.append(f"{label}: '{waarde}' is geen geldige categorie ({', '.join(sorted(CATEGORIE_KEUZES))}).")

        # datum
        if eig["soort"] == "datum" and not DATUM_RE.match(str(waarde)):
            fouten.append(f"{label}: '{waarde}' heeft niet het formaat yyyy-mm.")

        # url
        if eig["soort"] == "url" and not str(waarde).startswith("https://"):
            fouten.append(f"{label}: URL moet met https:// beginnen.")

        # url of mail
        if eig["soort"] == "url_of_mail":
            w = str(waarde).strip()
            if not (w.startswith("https://") or MAIL_RE.match(w)):
                fouten.append(f"{label}: moet een geldig e-mailadres of een https://-URL zijn.")

    # metadata vaste waarden
    taal = data.get("metadata", {}).get("taal")
    if taal and taal != "nld":
        waarschuwingen.append(f"metadata.taal: '{taal}' — op dit moment ondersteunt het register alleen 'nld'.")
    schema = data.get("metadata", {}).get("schema")
    if schema and schema not in {"0.3.0", "0.3.1", "0.4.0", "1.0.0"}:
        fouten.append(f"metadata.schema: '{schema}' is geen ondersteunde schemaversie (gebruik 1.0.0).")

    # rapport
    print(f"Validatie van: {pad}\n")
    if fouten:
        print(f"FOUTEN ({len(fouten)}):")
        for f_ in fouten:
            print(f"  - {f_}")
        print()
    if waarschuwingen:
        print(f"WAARSCHUWINGEN ({len(waarschuwingen)}):")
        for w in waarschuwingen:
            print(f"  - {w}")
        print()
    if not fouten and not waarschuwingen:
        print("Geen fouten of waarschuwingen. De registratie voldoet aan de gecontroleerde regels.")
    elif not fouten:
        print("Geen blokkerende fouten. Loop de waarschuwingen na en lever daarna op.")

    sys.exit(1 if fouten else 0)


if __name__ == "__main__":
    main()
