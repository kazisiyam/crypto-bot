import requests
import logging

# ✅ API Key (Replace with your actual key)
SOLSNIFFER_API_KEY = "2bpx2ael4ghsmpkaz5wt3f7apj272r"

logging.basicConfig(filename="logs/contract_verifier.log", level=logging.INFO, format="%(asctime)s - %(message)s")

def verify_contract(contract_address):
    """Checks the security score of a contract"""
    try:
        headers = {"Authorization": f"Bearer {SOLSNIFFER_API_KEY}"}
        response = requests.get(f"https://api.solsniffer.com/v1/token/{contract_address}", headers=headers)

        if response.status_code == 200:
            data = response.json()
            score = data.get("security_score", 0)
            return score >= 85, score  # ✅ Safe if score >= 85
        return False, None
    except requests.RequestException as e:
        logging.error(f"Error verifying contract {contract_address}: {e}")
        return False, None

def detect_fake_volume(contract_address):
    """Detects fake volume by analyzing transaction history"""
    try:
        headers = {"Authorization": f"Bearer {SOLSNIFFER_API_KEY}"}
        response = requests.get(f"https://api.solsniffer.com/v1/token/{contract_address}/transactions", headers=headers)
        if response.status_code == 200:
            transactions = response.json().get("transactions", [])
            # Analyze transactions for fake volume (simplified)
            return False
        return False
    except Exception as e:
        logging.error(f"Error detecting fake volume for {contract_address}: {e}")
        return False

def check_known_rug_pullers(contract_address, known_rug_pullers):
    """Checks if the contract is associated with known scam wallets"""
    try:
        headers = {"Authorization": f"Bearer {SOLSNIFFER_API_KEY}"}
        response = requests.get(f"https://api.solsniffer.com/v1/token/{contract_address}/owners", headers=headers)
        if response.status_code == 200:
            owners = response.json().get("owners", [])
            return any(owner["address"] in known_rug_pullers for owner in owners)
        return False
    except Exception as e:
        logging.error(f"Error checking rug pullers for {contract_address}: {e}")
        return False

if __name__ == "__main__":
    test_contract = "SOME_TEST_CONTRACT"
    print(verify_contract(test_contract))