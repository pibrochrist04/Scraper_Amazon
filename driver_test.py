from Scraper.amazon_scraper import AmazonScraper

scraper = AmazonScraper()
produits = scraper.rechercher_produits("clavier")

print(f"\nProduits récupérés : {len(produits)}")
for p in produits[:5]:
    print(p)