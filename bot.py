import os
import logging
from dotenv import load_dotenv
from pyrogram import Client, filters
from pytube import YouTube
from flask import Flask

# Load environment variables
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")

# Flask app for monitoring
app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running!"

# Initialize Pyrogram bot
bot = Client("yt_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Load cookies from file
def load_cookies(cookie_path="cookies/cookies.txt"):
    try:
        with open(cookie_path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        logging.warning("Cookies file not found. Proceeding without cookies.")
        return None

# YouTube download function
def download_youtube_video(url, cookies_path="cookies/cookies.txt"):
    cookies = load_cookies(cookies_path)
    try:
        yt = YouTube(url, cookies=cookies) if cookies else YouTube(url)
        stream = yt.streams.get_highest_resolution()
        file_path = stream.download()
        return file_path
    except Exception as e:
        logging.error(f"Error downloading video: {e}")
        return None

# Telegram command handler
@bot.on_message(filters.command("download"))
def handle_download(client, message):
    if len(message.command) < 2:
        message.reply_text("Usage: `/download <YouTube URL>`")
        return
    
    url = message.command[1]
    message.reply_text("Downloading video, please wait...")

    file_path = download_youtube_video(url)
    
    if file_path:
        message.reply_video(video=file_path, caption="Here is your video!")
        os.remove(file_path)  # Cleanup
    else:
        message.reply_text("Failed to download the video.")

# Start bot and web server
if __name__ == "__main__":
    from threading import Thread
    Thread(target=lambda: app.run(host="0.0.0.0", port=8080)).start()
    bot.run()