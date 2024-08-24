import logging

logger = logging.getLogger("my_logger")
logger.setLevel(logging.INFO)

handler = logging.FileHandler("custom.log")
handler.setLevel(logging.INFO)

formatter = logging.Formatter('[%(asctime)s] [%(filename)s:%(lineno)d] %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)

