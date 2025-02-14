import telebot
import webbrowser
import threading
import time
from telebot import types
import sys

# Replace with your actual Telegram bot token
bot = telebot.TeleBot('YOUR_BOT_TOKEN')

@bot.message_handler(commands=['start', 'menu'])
def send_menu(message):
    markup = types.InlineKeyboardMarkup()

    # Create reusable buttons for cleaner code
    button1 = types.InlineKeyboardButton("Windows 10", callback_data='button1')
    button2 = types.InlineKeyboardButton("Windows 11", callback_data='button2')
    button3 = types.InlineKeyboardButton("Office 2021", callback_data='button3')
    button4 = types.InlineKeyboardButton("Office 2019", callback_data='button4')
    button5 = types.InlineKeyboardButton("Office 365", callback_data='button5')
    donate = types.InlineKeyboardButton("Донат", callback_data='donate')
    kanal = types.InlineKeyboardButton("Канал автора", url='https://t.me/studio_relenas')

    # Add buttons to the markup
    markup.add(button1, button2)
    markup.add(button3, button4, button5)
    markup.add(donate, kanal)

    bot.send_message(message.chat.id, "Безплатні ліцензії Windows 10/11 Ліцензії Microsoft Office 2019/2021/365", reply_markup=markup)

def heartbeat():
    while True:
        try:
            # Send a more informative message about bot status
            bot.send_message(-1002191507750, "Бот работает исправно! Последнее обновление информации о ключах: " + time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))  # Add timestamp
        except:
            # Log the error for debugging
            print("Error sending heartbeat message:", sys.exc_info()[0])
            bot.send_message(-1002191507750, "Бот был выключен! Перезапуск...")  # Inform users of outage

        time.sleep(1800)  # Check every 30 minutes

heartbeat_thread = threading.Thread(target=heartbeat)
heartbeat_thread.start()

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'button1':
        # Consider fetching license keys from a reliable source and updating periodically
        message_text = """**Please note:** Distributing license keys may violate software terms of service. It's recommended to obtain them from official sources.

**Version** | **Client KMS Installation Key**
------- | --------
Windows 10 Pro | ... (Replace with placeholder)
Windows 10 Pro N | ... (Replace with placeholder)
... (Add other Windows 10 versions)
"""
        bot.send_message(call.message.chat.id, message_text, parse_mode='Markdown')

    elif call.data == 'button2':
        # Follow the same approach for other buttons (Windows 11, Office versions)
        message_text = """... (Provide information about Windows 11 keys)"""
        bot.send_message(call.message.chat.id, message_text, parse_mode='Markdown')

    # ... (Implement similar logic for button3, button4, button5)

    elif call.data == 'donate':
        message_text = """
Підтримуте мій проект/канал! Кожен донат важен.
Карти:
₴- 4441 1111 4637 1566
₴- 4441 1144 8410 4565
"""
        bot.send_message(call.message.chat.id, message_text, parse_mode='Markdown')

    bot.answer_callback_query(call.id)  # Acknowledge callback query

bot.polling(none_stop=True)