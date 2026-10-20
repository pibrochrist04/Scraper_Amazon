
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def creer_driver():
    """Configure et crée une instance de Chrome."""

    options = Options()

    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)

    return driver
