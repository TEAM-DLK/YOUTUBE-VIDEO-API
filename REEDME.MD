# YouTube Video API

A simple API to download YouTube videos and extract video information, built with Python and FastAPI.

## Features

- Download YouTube videos by URL.
- Extract video metadata (e.g., title, duration, etc.).
- Fast and easy to use with the FastAPI framework.

## Deployment

This project can be deployed on Heroku with ease using the "Deploy to Heroku" button below.

### **Deploy to Heroku**

To deploy this app to Heroku, click the button below:

[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/TEAM-DLK/YOUTUBE-VIDEO-API)

### **Manual Deployment (Alternative)**

If you prefer to deploy manually, follow these steps:

1. Fork or clone this repository.

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Create a new **Heroku** app:

    ```bash
    heroku create
    ```

4. Push the code to Heroku:

    ```bash
    git push heroku master
    ```

5. Open the app in your browser:

    ```bash
    heroku open
    ```

## Environment Variables

Before deploying, ensure you have set the following environment variables in your Heroku settings (or local environment) to configure the API:

- **API_ID**: Your Telegram API ID (required for using Telegram Bot API).
- **API_HASH**: Your Telegram API Hash (required for using Telegram Bot API).
- **BOT_TOKEN**: The token for your Telegram bot.
- **CHANNEL_USERNAME**: Your Telegram Channel username (without @).
- **COOKIES_PATH**: Path to the `cookies.txt` file for YouTube video download functionality (if applicable).

To set these variables in **Heroku**, you can use the Heroku Dashboard or the CLI:

```bash
heroku config:set API_ID=your_api_id API_HASH=your_api_hash BOT_TOKEN=your_bot_token CHANNEL_USERNAME=your_channel_username COOKIES_PATH=cookies.txt
