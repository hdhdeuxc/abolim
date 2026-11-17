from rubka import Bot
from PIL import Image

# راه‌اندازی ربات با توکن شما
bot = Bot("CJFABE0VVXJBDROGFZMHCHLYTALMNUQYEPKILJYUOBNCBCVTLIOCPXPMWURKCOHP")

@bot.on_message()
def handle_message(message):
    try:
        # پاسخ به پیام کاربر
        message.reply("سلام! ربات با موفقیت فعال شد و آنلاین است.")
    except Exception as e:
        print(f"Error handling message: {e}")

if __name__ == "__main__":
    print("Bot is starting...")
    bot.run()
    
