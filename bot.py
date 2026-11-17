from rubka import Bot

bot = Bot("CJFAE06VJXJBDROGFZHMCHLYTALMNUQYEPKJIJYOBNCBVCITOPXPWMWRKCOHP")

@bot.on_message()
def handle_message(message):
    message.reply("سلام!")

bot.run()
