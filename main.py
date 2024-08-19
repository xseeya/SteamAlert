from requests import get, post
import bs4
import time

from config import *


def check_online(steam_id: str):
    r = get(f'{steam_id}')
    soup = bs4.BeautifulSoup(r.text, 'html.parser')
    status = soup.find('div', 'profile_in_game_header')
    game = soup.find('div', 'profile_in_game_name')
    if status:
        if status and game:
            return f'💬Status: {status.text}\nℹ️Game: {game.get_text(strip=True)}'
        else:
            return f'💬Status: {status.text}'


def alert():
    while True:
        for i in steam_acc:
            status = check_online(i)
            if i not in status_of_account:
                status_of_account[i] = status
                time.sleep(timeout)
            else:
                if status == status_of_account[i]:
                    continue
                else:
                    status_of_account[i] = status
                    post(f'{tg_url}', data={
                            "chat_id": chat_id,
                            "text": f'❗️ Account status was changed\n\n🔎Link to account: {i}\n\n{status}',
                            "disable_web_page_preview": True,
                            "disable_notification": True,
                        })

                    time.sleep(timeout)


alert()
