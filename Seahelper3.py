import configparser
# import asyncio
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, InlineKeyboardMarkup, ChatActions

from Bothelper.functions import get_screen_browser, find_company_link_in_group
import Bothelper.Texts_Bothelper as Texts
import Bothelper.Buttons_Bothelper as Buttons
import Bothelper.decorators as decorator

config = configparser.ConfigParser()
config.read('Keys/key.ini')
token = config['Telegram']['token_test']  # token2
admin_id = config['Telegram']['admin_id']
channel_id = config['Telegram']['test_channel_id']  # channel_id
dashboard_channel_id = config['Telegram']['dashboard_channel_id']
log_channel_id = config['Telegram']['log_channel_id']

bot = Bot(token=token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


class AddCompany(StatesGroup):
    waiting_for_company_name = State()
    waiting_for_company_state = State()
    waiting_for_company_website = State()
    waiting_for_company_fleet = State()
    waiting_for_company_cadet = State()
    waiting_for_company_description = State()
    waiting_for_company_salary = State()
    waiting_for_callback_touch = State()
    waiting_for_callback_data_find_company = State()
    waiting_for_callback_data_send_message_to_admin = State()
    waiting_for_callback_data_admin_answer = State()


async def clear_all_global():
    global user_id
    user_id = None
    return user_id


global user_id


async def main():
    await dp.start_polling(bot)


@dp.message_handler(commands=['start'], state="*")
@decorator.check_sub_decorator_messages
async def bot_command_start(message: types.Message, state: FSMContext):
    await bot.send_chat_action(message.chat.id, ChatActions.TYPING)
    await state.get_state()
    await state.finish()
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(Buttons.button_menu)
    await message.answer(Texts.get_text_welcome, parse_mode='HTML',
                         reply_markup=keyboard,
                         )
    await AddCompany.waiting_for_callback_touch.set()


@dp.message_handler(commands=['stop'], state="*")
async def bot_command_stop(message: types.Message, state: FSMContext):
    await bot.send_chat_action(message.chat.id, ChatActions.TYPING)
    await state.get_state()
    await state.finish()
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(Buttons.button_menu)
    await message.answer(Texts.get_text_stop,
                         parse_mode='HTML',
                         reply_markup=keyboard,
                         )
    await AddCompany.waiting_for_callback_touch.set()


@dp.callback_query_handler(state="*", text_contains="menu")
@decorator.check_sub_decorator_query
async def bot_query_menu(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.answer()
    await bot.send_chat_action(callback_query.message.chat.id, ChatActions.TYPING)
    await state.get_state()
    await state.finish()
    query_user_id = callback_query.message.chat.id
    if query_user_id != int(admin_id):
        query_user_first_name = callback_query.message.chat.first_name
        await bot.send_message(log_channel_id,
                               Texts.get_user_touch_menu(query_user_id, query_user_first_name),
                               parse_mode='HTML'
                               )
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(Buttons.button_find_company, Buttons.button_rules)
    keyboard.add(Buttons.button_company_board, Buttons.button_channel)
    keyboard.add(Buttons.button_add_company, Buttons.button_group)
    keyboard.add(Buttons.button_contact_admin)
    await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
    await callback_query.message.answer(Texts.get_text_menu,
                                        parse_mode='HTML',
                                        reply_markup=keyboard,
                                        )
    await AddCompany.waiting_for_callback_touch.set()


@dp.callback_query_handler(state="*", text_contains="break")
async def bot_query_break(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.answer()
    await bot.send_chat_action(callback_query.message.chat.id, ChatActions.TYPING)
    await state.get_state()
    await state.finish()
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(Buttons.button_menu)
    await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
    await callback_query.message.answer(Texts.get_text_stop,
                                        reply_markup=keyboard,
                                        parse_mode='HTML'
                                        )
    await AddCompany.waiting_for_callback_touch.set()


@dp.callback_query_handler(state="*", text_contains="close")
async def bot_query_close(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.answer()
    await bot.send_chat_action(callback_query.message.chat.id, ChatActions.TYPING)
    await state.get_state()
    await state.finish()
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(Buttons.button_menu)
    await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
    await callback_query.message.answer(Texts.get_text_close,
                                        reply_markup=keyboard,
                                        parse_mode='HTML'
                                        )
    await AddCompany.waiting_for_callback_touch.set()


@dp.callback_query_handler(state=AddCompany.waiting_for_callback_touch, text_contains="admin")
async def bot_call_admin(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.answer()
    await bot.send_chat_action(callback_query.message.chat.id, ChatActions.TYPING)
    await state.get_state()
    await state.finish()
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(Buttons.button_break)
    await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
    await callback_query.message.answer(Texts.get_text_admin_start,
                                        reply_markup=keyboard,
                                        parse_mode='HTML'
                                        )
    await AddCompany.waiting_for_callback_data_send_message_to_admin.set()


@dp.message_handler(state=AddCompany.waiting_for_callback_data_send_message_to_admin)
async def bot_send_message_to_admin(message: types.Message, state: FSMContext):
    await bot.send_chat_action(message.chat.id, ChatActions.TYPING)
    keyboard1 = InlineKeyboardMarkup(row_width=2)
    keyboard1.add(Buttons.button_admin_answer, Buttons.button_admin_not_answer)
    message_to_admin = message.text
    global user_id
    user_id = message.from_user.id
    user_first_name = message.from_user.first_name
    await bot.send_message(chat_id=admin_id,
                           text=Texts.get_text_from_user(
                               user_id,
                               user_first_name,
                               message_to_admin),
                           reply_markup=keyboard1,
                           parse_mode='HTML'
                           )
    keyboard2 = InlineKeyboardMarkup(row_width=2)
    keyboard2.add(Buttons.button_write_more_admin, Buttons.button_close)
    await message.answer(Texts.get_text_admin_stop,
                         reply_markup=keyboard2,
                         parse_mode='HTML'
                         )
    await AddCompany.waiting_for_callback_touch.set()


@dp.callback_query_handler(state='*', text='answer', chat_id=admin_id)
async def admin_bot_answer(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.answer()
    await bot.send_chat_action(callback_query.message.chat.id, ChatActions.TYPING)
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(Buttons.button_admin_not_answer)
    await callback_query.message.answer(Texts.get_text_admin_should_answer,
                                        reply_markup=keyboard,
                                        parse_mode='HTML'
                                        )
    await AddCompany.waiting_for_callback_data_admin_answer.set()


@dp.message_handler(state=AddCompany.waiting_for_callback_data_admin_answer, chat_id=admin_id)
async def admin_bot_get_answer(message: types.Message, state: FSMContext):
    await bot.send_chat_action(message.chat.id, ChatActions.TYPING)
    admin_answer_text = message.text
    global user_id
    keyboard1 = InlineKeyboardMarkup(row_width=2)
    keyboard1.add(Buttons.button_write_more_admin, Buttons.button_close)
    await bot.send_message(text=Texts.get_text_from_admin(admin_answer_text),
                           chat_id=user_id,
                           reply_markup=keyboard1,
                           parse_mode='HTML'
                           )
    keyboard2 = InlineKeyboardMarkup(row_width=2)
    keyboard2.add(Buttons.button_admin_answer, Buttons.button_admin_not_answer)
    await message.answer(Texts.get_text_admin_should_answer_more,
                         reply_markup=keyboard2,
                         parse_mode='HTML')
    await AddCompany.waiting_for_callback_touch.set()


@dp.callback_query_handler(state='*', text='not_answer', chat_id=admin_id)
async def admin_bot_answer(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.answer()
    await bot.send_chat_action(callback_query.message.chat.id, ChatActions.TYPING)
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(Buttons.button_menu)
    await clear_all_global()
    await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
    await callback_query.message.answer(Texts.get_text_admin_did_not_answer,
                                        reply_markup=keyboard,
                                        parse_mode='HTML'
                                        )
    await AddCompany.waiting_for_callback_touch.set()


@dp.callback_query_handler(state=AddCompany.waiting_for_callback_touch, text='find_company')
async def find_company(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.answer()
    await bot.send_chat_action(callback_query.message.chat.id, ChatActions.TYPING)
    await state.get_state()
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(Buttons.button_break)
    await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
    await callback_query.message.answer(Texts.get_text_find_company_name,
                                        parse_mode='HTML',
                                        reply_markup=keyboard
                                        )
    await AddCompany.waiting_for_callback_data_find_company.set()


@dp.message_handler(state=AddCompany.waiting_for_callback_data_find_company)
async def company_name_find(message: Message, state: FSMContext):
    company_name = message.text
    company_link = await find_company_link_in_group(company_name)
    await state.update_data(company_name=company_name)
    if company_link:
        await bot.send_chat_action(message.chat.id, ChatActions.TYPING)
        keyboard = InlineKeyboardMarkup(row_width=1)
        keyboard.add(Buttons.button_menu)
        await message.answer(f"<a href='{company_link}'>{company_name}</a>",
                             reply_markup=keyboard,
                             parse_mode="HTML"
                             )
        await AddCompany.waiting_for_callback_touch.set()

    else:
        await bot.send_chat_action(message.chat.id, ChatActions.TYPING)
        keyboard = InlineKeyboardMarkup(row_width=2)
        keyboard.add(Buttons.button_find_company, Buttons.button_add_company)
        keyboard.add(Buttons.button_menu)
        await message.answer(Texts.get_text_company_not_found,
                             reply_markup=keyboard,
                             parse_mode='HTML'
                             )
        await AddCompany.waiting_for_callback_touch.set()


@dp.callback_query_handler(state=AddCompany.waiting_for_callback_touch, text='add_company')
async def add_company(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.answer()
    await bot.send_chat_action(callback_query.message.chat.id, ChatActions.TYPING)
    await state.get_state()
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(Buttons.button_break)
    await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
    await callback_query.message.answer(Texts.get_text_add_company_name,
                                        parse_mode='HTML',
                                        reply_markup=keyboard
                                        )
    await AddCompany.waiting_for_company_name.set()

    # await state.get_data()
    # if await state.get_data("company_name"):
    #     company_name = await state.get_data("company_name")
    #     keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
    #                                    one_time_keyboard=True
    #                                    )
    #     keyboard.add(KeyboardButton(company_name['company_name']))
    #     keyboard2 = InlineKeyboardMarkup(row_width=1)
    #     keyboard2.add(Buttons.button_break)
    #     await callback_query.answer()
    #     await callback_query.message.answer(Texts.get_text_approve_company_name,
    #                                         parse_mode='HTML',
    #                                         reply_markup=keyboard and keyboard2
    #                                         )
    #     await AddCompany.waiting_for_company_name.set()

    # else:
    #     await callback_query.answer()
    #     keyboard = InlineKeyboardMarkup(row_width=1)
    #     keyboard.add(Buttons.button_break)
    #     await callback_query.message.answer(Texts.get_text_add_company_name,
    #                                         parse_mode='HTML',
    #                                         reply_markup=keyboard
    #                                         )
    #     await AddCompany.waiting_for_company_name.set()


@dp.message_handler(state=AddCompany.waiting_for_company_name)
async def add_company_name(message: Message, state: FSMContext):
    await bot.send_chat_action(message.chat.id, ChatActions.TYPING)
    company_name = message.text
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(Buttons.button_break)
    await message.answer(Texts.get_text_company_state,
                         parse_mode='HTML',
                         reply_markup=keyboard
                         )
    await state.update_data(company_name=company_name)
    await AddCompany.waiting_for_company_state.set()


@dp.message_handler(state=AddCompany.waiting_for_company_state)
async def add_company_state(message: Message, state: FSMContext):
    await bot.send_chat_action(message.chat.id, ChatActions.TYPING)
    company_state = message.text
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(Buttons.button_break)
    await message.answer(Texts.get_text_company_cadet,
                         reply_markup=keyboard,
                         parse_mode='HTML'
                         )

    await state.update_data(company_state=company_state)
    await AddCompany.waiting_for_company_cadet.set()


@dp.message_handler(state=AddCompany.waiting_for_company_cadet)
async def add_company_cadet(message: Message, state: FSMContext):
    await bot.send_chat_action(message.chat.id, ChatActions.TYPING)
    company_cadet = message.text
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(Buttons.button_break)
    await message.answer(Texts.get_text_company_fleet,
                         reply_markup=keyboard,
                         parse_mode='HTML'
                         )
    await state.update_data(company_cadet=company_cadet)
    await AddCompany.waiting_for_company_fleet.set()


@dp.message_handler(state=AddCompany.waiting_for_company_fleet)
async def add_company_fleet(message: Message, state: FSMContext):
    await bot.send_chat_action(message.chat.id, ChatActions.TYPING)
    company_fleet = message.text
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(Buttons.button_break)
    await message.answer(Texts.get_text_company_website,
                         parse_mode='HTML',
                         reply_markup=keyboard
                         )
    await state.update_data(company_fleet=company_fleet)
    await AddCompany.waiting_for_company_website.set()


@dp.message_handler(state=AddCompany.waiting_for_company_website)
async def add_company_website(message: Message, state: FSMContext):
    await bot.send_chat_action(message.chat.id, ChatActions.TYPING)
    company_website = message.text
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(Buttons.button_break)
    await message.answer(Texts.get_text_company_salary,
                         reply_markup=keyboard,
                         parse_mode='HTML'
                         )
    await state.update_data(company_website=company_website)
    await AddCompany.waiting_for_company_salary.set()


@dp.message_handler(state=AddCompany.waiting_for_company_salary)
async def add_company_website(message: Message, state: FSMContext):
    await bot.send_chat_action(message.chat.id, ChatActions.TYPING)
    company_salary = message.text
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(Buttons.button_break)
    await message.answer(Texts.get_text_company_description,
                         reply_markup=keyboard,
                         parse_mode='HTML'
                         )
    await state.update_data(company_salary=company_salary)
    await AddCompany.waiting_for_company_description.set()


@dp.message_handler(state=AddCompany.waiting_for_company_description)
async def add_company_descr(message: Message, state: FSMContext):
    await bot.send_chat_action(message.chat.id, ChatActions.TYPING)
    creating_post = await message.answer(
        Texts.get_text_creating_post,
        parse_mode='HTML'
    )
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(Buttons.button_menu)
    company_description = message.text
    creator_user_id = message.from_user.id
    creator_user_first_name = message.from_user.first_name
    data = await state.get_data()
    company_name = data.get("company_name")
    company_state = data.get("company_state")
    company_fleet = data.get("company_fleet")
    company_website = data.get("company_website")
    company_cadet = data.get("company_cadet")
    company_salary = data.get("company_salary")
    await get_screen_browser(company_website)
    text = Texts.get_company_post(
        creator_user_id,
        creator_user_first_name,
        company_name,
        company_website,
        company_state,
        company_fleet,
        company_cadet,
        company_description,
        company_salary
    )

    with open('screenshot.png', 'rb') as screenshot:
        await bot.send_photo(chat_id=channel_id,  # dashboard_channel_id
                             caption=text,
                             photo=screenshot,
                             parse_mode='HTML'
                             )
        await state.finish()
        await AddCompany.waiting_for_callback_touch.set()
        await creating_post.delete()
        await message.answer(Texts.get_text_company_added,
                             parse_mode='HTML',
                             reply_markup=keyboard,
                             disable_web_page_preview=True
                             )


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
