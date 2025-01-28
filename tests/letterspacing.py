import allure
import pytest
import os, requests
from dotenv import load_dotenv
from PIL import Image
from io import BytesIO
import time
from playwright.sync_api import Page, expect
from urllib.parse import parse_qs
from static.test_uuid import PresetData

load_dotenv()

host_url = os.getenv("HOST")
static_url = os.getenv("STATIC_URL")


def maker_of_test_data():
    all_values = []
    all_keys = []
    for data in (PresetData):
        all_values += data.value
        all_keys += [int(data.name.split('_')[-1])] * len(data.value)
    return list(tuple(zip(all_keys, all_values)))


def make_new_url_tail_rounded_width(base_tail: str) -> str:
    query_params = parse_qs(base_tail)
    width = int(query_params['width'][0])
    if width % 20 != 0:
        new_width = width + 20 - (width % 20)
    eql_query_IM = query_params.copy()
    eql_query_IM['width'] = [str(new_width)]

    query_tail_im = ("&".join(f'{k}={v[0]}' for k, v in eql_query_IM.items()))
    return query_tail_im


def make_screenshot(self, img_uuid, **kwargs):
    test_name = os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split('[')[0]
    self.screenshot(path=f"./screenshots/{test_name}_{img_uuid}.png", **kwargs)
    return


def compare_screenshot(self, image_snapshot, img_uuid, timeout: float = 4000, diff: float = 0.7, **kwargs):
    test_name = os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split('[')[0]
    screenshot = Image.open(BytesIO(self.screenshot(timeout=timeout, **kwargs)))
    image_snapshot(screenshot, f"./screenshots/{test_name}_{img_uuid}.png", diff)
    return


data = maker_of_test_data()


@allure.story('Обзоры спортивных событий')
class TestReviews:
    @allure.title('Спорт матчи пресеты 505 ширина')
    @pytest.mark.parametrize("preset, review_uuid",
                             data
                             )
    def test_width_505_preset(self, page: Page, image_snapshot, preset, review_uuid):
        page.set_default_timeout(0)
        query_tail = f"presetId={preset}&width=505&scale=2&quality=80&mediaType=webp"
        querries_im = make_new_url_tail_rounded_width(query_tail)

        image_manager_url = f"{host_url}{review_uuid}?{querries_im}"
        stat_img_url = f"{static_url}{review_uuid}?{query_tail}"

        page.goto(image_manager_url)
        response = page.request.get(image_manager_url)

        if response.status == 404:
            pytest.skip("Image not found")
        elif response.status == 429 or response.status == 500:
            time.sleep(3)
            response = page.request.get(image_manager_url)
        else:
            page.goto(image_manager_url)
        expect(response).to_be_ok()

        make_screenshot(page, img_uuid=review_uuid)

        page.goto(stat_img_url)
        response = page.request.get(stat_img_url)
        while response.status == 429 or response.status == 500:
            time.sleep(2)
            page.goto(stat_img_url)
            response = page.request.get(stat_img_url)
        expect(response).to_be_ok()

        compare_screenshot(page, image_snapshot, img_uuid=review_uuid)

    @allure.title('Спорт матчи пресеты 637 ширина')
    @pytest.mark.parametrize("preset, review_uuid",
                             data
                             )
    def test_width_637_preset(self, page: Page, image_snapshot, preset, review_uuid):
        page.set_default_timeout(0)
        query_tail = f"presetId={preset}&width=637&scale=2&quality=80&mediaType=webp"
        querries_im = make_new_url_tail_rounded_width(query_tail)

        image_manager_url = f"{host_url}{review_uuid}?{querries_im}"
        stat_img_url = f"{static_url}{review_uuid}?{query_tail}"

        page.goto(image_manager_url)
        response = page.request.get(image_manager_url)
        # page.screenshot(path=f"./test/{Image.open(BytesIO(response.body()))}")

        if response.status == 404:
            pytest.skip("Image not found")
        elif response.status == 429 or response.status == 500:
            time.sleep(3)

            response = page.request.get(image_manager_url)
            page.goto(image_manager_url)
        expect(response).to_be_ok()

        make_screenshot(page, img_uuid=review_uuid)

        page.goto(stat_img_url)
        response = page.request.get(stat_img_url)
        while response.status == 429 or response.status == 500:
            time.sleep(3)
            page.goto(stat_img_url)
            response = page.request.get(stat_img_url)
        expect(response).to_be_ok()

        compare_screenshot(page, image_snapshot, img_uuid=review_uuid)
