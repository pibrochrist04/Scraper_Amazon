from Scraper.drivers import creer_driver, fermer_driver

driver = None

try:
    driver = creer_driver()
    driver.get("https://www.amazon.fr")

    print("Titre de la page :", driver.title)
    print("URL actuelle :", driver.current_url)

except Exception as erreur:
    print("Erreur :", erreur)

finally:
    fermer_driver(driver)