import telebot
import time

bot = telebot.TeleBot('7021182866:AAEQ8WR_QHMW14kSA8Qqcw6PnsuJ37cYpAI')
TARGET_CHAT_ID = -1002162846254

@bot.message_handler(commands=['start','menu'])
def heartbeat():
    while True:
        try:
            bot.send_message(-1002162846254, "Бот роботает исправно!")
        except:
            bot.send_message(-1002162846254, "Бот был выключен!")
        time.sleep(1800)

@bot.message_handler(func=lambda message: True)
def forward_message(message):
    sender_info = []
    if message.from_user.first_name:
        sender_info.append(message.from_user.first_name)
    if message.from_user.username:
        sender_info.append(f"@{message.from_user.username}")

    sender_text = ", ".join(sender_info) if sender_info else "Неизвестный пользователь"

    # Create keyboard with three buttons
    keyboard = telebot.types.InlineKeyboardMarkup()
    button1 = telebot.types.InlineKeyboardButton("Вопрос", callback_data=f"Вопрос_{message.chat.id}_{message.message_id}")
    button2 = telebot.types.InlineKeyboardButton("Идея", callback_data=f"Идея_{message.chat.id}_{message.message_id}")
    button3 = telebot.types.InlineKeyboardButton("Жалоба", callback_data=f"Жалоба_{message.chat.id}_{message.message_id}")
    keyboard.add(button1, button2, button3)

    forward_text = f"Сообщение от *{sender_text}*:\n\n{message.text}"
    try:
        bot.send_message(TARGET_CHAT_ID, forward_text, reply_markup=keyboard, parse_mode="Markdown")
    except telebot.apihelper.ApiException as e:
        print(f"Error sending message: {e}")  # Log the error

# Callback query handler
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    data = call.data.split("_")
    category = data[0]
    chat_id = int(data[1])
    # message_id = int(data[2])  # Unused variable, removed

    if category in ["Вопрос", "Идея", "Жалоба"]:
        bot.send_message(chat_id, f"Ваш {category} принят. Мы свяжемся с вами в ближайшее время.")

        # Additional actions based on category (add your logic here)
        if category == "Вопрос":
            pass
        elif category == "Идея":
            pass
        elif category == "Жалоба":
            pass


bot.polling(none_stop=True)
