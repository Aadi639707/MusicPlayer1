from pyrogram import Client, filters
import os

# Fetching prefix from Render variables
P = os.environ.get("PREFIX", "/")

@Client.on_message(filters.command("start", prefixes=P))
async def start_handler(client, message):
    await message.reply_text(
        f"👋 **Hello! I am Online.**\n\n"
        f"**Owner ID:** `{os.environ.get('OWNER_ID')}`\n"
        f"**Prefix:** `{P}`\n"
        "Send /ping to test speed!"
    )

@Client.on_message(filters.command("ping", prefixes=P))
async def ping_handler(client, message):
    await message.reply_text("🏓 **Pong!** Userbot is working perfectly.")
    
