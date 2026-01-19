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

# --- WEB SERVER FOR RENDER ---
web_app = Flask(__name__)

@web_app.route('/')
def home():
    return "Bot is Running with Environment Variables!"

def run_web():
    web_app.run(host='0.0.0.0', port=10000)

# --- CONFIGURATION (Fetching from Render Environment) ---
# Agar Render pe variable nahi milega toh ye default value uthayega
API_ID = int(os.environ.get("API_ID", 32348580))
API_HASH = os.environ.get("API_HASH", "ec7420fcd7ee27712fc8ed7334d7bc3e")
SESSION = os.environ.get("SESSION") 
SUDOERS = [7876183821]

from pyrogram import Client, filters

# Session check logic
if not SESSION:
    print(">> [ERROR] SESSION variable nahi mila! Render dashboard check karein.")
    sys.exit(1)

app = Client(
    name="MusicPlayer",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=SESSION,
    plugins=dict(root="plugins")
)

# --- STARTUP LOGIC ---
async def start_services():
    print(">> Starting Web Server...")
    Thread(target=run_web, daemon=True).start()
    
    print(">> Starting Userbot Engine...")
    try:
        await app.start()
        print(f">> [SUCCESS] Bot Live with Session!")
    except Exception as e:
        print(f">> [ERROR] Startup failed: {e}")
        return
    
    await asyncio.Event().wait()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_services())
    
