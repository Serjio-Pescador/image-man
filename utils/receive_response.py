import logging
import logging.config
import pytest
import time
import requests


def check_response(url, timeout: int = None, **kwargs):

    try:
        response = requests.get(url, timeout=timeout, **kwargs)
        while response.status_code != 200:
            if response.status_code == 404:
                logging.warning("404, Image not found.")
                pytest.skip("Image not found")
            elif response.status_code in [403, 400]:
                logging.error("Error, %s", response.status_code)
                return response
                # pytest.xfail("403, Access denied")
            elif response.status_code in [429]:
                time.sleep(2)
            else:
                logging.error("Undefined status code, %s", response.status_code)
                logging.error("Headers: %s", response.headers)
                # return response
            response = requests.get(url, timeout=timeout, **kwargs)
        assert response.ok
        return response
    except Exception as e:
        logging.exception("%s", e)
        pytest.fail("Undefined error")
