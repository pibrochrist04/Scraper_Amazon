
import csv
import os
from datetime import datetime


class ExportView:
    """Gère l'exportation des produits dans un fichier CSV."""

    def exporter_csv(self, produits, mot_cle):
        if not produits:
            print("Aucun produit à exporter.")
            return

        dossier = "exports"
        os.makedirs(dossier, exist_ok=True)

        nom_fichier = (
            f"{mot_cle.strip().replace(' ', '_')}_"
            f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        )

        chemin = os.path.join(dossier, nom_fichier)

        with open(chemin, "w", newline="", encoding="utf-8-sig") as fichier:
            colonnes = ["nom", "prix", "lien", "disponibilite"]
            writer = csv.DictWriter(fichier, fieldnames=colonnes)

            writer.writeheader()

            for produit in produits:
                if isinstance(produit, dict):
                    writer.writerow({
                        "nom": produit.get("nom", ""),
                        "prix": produit.get("prix", ""),
                        "lien": produit.get("lien", ""),
                        "disponibilite": produit.get("disponibilite", "")
                    })
                else:
                    writer.writerow({
                        "nom": produit.nom,
                        "prix": produit.prix,
                        "lien": produit.lien,
                        "disponibilite": produit.disponibilite
                    })

        print(f"Exportation réussie ! Fichier créé : {chemin}")
