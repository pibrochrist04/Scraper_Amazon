from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException

from config import HEADLESS, TIMEOUT


def creer_driver():
    
    options = Options
    
    if HEADLESS:
        options.add_argument("--headless=new")
    
    # Configurations du navigateur
    options.add_argument("--window-size=1920,1000")
    options.add_argument("--disable-notifactions")
    options.add_argument("--lang=fr-FR")
    
    try:
        # Démarrer Chrome
        driver = webdriver.chrome(options=options)
        
        # Définir le délai maximal de chargement d'une page
        driver.set_page_load_timeout(TIMEOUT)
        
        return driver
    
    except WebDriverException as erreur:
        raise RuntimeError(
            "Impossible de demarrer chrome avec selenium"
            "Verifier l'installation de selenium et chrome"
        ) from erreur
        
def fermer_driver(driver):
    if driver is not None:
        driver.quit()