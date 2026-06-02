import json
# import html
# import asyncio
from aiogram import types
import Mainbot.functions as functions  # Mainbot.functions as functions

ratings_file = 'Mainbot/ratings.json'


def load_ratings():
    try:
        with open(ratings_file, 'r') as file:
            ratings_data = json.load(file)
            ratings = {str(user_id): rating for user_id, rating in ratings_data.items()}
    except FileNotFoundError:
        ratings = {}
    return ratings


def save_ratings(ratings):
    ratings_data = {int(user_id): rating for user_id, rating in ratings.items()}
    with open(ratings_file, 'w') as file:
        json.dump(ratings_data, file)


ratings = load_ratings()

rating_triggers = ["спасибо", "спс", "благодарю", "благодарствую", "мерси", "сельвупле",
                   "дякую", "данке", "сенкс", "сенкью", "thank", "thanks", "mercy",
                   "👍", "👌", "🤝", "😍", "😻", "😘", "😚", "😽", "😙", "😗", "💋",
                   "❤", "➕", "+"
                   ]


async def handle_ratings(message: types.Message):
    reply_to = message.reply_to_message
    trigger = rating_triggers
    user_user = functions.get_user_link(message.from_user.id, message.from_user.first_name)
    if reply_to and any(trigger_word in message.text.lower() for trigger_word in trigger):
        thanked_user_id = reply_to.from_user.id
        thanked_user = functions.get_user_link(reply_to.from_user.id, reply_to.from_user.first_name)
        if str(thanked_user_id) not in ratings:
            ratings[str(thanked_user_id)] = 0
        ratings[str(thanked_user_id)] += 1
        response = f"{thanked_user}, вас поблагодарил: {user_user}. \n" \
                   f"Теперь ваш рейтинг: " \
                   f"<b>{ratings[str(thanked_user_id)]}</b>.\n" \
                   f"Продолжайте в том же духе!"
        await message.answer(response, parse_mode='HTML')
        save_ratings(ratings)
