import requests
import logging


logger = logging.getLogger("django")


def imgbb_download_file(url, file_path):
    api_response = requests.get(url)

    if api_response.status_code == 200:
        with open(file_path, 'wb') as f:
            f.write(api_response.content)

        return True
    else:
        logger.info(api_response)

    return False
