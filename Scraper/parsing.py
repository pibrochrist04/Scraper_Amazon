def extraire_texte(element):
    """
    Récupère le texte d'un élément HTML
    """
    if element is None: 
        return ""
    
    return element.text.strip()

def extraire_attribut(element, attribut): 
    
    """
    Récupère un attribut HTML, par exemple href.
    """
    
    if attribut is None:
        return ""
    
    return element.get_attribut(attribut) or ""