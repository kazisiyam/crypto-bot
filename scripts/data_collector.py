import time
import random
import logging
import requests
import undetected_chromedriver as uc
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.credentials import get_proxy_with_rotation, get_random_user_agent
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from config.credentials import get_proxy_with_rotation, get_random_user_agent

# ✅ Setup Logging
logging.basicConfig(filename="logs/scraper.log", level=logging.INFO, format="%(asctime)s - %(message)s")

def get_stealth_driver():
    """Initializes stealth ChromeDriver to avoid detection."""
    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-infobars")
    options.add_argument(f"user-agent={get_random_user_agent()}")

    proxy = get_proxy_with_rotation()
    options.add_argument(f"--proxy-server={proxy['http']}")

    driver = uc.Chrome(options=options)
    return driver

def solve_captcha(driver):
    """Detects and waits for manual CAPTCHA solving."""
    try:
        captcha_box = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "g-recaptcha"))
        )
        logging.warning("⚠️ CAPTCHA detected. Solve manually.")
        input("🔴 Press Enter after solving CAPTCHA...")
    except:
        logging.info("✅ No CAPTCHA detected.")

def browse_naturally(driver, url):
    """Opens URL and scrolls naturally to mimic human behavior."""
    driver.get(url)
    time.sleep(random.uniform(5, 10))
    for _ in range(3):
        driver.execute_script("window.scrollBy(0, 300);")
        time.sleep(random.uniform(2, 5))
    return driver.page_source

def scrape_pump_fun():
    """Scrapes trending coins from Pump.fun."""
    logging.info("🔍 Scraping Pump.fun...")
    driver = get_stealth_driver()
    html = browse_naturally(driver, "https://pump.fun/board")
    solve_captcha(driver)

    soup = BeautifulSoup(html, "html.parser")
    coins = soup.find_all("div", class_="coin-item")
    data = []
    
    for coin in coins:
        try:
            name = coin.find("h2", class_="coin-name").text
            price = float(coin.find("span", class_="coin-price").text.replace("$", "").strip())
            data.append({"name": name, "price": price})
        except Exception as e:
            logging.error(f"Error parsing Pump.fun coin: {e}")

    driver.quit()
    logging.info(f"✅ Scraped {len(data)} tokens from Pump.fun")
    return data

def scrape_dexscreener():
    """Scrapes DexScreener for trending tokens."""
    logging.info("🔍 Scraping DexScreener...")
    driver = get_stealth_driver()
    html = browse_naturally(driver, "https://dexscreener.com")
    solve_captcha(driver)

    soup = BeautifulSoup(html, "html.parser")
    tokens = soup.find_all("div", class_="token-entry")
    data = []

    for token in tokens:
        try:
            name = token.find("div", class_="token-name").text
            price = token.find("div", class_="token-price").text
            volume = token.find("div", class_="token-volume").text
            data.append({"name": name, "price": price, "volume": volume})
        except Exception as e:
            logging.error(f"Error parsing DexScreener token: {e}")

    driver.quit()
    logging.info(f"✅ Scraped {len(data)} tokens from DexScreener")
    return data

if __name__ == "__main__":
    scrape_pump_fun()
    scrape_dexscreener()