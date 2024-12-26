import os
import logging
from .utils_validations import *
from uuid import uuid4
from .constants import *
import traceback
from summI.settings import BASE_DIR
from .ocr_model.summi_ocr import recognize_text
from .ocr_api import recognize_text_api
import shutil

logger = logging.getLogger("django")


def create_dirs(path):
    """
    Create directories if they don't exist.
    
    Args:
        path (str): Path to create directory
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        if not os.path.exists(path):
            os.makedirs(path)
        return True
    except Exception as e:
        logger.error(traceback.format_exc())
        return False


def convert_to_png(uploaded_file, file_path):
    """
    Convert uploaded file to PNG format.
    
    Args:
        uploaded_file: Django uploaded file object
        file_path (str): Path to save the converted file
        
    Returns:
        str: Path to the converted PNG file, None if conversion fails
    """
    try:
        with Image.open(uploaded_file.file) as user_file:
            if create_dirs(file_path):
                new_file_name = "_".join(
                    uploaded_file.name.split(".")[:-1]) + ".png"
                file_path = os.path.join(file_path, new_file_name)
                user_file.save(file_path, format="png", lossless=True)
                return file_path
    except Exception as e:
        logger.error(traceback.format_exc())
    return None


def recognize_text_wrapper(file_path):
    """
    Wrapper function to handle text recognition from images.
    Uses either OCR API or local OCR model based on configuration.
    
    Args:
        file_path (str): Path to the image file
        
    Returns:
        str: Recognized text from the image
    """
    try:
        if USE_OCR_APIs:
            return recognize_text_api(file_path)
        else:
            return recognize_text(file_path)
    except Exception as e:
        logger.error(traceback.format_exc())
        return


def create_dir_in_temporary_media():
    """
    Create a temporary directory for storing media files.
    
    Returns:
        str: Path to the created temporary directory
    """
    try:
        temp_path = os.path.join(BASE_DIR, temporary_media, str(uuid4()))
        if not os.path.exists(temp_path):
            os.makedirs(temp_path)
        return temp_path
    except Exception as e:
        logger.error(traceback.format_exc())
        return ""


def remove_directory(file_path):
    """
    Remove a directory and its contents.
    
    Args:
        file_path (str): Path to the directory to remove
    """
    try:
        shutil.rmtree(file_path)
    except Exception as e:
        logger.error(traceback.format_exc())
