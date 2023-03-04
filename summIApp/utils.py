import os
import logging
import imghdr
from .utils_validations import *
from .ocr_model.webptojpeg import convert_webp_to_png
from .ocr_model.tifftopng import convert_tiff_to_png

logger = logging.getLogger("django")
def create_dirs(path):
    try:
        if not os.path.exists(path):
            os.makedirs(path)
        return True
    except Exception as e:
        logger.error(str(e))
        return False

def sensor(path):
    image_type = imghdr.what(path)
  if  image_type == 'tiff':
    return convert_tiff_to_png(path)
  elif image_type == 'webp' :
        return convert_webp_to_png(path)
  else:
    return None
