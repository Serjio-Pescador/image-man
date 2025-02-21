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
static_url = os.getenv("STATIC_URL")

def test_placeholder_preset(image_snapshot):
    # page.set_default_timeout(120000)
    # logging.info("uuid: %s", name_uuid)

    query_tail = f"?presetId=3312&width=505&scale=2&quality=80&mediaType=webp"
    query_tail_im = f"?presetId=3312&width=520&scale=2&quality=80&mediaType=webp"
    test_uuid = "a1c13b47-2f64-47a9-9cd0-6aa04f71ae31"

    image_manager_url = f"{host_url}{test_uuid}{query_tail_im}"
    # logging.info("static url: %s", image_manager_url)

    response = requests.get(image_manager_url)
    test_img = Image.open(BytesIO(response.content))
    with open("response_im.png", "wb") as f:
        f.write(response.content)
    assert response.ok

    stat_img_url = f"{static_url}{test_uuid}{query_tail}"
    stat_img = requests.get(stat_img_url).content

    name_static = "response_st.png"
    with open(name_static, "wb") as f:
        f.write(stat_img)

    img = Image.open("response_st.png")
    width, height = img.size
    print(width, height)
    assert width == 520

    image_snapshot(img, "response_im.png", 0.2)