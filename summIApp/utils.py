import os
import logging
from .utils_validations import *
from PIL import Image
from uuid import uuid4

logger = logging.getLogger("django")


def create_dirs(path):
    try:
        if not os.path.exists(path):
            os.makedirs(path)
        return True
    except Exception as e:
        logger.error(str(e))
        return False


def convert_to_png(tiff_file):
    try:
        # Open the tiff image using Image.open()
        img = Image.open(tiff_file)
        # Get the file name without extension
        file_name = os.path.splitext(tiff_file)[0]
        # Add '.png' to the file name
        temp_folder = str(uuid4())
        png_file = temp_folder + file_name + '.png'
        # Save the image as png using Image.save()
        img.save(png_file, format="png", lossless=True)
        return img
    except Exception as e:
        logger.error(str(e))
    return None