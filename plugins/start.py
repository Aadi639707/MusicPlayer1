from pyrogram import Client, filters

# Start Command
@Client.on_message(filters.command("start") & (filters.private | filters.group))
async def start_handler(client, message):
    try:
        await message.reply_text(
            "✨ **Music Bot is Ready!**\n\n"
            "I am running on Render Web Service.\n"
            "Use /ping to check response time."
        )
    except Exception as e:
        print(f"Error in start command: {e}")

# Ping Command
@Client.on_message(filters.command("ping") & (filters.private | filters.group))
async def ping_handler(client, message):
    await message.reply_text("🏓 **Pong!** I am responding fast.")
    
