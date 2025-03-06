from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait
import time
from asyncio import sleep
api_id = "24960778"
api_hash = "b60bf010f3561a695eb53d03d236695e"

# with Client(name="my_account", api_hash=api_hash, api_id=api_id) as app:
#     app.send_message("me", "Это я бот")

client = Client(name="my_account", api_hash=api_hash, api_id=api_id)
spam_text = 'Это спам мой друг'


@client.on_message(filters.command("type", prefixes='!') & filters.me)
def type(client_object, message: Message):
    input_text = message.text.split("!type ", maxsplit=1)[1]
    temp_text = input_text
    edited_text = ""
    typing_symbol = "|"

    while edited_text != input_text:
        try:
            message.edit(edited_text + typing_symbol)
            time.sleep(0.05)
            edited_text = edited_text + temp_text[0]
            temp_text = temp_text[1:]
            message.edit(edited_text)
            time.sleep(0.05)
        except FloodWait:
            print("Превышен лимит сообщений")

@client.on_message(filters.command('spam', prefixes= '!') & filters.me)
async def enable_spam(_, message):
    await message.delete()
    cmd = message.text.split("!spam") 
    for i in range(int(cmd[1])):
        await message.reply(spam_text)  

@client.on_message(filters.command('!love', prefixes='!') & filters.me)
async def enable_spam(_, message):
    await message.delete()
    


client.run()


