import allure
import pytest
import os
from dotenv import load_dotenv
import logging
from playwright.sync_api import Page
from utils import make_screenshot, compare_screenshot
from utils import maker_of_test_data, make_new_url_tail_rounded_width
from utils import check_response
from static.test_uuid import PresetData

load_dotenv()

host_url = os.getenv("HOST")
static_url = os.getenv("STATIC_URL")

data = maker_of_test_data(PresetData)


# @allure.story('Обзоры спортивных событий')
class TestSportReviews:

    @allure.title('Спорт матчи пресеты')
    @allure.story('303 ширина')
    @pytest.mark.parametrize("preset, review_uuid",
                             data
                             )
    def test_width_303_preset(self, page: Page, image_snapshot, preset, review_uuid):
        page.set_default_timeout(120000)
        logging.info("uuid: %s", review_uuid)

        query_tail = f"presetId={preset}&width=303&scale=1&quality=80&mediaType=webp"
        querries_im = make_new_url_tail_rounded_width(query_tail)

        image_manager_url = f"{host_url}{review_uuid}?{querries_im}"
        stat_img_url = f"{static_url}{review_uuid}?{query_tail}"

        logging.info("static url: %s", stat_img_url)
        logging.info("IM url: %s", image_manager_url)

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

    @allure.title('Спорт матчи пресеты')
    @allure.story('350 ширина')
    @pytest.mark.parametrize("preset, review_uuid",
                             data
                             )
    def test_width_350_preset(self, page: Page, image_snapshot, preset, review_uuid):
        page.set_default_timeout(120000)
        logging.info("uuid: %s", review_uuid)

        query_tail = f"presetId={preset}&width=350&scale=1&quality=80&mediaType=webp"
        querries_im = make_new_url_tail_rounded_width(query_tail)

        image_manager_url = f"{host_url}{review_uuid}?{querries_im}"
        stat_img_url = f"{static_url}{review_uuid}?{query_tail}"

        logging.info("static url: %s", stat_img_url)
        logging.info("IM url: %s", image_manager_url)

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


    @allure.title('Спорт матчи пресеты')
    @allure.story('360 ширина')
    @pytest.mark.parametrize("preset, review_uuid",
                             data
                             )
    def test_width_360_preset(self, page: Page, image_snapshot, preset, review_uuid):
        page.set_default_timeout(120000)
        logging.info("uuid: %s", review_uuid)

        query_tail = f"presetId={preset}&width=360&scale=1&quality=80&mediaType=webp"
        querries_im = make_new_url_tail_rounded_width(query_tail)

        image_manager_url = f"{host_url}{review_uuid}?{querries_im}"
        stat_img_url = f"{static_url}{review_uuid}?{query_tail}"

        logging.info("static url: %s", stat_img_url)
        logging.info("IM url: %s", image_manager_url)

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

    @allure.title('Спорт матчи пресеты')
    @allure.story('505 ширина')
    @pytest.mark.parametrize("preset, review_uuid",
                             data
                             )
    def test_width_505_preset(self, page: Page, image_snapshot, preset, review_uuid):
        page.set_default_timeout(120000)
        logging.info("uuid: %s", review_uuid)

        query_tail = f"presetId={preset}&width=505&scale=2&quality=80&mediaType=webp"
        querries_im = make_new_url_tail_rounded_width(query_tail)

        image_manager_url = f"{host_url}{review_uuid}?{querries_im}"
        stat_img_url = f"{static_url}{review_uuid}?{query_tail}"

        logging.info("static url: %s", stat_img_url)
        logging.info("IM url: %s", image_manager_url)

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


    @allure.title('Спорт матчи пресеты')
    @allure.story('606 ширина')
    @pytest.mark.parametrize("preset, review_uuid",
                             data
                             )
    def test_width_606_preset(self, page: Page, image_snapshot, preset, review_uuid):
        page.set_default_timeout(120000)
        logging.info("uuid: %s", review_uuid)

        query_tail = f"presetId={preset}&width=606&scale=2&quality=80&mediaType=webp"
        querries_im = make_new_url_tail_rounded_width(query_tail)

        image_manager_url = f"{host_url}{review_uuid}?{querries_im}"
        stat_img_url = f"{static_url}{review_uuid}?{query_tail}"

        logging.info("static url: %s", stat_img_url)
        logging.info("IM url: %s", image_manager_url)

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


    @allure.title('Спорт матчи пресеты')
    @allure.story('637 ширина')
    @pytest.mark.parametrize("preset, review_uuid",
                             data
                             )
    def test_width_637_preset(self, page: Page, image_snapshot, preset, review_uuid):
        page.set_default_timeout(120000)
        logging.info("uuid: %s", review_uuid)

        query_tail = f"presetId={preset}&width=637&scale=2&quality=80&mediaType=webp"
        querries_im = make_new_url_tail_rounded_width(query_tail)

        image_manager_url = f"{host_url}{review_uuid}?{querries_im}"
        stat_img_url = f"{static_url}{review_uuid}?{query_tail}"

        logging.info("static url: %s", stat_img_url)
        logging.info("IM url: %s", image_manager_url)

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

    @allure.title('Спорт матчи пресеты')
    @allure.story('700 ширина')
    @pytest.mark.parametrize("preset, review_uuid",
                             data
                             )
    def test_width_700_preset(self, page: Page, image_snapshot, preset, review_uuid):
        page.set_default_timeout(120000)
        logging.info("uuid: %s", review_uuid)

        query_tail = f"presetId={preset}&width=700&scale=2&quality=80&mediaType=webp"
        querries_im = make_new_url_tail_rounded_width(query_tail)

        image_manager_url = f"{host_url}{review_uuid}?{querries_im}"
        stat_img_url = f"{static_url}{review_uuid}?{query_tail}"

        logging.info("static url: %s", stat_img_url)
        logging.info("IM url: %s", image_manager_url)

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


    @allure.title('Спорт матчи пресеты')
    @allure.story('720 ширина')
    @pytest.mark.parametrize("preset, review_uuid",
                             data
                             )
    def test_width_720_preset(self, page: Page, image_snapshot, preset, review_uuid):
        page.set_default_timeout(120000)
        logging.info("uuid: %s", review_uuid)

        query_tail = f"presetId={preset}&width=720&scale=2&quality=80&mediaType=webp"
        querries_im = make_new_url_tail_rounded_width(query_tail)

        image_manager_url = f"{host_url}{review_uuid}?{querries_im}"
        stat_img_url = f"{static_url}{review_uuid}?{query_tail}"

        logging.info("static url: %s", stat_img_url)
        logging.info("IM url: %s", image_manager_url)

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
