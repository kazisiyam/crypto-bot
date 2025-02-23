# CRYPTO_TRADING_BOT

## Overview
This project is a fully automated cryptocurrency trading bot designed to analyze market trends, scrape data from various sources, verify token security, and execute trades based on AI-driven predictions. The bot operates on the Solana and BNB blockchains and integrates multiple data sources for informed decision-making.

## **Disclaimer**
This repository is strictly **NOT for public use**. The project contains proprietary trading logic, API keys, and sensitive information that must not be shared. Unauthorized distribution or usage is prohibited.

## **Installation and Setup**
### **1. Create a Virtual Environment**
Navigate to the project directory and run:
```bash
python3 -m venv venv
```

### **2. Activate the Virtual Environment**
#### **Mac/Linux:**
```bash
source venv/bin/activate
```
#### **Windows (PowerShell):**
```powershell
venv\Scripts\Activate
```
#### **Windows (Command Prompt):**
```cmd
venv\Scripts\activate
```

### **3. Install Dependencies**
Run the following command to install all required Python packages:
```bash
pip install -r requirements.txt
```

## **File Structure**
```
CRYPTO_TRADING_BOT/
│── data/                     # Stores historical and live market data
│── environment/               # Handles AI training and testing environments
│── logs/                      # Stores log files for debugging
│── models/                    # AI models for trading predictions
│   ├── ai_analyzer.py         # AI analysis for token profitability
│   ├── q_learning.py          # Reinforcement learning model
│   ├── train_q_learning.py    # Training script for Q-learning model
│── scripts/                   # Scripts for various functions
│   ├── contract_verifier.py   # Checks token legitimacy using SolSniffer API
│   ├── data_collector.py      # Scrapes tokens from GMGN, Pump.fun, etc.
│   ├── login_bot.py           # Logs into the trading platform
│   ├── social_analyzer.py     # Analyzes social media presence
│   ├── trade_executor.py      # Executes trades based on AI predictions
│── utils/                     # Utility functions and helpers
│── main.py                    # Main script to run the trading bot
│── README.md                  # Project documentation
│── requirements.txt           # List of required Python packages
```

## **How It Works**
1. **Data Collection**: The bot scrapes new tokens from multiple sources (Pump.fun, GMGN, Dexscreener, Meteora, etc.).
2. **Social Media Analysis**: The bot checks X (formerly Twitter) for notable mentions and verifies account credibility.
3. **Token Verification**: The bot uses SolSniffer API to check contract security scores and detect rug pulls.
4. **AI Prediction**: The trained AI model predicts profitability based on historical and real-time data.
5. **Trade Execution**: If a token meets profitability criteria, the bot executes trades and monitors performance.
6. **Learning & Optimization**: The Q-learning model continuously improves trading strategies based on past performance.

## **Usage**
Run the bot by executing:
```bash
python main.py
```

## **Security Measures**
- API keys are stored securely in a configuration file (not included in this repository).
- The bot includes anti-rug and fake volume detection mechanisms.
- All trading actions are logged for review.

## **Important Notes**
- Ensure the bot runs in a **secure environment**.
- Do **not** expose API keys or trading strategies.
- This bot is **experimental** and should not be used with real funds without thorough testing.

## **License**
This project is proprietary. Unauthorized use, distribution, or reproduction is strictly prohibited.