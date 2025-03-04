import allure
import pytest
import os
from dotenv import load_dotenv
from utils.compare_picture import compare_screenshot
from utils.make_storage_picture import make_screenshot
from utils.utils_func import maker_of_test_data, make_new_url_tail_rounded_width
from utils.receive_response import check_response
from static.test_uuid import PresetData, WidthSportReview
from utils.app_logger import get_logger
from utils.utils_func import compare_two_string


logger = get_logger(__name__)

load_dotenv()

host_url = os.getenv("HOST")
static_url = os.getenv("STATIC_URL")

presets = [3670, 3672, 3675]
widths = [253, 350, 531, 637, 700]
presets_for_test = []
for x in range(len(PresetData.preset_3360.value)):
    presets_for_test.append(presets[(x % 3)])
# print(presets_for_test)
uuids = PresetData.preset_3360.value


@allure.story('Новые обзоры и моменты')
class TestNewSportReview:
    @pytest.mark.parametrize("required_width", widths)
    @pytest.mark.parametrize("review_uuid, preset", list(zip(PresetData.preset_3360.value, presets_for_test)))
    @allure.title("{review_uuid}_{preset} - {required_width}")
    def test_new_sport_review(self, image_snapshot, preset, review_uuid, required_width):
        logger.info("uuid: %s", review_uuid)

        if required_width < 350:
            scale_factor = 1
        else:
            scale_factor = 2

        query_tail = f"presetId={preset}&width={required_width}&scale={scale_factor}&quality=80&mediaType=webp"
        query_alphabet = f"mediatype=webp&presetid={preset}&quality=80&scale={scale_factor}&width={required_width}"
        query_im, response_width = make_new_url_tail_rounded_width(query_alphabet)

        image_manager_url = f"{host_url}{review_uuid}?{query_im}"
        logger.info("IM url: %s", image_manager_url)
        response_im = check_response(image_manager_url)

        name_file = f"uuid_{review_uuid}_{preset}_width_{required_width}"
        make_screenshot(response_im, img_uuid=name_file, required_width=response_width)

        stat_img_url = f"{static_url}{review_uuid}?{query_tail}"
        logger.info("static url: %s", stat_img_url)
        response_static = check_response(stat_img_url)

        compare_two_string(response_im.headers.get('etag'), response_static.headers.get('etag'), "ETAG")
        compare_screenshot(response_static, image_snapshot, img_uuid=name_file, required_width=response_width)

    if __name__ == "__main__":
        test_new_sport_review()
