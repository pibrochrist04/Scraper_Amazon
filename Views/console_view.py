
def afficher_produits(produits):
    if not produits:
        print("Aucun produit à afficher.")
        return

    for index, produit in enumerate(produits, start=1):
        print(f"\n--- Produit {index} ---")
        print(f"Nom : {produit.nom}")
        print(f"Prix : {produit.prix or 'Non disponible'}")
        print(f"Note : {produit.note or 'Non disponible'}")
        print(
            f"Nombre d'avis : "
            f"{produit.nombre_avis or 'Non disponible'}"
        )
        print(f"URL : {produit.url or 'Non disponible'}")
