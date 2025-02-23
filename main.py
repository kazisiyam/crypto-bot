import logging
import pandas as pd
from scripts.data_collector import scrape_pump_fun, scrape_gmgn, scrape_meteora, scrape_dexscreener
from scripts.social_analyzer import analyze_social_media
from scripts.contract_verifier import verify_contract, detect_fake_volume, check_known_rug_pullers
from models.ai_analyzer import predict
from scripts.trade_executor import execute_trade
from scripts.login_bot import login_to_bullx

# ✅ Setup Logging
logging.basicConfig(filename="logs/main.log", level=logging.INFO, format="%(asctime)s - %(message)s")

def main():
    logging.info("🚀 Bot Started")

    # ✅ Log into BullX
    login_to_bullx()

    # ✅ Scrape Data
    logging.info("🔍 Scraping tokens...")
    all_data = []
    for scraper in [scrape_pump_fun, scrape_gmgn, scrape_meteora, scrape_dexscreener]:
        scraped_data = scraper()
        if not scraped_data:
            logging.warning(f"⚠️ {scraper.__name__} returned no data.")
        all_data.extend(scraped_data)

    # ✅ Create DataFrame
    if not all_data:
        logging.error("❌ No data collected. Exiting bot.")
        return

    df = pd.DataFrame(all_data)

    # ✅ Ensure 'name' Column Exists
    if 'name' not in df.columns:
        logging.error("❌ Missing 'name' column in DataFrame. Exiting.")
        print("ERROR: 'name' column not found in DataFrame. Fix scraper.")
        return

    # ✅ Social Media Analysis
    logging.info("🔍 Analyzing social media trust levels...")
    df['social_score'] = df['name'].apply(lambda x: analyze_social_media(x).get('trust_score', 0))

    # ✅ Contract Verification
    logging.info("🔍 Verifying contracts...")
    df['contract_score'] = df['contract_address'].apply(lambda x: verify_contract(x)[1] if x else 0)
    df = df[df['contract_score'] >= 85]  # Filter safe tokens

    # ✅ Fake Volume & Rug Pull Detection
    df['fake_volume'] = df['contract_address'].apply(detect_fake_volume)
    df['is_rug_pull'] = df['contract_address'].apply(lambda x: check_known_rug_pullers(x, ['known_rug_puller_address']))
    df = df[(df['fake_volume'] == False) & (df['is_rug_pull'] == False)]

    # ✅ AI Profitability Prediction
    logging.info("🤖 Running AI Analysis...")
    features = ['price', 'volume', 'social_score', 'contract_score']
    if not all(f in df.columns for f in features):
        logging.error("❌ Missing required features for AI prediction.")
        return

    new_data = df[features]
    predictions = predict('models/model.pkl', new_data)
    df['predicted_profitability'] = predictions

    # ✅ Display Results
    profitable_tokens = df[df['predicted_profitability'] == True]['name'].tolist()
    logging.info(f"💰 Profitable Tokens: {profitable_tokens}")
    print(f"💰 Profitable Tokens: {profitable_tokens}")

if __name__ == "__main__":
    main()