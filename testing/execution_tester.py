import os
import sys
import logging
import time
import requests

# ✅ Ensure `scripts/` is recognized
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from scripts.login_bot import login_to_bullx

# ✅ Setup Logging
logging.basicConfig(filename=os.path.join(BASE_DIR, "logs/trade_executor.log"),
                    level=logging.INFO,
                    format="%(asctime)s - %(message)s")

# ✅ Example API Token (Replace with actual)
BULLX_API_KEY = "YOUR_BULLX_API_KEY"

def execute_trade(action, token, amount):
    """Executes a buy/sell trade on BullX"""
    url = f"https://bullx.io/api/trade"
    headers = {"Authorization": f"Bearer {BULLX_API_KEY}", "Content-Type": "application/json"}

    payload = {"action": action, "token": token, "amount": amount}
    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        logging.info(f"✅ {action.upper()} {amount} of {token} successfully.")
    else:
        logging.error(f"❌ Failed to {action} {token}. Response: {response.text}")

if __name__ == "__main__":
    logging.info("🚀 Running Trade Execution Tester...")

    # Ensure logged in before executing trades
    login_to_bullx()

    # Example trade execution
    execute_trade("buy", "PEPE", 0.01)
    time.sleep(2)
    execute_trade("sell", "PEPE", 0.02)

    logging.info("✅ All Trade Execution Complete!")