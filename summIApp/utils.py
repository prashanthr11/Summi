import os
import logging
from .utils_validations import *
from uuid import uuid4
from .constants import *
import traceback
from summI.settings import BASE_DIR

logger = logging.getLogger("django")


def create_dirs(path):
    try:
        if not os.path.exists(path):
            os.makedirs(path)
        return True
    except Exception as e:
        logger.error(traceback.format_exc())
        return False


def convert_to_png(image_obj):
    try:
        temporary_path = os.path.join(BASE_DIR, TEMP_DIR)
        if not os.path.exists(temporary_path):
            os.mkdir(temporary_path)

        file_path = os.path.join(temporary_path, str(uuid4()) + ".png")
        image_obj.save(file_path, format="png", lossless=True)
        return file_path
    except Exception as e:
        logger.error(traceback.format_exc())
    return None
