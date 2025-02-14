import telebot

bot = telebot.TeleBot('7309094710:AAER1CaTwigb7gWep19cU-OhDy_aGj5GSyo')
CHAT_ID = -1002191507750
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    bot.forward_message(CHAT_ID, message.chat.id, message.message_id)
    markup = telebot.types.InlineKeyboardMarkup()
    button1 = telebot.types.InlineKeyboardButton(
        text=f'Ник: {message.from_user.username}', callback_data='username'
    )
    button2 = telebot.types.InlineKeyboardButton(
        text='Нажатая кнопка', callback_data='button_pressed'
    )
    markup.add(button1, button2)
    bot.send_message(message.chat.id, 'Сообщение отправлено в чат', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    if call.data == 'username':
        bot.answer_callback_query(call.id, 'Это ваш ник')
    elif call.data == 'button_pressed':
        bot.answer_callback_query(call.id, 'Вы нажали кнопку')
bot.polling(non_stop=True)
