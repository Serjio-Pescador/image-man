import allure
import pytest
import os
from dotenv import load_dotenv
import logging
import requests
import PIL
# from playwright.sync_api import Page
from utils import make_screenshot, compare_screenshot
from utils import maker_of_test_data, make_new_url_tail_rounded_width
from utils import check_response
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
        # page.set_default_timeout(120000)
        logging.info("uuid: %s", review_uuid)

        if required_width < 350:
            scale_factor = 1
        else:
            scale_factor = 2
        query_tail = f"presetId={preset}&width={required_width}&scale={scale_factor}&quality=80&mediaType=webp"
        query_im, response_width = make_new_url_tail_rounded_width(query_tail)

        image_manager_url = f"{host_url}{review_uuid}?{query_im}"
        stat_img_url = f"{static_url}{review_uuid}?{query_tail}"

        logging.info("static url: %s", stat_img_url)
        logging.info("IM url: %s", image_manager_url)

        response = requests.get(image_manager_url)
        while check_response(response) != 200:
            response = requests.get(image_manager_url)
        assert response.ok

        name_file = f"uuid_{review_uuid}_{preset}_width_{required_width}"
        make_screenshot(response, img_uuid=name_file, required_width=response_width)

        response_static = requests.get(stat_img_url)
        while check_response(response_static) != 200:
            response_static = requests.get(stat_img_url)
        assert response_static.ok

        compare_screenshot(response_static.content, image_snapshot, img_uuid=name_file, required_width=response_width)
