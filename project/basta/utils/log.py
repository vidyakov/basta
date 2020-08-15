from datetime import datetime

from termcolor import cprint


class Logger:
    def __init__(self, name: str = 'logs', path: str = '') -> None:
        self.name = name
        self.path = path

    @property
    def filename(self) -> str:
        return f'{self.path}/{self.name}.log'

    @staticmethod
    def _print_logs(logs: str) -> None:
        cprint(logs, 'red')

    def _write_logs_to_file(self, logs: str) -> None:
        with open(self.filename, 'a', encoding='utf-8') as file:
            file.write(f'{logs}\n')

    def debug(self, message: str) -> None:
        log_message = f'DEBUG\t{datetime.now()}\t{message}'
        self._print_logs(log_message)
        self._write_logs_to_file(log_message)

    def info(self, message: str) -> None:
        log_message = f'INFO\t{datetime.now()}\t{message}'
        self._print_logs(log_message)
        self._write_logs_to_file(log_message)

    def warning(self, message: str) -> None:
        log_message = f'WARNING\t{datetime.now()}\t{message}'
        self._print_logs(log_message)
        self._write_logs_to_file(log_message)

    def deco(self, mode):
        def decorator(func):
            def wrapper(*args, **kwargs):
                result = func(*args, **kwargs)
                logger_attr = getattr(self, mode)
                logger_attr(f'call: {func.__name__}, args: {args}, kwargs: {kwargs}, result: {result}')
                return result
            return wrapper
        return decorator
