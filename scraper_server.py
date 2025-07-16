from flask import Flask, request, jsonify
import threading
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import json

app = Flask(__name__)
scraping_state = {
    "paused": False,
    "stopped": False,
    "progress": 0,
    "total": 0,
    "start_page": 1,
    "end_page": 1
}

def get_links(driver, page_url):
    driver.get(page_url)
    time.sleep(2)
    links = [a.get_attribute('href') for a in driver.find_elements(By.CSS_SELECTOR, ".product-title > a")]
    return links

def get_article_data(driver, url):
    driver.get(url)
    time.sleep(1)
    try:
        titre = driver.find_element(By.CSS_SELECTOR, "h1.h1").text.strip()
    except:
        titre = "Titre introuvable"
    print(f"Scraped: {titre} - {url}")
    return {"titre": titre, "url": url}

def scraper(start_page, end_page):
    print(f"==> Scraper started from {start_page} to {end_page}")
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    data = []
    all_links = []
    for i in range(start_page, end_page + 1):
        page_url = f"ton site?page={i}" if i > 1 else "ton site"
        links = get_links(driver, page_url)
        all_links.extend(links)
    scraping_state["total"] = len(all_links)
    for idx, link in enumerate(all_links, 1):
        while scraping_state["paused"]:
            time.sleep(0.5)
        if scraping_state["stopped"]:
            break
        article = get_article_data(driver, link)
        data.append(article)
        scraping_state["progress"] = idx
    driver.quit()
    with open("resultats.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    return data

@app.route("/start", methods=["POST"])
def start():
    body = request.get_json()
    start_page = int(body.get("start_page", 1))
    end_page = int(body.get("end_page", 1))
    scraping_state["paused"] = False
    scraping_state["stopped"] = False
    scraping_state["progress"] = 0
    scraping_state["start_page"] = start_page
    scraping_state["end_page"] = end_page
    threading.Thread(target=scraper, args=(start_page, end_page)).start()
    return jsonify({"status": "started"})

@app.route("/pause", methods=["POST"])
def pause():
    scraping_state["paused"] = True
    return jsonify({"status": "paused"})

@app.route("/resume", methods=["POST"])
def resume():
    scraping_state["paused"] = False
    return jsonify({"status": "resumed"})

@app.route("/status", methods=["GET"])
def status():
    return jsonify(scraping_state)

@app.route("/stop", methods=["POST"])
def stop():
    scraping_state["stopped"] = True
    return jsonify({"status": "stopped"})

if __name__ == "__main__":
    app.run(port=5001)
