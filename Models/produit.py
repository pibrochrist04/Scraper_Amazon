
from dataclasses import dataclass


@dataclass
class Produit:
    nom: str
    prix: str = ""
    note: str = ""
    nombre_avis: str = ""
    url: str = ""
