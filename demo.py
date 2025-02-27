from us_visa.logger.logger import logging
from us_visa.exception.exception import CustomException
import sys

# logging.info('Custom Log')

try:
    a = 2/0
except Exception as e:
    raise CustomException(e,sys)

