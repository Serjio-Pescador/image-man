import allure
import pytest
import os
from dotenv import load_dotenv
import logging
from playwright.sync_api import Page
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
    # @allure.story("")
    @pytest.mark.parametrize("q_width", WidthSportReview.required_width.value)
    @allure.title("{review_uuid} - {q_width}")
    @pytest.mark.parametrize("preset, review_uuid",
                             data
                             )
    def test_sport_preset(self, page: Page, image_snapshot, preset, review_uuid, q_width):
        page.set_default_timeout(120000)
        logging.info("uuid: %s", review_uuid)

        query_tail = f"presetId={preset}&width={q_width}&scale=1&quality=80&mediaType=webp"
        querries_im = make_new_url_tail_rounded_width(query_tail)

        image_manager_url = f"{host_url}{review_uuid}?{querries_im}"
        stat_img_url = f"{static_url}{review_uuid}?{query_tail}"

        logging.info("static url: %s", stat_img_url)
        logging.info("IM url: %s", image_manager_url)

        response = page.goto(image_manager_url)
        while check_response(response) != 200:
            response = page.goto(image_manager_url)
        assert response.ok

        name_file = f"uuid_{review_uuid}_{preset}_width_{q_width}"
        make_screenshot(page, img_uuid=name_file)

        response = page.goto(stat_img_url)
        while check_response(response) != 200:
            response = page.goto(stat_img_url)
        assert response.ok

        compare_screenshot(page, image_snapshot, img_uuid=name_file)
