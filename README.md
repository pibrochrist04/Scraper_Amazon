# 🛒 Amazon Scraper

Programme Python qui recherche un produit sur **Amazon.fr**, extrait automatiquement les informations des résultats (nom, prix, lien) avec **Selenium**, puis les enregistre dans un fichier **CSV**.

Projet réalisé dans le cadre du cours de Python à l'Institut Ivoirien de Technologie (IIT).

---

## 📌 Sommaire

1. [Objectif du projet](#-objectif-du-projet)
2. [Fonctionnalités](#-fonctionnalités)
3. [Technologies utilisées](#-technologies-utilisées)
4. [Architecture du projet](#-architecture-du-projet)
5. [Fonctionnement](#-fonctionnement)
6. [Installation](#-installation)
7. [Utilisation](#-utilisation)
8. [Exemple de résultat](#-exemple-de-résultat)
9. [Difficultés rencontrées](#-difficultés-rencontrées)
10. [Limites](#-limites)
11. [Auteur](#-auteur)

---

## 🎯 Objectif du projet

Le **web scraping** consiste à faire faire à un programme ce qu'un humain fait à la main : ouvrir une page web, repérer les informations utiles et les recopier dans un tableau.

Ici, le programme :

1. demande à l'utilisateur le produit qu'il recherche ;
2. ouvre Chrome et effectue la recherche sur Amazon.fr ;
3. lit les résultats affichés ;
4. enregistre les données dans un fichier CSV exploitable avec Excel.

---

## ✨ Fonctionnalités

- Saisie du produit recherché par l'utilisateur
- Pilotage automatique de Google Chrome avec Selenium
- Extraction du **nom**, du **prix** et du **lien** de chaque produit
- Affichage des résultats dans la console
- Export des résultats dans un fichier CSV
- Gestion des erreurs : mot-clé vide, aucun résultat, délai dépassé, vérification anti-robot d'Amazon

---

## 🧰 Technologies utilisées

| Outil | Rôle |
|---|---|
| Python 3 | Langage du projet |
| Selenium | Pilotage du navigateur Chrome |
| Google Chrome | Navigateur utilisé pour charger Amazon |
| CSV (module standard) | Enregistrement des données |
| Git / GitHub | Versionnement et partage du code |

---

## 🏗️ Architecture du projet

Le projet sépare les responsabilités : chaque fichier a **un seul rôle**.

```
Amazon_scraping/
├── App/
│   └── Controllers/
│       └── scraping_controllers.py   # Chef d'orchestre
├── Models/
│   ├── produit.py                    # Représente un produit
│   └── depot.py                      # Stocke la liste des produits
├── Scraper/
│   ├── drivers.py                    # Démarre / ferme Chrome
│   ├── amazon_scraper.py             # Effectue la recherche sur Amazon
│   └── parsing.py                    # Extrait les textes et attributs HTML
├── Views/
│   ├── console_view.py               # Affichage dans le terminal
│   └── export_view.py                # Export CSV
├── data/                             # Fichiers CSV générés
├── config.py                         # Paramètres globaux
├── main.py                           # Point d'entrée du programme
└── requirements.txt                  # Dépendances
```

### Rôle de chaque fichier

| Fichier | Rôle |
|---|---|
| `main.py` | Point d'entrée : demande le produit à l'utilisateur et lance le contrôleur |
| `scraping_controllers.py` | Coordonne les étapes : recherche, affichage, export |
| `drivers.py` | Configure et démarre Chrome avec Selenium, puis le ferme proprement |
| `amazon_scraper.py` | Ouvre la page de recherche Amazon, attend les résultats et lit chaque carte produit |
| `parsing.py` | Fonctions utilitaires pour extraire le texte et les attributs d'un élément HTML |
| `produit.py` | Modèle de données : un produit avec son nom, son prix et son lien |
| `depot.py` | Conserve la liste des produits récupérés |
| `console_view.py` | Affiche les produits dans le terminal |
| `export_view.py` | Écrit les produits dans un fichier CSV |
| `config.py` | Paramètres : URL d'Amazon, mode headless, délai maximal, dossier d'export |

---

## ⚙️ Fonctionnement

```
main.py
   │  (demande le produit)
   ▼
ScrapingController
   │
   ├──► AmazonScraper ──► drivers.py   (ouvre Chrome)
   │         │
   │         └──────────► parsing.py   (extrait nom, prix, lien)
   │
   ├──► console_view.py  (affiche les résultats)
   │
   └──► export_view.py   (crée le fichier CSV)
```

### Les étapes du scraping

1. **Ouvrir la page** : Chrome est lancé et va sur `https://www.amazon.fr/s?k=<produit>`.
2. **Attendre les résultats** : Selenium attend que les cartes produit apparaissent (`WebDriverWait`).
3. **Extraire les données** : pour chaque carte, le programme lit le titre, le prix et le lien grâce à des **sélecteurs CSS**.
4. **Exporter** : les données sont enregistrées dans un fichier CSV.

---

## 🚀 Installation

### Prérequis

- Python 3.10 ou plus récent
- Google Chrome installé
- Git

### Étapes

```bash
# 1. Cloner le dépôt
git clone https://github.com/pibrochrist04/Scraper_Amazon.git
cd Scraper_Amazon

# 2. Créer l'environnement virtuel
python -m venv .venv

# 3. L'activer
# Windows (PowerShell) :
.venv\Scripts\Activate.ps1
# Linux / macOS :
source .venv/bin/activate

# 4. Installer les dépendances
pip install -r requirements.txt
```

> Selenium récupère automatiquement le pilote Chrome nécessaire (Selenium Manager). Une connexion Internet est requise au premier lancement.

---

## ▶️ Utilisation

```bash
python main.py
```

Le programme demande alors :

```
Quel produit recherchez-vous ? clavier
```

Chrome s'ouvre, Amazon se charge, les produits sont affichés dans le terminal, puis enregistrés dans un fichier CSV dans le dossier `data/`.

### Paramètres modifiables (`config.py`)

| Paramètre | Description |
|---|---|
| `AMAZON_URL` | Adresse du site Amazon |
| `HEADLESS` | `False` : Chrome visible. `True` : Chrome sans fenêtre |
| `TIMEOUT` | Délai maximal d'attente (en secondes) |

---

## 📄 Exemple de résultat

Fichier CSV généré :

```csv
nom,prix,lien
Clavier Logitech K120,12,99 €,https://www.amazon.fr/...
Clavier Razer BlackWidow,89,00 €,https://www.amazon.fr/...
```

---

## 🧩 Difficultés rencontrées

- **Aucun produit récupéré** : les sélecteurs CSS ne correspondaient pas au HTML réel d'Amazon. Il a fallu inspecter la page (clic droit → *Inspecter*) pour trouver les bonnes balises.
- **Prix vide** : le prix est dans un élément visuellement caché (`span.a-offscreen`). Avec Selenium, `.text` ne renvoie que le texte visible ; il faut lire l'attribut `textContent`.
- **Cartes parasites** : certains blocs de la page (bannières, publicités) ressemblent à des produits. Ils sont filtrés grâce à l'attribut `data-asin`.
- **Fichiers `.pyc`** : le dossier `__pycache__` est généré automatiquement par Python, il est ignoré par Git via `.gitignore`.

---

## ⚠️ Limites

- Amazon modifie régulièrement la structure de ses pages : les sélecteurs CSS peuvent devoir être mis à jour.
- Amazon peut afficher un **CAPTCHA** ou bloquer les accès automatisés. Dans ce cas, le programme l'indique et ne renvoie aucun résultat.
- Seule la première page de résultats est analysée.
- Ce projet est réalisé **à but pédagogique**. Avant toute utilisation à plus grande échelle, il faut consulter les conditions d'utilisation du site.

---

## 👤 Auteur

**TAYE Christ Emmanuel**
Licence 2 Génie logiciel, Institut Ivoirien de Technologie (IIT), bassam, Côte d'Ivoire

Projet réalisé dans le cadre du cours de Python.