import logging


def log_details():
    logging.basicConfig(
        filename='report.log',
        level=logging.INFO,
        format='%(asctime)s -%(levelname)s -%(message)s',
        datefmt='%Y-%m-%d %H:%M:%S %p'
    )
    return logging.getLogger()


print(logging.__file__)

logger = log_details()
logger.info("This is a info message")
logger.debug("This is a debug message")
logger.warning("This is a warning message")
logger.error("This is a error message")
