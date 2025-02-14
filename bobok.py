import telebot

bot = telebot.TeleBot('7418136201:AAHIhvqAJRCJmOQZ7_o4RILRPB0_uBCWIlg')
user_balances = {}
levels = {1: 10, 2: 50, 3: 150}  # Пример уровней с стоимостью

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    if user_id not in user_balances:
        user_balances[user_id] = 0  # Инициализируем баланс, если пользователь новый
    bot.reply_to(message, "Добро пожаловать в кликер! Нажмите /click чтобы начать.")

@bot.message_handler(commands=['click'])
def click(message):
    user_id = message.from_user.id
    user_balances[user_id] += 1
    bot.reply_to(message, f"Ваш баланс: {user_balances[user_id]}")

@bot.message_handler(commands=['upgrade'])
def upgrade(message):
    user_id = message.from_user.id
    current_level = get_current_level(user_id)
    next_level_cost = levels.get(current_level + 1, None)

    if next_level_cost and user_balances[user_id] >= next_level_cost:
        user_balances[user_id] -= next_level_cost
        bot.reply_to(message, f"Поздравляем! Вы достигли уровня {current_level + 1}")
    else:
        bot.reply_to(message, "Недостаточно средств для прокачки или вы достигли максимального уровня.")

def get_current_level(user_id):
    balance = user_balances[user_id]
    current_level = 1

    for level, cost in levels.items():  # Iterate over dictionary items
        if balance >= cost:
            current_level = level
        else:
            break

    return current_level


bot.polling(none_stop=True)
