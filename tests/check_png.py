import allure
import pytest
import os
import logging
import requests
from dotenv import load_dotenv
from utils import make_screenshot, compare_screenshot
from utils import maker_of_test_data
from utils import check_response
from static.test_uuid import PlaceholderPresets
from PIL import Image
from io import BytesIO

load_dotenv()

host_url = os.getenv("HOST")


def test_placeholder_preset():
    # page.set_default_timeout(120000)
    # logging.info("uuid: %s", name_uuid)

    query_tail = f"presetId=3312&width=720"

    image_manager_url = f"{host_url}f9985145-c6d7-4d83-a85a-7c9cda10907f?{query_tail}"
    logging.info("static url: %s", image_manager_url)

    response = requests.get(image_manager_url)
    test_img = Image.open(BytesIO(response.content))
    with open("response.png", "wb") as f:
        f.write(response.content)
    assert response.ok
