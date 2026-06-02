from Mainbot.functions import get_user_link  # Mainbot.functions

chat_rules = (
    "<a href=\"https://telegra.ph/Morskie-Agentstva-Moryaki-Rossii-Kryuingi-06-25\">"
    "📜<b>Правила проекта.</b></a>\n"
    "💪Будь активен, делись мнением и отзывом, приглашай друзей.\n"
    "🤖Используй кнопку навигации по проекту.\n"
    "🕹В разделе навигации найди крюинг/судовладельца, "
    "о котором хочешь рассказать или спросить.\n"
    "📝Добавь компанию, которую хочешь обсудить."
)

gpt_role = (
    "Ты Юнга. Помощник в чате для моряков. "
    "Ты хорошо строишь русскую речь "
    "в своих ответах. "
    "Отвечаешь кратко но с юмором, "
    "в манере пиратов из романа "
    "Роберта Льюиса Стивенсона. "
    "Так же предлагаешь морякам "
    "перейти на канал навигации: "
    "https://t.me/SeahelperBot там "
    "найти в поиске необходимую "
    "компанию или добавить компанию "
    "в каталог для обсуждения вручную. "
    "Твой ответ содержит не более 500 токенов"

)

ask_chat_gpt = ("🤖Я <b>Юнга</b>, ChatGPT AI V 3.5 Turbo.\n"
                "🤝Я отвечу на любой твой вопрос.\n"
                "❓Для того, чтобы задать мне вопрос, используй "
                "Слово-Триггер: <b>Юнга</b> вначале вопроса:\n"
                "👉<i>Юнга, как уйти в первый рейс?..и т.д.</i>\n")


def welcome_new_chat_member(new_member_id, new_member_first_name):
    text = (f"👋<b>Добро пожаловать в группу,</b>\n"
            f"{get_user_link(new_member_id, new_member_first_name)}!")
    return text


def get_text_left_chat_member(left_user_id, left_user_name):
    text = f"👎<b>Вышел из группы:</b> {get_user_link(left_user_id, left_user_name)}"
    return text


def get_text_new_chat_member(new_member_id, new_member_first_name):
    text = f"👍<b>Присоединился:</b> {get_user_link(new_member_id, new_member_first_name)}"
    return text
