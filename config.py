from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

AMAZON_URL = "https://www.amazon.fr"
HEADLESS = False
TIMEOUT = 15
PAGES_MAX = 3
DELAI_ENTRE_PAGES = (3, 6)

EXPORT_DIR = BASE_DIR / "exports"