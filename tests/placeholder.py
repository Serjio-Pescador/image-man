import allure
import pytest
import os
import logging
from dotenv import load_dotenv
from utils.utils import compare_screenshot, make_screenshot
from utils.utils import maker_of_test_data
from utils.receive_ok_response import check_response
from static.test_uuid import PlaceholderPresets


load_dotenv()
host_url = os.getenv("HOST")
static_url = os.getenv("STATIC_URL")

data = maker_of_test_data(PlaceholderPresets)


@allure.story('Плейсхолдеры имен')
class TestPlaceholders:

    @pytest.mark.parametrize("preset, name_uuid", data)
    @allure.title("{name_uuid} - {preset}")
    def test_placeholder_preset(self, image_snapshot, preset, name_uuid):

        logging.info("Name of person uuid: %s", name_uuid)
        query_tail = f"presetId={preset}&width=720"

        image_manager_url = f"{host_url}{name_uuid}?{query_tail}"
        logging.info("Image-Manager url: %s", image_manager_url)

        stat_url = f"{static_url}{name_uuid}?{query_tail}"
        logging.info("Static url: %s", image_manager_url)

        response_im = check_response(image_manager_url)
        response_stat = check_response(stat_url)

        make_screenshot(response_im, img_uuid=name_uuid)
        compare_screenshot(response_stat, image_snapshot, img_uuid=name_uuid, diff=0.1)
