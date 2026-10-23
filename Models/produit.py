class Produit:
    def __init__(self, nom, prix="", lien="", disponibilite=""):
        self.nom = nom
        self.prix = prix
        self.lien = lien
        self.disponibilite = disponibilite
        
    def __str__(self):
        return(
            f"Nom : {self.nom}\n"
            f"Prix : {self.prix}\n"
            f"Lien : {self.lien}\n"
            f"Disponibilité : {self.disponibilite}"
        )