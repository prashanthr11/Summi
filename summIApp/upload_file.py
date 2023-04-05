import base64
from decouple import config
import requests
import logging
import traceback

imgbb_url = "https://api.imgbb.com/1/upload"
logger = logging.getLogger("django")


def imgbb_upload(file):
    try:
        encoded_string = base64.b64encode(file.read())

        # with open('tmp.txt', 'w') as f:
        #     f.write(str(encoded_string))
        print(encoded_string)
        # with open(file, "rb") as image_file:
        #     encoded_string = base64.b64encode(image_file.read())

        params = {
            "key": config("API_KEY")
        }

        api_response = requests.post(imgbb_url, params=params, data={
            "image": encoded_string
        })
        print(api_response.json())

        return api_response.json()
    except Exception as e:
        logger.error(traceback.format_exc())
        return {
            "status_code": 500,
            "error": {
                "message": str(e)
            }
        }
