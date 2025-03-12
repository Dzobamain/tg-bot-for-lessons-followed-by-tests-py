from config import bot, CHANNEL_ID

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