from aiogram import types
import asyncio
from Mainbot.functions import get_user_link  # from Mainbot.functions import get_user_linki


async def navigation_button(bot, message: types.Message):
    await bot.delete_message(message.chat.id, message.message_id)
    keyboard = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton(text='🕹 Навигация 🕹',
                                        url="https://t.me/SeahelperBot"
                                        )
    keyboard.add(button)
    sent_message = await message.answer("🕹<b>Кнокпа навигации.</b>\n"
                                        "<i>Жми и переходи "
                                        "на страницу навигации проекта.</i>",
                                        reply_markup=keyboard,
                                        parse_mode='HTML'
                                        )

    await asyncio.sleep(60)
    await bot.delete_message(message.chat.id, sent_message.message_id)


async def key_navi_reply(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Навигация')
    markup.add(btn1)
    await message.answer(text="🤖Приветствую, "
                              f"{get_user_link(message.from_user.id, message.from_user.first_name)}! \n"
                              "У нас установлена удобная навигация под клавиатурой.\n"
                              "Вызывай и пользуйся. ",
                         parse_mode='HTML',
                         reply_markup=markup.row()
                         )
