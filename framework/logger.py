import logging
import logging.handlers
import sys

from settings import BASE_DIR
from settings import LOGGER_CONFIG

sys.path.append('../')

# init formatter
normal_format = LOGGER_CONFIG['formatters']['normal']['format']
app_formatter = logging.Formatter(normal_format)

# init output streams
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(app_formatter)
stream_handler.setLevel(logging.DEBUG)
log_file = logging.handlers.RotatingFileHandler(
    BASE_DIR.joinpath('logs', 'server.log'),
    encoding='utf-8',
    maxBytes=1048576,
    backupCount=6,
)
log_file.setFormatter(app_formatter)
log_file.setLevel(logging.DEBUG)

LOGGER = logging.getLogger('server')
LOGGER.addHandler(stream_handler)
LOGGER.addHandler(log_file)
LOGGER.setLevel(logging.DEBUG)

if __name__ == '__main__':
    LOGGER.critical('Критическая ошибка')
    LOGGER.error('Ошибка')
    LOGGER.debug('Отладочная информация')
    LOGGER.info('Информационное сообщение')