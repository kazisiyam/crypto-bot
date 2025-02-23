import logging
import time
import requests
from scripts.login_bot import login_to_bullx

# ✅ Setup Logging
logging.basicConfig(filename="logs/trade_executor.log", level=logging.INFO, format="%(asctime)s - %(message)s")

BULLX_API_KEY = "YOUR_BULLX_API_KEY"

def execute_trade(action, token, amount, slippage=15):
    """Executes a trade on BullX with priority fee & slippage."""
    url = f"https://bullx.io/api/trade"
    headers = {"Authorization": f"Bearer {BULLX_API_KEY}", "Content-Type": "application/json"}

    payload = {"action": action, "token": token, "amount": amount, "slippage": slippage}
    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        logging.info(f"✅ {action.upper()} {amount} of {token} successfully.")
    else:
        logging.error(f"❌ Failed to {action} {token}. Response: {response.text}")

def auto_trade():
    """Finds profitable tokens and executes trades."""
    login_to_bullx()
    tokens = ["PEPE", "BONK"]  # Placeholder for AI-selected tokens

    for token in tokens:
        execute_trade("buy", token, 1)
        time.sleep(2)
        execute_trade("sell", token, 0.85)

if __name__ == "__main__":
    auto_trade()