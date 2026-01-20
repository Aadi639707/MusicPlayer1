import asyncio
import os
import sys
from threading import Thread
from flask import Flask
from pyrogram import Client

# --- WEB SERVER FOR RENDER ---
web_app = Flask(__name__)
@web_app.route('/')
def home(): return "Bot is Online!"

def run_web():
    web_app.run(host='0.0.0.0', port=10000)

# --- CONFIGURATION ---
API_ID = int(os.environ.get("API_ID", 32348580))
API_HASH = os.environ.get("API_HASH", "ec7420fcd7ee27712fc8ed7334d7bc3e")
SESSION = os.environ.get("SESSION")

if not SESSION:
    print("ERROR: SESSION variable missing!")
    sys.exit(1)

app = Client(
    name="MusicPlayer",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=SESSION,
    plugins=dict(root="plugins"),
    in_memory=True # Resolves database/peer issues on Render
)

async def start_bot():
    print(">> Starting Server...")
    Thread(target=run_web, daemon=True).start()
    await app.start()
    print(">> BOT IS LIVE!")
    await asyncio.Event().wait()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_bot())
    
