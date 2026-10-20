
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

EXPORT_DIR = BASE_DIR / "exports"
EXPORT_FILE = EXPORT_DIR / "produits.csv"

# Recherche de démonstration sur Amazon France
AMAZON_URL = "https://www.amazon.fr/s?k=clavier"

# Temps d'attente après le chargement de la page
PAGE_WAIT_SECONDS = 3
    