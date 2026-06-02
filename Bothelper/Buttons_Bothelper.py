from aiogram.types import KeyboardButton, InlineKeyboardButton

button_yes = KeyboardButton('ДА!')
button_no = KeyboardButton('Нет!')
button_noinfo = KeyboardButton('no info')

button_find_company = InlineKeyboardButton(text='🔍Найти', callback_data='find_company')
button_add_company = InlineKeyboardButton(text='📝Добавить', callback_data='add_company')
button_break = InlineKeyboardButton(text='🚫Прервать действие.', callback_data='break')
button_close = InlineKeyboardButton(text='🆑Закрыть', callback_data='close')
button_menu = InlineKeyboardButton(text='📋Меню', callback_data='menu')
button_contact_admin = InlineKeyboardButton(text='👽Написать админу', callback_data='admin')
button_write_more_admin = InlineKeyboardButton(text='👽Еще...', callback_data='admin_more')
button_admin_answer = InlineKeyboardButton(text='🖌Ответить', callback_data='answer')
button_admin_not_answer = InlineKeyboardButton(text='❌Не отвечать', callback_data='not_answer')

button_channel = InlineKeyboardButton(text='📢Канал',
                                      url='https://t.me/SeaCrewDash')
button_group = InlineKeyboardButton(text='👥Группа', callback_data='group',
                                    url='https://t.me/SeaCrewChat')
button_rules = InlineKeyboardButton(text='📜Правила',
                                    url='https://telegra.ph/Morskie-Agentstva-Moryaki-Rossii-Kryuingi-06-25')
button_company_board = InlineKeyboardButton(text='📋Список (A-Z)',
                                            url='https://telegra.ph/Spisok-kryuing-kompanij-06-27')

# button_back = InlineKeyboardButton(text='🔙Назад', callback_data='back')
# button_next = InlineKeyboardButton(text='🔜Далее', callback_data='next')
