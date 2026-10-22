
import csv

from config import EXPORT_DIR, EXPORT_FILE


def exporter_produits(produits):
    EXPORT_DIR.mkdir(parents=True, exist_ok=True)

    champs = [
        "nom",
        "prix",
        "note",
        "nombre_avis",
        "url",
    ]

    with EXPORT_FILE.open(
        "w",
        newline="",
        encoding="utf-8-sig",
    ) as fichier:
        writer = csv.DictWriter(
            fichier,
            fieldnames=champs,
        )

        writer.writeheader()

        for produit in produits:
            writer.writerow({
                "nom": produit.nom,
                "prix": produit.prix,
                "note": produit.note,
                "nombre_avis": produit.nombre_avis,
                "url": produit.url,
            })

    print(f"Fichier exporté : {EXPORT_FILE}")
