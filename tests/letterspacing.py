import allure
import pytest
import os, requests
from dotenv import load_dotenv
import time
from playwright.sync_api import Page, expect
from utils import make_screenshot, compare_screenshot
from utils import maker_of_test_data, make_new_url_tail_rounded_width
from utils import check_response
from static.test_uuid import PresetData

load_dotenv()

host_url = os.getenv("HOST")
static_url = os.getenv("STATIC_URL")

data = maker_of_test_data(PresetData)


@allure.story('Обзоры спортивных событий')
class TestReviews:
    @allure.title('Спорт матчи пресеты 505 ширина')
    @pytest.mark.parametrize("preset, review_uuid",
                             data
                             )
    def test_width_505_preset(self, page: Page, image_snapshot, preset, review_uuid):
        page.set_default_timeout(150000)
        query_tail = f"presetId={preset}&width=505&scale=2&quality=80&mediaType=webp"
        querries_im = make_new_url_tail_rounded_width(query_tail)

        image_manager_url = f"{host_url}{review_uuid}?{querries_im}"
        stat_img_url = f"{static_url}{review_uuid}?{query_tail}"

        response = page.goto(image_manager_url)
        while check_response(response) != 200:
            response = page.goto(image_manager_url)
            assert response.ok

        make_screenshot(page, img_uuid=review_uuid)

        response = page.goto(stat_img_url)
        while check_response(response) != 200:
            response = page.goto(stat_img_url)
            assert response.ok

        compare_screenshot(page, image_snapshot, img_uuid=review_uuid)

    @allure.title('Спорт матчи пресеты 637 ширина')
    @pytest.mark.parametrize("preset, review_uuid",
                             data
                             )
    def test_width_637_preset(self, page: Page, image_snapshot, preset, review_uuid):
        page.set_default_timeout(150000)
        query_tail = f"presetId={preset}&width=637&scale=2&quality=80&mediaType=webp"
        querries_im = make_new_url_tail_rounded_width(query_tail)

        image_manager_url = f"{host_url}{review_uuid}?{querries_im}"
        stat_img_url = f"{static_url}{review_uuid}?{query_tail}"

        response = page.goto(image_manager_url)
        while check_response(response) != 200:
            response = page.goto(image_manager_url)
        assert response.ok

        make_screenshot(page, img_uuid=review_uuid)

        response = page.goto(stat_img_url)
        while check_response(response) != 200:
            response = page.goto(stat_img_url)
        assert response.ok

        compare_screenshot(page, image_snapshot, img_uuid=review_uuid)
