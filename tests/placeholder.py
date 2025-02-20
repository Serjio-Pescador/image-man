import allure
import pytest
import os
import logging
from dotenv import load_dotenv
from utils import make_screenshot, compare_screenshot
from utils import maker_of_test_data
from utils import check_response
from static.test_uuid import PlaceholderPresets

load_dotenv()

host_url = os.getenv("HOST")

data = maker_of_test_data(PlaceholderPresets)

@allure.story('Плейсхолдеры имен')
class TestPlaceholders:

    @pytest.mark.parametrize("preset, name_uuid", data)
    @allure.title("{name_uuid} - {preset}")
    def test_placeholder_preset(self, page, image_snapshot, preset, name_uuid):
        page.set_default_timeout(120000)
        logging.info("uuid: %s", name_uuid)

        query_tail = f"presetId={preset}&width=720"

        image_manager_url = f"{host_url}{name_uuid}?{query_tail}"
        logging.info("static url: %s", image_manager_url)

        response = page.goto(image_manager_url)
        while check_response(response) != 200:
            response = page.goto(image_manager_url)
        assert response.ok

        # make_screenshot(page, img_uuid=review_uuid)
        compare_screenshot(page, image_snapshot, img_uuid=name_uuid, diff=0.05, src_path='./static/layouts/')