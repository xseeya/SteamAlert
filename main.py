from requests import get, post
import bs4
import time

from config import *


def check_online(steam_id : str):
    r = get(f'{steam_id}')
    soup = bs4.BeautifulSoup(r.text, 'html.parser')
    status = soup.find('div', 'profile_in_game_header')
    game = soup.find('div', 'profile_in_game_name')

    if status and game:
        return f'💬{status.text}\nℹ️Игра: {game.get_text(strip=True)}'
    else:
        return f'💬{status.text}'


def alert():
    while True:
        for i in steam_acc:
            post(f'{tg_url}', data={
                "chat_id": chat_id,
                "text": f'🔎Ссылка на аккаунт: {i}\n\n{check_online(f'{i}')}',
                "disable_web_page_preview": True,
                "disable_notification": True,
            })
            time.sleep(timeout)


alert()