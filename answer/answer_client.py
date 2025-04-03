from config import bot, helpMessage

# Response check
def check_answer(message, questions, index, correct_letter, lesson_number, level_index):
    from test.test_functions import ask_question
    from main import start, help, test
    
    global incorrect_answers
    user_answer = message.text.lower().strip()
    
    if user_answer.startswith("/"):
        if user_answer == "/start":
            start(message)
        elif user_answer == "/help":
            help(message)
        elif user_answer == "/test":
            test(message)
        else:
            bot.send_message(message.chat.id, "try /help")
        bot.register_next_step_handler_by_chat_id(
            message.chat.id,
            check_answer,
            questions,
            index,
            correct_letter,
            lesson_number,
            level_index
        )
        return

    if user_answer == correct_letter:
        bot.send_message(message.chat.id, "✅ Correctly")
        ask_question(message.chat.id, questions, index + 1, lesson_number, level_index)
        incorrect_answers = 0
    else:
        incorrect_answers += 1
        bot.send_message(message.chat.id, "❌ Incorrect")
        if incorrect_answers >= 2:
            bot.send_message(message.chat.id, helpMessage)
            incorrect_answers = 0
        
        bot.register_next_step_handler_by_chat_id(
            message.chat.id,
            check_answer,
            questions,
            index,
            correct_letter,
            lesson_number,
            level_index
        )