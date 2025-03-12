import pytest
import time
import requests
from utils.app_logger import get_logger


logger = get_logger(__name__)


def check_response(url, timeout: int = None, **kwargs):
    try:
        response = requests.get(url, timeout=timeout, **kwargs)
        while response.status_code != 200:
            if response.status_code == 404:
                logger.warning("404, Image not found.")
                pytest.skip("Image not found")
            elif response.status_code in [403, 400]:
                logger.warning("Error, %s", response.status_code)
                return response
                # pytest.xfail("403, Access denied")
            elif response.status_code in [429]:
                time.sleep(2)
            else:
                logger.error("Undefined status code, %s", response.status_code)
                logger.error("Headers: %s", response.headers)
                # return response
            response = requests.get(url, timeout=timeout, **kwargs)
        assert response.ok
        e_tag = response.headers.get("etag")
        logger.info("Etag: %s", e_tag)
        return response
    except Exception as e:
        logger.exception("%s", e)
        pytest.fail("Undefined error")


if __name__ == "__main__":
    check_response(url=None)
