import os
from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup
import html


# from googlesearch import search


async def get_screen_browser(url: str):
    try:
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        # ChromeDriverManager().install()
        browser = webdriver.Chrome(options=chrome_options)
        browser.get(url)
        script_directory = os.path.dirname(os.path.abspath(__file__))
        screenshot_path = os.path.join(script_directory, '../screenshot.png')
        browser.save_screenshot(screenshot_path)
        browser.quit()
    except Exception as e:
        print(str(e).splitlines()[0])
        await get_screen_browser('https://www.google.com')


async def find_company_link_in_group(company_name):
    url = "https://telegra.ph/Spisok-kryuing-kompanij-06-27"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    for link in soup.find_all("a"):
        if company_name.lower() in link.text.lower():
            return link["href"]

    return None


def get_user_link(user_id, first_name):
    user_link = f'<a href="tg://user?id={user_id}">{html.escape(first_name)}</a>'
    return user_link

# async def get_website(company_name: str):
#     websites = [j for j in search(company_name, num_results=1)]
#     if websites:
#         website = websites[0]
#         return website
#     else:
#         return None
