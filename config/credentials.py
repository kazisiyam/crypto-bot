import random

# ✅ List of Proxies
PROXY_LIST = [
    {"host": "proxy1.example.com", "port": 8080, "username": "user1", "password": "pass1"},
    {"host": "proxy2.example.com", "port": 8080, "username": "user2", "password": "pass2"},
]

# ✅ Function to rotate proxies
def get_proxy_with_rotation():
    proxy = random.choice(PROXY_LIST)
    return {
        "http": f"http://{proxy['username']}:{proxy['password']}@{proxy['host']}:{proxy['port']}",
        "https": f"http://{proxy['username']}:{proxy['password']}@{proxy['host']}:{proxy['port']}",
    }

# ✅ Random User-Agent Generator
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36",
]

def get_random_user_agent():
    return random.choice(USER_AGENTS)