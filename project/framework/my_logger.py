import os
import sys
from datetime import datetime


class SingletonByName(type):

    def __init__(cls, name, bases, attrs, *args, **kwargs):
        super().__init__(name, bases, attrs, *args, **kwargs)
        cls.__instance = {}

    def __call__(cls, *args, **kwargs):
        name = ''
        if args:
            name = args[0]

        if kwargs:
            name = kwargs['name']

        try:
            return cls.__instance[name]
        except KeyError:
            cls.__instance[name] = super().__call__(*args, **kwargs)
            return cls.__instance[name]


class MyLogger(metaclass=SingletonByName):
    _default_log_path = f'{os.path.dirname(sys.argv[0])}/logs'

    def __init__(self, name):
        self.name = name
        if not os.path.exists(self._default_log_path):
            os.mkdir(self._default_log_path)

        self.path = f'{self._default_log_path}/{self.name}.log'

    def _get_log_string(self, postfix: str) -> str:
        return f'{datetime.now().strftime("%d.%m.%Y %H:%M:%S")}: {postfix}'

    def _save(self, path: str, log_string: str) -> None:
        with open(path, 'a', encoding='utf-8') as f_obj:
            f_obj.write(log_string)

    def log(self, message: str) -> None:
        log_string = self._get_log_string(f'LOG: {message}')
        print(log_string)
        self._save(self.path, log_string)

    def error(self, text: str) -> None:
        error_string = self._get_log_string(f'ERROR: {text}')
        print(error_string)
        self._save(self.path, error_string)
