from Scraper.amazon_scraper import AmazonScraper
from Models.depot import Depot
from Views.console_view import ConsoleView
from Views.export_view import ExportView
from App.Controllers.scraping_controllers import ScrapingController


def main():
    # 1. Créer les objets dont le contrôleur a besoin
    scraper = AmazonScraper()
    depot = Depot()
    console_view = ConsoleView()
    export_view = ExportView()

    # 2. Créer le contrôleur et lui donner ces objets
    controleur = ScrapingController(
        scraper, depot, console_view, export_view
    )

    print("=== SCRAPER AMAZON ===")

    # 3. Boucle : l'utilisateur peut faire plusieurs recherches
    while True:
        mot_cle = input("\nQuel produit cherchez-vous ? ")
        controleur.lancer_recherche(mot_cle)

        reponse = input("\nFaire une autre recherche ? (o/n) : ")
        if reponse.strip().lower() != "o":
            break

    total = len(depot.obtenir_tous())
    print(f"\nTerminé. {total} produit(s) récupéré(s) pendant cette session.")


if __name__ == "__main__":
    main()