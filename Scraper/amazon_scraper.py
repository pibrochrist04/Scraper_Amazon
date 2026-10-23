from urllib.parse import quote_plus

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from Scraper.drivers import creer_driver, fermer_driver
from Scraper.parsing import extraire_texte, extraire_attribut
from config import AMAZON_URL, TIMEOUT


SELECTEUR_CARTE = "div[data-component-type='s-search-result']"

# Plusieurs sélecteurs possibles : Amazon change souvent son HTML.
# On essaie chacun dans l'ordre jusqu'à en trouver un qui fonctionne.
SELECTEURS_TITRE = ["h2 span", "h2"]
SELECTEURS_PRIX = ["span.a-price span.a-offscreen"]
SELECTEURS_LIEN = [
    "h2 a",
    "a:has(h2)",
    "a.a-link-normal.s-no-outline",
    "a[href*='/dp/']",
]


class AmazonScraper:
    """Recherche des produits sur Amazon avec Selenium."""

    def _premier_element(self, carte, selecteurs):
        """Retourne le premier élément trouvé parmi plusieurs sélecteurs."""
        for selecteur in selecteurs:
            elements = carte.find_elements(By.CSS_SELECTOR, selecteur)
            if elements:
                return elements[0]
        return None

    def rechercher_produits(self, mot_cle):
        if not mot_cle or not mot_cle.strip():
            return []

        driver = None
        produits = []

        try:
            driver = creer_driver()

            # Construire l'URL de recherche
            recherche = quote_plus(mot_cle.strip())
            url = f"{AMAZON_URL}/s?k={recherche}"

            driver.get(url)

            # Attendre l'apparition des résultats
            attente = WebDriverWait(driver, TIMEOUT)
            attente.until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, SELECTEUR_CARTE)
                )
            )

            cartes = driver.find_elements(By.CSS_SELECTOR, SELECTEUR_CARTE)
            print(f"[info] {len(cartes)} cartes trouvées sur la page.")

            for carte in cartes:
                nom = extraire_texte(
                    self._premier_element(carte, SELECTEURS_TITRE)
                )
                prix = extraire_texte(
                    self._premier_element(carte, SELECTEURS_PRIX)
                )
                lien = extraire_attribut(
                    self._premier_element(carte, SELECTEURS_LIEN), "href"
                )

                if lien.startswith("/"):
                    lien = AMAZON_URL + lien

                if nom:
                    produits.append({
                        "nom": nom,
                        "prix": prix,
                        "lien": lien
                    })

            print(f"[info] {len(produits)} produits extraits.")
            return produits

        except TimeoutException:
            print(
                "Aucun résultat n'a été détecté dans le délai prévu. "
                "Amazon a peut-être affiché une vérification."
            )
            return []

        finally:
            if driver is not None:
                fermer_driver(driver)