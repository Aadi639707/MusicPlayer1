import asyncio
import os
import sys
import subprocess
from threading import Thread

# --- FAST FLASK AUTO-INSTALLER ---
try:
    from flask import Flask
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "flask"])
    from flask import Flask

# --- WEB SERVER FOR RENDER (Fast Response) ---
web_app = Flask(__name__)

@web_app.route('/')
def home():
    return "Bot is Running Fast & Stable!"

def run_web():
    # Render hamesha port 10000 dhoondta hai
    web_app.run(host='0.0.0.0', port=10000)

# --- BOT CONFIGURATION ---
API_ID = 32348580
API_HASH = "ec7420fcd7ee27712fc8ed7334d7bc3e"
SESSION = "BQHtmaQAuwrsgGW5ZQEDE47TCrF6rWYJz-DozY0LNhSEYFg6uLMzBeV2L-otqHkuG6H9m-ZbONzHKpzidL6FKaKkq8vrhYVZYra635OKzeJ8RZrtnLpxcV_UXOIqSjv (Aapki Puri Session String)"
SUDOERS = [7876183821] # Aapki ID

from pyrogram import Client, filters

app = Client(
    name="MusicPlayer",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=SESSION,
    plugins=dict(root="plugins") # Aapke saare commands yahan se load honge
)

# --- REACTION & EDIT PROTECTION ---
@app.on_edited_message(filters.group & ~filters.me)
async def delete_edited_handler(client, message):
    if message.from_user and message.from_user.id in SUDOERS:
        return
    try:
        await message.delete()
    except:
        pass

# --- STARTUP LOGIC ---
async def start_services():
    print(">> Starting Web Server...")
    Thread(target=run_web, daemon=True).start()
    
    print(">> Starting Userbot Engine...")
    try:
        await app.start()
        # Kitne plugins load hue check karne ke liye:
        print(f">> [SUCCESS] {len(app.plugins) if app.plugins else 0} Plugins Loaded!")
        print(">> BOT IS LIVE AND FAST!")
    except Exception as e:
        print(f">> [ERROR] Startup failed: {e}")
        return
    
    await asyncio.Event().wait()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_services())
    
