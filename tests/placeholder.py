import allure
import pytest
import os
from dotenv import load_dotenv
from utils.compare_picture import compare_screenshot
from utils.make_storage_picture import make_screenshot
from utils.utils_func import maker_of_test_data
from utils.receive_response import check_response
from static.test_uuid import PlaceholderPresets
from utils.app_logger import get_logger, handler


logger = get_logger(__name__)
# logger.addHandler(handler)

load_dotenv()
im_prod = os.getenv("IM_PROD")
im_pre = os.getenv("IM_PRE")

data = maker_of_test_data(PlaceholderPresets)


@allure.story('Плейсхолдеры имен')
@allure.label('owner', "s.rybak@okko.tv")
class TestPlaceholders:

    @pytest.mark.parametrize("preset, name_uuid", data)
    @allure.title("{name_uuid} - {preset}")
    def test_placeholder_preset(self, image_snapshot, preset, name_uuid):

        logger.info("Name of person uuid: %s", name_uuid)
        query_tail = f"presetId={preset}&width=720"

        image_manager_prod_url = f"{im_prod}{name_uuid}?{query_tail}"
        logger.info("IM PROD url: %s", image_manager_prod_url)
        response_prod = check_response(image_manager_prod_url)

        image_manager_pre_url = f"{im_pre}{name_uuid}?{query_tail}"
        logger.info("IM PRE url: %s", image_manager_pre_url)
        response_pre = check_response(image_manager_pre_url)

        make_screenshot(response_prod, img_uuid=name_uuid)
        compare_screenshot(response_pre, image_snapshot, img_uuid=name_uuid, diff=0.1)

    if __name__ == "__main__":
        test_placeholder_preset()
