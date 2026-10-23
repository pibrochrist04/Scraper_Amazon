
from Scraper.amazon_scraper import scraper_amazon
from Views.console_view import afficher_produits
from Views.export_view import exporter_produits


def lancer_scraping():
    """Coordonne le scraping, l'affichage et l'export."""

    print("Lancement du scraping...")

    produits = scraper_amazon()

    afficher_produits(produits)

    if produits:
        exporter_produits(produits)
    else:
        print("Aucun produit à exporter.")

    return produits
