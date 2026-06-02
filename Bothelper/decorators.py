import configparser
from aiogram import Bot
from aiogram.dispatcher.handler import CancelHandler

import Bothelper.Texts_Bothelper as Texts  # import Bothelper.Texts_Bothelper as Texts

config = configparser.ConfigParser()
config.read('Keys/key.ini')
token = config['Telegram']['token_test']  # token2
admin_id = config['Telegram']['admin_id']
channel_id = config['Telegram']['test_channel_id']  # channel_id
dashboard_channel_id = config['Telegram']['dashboard_channel_id']
log_channel_id = config['Telegram']['log_channel_id']

bot = Bot(token=token)


def check_sub_decorator_messages(func):
    async def wrapper(message, state):
        member = await bot.get_chat_member(channel_id, message.from_user.id)
        if not member.is_chat_member():
            await message.answer(Texts.get_text_check_sub, parse_mode='HTML')
            raise CancelHandler()
        return await func(message, state)

    return wrapper


def check_sub_decorator_query(func):
    async def wrapper(callback_query, state):
        member = await bot.get_chat_member(channel_id, callback_query.from_user.id)
        if not member.is_chat_member():
            await callback_query.answer()
            await callback_query.message.answer(Texts.get_text_check_sub, parse_mode='HTML')
            raise CancelHandler()
        return await func(callback_query, state)

    return wrapper
