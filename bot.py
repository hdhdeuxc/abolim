From rubpy import Client, filters
from rubpy.types import Update

# ساخت کلاینت ربات با استفاده از توکن شما
bot = Client(name='my_bot', token='CJFABE0VVXJBDROGFZMHCHLYTALMNUQYEPKILJYUOBNCBCVTLIOCPXPMWURKCOHP')

@bot.on_message_updates(filters.text)
async def updates(update: Update):
    # چاپ پیام دریافتی در لاگ‌ها برای تست
    print(update)
    # پاسخ به کاربر برای تست سلامت ربات
    await update.reply('سلام! ربات شما با موفقیت در رندر روشن شد. 🚀')

if __name__ == '__main__':
    bot.run()
