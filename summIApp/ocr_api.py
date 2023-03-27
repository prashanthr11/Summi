from google.cloud import vision
# from google.cloud.vision import types
import io
from PIL import Image, ImageDraw
from enum import Enum
import logging
import traceback


logger = logging.getLogger("django")


def recognize_text_api(file_path):
    try:

        client = vision.ImageAnnotatorClient()
        with io.open(file_path, 'rb') as image_file1:
            content = image_file1.read()

        content_image = vision.types.Image(content=content)
        response = client.document_text_detection(image=content_image)
        document = response.full_text_annotation
        print(response)
        print("---"*10 + "\n")
        print(response.full_text_annotation)
        return document

    except Exception as e:
        logger.error(traceback.format_exc())
        return ""
