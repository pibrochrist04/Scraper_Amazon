
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException

from config import HEADLESS, TIMEOUT


def creer_driver():
    """
    Configure et démarre le navigateur Chrome.
    Retourne l'objet WebDriver si le démarrage réussit.
    """

    options = Options()

    # Exécuter Chrome sans afficher sa fenêtre si HEADLESS = True
    if HEADLESS:
        options.add_argument("--headless=new")

    # Configurations du navigateur
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-notifications")
    options.add_argument("--lang=fr-FR")

    try:
        # Démarrer Chrome
        driver = webdriver.Chrome(options=options)

        # Définir le délai maximal de chargement d'une page
        driver.set_page_load_timeout(TIMEOUT)

        return driver

    except WebDriverException as erreur:
        raise RuntimeError(
            "Impossible de démarrer Chrome avec Selenium. "
            "Vérifie l'installation de Chrome et de Selenium."
        ) from erreur


def fermer_driver(driver):
    """
    Ferme le navigateur et libère ses ressources.
    """

    if driver is not None:
        driver.quit()
