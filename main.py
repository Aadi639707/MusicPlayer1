import asyncio
import os
from pyrogram import Client, filters
from flask import Flask
from threading import Thread

# --- RENDER WEB SERVER (Fixes Port Scan Timeout) ---
web_app = Flask('')

@web_app.route('/')
def home():
    return "Bot is Running 24/7!"

def run_web():
    # Render free tier hamesha port 10000 dhoondta hai
    web_app.run(host='0.0.0.0', port=10000)

def keep_alive():
    t = Thread(target=run_web)
    t.daemon = True
    t.start()

# --- BOT CONFIGURATION ---
API_ID = 32348580
API_HASH = "ec7420fcd7ee27712fc8ed7334d7bc3e"
SESSION = "BQHtmaQAuwrsgGW5ZQEDE47TCrF6rWYJz-DozY0LNhSEYFg6uLMzBeV2L-otqHkuG6H9m-ZbONzHKpzidL6FKaKkq8vrhYVZYra635OKzeJ8RZrtnLpxcV_UXOIqSjvQ50Tqip1qUDK0A9jCDHcDcvdj0G6PLWIPfQrB2pq9d6EPryhtG6pG4uzECSGHiFSwmNYpGHgQNcf0S6lgvA0EeAAgJca9y2aTHFJcJyuv-GUfIcmdoF0qwtcFUgfHYu60cXS_HIhpHx75AYwsQ4H3geOjuT9ZfjgjQbwUFC74dUve51iJ8DMq_WZ_CxaQxYLh6IME7tdS-f4Avdyr0JHn8YwEsF5MnAAAAABxzmw7AA"

app = Client(
    name="MusicPlayer",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=SESSION,
    plugins=dict(root="plugins") # Ye aapke plugins folder se commands uthayega
)

# --- REACTION PROTECTION ---
@app.on_edited_message(filters.group & ~filters.me)
async def delete_edited_handler(client, message):
    if not message.text and not message.caption:
        return
    
    SUDOERS = [7876183821]
    if message.from_user and message.from_user.id in SUDOERS:
        return

    try:
        await message.delete()
    except:
        pass

async def start_bot():
    print(">> Starting Web Server...")
    keep_alive()
    
    print(">> Starting Userbot...")
    try:
        await app.start()
        print(">> BOT IS LIVE!")
    except Exception as e:
        print(f"Startup Error: {e}")
        return
    
    await asyncio.Event().wait()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_bot())
    
