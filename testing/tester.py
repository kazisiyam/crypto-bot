import os
import sys
import logging

# Get the absolute path of the `testing/` directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR)  # Go up one level
sys.path.append(ROOT_DIR)  # Add root directory to Python path

# Setup logging
logging.basicConfig(filename=os.path.join(ROOT_DIR, "logs/tester.log"),
                    level=logging.INFO,
                    format="%(asctime)s - %(message)s")

# ✅ Run AI Model Tester
logging.info("🚀 Running AI Tester...")
exec(open(os.path.join(BASE_DIR, "ai_tester.py")).read())

# ✅ Run Trade Execution Tester
logging.info("🚀 Running Trade Execution Tester...")
exec(open(os.path.join(BASE_DIR, "execution_tester.py")).read())

print("✅ All tests completed successfully.")