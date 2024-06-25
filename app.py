# print("Om SaiRam")
import sys
from signLanguage.logger import logging
from signLanguage.exception import SignException


logging.info("Welcome to the Sign Language Detection")
try:
    a = 10 / 0
except Exception as e:
    raise SignException(e, sys) from e
