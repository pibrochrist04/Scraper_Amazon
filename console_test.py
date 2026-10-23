
from Models.produit import Produit
from Views.console_view import ConsoleView

produits = [
    Produit(
        nom="HP Pavilion 15",
        prix="499,99 €",
        lien="https://www.amazon.fr/",
        disponibilite="En stock"
    ),
    Produit(
        nom="Lenovo IdeaPad Slim 3",
        prix="429,00 €",
        lien="https://www.amazon.fr/",
        disponibilite="Non précisée"
    )
]

vue = ConsoleView()
vue.afficher_produits(produits)
