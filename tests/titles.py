import allure
import pytest
import os
from dotenv import load_dotenv
from utils.compare_picture import compare_screenshot
from utils.make_storage_picture import make_screenshot
from utils.receive_response import check_response
from static.test_uuid import TitlePresets
from utils.app_logger import get_logger


logger = get_logger(__name__)

load_dotenv()
im_prod = os.getenv("IM_PROD")
im_pre = os.getenv("IM_PRE")


@allure.story('Использование Title')
class TestTitles:
    @pytest.mark.parametrize("preset", TitlePresets.presets.value)
    @pytest.mark.parametrize("data_uuid", TitlePresets.title_uuid.value)
    @allure.title("{data_uuid} - {preset}")
    def test_use_title_in_query_preset(self, image_snapshot, preset, data_uuid):

        logger.info("Title uuid: %s", data_uuid)
        query_tail = f"presetid={preset}&width=637&title=Changed Title."

        image_manager_url = f"{im_prod}{data_uuid}?{query_tail}"
        logger.info("Image-Manager PROD url: %s", image_manager_url)
        response_im = check_response(image_manager_url)

        name_screenshot = f"{preset}_{data_uuid}"
        make_screenshot(response_im, img_uuid=name_screenshot)

        pre_url = f"{im_pre}{data_uuid}?{query_tail}"
        logger.info("Image-Manager PRE url: %s", pre_url)
        response_pre = check_response(pre_url)

        compare_screenshot(response_pre, image_snapshot, img_uuid=name_screenshot, diff=0.3)

    if __name__ == "__main__":
        test_use_title_in_query_preset()
