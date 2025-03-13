import random
import os
from config import bot, LEVEL_NAMES, LEVELS, helpMessage, special_char
from answer.answer_client import check_answer

def start_test(chat_id, lesson_number, level_index):
    if level_index >= len(LEVELS):
        bot.send_message(chat_id, "🏁 Finish")
        return

    LEVEL_PATH = LEVELS[level_index]
    file_path = f"{LEVEL_PATH}{lesson_number}.txt"

    if not os.path.exists(file_path):
        # If the file is not found at the current level, move to the next level
        start_test(chat_id, 1, level_index + 1)
        return

    lesson_link, questions = read_questions_from_file(file_path)

    bot.send_message(chat_id, f"🔹 Level: {LEVEL_NAMES[level_index]}")
    bot.send_message(chat_id, f"📚 Lesson: {lesson_link}")

    if not questions:
        bot.send_message(chat_id, "⚠️ to next level")
        start_test(chat_id, lesson_number + 1, level_index)
        return

    ask_question(chat_id, questions, 0, lesson_number, level_index)

def read_questions_from_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.read().strip().split("\n")

    lesson_link = lines[0] if lines else ""
    questions_data = lines[1:]

    questions = []
    current_question = None

    for line in questions_data:
        line = line.strip()
        if not line:
            continue
        if line == special_char:
            if current_question:
                questions.append(current_question)
            current_question = None
        elif current_question is None:
            current_question = {"question": line, "correct_answer": "", "options": []}
        elif current_question["correct_answer"] == "":
            current_question["correct_answer"] = line
            current_question["options"].append(line)
        else:
            current_question["options"].append(line)

    if current_question:
        questions.append(current_question)

    return lesson_link, questions

# Function for formatting questions
def format_question(question_data):
    options = question_data["options"]
    random.shuffle(options)  # Shuffling the answers

    letters = ["a", "b", "c", "d"]
    formatted_options = [f"{letters[i]}) {options[i]}" for i in range(len(options))]

    correct_letter = letters[options.index(question_data["correct_answer"])] # Determining the correct letter

    return f"{question_data['question']}\n" + "\n".join(formatted_options), correct_letter

# Sending questions
def ask_question(chat_id, questions, index, lesson_number, level_index):
    if index >= len(questions):
        start_test(chat_id, lesson_number + 1, level_index)
        return

    question_text, correct_letter = format_question(questions[index])

    bot.send_message(chat_id, question_text)
    bot.register_next_step_handler_by_chat_id(
        chat_id,
        check_answer,
        questions,
        index,
        correct_letter,
        lesson_number,
        level_index
    )