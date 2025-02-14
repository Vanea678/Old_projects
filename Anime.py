import telebot
from telebot import types

bot = telebot.TeleBot("7267859610:AAEdgWlmmgHRl4KSz2jGg4Yyo1xH3VO8fxI")
WEB_APP_URL = 'https://anime-hub-web-rqcj.vercel.app/'

@bot.message_handler(commands=['start'])
def send_menu(message):
    markup = types.InlineKeyboardMarkup()
    web_app_button = telebot.types.WebAppInfo(url=WEB_APP_URL)
    BRW = types.InlineKeyboardButton("Аниме Онлайн🎫", web_app=web_app_button)
    button2 = types.InlineKeyboardButton("Про бота🤖", callback_data='')
    kanal = types.InlineKeyboardButton("Канал автора👉", url='https://t.me/studio_relenas')
    button4 = types.InlineKeyboardButton("Поддержка бота ️📒", url='https://t.me/nasa_20211')
    button5 = types.InlineKeyboardButton("Донат💸", callback_data='donate')
    markup.add(button2)
    markup.add(button4, button5)
    markup.add(BRW, kanal)
    bot.send_message(message.chat.id,"""<b>Главное меню выбор пункта:""", reply_markup=markup)

    def callback_query(call):
        if call.data == "donate":
            markup = types.InlineKeyboardMarkup()
            button_2 = types.InlineKeyboardButton("MONOBANK💸", url='https://send.monobank.ua/jar/4hCWns64MS')
            button_3 = types.InlineKeyboardButton("Trush Wallet", callback_data="Krypto")
            markup.add(button_2, )
            markup.add(button_3, )
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="""Допомого проекту""", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
        if call.data == "Krypto":
            markup = types.InlineKeyboardMarkup()
            KRP = types.InlineKeyboardButton("BTC", url='https://link.trustwallet.com/send?coin=0&address=bc1qe6cn8567w0j72cvj59mn9twvrl8h0r702cs7fj')
            KRP1 = types.InlineKeyboardButton("ETH", url='https://link.trustwallet.com/send?coin=60&address=0x19627eaFEe2ba87c2960d080B02E5B1119A17A36')
            KRP2 = types.InlineKeyboardButton("TON", url='https://link.trustwallet.com/send?coin=607&address=UQB42NobC_Hz96YQOB4UqHkH8UdrCAqITqS54oqb6viubfRy')
            KRP3 = types.InlineKeyboardButton("NOT", url='https://link.trustwallet.com/send?coin=607&address=UQB42NobC_Hz96YQOB4UqHkH8UdrCAqITqS54oqb6viubfRy&token_id=EQAvlWFDxGF2lXm67y4yzC17wYKD9A0guwPkMs1gOsM__NOT')
            KRP4 = types.InlineKeyboardButton("MATIС", url='https://link.trustwallet.com/send?coin=966&address=0x19627eaFEe2ba87c2960d080B02E5B1119A17A36')
            KRP5 = types.InlineKeyboardButton("BNB", url='https://link.trustwallet.com/send?coin=20000714&address=0x19627eaFEe2ba87c2960d080B02E5B1119A17A36')
            KRP6 = types.InlineKeyboardButton("CRO", url='https://link.trustwallet.com/send?coin=10000025&address=0x19627eaFEe2ba87c2960d080B02E5B1119A17A36')
            KRP7 = types.InlineKeyboardButton("DOGE", url='https://link.trustwallet.com/send?coin=3&address=DCapGigHcqmnHh9kvfe26cx7vJwYsRdG75')
            KRP8 = types.InlineKeyboardButton("KSM", url='https://link.trustwallet.com/send?coin=434&address=EwaCZvJHcS7evxasXiDjtruUao1R6k33kEN69GXSuMaRcj5')
            KRP9 = types.InlineKeyboardButton("TRX", url='https://link.trustwallet.com/send?coin=195&address=TLZS9HwuhD693Yp8i9MXDCDigEsKW2LVmu')
            markup.add(KRP2)
            markup.add(KRP,KRP1,KRP3)
            markup.add(KRP4,KRP5,KRP6)
            markup.add(KRP7,KRP8,KRP9)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="""""", reply_markup=markup)




bot.polling(non_stop=True)