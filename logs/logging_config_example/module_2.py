import logging

logger = logging.getLogger(__name__)


def divide_number(dividend: int | float, divider: int | float):

    logger.debug('Лог DEBUG')
    logger.info('Лог INFO')
    logger.warning('Лог WARNING')
    logger.error('Лог ERROR')
    logger.critical('Лог CRITICAL')

    try:
        return dividend / divider
    except ZeroDivisionError:
        logger.exception('Произошло деление на 0')
