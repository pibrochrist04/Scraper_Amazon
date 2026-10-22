
from bs4 import BeautifulSoup
from Models.produit import Produit


def extraire_produits(html):
    """Transforme le HTML d'une page en liste de produits."""

    soup = BeautifulSoup(html, "html.parser")

    produits = []

    cartes = soup.select(
        'div[data-component-type="s-search-result"]'
    )

    for carte in cartes:
        titre = carte.select_one("h2 a span")
        lien = carte.select_one("h2 a")
        prix = carte.select_one(".a-price .a-offscreen")
        note = carte.select_one("span.a-icon-alt")
        avis = carte.select_one(
            "a[href*='#customerReviews'] span"
        )

        if titre is None:
            continue

        url = ""

        if lien and lien.get("href"):
            href = lien["href"]

            if href.startswith("/"):
                url = "https://www.amazon.fr" + href
            else:
                url = href

        produit = Produit(
            nom=titre.get_text(" ", strip=True),
            prix=prix.get_text(strip=True) if prix else "",
            note=note.get_text(strip=True) if note else "",
            nombre_avis=avis.get_text(strip=True) if avis else "",
            url=url,
        )

        produits.append(produit)

    return produits
