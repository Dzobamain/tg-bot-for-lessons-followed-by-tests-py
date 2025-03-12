from config import bot

def command_help(message):
    helpMessage = """📚 Commands:
    /start
    /help
    /test
    """
    bot.send_message(message.chat.id, helpMessage)