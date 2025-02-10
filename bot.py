from pyrogram import Client, filters
from pytube import YouTube
import os
from config import API_ID, API_HASH, BOT_TOKEN, COOKIES_PATH, CHANNEL_USERNAME

# Initialize Pyrogram bot
bot = Client("yt_downloader", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@bot.on_message(filters.command("start"))
def start(client, message):
    user = message.from_user.id

@bot.on_message(filters.text & filters.private)
def download_video(client, message):
    user = message.from_user.id
    
    url = message.text
    try:
        yt = YouTube(url, use_oauth=False, allow_oauth_cache=True)

        # Load cookies
        with open(COOKIES_PATH, "r", encoding="utf-8") as f:
            cookies = f.read()
        yt.cookies.load_from_str(cookies)

        # Download video
        video = yt.streams.get_highest_resolution()
        file_path = video.download()

        # Send video
        message.reply_video(video=open(file_path, "rb"), caption=f"Downloaded: {yt.title}")
        os.remove(file_path)

    except Exception as e:
        message.reply_text(f"Error: {e}")

bot.run()