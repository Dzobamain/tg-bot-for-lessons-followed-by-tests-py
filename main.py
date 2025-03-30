from config import bot, CHANNEL_ID, helpMessage, incorrect_answers
from help.help_functions import command_help
from test.test_functions import start_test

def check_subscription(user_id):
    if not CHANNEL_ID:
        return True
    try:
        chat_member = bot.get_chat_member(CHANNEL_ID, user_id)
        if chat_member.status in ['member', 'administrator', 'creator']:
            return True
        else:
            return False
    except Exception as e:
        print(f"ERROR: {e}")
        return False

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, f"Hi, {message.from_user.first_name}")
    user_id = message.from_user.id
    if check_subscription(user_id):
        bot.send_message(message.chat.id, "✅ Verification successful")
        help(message)
    else:
        not_verified_message = "❌ You need a subscription"
        bot.send_message(message.chat.id, not_verified_message)

@bot.message_handler(commands=["help"])
def help(message):
    command_help(message)

@bot.message_handler(commands=["test"])
def test(message):
    start_test(message.chat.id, 1, 0)

bot.polling(none_stop=True, timeout=60)