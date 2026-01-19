from pyrogram import Client, filters

@Client.on_message(filters.command("start") & (filters.private | filters.group))
async def start_command(client, message):
    await message.reply_text(
        "✨ **Music Player is Online!**\n\n"
        "I am now running on the upgraded engine. "
        "Type /ping to check my response time."
    )

@Client.on_message(filters.command("ping") & (filters.private | filters.group))
async def ping_command(client, message):
    await message.reply_text("🏓 **Pong!** The bot is responding fast.")
    
