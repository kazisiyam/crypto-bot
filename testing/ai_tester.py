import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
import logging

# ✅ Setup Logging
logging.basicConfig(filename="logs/ai_analyzer.log", level=logging.INFO, format="%(asctime)s - %(message)s")

# Get absolute path of `historical_data.csv`
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data/historical_data.csv")

def load_data(file_path):
    """Loads historical data from CSV"""
    return pd.read_csv(file_path)

def prepare_data(df):
    """Prepares data for training"""
    features = ["price", "volume", "social_score", "contract_score"]
    X = df[features]
    y = df["is_profitable"]
    return train_test_split(X, y, test_size=0.2, random_state=42)

def train_model(X_train, y_train, model_path = "testing/models/model.pkl"):
    """Trains the RandomForest Model"""
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    joblib.dump(model, model_path)
    logging.info("✅ AI Model trained and saved.")
    return model

def evaluate_model(model, X_test, y_test):
    """Evaluates model accuracy"""
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    logging.info(f"✅ Model Accuracy: {accuracy}")
    return accuracy

def predict(model_path, new_data):
    """Predicts profitability of a new token"""
    model = joblib.load(model_path)
    return model.predict(new_data)

if __name__ == "__main__":
    logging.info("🚀 AI Model Training Started...")
    df = load_data(DATA_PATH)
    X_train, X_test, y_train, y_test = prepare_data(df)
    model = train_model(X_train, y_train)
    evaluate_model(model, X_test, y_test)

    # Example prediction
    new_coin = pd.DataFrame({"price": [10.0], "volume": [1000000], "social_score": [90], "contract_score": [95]})
    prediction = predict("testing/models/model.pkl", new_coin)

    print(f"Prediction for new coin: {'Profitable' if prediction[0] else 'Not Profitable'}")
    logging.info("✅ AI Prediction Completed.")