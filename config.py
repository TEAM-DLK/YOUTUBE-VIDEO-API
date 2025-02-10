import os
from dotenv import load_dotenv

# Load environment variables from a .env file if running locally
load_dotenv()

class Config:
    # General settings
    API_ID = os.getenv('API_ID')  # Telegram API ID
    API_HASH = os.getenv('API_HASH')  # Telegram API Hash
    BOT_TOKEN = os.getenv('BOT_TOKEN')  # Telegram Bot Token
    CHANNEL_USERNAME = os.getenv('CHANNEL_USERNAME')  # Channel username (without @)
    COOKIES_PATH = os.getenv('COOKIES_PATH', 'cookies/cookies.txt')  # Path to cookies file