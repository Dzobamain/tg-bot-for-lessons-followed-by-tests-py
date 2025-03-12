import os
import telebot
from dotenv import load_dotenv

# API
load_dotenv()

TOKEN = os.getenv("TELEGRAM_API_TOKEN")
CHANNEL_ID = os.getenv("TELEGRAM_CHANNEL_ID")
# Bot
bot = telebot.TeleBot(TOKEN)
# Levels
LEVELS = ["test/basicLevel/", "test/mediumLevel/", "test/proLevel/"]
LEVEL_NAMES = ["BASIC Level", "MEDIUM Level", "PRO Level"]
current_level_index = 0
helpMessage = "help to user_name"
incorrect_answers = 0