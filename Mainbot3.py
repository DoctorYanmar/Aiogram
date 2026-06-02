import asyncio
import configparser
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import Message, ChatActions

from Mainbot.buttons import navigation_button, key_navi_reply
from Mainbot.ratings import handle_ratings
import Mainbot.texts as texts
from Mainbot.chatgpt import get_gpt_message
from Mainbot.functions import restricted

config = configparser.ConfigParser()
config.read('Keys/key.ini')

token = config['Telegram']['token_test']  # token
admin_id = config['Telegram']['admin_id']
channel_id = config['Telegram']['test_channel_id']  # channel_id
dashboard_channel_id = config['Telegram']['dashboard_channel_id']
log_channel_id = config['Telegram']['log_channel_id']

bot = Bot(token=token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


async def main():
    await dp.start_polling()


@dp.message_handler(commands=['start'])
async def handle_start(message: Message):
    await bot.send_chat_action(message.chat.id, ChatActions.TYPING)
    await key_navi_reply(message)


@dp.message_handler(lambda message: 'навигация' in message.text.lower())
@restricted
async def handle_navigation_button(message: Message):
    await bot.send_chat_action(message.chat.id, ChatActions.TYPING)
    await navigation_button(bot, message)


@dp.message_handler(lambda message: 'юнга' in message.text.lower())
@restricted
async def handle_gpt_message(message: Message):
    await bot.send_chat_action(message.chat.id, ChatActions.TYPING)
    thinking = await message.answer('🤔Дай подумаю...')
    await get_gpt_message(message)
    await bot.delete_message(message.chat.id, thinking.message_id)


@dp.message_handler(content_types=['new_chat_members'], chat_id=channel_id)
async def handle_new_members(message: Message):
    await bot.send_chat_action(message.chat.id, ChatActions.TYPING)
    new_members = message.new_chat_members
    await bot.delete_message(message.chat.id, message.message_id)
    for member in new_members:
        new_member_id = member.id
        new_member_first_name = member.first_name
        welcome_message = await bot.send_message(
            message.chat.id,
            texts.welcome_new_chat_member(new_member_id, new_member_first_name),
            parse_mode='HTML'
        )
        await bot.send_message(
            log_channel_id,
            texts.get_text_new_chat_member(new_member_id, new_member_first_name),
            parse_mode='HTML'
        )
        await asyncio.sleep(10)
        await bot.delete_message(message.chat.id, welcome_message.message_id)
        await bot.send_chat_action(message.chat.id, ChatActions.TYPING)
        rules_message = \
            await bot.send_message(
                message.chat.id,
                text=texts.chat_rules,
                disable_web_page_preview=True,
                parse_mode='HTML'
            )
        await asyncio.sleep(30)
        await bot.delete_message(message.chat.id, rules_message.message_id)
        await bot.send_chat_action(message.chat.id, ChatActions.TYPING)
        await message.answer(texts.ask_chat_gpt, parse_mode='HTML')


@dp.message_handler(content_types=['left_chat_member'], chat_id=channel_id)
async def handle_left_chat_member(message: Message):
    left_user_id = message.left_chat_member.id
    left_user_name = message.left_chat_member.first_name
    await bot.send_message(
        log_channel_id,
        texts.get_text_left_chat_member(left_user_id, left_user_name),
        parse_mode='HTML'
    )
    # print(left_user_id, left_user_name)
    await bot.delete_message(message.chat.id, message.message_id)


@dp.message_handler(lambda message: True)
async def handle_all_messages(message: Message):
    await bot.send_chat_action(message.chat.id, ChatActions.TYPING)
    await handle_ratings(message)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
