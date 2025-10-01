import logging


class Logger:

    @staticmethod
    def info(message):
        print(message)
        logging.info(message)

    @staticmethod
    def warning(message):
        print(message)
        logging.warning(message)

    @staticmethod
    def error(message):
        print(message)
        logging.error(message)