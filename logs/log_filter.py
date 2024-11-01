import logging


# Определяем свой фильтр, переопределяем метод filter,
# record будет ссылаться на объект класса LogRecord
class ErrorLogFilter(logging.Filter):
    def filter(self, record):
        return record.levelname == 'ERROR' and 'важно' in record.msg.lower()


class EvenLogFilter(logging.Filter):
    def filter(self, record):
        return not record.i % 2


# Инициализируем логгер
logger = logging.getLogger(__name__)

# Создаем хэндлер, который будет направлять логи в stderr
stderr_handler = logging.StreamHandler()

# Подключаем фильтр к хэндлеру
example: int = int(input('Номер фильтра(1/2): '))
if example == 1:
    stderr_handler.addFilter(ErrorLogFilter())
else:
    stderr_handler.addFilter(EvenLogFilter())

# Подключаем хэндлер к логгеру
logger.addHandler(stderr_handler)

# Вызываем логи
if example == 1:
    logger.error('Важно! Это лог с ошибкой!')
    logger.info('Важно! Это лог с info!')
    logger.warning('Важно! Это лог с предупреждением!')
    logger.error('Это лог с ошибкой!')
else:
    for i in range(1, 5):
        logger.warning('Важно! Это лог с предупреждением! '
                       '%d', i, extra={'i': i})
