import allure
import pytest
import os
from dotenv import load_dotenv
import logging
from utils.compare_picture import compare_screenshot
from utils.make_storage_picture import make_screenshot
from utils.utils import maker_of_test_data, make_new_url_tail_rounded_width
from utils.receive_response import check_response
from static.test_uuid import PresetData, WidthSportReview


load_dotenv()

host_url = os.getenv("HOST")
static_url = os.getenv("STATIC_URL")

data = maker_of_test_data(PresetData)


@allure.story('Спорт матчи и обзоры')
class TestSportReviews:
    @pytest.mark.parametrize("required_width", WidthSportReview.required_width.value)
    @allure.title("{review_uuid} - {required_width}")
    @pytest.mark.parametrize("preset, review_uuid",
                             data
                             )
    def test_sport_preset(self, image_snapshot, preset, review_uuid, required_width):
        logging.info("uuid: %s", review_uuid)

        if required_width < 350:
            scale_factor = 1
        else:
            scale_factor = 2

        query_tail = f"presetId={preset}&width={required_width}&scale={scale_factor}&quality=80&mediaType=webp"
        query_alphabet = f"mediatype=webp&presetid={preset}&quality=80&scale={scale_factor}&width={required_width}"
        query_im, response_width = make_new_url_tail_rounded_width(query_alphabet)

        image_manager_url = f"{host_url}{review_uuid}?{query_im}"
        logging.info("IM url: %s", image_manager_url)

        stat_img_url = f"{static_url}{review_uuid}?{query_tail}"
        logging.info("static url: %s", stat_img_url)

        response_im = check_response(image_manager_url)

        name_file = f"uuid_{review_uuid}_{preset}_width_{required_width}"
        make_screenshot(response_im, img_uuid=name_file)

        response_static = check_response(stat_img_url)

        compare_screenshot(response_static, image_snapshot, img_uuid=name_file, required_width=response_width)
