import os
import datetime
from loguru import logger
from dotenv import load_dotenv

load_dotenv()

log_path = os.getenv("LOG_PATH")
if not os.path.exists(log_path):
    os.mkdir(log_path)

log_path = os.path.join(log_path, f'{datetime.datetime.now().strftime("%Y-%m-%d")}.log')

logger.add(log_path, rotation='50MB', encoding='utf-8', enqueue=True, compression='zip')
