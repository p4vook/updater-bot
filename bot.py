import config
from telethon import TelegramClient, events

bot = TelegramClient('updater_bot', config.API_ID, config.API_HASH).start(bot_token=config.BOT_TOKEN)

@bot.on(events.MessageEdited(chats=[config.FROM_CHAT_ID]))
async def handler(event):
    if event.id == config.FROM_MESSAGE_ID:
        print(f"Updating message, changed at {event.date}")
        await bot.edit_message(config.TO_CHAT_ID, config.TO_MESSAGE_ID, event.text)

bot.run_until_disconnected()
