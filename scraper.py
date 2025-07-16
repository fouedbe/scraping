from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import json
import time
import streamlit as st

BASE_URL = "ton site"


def get_links(driver, page_url):
    driver.get(page_url)
    time.sleep(4)
    links = [a.get_attribute('href') for a in driver.find_elements(By.CSS_SELECTOR, ".product-title > a")]
    print(f"{len(links)} liens extraits de {page_url}")
    for l in links:
        print(l)
    return links


def get_article_data(driver, url):
    driver.get(url)
    time.sleep(2)
    # Titre du produit
    titre = driver.find_element(By.CSS_SELECTOR, "h1.h1").text.strip()
    # Contenu/description du produit
    contenu = driver.find_element(By.CSS_SELECTOR, "div.product-information").text.strip()
    # Référence
    try:
        reference = driver.find_element(By.CSS_SELECTOR, "span[itemprop='sku']").text.strip()
    except:
        reference = ""
    # Disponibilité magasin
    disponibilite = []
    try:
        dispo_elements = driver.find_elements(By.CSS_SELECTOR, "div#product-availability-list li")
        for el in dispo_elements:
            disponibilite.append(el.text.strip())
    except:
        disponibilite = []
    return {
        "titre": titre,
        "url": url,
        "contenu": contenu,
        "reference": reference,
        "disponibilite_magasin": disponibilite
    }


def scraper(start_page, end_page):
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    data = []
    all_links = []

    for i in range(start_page, end_page + 1):
        page_url = BASE_URL if i == 1 else f"{BASE_URL}?page={i}"
        links = get_links(driver, page_url)
        all_links.extend(links)

    for idx, link in enumerate(all_links, 1):
        # Pause si demandé
        while st.session_state['paused']:
            time.sleep(0.5)
        try:
            article = get_article_data(driver, link)
            data.append(article)
            st.info(f"Articles scrapés : {idx} / {len(all_links)}")
        except Exception as e:
            st.warning(f"Erreur avec {link}: {e}")

    driver.quit()
    return data


def main():
    n_pages = int(input("Combien de pages voulez-vous scraper ? "))
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    data = []
    all_links = []
    for i in range(1, n_pages + 1):
        if i == 1:
            page_url = BASE_URL
        else:
            page_url = f"{BASE_URL}?page={i}"
        links = get_links(driver, page_url)
        all_links.extend(links)
    for link in all_links:
        try:
            article = get_article_data(driver, link)
            data.append(article)
        except Exception as e:
            print(f"Erreur avec {link}: {e}")
    driver.quit()
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main() 