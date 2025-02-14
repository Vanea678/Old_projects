import telebot
from telebot import types

bot = telebot.TeleBot("7882126567:AAFjT36DAi7ym0iDQKY_WICn9WprekSo0II")

@bot.message_handler(commands=['start'])
def send_call(message):
    bot.reply_to(message, """При использование бота автор и разработчики софта несёт ответственность за ваши действия.
Бот Сохраняет всю историю поиска.
Для принятия что автор не несет ответственность за ваши действия  эту кнопку.
/menu""")

@bot.message_handler(commands=['restart', 'menu'])
def send_menu(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("Поиск🔎", callback_data="soft",)
    button2 = types.InlineKeyboardButton("Софт🕵️", callback_data='soft')
    donate = types.InlineKeyboardButton("Донат💵", url='https://send.monobank.ua/jar/4hCWns64MS')
    kanal = types.InlineKeyboardButton("Канал автора👉", url='https://t.me/studio_relenas')
    markup.add(button1, button2)
    markup.add(donate, kanal)
    bot.send_message(message.chat.id, text="Главное меню выбор пункта:" ,reply_markup=markup)

    def callback_query(call):
        if call.data == "soft":
            markup = types.InlineKeyboardMarkup()
            button_2 = types.InlineKeyboardButton("Поиск", url='https://t.me/Glassboga_bot')
            button_3 = types.InlineKeyboardButton("Премиум Поиск (Недоступно.)", callback_data="info1")
            markup.add(button_2,)
            markup.add(button_3,)
            bot.send_message(call.chat.id, "Пойск", reply_markup=markup)

bot.polling(non_stop=True)