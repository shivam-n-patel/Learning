import asyncio
from aiogram import Bot, F
import cv2

from aiogram.types import Message, BufferedInputFile
from aiogram.filters import Command

from basic import get_start
import admin

bot, dp = admin.admin()

# @dp.message(Command(commands=['pic']))
# async def get_photo(msg: Message):
#     await msg.answer("You Sent a Photo!")
    
    # file = await bot.get_file(msg.photo[-1].file_id)
    # await bot.download_file(file_path=file.file_path, destination='photo.jpg')
    
  

async def send_photo_to_user(msg: Message, bot: Bot):
    
    colored_image = cv2.imread(str(msg.from_user.id)+"pic.jpg")
    bw_image = cv2.cvtColor(colored_image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(str(msg.from_user.id)+"pic.jpg", bw_image)
    
    file_to_send = BufferedInputFile.from_file(str(msg.from_user.id)+"pic.jpg")
    await bot.send_photo(msg.chat.id, file_to_send)
    
async def recv(msg: Message, bot: Bot):
    await msg.answer("Send a Picture")
    admin.flag[msg.from_user.id] = 1
    # file_to_send = BufferedInputFile.from_file("bot.jpeg")
    # await bot.send_photo(msg.chat.id, file_to_send)
    
    

async def on_photo_receive(message: Message, bot: Bot):
    
    if message.from_user.id not in admin.flag:
        admin.flag[message.from_user.id] = 0
    
    if admin.flag[message.from_user.id]  == 1:  
        file = await bot.get_file(message.photo[-1].file_id)
        await bot.download_file(file.file_path, str(message.from_user.id)+'pic.jpg')
        
        await send_photo_to_user(message, bot)
        
        admin.flag[message.from_user.id]  = 0
        

async def start():
    
    dp.message.register(get_start, Command(commands=['start','help']))
    dp.message.register(recv,Command(commands=['convert']))
    
    dp.message.register(on_photo_receive, F.photo)
    
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()



if __name__ == "__main__":
    asyncio.run(start())