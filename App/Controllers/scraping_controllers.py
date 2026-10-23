from Models.produit import Produit


class ScrapingController:
    """Chef d'orchestre : relie le scraper, le dépôt et les vues."""

    def __init__(self, scraper, depot, console_view, export_view):
        self.scraper = scraper
        self.depot = depot
        self.console_view = console_view
        self.export_view = export_view

    def lancer_recherche(self, mot_cle):
        # 1. Vérifier la saisie de l'utilisateur
        if not mot_cle or not mot_cle.strip():
            print("Erreur : veuillez bien saisir le nom du produit.")
            return []

        mot_cle = mot_cle.strip()

        # 2. Récupérer les données brutes (liste de dictionnaires)
        try:
            donnees = self.scraper.rechercher_produits(mot_cle)
        except RuntimeError as erreur:
            # Levée par creer_driver() si Chrome ne démarre pas
            print(f"Erreur : {erreur}")
            return []

        if not donnees:
            print("Aucun produit trouvé.")
            return []

        # 3. Transformer chaque dictionnaire en objet Produit
        produits = [
            Produit(
                nom=donnee.get("nom", ""),
                prix=donnee.get("prix", ""),
                lien=donnee.get("lien", ""),
                disponibilite=donnee.get("disponibilite", ""),
            )
            for donnee in donnees
        ]

        # 4. Conserver les produits dans le dépôt
        self.depot.ajouter_tous(produits)

        # 5. Afficher puis exporter
        self.console_view.afficher_produits(produits)
        self.export_view.exporter_csv(produits, mot_cle)

        return produits