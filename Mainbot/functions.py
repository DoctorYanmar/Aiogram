from aiogram import types
import configparser
import html

config = configparser.ConfigParser()
config.read('Keys/key.ini')
channel_id = config['Telegram']['test_channel_id']  # channel_id


def respond_to_trigger(func):
    async def wrapped(message):
        if 'юнга' in message.text.lower():
            await func(message)

    return wrapped


def restricted(func):
    async def wrapped(message: types.Message):
        if message.chat.id == int(channel_id):
            return await func(message)
        else:
            await message.reply("Извините, я могу отвечать только в группе: @seacrewchat.")

    return wrapped


def get_user_link(user_id, first_name):
    user_link = f'<a href="tg://user?id={user_id}">{html.escape(first_name)}</a>'
    return user_link
