import time
import logging
import pandas as pd
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from scripts.contract_verifier import verify_contract

# ✅ Setup Logging
logging.basicConfig(filename="logs/pumpfun_scraper.log", level=logging.INFO, format="%(asctime)s - %(message)s")

# ✅ Use Your Personal Chrome Profile
chrome_options = Options()
chrome_options.add_argument("user-data-dir=/Users/kazi/Library/Application Support/Google/Chrome")
chrome_options.add_argument("profile-directory=Profile 2")  # Make sure this matches your actual profile
chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # Reduce bot detection

# ✅ Start Chrome
driver = uc.Chrome(options=chrome_options)

def open_pump_fun():
    """Opens Pump.fun and loads trending tokens"""
    logging.info("🚀 Opening Pump.fun")
    driver.get("https://pump.fun/board")
    time.sleep(5)  # Wait for page to load

    # Scroll down to load more tokens
    for _ in range(3):
        driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
        time.sleep(3)

def scrape_tokens():
    """Extracts token names & contract addresses"""
    logging.info("🔍 Scraping Pump.fun tokens...")
    tokens = []
    
    # Find all token elements on Pump.fun
    token_elements = driver.find_elements(By.CSS_SELECTOR, ".TokenCardstyles__Container-sc-1mptby1-0")

    for token in token_elements:
        try:
            name = token.find_element(By.CSS_SELECTOR, ".TokenCardstyles__Name-sc-1mptby1-1").text
            contract_address = token.find_element(By.CSS_SELECTOR, ".TokenCardstyles__Address-sc-1mptby1-2").text
            
            tokens.append({"name": name, "contract_address": contract_address})
        except Exception as e:
            logging.error(f"❌ Error scraping token: {e}")
    
    logging.info(f"✅ Found {len(tokens)} tokens.")
    return tokens

def verify_tokens(tokens):
    """Filters out bad tokens using contract_verifier.py"""
    verified_tokens = []

    for token in tokens:
        is_safe, score = verify_contract(token["contract_address"])
        
        if is_safe:
            logging.info(f"✅ {token['name']} passed with a score of {score}")
            verified_tokens.append(token)
        else:
            logging.warning(f"❌ {token['name']} failed with a score of {score}")

    return verified_tokens

def save_to_csv(tokens):
    """Saves verified tokens to a CSV file"""
    df = pd.DataFrame(tokens)
    df.to_csv("data/verified_tokens.csv", index=False)
    logging.info(f"📂 Saved {len(tokens)} verified tokens to CSV.")

if __name__ == "__main__":
    open_pump_fun()
    raw_tokens = scrape_tokens()
    good_tokens = verify_tokens(raw_tokens)
    save_to_csv(good_tokens)
    driver.quit()
    logging.info("✅ Pump.fun scraping complete!")