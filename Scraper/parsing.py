def extraire_texte(element):
    """
    Récupère le texte d'un élément HTML.

    On utilise textContent plutôt que .text : le prix d'Amazon est dans
    un <span class="a-offscreen"> invisible, et .text renvoie "" pour
    un élément invisible.
    """
    if element is None:
        return ""

    texte = element.get_attribute("textContent") or ""
    return texte.strip()


def extraire_attribut(element, attribut):
    """
    Récupère un attribut HTML, par exemple href.
    """
    if element is None or not attribut:
        return ""

    return element.get_attribute(attribut) or ""