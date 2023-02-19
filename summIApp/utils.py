import os
import logging
from .utils_validations import *


logger = logging.getLogger("django")
def create_dirs(path):
    try:
        if not os.path.exists(path):
            os.makedirs(path)
        return True
    except Exception as e:
        logger.error(str(e))
        return False
