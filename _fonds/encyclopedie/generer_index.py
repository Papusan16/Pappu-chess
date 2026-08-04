#!/usr/bin/env python3
"""Régénère _fonds/encyclopedie/INDEX.json depuis les front-matter des entrées.

Le manifeste est un CACHE D'AFFICHAGE, pas une source : il ne sert qu'à
l'overlay (pastille « entrée riche », effacement de la fiche en dur qu'une
entrée périme, résolution cliquable/amorce des liens internes). La vérité
reste le fichier .md, chargé au clic. Un manifeste périmé fait au pire
apparaître un doublon dans la liste — jamais perdre un contenu.

Contrôle fait au passage : chaque id cité dans `remplace:` doit exister
parmi les fiches en dur de Papu_Chess.html (ENC / OPS / PEOPLE). Une faute
de frappe n'efface rien et ne dirait rien sans ce contrôle.

Usage : python3 _fonds/encyclopedie/generer_index.py
"""
import json
import re
import sys
from pathlib import Path

ICI = Path(__file__).resolve().parent
RACINE = ICI.parent.parent
APP = RACINE / "Papu_Chess.html"

# Attributs recopiés dans le manifeste. Le reste du front-matter (sources,
# notes de provenance…) n'a rien à faire ici : il se lit dans le .md.
SCALAIRES = ("id", "nom", "phase", "onglet")
LISTES = ("rayons", "alias", "liens", "remplace")


def lire_front_matter(texte):
    """Sous-ensemble de YAML suffisant pour nos en-têtes : scalaires,
    listes en ligne ([a, b]) et listes à tirets. Les blocs imbriqués
    (sources:) sont sautés, ils ne nous intéressent pas ici."""
    m = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n", texte, re.S)
    if not m:
        return {}
    meta, lignes, i = {}, m.group(1).split("\n"), 0
    while i < len(lignes):
        cle = re.match(r"^([a-zA-Z_]+):\s*(.*)$", lignes[i])
        if not cle:
            i += 1
            continue
        nom, reste = cle.group(1), cle.group(2).strip()
        i += 1
        if reste:
            if reste.startswith("[") and reste.endswith("]"):
                meta[nom] = [x.strip() for x in reste[1:-1].split(",") if x.strip()]
            else:
                meta[nom] = reste.strip('"')
            continue
        items = []
        while i < len(lignes) and re.match(r"^\s+\S", lignes[i]):
            tiret = re.match(r"^\s*-\s*(.*)$", lignes[i])
            # un tiret suivi d'une clé (« - nature: … ») ouvre un bloc
            # structuré : ce n'est pas une liste de valeurs, on l'ignore
            if tiret and not re.match(r"^[a-zA-Z_]+:", tiret.group(1)):
                items.append(tiret.group(1).strip().strip('"'))
            i += 1
        meta[nom] = items
    return meta


def onglet_derive(meta):
    """Rayon (+ phase) → onglet d'affichage. RECOPIE de la table `encTabOf` de
    Papu_Chess.html : les deux doivent rester d'accord (elle ne sert ici qu'à
    signaler une incohérence, l'app reste seule maîtresse de l'affichage)."""
    if meta.get("onglet"):
        return meta["onglet"]
    rayon = (meta.get("rayons") or [""])[0].lower()
    phase = (meta.get("phase") or "").lower()
    if rayon.startswith("histoire"):
        return "history"
    if rayon.startswith("pratique"):
        return "practice"
    if rayon.startswith("m"):
        return "method"
    if rayon.startswith("th"):
        return "openings" if phase == "ouverture" else "strategy"
    if rayon.startswith("te"):
        return "endgames" if phase == "finale" else "tactics"
    return "tactics"


def ids_fiches_en_dur():
    """Les fiches en dur de l'application : id → onglet (ENC.*, OPS, PEOPLE)."""
    if not APP.exists():
        return None
    h = APP.read_text(encoding="utf-8")
    # onglet d'origine de chaque lot de fiches, tel que SECTIONS le déclare
    onglet_du_lot = {"tactics": "tactics", "strategy": "strategy", "endgames": "endgames",
                     "method": "method", "OPS": "openings", "PEOPLE": "history"}
    ids = {}
    for cle in ("ENC={", "OPS=[", "PEOPLE={"):
        i = h.find(cle)
        if i < 0:
            continue
        ouvre = h[i + len(cle) - 1]
        ferme = {"{": "}", "[": "]"}[ouvre]
        prof, j = 0, i + len(cle) - 1
        while j < len(h):
            if h[j] == ouvre:
                prof += 1
            elif h[j] == ferme:
                prof -= 1
                if prof == 0:
                    break
            j += 1
        blob = json.loads(h[i + len(cle) - 1: j + 1])
        if isinstance(blob, dict) and cle.startswith("PEOPLE"):
            ids.update({k: onglet_du_lot["PEOPLE"] for k in blob})
        elif isinstance(blob, dict):  # ENC : un lot par onglet
            for nom_lot, lot in blob.items():
                ids.update({x["id"]: onglet_du_lot.get(nom_lot, nom_lot)
                            for x in lot if "id" in x})
        else:  # OPS
            ids.update({x["id"]: onglet_du_lot["OPS"] for x in blob if "id" in x})
    return ids


def main():
    entrees, avertissements = [], []
    for f in sorted(ICI.glob("*.md")):
        if f.name == "FORMAT.md":
            continue
        texte = f.read_text(encoding="utf-8")
        meta = lire_front_matter(texte)
        if not meta.get("id"):
            avertissements.append(f"{f.name} : pas d'`id` en front-matter — ignorée.")
            continue
        if meta["id"] != f.stem:
            avertissements.append(
                f"{f.name} : id « {meta['id']} » ≠ nom de fichier « {f.stem} »."
            )
        e = {c: meta[c] for c in SCALAIRES if meta.get(c)}
        e.update({c: meta[c] for c in LISTES if meta.get(c)})
        # nombre de démonstrations : compté sur les titres, sans parser le corps.
        # `(?!s)` écarte le titre chapeau « ## Démonstrations » qui n'en est pas une.
        e["demos"] = len(re.findall(r"^###?\s+Démonstration(?!s)", texte, re.M))
        entrees.append(e)

    dur = ids_fiches_en_dur()
    if dur is None:
        avertissements.append("Papu_Chess.html introuvable — `remplace:` non vérifié.")
    else:
        for e in entrees:
            onglet = onglet_derive(e)
            for cible in e.get("remplace", []):
                if cible not in dur:
                    avertissements.append(
                        f"{e['id']} : remplace « {cible} », qui n'est aucune fiche en dur."
                    )
                elif dur[cible] != onglet:
                    # L'entrée effacerait une fiche d'un onglet pour réapparaître dans un
                    # autre : le joueur la perdrait de vue. `onglet:` sert exactement à ça.
                    avertissements.append(
                        f"{e['id']} : rangée dans « {onglet} » mais périme « {cible} », "
                        f"qui vit dans « {dur[cible]} » — ajoute `onglet: {dur[cible]}` "
                        f"si c'est là que le joueur doit la trouver."
                    )

    (ICI / "INDEX.json").write_text(
        json.dumps(entrees, ensure_ascii=False, indent=1) + "\n", encoding="utf-8"
    )
    print(f"INDEX.json : {len(entrees)} entrée(s).")
    for e in entrees:
        print(f"  · {e['id']:26} onglet={onglet_derive(e):9} démos={e['demos']} "
              f"remplace={e.get('remplace', [])}")
    for a in avertissements:
        print(f"  ⚠ {a}")
    return 1 if avertissements else 0


if __name__ == "__main__":
    sys.exit(main())
