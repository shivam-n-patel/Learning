from aiogram import Bot, Dispatcher
import logging

TOKEN = "6347569730:AAEkXqBVgXhrpCMznvAyTKyb2TrxeRpm3TQ"

async def start_bot(bot: Bot):
    await bot.send_message("6105400931", f"Hello, I am Online✋!")
    
async def stop_bot(bot: Bot):
    await bot.send_message("6105400931", f"Bye, I am going Offlie👋!")

flag = {}

def admin():
    logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
                    )

    bot = Bot(token=TOKEN, parse_mode="HTML")
    dp = Dispatcher()

    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
        
    return bot, dp