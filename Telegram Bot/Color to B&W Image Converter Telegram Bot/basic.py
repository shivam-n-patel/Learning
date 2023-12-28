import aiogram
import admin

async def get_start(msg: aiogram.types.Message, bot: aiogram.Bot):
    # await bot.send_message(msg.from_user.id, f"Hello, {msg.from_user.first_name} send_message.")
    # await bot.send_message(msg.from_user.id, f"<b>Hello, {msg.from_user.first_name} send_message.</b>") #formattig
    
    helpText = f"Hello, {msg.from_user.first_name}.\nHere are some commands you can execute:\n/help - Get the Menu\n/convert - convert image"
    await msg.answer(helpText)
    admin.flag[msg.from_user.id]  = 0
    # await msg.answer(f"<s>Hello, {msg.from_user.first_name} answer.</s>")
    
    # await msg.reply(f"Hello, {msg.from_user.first_name} reply.")
    # await msg.reply(f"<tg-spoiler>Hello, {msg.from_user.first_name} reply.</tg-spoiler>")

