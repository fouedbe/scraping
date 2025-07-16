# Scraper Smartphones Tunisianet

## 📋 Présentation
Ce projet permet de scraper les informations des smartphones depuis le site [tunisianet.com.tn](https://www.tunisianet.com.tn/596-smartphone-tunisie) et de contrôler le scraping via une interface web (Streamlit) et un backend Flask.

## 🗂️ Structure du projet
- `scraper.py` : Script principal de scraping (extraction des données, sauvegarde dans `data.json`).
- `scraper_server.py` : Serveur Flask pour lancer/pauser/reprendre/arrêter le scraping à distance (sauvegarde dans `resultats.json`).
- `app.py` : Interface Streamlit pour contrôler le scraping via le backend Flask.
- `requirements.txt` : Dépendances Python nécessaires.
- Fichiers de sortie :
  - `data.json` : Résultat du scraping via `scraper.py` (données détaillées).
  - `resultats.json` : Résultat du scraping via le serveur Flask (titres et URLs).
  - `smartphones.json`, `tayara_ads.json`, etc. : Exemples ou autres jeux de données.

## 🚀 Installation
1. **Installer les dépendances** :
   ```bash
   pip install -r requirements.txt
   ```
2. **Installer Chrome** (si ce n'est pas déjà fait) et s'assurer que le driver Chrome est compatible (géré automatiquement par `webdriver-manager`).

## ⚙️ Utilisation
### 1. Scraping direct (manuel)
```bash
python scraper.py
```
- Saisir le nombre de pages à scraper.
- Les résultats sont enregistrés dans `data.json`.

### 2. Scraping via serveur Flask (contrôle à distance)
- Lancer le serveur :
  ```bash
  python scraper_server.py
  ```
- Utiliser les endpoints :
  - `/start` (POST) : Démarrer le scraping
  - `/pause` (POST) : Mettre en pause
  - `/resume` (POST) : Reprendre
  - `/stop` (POST) : Arrêter
  - `/status` (GET) : Voir l'état
- Les résultats sont enregistrés dans `resultats.json`.

### 3. Interface web (Streamlit)
- Lancer l'interface :
  ```bash
  streamlit run app.py
  ```
- Permet de contrôler le scraping via le backend Flask (démarrer, pause, reprise, stop, suivi de la progression).

## 📦 Fichiers de sortie
- `data.json` : Données détaillées (titre, url, description, référence, disponibilité...)
- `resultats.json` : Liste simple (titre, url)
- `smartphones.json` : Exemple de données enrichies (avec prix)
- `tayara_ads.json` : Autres données (exemple d'annonces immobilières)

## 🗃️ Organisation recommandée
Pour plus de clarté, il est conseillé de séparer les scripts dans un dossier dédié :
```
scraper/
  ├── scraper.py
  └── scraper_server.py
```

---

# 🇹🇳 شرح المشروع بالتونسي

المشروع هذا يعمل سكرايبينغ (scraping) للسمارتفونات من موقع Tunisianet و يعطيك واجهة باش تتحكم في السكرايبينغ (تبدأ، توقف، تكمّل...).

## كيفاش تخدم بيه ؟
1. **ركّب الباكيجات** :
   ```bash
   pip install -r requirements.txt
   ```
2. **باش تسكرابي بيدك** :
   ```bash
   python scraper.py
   ```
   و تلقى الداتا في `data.json`
3. **باش تتحكم من بعيد (Flask + Streamlit)** :
   - شغّل السيرفر :
     ```bash
     python scraper_server.py
     ```
   - شغّل الواجهة :
     ```bash
     streamlit run app.py
     ```
   - تحكم من الواجهة (start, pause, resume, stop)
   - تلقى الداتا في `resultats.json`

## ملاحظة
- يلزم يكون عندك Google Chrome.
- السكرايبينغ يستعمل Selenium و WebDriver Manager.
- فما داتا أخرى في project (ex: smartphones.json, tayara_ads.json) كأمثلة.

---

**Auteur :**
- Projet open-source pour l'apprentissage et l'automatisation du scraping en Tunisie 🇹🇳 