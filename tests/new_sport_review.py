import allure
import pytest
import os
from dotenv import load_dotenv
from utils.compare_picture import compare_screenshot
from utils.make_storage_picture import make_screenshot
from utils.utils_func import make_new_url_tail_rounded_width
from utils.receive_response import check_response
from static.test_uuid import PresetData
from utils.app_logger import get_logger
from utils.utils_func import compare_two_string, compare_two_digital
from utils.utils_func import make_url_tail_in_alphabet_lower


logger = get_logger(__name__)

load_dotenv()

host_url = os.getenv("HOST")
static_url = os.getenv("STATIC_URL")

presets = [3670, 3671, 3674, 3675]
widths = [253, 350, 531, 637, 700]
presets_for_test = []
for x in range(len(PresetData.preset_3360.value)):
    presets_for_test.append(presets[(x % 4)])
uuids = PresetData.preset_3360.value


@allure.story('Новые обзоры и моменты')
@allure.label('owner', "s.rybak@okko.tv")
class TestNewSportReview:
    @pytest.mark.parametrize("required_width", widths)
    @pytest.mark.parametrize("review_uuid, preset", list(zip(PresetData.preset_3360.value, presets_for_test)))
    @allure.title("{review_uuid}_{preset} - {required_width}")
    @allure.issue("DEV-149843")
    def test_new_sport_review(self, image_snapshot, preset, review_uuid, required_width):
        logger.info("uuid: %s", review_uuid)

        if required_width < 350:
            scale_factor = 1
        else:
            scale_factor = 2

        query_tail = f"presetId={preset}&width={required_width}&scale={scale_factor}&quality=80&mediaType=webp"
        query_im, response_width = make_new_url_tail_rounded_width(query_tail)

        image_manager_url = make_url_tail_in_alphabet_lower(f"{host_url}{review_uuid}?{query_im}")
        logger.info("IM url: %s", image_manager_url)
        response_im = check_response(image_manager_url)

        name_file = f"uuid_{review_uuid}_{preset}_width_{required_width}"
        img_width, img_height = make_screenshot(response_im, img_uuid=name_file)

        stat_img_url = f"{static_url}{review_uuid}?{query_tail}"
        logger.info("static url: %s", stat_img_url)
        response_static = check_response(stat_img_url)

        if required_width:
            compare_two_digital(response_width, img_width, "WIDTH")
        compare_two_string(response_im.headers.get('etag'), response_static.headers.get('etag'), "ETAG")
        compare_screenshot(response_static, image_snapshot, img_uuid=name_file, required_width=response_width)

    if __name__ == "__main__":
        test_new_sport_review()
