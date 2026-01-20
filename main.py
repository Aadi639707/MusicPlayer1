import asyncio
import os
import sys
from threading import Thread
from flask import Flask
from pyrogram import Client

# --- WEB SERVER FOR RENDER ---
web_app = Flask(__name__)
@web_app.route('/')
def home(): return "Music Bot is Active!"

def run_web():
    web_app.run(host='0.0.0.0', port=10000)

# --- FETCHING YOUR RENDER VARIABLES ---
API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
SESSION = os.environ.get("SESSION")
BOT_TOKEN = os.environ.get("BOT_TOKEN") # Added from your screenshot

# Extra Configs from your Vars
SUDOERS = [int(i) for i in os.environ.get("SUDOERS", "7876183821").split()]
PREFIX = os.environ.get("PREFIX", "/")

app = Client(
    name="MusicPlayer",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=SESSION,
    bot_token=BOT_TOKEN, # Using both for faster resolving
    plugins=dict(root="plugins"),
    in_memory=True 
)

async def start_bot():
    print(">> Starting Web Server...")
    Thread(target=run_web, daemon=True).start()
    
    print(">> Logging in Userbot...")
    await app.start()
    
    # Auto-resolve peer issues
    print(">> Resolving database...")
    await app.get_me() 
    
    loaded = len(app.plugins) if app.plugins else 0
    print(f">> [SUCCESS] {loaded} Plugins Loaded!")
    print(f">> Bot is now live with Prefix: {PREFIX}")
    
    await asyncio.Event().wait()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_bot())
    
