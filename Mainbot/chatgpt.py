import configparser
from aiogram.types import Message
import openai
from Mainbot.texts import gpt_role  # from Mainbot.texts import gpt_role

config = configparser.ConfigParser()
config.read('Keys/key.ini')
openai.api_key = config['OpenAI']['openai_key']


async def get_gpt_message(message: Message):
    user_text = message.text
    msg_for_user = await openai_message(msg_for_openai=user_text)
    await message.answer(msg_for_user, disable_web_page_preview=True)


async def openai_message(msg_for_openai: str):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        temperature=0.9,
        max_tokens=900,
        messages=[
            {"role": "system", "content": f'{gpt_role}'
             },
            {"role": "user", "content": msg_for_openai}
        ]
    )
    return response.choices[0].message.content
