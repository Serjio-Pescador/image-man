import allure
import pytest
import os
from dotenv import load_dotenv
from utils.compare_picture import compare_screenshot
from utils.make_storage_picture import make_screenshot
from utils.utils_func import maker_of_test_data, make_new_url_tail_rounded_width
from utils.receive_response import check_response
from static.test_uuid import ButtonsPresets
from utils.app_logger import get_logger
from utils.utils_func import compare_two_string
from utils.utils_func import make_url_tail_in_alphabet_lower


logger = get_logger(__name__)

load_dotenv()

host_url = os.getenv("HOST")
static_url = os.getenv("STATIC_URL")


@allure.story('Кнопки категорий с картинками')
@allure.label('owner', "s.rybak@okko.tv")
class TestButtonsCategory:
    @pytest.mark.parametrize("required_width", ButtonsPresets.widths.value)
    @pytest.mark.parametrize("preset", ButtonsPresets.presets.value)
    @pytest.mark.parametrize("data_uuid", ButtonsPresets.data_uuid.value)
    @allure.title("{button_uuid} - {required_width}")
    def test_sport_preset(self, image_snapshot, preset, data_uuid, required_width):
        logger.info("uuid: %s", data_uuid)

        if required_width < 350:
            scale_factor = 1
        else:
            scale_factor = 2

        query_tail = f"presetId={preset}&width={required_width}&scale={scale_factor}&quality=80&mediaType=webp"
        query_im, response_width = make_new_url_tail_rounded_width(query_tail)

        image_manager_url = make_url_tail_in_alphabet_lower(f"{host_url}{data_uuid}?{query_im}")
        logger.info("IM url: %s", image_manager_url)
        response_im = check_response(image_manager_url)

        name_file = f"uuid_{data_uuid}_{preset}_width_{required_width}"
        make_screenshot(response_im, img_uuid=name_file)

        stat_img_url = f"{static_url}{data_uuid}?{query_tail}"
        logger.info("static url: %s", stat_img_url)
        response_static = check_response(stat_img_url)

        compare_two_string(response_im.headers.get('etag'), response_static.headers.get('etag'), "ETAG")
        compare_screenshot(response_static, image_snapshot, img_uuid=name_file)

    if __name__ == "__main__":
        test_sport_preset()
