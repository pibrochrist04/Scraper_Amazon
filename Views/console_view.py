
class ConsoleView:
    """Gère l'affichage des produits dans le terminal."""

    def afficher_produits(self, produits):
        if not produits:
            print("Aucun produit trouvé.")
            return

        print("\n" + "=" * 60)
        print("          RÉSULTATS DE RECHERCHE AMAZON")
        print("=" * 60)

        for index, produit in enumerate(produits, start=1):
            print(f"\nProduit n° {index}")
            print("-" * 60)

            if isinstance(produit, dict):
                print(f"Nom : {produit.get('nom', '')}")
                print(f"Prix : {produit.get('prix', '')}")
                print(f"Lien : {produit.get('lien', '')}")
                print(
                    f"Disponibilité : "
                    f"{produit.get('disponibilite', '')}"
                )
            else:
                print(produit)

        print("\n" + "=" * 60)
        print(f"Nombre de produits : {len(produits)}")
        print("=" * 60)
