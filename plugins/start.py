from pyrogram import Client, filters

@Client.on_message(filters.command("start") & filters.private)
async def start_cmd(client, message):
    await message.reply_text("Hello! Main Zinda hoon aur kaam kar raha hoon.")
  
