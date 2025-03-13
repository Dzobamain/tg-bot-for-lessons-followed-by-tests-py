from config import bot, LEVELS, LEVEL_NAMES, helpMessage, incorrect_answers
from subscription_checker import check_subscription
from help.help_functions import command_help
from test.test_functions import start_test

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, f"Hi, {message.from_user.first_name}")
    user_id = message.from_user.id
    if check_subscription(user_id):
        bot.send_message(message.chat.id, "✅GEATE")
        help(message)
    else:
        not_verified_message = "❌ERROR"
        bot.send_message(message.chat.id, not_verified_message)

@bot.message_handler(commands=["help"])
def help(message):
    command_help(message)

@bot.message_handler(commands=["test"])
def test(message):
    start_test(message.chat.id, 1, 0)

bot.polling(none_stop=True, timeout=60)