import logging


def generate_log():
    logging.basicConfig(
        filename='report.log',
        level=logging.INFO,
        format='%(asctime)s -%(levelname)s -%(message)s',
        datefmt='%Y-%m-%d %H:%M:%S %p'
    )
    return logging.getLogger()
