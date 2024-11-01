import logging
import sys

# logging.basicConfig(
#     level=logging.DEBUG,
#     format='[{asctime}] #{levelname:8} {filename}:'
#            '{lineno} - {name} - {message}',
#     style='{'
# )


# Определяем виды форматирования
format_1 = '#%(levelname)-8s [%(asctime)s] - %(filename)s:'\
           '%(lineno)d - %(name)s - %(message)s'
format_2 = '[{asctime}] #{levelname:8} {filename}:'\
           '{lineno} - {name} - {message}'

# Инициализируем форматтеры
formatter_1 = logging.Formatter(fmt=format_1)
formatter_2 = logging.Formatter(fmt=format_2, style='{')

# Создаем логгер
logger = logging.getLogger(__name__)

# Инициализируем хэндлеры
stderr_handler = logging.StreamHandler()
stdout_handler = logging.StreamHandler(sys.stdout)
file_handler = logging.FileHandler('logs.log')

# Устанавливаем форматтеры для хэндлеров
stderr_handler.setFormatter(formatter_1)
stdout_handler.setFormatter(formatter_2)
file_handler.setFormatter(formatter_1)

# Добавляем хэндлеры логгеру
logger.addHandler(stdout_handler)
logger.addHandler(stderr_handler)
logger.addHandler(file_handler)

print(logger.handlers)

# Создаем лог
logger.warning('Это лог с предупреждением!')
