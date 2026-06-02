from Bothelper.functions import get_user_link  # from Bothelper.functions import get_user_link

get_text_welcome = ("👋<b>Приветствую тебя, моряк!</b> 🤝\n"
                    "🔥<i>Рады видеть тебя на нашем проекте!</i>\n"
                    "<i>Используй кнопкy меню ниже:</i>"
                    )

get_text_menu = ("🔍<b>Найти</b> - <i>Быстрый поиск по названию компании.</i>\n"
                 "📋<b>Список(A-Z)</b> - <i>Список компаний по алфавиту.</i>\n"
                 "📝<b>Добавить</b> - <i>Добавить компанию к обсуждению.</i>\n"
                 "📜<b>Правила</b> - <i>Обязательно к прочтению!</i> \n"
                 "📢<b>Канал</b> - <i>Канал, где размещены все компании. </i>\n"
                 "👥<b>Группа</b> - <i>Чат проекта: обсуждение и общение. </i>\n"
                 "<b>Выбери действие:</b>\n"
                 )

get_text_find_company_name = ("🔍<b>Поиск компании.</b>\n"
                              "<i>Напиши название компании:</i>\n"
                              "🇺🇸<i>English only!</i>"
                              )

get_text_add_company_name = ("📝<b>Добавление компании.</b>\n"
                             "<i>Напиши название компании:</i>\n"
                             "🇺🇸<i>English only!</i>"
                             )

# get_text_approve_company_name = ("<b>Добавление компании.</b>\n"
#                                  "Подтвердите название компании: \n"
#                                  "<i>если название не верно, введите его вручную</i>"
#                                  )

get_text_company_state = ("📊<b>Укажи тип компании: </b> \n"
                          "<i>-Крюинг\n-Шипменеджмент\n-Оператор\n-Судовладелец</i>"
                          )

get_text_company_fleet = ("🚢<b>Напиши флот компании через запятую: </b>\n"
                          "<i>если нет информации, отправь прочерк</i>"
                          )

get_text_company_cadet = ("👩‍🦲<b>В компании работает кадетская программа?</b> \n"
                          "<i>Напиши <b>Да/Нет</b> или отправь прочерк</i>"
                          )

get_text_company_description = ("🧾<b>Добавь небольшое описание. </b>\n"
                                "<b>Все что вы знаешь о компании: </b>\n"
                                "<i>отправь прочерк, если ничего не известно</i>"
                                )

get_text_company_salary = ("💵<b>Способы перевода зарплаты морякам: \n</b>"
                           "<i>Перевод в Райфайзен, Shipmoney, Martrust, наличка...\n</i>"
                           "<i>Eсли нет информации, отправь прочерк</i> "
                           )

get_text_company_website = ("📡<b>Вебсайт компании: </b>\n"
                            "<i>если вебсайта нет, отправь прочерк</i>"
                            )

get_text_company_not_found = ("❌<b>Компания не найдена.</b> \n"
                              "<i>Искать заново или добавить компанию?</i>"
                              )

get_text_company_added = ("✔️<b>Компания добавлена:</b>\n"
                          "<b><a href=\"https://t.me/SeaCrewDash\">Канал Проекта</a></b>\n"
                          "<i>После проверки модератором компания появится в списке:</i>\n"
                          "<i><a href=\"https://telegra.ph/Spisok-kryuing-kompanij-06-27\">Список (A-Z)</a></i>\n"
                          "🤝Спасибо за участие в проекте! 🔥"
                          )

get_text_stop = ("🛑<b>Остановлено!</b>\n"
                 "<i>Используй кнопкy меню ниже:</i>"
                 )

get_text_close = ("🆑<b>Закрыто!</b>\n"
                  "<i>Используй кнопкy меню ниже:</i>"
                  )

get_text_admin_start = ("🧾<b>Напиши сообщение, "
                        "которое необходимо передать админу:</b>\n"
                        "👽<i>Он ответит в ближайшее время.</i>"
                        )

get_text_admin_stop = ("👍<b>Сообщение отправлено.</b>\n"
                       "🕦<i>Ожидай ответа администратора.</i>")

get_text_admin_should_answer = "👽<b>Напиши ответ на сообщение:</b>\n"

get_text_admin_should_answer_more = "👽<b>Ответить далее?</b>"

get_text_admin_did_not_answer = ("🛑<b>Без ответа!</b>\n"
                                 "<i>Данные пользователя стёрты</i>"
                                 )

get_text_check_sub = ("🔔Пожалуйста, подпишись на группу проекта, "
                      "для работы с ботом:\n@seacrewchat"
                      )

get_text_creating_post = "🕓<i>Создаю пост...</i>"


# def get_text_company_website(website):
#     website_text = (f"<b>Подтвердите вебсайт компании:</b> \n"
#                     f"<i>(если вебсайт не верен, введите его вручную</i>)\n\n"
#                     f"{website}")
#     return website_text


def get_text_from_user(user_id, user_first_name, message_to_admin):
    user_sent_message_to_admin = \
        (
            f'⚡️<b>Сообщение от</b> {get_user_link(user_id, user_first_name)}:\n'
            f'<i>{message_to_admin}</i>'
        )
    return user_sent_message_to_admin


def get_text_from_admin(admin_answer_text):
    admin_sent_message_to_user = \
        (
            '⚡️<b>Ответ от Админа:</b>\n'
            f'{admin_answer_text}'
        )
    return admin_sent_message_to_user


def get_user_touch_menu(query_user_id, query_user_first_name):
    user_touch_menu = (
        f"📋<b>Нажал menu:</b> {get_user_link(query_user_id, query_user_first_name)}"
    )
    return user_touch_menu


def get_company_post(creator_user_id,
                     creator_user_first_name,
                     company_name,
                     company_website,
                     company_state,
                     company_fleet,
                     company_cadet,
                     company_description,
                     company_salary
                     ):
    post_text = (
        f"<b>{company_name}</b>\n\n"
        f"<b>Сайт: \n"
        f"{company_website}</b> \n\n"
        f"<b>{company_state}.</b>\n"
        f"<i>{company_description}</i> \n\n"
        "<b>Флот:</b> \n"
        f"-<i>{company_fleet}</i> \n\n"
        "<b>Расположение: </b> \n"
        "-<i>processing...</i> \n\n"
        f"<b>Кадетская программа: </b>{company_cadet}\n\n"
        "<b>Способы перевода зарплаты: </b>\n"
        f"<i>-{company_salary}</i>\n\n"
        "☑️ <a href=\"https://t.me/SeahelperBot\">"
        "<b>Навигация проекта</b></a> ☑️\n\n"
        "<i>(Информация взятая из открытых источников.</i>"
        "<i>Информация используется только в ознакомительных целях).</i>\n\n"
        f"<i>Posted by: {get_user_link(creator_user_id, creator_user_first_name)}</i>\n\n"
        "🔽<b>Оставить отзыв</b>🔽"
    )
    return post_text
