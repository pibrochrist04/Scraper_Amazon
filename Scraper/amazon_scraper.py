
from urllib.parse import quote_plus

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from Scraper.drivers import creer_driver, fermer_driver
from Scraper.parsing import extraire_texte, extraire_attribut
from config import AMAZON_URL, TIMEOUT


class AmazonScraper:
    """Recherche des produits sur Amazon avec Selenium."""

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
                    (By.CSS_SELECTOR, "div[data-component-type='s-search-result']")
                )
            )

            cartes = driver.find_elements(
                By.CSS_SELECTOR,
                "div[data-component-type='s-search-result']"
            )

            for carte in cartes:
                titre_element = carte.find_elements(
                    By.CSS_SELECTOR, "h2 a span"
                )

                prix_element = carte.find_elements(
                    By.CSS_SELECTOR, "span.a-price span.a-offscreen"
                )

                lien_element = carte.find_elements(
                    By.CSS_SELECTOR, "h2 a"
                )

                nom = (
                    extraire_texte(titre_element[0])
                    if titre_element else ""
                )

                prix = (
                    extraire_texte(prix_element[0])
                    if prix_element else ""
                )

                lien = (
                    extraire_attribut(lien_element[0], "href")
                    if lien_element else ""
                )

                if lien.startswith("/"):
                    lien = AMAZON_URL + lien

                if nom:
                    produits.append({
                        "nom": nom,
                        "prix": prix,
                        "lien": lien
                    })

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
