import asyncio
import os
import sys
from threading import Thread
from flask import Flask
from pyrogram import Client, filters

# --- WEB SERVER FOR RENDER ---
web_app = Flask(__name__)

@web_app.route('/')
def home():
    return "Bot Engine is Running!"

def run_web():
    # Render uses port 10000 by default
    web_app.run(host='0.0.0.0', port=10000)

# --- CONFIGURATION ---
API_ID = int(os.environ.get("API_ID", 32348580))
API_HASH = os.environ.get("API_HASH", "ec7420fcd7ee27712fc8ed7334d7bc3e")
SESSION = os.environ.get("SESSION")
SUDOERS = [7876183821]

if not SESSION:
    print("CRITICAL ERROR: SESSION string is missing in Environment Variables!")
    sys.exit(1)

app = Client(
    name="MusicPlayer",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=SESSION,
    plugins=dict(root="plugins")
)

async def start_bot():
    print("Starting Web Server...")
    Thread(target=run_web, daemon=True).start()
    
    print("Starting Userbot...")
    await app.start()
    
    # Check if plugins are loaded correctly
    loaded_plugins = len(app.plugins) if app.plugins else 0
    print(f"Successfully loaded {loaded_plugins} plugins.")
    print("BOT IS NOW ONLINE!")
    
    await asyncio.Event().wait()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_bot())
    
