import telebot
import time
TOKEN = '7479862608:AAFBa3nhHRzPTJW7u9YxjhNT_W5xhtM9_nc'
bot = telebot.TeleBot(TOKEN)
WEB_APP_URL = 'https://xv4pvn5mnjoedjzym9tzha.on.drv.tw/relenas%20server/'

@bot.message_handler(commands=['start', 'website'])
def heartbeat():
    while True:
        try:
            bot.send_message(-1002191507750, "Бот роботает исправно!")
        except:
            bot.send_message(-1002191507750, "Бот был выключен!")
        time.sleep(1800)
def start(message):
    keyboard = telebot.types.InlineKeyboardMarkup()

    keyboard.add(telebot.types.InlineKeyboardButton(text="Открыть сайт", web_app=web_app_button))
    bot.send_message(message.chat.id, "Нажмите кнопку, чтобы открыть сайт:", reply_markup=keyboard)

bot.polling(none_stop=True)