import logging
import pytest
import time
import requests


def check_response(url):

    response = requests.get(url)

    while response.status_code != 200:
        if response.status_code == 404:
            logging.warning("404, Image not found.")
            pytest.skip("Image not found")
        elif response.status_code in [403, 400]:
            return response
            # pytest.xfail("403, Access denied")
        elif response.status_code == 429 or response.status_code == 500:
            time.sleep(2)
        else:
            return response
        response = requests.get(url)
    assert response.ok
    return response
