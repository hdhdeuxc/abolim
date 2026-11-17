from rubka.asynco import Robot, Message, filters
import asyncio

TOKEN = "CJFABE0VVXJBDROGFZMHCHLYTALMNUQYEPKILJYUOBNCBCVTLIOCPXPMWURKCOHP"
bot = Robot(TOKEN)

@bot.on_message(filters.text("سلام"))
async def salam_handler(app, message: Message):
    await message.reply("سلام 🌸")

asyncio.run(bot.run())
