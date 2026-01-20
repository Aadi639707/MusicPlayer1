from pyrogram import Client, filters

@Client.on_message(filters.command("start") & (filters.private | filters.group))
async def start_handler(client, message):
    try:
        await message.reply_text(
            "✨ **Bot is Online!**\n\n"
            "Status: Active ✅\n"
            "I am ready to take commands."
        )
    except Exception as e:
        print(f"Error: {e}")

@Client.on_message(filters.command("ping") & (filters.private | filters.group))
async def ping_handler(client, message):
    await message.reply_text("🏓 **Pong!** Bot speed is excellent.")
    
