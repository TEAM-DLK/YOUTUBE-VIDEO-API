import os
from dotenv import load_dotenv

# Load environment variables from .env file if running locally
load_dotenv()

# Expose environment variables directly
API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')
BOT_TOKEN = os.getenv('BOT_TOKEN')
CHANNEL_USERNAME = os.getenv('CHANNEL_USERNAME')
COOKIES_PATH = os.getenv('COOKIES_PATH', 'cookies.txt')