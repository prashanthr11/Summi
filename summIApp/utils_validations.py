from PIL import Image
import logging
from pathvalidate import sanitize_filename


logger = logging.getLogger("django")
def validate_file(file):
    try:
        img = Image.open(file)
        print(img.format)

        return img.format.upper() in ["PNG", "JPG", "JPEG", "WEBP", "TIFF"]
    except Exception as e:
        logger.error(str(e))
        return False

def strip_html(name):
    sanitized_filename = ""
    try:
        sanitized_filename = sanitize_filename(name)
        return sanitized_filename
    except Exception as e:
        logger.error(str(e))
    return sanitized_filename
