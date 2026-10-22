
class Depot:
    """Conserve les produits récupérés pendant l'exécution."""

    def __init__(self):
        self.produits = []

    def ajouter_tous(self, produits):
        self.produits.extend(produits)

    def obtenir_tous(self):
        return self.produits
