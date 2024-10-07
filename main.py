import json
import requests
import config
from pprint import pprint

api = config.API_URL
token = config.BOT_TOKEN


def write_update():
    with open('update_example.json', 'w') as file:
        update = requests.get(f'{api}{token}/getUpdates').json()
        json.dump(update, file, ensure_ascii=False, indent=4)


update = requests.get(f'{api}{token}/getUpdates').json()
pprint(update, indent=2)
