import requests
import time
import my_config

API_URL = my_config.API_URL
API_CATS_URL = my_config.API_CATS_URL
BOT_TOKEN = my_config.BOT_TOKEN
ERROR_TEXT = 'Здесь должна была быть картинка с котиком :('

offset = -2
counter = 0
cat_response: requests.Response


while counter < 50:
    print('attempt = ', counter)
    updates = requests.get(f'{API_URL}{BOT_TOKEN}'
                           f'/getUpdates?offset={offset + 1}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            cat_response = requests.get(API_CATS_URL)
            if cat_response.status_code == 200:
                cat_link = cat_response.json()[0]['url']
                requests.get(f'{API_URL}{BOT_TOKEN}/sendPhoto?'
                             f'chat_id={chat_id}&photo={cat_link}')
            else:
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?'
                             f'chat_id={chat_id}&text={ERROR_TEXT}')

    time.sleep(1)
    counter += 1
