import time
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# ✅ Path to Your Personal Chrome Profile
CHROME_USER_DATA_DIR = "/Users/kazi/Library/Application Support/Google/Chrome"
CHROME_PROFILE = "Profile 2"  # ✅ Ensure this matches your personal profile name

def login_to_bullx():
    """Logs into BullX using the saved Chrome profile to retain sessions."""
    logging.info("🔐 Logging into BullX...")

    chrome_options = Options()
    chrome_options.add_argument(f"user-data-dir={CHROME_USER_DATA_DIR}")
    chrome_options.add_argument(f"profile-directory={CHROME_PROFILE}")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # Stealth mode

    # ✅ Initialize WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # ✅ Open BullX Login Page
    driver.get("https://bullx.io/pump-vision")
    time.sleep(10)  # Wait for the login page to load

    # ✅ Manually Enter OTP if Required
    #input("📩 Enter OTP in BullX and press [ENTER] to continue...")

    logging.info("✅ BullX Login Successful!")
    return driver  # Return driver for further use

def login_to_telegram():
    """Logs into Telegram Web using the saved Chrome profile."""
    logging.info("🔐 Logging into Telegram Web...")

    chrome_options = Options()
    chrome_options.add_argument(f"user-data-dir={CHROME_USER_DATA_DIR}")
    chrome_options.add_argument(f"profile-directory={CHROME_PROFILE}")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")

    # ✅ Initialize WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # ✅ Open Telegram Web Login
   # driver.get("https://web.telegram.org/k/")
    #time.sleep(10)  # Allow time for QR code scan

    #logging.info("📩 Scan the QR Code with Telegram App & Press [ENTER] to Continue...")
    #input("➡️ Press [ENTER] after logging in...")

    logging.info("✅ Telegram Login Successful!")
    return driver  # Return driver for further use

if __name__ == "__main__":
    driver = login_to_bullx()
    driver = login_to_telegram()