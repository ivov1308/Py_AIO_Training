import os

from environs import Env

env = Env()  # Создаем экземпляр класса Env
env.read_env('my_config.py')  # Считываем .env и извлекаем из него переменные в окружение

bot_token = env('BOT_TOKEN')
admin_id = env.int('ADMIN_ID')


print(bot_token)
print(admin_id)
print()
print(os.getenv('BOT_TOKEN'))
print(os.getenv('ADMIN_ID'))
