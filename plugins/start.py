from pyrogram import Client, filters

@Client.on_message(filters.command("start") & (filters.private | filters.group))
async def start_command(client, message):
    try:
        await message.reply_text(
            "Hi! I am your Music Player Bot.\n"
            "Status: **Online and English Integrated** ✅\n\n"
            "Try /ping to test my speed."
        )
    except Exception as e:
        print(f"Error in start command: {e}")

@Client.on_message(filters.command("ping") & (filters.private | filters.group))
async def ping_command(client, message):
    await message.reply_text("🏓 **Pong!** I am responding fast.")
    
