
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

from config import AMAZON_URL
from Scraper.drivers import creer_driver
from Scraper.parsing import extraire_produits


def scraper_amazon(url=AMAZON_URL):
    driver = creer_driver()

    try:
        driver.get(url)

        attente = WebDriverWait(driver, 20)

        attente.until(
            lambda navigateur: navigateur.find_elements(
                By.CSS_SELECTOR,
                'div[data-component-type="s-search-result"]'
            )
        )

        html = driver.page_source
        produits = extraire_produits(html)

        return produits

    except TimeoutException:
        print("Aucun résultat détecté dans le délai imparti.")
        return []

    finally:
        driver.quit()
