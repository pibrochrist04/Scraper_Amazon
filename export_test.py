
from Views.export_view import ExportView

produits = [
    {
        "nom": "Ordinateur portable HP",
        "prix": "499,99 €",
        "lien": "https://www.amazon.fr/",
        "disponibilite": "Disponible"
    },
    {
        "nom": "Souris sans fil",
        "prix": "19,99 €",
        "lien": "https://www.amazon.fr/",
        "disponibilite": "Disponible"
    }
]

exportateur = ExportView()
exportateur.exporter_csv(produits, "ordinateur portable")
