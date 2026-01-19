from pyrogram import Client, filters

# Welcome Command
@Client.on_message(filters.command("start") & (filters.private | filters.group))
async def start_handler(client, message):
    await message.reply_text(
        "✨ **Welcome to Music Player!**\n\n"
        "I am working perfectly in English now. "
        "Use /ping to check my speed!"
    )

# Speed Test Command
@Client.on_message(filters.command("ping") & (filters.private | filters.group))
async def ping_handler(client, message):
    await message.reply_text("🏓 **Pong!** Bot is fast and active.")
    
