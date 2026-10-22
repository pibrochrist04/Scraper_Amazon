
from Scraper.amazon_scraper import scraper_amazon
from Models.depot import Depot
from Views.console_view import afficher_produits
from Views.export_view import exporter_produits


def lancer_scraping():
    produits_recuperes = scraper_amazon()

    depot = Depot()
    depot.ajouter_tous(produits_recuperes)

    produits = depot.obtenir_tous()

    afficher_produits(produits)

    if produits:
        exporter_produits(produits)

    return produits
