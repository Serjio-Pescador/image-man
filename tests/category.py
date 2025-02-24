import random

import allure
import pytest
import os
import logging
from dotenv import load_dotenv
from utils.compare_picture import compare_screenshot
from utils.make_storage_picture import make_screenshot
from utils.receive_response import check_response
from static.test_uuid import Category


load_dotenv()
im_prod = os.getenv("IM_PROD")
im_pre = os.getenv("IM_PRE")


@allure.story('Формирование картинки для Категорий')
class TestCategory:
    @pytest.mark.parametrize("preset", Category.presets.value)
    @pytest.mark.parametrize("title", Category.titles.value)
    # @pytest.mark.parametrize("data_uuid", Category.category_uuid.value)
    @allure.title("Категории - {preset}")
    def test_category_preset(self, image_snapshot, preset, title):

        list_of_uuids = Category.category_uuid.value
        test_list = []
        for r in range(3):
            test_list.append(random.choice(list_of_uuids))

        # three_random_uuids = str(tuple(test_list))[1:-1]
        three_random_uuids = str(tuple(test_list)).replace("'", '').replace(" ", '')
        logging.info("Category uuid: %s", three_random_uuids)

        query_tail = f"title={title}&presetId={preset}&width=531&scale=2&quality=80&mediaType=webp"

        image_manager_url = f"{im_prod}{str(three_random_uuids)[1:-1]}?{query_tail}"
        logging.info("Image-Manager PROD url: %s", image_manager_url)

        pre_url = f"{im_pre}{str(three_random_uuids)[1:-1]}?{query_tail}"
        logging.info("Image-Manager PRE url: %s", pre_url)

        response_im = check_response(image_manager_url, timeout=15)
        if response_im.status_code == 400:
            pytest.fail(" -> Bad request to PROD <- ")

        name_screenshot = f"{preset}_{three_random_uuids.replace(',', '_')[1:-1:2]}"
        logging.info("Short name of screenshot: %s", name_screenshot)
        make_screenshot(response_im, img_uuid=name_screenshot)

        response_pre = check_response(pre_url, timeout=15)
        if response_pre.status_code == 400:
            pytest.fail(" -> Bad request to PRE <- ")

        compare_screenshot(response_pre, image_snapshot, img_uuid=name_screenshot, diff=0.3)
